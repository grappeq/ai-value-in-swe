# Source: agent-code-maintenance-2026

## Identity (verified, not assumed)

- **Title:** "To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study"
- **Authors:** Shota Sawada, Tatsuya Shirai, Yutaro Kashiwa, Ken'ichi Yamaguchi, Hiroshi Iwata, Hajimu Iida
- **Affiliations:** National Institute of Technology, Nara College (Japan); Nara Institute of Science and Technology (Japan)
- **arXiv ID:** 2605.06464 (v2, 9 May 2026; v1 7 May 2026)
- **Venue:** Accepted to the 30th International Conference on Evaluation and Assessment in Software Engineering (EASE 2026, Glasgow, June 2026) — a peer-reviewed empirical-SE venue, not a preprint-only/unreviewed drop
- **Funding:** JSPS KAKENHI (JP24K02921, JP25K03100), JST PRESTO (JPMJPR22P3), ASPIRE (JPMJAP2415), CREST (JPMJCR23M1, JPMJCR26X7) — all Japanese public science-funding bodies. No vendor or consultancy funding declared. No COI statement beyond implicit absence of one.
- **Full text obtained:** arxiv.org/html/2605.06464 (HTML full text), cross-checked against a second independent fetch of the same URL with different extraction prompts (abstract quote, Table 1 quote, RQ3 quote, section headings all matched consistently across both fetches — no internal contradiction found, so treating as a genuine full-text read, not an abstract-only skim).

**Original ledger guess vs verified reality:** guess was "tier ~B, era E3, feeds RQ3." Verified as: **Tier B confirmed**, **era E3 confirmed**, but the source is *broader* than RQ3 alone — it primarily produces cost/maintenance-burden data (RQ4-relevant) and a value/failure-map data point (RQ1/RQ3), and bears directly on §5 tension 4 (quality debt) and tension 6 (bottleneck displacement).

## What the paper actually is

An observational comparison of post-merge maintenance activity on AI-agent-generated files vs human-authored files, drawn from the **AIDev dataset** (Li et al., 2025) — 456,000+ PRs from five autonomous coding agents (OpenAI Codex, Devin, GitHub Copilot, Cursor, Claude Code) across ~61,000 repositories. The authors filtered to repos with >100 GitHub stars (2,807 candidates), then sampled 100 repositories, and from each sampled up to 10 AI-generated files and up to 10 human-generated files created in the same period. Final sample: **508 AI-generated files, 508 human-generated files, 3,238 total maintenance commits** (1,543 on AI files, 1,695 on human files) observed over a minimum six-month window (files created Dec 2024–Jul 2025, maintenance tracked through 31 Jan 2026).

AI authorship of a *file* was determined by whether the file was added by a commit whose committer name matched a known agent-bot identifier (`claude[bot]`, `Cursor Agent`, `Copilot`, `devin-ai-integration`). Codex was **excluded from analysis** because its commits could not be reliably attributed to a bot account — a real gap given Codex is one of the five agents in the parent dataset.

Maintenance-commit *type* was classified using an existing automated tool, the "Conventional Commits Classification System" (CCS), reported elsewhere at **77.95% precision** — i.e. roughly 1 in 5 category labels in Table 1 may be wrong. The paper does not report recall or a confusion matrix, and does not manually validate a sample of the automated labels itself.

No inferential statistics anywhere in the paper: no significance tests, no p-values, no confidence intervals, no regression/effect-size modelling. All results are raw counts, percentages, and violin-plot visualisations of distributions. This caps the tier at B rather than A regardless of sample size, per PROTOCOL §3 (Tier A requires RCT/controlled-experiment/telemetry-with-counterfactual; this is telemetry without a counterfactual or randomisation).

Critically, **task assignment was not randomised**: which files/tasks a repo maintainer routed to an AI agent vs handled themselves is entirely due to real-world developer choice, and the authors themselves flag this as a threat: "developers may avoid AI for critical files or apply it only in specific cases." This means every AI-vs-human comparison in the paper is confounded by self-selection — a plausible reading is that agents were routed toward lower-stakes, self-contained files, which would independently explain both "less maintenance needed" and "fewer bug-fix commits" without implying AI code is more maintainable in a like-for-like sense.

## Grading

