# Parker Brain: catalog of what was saved

Source: https://github.com/real-simple-labs/parker-brain (branch `main`, commit `938ddeb7e0cb1489a89049a93deb7be14b1c1579`), downloaded 2026-11-05.
Full copy: [parker-brain/](parker-brain/) with 559 files, each hash-verified against the download.

Licence: PolyForm Noncommercial 1.0.0, see [LICENSE.md](parker-brain/LICENSE.md). Commercial use needs a separate written licence from the copyright holder.

## Skills

| Skill | Files | What it does |
|---|---|---|
| [ad-account-analysis](parker-brain/.claude/skills/ad-account-analysis/SKILL.md) | 8 | Analyze Meta ad account data — read what's spending, what's converting, what's fatiguing, and where the audience is being reached. Use when the user wants an account audit, a single-ad diagnosis, a placement read, a demographic breakdown, or a fatigue check. |
| [ai-ad-generation](parker-brain/.claude/skills/ai-ad-generation/SKILL.md) | 10 | Generate AI ad assets — Veo 3 video prompts and AI image static prompts — with brand context, compliance, and forensic direction. The output is prompt text the user pastes into the AI tool, not the final asset. |
| [brand-idea-bank-maintenance](parker-brain/.claude/skills/brand-idea-bank-maintenance/SKILL.md) | 1 | Maintain a brand-specific idea bank from context docs, research, Parker data, user conversations, manual ideas-tab saves, expert signals, competitor ads, organic videos, and internal Parker observations. |
| [dream](parker-brain/.claude/skills/dream/SKILL.md) | 1 | Run the dreaming system on demand for a brand and the person using it. Read the day of comms — the conversations the user had with Parker, plus any connected comms — against everything Parker has accumulated, and come back with proposals across six buckets: context updates, skill improvements, schedules to create, new ideas to research, new open loops, and the person (what Parker now understands about them and what to tee up for them). Framed as the morning suggestion. Use when Jimmy runs /dream or asks Parker what it has been thinking about, what it would suggest, or to dream on a brand. |
| [evaluate-ideas](parker-brain/.claude/skills/evaluate-ideas/SKILL.md) | 1 | Rank the brand idea bank against the approved Phase-2 strategic roadmap. Grades the whole captured pile — which priority each idea serves, the lever it pulls, how strong the evidence is, whether it trips a roads-not-taken kill — and produces a ranked shortlist by priority that ends in a plain ranked call the sprint plan sizes into a round, plus a read of what the bank is starving for. The skeptical pass. Run after harvest-ideas (weekly), when the bank grows enough to change the rank, or when the roadmap is re-approved. |
| [expert-signal-intake](parker-brain/.claude/skills/expert-signal-intake/SKILL.md) | 1 | Turn a knowledge source Jimmy hands Parker — an expert video, transcript, tweet, post, newsletter, podcast, article, or report — into an exact, verbatim proposal of what Parker would change, for Jimmy to approve, modify, or deny before anything is written. Use when Jimmy drops a source and wants Parker to learn from it. |
| [harvest-ideas](parker-brain/.claude/skills/harvest-ideas/SKILL.md) | 1 | Weekly agentic idea hunt for the brand. Assembles a hunt brief (roadmap, personas, live account read, tried-and-failed, user signals), runs a cold brainstorm before any feed opens, then fans out hunter lenses — customer language, organic/format with a trend lane, old-ads corpus, far-transfer wildcard — and captures each find verbatim with its spark into idea-bank/entries with full provenance and a viewable reference link. This is the capture half of Phase 3; grading is the separate evaluate-ideas skill. Use weekly as a scheduled routine, or when asked to find, harvest, or hunt ideas for the brand. |
| [headlines](parker-brain/.claude/skills/headlines/SKILL.md) | 25 | Write headlines for ads — static, video text overlays, paid social, landing page hero. Picks the right structural pattern for the brand type (lifestyle vs problem/solution), the awareness stage, and the customer language available. |
| [hooks](parker-brain/.claude/skills/hooks/SKILL.md) | 21 | Write hooks for a specific ad — the first three seconds that earn the click and the watch. Uses the proven hook formats from the canonical taxonomy, picks the right one for the brand and audience, and produces hooks built around a specific ICP and emotion. |
| [improve-system](parker-brain/.claude/skills/improve-system/SKILL.md) | 1 | Apply the self-improvement system on demand. Read the accumulated reasoning traces and update this brand's and this user's living context to reflect what Parker has learned. Use when Jimmy runs /improve-system or asks Parker to apply what it has learned, fold the traces in, or get this brand's context up to date with recent feedback. |
| [iterations](parker-brain/.claude/skills/iterations/SKILL.md) | 13 | The full iteration flow in one skill — choose which ads to iterate on, then make the iterations. If the user names a specific ad, go straight to making iterations; if they ask account-level (which ads should we iterate on, what to iterate this month), select the ads first, then make iterations on each. |
| [open-loops-advance](parker-brain/.claude/skills/open-loops-advance/SKILL.md) | 5 | Turn a promoted open loop into a hypothesis — a falsifiable prediction plus the few complementary pulls that together settle it, triangulated across the ad account, reviews, and competitors as the question needs and runnable with Parker's tools. Use when advancing a Tier-1 (or activated Tier-2) loop from the open-loops roll-up into the testing queue, or when the user says advance the open loops, form a hypothesis, or plan how to test a loop. |
| [open-loops-validate](parker-brain/.claude/skills/open-loops-validate/SKILL.md) | 6 | Run a hypothesis's test plan, gather the evidence, and honestly resolve the loop into one of the four validation states — validated, invalidated, inconclusive, or insufficient evidence. Use when a hypothesis is approved or proceeding and it is time to test it, or when the user says validate this, run the test, close the loop, or what did the research find. |
| [propagate-craft](parker-brain/.claude/skills/propagate-craft/SKILL.md) | 1 | Push-based re-ship of the factory methodology bundle into brand brains that carry the method as copied files — the legacy vendored-parker-system layout and decoupled brains that asked for a refresh. Brains on the standard layout (parker-system as a pinned submodule) do NOT use this; they update by moving the pin via their own /update-brain routine, and migrations/v1.md converts a legacy brain to that layout. Use for a factory-initiated sweep of the remaining copy-based brains. |
| [recreate](parker-brain/.claude/skills/recreate/SKILL.md) | 1 | Faithfully recreate one ad for the brand - a competitor ad, an inspiration ad, a swipe-file save, a TikTok, or one of the brand's own ads. First decides whether the ad is a video or a static image, then runs exactly one method - adapting scripts for video, static ad recreation for an image - never both. Output is a near 1:1 recreation in the brand's voice and customer language, not new concepts or variations. Use when someone says "recreate this," "/recreate," "make this for our brand," "can we do something like this," "adapt this ad," or hits Recreate in the Parker app. For new variations of the brand's own winners, use iterations instead. |
| [refresh-context](parker-brain/.claude/skills/refresh-context/SKILL.md) | 1 | Keep the brand brain from going stale. Reads running-notes/refresh-schedule.md and each standing doc's refresh_by frontmatter, surfaces what is overdue or due soon, walks the Phase 1→2→3 dependency spine to catch docs made stale by upstream changes even when their own date is fine, and re-runs the generating prompt for each — carrying the prior version forward and re-stamping the dates. Use weekly as a scheduled routine, or whenever asked to refresh, re-run, or check the freshness of the brand brain or any context doc. |
| [scriptwriting](parker-brain/.claude/skills/scriptwriting/SKILL.md) | 29 | Write ad scripts that sound spoken, not written, by adapting proven reference ads into the brand's own voice fingerprint. AI cannot write good scripts cold — references are the default input and the brand script-voice profile is the sound. Every script passes the spoken-script-voice AI-tells check and read-aloud test. Net-new from scratch is the rare fallback. |
| [self-improve](parker-brain/.claude/skills/self-improve/SKILL.md) | 1 | Parker's self-improvement governance for the brand — the disposing half of the living layer. Weekly it curates captured reasoning traces and decides which dreaming proposals get promoted, human in the loop — including the doc-alignment proposals the research cycle files. It is the gate: dreaming and research propose, self-improvement disposes. The loop pipeline itself (roll-up, hypotheses, validations, re-validations) runs in /research-loops. Use weekly as a scheduled routine, or when asked to curate learnings, promote proposals, or self-improve. |
| [self-improvement-intake](parker-brain/.claude/skills/self-improvement-intake/SKILL.md) | 1 | Capture reasoning traces from user feedback, approvals, rejections, reroutes, expert learnings, and strategic decisions so Parker improves over time. |
| [set-up-brain](parker-brain/.claude/skills/set-up-brain/SKILL.md) | 1 | The front door to building a brand's brain. Run this when standing up a new brand — it needs the Parker MCP connected for data, and the brand's synced folder from the Parker Desktop app (which creates the brand's repo and usually opens this very session inside it). It welcomes the person, works inside the folder Parker Desktop keeps in sync, connects and tests the data, asks the short brand intake (the things Parker genuinely can't observe), runs the full build in dependency order, confirms everything synced, and hands off to get-started. Follows prompts/onboarding-runner.md as the detailed method. Use when someone says set up a brand, build the brain, onboard a new brand, or get started building. Also the right entry when the brand's brain already exists — it detects a built brain and retrieves it, handing off to get-started instead of rebuilding — and when the brain was only scaffolded (set up with the method and empty running notes, not built), which it builds without redoing the setup. |
| [setup-routines](parker-brain/.claude/skills/setup-routines/SKILL.md) | 1 | Arms the brand brain's standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill registers the schedules, which are per-account and can't be committed. The onboarding build runs it automatically at the stamp step (build mode, no questions); run it yourself after cloning the brain into a new Claude Code cloud instance, or any time to change a cadence or turn a routine off. |
| [update-parker-skill](parker-brain/.claude/skills/update-parker-skill/SKILL.md) | 4 | Make a correct update to Parker's prompts, system docs, rubrics, knowledge docs, training corpus, or brand outputs — and propagate the change everywhere it needs to land. Use this skill whenever you are changing any part of the Parker context-engineering system, including tightening a rule, adding a principle, propagating a pattern, adding or modifying a prompt, adding a knowledge doc, or evolving a skill. The skill exists because Parker's docs are highly cross-referenced and inheritance-driven, and updates that look local often have non-obvious downstream impact. |
| [weekly-creative-report](parker-brain/.claude/skills/weekly-creative-report/SKILL.md) | 4 | Build the brand's weekly creative report, a polished, shareable page an agency can send straight to the brand's CMO and team. Leads with the brand's own north-star metric, shows this week against last week and the last 8 weeks, puts the top creatives on the page with thumbnails and why they work (every ad links to the actual ad), flags what's tiring or wasting spend, and ends with next week's plan. An agency can report on just the ads it launched or the whole account. Outputs one HTML file in the Parker V2 look (and a PDF when Chrome is on the machine). The first run asks a few short setup questions, pre-filled from the brand brain, and every later run reuses the answers. Use when someone says "weekly report," "weekly creative report," "make the client report," "report for the CMO," "how did last week go, in a deck I can send," or "/weekly-creative-report. |

