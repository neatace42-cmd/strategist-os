#!/usr/bin/env python3
"""Weekly performance report for the NutraEssence Strategy Brain (no installs needed: Python 3 standard library).

Usage (from the repo folder):
    python3 tools/weekly_report.py data/meta-exports/2026-11-09_to_2026-11-15.csv
    python3 tools/weekly_report.py THIS_WEEK.csv --prev LAST_WEEK.csv
    python3 tools/weekly_report.py                      # newest CSV in data/meta-exports (prev = the one before)

What it does
  1. Reads an ad-level export from Dolphin or Meta Ads Manager (column names are matched loosely).
  2. Works out per-ad metrics: CPA, ROAS, hook rate, hold rate, CTR, CPM, frequency.
  3. Reads each ad name (playbook/naming-convention.md) to find its angle, persona, format, hook and version.
  4. Calls winners with brand/targets.json (CPA and ROAS together, the owner's north star). With no targets it uses
     the account's own medians ("relative mode") and says so.
  5. Groups results by angle, persona and format (spend, CPA, ROAS, win rate), lists top ads, a watch list,
     iteration candidates with a diagnosis (playbook/metrics.md), and writes reports/weekly/<end-date>.md + .json.
Claude then adds the human read: what it means, 3 iterations and 1 new angle (see .claude/skills/weekly-report).
"""
import csv, json, os, re, sys, statistics, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# loose header matching: our field -> possible export headers (lower-case, punctuation removed)
ALIASES = {
    'ad_name': ['ad name', 'ad_name', 'name', 'ad'],
    'spend': ['amount spent', 'amount spent usd', 'spend', 'cost', 'amount spent (usd)'],
    'impressions': ['impressions', 'impr'],
    'reach': ['reach'],
    'video_3s_views': ['3second video plays', '3 second video plays', 'video plays at 3 seconds', 'video_3s_views', '3s views', 'video plays 3s'],
    'thruplays': ['thruplays', 'thruplay', 'thru plays', 'video thruplay'],
    'link_clicks': ['outbound clicks', 'link clicks', 'link_clicks', 'clicks all', 'clicks'],
    'purchases': ['purchases', 'results', 'website purchases', 'purchase'],
    'revenue': ['purchases conversion value', 'purchase conversion value', 'website purchases conversion value', 'revenue', 'conversion value'],
}
NAME_RE = re.compile(r'^(?P<segment>[A-Z0-9]+)_(?P<angle>A\d{2,3})_(?P<persona>P\d{1,2})_(?P<format>[A-Z]+)_(?P<hook>H\d{1,2})_(?P<version>v\d{1,3})', re.I)


def norm(h):
    return re.sub(r'[^a-z0-9 ]', '', h.lower().replace('-', ' ')).strip()


def num(v):
    if v is None:
        return 0.0
    v = str(v).replace(',', '').replace('$', '').replace('%', '').strip()
    try:
        return float(v) if v not in ('', '-', '—') else 0.0
    except ValueError:
        return 0.0