- **Tier:** B (structured observational / telemetry without randomisation or counterfactual; decent sample size — 508+508 files, 100 repos — and a real, matched-context design comparing AI vs human files from the *same repo* and *same time window*, which is better than most Tier C practitioner write-ups, but it stops short of Tier A because of the self-selection confound and complete absence of inferential statistics)
- **Era:** E3 (agentic). All five source tools (Codex, Devin, Copilot-agent, Cursor, Claude Code) are autonomous PR-generating agents, not autocomplete or chat-panel tools. This is squarely the tool modality PROTOCOL §2 defines as E3.
- **Independence:** Independent academic authors, publicly funded, no vendor/consultancy money, no declared COI. No COI flag needed (this is not a Tier D source).
- **Population:** 508 AI-generated files / 508 human-generated files, 100 popular open-source GitHub repositories (>100 stars), 3,238 total maintenance commits. No developer-seniority data — the unit of analysis is files/commits, not individual developers, so no seniority split is possible from this source.
- **Codebase context:** open-source, "popular" (>100-star) repositories only — external validity to closed-source enterprise/production codebases is untested and plausibly limited; OSS contributor norms and review culture differ from internal enterprise engineering.
- **What this source can support:** a description of the *volume and type* of post-merge maintenance work generated by agent-authored code in popular OSS repos, and a data point that humans still perform the large majority (83–93%) of that maintenance regardless of who wrote the original file.
- **What this source cannot support:** any causal claim that AI-generated code is "more maintainable" or "lower quality debt" than human code — the self-selection confound, the absence of complexity/criticality controls, and the absence of any inferential statistics rule that out. It also cannot speak to enterprise/brownfield/closed-source contexts, to individual developer productivity, or to cost in money/time/tokens (none reported).

## Extraction records

### Finding 1 — AI-generated files receive markedly less maintenance activity in month 1, gap narrows over time
**RQ tag:** RQ1, RQ3, §5-tension-4 (quality debt)
**Metric:** commit count per file per month (relative to file-creation month)
**Effect size (as reported):** "AI-generated files exhibited approximately half the commit count of human-generated files during the first month." No exact counts, medians, or CIs are given in the text — the underlying data is shown only as a violin plot (Figure 2a) with no accompanying summary statistics. "From the fourth month onward, the gap with human-generated files narrows."
**Direction:** AI-generated files receive less maintenance (fewer commits) than human-generated files, most sharply in the first month; the gap shrinks by month 4+.
**Measurement basis:** measured (git commit telemetry), not self-reported.
**Quality note:** Qualitative claim ("approximately half") not backed by an exact number in the prose — this is a description of a graphic, not a reportable point estimate. Treat as directional only.

### Finding 2 — AI-generated files see smaller-magnitude changes per maintenance commit
**RQ tag:** RQ1, RQ3
**Metric:** percentage of file lines changed per commit (normalised by file size)
**Effect size (as reported):** "Human-generated files exhibit a larger magnitude [of change] compared to AI-generated files... The smaller magnitude of changes in AI-generated files implies that maintenance is often limited to minor changes or slight modifications." Again, no exact median/mean percentage is given in the prose; only a violin-plot distribution (Figure 2b) and a decreasing-trend statement. "A decreasing trend was observed in the modification ratio of AI-generated files [over time]."
**Direction:** AI-generated files undergo smaller, shallower edits than human files when they are touched at all.
**Measurement basis:** measured (git diff line counts).
**Quality note:** Same limitation as Finding 1 — no point estimate, graphic-only. Cannot be cited with a number; only the direction and qualitative size ("minor") are usable.

### Finding 3 — Maintenance-commit type distribution differs: AI code skews to feature extension, human code skews to bug-fix and docs
**RQ tag:** RQ1, RQ3, §5-tension-4 (quality debt/refactor-rate proxy)
**Metric:** % of maintenance commits by Conventional-Commits category (Table 1), out of 1,543 AI-file commits and 1,695 human-file commits
**Effect size (exact, as reported):**
- `feat`: AI 21.78% (336/1,543) vs Human 15.10% (256/1,695) — diff +6.68 pp
- `fix`: AI 11.73% (181/1,543) vs Human 16.76% (284/1,695) — diff −5.03 pp
- `docs`: AI 10.76% (166/1,543) vs Human 16.22% (275/1,695) — diff −5.46 pp
- `refactor`: AI 14.19% (219/1,543) vs Human 15.10% (256/1,695) — diff −0.91 pp
- `chore`: AI 13.35% (206/1,543) vs Human 11.50% (195/1,695) — diff +1.85 pp
- `build`: AI 10.05% (155/1,543) vs Human 8.02% (136/1,695) — diff +2.03 pp
- `test`: AI 6.09% (94/1,543) vs Human 6.31% (107/1,695) — diff −0.22 pp
- `ci`: AI 4.47% (69/1,543) vs Human 4.54% (77/1,695) — diff −0.07 pp
- `style`: AI 4.86% (75/1,543) vs Human 3.95% (67/1,695) — diff +0.91 pp
- `perf`: AI 2.01% (31/1,543) vs Human 2.24% (38/1,695) — diff −0.23 pp
**Direction:** AI-generated files' post-merge maintenance is disproportionately feature-extension work; human-generated files' maintenance is disproportionately bug-fixing and documentation work.
**Measurement basis:** measured, but via an automated classifier at only 77.95% precision (no recall figure, no manual spot-check reported) — treat percentages as approximate, not exact ground truth.
**Quality note:** Largest and second-largest deltas (feat +6.68pp, docs −5.46pp, fix −5.03pp) are the headline result; the smaller categories (test, ci, perf, style) show near-zero differences and should not be over-read as findings.