## Brand-brain routine skills (templates)

These live in `templates/brand-routines/claude/skills/` and get copied into each brand brain.

| Skill | What it does |
|---|---|
| [disconnect-factory](parker-brain/templates/brand-routines/claude/skills/disconnect-factory/SKILL.md) | Decouple this brain from the public parker-brain factory so the team can develop their own version of the method. Converts the read-only parker-system/ submodule into plain files the team owns and can edit, removes the read-only guardrails, and flips the update posture so /update-brain stops offering pin bumps. Use when the team says they want to customize the method itself, own their prompts and craft docs, disconnect from Parker's updates, or go independent. |
| [dream](parker-brain/templates/brand-routines/claude/skills/dream/SKILL.md) | Parker's dreaming run for the brand and the person using it — the planning half of the living layer. Reads the day's comms (the conversations the user had with Parker first, then any connected comms) against the vault and returns proposals across six buckets — context updates, skill improvements, schedules to create, new ideas to research, new open loops, and the person (what Parker now understands about them and what to tee up for them) — into dreaming/proposals/pending. Captures verbatim; proposes, never applies; promotion runs through self-improve with the human in the loop. Use daily as a scheduled routine, or when asked to "dream", brainstorm overnight, or "what were you thinking about". |
| [evaluate-ideas](parker-brain/templates/brand-routines/claude/skills/evaluate-ideas/SKILL.md) | Rank the brand idea bank against the approved Phase-2 strategic roadmap. Grades the whole captured pile — which priority each idea serves, the lever it pulls, how strong the evidence is, whether it trips a roads-not-taken kill — and produces a ranked shortlist by priority that ends in a plain ranked call the sprint plan sizes into a round, plus a read of what the bank is starving for. The skeptical pass. Run after harvest-ideas (weekly), when the bank grows enough to change the rank, or when the roadmap is re-approved. |
| [get-started](parker-brain/templates/brand-routines/claude/skills/get-started/SKILL.md) | The first-run walkthrough for a brand brain — the orientation a new owner or a teammate who just got the brain through Parker Desktop needs so they aren't left in decision paralysis. It first reads how familiar the person is with this kind of system and calibrates to them, then covers, in plain language and paced one thing at a time, what the brain is, what was built, how the files work, how they grow it, what Parker can actually pull and do, what skills are, how to connect their other tools, what the brain does on its own, what to automate now, how to bring teammates in, and where to start. Run on a fresh brain, when someone is new to it, or whenever asked to walk me through this / what is this / where do I start / give me the tour / I'm new here. |
| [harvest-ideas](parker-brain/templates/brand-routines/claude/skills/harvest-ideas/SKILL.md) | Weekly agentic idea hunt for the brand. Assembles a hunt brief (roadmap, personas, live account read, tried-and-failed, user signals), runs a cold brainstorm before any feed opens, then fans out hunter lenses — customer language, organic/format with a trend lane, old-ads corpus, far-transfer wildcard — and captures each find verbatim with its spark into idea-bank/entries with full provenance and a viewable reference link. This is the capture half of Phase 3; grading is the separate evaluate-ideas skill. Use weekly as a scheduled routine, or when asked to find, harvest, or hunt ideas for the brand. |
| [refresh-context](parker-brain/templates/brand-routines/claude/skills/refresh-context/SKILL.md) | Keep the brand brain from going stale. Reads running-notes/refresh-schedule.md and each standing doc's refresh_by frontmatter, surfaces what is overdue or due soon, walks the Phase 1→2→3 dependency spine to catch docs made stale by upstream changes even when their own date is fine, and re-runs the generating prompt for each — carrying the prior version forward and re-stamping the dates. Use weekly as a scheduled routine, or whenever asked to refresh, re-run, or check the freshness of the brand brain or any context doc. |
| [research-loops](parker-brain/templates/brand-routines/claude/skills/research-loops/SKILL.md) | The weekly research cycle — runs the open-loops pipeline end to end so the brand's strategic questions actually get answered instead of piling up. Rolls up and grades the open loops, advances the promoted ones into hypotheses, runs the validations in the testing queue, runs due re-validations, reports what was learned, and then aligns the standing docs with the confirmed findings so the brain never says the old thing after the research says otherwise. Use weekly as a scheduled routine, or when asked to run the research, advance the loops, work the testing queue, or "what have we learned". |
| [save-brain](parker-brain/templates/brand-routines/claude/skills/save-brain/SKILL.md) | How this brain saves and syncs itself — the required knowledge for anything save, sync, backup, clone, or share-shaped in a Parker Brain, and for any impulse to run git here. The short of it - on a person's computer, files written to disk are the whole job, the Parker Desktop app syncs the folder both ways, and the agent never runs git against this repo; in a cloud run (a scheduled routine or a hosted sandbox, no Parker Desktop) the agent gets the brain through the Parker MCP and saves it with git itself. Covers finding the brain folder, what to do when the app has paused the folder on a clash (files holding both versions between <<<<<<< and >>>>>>> marks), cloud runs, what to do when the app isn't installed, and the rare self-managed exception. Use whenever saving work, syncing, backing up, combining a clash, running on a schedule, or fixing something that looks like a sync problem. |
| [self-improve](parker-brain/templates/brand-routines/claude/skills/self-improve/SKILL.md) | Parker's self-improvement governance for the brand — the disposing half of the living layer. Weekly it curates captured reasoning traces and decides which dreaming proposals get promoted, human in the loop — including the doc-alignment proposals the research cycle files. It is the gate: dreaming and research propose, self-improvement disposes. The loop pipeline itself (roll-up, hypotheses, validations, re-validations) runs in /research-loops. Use weekly as a scheduled routine, or when asked to curate learnings, promote proposals, or self-improve. |
| [setup-routines](parker-brain/templates/brand-routines/claude/skills/setup-routines/SKILL.md) | Arms the brand brain's standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill registers the schedules, which are per-account and can't be committed. The onboarding build runs it automatically at the stamp step (build mode, no questions); run it yourself after cloning the brain into a new Claude Code cloud instance, or any time to change a cadence or turn a routine off. |
| [update-brain](parker-brain/templates/brand-routines/claude/skills/update-brain/SKILL.md) | The weekly check that keeps this brain current with the parker-brain standard — without overriding anything the team chose. Compares the pinned parker-system/ release against the newest factory tag and, on the standard layout, installs it on its own when every migration on the way is safe to run unattended; the migrations run in order and a script re-syncs the copied skills deterministically. A migration that needs a person, a decoupled brain, or a team that turned automatic updates off gets one short question instead. What the team modified stays theirs; what they declined stays declined. Use weekly as a scheduled routine, or when asked to update the brain, check for updates, sync with the standard, or "what's new in Parker". |

