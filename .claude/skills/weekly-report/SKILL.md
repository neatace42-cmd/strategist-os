---
name: weekly-report
description: "Monday performance report: runs tools/weekly_report.py on the newest Dolphin/Meta CSV, then adds the human read (what it means, 3 iterations, 1 new angle) and updates the testing log. Use when the owner says weekly report, Monday report, how did the ads do, or drops a new export."
---

# Weekly report (every Monday)

1. Check `data/meta-exports/` for the newest export (format: `data/README.md`). If none, say so and stop.
2. Run `python3 tools/weekly_report.py` (it picks the newest file, and the one before as last week). It writes
   `reports/weekly/<end-date>.md` and `.json`.
3. Read the report, `playbook/metrics.md`, `strategy/roadmap.md` and `testing/testing-log.md`. Fill section 8:
   - **What it means** (3–5 plain lines; spend × ROAS is the truth; label Inferred vs Verified).
   - **3 iterations**: only on winners/close ads from section 7; one variable each; say which variable and why
     (use the diagnosis). Name the new ad (`playbook/naming-convention.md`, version +1).
   - **1 new angle** from the latest `idea-bank/evaluation-*.md` (highest-ranked untested idea that fits the roadmap).
   - **Did last week's plan happen?** Compare with last week's section 8.
4. Testing log: close tests whose ads now have enough spend (result + learning; validated / invalidated /
   inconclusive / not enough data); open rows for new ads.
5. If ads don't follow the naming rule, list them and ask the owner to rename (or map them by hand in the report).
6. Add a line to `running-notes/routine-log.md`. Never invent numbers; exact figures only.