def read_export(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return [], {}
    headers = {norm(h): h for h in rows[0].keys()}
    found = {}
    for field, names in ALIASES.items():
        for n in names:
            if norm(n) in headers:
                found[field] = headers[norm(n)]
                break
    ads = {}
    for r in rows:
        name = (r.get(found.get('ad_name', ''), '') or '').strip()
        if not name or name.lower().startswith('total'):
            continue
        a = ads.setdefault(name, {k: 0.0 for k in ALIASES if k != 'ad_name'})
        for k in a:
            if k in found:
                a[k] += num(r.get(found[k]))
    return [dict(ad_name=n, **v) for n, v in ads.items()], found


def metrics(a):
    d = lambda x, y: (x / y) if y else None
    a['cpa'] = d(a['spend'], a['purchases'])
    a['roas'] = d(a['revenue'], a['spend'])
    video = a['video_3s_views'] > 0  # statics have no video plays: hook/hold don't apply
    a['hook_rate'] = d(a['video_3s_views'], a['impressions']) if video else None
    a['hold_rate'] = d(a['thruplays'], a['video_3s_views']) if video else None
    a['ctr'] = d(a['link_clicks'], a['impressions'])
    a['cpm'] = d(a['spend'] * 1000, a['impressions'])
    a['frequency'] = d(a['impressions'], a['reach'])
    a['cvr'] = d(a['purchases'], a['link_clicks'])
    m = NAME_RE.match(a['ad_name'])
    a.update({k: (m.group(k).upper() if k != 'version' else m.group(k).lower()) for k in ('segment', 'angle', 'persona', 'format', 'hook', 'version')} if m
             else {'segment': None, 'angle': None, 'persona': None, 'format': None, 'hook': None, 'version': None})
    return a


def load_targets():
    p = os.path.join(ROOT, 'brand', 'targets.json')
    try:
        t = json.load(open(p))
    except Exception:
        t = {}
    return t


def judge(ads, t):
    """Winner = CPA at/below target AND ROAS at/above break-even, at meaningful spend (owner's north star)."""
    spend_total = sum(a['spend'] for a in ads) or 1
    min_spend = t.get('min_spend_to_judge') or max(50.0, 0.02 * spend_total)
    cpa_t, roas_t = t.get('cpa_target'), t.get('roas_breakeven')
    mode = 'targets'
    judged = [a for a in ads if a['spend'] >= min_spend]
    if cpa_t is None or roas_t is None:
        mode = 'relative'
        cpas = [a['cpa'] for a in judged if a['cpa']]
        roass = [a['roas'] for a in judged if a['roas'] is not None]
        cpa_t = cpa_t if cpa_t is not None else (statistics.median(cpas) if cpas else None)
        roas_t = roas_t if roas_t is not None else (statistics.median(roass) if roass else None)
    for a in ads:
        if a['spend'] < min_spend:
            a['verdict'] = 'too early'
        elif a['purchases'] == 0:
            a['verdict'] = 'loser'
        else:
            ok_cpa = cpa_t is not None and a['cpa'] is not None and a['cpa'] <= cpa_t
            ok_roas = roas_t is not None and a['roas'] is not None and a['roas'] >= roas_t
            a['verdict'] = 'winner' if ok_cpa and ok_roas else ('close' if ok_cpa or ok_roas else 'loser')
    return {'mode': mode, 'cpa_line': cpa_t, 'roas_line': roas_t, 'min_spend': round(min_spend, 2)}


def diagnose(a, b):
    """Plain-English read of the weakest link (playbook/metrics.md). b = benchmarks."""
    out = []
    if a['hook_rate'] is not None and a['hook_rate'] < b['hook_rate']:
        out.append('low hook rate: test a new first 1-3 s (visual, sound, first line)')
    elif a['hold_rate'] is not None and a['hold_rate'] < b['hold_rate']:
        out.append('good hook, weak hold: tighten pacing, show the problem sooner, re-hook at 3-5 s')
    if a['ctr'] is not None and a['ctr'] < b['ctr']:
        if a['cvr'] and a['cvr'] >= b['cvr']:
            out.append('low CTR but buyers convert: fix hook/headline/visual, protect the body')
        else:
            out.append('low CTR: strengthen the CTA or offer at the end')
    elif a['cvr'] is not None and a['cvr'] < b['cvr']:
        out.append('clicks but few buyers: check the ad and landing page say the same thing; check the offer')
    if a['frequency'] and a['frequency'] > b['frequency']:
        out.append(f"frequency {a['frequency']:.2f}: fatigue risk, plan a new creator/format/angle version")
    return out or ['no obvious weak link this week']


def group(ads, key):
    g = {}
    for a in ads:
        k = a.get(key) or 'unmapped'
        x = g.setdefault(k, {'ads': 0, 'spend': 0.0, 'purchases': 0.0, 'revenue': 0.0, 'winners': 0, 'judged': 0})
        x['ads'] += 1; x['spend'] += a['spend']; x['purchases'] += a['purchases']; x['revenue'] += a['revenue']
        if a['verdict'] != 'too early':
            x['judged'] += 1
            x['winners'] += a['verdict'] == 'winner'
    for x in g.values():
        x['cpa'] = x['spend'] / x['purchases'] if x['purchases'] else None
        x['roas'] = x['revenue'] / x['spend'] if x['spend'] else None
        x['win_rate'] = x['winners'] / x['judged'] if x['judged'] else None
    return dict(sorted(g.items(), key=lambda kv: -kv[1]['spend']))


def f_money(v): return '—' if v is None else f'${v:,.2f}'
def f_pct(v): return '—' if v is None else f'{v * 100:.2f}%'
def f_x(v): return '—' if v is None else f'{v:.2f}'


def dates_from(path):
    m = re.findall(r'(\d{4}-\d{2}-\d{2})', os.path.basename(path))
    return (m[0], m[-1]) if m else (None, datetime.date.today().isoformat())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv', nargs='?')
    ap.add_argument('--prev')
    ap.add_argument('--out')
    args = ap.parse_args()
    exp_dir = os.path.join(ROOT, 'data', 'meta-exports')
    files = sorted(f for f in os.listdir(exp_dir) if f.endswith('.csv') and not f.startswith('_'))
    cur = args.csv or (os.path.join(exp_dir, files[-1]) if files else None)
    if not cur:
        sys.exit('No CSV found. Put an export in data/meta-exports/ (see data/README.md).')
    prev = args.prev
    if not prev and not args.csv and len(files) > 1:
        prev = os.path.join(exp_dir, files[-2])

    t = load_targets()
    b = {'hook_rate': 0.30, 'hold_rate': 0.12, 'ctr': 0.01, 'frequency': 1.75, 'cvr': 0.02}
    b.update(t.get('benchmarks', {}))
    ads, found = read_export(cur)
    if not ads:
        sys.exit('The CSV has no ad rows.')
    ads = [metrics(a) for a in ads]
    rule = judge(ads, t)
    prev_ads = {}
    if prev:
        p_ads, _ = read_export(prev)
        prev_ads = {a['ad_name']: metrics(a) for a in p_ads}

    tot = {k: sum(a[k] for a in ads) for k in ('spend', 'impressions', 'video_3s_views', 'thruplays', 'link_clicks', 'purchases', 'revenue')}
    tot = metrics(dict(ad_name='TOTAL', reach=0, **tot))
    ptot = None
    if prev_ads:
        pt = {k: sum(a[k] for a in prev_ads.values()) for k in ('spend', 'impressions', 'video_3s_views', 'thruplays', 'link_clicks', 'purchases', 'revenue')}
        ptot = metrics(dict(ad_name='PREV', reach=0, **pt))

    start, end = dates_from(cur)
    sample = os.path.basename(cur).upper().startswith('SAMPLE')
    unmapped = [a['ad_name'] for a in ads if not a['angle']]
    judged = [a for a in ads if a['verdict'] != 'too early']
    winners = [a for a in ads if a['verdict'] == 'winner']
    top = sorted(ads, key=lambda a: -a['spend'])[:5]

    watch = []
    for a in ads:
        p = prev_ads.get(a['ad_name'])
        why = []
        if a['frequency'] and a['frequency'] > b['frequency']:
            why.append(f"frequency {a['frequency']:.2f}")
        if p and p['hook_rate'] and a['hook_rate'] is not None and a['hook_rate'] < p['hook_rate'] * 0.85:
            why.append(f"hook rate down {f_pct(p['hook_rate'])} → {f_pct(a['hook_rate'])}")
        if p and p['cpa'] and a['cpa'] and a['cpa'] > p['cpa'] * 1.2:
            why.append(f"CPA up {f_money(p['cpa'])} → {f_money(a['cpa'])}")
        if a['spend'] >= rule['min_spend'] and a['purchases'] == 0:
            why.append(f"spent {f_money(a['spend'])} with no purchases")
        if why:
            watch.append((a, why))
    # iteration candidates: winners/close ads with meaningful spend, biggest spend first; never a loser
    cands = sorted([a for a in ads if a['verdict'] in ('winner', 'close')], key=lambda a: -a['spend'])[:5]

    L = []
    L.append(f"---\ngenerated_on: {datetime.date.today().isoformat()}\nperiod: {start or '?'} to {end}\nsource_file: {os.path.relpath(cur, ROOT)}\n"
             f"previous_file: {os.path.relpath(prev, ROOT) if prev else 'none'}\n---")
    L.append(f"# Weekly report: {start or '?'} to {end}")
    if sample:
        L.append("\n> ⚠️ **SAMPLE DATA.** These numbers are made up to show how the report works. Drop a real export in `data/meta-exports/`.")
    L.append("\n## 1. The week in numbers")
    rows = [('Spend', 'spend', f_money), ('Purchases', 'purchases', lambda v: f'{v:,.0f}'), ('CPA', 'cpa', f_money), ('ROAS', 'roas', f_x),
            ('Hook rate', 'hook_rate', f_pct), ('Hold rate', 'hold_rate', f_pct), ('CTR', 'ctr', f_pct), ('CPM', 'cpm', f_money)]
    L.append('| Metric | This week | Last week |\n|---|---|---|')
    for lab, k, f in rows:
        L.append(f"| {lab} | {f(tot[k])} | {f(ptot[k]) if ptot else '—'} |")
    L.append(f"\n**Winner rule** ({rule['mode']} mode): CPA ≤ {f_money(rule['cpa_line'])} **and** ROAS ≥ {f_x(rule['roas_line'])}, judged only on ads with "
             f"≥ {f_money(rule['min_spend'])} spend." + (" Targets are not set, so the lines are this week's medians (fill `brand/targets.json`)." if rule['mode'] == 'relative' else ''))
    L.append(f"**Win rate:** {len(winners)} of {len(judged)} judged ads ({f_pct(len(winners) / len(judged)) if judged else '—'}); {len(ads) - len(judged)} too early to judge.")

    L.append("\n## 2. Top ads by spend")
    L.append('| Ad | Verdict | Spend | CPA | ROAS | Hook | Hold | CTR |\n|---|---|---|---|---|---|---|---|')
    for a in top:
        L.append(f"| `{a['ad_name']}` | {a['verdict']} | {f_money(a['spend'])} | {f_money(a['cpa'])} | {f_x(a['roas'])} | {f_pct(a['hook_rate'])} | {f_pct(a['hold_rate'])} | {f_pct(a['ctr'])} |")

    for title, key, names in (("3. By angle", 'angle', None), ("4. By persona", 'persona', None), ("5. By format", 'format', None)):
        g = group(ads, key)
        L.append(f"\n## {title}")
        L.append('| ' + key.capitalize() + ' | Ads | Spend | CPA | ROAS | Win rate |\n|---|---|---|---|---|---|')
        for k, x in g.items():
            L.append(f"| {k} | {x['ads']} | {f_money(x['spend'])} | {f_money(x['cpa'])} | {f_x(x['roas'])} | "
                     f"{(str(x['winners']) + '/' + str(x['judged'])) if x['judged'] else '—'} |")

    L.append("\n## 6. Watch list")
    if watch:
        for a, why in watch:
            L.append(f"- `{a['ad_name']}`: {'; '.join(why)}")
    else:
        L.append('- Nothing flagged.' + ('' if prev_ads else ' (No previous week to compare with, so trend checks were skipped.)'))

    L.append("\n## 7. Iteration candidates (never iterate on a loser)")
    if cands:
        for a in cands:
            L.append(f"- `{a['ad_name']}` ({a['verdict']}, {f_money(a['spend'])}): " + '; '.join(diagnose(a, b)))
    else:
        L.append('- None this week: no ad met the winner or close line at meaningful spend.')

    if unmapped:
        L.append("\n## Ads that don't follow the naming rule\nThese can't be matched to an angle (see `playbook/naming-convention.md`):")
        L += [f"- `{n}`" for n in unmapped]
    L.append("\n## 8. Claude's read (filled in by the weekly-report routine)\n- What it means:\n- 3 iterations:\n- 1 new angle to test:\n- Did last week's plan happen?\n")
    L.append(f"_Columns found in the export: {', '.join(sorted(found))}. Missing ones show as —._")

    out = args.out or os.path.join(ROOT, 'reports', 'weekly', f"{'SAMPLE_' if sample else ''}{end}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write('\n'.join(L) + '\n')
    json.dump({'period': [start, end], 'sample': sample, 'rule': rule, 'totals': tot, 'previous_totals': ptot,
               'ads': ads, 'by_angle': group(ads, 'angle'), 'by_persona': group(ads, 'persona'), 'by_format': group(ads, 'format')},
              open(out[:-3] + '.json', 'w'), indent=1, default=str)
    print('Report written:', os.path.relpath(out, ROOT))


if __name__ == '__main__':
    main()