## Review agents

| Agent | What it does |
|---|---|
| [context-grounding-review](parker-brain/.claude/agents/context-grounding-review.md) | Independent grounding review for creative and strategy output, run as a peer strategist, not a citation checker. Spawned by the creative skills on a finished draft, before the voice review. First reads the method docs the task routes to — fully, the same reads the generator owed — then runs the deterministic grounding-check, then reviews the draft through the methods' own reasoning. Verifies three things: the right context was loaded and pulled, nothing was fabricated, and the methods were applied correctly, not just cited. Returns grounded or bounced, with missing loads, missing pulls, and misapplications named and doc-cited. |
| [creative-voice-review](parker-brain/.claude/agents/creative-voice-review.md) | Independent voice review for creative deliverables — scripts, headlines, hooks, overlay and static copy, ad-prompt spoken lines, iteration copy. Spawned by the creative skills on a finished draft before it ships. Runs the mechanical voice-lint, judges the flags against the brand's voice profile, catches what regex can't, and returns per-line verdicts with rewrites in the brand's register. Never restructures strategy. |

## Creative strategy knowledge

| Document | Title | KB |
|---|---|---|
| [ad-account-analysis.md](parker-brain/creative-strategy-context/ad-account-analysis.md) | Analyzing Ad Account Data | 39 |
| [adapting-scripts.md](parker-brain/creative-strategy-context/adapting-scripts.md) | Adapting Scripts | 33 |
| [ad-formats/both/index.md](parker-brain/creative-strategy-context/ad-formats/both/index.md) | Cross-modality ad formats | 6 |
| [ad-formats/README.md](parker-brain/creative-strategy-context/ad-formats/README.md) | Ad formats context | 4 |
| [ad-formats/static/index.md](parker-brain/creative-strategy-context/ad-formats/static/index.md) | Static ad formats | 4 |
| [ad-formats/video/index.md](parker-brain/creative-strategy-context/ad-formats/video/index.md) | Video ad formats | 7 |
| [ad-metrics-glossary.md](parker-brain/creative-strategy-context/ad-metrics-glossary.md) | Ad Metrics Glossary | 22 |
| [advertising-luxury-and-higher-price-points.md](parker-brain/creative-strategy-context/advertising-luxury-and-higher-price-points.md) | Advertising luxury and higher price points | 12 |
| [advertising-to-older-audiences.md](parker-brain/creative-strategy-context/advertising-to-older-audiences.md) | Advertising to older audiences | 12 |
| [ai-animation-prompting.md](parker-brain/creative-strategy-context/ai-animation-prompting.md) | AI Animation Prompting | 2 |
| [ai-static-ad-generation.md](parker-brain/creative-strategy-context/ai-static-ad-generation.md) | AI Image Ad Prompt Generation Context Document | 53 |
| [ai-writing-tells.md](parker-brain/creative-strategy-context/ai-writing-tells.md) | AI Writing Tells | 13 |
| [algospeak.md](parker-brain/creative-strategy-context/algospeak.md) | Algospeak | 15 |
| [analyzing-public-ad-accounts.md](parker-brain/creative-strategy-context/analyzing-public-ad-accounts.md) | Analyzing public ad accounts | 24 |
| [andromeda-v2.md](parker-brain/creative-strategy-context/andromeda-v2.md) | Meta Creative Diversity: The 2026 Playbook (Andromeda v2) | 41 |
| [creative-consumption-analysis.md](parker-brain/creative-strategy-context/creative-consumption-analysis.md) | Creative Consumption Analysis | 5 |
| [creative-strategy-by-brand-size.md](parker-brain/creative-strategy-context/creative-strategy-by-brand-size.md) | Creative strategy by brand size | 7 |
| [creative-strategy-fundamentals.md](parker-brain/creative-strategy-context/creative-strategy-fundamentals.md) | Creative strategy fundamentals | 15 |
| [creator-briefs.md](parker-brain/creative-strategy-context/creator-briefs.md) | Creator briefs | 9 |
| [customer-review-mining-method.md](parker-brain/creative-strategy-context/customer-review-mining-method.md) | Customer review mining — method | 23 |
| [emotional-delivery-and-timing.md](parker-brain/creative-strategy-context/emotional-delivery-and-timing.md) | Emotional Delivery and Timing — the layer beneath hooks | 8 |
| [expert-insights/context-update-candidates/2026-06-03-claude-creative-strategy-os-reasoning-traces.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/2026-06-03-claude-creative-strategy-os-reasoning-traces.md) | Context update candidates - Claude creative strategy OS and reasoning traces | 6 |
| [expert-insights/context-update-candidates/2026-06-03-creative-forecasting-volume-hit-rate-churn.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/2026-06-03-creative-forecasting-volume-hit-rate-churn.md) | Context update candidates - Creative forecasting volume, hit rate, churn, and half-life | 6 |
| [expert-insights/context-update-candidates/2026-06-03-meta-2026-creative-scaling-persona-remix.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/2026-06-03-meta-2026-creative-scaling-persona-remix.md) | Context update candidates - Meta 2026 creative scaling and persona remixing | 7 |
| [expert-insights/context-update-candidates/2026-06-18-12-combination-ad-iteration-system.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/2026-06-18-12-combination-ad-iteration-system.md) | Context update candidates — The 12-combination ad-iteration system (Sarah) | 7 |
| [expert-insights/context-update-candidates/2026-06-18-organic-content-playbook-2026.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/2026-06-18-organic-content-playbook-2026.md) | Context update candidates — Organic content playbook 2026 (Tonic Health / Sunny) | 8 |
| [expert-insights/context-update-candidates/README.md](parker-brain/creative-strategy-context/expert-insights/context-update-candidates/README.md) | Review queue — proposals pending Jimmy's approval | 11 |
| [expert-insights/curation/README.md](parker-brain/creative-strategy-context/expert-insights/curation/README.md) | Expert Insights Curation | 1 |
| [expert-insights/inbox/2026-06-03-claude-creative-strategy-os-reasoning-traces.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-03-claude-creative-strategy-os-reasoning-traces.md) | Expert signal - Claude creative strategy OS and reasoning traces | 14 |
| [expert-insights/inbox/2026-06-03-creative-forecasting-volume-hit-rate-churn.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-03-creative-forecasting-volume-hit-rate-churn.md) | Expert signal - Creative forecasting as inventory planning | 13 |
| [expert-insights/inbox/2026-06-03-meta-2026-creative-scaling-persona-remix.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-03-meta-2026-creative-scaling-persona-remix.md) | Expert signal - Meta 2026 creative scaling, persona remixing, and context engineering | 17 |
| [expert-insights/inbox/2026-06-18-12-combination-ad-iteration-system.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-18-12-combination-ad-iteration-system.md) | Expert signal — The 12-combination ad-iteration system (Sarah) | 18 |
| [expert-insights/inbox/2026-06-18-dara-denney-nine-converting-hooks.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-18-dara-denney-nine-converting-hooks.md) | Expert signal — Dara Denney's nine "converting" Meta hooks (anti-bloat verdict) | 6 |
| [expert-insights/inbox/2026-06-18-hijacking-visual-tension-organic-2-second-hooks.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-18-hijacking-visual-tension-organic-2-second-hooks.md) | Expert signal — Hijacking visual tension from organic content for two-second hooks (Sarah / School community call) | 17 |
| [expert-insights/inbox/2026-06-18-neurologically-sound-hooks-first-second.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-18-neurologically-sound-hooks-first-second.md) | Expert signal — Neurologically sound hooks and the first second (Tether Lab / Neurons Inc research) | 15 |
| [expert-insights/inbox/2026-06-18-organic-content-playbook-2026.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-18-organic-content-playbook-2026.md) | Expert signal — The organic content playbook 2026 | 15 |
| [expert-insights/inbox/2026-06-19-emotional-delivery-timing-teep.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-19-emotional-delivery-timing-teep.md) | Expert signal — Emotional delivery and timing (valence/intensity + TEEP) | 5 |
| [expert-insights/inbox/2026-06-19-permission-hooks-zone-1-soft-creative.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-06-19-permission-hooks-zone-1-soft-creative.md) | Expert signal — Permission hooks, the Emotional Zone Audit, soft creative | 5 |
| [expert-insights/inbox/2026-10-09-meta-creative-shop-creative-playbook.md](parker-brain/creative-strategy-context/expert-insights/inbox/2026-10-09-meta-creative-shop-creative-playbook.md) | Expert signal - Meta Creative Shop, "Creative on Meta: Creative Playbook" | 4 |
| [expert-insights/inbox/README.md](parker-brain/creative-strategy-context/expert-insights/inbox/README.md) | Expert Insights Inbox | 1 |
| [expert-insights/INDEX.md](parker-brain/creative-strategy-context/expert-insights/INDEX.md) | Creative Strategy Expert Insights Index | 18 |
| [expertise-routing.md](parker-brain/creative-strategy-context/expertise-routing.md) | Expertise routing — which creative-strategy-context docs each doc type loads | 31 |
| [gifting/2026/2026-q4-read.md](parker-brain/creative-strategy-context/gifting/2026/2026-q4-read.md) | 2026 Q4 Gifting — the year-specific read | 5 |
| [gifting/README.md](parker-brain/creative-strategy-context/gifting/README.md) | Gifting — year folders | 2 |
| [gifting-and-q4-creative.md](parker-brain/creative-strategy-context/gifting-and-q4-creative.md) | Gifting and Q4 Creative | 23 |
| [hook-psychology.md](parker-brain/creative-strategy-context/hook-psychology.md) | Hook Psychology — The Cognitive Science Beneath The Taxonomy | 21 |
| [hooks.md](parker-brain/creative-strategy-context/hooks.md) | Hooks Context Document | 62 |
| [ideation-and-brainstorming.md](parker-brain/creative-strategy-context/ideation-and-brainstorming.md) | Ideation and brainstorming | 37 |
| [iterations.md](parker-brain/creative-strategy-context/iterations.md) | Making Iterations | 157 |
| [killer-performance-ads.md](parker-brain/creative-strategy-context/killer-performance-ads.md) | How to Make Killer Performance Ads (For Editors and Strategists) — Volume 1 | 24 |
| [legal-ai-ugc.md](parker-brain/creative-strategy-context/legal-ai-ugc.md) | Legal: AI UGC | 6 |
| [lifestyle-headline-generator.md](parker-brain/creative-strategy-context/lifestyle-headline-generator.md) | Lifestyle Brand Headline Generator | 41 |
| [lifestyle-video-ad-formats.md](parker-brain/creative-strategy-context/lifestyle-video-ad-formats.md) | Lifestyle Video Ad Formats | 94 |
| [meta-creative-playbook.md](parker-brain/creative-strategy-context/meta-creative-playbook.md) | Creative On Meta: Meta's First-Party Creative Playbook (2026) | 25 |
| [new-product-launches.md](parker-brain/creative-strategy-context/new-product-launches.md) | Launching Ads For New Products And New SKUs | 64 |
| [new-sku-launch.md](parker-brain/creative-strategy-context/new-sku-launch.md) | New SKU Launch | 2 |
| [non-problem-solution-creative.md](parker-brain/creative-strategy-context/non-problem-solution-creative.md) | Non-problem-solution creative | 5 |
| [old-ads/INDEX.md](parker-brain/creative-strategy-context/old-ads/INDEX.md) | Old-ads corpus — index | 1 |
| [old-ads/README.md](parker-brain/creative-strategy-context/old-ads/README.md) | The old-ads corpus | 5 |
| [organic-social-analysis.md](parker-brain/creative-strategy-context/organic-social-analysis.md) | Organic social analysis | 16 |
| [parker-taste/idea-bank/founder-podcast-objection-handling/idea.md](parker-brain/creative-strategy-context/parker-taste/idea-bank/founder-podcast-objection-handling/idea.md) | Founder podcast objection-handling | 5 |
| [parker-taste/idea-bank/INDEX.md](parker-brain/creative-strategy-context/parker-taste/idea-bank/INDEX.md) | Creative Strategy Parker Taste Idea Bank — Index | 2 |
| [parker-taste/idea-bank/README.md](parker-brain/creative-strategy-context/parker-taste/idea-bank/README.md) | Creative Strategy Parker Taste Idea Bank | 9 |
| [parker-taste/patterns-to-monitor/INDEX.md](parker-brain/creative-strategy-context/parker-taste/patterns-to-monitor/INDEX.md) | Creative Strategy Patterns To Monitor — Index | 23 |
| [parker-taste/patterns-to-monitor/README.md](parker-brain/creative-strategy-context/parker-taste/patterns-to-monitor/README.md) | Creative Strategy Patterns To Monitor | 3 |
| [persona-research-and-creative-strategy-process.md](parker-brain/creative-strategy-context/persona-research-and-creative-strategy-process.md) | Persona research and creative strategy process | 25 |
| [problem-solution-headline-writer.md](parker-brain/creative-strategy-context/problem-solution-headline-writer.md) | Problem/Solution Headline Writer | 54 |
| [problem-solution-video-ad-formats.md](parker-brain/creative-strategy-context/problem-solution-video-ad-formats.md) | Problem-Solution Video Ad Formats | 78 |
| [scriptwriting.md](parker-brain/creative-strategy-context/scriptwriting.md) | Scriptwriting | 33 |
| [seasonality.md](parker-brain/creative-strategy-context/seasonality.md) | Seasonality | 9 |
| [selecting-ads-to-iterate-on.md](parker-brain/creative-strategy-context/selecting-ads-to-iterate-on.md) | Choosing Which Ads to Iterate On | 21 |
| [spoken-script-voice.md](parker-brain/creative-strategy-context/spoken-script-voice.md) | Spoken-Script Voice | 30 |
| [static-ad-design.md](parker-brain/creative-strategy-context/static-ad-design.md) | Static ad design | 11 |
| [static-ad-recreation.md](parker-brain/creative-strategy-context/static-ad-recreation.md) | Static Ad Recreation Context Document | 9 |
| [veo3-video-prompting.md](parker-brain/creative-strategy-context/veo3-video-prompting.md) | Veo 3 Video Generation Context Document | 28 |
| [visuals.md](parker-brain/creative-strategy-context/visuals.md) | Visuals | 10 |
| [visual-vocabulary-method.md](parker-brain/creative-strategy-context/visual-vocabulary-method.md) | Visual-Vocabulary Method | 22 |