### Finding 4 — Human developers perform the large majority of maintenance on AI-generated files, though AI agents do more of their "own" files' upkeep than they do of human files
**RQ tag:** RQ3 (primary), §5-tension-6 (bottleneck displacement — humans still absorb the bulk of downstream work), RQ4 (cost — proxy for human-effort share)
**Metric:** % of maintenance commits attributed to human vs AI-agent committer, split by whether the original file was AI- or human-authored
**Effect size (exact, as reported):**
- On AI-generated files (n=1,543 maintenance commits): humans made 83.21% (1,284), AI agents made 16.79% (259)
- On human-generated files (n=1,695 maintenance commits): humans made 92.98% (1,576), AI agents made 7.02% (119)
**Direction:** AI agents are ~2.4x more likely to be the committer of a maintenance change on a file they originally wrote (16.79%) than on a human-authored file (7.02%) — but in absolute terms, humans still do the overwhelming majority of maintenance in both cases.
**Measurement basis:** measured (committer-identity telemetry).
**Quality note:** No cost/time/token data accompanies this — it is a share of *commit count*, not a share of *effort*; a single human commit could represent far more or less work than a single AI commit. Cannot be used to estimate reviewer-hours or licence-cost offset.

### Finding 5 (methodological caveat, recorded per Evidence Rule 3) — Comparison is confounded by non-random task assignment; authors flag this themselves
**RQ tag:** cross-cutting — affects how much weight Findings 1–4 can carry for RQ1/RQ3/RQ5
**What was found:** The study does not randomise which files/tasks go to an AI agent vs a human; this is left to real-world developer/maintainer choice in each of the 100 sampled repos. The authors' own threats-to-validity section states: "File importance and intended usage are also uncontrolled: developers may avoid AI for critical files or apply it only in specific cases," and separately note the dataset window ("first six months after agentic coding tools were released") likely captures "early adopters prioritizing feature development over maintenance" rather than steady-state usage.
**Direction/status:** This is a **negative/limiting result about the study's own design**, not a finding about AI code quality — recorded per Evidence Rule 3 (record nulls/negatives with equal diligence). It materially weakens any causal reading of Findings 1–3: "less maintenance + fewer bug-fix commits" is equally consistent with "agents write more maintainable code" and with "agents were only ever assigned simpler, lower-stakes, non-critical files in the first place."
**Measurement basis:** N/A (methodological/design observation, author-acknowledged).

