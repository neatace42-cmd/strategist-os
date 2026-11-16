# Connector log (credit-costing calls)
Owner rule: keep connector use modest; log every paid call.

| Date | Connector | Call | Purpose | Cost |
|---|---|---|---|---|
| 2026-11-16 | ScaleBot | `get_available_brands` (needed before the Reddit preflight) | Phase 1 VoC: check whether Reddit evidence collection is free | $0: failed, "SCALE Skool trial was cancelled". No Reddit run made |
| 2026-11-16 | WebSearch (built-in) | 1 standard search: Zepbound hair loss, women, protein, still shedding | Fresh public forum voice for Phase 1 VoC | No connector credits. It found no Reddit threads, only Mayo Clinic Connect and blog pages |
| 2026-11-16 | WebFetch (built-in) | Tried 2 fetches: a connect.mayoclinic.org thread and a reddit.com search | Read threads word for word so they could be quoted | $0: both blocked by this session's network. Nothing read, so nothing quoted |
| 2026-11-16 | Trendtrack | check_credits | Check balance before research (plan quota 10,000; 8,554 left at start) | 0 |
| 2026-11-16 | Trendtrack | search_ads (brand "Balmbare", active, longest running) | Balmbare active ads | 29 units |
| 2026-11-16 | Trendtrack | search_ads (brand "Nutrafol" + keyword "GLP-1") | Nutrafol GLP-1 ads. Keyword matched any brand, so it returned other GLP-1 advertisers, no Nutrafol | 30 units |
| 2026-11-16 | Trendtrack | search_ads (brand "MDhair", active, longest running) | MDhair active ads + transcripts | 30 units |
| 2026-11-16 | Trendtrack | search_ads (brand "Wellbel", active) | Wellbel active ads. 0 results | 0 |
| 2026-11-16 | Trendtrack | search_ads (brand "Nutrafol", women, active) | Retry for Nutrafol. 0 results | 0 |
| 2026-11-16 | Atria | search_library_ads ("GLP-1 hair", most_active) | Category scan. Wasted: sort by run length ignored the query, returned unrelated ads | counts toward monthly ad-search allowance; credits unknown |
| 2026-11-16 | Atria | search_library_ads ("Balmbare GLP-1 hair", best_match) | Balmbare + Nutrafol GLP-1 ads, other category ads | counts toward monthly ad-search allowance; credits unknown |
| 2026-11-16 | Atria | search_library_ads ("Wellbel GLP-1 hair", best_match) | Wellbel GLP-1 ads | counts toward monthly ad-search allowance; credits unknown |
| 2026-11-16 | Atria | get_library_ad_transcript (m2206121063267686) | Wellbel x Daniel Yadegar MD ad (most reused creative) | free (tool says no AI credits) |
| 2026-11-16 | Atria | get_library_ad_transcript (m1891069788739068) | Nutrafol GLP-1 UGC ad | free |
| 2026-11-16 | Atria | get_library_ad_transcript (m1126314253714399) | Bloom & Bond ad (pumpkin seed oil + saw palmetto, new rival) | free |
