---
name: log-test
description: "Opens, updates and closes tests in the testing log, and turns open questions into hypotheses and results. Use when the owner says log a test, close the test, what did we learn, or this ad went live."
---

# Log a test

- **Open** (ad goes live): a row in `testing/testing-log.md`: ID (T-YYYYMMDD-n), start date, ad name(s), short
  hypothesis, metric + benchmark, status "running".
- **Close** (enough spend, usually 2× target CPA or 7 days): result with exact numbers from `reports/weekly/`,
  status validated / invalidated / inconclusive / not enough data, the learning in one plain sentence, a re-check
  date. The long version goes to `testing/results/<ID>.md`.
- **Learnings travel:** a validated or invalidated result updates `strategy/roadmap.md` (priorities or roads not
  taken) and the idea's entry in `idea-bank/`.
- **Open questions** from any doc go to `testing/open-loops/`, scored 1–5 on stakes, confidence, researchability and
  novelty (17+ out of 20 = test soon). Promote the best to `testing/hypotheses/` with a test plan.