## General knowledge

| Document | Title | KB |
|---|---|---|
| [best-use-cases.md](parker-brain/global/knowledge/best-use-cases.md) | Best use cases for Parker | 37 |
| [performance/account-structure-principles.md](parker-brain/global/knowledge/performance/account-structure-principles.md) | Account structure principles | 12 |
| [performance/expert-insights/context-update-candidates/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md](parker-brain/global/knowledge/performance/expert-insights/context-update-candidates/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md) | Candidate / draft pointer — Marketing Operators ep. 111 (signal engineering + reach) | 4 |
| [performance/expert-insights/context-update-candidates/2026-06-18-meta-performance-summit-playbook.md](parker-brain/global/knowledge/performance/expert-insights/context-update-candidates/2026-06-18-meta-performance-summit-playbook.md) | Context update candidates — Meta Performance Summit playbook (Disruptor School) | 6 |
| [performance/expert-insights/context-update-candidates/README.md](parker-brain/global/knowledge/performance/expert-insights/context-update-candidates/README.md) | Review queue — proposals pending Jimmy's approval (Performance) | 7 |
| [performance/expert-insights/curation/README.md](parker-brain/global/knowledge/performance/expert-insights/curation/README.md) | Performance Expert Insights — Curation | 1 |
| [performance/expert-insights/inbox/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md](parker-brain/global/knowledge/performance/expert-insights/inbox/2026-06-18-marketing-operators-ep111-signal-engineering-reach.md) | Expert signal — Marketing Operators ep. 111 (signal engineering + reach testing) | 14 |
| [performance/expert-insights/inbox/2026-06-18-marketing-operators-mpms-2026-debrief.md](parker-brain/global/knowledge/performance/expert-insights/inbox/2026-06-18-marketing-operators-mpms-2026-debrief.md) | Expert signal — Marketing Operators MPMS 2026 debrief + TikTok Shop | 20 |
| [performance/expert-insights/inbox/2026-06-18-meta-performance-summit-playbook.md](parker-brain/global/knowledge/performance/expert-insights/inbox/2026-06-18-meta-performance-summit-playbook.md) | Expert signal — Meta Performance Summit playbook (Disruptor School) | 19 |
| [performance/expert-insights/inbox/README.md](parker-brain/global/knowledge/performance/expert-insights/inbox/README.md) | Performance Expert Insights Inbox | 1 |
| [performance/expert-insights/INDEX.md](parker-brain/global/knowledge/performance/expert-insights/INDEX.md) | Performance (Media Buying) Expert Insights Index | 9 |
| [performance/incrementality-and-lift.md](parker-brain/global/knowledge/performance/incrementality-and-lift.md) | Incrementality and lift | 13 |
| [webinars/2026-07-02-monthly-webinar.md](parker-brain/global/knowledge/webinars/2026-07-02-monthly-webinar.md) | Monthly webinar — Thursday 2 July 2026 | 78 |
| [webinars/2026-08-06-monthly-webinar.md](parker-brain/global/knowledge/webinars/2026-08-06-monthly-webinar.md) | Monthly webinar — Thursday 6 August 2026 | 82 |
| [webinars/INDEX.md](parker-brain/global/knowledge/webinars/INDEX.md) | Parker monthly webinars | 7 |