### Finding 6 (methodological caveat, recorded per Evidence Rule 3) — No inferential statistics reported anywhere in the paper
**RQ tag:** RQ2 (measurement methods) — bears on how much trust to place in this source's numbers generally
**What was found:** All results in the paper (Findings 1–4 above) are descriptive: raw counts, percentages, and unlabelled violin-plot distributions. No significance testing, no confidence intervals, no regression controlling for file size/complexity/repo, no effect-size statistics (Cohen's d, odds ratios, etc.) are reported anywhere in the text.
**Direction/status:** Negative finding about evidentiary strength, recorded per Evidence Rule 3. Every percentage-point difference in Finding 3, for example, is presented without any indication of whether it is distinguishable from sampling noise at n≈1,500–1,700 commits per group.
**Measurement basis:** N/A (methodological observation).

## Cross-reference notes (against protocol tensions, not against other sources — this run did not read LEDGER.md or other source files per blind-extraction rules)

- **§5 tension 4 (quality debt / GitClear churn-duplication):** this source is a *partial counter-signal* to "AI code needs more rework" — it finds AI files need proportionally *fewer* fix commits and less overall maintenance volume than human files. But per Finding 5, this reading is confounded by task self-selection, so it should not be presented as contradicting GitClear's churn/duplication findings without that caveat — they may not even be measuring the same construct (GitClear measures churn/duplication in the code itself; this paper measures commit-count/type on the file post-merge).
- **§5 tension 6 (bottleneck displacement):** Finding 4 is directly relevant — even for the tool-generated files, ~83% of downstream maintenance commits are made by humans, not agents. This is consistent with (but does not prove, given no time/effort data) a bottleneck-displacement story: agents may generate code fast, but the human maintenance burden does not disappear, it just changes composition (more feature-extension, less bug-fixing, per Finding 3).
- **RQ4 (cost profile):** this source contains no licence/token/time cost data at all — it is a pure commit-count/type study. It cannot fill the RQ4 evidence gap beyond the indirect "83% of maintenance commits are human-authored" share-of-commits proxy (Finding 4), which is not effort-normalised.

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
agent-code-maintenance-2026	2026	B	E3	observational telemetry, matched-repo/time-window comparison, no randomisation	508 AI-generated files vs 508 human-generated files, 100 OSS repos (>100 stars), 3238 maintenance commits, AIDev dataset (5 agents: Codex/Devin/Copilot/Cursor/Claude Code; Codex excluded from attribution)	T4,T5	commits per file per month (frequency)	"approximately half the commit count" of human files in month 1; gap narrows from month 4+	AI files receive less maintenance, narrowing over time	measured	none reported	not measured (file/commit-level unit, not developer-level)	popular open-source GitHub repos, PRs Dec 2024-Jul 2025, tracked to Jan 2026	independent academic, JSPS/JST-funded, no vendor COI	no exact point estimate given, graphic-only (violin plot), non-randomised task assignment confounds interpretation	4
agent-code-maintenance-2026	2026	B	E3	observational telemetry, matched-repo/time-window comparison, no randomisation	508 AI-generated files vs 508 human-generated files, 100 OSS repos (>100 stars), 3238 maintenance commits	T4,T5	% of file lines changed per maintenance commit (magnitude)	human files show "larger magnitude" of change than AI files; decreasing trend over time for AI files; no exact % given	AI files undergo smaller/shallower edits than human files	measured	none reported	not measured	popular open-source GitHub repos, PRs Dec 2024-Jul 2025, tracked to Jan 2026	independent academic, JSPS/JST-funded, no vendor COI	no exact point estimate, graphic-only (violin plot); cannot be cited with a number	3
agent-code-maintenance-2026	2026	B	E3	observational telemetry, automated Conventional-Commits classifier (77.95% precision, no recall reported)	1543 AI-file maintenance commits vs 1695 human-file maintenance commits, 100 OSS repos	T4,T5,T6,T10	% of maintenance commits by type (feat/fix/docs/refactor/etc, Table 1)	feat: AI 21.78% vs Human 15.10% (+6.68pp); fix: AI 11.73% vs Human 16.76% (-5.03pp); docs: AI 10.76% vs Human 16.22% (-5.46pp); refactor: AI 14.19% vs Human 15.10% (-0.91pp)	AI-file maintenance skews to feature extension; human-file maintenance skews to bug-fix and documentation	measured (automated classifier, 77.95% precision)	none reported	not measured	popular open-source GitHub repos, PRs Dec 2024-Jul 2025	independent academic, JSPS/JST-funded, no vendor COI	classifier precision only 77.95%, no manual validation reported; no significance testing on the pp deltas	4
agent-code-maintenance-2026	2026	B	E3	observational telemetry, committer-identity attribution	1543 AI-file maintenance commits, 1695 human-file maintenance commits, 100 OSS repos	T4,T5	% of maintenance commits made by human vs AI-agent committer	on AI-generated files: human 83.21% (1284/1543), AI 16.79% (259/1543); on human-generated files: human 92.98% (1576/1695), AI 7.02% (119/1695)	humans perform large majority of maintenance in both cases; AI agents ~2.4x more active maintaining their own files than human-authored files	measured	none (share of commit count, not effort/time/cost)	not measured	popular open-source GitHub repos, PRs Dec 2024-Jul 2025, tracked to Jan 2026	independent academic, JSPS/JST-funded, no vendor COI	commit-count share is not effort-normalised; cannot estimate reviewer-hours or cost offset from this alone	4
agent-code-maintenance-2026	2026	B	E3	author-acknowledged design limitation, non-randomised task assignment	100 OSS repos, developer/maintainer discretion over AI vs human task routing	T4,T5	N/A - methodological/design finding	authors state developers "may avoid AI for critical files or apply it only in specific cases"; dataset window captures "early adopters prioritizing feature development over maintenance"	self-selection confound weakens causal reading of all frequency/magnitude/type findings in this source	N/A (design observation)	none	not measured	popular open-source GitHub repos, PRs Dec 2024-Jul 2025	independent academic, JSPS/JST-funded, no vendor COI	this is a null/negative finding about the study's own internal validity, recorded per evidence rule 3; materially caps confidence on Findings 1-3	5
agent-code-maintenance-2026	2026	B	E3	author-acknowledged absence of inferential statistics	full sample, 3238 commits total	T4,T5	N/A - methodological finding	no significance tests, CIs, or regression controls reported anywhere in the paper	all reported percentage-point differences (Table 1 etc.) are undifferentiated from sampling noise	N/A	none	not measured	popular open-source GitHub repos	independent academic, JSPS/JST-funded, no vendor COI	negative finding re: evidentiary strength, recorded per evidence rule 3; relevant to RQ2 (measurement-method trustworthiness)	3
