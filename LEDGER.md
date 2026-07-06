# Research Ledger
Phase: 1 (landscape sweep) | Gate status: OPEN (Phase 0 reviewed and Phase 1 opened by human, 2026-07-06)
Last session: 2026-07-06 | Last commit: see git log
Phase 1 target: ~15–25 further sources (≥25 total incl. anchors), worked from the Queued table by priority; per-RQ query plans (§6.5) fill gaps the queue doesn't cover. Outstanding non-blocking item: SPACE browser check (human).

## Phase 0 gate summary (for human review)
All 12 seed anchors verified: 11 VERIFIED (stanford-denisov-blanch upgraded via talk transcripts; gitclear-2026 upgraded via human-supplied full PDF — which also weakened GitClear's side of the churn contradiction: undisclosed ~3.3–3.8x dataset growth coincides with the churn step), 1 PARTIALLY VERIFIED (SPACE: ACM bot-block — needs a human browser check). One optional low-priority residual (Stanford slide-only figures). Four contradictions logged in synthesis/contradictions.md (GitClear churn vs peer-reviewed null; DORA throughput flip; perception-gap direction reversal; Uplevel bug rate vs vendor counter-claims). Headline Phase 0 findings: (1) the seed's era framing was optimistic — only METR is genuinely (early-)E3 among rigorous anchors; every other rigorous source is E1/E2 and baseline-only under the era transfer rule; (2) no true agentic-tool RCT beyond METR exists as of Jul 2026 — the E3 literature has converged on large-N PR-mining and diff-in-diff (Tier B), consistent with the §8 scarcity clause; (3) several canonical numbers needed correction before use (Google 21% = non-significant model; Peng CI [21%,89%], never peer-reviewed; DORA 2024 "stability −7.2%" not "instability +7.2%"; Cui seniority gains directional-only). ~45 triaged candidates queued for Phase 1, E3-weighted, incl. strong Tier C postmortem/bottleneck material. Decision requested: review the three Blocked items, approve the corrected source list, and open the Phase 1 gate.

## Done
| source_id | RQ | tier | era | batch |
|---|---|---|---|---|
| anthropic-economic-index | RQ1 | D (COI: vendor self-analysis) | E2/E3 split by surface | 1 |
| metr-2025-rct | RQ1, RQ2 | A | E3 (early IDE-agent; boundary caveat) | 1 |
| stanford-denisov-blanch | RQ1, RQ3, RQ5 | B (talk-grade figures) | E1/E2-mixed; 2026 wave E3 | 1 |
| gitclear-2025 | RQ3, RQ4 | B (COI: dual-vendor, GitClear + GitKraken) | E1/E2 trendline; 2026 edn E2/E3-blend, no modality split (authors' own admission) | 1 |
| dora-2025 | RQ5, RQ2 | B (vendor-adjacency flag) | E1/E2/E3 mixed, weighted pre-agentic | 1 |
| google-rct-2024 | RQ1 | A (COI: Google-on-Google; headline 21% non-significant in main model) | E1/E2 boundary, autocomplete-dominant | 2 |
| stackoverflow-survey-2025 | RQ2 | B (topline-percentages survey; self-selection; reverse-COI noted) | E1/E2/E3 mixed; agent sub-items E3 | 2 |
| peng-2023-copilot-rct | RQ1, RQ2 | A (COI: 3/4 authors GitHub/MS; never peer-reviewed) | E1 | 2 |
| cui-2024-copilot-field | RQ1, RQ3 | A (COI: 2/6 MS authors, vendor data; Mgmt Sci Feb 2026) | E1 (seed's E2 tag unsupported) | 2 |
| uplevel-2024 | RQ2, RQ6 | D (COI: vendor marketing; access-not-usage confound) | E1 | 2 |
| dora-2024 | RQ5, RQ2 | B (vendor-adjacency flag) | E2-dominant + E1; no E3 in instrument | 3 |
| space-dx-core4 | RQ6 | SPACE: B-equiv methodology (COI: 5/6 MS/GitHub authors); DX Core 4: D (COI: vendor) | era-independent; DX AI ext E3-relevant | 3 |
| metr-2026-uplift | RQ1, RQ2 | C (self-declared unreliable wave; belief statement ≠ evidence) | E3 later-gen (no per-task tool split) | P1.1 |
| agents-vs-ides-2026 | RQ1, RQ3, RQ5 | A (DiD+PSM telemetry w/ counterfactuals; NOT an RCT; no CIs reported; LOC/commit outcomes are §5.7-suspect metrics) | E3 treatment; E2/E3 prior-exposure | P1.1 |
| dora-2026-roi | RQ4, RQ5 | D (COI: consulting-arm co-authorship; no new data; illustrative-only numbers — deliberate downgrade from DORA-brand B) | mixed, inherits 2025 survey's pre-agentic weighting | P1.1 |
| he-2026-2x-mandate | RQ5, RQ1, RQ4 | A (staggered DiD, placebo tests; single unnamed firm; NOT independent of stanford-denisov-blanch — shared author) | E3 confirmed (Cursor, Claude Code, in-house agents) | P1.1 |
| faros-2026-whiplash | RQ5, RQ4 | D (COI: reverse-direction — alarm sells governance tooling; before/after design, confounders unaddressed) | E2/E3 blend; agentic authorship <1% of dataset | P1.1 |
| heilman-2026-microsoft | RQ1, RQ5, RQ6 | A (TWFE dose-response, placebo battery; intensity-only identification, no never-adopters; COI: 3/3 Microsoft, undisclosed) | E1/E2 (agent modes absent from telemetry — NOT the E3 comparator it's cited as) | P1.2 |
| agoda-2026-bottleneck | RQ5 | C weak-end (named org, no vendor COI — but zero own numbers; mechanism corroboration only, cannot carry numeric claims; InfoQ's "Agoda numbers" are actually Faros's) | E3 confirmed | P1.2 |
| churn-151-repos-2025 | RQ3 | A (RDD + placebos, peer-reviewed TSE; within-repo counterfactual; clean independence) | E1/E2 (explicitly disclaims Claude Code-era tools) | P1.2 |
| shen-2026-coding-skills | RQ3, RQ4, RQ6 (skill-formation theme) | A-candidate (RCT n=52; small N, single session; COI: Anthropic reputational, tested GPT-4o not Claude) | E2 chat — NOT agentic; era-transfer caveat applies | P1.2 |
| dx-reock-2026 | RQ5, RQ1 | D (COI: reverse-direction, measurement vendor; near-zero methodology disclosure) | E2/E3 blend, unsplit | P1.2 |

## Queued
| source_id / search target | RQ | priority |
|---|---|---|
| METR 11 May 2026 AI usage self-report survey (metr.org/blog/2026-05-11-ai-usage-survey/) — direct tension-1/RQ2 material | RQ2 | high |
| METR "forthcoming" autonomous-agent evidence (per arXiv:2507.09089 §4.1) — search target | RQ1 | medium |
| METR critiques roundup (Zvi Mowshowitz; The Experimentalist) | RQ2 | medium |
| MIT NANDA "GenAI Divide" report — shadow-AI critique (via dora-2026-roi leads) | RQ3 | medium |
| DORA 2025 critiques/analyses (RedMonk, InfoQ, getDX) | RQ2, RQ5 | medium |
| DORA 2026 annual report — re-check September 2026 (does not exist as of Jul 2026) | RQ5 | note |
| arXiv 2606.21804 "Is Agent Code Less Maintainable Than Human Code?" — direct E3 quality test | RQ3 | high |
| arXiv 2603.28592 "Debt Behind the AI Boom" | RQ3, RQ4 | medium |
| GitClear Jan 2026 "Top Performers" piece | RQ1 | low |
| Hoffmann, Boysel, Nagle, Peng & Xu (2025) HBS WP 25-021 "Generative AI and the Nature of Work" — task-allocation quasi-experiment | RQ1 | medium |
| Denisov-Blanch Dec 2025 "inflection point" artefact + ASE 2026 repo-AI-config paper — search targets | RQ3, RQ5 | medium |
| "Ghost engineers" critiques (Jellyfish, HN) — anti-metrics material on the Stanford model | RQ2, RQ6 | low |
| OpenAI/NBER "How People Use ChatGPT" (WP 34255) — comparable vendor usage index, Tier D baseline | RQ1 | low |
| Economic Index methodology critiques (Strauss; Empiricrafting) | RQ2 | low |
| Stack Overflow 2026 survey results — re-check ~Q4 2026 (collection opened 23 Jun 2026, no results yet) | RQ2 | note |
| SO "Closing the developer AI trust gap" post (Feb 2026) | RQ2, RQ6 | low |
| Stray et al. (HICSS 2026) — independent 2-yr NAV IT longitudinal: null commit-activity change, perception ≠ measured | RQ2, RQ5 | high |
| arXiv 2506.10051 — brownfield student study | RQ3 | medium |
| E3-era seniority evidence hunt — does the junior-gains pattern reverse under agentic tools? (Pragmatic Engineer etc., Tier C/D) | RQ1, RQ3 | high |
| arXiv 2504.11436 "Shifting Work Patterns with Generative AI" (Microsoft) | RQ1 | medium |
| arXiv 2509.20353 — Copilot longitudinal case study | RQ2, RQ5 | medium |
| AIDev dataset paper (arXiv 2602.09185) — provenance/independence check: many MSR 2026 agentic-PR studies share this one dataset, which caps their triangulation value | RQ2 | high |
| arXiv:2510.24265 "The Fast and Spurious: Developer Productivity with GenAI" | RQ2 | medium |
| arXiv:2601.20112 "Usage, Effects and Requirements for AI Coding Assistants in the Enterprise" | RQ1, RQ4 | medium |
| GitHub/Accenture Nov 2024 counter-research (Tier D; side B of the defect-rate contradiction) | RQ3 | medium |
| CodeRabbit Dec 2025 review-quality report (~1.7x issues in AI-coauthored PRs; Tier D) | RQ3, RQ4 | medium |
| arXiv 2510.10165 — AI-assisted programming and technical-debt/maintenance burden | RQ3, RQ4 | medium |
| — E3 sweep, code review (T7): Cloudflare "AI Code Review at scale" (C, E3, real cost data) | RQ1, RQ4 | high |
| — arXiv 2604.03196 "From Industry Claims to Empirical Reality" code-review agents, MSR 2026 (B, E3) | RQ1, RQ2 | high |
| — arXiv 2605.02273 "These Aren't the Reviews You're Looking For" — most AI PRs unreviewed or AI-reviewed (B, E3) | RQ5, RQ3 | high |
| — arXiv 2605.22534 why agentic PRs merge/reject, MSR 2026 (B, E3) | RQ3 | medium |
| — arXiv 2601.21276 "More Code, Less Reuse" — redundancy up, reviewer sentiment up (B, E3) | RQ2, RQ3 | medium |
| — GitHub blog "Agent pull requests are everywhere" (D, E3; 60M+ Copilot reviews claim) | RQ5 | medium |
| — Microsoft devblog AI-powered code reviews rollout (D, E3) | RQ1 | low |
| — E3 sweep, incident response (T8): Zalando 2-yr postmortem analysis, ~10% surface-attribution error (C, E3) | RQ3 | high |
| — arXiv 2601.22208 "Stalled, Biased, and Confused" RCA reasoning failures, 48k scenarios (A/B, E3) | RQ3 | high |
| — arXiv 2604.12108 Google Auto-Diagnose test-failure RCA, ICSE-SEIP 2026 (B/C, COI, E3) | RQ1 | medium |
| — Datadog LLM postmortem pipeline (D, E3) | RQ1 | medium |
| — E3 sweep, agent-code quality/security: arXiv 2605.06464 agent-code maintenance (B, E3) | RQ3 | high |
| — arXiv 2601.15195 failed agentic PRs taxonomy (B, E3) | RQ3 | high |
| — arXiv 2605.29442 developer-agent misalignment, 20,574 sessions (B, E3) | RQ3 | high |
| — arXiv 2606.14796 tech-debt multivocal review (B, E2/E3) | RQ3 | medium |
| — Amazon Mar 2026 AI-linked outages + 90-day safety reset (C journalism; causation contested by Amazon) | RQ3, RQ5 | medium |
| — GitLab AI Accountability Report 2026 "AI Paradox" survey (D, E3, self-reported) | RQ5, RQ2 | medium |
| — Opsera 2026 benchmark (D; headline %s lack methodology — cautious full read only, never cite headline alone) | RQ3 | low |
| Agoda CTO Zalzberg interview (Tech Wire Asia) — actual Agoda numbers (~27% uplift, 1–6 hrs/wk saved), different spokesperson/topic from Stern post | RQ1, RQ5 | medium |
| — Zendesk "absorption capacity" via InfoQ (C, E3; chase primary) | RQ5 | high |
| — E3 sweep, agentic controlled/mining studies: arXiv 2511.04427 "Speed at the Cost of Quality" Cursor DiD, MSR 2026 (B, E3) | RQ3, RQ5 | high |
| — arXiv 2602.08915 task-stratified agent PR acceptance: Devin 42.9% vs Codex 81.6%, MSR 2026 (B, E3) | RQ1, RQ3 | high |
| — arXiv 2605.23135 Vella & Blincoe 2-wave longitudinal: 84% self-report gains vs rising cognitive load (B, E3) | RQ2 | high |
| — arXiv 2605.20049 code-cleanliness minimal-pair, Claude Code: token use −7–8% (B, E3) | RQ3, RQ4 | high |
| — arXiv 2509.14745 agentic PRs on GitHub: 83.8% merge rate (B, E3) | RQ1 | medium |
| — arXiv 2604.13108 architecture descriptors as agent navigation (B, E3) | RQ1, RQ3 | medium |
| — arXiv 2606.13298 architectural quality under agentic adoption, DiD 151 Java repos (B, E3) | RQ3 | medium |
| — arXiv 2602.00164 why fix-related agentic PRs stay unmerged (B, E3) | RQ3 | medium |
| — arXiv 2605.04779 meta-analysis GenAI programming productivity 2019–2025, g=0.33 (B, mixed era) | RQ1 | medium |
| — E3 sweep, rollouts/postmortems: Salesforce eng blog — Cursor legacy test coverage, 26→4 eng-days/repo (C, E3) | RQ4, RQ5 | high |
| — Pragmatic Engineer "AI Tooling for Software Engineers in 2026" survey, n=906 (C, E3, self-report) | RQ1, RQ2 | high |
| — Uber Claude Code budget burn (Forbes/The Information; $150–2,000/eng/mo, 84% adoption) (C/D, E3) | RQ4 | high |
| — Replit agent production-DB deletion + fabrication postmortem (C, E3) | RQ3 | high |
| — QCon London 2026 Böckeler keynote: cost escalation 12¢/100 lines → ~$91k/yr (C, E3) | RQ4 | high |
| — Cursor vendor case-study set (Coinbase 90% idea→prod, Faire 2x PRs, NVIDIA 3x commits, Salesforce 30%) — triangulation pair with Salesforce eng blog (D, COI, E3) | RQ1, RQ5 | medium |
| — Grigorev first-hand postmortem: Claude Code + Terraform dropped production DB (C, E3) | RQ3 | medium |
| — AWS Kiro 13-hr Cost Explorer outage (D secondary; "user error" framing suspect; 1,500-eng petition) | RQ3 | medium |
| — Anthropic Apr 2026 Claude Code quality postmortem (D, COI, E3) | RQ3 | medium |
| — Pragmatic Engineer "How Claude Code Is Built" + Wolff QCon talk (C/D; Anthropic self-report, 90% Claude-written claim) | RQ1 | low |
| — arXiv 2508.00178 "The SPACE of AI" — SPACE co-author's AI-era follow-up (Jul 2025) | RQ6 | high |
| Shen-Tamkin OSF data pull — resolve absolute quiz-percentage discrepancy ("50% vs 67%" announcement vs ~64/80% in paper fetches) before any exec-brief use | RQ6 | low |
| Dedicated skill-formation/cognitive-debt search sweep (theme approved in v0.4; current sources found incidentally) | RQ4, RQ6 | medium |
| DX/Tacho study (121,000 devs / 450+ companies) — check overlap/redundancy vs dx-reock-2026 | RQ1 | medium |
| arXiv 2502.15287 "Time Warp" (Microsoft, ICSE-SEIP 2025 Distinguished Paper) — actual source of coding-time share: ~11% actual / ~20% ideal (Noda's "16%" is a misquote — never propagate it) | RQ6 | medium |
| — [colleague] arXiv 2605.01160 "Productivity-Reliability Paradox" — single-author MLR of 67 sources + 4-mo pilot; synthesis cross-check only | RQ5 | medium |
| — [colleague] Orosz "Slow down to speed up" talk (C, E3; get transcript via yt-dlp) | RQ1, RQ5 | medium |
| — [colleague] HBR "Psychological Costs of Adopting AI" (May 2026) — general workforce, not SWE; chase its underlying studies | RQ4 | low |
| — Storey "cognitive debt" concept (via tomwojcik post) — RQ6 vocabulary/instrument lead | RQ6 | low |

## Blocked
| source_id | reason | needs |
|---|---|---|
| stanford-denisov-blanch (residual only — RESOLVED for all spoken figures via yt-dlp transcripts of both talks) | slide-only figures remain audio-unverifiable: team quartile split, 4.8%→19% widening-gap number, ~30–100h learning curve (origin now unknown — do not cite as talk-confirmed); "7–9% Copilot-class" absent from both transcripts, likely secondary-source error | OPTIONAL, low priority: human skim of slides/video visuals; otherwise treat slide-only figures as secondary-sourced |
| space-dx-core4 (SPACE primary-text upgrade only — record built from convergent secondaries + verified abstract) | ACM-family domains (queue.acm.org, cacm.acm.org, dl.acm.org) all 403 the fetch tool — likely bot-blocking, not a paywall; no preprint exists | human to open queue.acm.org/detail.cfm?id=3454124 in a browser and confirm free readability (then upgrade to full primary read) |

## Rejected (triage)
| source | one-line reason |
|---|---|
| [colleague] James Shore "You Need AI That Reduces Maintenance Costs" (May 2026) | credible practitioner, but hypothetical numbers by the author's own admission — framing lens for RQ4 synthesis, not evidence |
| [colleague] terriblesoftware.org "Using my fucking brain" (May 2026) | personal anecdote, no data — cognitive-debt cluster colour only |
| [colleague] siddhantkhare.com "AI fatigue is real" (2026) | personal essay, two-week self-log only, no data — same cluster |
| [colleague] tomwojcik.com "What AI coding costs you" (Feb 2026) | essay; its citable evidence (Shen-Tamkin RCT, Storey cognitive debt) captured directly in Queued |
| [colleague] arXiv 2506.08872 "Your Brain on ChatGPT" (essay-writing EEG) | out of SDLC scope; per PROTOCOL v0.4 (approved) admissible as era-independent mechanism background only — never carries an SWE claim |

## RQ status
RQ1: OPEN | RQ2: OPEN | RQ3: OPEN | RQ4: OPEN | RQ5: OPEN | RQ6: OPEN

## Batch log
- 2026-07-06 phase-1 batch 1 (P1.1): five top-priority E3 sources extracted (metr-2026-uplift, agents-vs-ides-2026, dora-2026-roi, he-2026-2x-mandate, faros-2026-whiplash). The E3 evidence picture sharpened considerably: he-2026-2x-mandate is now the strongest E3 source (Tier A DiD; causal throughput 1.46–1.72x, review coverage 89%→68%, token spend 20x — but single firm, shares an author with Stanford so no independent triangulation); agents-vs-ides-2026 corrected our Phase 0 flag (NOT an RCT — DiD+PSM) and adds non-vendor telemetry for the quality-debt tension (+18% warnings, +39% complexity, persistent); metr-2026-uplift bounds the −19% anchor without updating it (wave self-declared unreliable, Tier C); dora-2026-roi downgraded to D (consulting co-production, J-curve is analogy not measurement — "reframe not resolution" added to tension 3); faros-2026-whiplash verified but design is functionally before/after with unaddressed confounders, agentic authorship <1% of its dataset. New provisional contradiction: Faros vs DX/Reock on throughput-gain magnitude (tension 6). Grading discipline note: two brand-name sources (DORA interim, Faros) both required D grades against brand expectations; the MSR 2026 AIDev-dataset cluster shares provenance, capping triangulation counts.
- 2026-07-06 phase-0 batch 3: final anchors verified (dora-2024, space-dx-core4) + all five §6 E3 search directives executed as two triage sweeps. dora-2024: full PDF read; sign-framing correction (primary says delivery *stability* −7.2%, DORA 2025's paraphrase inverted the construct name); 2024's own metric restructuring (new rework-rate item in the stability factor) confirms the RedMonk comparability critique — the 2024→2025 flip has three live explanations. space-dx-core4: DX Core 4 speed metric is "Diffs per Engineer" (Diff Authoring Time is Meta's, unrelated); SPACE primary blocked by ACM 403 (likely bot-block — human browser check requested). Sweeps: no new true agentic RCTs exist (field converged on PR-mining/DiD, Tier B — scarcity consistent with §8); incident-response literature thin as predicted; bottleneck-displacement was the richest directive with Agoda/Zendesk/Faros/GitLab converging on review/absorption-capacity displacement; four genuine E3 postmortems found (Replit, Grigorev, AWS Kiro, Anthropic). Search notes: MSR 2026 + the AIDev dataset are hubs for agentic-PR studies; incident/failure-language queries ("deleted database", "postmortem", "rolled back") massively outperform rollout-language queries for Tier C postmortem material — treat as a standing search lane; SEO content mills poison "AI code security statistics" queries — reject anything untraceable to a named methodology.
- 2026-07-06 phase-0 batch 2: five pre-agentic anchors verified (google-rct-2024, stackoverflow-survey-2025, peng-2023-copilot-rct, cui-2024-copilot-field, uplevel-2024). All confirmed E1 or E1/E2 — baseline/methodology value only, per the era transfer rule. Material corrections: Google's famous "21% faster" is the non-significant model estimate (p=.086; a different spec gives ~26% significant); Peng's 55.8% carries a wide CI [21%, 89%] and was never peer-reviewed; Cui is now peer-reviewed (Mgmt Sci Feb 2026), 26.08% PRs confirmed, seniority gains directional-only (ns), era corrected E1-only, plus a measured build-success decline (−17.4% Accenture) the seed omitted. Two contradictions logged: perception-gap direction reverses between Peng (underestimate) and METR (overestimate); Uplevel +41% bugs (D) vs GitHub/Accenture counter-research (D, queued). SO 2026 survey is collection-only until ~Q4 2026. Search note: author-hosted/MIT-hosted preprint PDFs + pdftotext beat WebFetch on garbled text layers; SSRN 403s.
- 2026-07-06 phase-0 batch 1: five E3-anchor verifications done (metr-2025-rct, dora-2025, gitclear-2025, stanford-denisov-blanch, anthropic-economic-index). Headline outcome: the seed list survives but its era framing was optimistic — only METR is genuinely (early-)E3; Stanford's quadrant figures are talk-published E1/E2-mixed, GitClear 2025 is E1/E2 trendline, DORA 2025 respondents are 61% agent-mode-never. Two contradictions logged (GitClear churn vs arXiv 2507.10422; DORA 2024→2025 throughput flip with instability persisting). Two Blocked items need human input (Stanford talk videos; GitClear 2026 email gate). Strong new E3 leads queued: METR Feb 2026 update, arXiv 2607.01904 (2x-mandate diff-in-diff), DORA 2026 ROI interim, arXiv 2606.21804. Search-strategy note: arXiv preprints and vendors' own S3-hosted PDFs beat landing pages; secondary write-ups repeatedly misquote effect sizes (METR CI misquote; Stanford headline number varies by write-up) — always pull primary numbers.
- 2026-07-06 setup (2): protocol v0.3 — reweighted toward practitioner evidence: Tier C is the expected volume centre, ≥3 independent Tier C sources can carry an exec-brief claim (medium confidence cap), Tier C hunting grounds and practitioner query variants added. Few formal papers expected; that is by design, not a gap.
- 2026-07-06 setup: protocol v0.2 adopted (renamed to PROTOCOL.md; per-source commits; era-by-modality; preprint rule; TSV schema + era/measurement_basis columns; §6.5 query plans; saturation rule disambiguated; DoD scarcity clause; RQ4 expectation pre-registered). Repository initialised, scaffolding created. No research batches yet — Phase 0 not started.