## System and method docs

| Document | Title | KB |
|---|---|---|
| [attribution-principle.md](parker-brain/system/attribution-principle.md) | Attribution — design principle | 6 |
| [brain-scaffold.md](parker-brain/system/brain-scaffold.md) | Brain scaffold: what a new brand brain starts with, and how it gets there | 19 |
| [brain-sync.md](parker-brain/system/brain-sync.md) | Brain sync — how a brand brain stays saved, and what the agent's job is (and isn't) | 28 |
| [codex-support.md](parker-brain/system/codex-support.md) | Codex support | 10 |
| [growing-the-brain.md](parker-brain/system/growing-the-brain.md) | Growing the brain — the scaffold is a floor, not a ceiling | 12 |
| [master-file-structure.md](parker-brain/system/master-file-structure.md) | Parker v2 — Master File Structure | 71 |
| [master-prompt-review.md](parker-brain/system/master-prompt-review.md) | Master prompt review | 19 |
| [open-loops-system.md](parker-brain/system/open-loops-system.md) | Open loops, hypotheses, and validations | 32 |
| [parker-system-map.md](parker-brain/system/parker-system-map.md) | Parker system map | 90 |
| [parker-tool-names.md](parker-brain/system/parker-tool-names.md) | Parker tool names — current vs legacy | 4 |
| [parker-tools.md](parker-brain/system/parker-tools.md) | Parker's tools — what Parker can actually pull | 16 |
| [refresh-cadence.md](parker-brain/system/refresh-cadence.md) | Refresh cadence — keeping the brand brain from going stale | 10 |
| [schedules.md](parker-brain/system/schedules.md) | Schedules — keeping a brand brain running on its own | 7 |
| [system-of-records.md](parker-brain/system/system-of-records.md) | System of records | 12 |
| [three-phase-operating-model.md](parker-brain/system/three-phase-operating-model.md) | The three-phase operating model | 12 |
| [usage-logging.md](parker-brain/system/usage-logging.md) | Optional token usage logging | 9 |

## Self-improvement

