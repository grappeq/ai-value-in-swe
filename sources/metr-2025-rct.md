# metr-2025-rct — METR RCT on experienced open-source developers

## Citation

Becker, J., Rush, N., Barnes, B. (Elizabeth), & Rein, D. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.* Model Evaluation & Threat Research (METR).

- arXiv: [2507.09089](https://arxiv.org/abs/2507.09089) — v1 12 Jul 2025; **v2 25 Jul 2025 (version read for this record)**. 51 pages. DOI: 10.48550/arXiv.2507.09089
- METR blog announcement (10 Jul 2025): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Data + analysis code: https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs (anonymised `data_complete.csv`, 246 issues; `regression.py`)
- Status: preprint / METR working paper; no peer-reviewed venue identified as of Jul 2026.

## Verification status

**VERIFIED.** Full text (arXiv v2 PDF, 51 pp.) fetched and read; headline numbers cross-checked against METR's blog post and the numeric output in the GitHub repo README. No paywall; no preprint substitution needed (the arXiv version *is* the canonical version).

## Tier & era & independence

- **Tier: A.** Randomised controlled trial (task-level randomisation, 246 tasks), pre-registered outcome measure (tasks defined before assignment), released data and code, 21-factor robustness/artefact analysis.
- **Era: E3 (early-agentic), with an E2/E3-boundary caveat.** Modality actually studied: Cursor Pro (agent + chat + autocomplete) with Claude 3.5/3.7 Sonnet, Feb–Jun 2025 frontier. Developers used "Cursor agents/chat in majority of AI-allowed issues" (§C.2.10); model mix on labelled recordings: Claude 3.7 Sonnet thinking 25%, Claude 3.7 Sonnet 34%, Claude 3.5 Sonnet 23%, GPT-4o 11%, Gemini 2.5 Pro 3%, o1 2%. This is early IDE-agent work, not autonomous PR agents, and most tasks pre-date Claude 4-class models — findings should not be read as covering late-2025+ agents (METR themselves say so; see Recency check).
- **Independence:** Independent non-profit research organisation; not a tool vendor; no vendor sponsorship of the study; developers paid $150/hour by METR. No Tier-D COI flag. Minor flags: (a) METR has commercial evaluation relationships with frontier labs; (b) recruitment partly via METR's professional networks; (c) self-selection — developers who believe they get large AI speedups may have declined to participate (authors' own caveat).

## Method & population

