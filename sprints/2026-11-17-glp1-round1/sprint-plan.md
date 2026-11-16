---
generated_on: 2026-11-16
refresh_by: 2026-12-15   # write retro.md when every concept has meaningful spend
status: Proposed — owner approval pending
source: strategy/roadmap.md, idea-bank/evaluation-2026-11-16.md, playbook/method.md §6, playbook/naming-convention.md
---
# Sprint plan: GLP-1 round 1 (from 2026-11-17)

## 1. Round size, and why
- **Method rule** (`playbook/method.md` §6): count the truly new concepts that go live per week now, plan about double,
  limited by budget.
- **We can't count that yet: there is no real account data** (`data/meta-exports/` holds only SAMPLE files, clearly made
  up). Data-limited.
- **Proposal: 6 concepts**, each with 2–4 variations, **19 ads in total** (17 variations across the 6 concepts + 2 static
  companions; table below). Why 6: it covers the 3 priorities with enough concepts to compare
  (P1 3 · P2 2 · P6 1), uses all five live Studio formats plus UGC once (format is the "loudest" variable, metrics.md),
  and is a manageable first load for the Studio queue. (*Inferred*)
- **Budget:** to judge a concept, each needs about **2× the target CPA** of spend (or 7 days), per
  `.claude/skills/log-test`. So round 1 needs at least **6 × 2 × target CPA**. The target CPA is owner-held, so I can't
  put a dollar figure here. Suggested setup (*Inferred*): one ad set per concept, so every concept actually gets spend
  and the results can be compared.
- **Testing mix:** no winners exist, so 0 iterations. 5 core new concepts + 1 wild slot (concept 6). See
  `strategy/roadmap.md` → Testing mix.

## 2. Concepts (creative tracker)
Awareness: U = unaware · P = problem-aware · S = solution-aware · Pr = product-aware.

| # | Concept | Angle ID | Persona | Awareness | Doorway | Leading emotion | Studio format | Variations (2–4) | Static companion | Evidence band | Sensitive-topic flag | Ad name |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "I did the protein": agree, then add | A01 (+ I-6, A12 hook) | P1 | S | switch + awakening | frustration → understood | ugc (fallback: one-character drama) | 3: H1 hair tie / kitchen · H2 product line-up / bathroom · H3 "no lectures" / car, 30 s | **Y** `GLP1_A01_P1_STAT_H1_v1` | HIGH | AI person telling a first-person pain story (disclosed); mechanism wording | `GLP1_A01_P1_UGC_H1_v1` |
| 2 | Your hair's bodyguard went home early | A22 (+ I-10 format, I-3 hook) | P1 | P | awakening | confusion → "now I get it" | adrama | 3: H1 clip slips · H2 hair tie · H3 cold open on the bodyguard (alt first-dialogue clips) | N | MEDIUM | mechanism shown as cartoon; no "after" hair | `GLP1_A22_P1_ANIM_H1_v1` |
| 3 | The honest version: just the label | A29 (+ A23, A04) | P1 | S → Pr | switch | skepticism → trust | native | 3 images: H1 label + sticky note · H2 hair tie + jar · H3 "what was I missing?" list; primary text V3 adds the honest disqualifier (A27) | n/a (is an image) | MEDIUM | implied comparison with hype ads (no names) | `GLP1_A29_P1_NAT_H1_v1` |
| 4 | "Isn't vanity", with a reason | A03 (+ I-3 hook) | P2 | P | awakening | guilt → permission | drama | 3: H1 clip into the sink · H2 hair tie · H3 "Is it vain to miss my hair?"; 60 s cutdown | **Y** `GLP1_A03_P2_STAT_H1_v1` | MEDIUM | weight-loss context without body cues | `GLP1_A03_P2_DRAMA_H1_v1` |
| 5 | It eased off, then the dose went up | A21 (+ I-4) | P2 (overlay: dose increase) | P | awakening | dread → control | static | 3: H1 calendar + brush · H2 hair tie on wrist · H3 illustrated steps | n/a (is a static) | MEDIUM | the word "dose" (no "you", no mg) | `GLP1_A21_P2_STAT_H1_v1` |
| 6 | Don't wait and hope (song) — wild slot | A30 (I-2) | P6 | U | awakening | quiet worry → agency | song | 2 first-clip visual variations: H1 fridge plan · H2 brush on the vanity | N | LOW | implied prevention ("start early"); no "prevents" | `GLP1_A30_P6_SONG_H1_v1` |

Variation ad names follow the convention: the hook number changes (`..._H2_v1`, `..._H3_v1`), the rest stays.
Briefs: `sprints/2026-11-17-glp1-round1/briefs/<ad name>.md`.

**Checks against the owner's asks:** spread P1 3 / P2 2 / P6 1 (roadmap weights) · 5 of 6 are differentiated core
angles (A01, A22, A29, A03 led by "isn't vanity", A21) · static/native: concepts 3 and 5 plus 2 companions · UGC:
concept 1 · 4 of 6 aimed at unaware/problem-aware.

## 3. What stays fixed across the round (so results compare)
- Every concept uses the same hedged mechanism wording ("body fat makes some of our estrogen... that shield can drop...
  one reason") and agrees that weight loss and protein matter.
- Same proof stack: doses on the label, two softgels, "about three months", 90-day money-back guarantee.
- Same end line in primary text: "Check with your doctor about your routine."
- No testimonials, no numbers beyond the label and the guarantee.

## 4. Order of production (fastest first, *Inferred*)
1. Concepts 3 and 5 (native, static) and the 2 static companions: image jobs, quickest to review.
2. Concept 1 (UGC, or drama fallback) and concept 4 (drama).
3. Concepts 2 and 6 (animation, song): longest jobs.

## 5. Before anything goes live (owner)
- Landing page for GLP-1 traffic (advertorial or PDP)? The mechanism needs a page that continues the story.
- Approve AI-people disclosure (`strategy/creator-input.md` §3) and drug-word risk ("dose", "the shot", "GLP-1").
- Fill `brand/targets.json` so "meaningful spend" and "winner" can be judged.

## Open questions
1. Is 6 concepts / 19 ads the right load for the Studio and the budget? (owner)
2. Does every concept get its own ad set? (owner / media buyer)
3. If UGC isn't live, accept the one-character drama fallback for concept 1? (owner)