| Document | Title | KB |
|---|---|---|
| [dreaming-system.md](parker-brain/self-improvement/dreaming-system.md) | Dreaming system | 13 |
| [reasoning-traces/2026-07/2026-07-03-bypass-hook-pull-log-bounce-traces.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-bypass-hook-pull-log-bounce-traces.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-context-grounding-gate.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-context-grounding-gate.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-03-creative-voice-review-gate.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-creative-voice-review-gate.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-gates-auto-run-and-lead-with-reasoning.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-gates-auto-run-and-lead-with-reasoning.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-03-grounding-agent-peer-strategist.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-grounding-agent-peer-strategist.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-grounding-check-facts-not-flavor.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-grounding-check-facts-not-flavor.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-refresh-context-phase-dependency-spine.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-refresh-context-phase-dependency-spine.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-03-register-translation-and-skill-birth-principles.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-register-translation-and-skill-birth-principles.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-03-rhetorical-self-question-tell.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-rhetorical-self-question-tell.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-routine-run-log-and-arming-scope.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-routine-run-log-and-arming-scope.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-rsl-is-doctrine-canon-script-coach-refit.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-rsl-is-doctrine-canon-script-coach-refit.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-strategy-first-tactical-baseline.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-strategy-first-tactical-baseline.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-03-team-conversations-phase1-source.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-team-conversations-phase1-source.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-03-user-profile-system.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-03-user-profile-system.md) |  | 5 |
| [reasoning-traces/2026-07/2026-07-08-reading-level-block-phase1.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-08-reading-level-block-phase1.md) |  | 4 |
| [reasoning-traces/2026-07/2026-07-08-submodule-layout-decision.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-08-submodule-layout-decision.md) | 2026-07-08 — Why the brand brain mounts the factory instead of copying it | 3 |
| [reasoning-traces/2026-07/2026-07-09-harvest-ideas-v2-proposal.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-09-harvest-ideas-v2-proposal.md) | Harvest v2 proposal | 23 |
| [reasoning-traces/2026-07/2026-07-10-migration-and-release-note-per-change.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-10-migration-and-release-note-per-change.md) | 2026-07-10 — Every change ships its versioning artifacts, not just the change | 4 |
| [reasoning-traces/2026-07/2026-07-14-identity-second-person.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-14-identity-second-person.md) | Identity is second person | 3 |
| [reasoning-traces/2026-07/2026-07-14-main-only-git-explicit-permission.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-14-main-only-git-explicit-permission.md) |  | 3 |
| [reasoning-traces/2026-07/2026-07-14-onboarding-existence-triage.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-14-onboarding-existence-triage.md) |  | 3 |
| [reasoning-traces/2026-07/2026-07-24-voice-output-style-layer.md](parker-brain/self-improvement/reasoning-traces/2026-07/2026-07-24-voice-output-style-layer.md) |  | 4 |
| [reasoning-traces/2026-08/2026-08-07-craft-doc-intake-sweeps-the-skill-layer.md](parker-brain/self-improvement/reasoning-traces/2026-08/2026-08-07-craft-doc-intake-sweeps-the-skill-layer.md) |  | 5 |
| [reasoning-traces/2026-09/2026-09-25-brain-scaffold-script.md](parker-brain/self-improvement/reasoning-traces/2026-09/2026-09-25-brain-scaffold-script.md) |  | 4 |
| [reasoning-traces/2026-10/2026-10-01-voice-gate-terminal-states.md](parker-brain/self-improvement/reasoning-traces/2026-10/2026-10-01-voice-gate-terminal-states.md) |  | 3 |
| [self-improvement-system.md](parker-brain/self-improvement/self-improvement-system.md) | Parker self-improvement system | 11 |
| [the-living-loop.md](parker-brain/self-improvement/the-living-loop.md) | The living loop — dreaming and self-improvement | 7 |

## Prompts

