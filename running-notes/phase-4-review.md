# Phase 4 review: the loop

**What was built**
- `tools/weekly_report.py`: reads a Dolphin/Meta ad-level CSV (column names matched loosely), computes CPA, ROAS,
  hook rate, hold rate, CTR, CPM, frequency; reads the angle/persona/format from the ad name; calls winners with
  CPA **and** ROAS (your north star) from `brand/targets.json`, or against the week's medians until you fill it;
  groups results by angle, persona and format with win rates; builds a watch list (fatigue, falling hook rate,
  rising CPA, spend without sales) and iteration candidates with a plain diagnosis. Tested on two weeks of
  **SAMPLE** data (`data/meta-exports/SAMPLE_*.csv`, clearly made up) → `reports/weekly/SAMPLE_2026-11-15.md`.
- Routines as Claude Code skills (`.claude/skills/`): `weekly-report`, `iterate-ad`, `competitor-watch`,
  `idea-hunt`, `angle-to-brief`, `log-test`.
- `playbook/hook-audit.md` (monthly), `idea-bank/_entry-template.md`, the testing log and open-loops flow.

**To make it real**
1. Fill `brand/targets.json` (CPA target, break-even ROAS). It stays in this private repo.
2. Name ads by `playbook/naming-convention.md` from now on.
3. Every Monday: export last week at ad level → `data/meta-exports/` → say "weekly report".

**Not built (yet):** the dashboard page and automatic scheduling (a Monday reminder can be added later).