- **Design:** RCT; each real issue randomly assigned AI-allowed vs AI-disallowed (fair coin; 25 early issues randomised differently, results robust to their exclusion). In AI-allowed, developers may use any AI tools *or none*; in AI-disallowed, no generative AI (LLM autocomplete banned, non-LLM autocomplete and search engines allowed).
- **Population:** 16 experienced OSS developers (typically 10+ years' experience); on average 5 years and ~1,500 commits on their repository (59% of repo lifetime). 93% had prior LLM experience; only 44% prior Cursor experience (METR provided Cursor Pro subscriptions and basic training).
- **Repositories:** large, mature OSS projects — averages: 23,000 stars, 1.1M lines of code, 10 years old, 4,900 forks, 20,000 commits, 710 committers; high review/quality bars.
- **Tasks:** 246 real issues (bug reports, feature requests, work items), ~2.0 hours average; capped at ~2 hours (longer work split). 136 completed AI-allowed, 110 AI-disallowed.
- **Outcome:** self-reported total implementation time (pre- and post-PR-review), validated against screen recordings (recordings with >20% discrepancy excluded from the labelled-activity subset); regression-adjusted using pre-randomisation per-issue developer forecasts as a difficulty control (log-linear OLS, HC3 SEs).
- **Supplementary data:** 143 hours of screen recordings manually labelled at ~10 s resolution (84 valid hours / 74 issues after filtering); Cursor analytics; exit interviews/surveys; incentivised expert forecasts.

## Key findings

All task-type tags: primary **T4** (feature dev in mature codebases) and **T8** (debugging/bug fixes), with some **T5**; issues are a mix of bug reports, features, and work items in 1M+ LOC brownfield repos and are not reported broken down by type.

1. **Headline slowdown (measured):** allowing AI increased completion time by **19%** (regression point estimate S = 0.188, i.e. E[T|AI]/E[T|no-AI] − 1; 95% CI per repo README: **(0.013, 0.395)** HC3, (0.016, 0.39) clustered by developer — excludes zero). Raw unadjusted ratio is 34% (AI-allowed issues were forecast slightly harder; regression corrects). Robust across alternative outcome measures, estimators, and subsets (subset estimates typically 20–24%; up to 42% in one dropout subset). [T4/T8; measured]
2. **Perceived speedup (self-reported):** before the study developers forecast AI would cut completion time by **24%**; after the study they estimated it *had* cut their time by **20%** — while actually being 19% slower. The perception–reality delta (~39–43 pp swing) is itself the finding for RQ2/RQ6. [T4/T8; self-reported vs measured — both reported by the source; delta recorded as its own finding]
3. **Expert miscalibration (self-reported forecasts):** 34 economics experts forecast 39% speedup; 54 ML experts forecast 38% speedup. Both directionally wrong. [era-independent methodology point]
4. **Time reallocation (measured, labelled-recording subset, 74 issues):** with AI allowed, developers spend less time actively coding and reading/searching, and instead spend time prompting AI, waiting on generations (~4% of time), and reviewing/cleaning AI output (~9% of time); idle time also somewhat higher. Developers accept **<44%** of AI generations; a majority report making major changes to clean up AI code. [T4/T8; measured]
5. **Null/secondary (measured):** PR quality qualitatively similar between conditions (high-review-bar repos; merged PRs rarely flawed) — the slowdown is not explained by lower-quality AI-condition output. Similar slowdown for developers with prior Cursor experience; no clear learning effect over the first 30–50 hours of Cursor use. Developer time forecasts correlate well with actual times (r = 0.64 AI-allowed, 0.59 AI-disallowed) — calibrated on difficulty, miscalibrated on AI benefit. [measured]
6. **Factor analysis (suggestive, authors' caution: underpowered for multiple comparisons):** of 21 candidate factors, **5 likely contribute** to slowdown — (i) over-optimism about AI usefulness, (ii) high developer familiarity with repos (more familiar ⇒ more slowdown), (iii) large and complex repositories, (iv) low AI reliability (<44% acceptance), (v) implicit repository context AI cannot use. 10 factors unclear/mixed (incl. experimentally driven AI overuse, scope creep — 47% more LOC per forecast hour in AI-allowed issues, suboptimal elicitation); **6 factors have evidence against** (incl. unfamiliar IDE, cheating, issue dropout, non-robust outcome/estimator, non-frontier models). [mechanism evidence for RQ3]

## What this can and cannot support

Tier-A evidence that early-2025 IDE-agent tooling slowed *experienced* developers on *highly familiar, large, mature* codebases, and that self-reported AI speedup is unreliable there; it cannot support claims about juniors, unfamiliar or greenfield code, late-2025+ agents, or "AI doesn't help developers" in general — the authors explicitly disclaim all four.

## Corrections vs the seed description (PROTOCOL §6)

- Seed "−19% study… ~19% slower while believing they were ~20% faster": **accurate** as stated. Precision added: point estimate 18.8%, 95% CI (1.3%, 39.5%); post-hoc perceived speedup 20% (pre-study forecast 24%; experts 38–39%).
- Seed "using agentic tooling": **partially correct** — Cursor Pro agent/chat with Claude 3.5/3.7 Sonnet, i.e. early IDE-agent modality, not autonomous PR agents; autocomplete and chat were also in the mix. Keep the E3 tag but with the boundary caveat above.
- One circulating misquote to guard against: some secondary write-ups claim the CI spans zero ("−26% to +9%"); METR's own repo README shows the 95% CI as (0.013, 0.395) — it does **not** include zero. Do not propagate the secondary figure.
- The abstract v2 says **21** factors examined (the blog and some summaries say 20); 21 is correct per the paper.

## Follow-up leads (for Phase 1 queue)

1. **METR (2026-02-24), "We are Changing our Developer Productivity Experiment Design"** — https://metr.org/blog/2026-02-24-uplift-update/ — METR's own follow-up wave (Aug 2025: 57 devs, 143 repos, 800+ tasks, $50/hr): returning devs −18% slowdown (CI −38% to +9%), new devs −4% (CI −15% to +9%), but METR judges the data *unreliable* (selection bias — 30–50% of devs withheld tasks they didn't want to do without AI; lower pay; concurrent-agent time-tracking problems) and now believes developers are likely more sped up in early 2026 than the early-2025 estimate, with only "very weak evidence" on magnitude. **Highest-priority lead: partially contextualises this anchor.**
2. **METR (2025-08-11), "Notes on Scientific Communication at METR"** — https://metr.org/blog/2025-08-11-science-comms-at-metr/ — METR's own account of how the study was over-generalised in the press; useful for RQ2/RQ6 framing.
3. **Zvi Mowshowitz, "On METR's AI Coding RCT"** — https://thezvi.substack.com/p/on-metrs-ai-coding-rct — detailed independent commentary/critique roundup.
4. **The Experimentalist, "Critiquing the METR Productivity Study"** — https://substack.the-experimentalist.com/p/critiquing-the-metr-productivity — methodological critique (Tier C commentary).
5. **DX newsletter, "METR's study on how AI affects developer productivity"** — https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity — practitioner-analytics reading; DX is a metrics vendor, treat as Tier D.
6. **Faros AI, "What METR's Study Missed About AI Productivity in the Wild"** — https://www.faros.ai/blog/lab-vs-reality-ai-productivity-study-findings — vendor telemetry counterpoint (claims +9% tasks, +47% PRs/day on high-adoption teams); Tier D, COI-flag.
7. **Rob Bowley (2026-04-04), "METR's developer productivity research: 2026 update"** — https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/ — practitioner summary of the 2026 redesign; Tier C lead.
8. **Paper's own pointer:** "preliminary evidence (forthcoming) that fully autonomous AI agents using Claude 3.7 Sonnet can often correctly implement the core functionality of issues" from study repos (§4.1) — search for this METR follow-up publication.
9. No independent full replication RCT found as of Jul 2026 — the perception–reality gap replication question (PROTOCOL §5.1) remains open.

## Recency check notes

Source is ~12 months old at verification (Jul 2025 → Jul 2026). Not retracted; arXiv v2 (25 Jul 2025) is the latest version found. **Partially superseded in interpretation, not in result:** METR's Feb 2026 update stands by the original experiment but (a) reports their attempted continuation produced unreliable data, and (b) states their belief that AI speedup has likely improved since early 2025. Any use of the −19% figure must carry the "early-2025 tools, experienced devs, familiar mature repos" scoping and should cite the Feb 2026 update alongside it. The perception-gap finding (measured vs self-reported delta) is the most era-durable part and is plausibly era-independent per PROTOCOL §2.