| Document | Title | KB |
|---|---|---|
| [_brand-intake-context-block.md](parker-brain/prompts/_brand-intake-context-block.md) | Brand-intake context block (synced source) | 3 |
| [_expertise-core-block.md](parker-brain/prompts/_expertise-core-block.md) | Expertise core block | 7 |
| [_notion-ai-tagging-and-foundational-context.md](parker-brain/prompts/_notion-ai-tagging-and-foundational-context.md) | Notion prompt library context — AI tagging and foundational analysis | 11 |
| [_open-loops-core-block.md](parker-brain/prompts/_open-loops-core-block.md) | Open-loops core block | 10 |
| [_parker-voice-block.md](parker-brain/prompts/_parker-voice-block.md) | Parker voice block | 14 |
| [_reading-level-block.md](parker-brain/prompts/_reading-level-block.md) | Reading level block | 4 |
| [_team-conversations-source-block.md](parker-brain/prompts/_team-conversations-source-block.md) | Team-conversations source block (synced source) | 3 |
| [audits-biweekly/biweekly-iterations-report.md](parker-brain/prompts/audits-biweekly/biweekly-iterations-report.md) | Prompt — bi-weekly iterations report | 31 |
| [audits-monthly/monthly-hook-audit.md](parker-brain/prompts/audits-monthly/monthly-hook-audit.md) | Prompt — monthly hook audit | 52 |
| [audits-monthly/monthly-organic-tiktok-audit.md](parker-brain/prompts/audits-monthly/monthly-organic-tiktok-audit.md) | Prompt — monthly organic TikTok audit | 39 |
| [audits-monthly/monthly-performance-report.md](parker-brain/prompts/audits-monthly/monthly-performance-report.md) | Prompt — monthly performance report | 32 |
| [audits-monthly/monthly-tiktok-mining.md](parker-brain/prompts/audits-monthly/monthly-tiktok-mining.md) | Prompt — monthly TikTok mining | 33 |
| [audits-monthly-external/monthly-creative-landscape.md](parker-brain/prompts/audits-monthly-external/monthly-creative-landscape.md) | Prompt — monthly creative landscape | 33 |
| [audits-monthly-external/monthly-top-impressions-report.md](parker-brain/prompts/audits-monthly-external/monthly-top-impressions-report.md) | Prompt — monthly top-impressions report | 33 |
| [audits-quarterly/90-day-creative-strategy-audit.md](parker-brain/prompts/audits-quarterly/90-day-creative-strategy-audit.md) | Prompt — 90-day creative strategy audit | 39 |
| [audits-quarterly/90-day-diversity-audit.md](parker-brain/prompts/audits-quarterly/90-day-diversity-audit.md) | Prompt — 90-day creative diversity audit, format lens | 32 |
| [audits-quarterly/90-day-performance-audit.md](parker-brain/prompts/audits-quarterly/90-day-performance-audit.md) | Prompt — 90-day performance and delivery audit | 31 |
| [audits-quarterly/customer-review-audit.md](parker-brain/prompts/audits-quarterly/customer-review-audit.md) | Prompt — customer review audit | 35 |
| [audits-quarterly/quarterly-whitespace-analysis.md](parker-brain/prompts/audits-quarterly/quarterly-whitespace-analysis.md) | Prompt — quarterly whitespace analysis | 32 |
| [audits-quarterly-external/90-day-creative-strategy-audit-external.md](parker-brain/prompts/audits-quarterly-external/90-day-creative-strategy-audit-external.md) | Prompt — 90-day creative strategy audit, external | 36 |
| [audits-quarterly-external/90-day-diversity-audit-external.md](parker-brain/prompts/audits-quarterly-external/90-day-diversity-audit-external.md) | Prompt — 90-day diversity audit, external | 31 |
| [audits-quarterly-external/90-day-performance-audit-external.md](parker-brain/prompts/audits-quarterly-external/90-day-performance-audit-external.md) | Prompt — 90-day performance audit, external | 34 |
| [audits-quarterly-external/single-competitor-ad-analysis.md](parker-brain/prompts/audits-quarterly-external/single-competitor-ad-analysis.md) | Prompt — single competitor ad analysis | 32 |
| [audits-weekly/weekly-performance-snapshot.md](parker-brain/prompts/audits-weekly/weekly-performance-snapshot.md) | Prompt — weekly performance snapshot | 28 |
| [brand-profile/_foundations.md](parker-brain/prompts/brand-profile/_foundations.md) | Foundations for building context docs | 17 |
| [brand-profile/ad-account-evaluation.md](parker-brain/prompts/brand-profile/ad-account-evaluation.md) | Prompt - brand ad account evaluation | 42 |
| [brand-profile/brand-identity-analysis.md](parker-brain/prompts/brand-profile/brand-identity-analysis.md) | Prompt — brand identity analysis | 37 |
| [brand-profile/brand-profile-narrative.md](parker-brain/prompts/brand-profile/brand-profile-narrative.md) | Prompt — brand profile narrative | 35 |
| [brand-profile/category-and-market-research.md](parker-brain/prompts/brand-profile/category-and-market-research.md) | Prompt — category and market research | 33 |
| [brand-profile/community-and-forums.md](parker-brain/prompts/brand-profile/community-and-forums.md) | Prompt — community and forums | 46 |
| [brand-profile/competitive-landscape.md](parker-brain/prompts/brand-profile/competitive-landscape.md) | Prompt — competitive landscape | 33 |
| [brand-profile/customer-journey-and-persona-discovery.md](parker-brain/prompts/brand-profile/customer-journey-and-persona-discovery.md) | Prompt — customer journey and persona discovery | 50 |
| [brand-profile/marketing-calendar-and-campaigns.md](parker-brain/prompts/brand-profile/marketing-calendar-and-campaigns.md) | Prompt — marketing calendar and campaigns | 40 |
| [brand-profile/operations-and-team.md](parker-brain/prompts/brand-profile/operations-and-team.md) | Prompt — operations and team | 41 |
| [brand-profile/organic-channels-inventory.md](parker-brain/prompts/brand-profile/organic-channels-inventory.md) | Prompt — organic channels inventory | 42 |
| [brand-profile/performance-targets-and-metrics.md](parker-brain/prompts/brand-profile/performance-targets-and-metrics.md) | Prompt — performance targets and metrics | 60 |
| [brand-profile/README.md](parker-brain/prompts/brand-profile/README.md) | Brand-profile prompts | 4 |
| [brand-profile/reputation-analysis.md](parker-brain/prompts/brand-profile/reputation-analysis.md) | Prompt — reputation analysis | 46 |
| [brand-profile/visual-vocabulary.md](parker-brain/prompts/brand-profile/visual-vocabulary.md) | Prompt: visual vocabulary | 38 |
| [brand-profile/website-and-product-audit.md](parker-brain/prompts/brand-profile/website-and-product-audit.md) | Prompt — website and product audit | 38 |
| [competitor-profile/competitor-ad-account-evaluation.md](parker-brain/prompts/competitor-profile/competitor-ad-account-evaluation.md) | Prompt — competitor ad account evaluation | 39 |
| [competitor-profile/competitor-brand-identity-analysis.md](parker-brain/prompts/competitor-profile/competitor-brand-identity-analysis.md) | Prompt — competitor brand identity analysis | 37 |
| [competitor-profile/competitor-community-and-forums.md](parker-brain/prompts/competitor-profile/competitor-community-and-forums.md) | Prompt — competitor community and forums | 35 |
| [competitor-profile/competitor-customer-and-persona-discovery.md](parker-brain/prompts/competitor-profile/competitor-customer-and-persona-discovery.md) | Prompt — competitor customer and persona discovery | 36 |
| [competitor-profile/competitor-organic-channels-audit.md](parker-brain/prompts/competitor-profile/competitor-organic-channels-audit.md) | Prompt — competitor organic channels audit | 38 |
| [competitor-profile/competitor-reputation-analysis.md](parker-brain/prompts/competitor-profile/competitor-reputation-analysis.md) | Prompt — competitor reputation analysis | 36 |
| [competitor-profile/competitor-reviews-and-customer-language.md](parker-brain/prompts/competitor-profile/competitor-reviews-and-customer-language.md) | Prompt — competitor reviews and customer language | 37 |
| [competitor-profile/competitor-snapshot.md](parker-brain/prompts/competitor-profile/competitor-snapshot.md) | Prompt — competitor snapshot | 35 |
| [competitor-profile/competitor-website-and-product-audit.md](parker-brain/prompts/competitor-profile/competitor-website-and-product-audit.md) | Prompt — competitor website and product audit | 36 |
| [competitor-profile/running-notes-on-competitor.md](parker-brain/prompts/competitor-profile/running-notes-on-competitor.md) | Prompt — running notes on the competitor | 33 |
| [competitor-profile/working-thesis-synthesis.md](parker-brain/prompts/competitor-profile/working-thesis-synthesis.md) | Prompt — working-thesis synthesis | 42 |
| [global-databases/expert-signal-db.md](parker-brain/prompts/global-databases/expert-signal-db.md) | Spec - expert signal database | 15 |
| [global-databases/global-ai-tagged-ads-db.md](parker-brain/prompts/global-databases/global-ai-tagged-ads-db.md) | Spec — global AI-tagged ads database | 13 |
| [global-databases/internal-favorites-db.md](parker-brain/prompts/global-databases/internal-favorites-db.md) | Spec — internal favorites database | 11 |
| [global-databases/parker-favorites-db.md](parker-brain/prompts/global-databases/parker-favorites-db.md) | Spec — Parker favorites database | 11 |
| [global-databases/README.md](parker-brain/prompts/global-databases/README.md) | Global Database Prompts | 1 |
| [ideas-and-briefs/brand-idea-bank.md](parker-brain/prompts/ideas-and-briefs/brand-idea-bank.md) | Spec - brand idea bank | 21 |
| [ideas-and-briefs/brief-creation.md](parker-brain/prompts/ideas-and-briefs/brief-creation.md) | Prompt — brief creation | 34 |
| [ideas-and-briefs/idea-evaluation.md](parker-brain/prompts/ideas-and-briefs/idea-evaluation.md) | Prompt — idea evaluation | 23 |
| [ideas-and-briefs/sprint-plan.md](parker-brain/prompts/ideas-and-briefs/sprint-plan.md) | Prompt — sprint plan | 30 |
| [market-synthesis/gaps-opportunities-inspo.md](parker-brain/prompts/market-synthesis/gaps-opportunities-inspo.md) | Prompt — gaps, opportunities, inspo | 19 |
| [onboarding-runner.md](parker-brain/prompts/onboarding-runner.md) | Onboarding runner — build a brand brain from scratch | 99 |
| [open-loops/open-loops-roll-up.md](parker-brain/prompts/open-loops/open-loops-roll-up.md) | Prompt — open-loops roll-up and grading | 30 |
| [personas/ad-account.md](parker-brain/prompts/personas/ad-account.md) | Prompt — ad account | 32 |
| [personas/ad-comments.md](parker-brain/prompts/personas/ad-comments.md) | Prompt — ad comments | 31 |
| [personas/brand-reputation.md](parker-brain/prompts/personas/brand-reputation.md) | Prompt — brand reputation | 31 |
| [personas/brand-self-echo-detection.md](parker-brain/prompts/personas/brand-self-echo-detection.md) | Prompt — brand-self-echo detection | 34 |
| [personas/cross-persona-bias-notes.md](parker-brain/prompts/personas/cross-persona-bias-notes.md) | Prompt — cross-persona bias notes | 34 |
| [personas/customer-reviews.md](parker-brain/prompts/personas/customer-reviews.md) | Prompt — customer reviews | 33 |
| [personas/lifecycle-journey-maps.md](parker-brain/prompts/personas/lifecycle-journey-maps.md) | Prompt - lifecycle journey maps | 24 |
| [personas/other-reviews.md](parker-brain/prompts/personas/other-reviews.md) | Prompt — other reviews | 31 |
| [personas/personas-profile.md](parker-brain/prompts/personas/personas-profile.md) | Prompt — personas profile | 42 |
| [personas/persona-voice-library.md](parker-brain/prompts/personas/persona-voice-library.md) | Prompt - persona voice and emotion library | 24 |
| [personas/post-purchase-surveys.md](parker-brain/prompts/personas/post-purchase-surveys.md) | Prompt — post-purchase surveys | 32 |
| [personas/reddit.md](parker-brain/prompts/personas/reddit.md) | Prompt — reddit | 31 |
| [README.md](parker-brain/prompts/README.md) | Running the prompts — the build order for standing up a brand brain | 13 |
| [strategic-roadmap/creator-talent-strategy-input.md](parker-brain/prompts/strategic-roadmap/creator-talent-strategy-input.md) | Prompt — creator and talent strategy input | 31 |
| [strategic-roadmap/messaging-strategy-input.md](parker-brain/prompts/strategic-roadmap/messaging-strategy-input.md) | Prompt — messaging strategy input | 31 |
| [strategic-roadmap/persona-strategy-input.md](parker-brain/prompts/strategic-roadmap/persona-strategy-input.md) | Prompt — persona strategy input | 31 |
| [strategic-roadmap/product-priority.md](parker-brain/prompts/strategic-roadmap/product-priority.md) | Prompt — product priority | 33 |
| [strategic-roadmap/strategic-roadmap.md](parker-brain/prompts/strategic-roadmap/strategic-roadmap.md) | Prompt — strategic roadmap | 33 |
| [voice-of-customer/voc-anti-language.md](parker-brain/prompts/voice-of-customer/voc-anti-language.md) | Prompt — VoC anti-language extraction | 32 |
| [voice-of-customer/voc-aspirational.md](parker-brain/prompts/voice-of-customer/voc-aspirational.md) | Prompt — VoC aspirational phrase extraction | 32 |
| [voice-of-customer/voc-category-jargon.md](parker-brain/prompts/voice-of-customer/voc-category-jargon.md) | Prompt — VoC category jargon extraction | 32 |
| [voice-of-customer/voc-corpus-profile.md](parker-brain/prompts/voice-of-customer/voc-corpus-profile.md) | Prompt - VoC corpus profile | 15 |
| [voice-of-customer/voc-metaphor.md](parker-brain/prompts/voice-of-customer/voc-metaphor.md) | Prompt — VoC metaphor extraction | 33 |
| [voice-of-customer/voc-objection.md](parker-brain/prompts/voice-of-customer/voc-objection.md) | Prompt — VoC objection extraction | 31 |
| [voice-of-customer/voc-outcome-phrase.md](parker-brain/prompts/voice-of-customer/voc-outcome-phrase.md) | Prompt — VoC outcome phrase extraction | 31 |
| [voice-of-customer/voc-pain-phrase.md](parker-brain/prompts/voice-of-customer/voc-pain-phrase.md) | Prompt — VoC pain phrase extraction | 31 |
| [voice-of-customer/voc-surprise-delight.md](parker-brain/prompts/voice-of-customer/voc-surprise-delight.md) | Prompt — VoC surprise and delight extraction | 31 |
| [voice-of-customer/voc-trigger-moment.md](parker-brain/prompts/voice-of-customer/voc-trigger-moment.md) | Prompt — VoC trigger moment extraction | 32 |
| [voice-of-customer/voice-of-customer-assembly.md](parker-brain/prompts/voice-of-customer/voice-of-customer-assembly.md) | Prompt — Voice of Customer assembly | 38 |

## Templates

| Document | Title | KB |
|---|---|---|
| [brand-brain-CLAUDE-template.md](parker-brain/templates/brand-brain-CLAUDE-template.md) | Brand-brain CLAUDE.md template | 46 |
| [brand-lens-template.md](parker-brain/templates/brand-lens-template.md) | Brand lens template | 4 |
| [brand-notes-from-org-template.md](parker-brain/templates/brand-notes-from-org-template.md) | Brand-notes-from-org template | 4 |
| [brand-routines/AGENTS.md](parker-brain/templates/brand-routines/AGENTS.md) | AGENTS.md — this brand's brain, for OpenAI Codex (and any AGENTS.md-reading harness) | 5 |
| [brand-routines/claude/README.md](parker-brain/templates/brand-routines/claude/README.md) | `.claude/` — the brand brain's routines and config | 12 |
| [brand-routines/codex/README.md](parker-brain/templates/brand-routines/codex/README.md) | `.codex/` — the brand brain on OpenAI Codex | 4 |
| [brand-routines/README.md](parker-brain/templates/brand-routines/README.md) | Brand-routines template — the stampable living loop | 9 |
| [brand-routines/schedules/dream.md](parker-brain/templates/brand-routines/schedules/dream.md) | Schedule — dream | 3 |
| [brand-routines/schedules/ideas-weekly.md](parker-brain/templates/brand-routines/schedules/ideas-weekly.md) | Schedule — ideas-weekly (harvest → evaluate) | 3 |
| [brand-routines/schedules/README.md](parker-brain/templates/brand-routines/schedules/README.md) | Schedules | 4 |
| [brand-routines/schedules/refresh-context.md](parker-brain/templates/brand-routines/schedules/refresh-context.md) | Schedule — refresh-context | 2 |
| [brand-routines/schedules/research-loops.md](parker-brain/templates/brand-routines/schedules/research-loops.md) | Schedule — research-loops | 3 |
| [brand-routines/schedules/self-improve.md](parker-brain/templates/brand-routines/schedules/self-improve.md) | Schedule — self-improve | 3 |
| [brand-routines/schedules/update-brain.md](parker-brain/templates/brand-routines/schedules/update-brain.md) | Schedule — update-brain | 4 |
| [brand-rules-template.md](parker-brain/templates/brand-rules-template.md) | Brand rules — {{BRAND_NAME}} | 2 |
| [brand-scaffold/audits/README.md](parker-brain/templates/brand-scaffold/audits/README.md) | Audits | 2 |
| [brand-scaffold/briefs/README.md](parker-brain/templates/brand-scaffold/briefs/README.md) | Briefs | 1 |
| [brand-scaffold/competitors/README.md](parker-brain/templates/brand-scaffold/competitors/README.md) | Competitors | 2 |
| [brand-scaffold/dreaming/README.md](parker-brain/templates/brand-scaffold/dreaming/README.md) | Dreaming | 1 |
| [brand-scaffold/expert-insights/README.md](parker-brain/templates/brand-scaffold/expert-insights/README.md) | Expert insights | 1 |
| [brand-scaffold/hypotheses/README.md](parker-brain/templates/brand-scaffold/hypotheses/README.md) | Hypotheses | 1 |
| [brand-scaffold/idea-bank/README.md](parker-brain/templates/brand-scaffold/idea-bank/README.md) | Idea bank | 1 |
| [brand-scaffold/open-loops/README.md](parker-brain/templates/brand-scaffold/open-loops/README.md) | Open loops | 2 |
| [brand-scaffold/personas/README.md](parker-brain/templates/brand-scaffold/personas/README.md) | Personas | 2 |
| [brand-scaffold/README.md](parker-brain/templates/brand-scaffold/README.md) | {{BRAND_NAME}}'s Parker brain | 2 |
| [brand-scaffold/re-validations/README.md](parker-brain/templates/brand-scaffold/re-validations/README.md) | Re-validations | 1 |
| [brand-scaffold/source-pulls/README.md](parker-brain/templates/brand-scaffold/source-pulls/README.md) | Source pulls | 1 |
| [brand-scaffold/sprints/README.md](parker-brain/templates/brand-scaffold/sprints/README.md) | Sprints | 1 |
| [brand-scaffold/strategy/README.md](parker-brain/templates/brand-scaffold/strategy/README.md) | Strategy | 1 |
| [brand-scaffold/sub-context-docs/README.md](parker-brain/templates/brand-scaffold/sub-context-docs/README.md) | Sub-context docs | 2 |
| [brand-scaffold/validations/README.md](parker-brain/templates/brand-scaffold/validations/README.md) | Validations | 1 |
| [brand-scaffold/workflows/README.md](parker-brain/templates/brand-scaffold/workflows/README.md) | Workflows | 1 |
| [missing-context-template.md](parker-brain/templates/missing-context-template.md) | Missing-context template | 4 |
| [personas-design.md](parker-brain/templates/personas-design.md) | Personas — design principles | 7 |
| [personas-template.md](parker-brain/templates/personas-template.md) | Template — personas-profile.md | 12 |
| [refresh-schedule-template.md](parker-brain/templates/refresh-schedule-template.md) | Refresh-schedule template | 6 |
| [routine-log-template.md](parker-brain/templates/routine-log-template.md) | Routine-log template | 2 |
| [standard-sync-template.md](parker-brain/templates/standard-sync-template.md) | Standard sync — the update ledger | 2 |
| [success-definition-template.md](parker-brain/templates/success-definition-template.md) | Success definition — {{BRAND_NAME}} | 1 |
| [user-profile-template.md](parker-brain/templates/user-profile-template.md) | User-profile template | 10 |
| [voc-design.md](parker-brain/templates/voc-design.md) | Voice of Customer — design principles | 7 |
| [voc-template.md](parker-brain/templates/voc-template.md) | Template — voice-of-customer.md | 9 |
