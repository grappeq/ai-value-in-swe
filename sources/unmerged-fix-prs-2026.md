# Source: Alam, Mondal & Roy (2026) — "Why Are AI Agent–Involved Pull Requests (Fix-Related) Remain Unmerged? An Empirical Study"

## Identity (verified from full text, not abstract alone)

- **Title (exact):** "Why Are AI Agent–Involved Pull Requests (Fix-Related) Remain Unmerged? An Empirical Study"
- **Authors:** Khairul Alam, Saikat Mondal, Banani Roy — all University of Saskatchewan, Canada
- **arXiv ID:** 2602.00164v1 [cs.SE] (cross-listed cs.AI), submitted 29 January 2026
- **Venue/status:** Accepted at **MSR '26** (23rd International Conference on Mining Software Repositories), 13–14 April 2026, Rio de Janeiro, Brazil. ACM ISBN 979-8-4007-2474-9/2026/04, DOI 10.1145/3793302.3793611. This is a peer-reviewed conference paper (5 pages), not a raw preprint-only submission — the arXiv posting is the accepted camera-ready/pre-proceedings version. No version-difference concerns; no preprint-substitution issue arose (Tier A/B preprint-substitution rule not needed — full text was directly accessible via arXiv PDF).
- **Funding/COI:** NSERC (Canada) + industry-stream NSERC CREATE in Software Analytics Research (SOAR). No vendor (GitHub/Microsoft/OpenAI/Anthropic/etc.) funding or authorship disclosed. **Not Tier D; no COI flag required.**
- **Replication package:** publicly available (Zenodo, cited as [14] in the paper).

## Dataset provenance (explicit — independence-critical)

The study does **not** collect its own PR corpus. It draws entirely on the **AIDEV-POP dataset** (Li, Zhang & Hassan, 2025, released November 2025, Zenodo DOI 10.5281/zenodo.16919272), which is explicitly the "AIDev: Studying AI Coding Agents on GitHub" dataset — i.e. **the same public AIDev agentic-PR dataset** referenced elsewhere in this project's evidence base (see `sources/aidev-dataset-2026.md`, not read here per blind-extraction rules, but its filename alone confirms this project already has an AIDev-dataset-based source). AIDEV-POP contains 33,596 total AI-authored PRs; this paper filters to **8,106 fix-related PRs** (a ~24% subset) authored by five agents.

**Independence flag (high priority):** any other source in this project's evidence base that is also built on AIDev/AIDEV-POP (in whole or in part) shares underlying data-generating process with this paper. They are **not independent observations** for triangulation purposes under PROTOCOL §3's "three independent Tier C sources" rule or general cross-referencing — a shared-dataset cluster should be treated as one data point, not several, regardless of how many papers mine it. The manual qualitative layer (326-PR failure-cause coding) is original work by these authors and is independent of other AIDev-based papers' framing, but the underlying PR population and outcome labels (merged/closed/open) are not.

The dataset's own provenance (how AIDev/AIDEV-POP identified "AI agent–authored" PRs, and what repositories/ecosystems it covers) is not restated in this paper — readers must consult the AIDev dataset paper itself. This paper does not report repository count, language/ecosystem breakdown, or repository maturity/size — a real limitation for RQ3/RQ5 (task-characteristic and brownfield/greenfield analysis) that this paper does not address.

## Grading

- **Tier: B** (structured observational / large-scale telemetry without randomisation). Rationale: 8,106-PR quantitative census is telemetry-scale but has no counterfactual or control condition (no comparison to human-authored fix PRs in the same repos, so agent vs. baseline merge rates cannot be inferred from this paper alone). The qualitative layer (326-PR stratified random sample, 95% CI / 5% margin of error, dual independent coding with Cohen's κ = 0.82 "substantial agreement," disagreements resolved by discussion) is methodologically solid practitioner-grade empirical work — well above ad hoc case study, but still observational, not experimental. Peer review at a recognised venue (MSR) adds credibility over an unreviewed preprint or vendor blog. **Does not qualify for Tier A** (no RCT, no controlled comparison group).
- **Era: E3 (agentic).** All five studied tools — OpenAI Codex, GitHub Copilot (agent mode), Devin, Cursor, Claude Code — are autonomous PR-generating coding agents operating in a submit → respond-to-review → iterate loop against real repositories, squarely matching the PROTOCOL §2 E3 definition. No E1/E2 modality mixing.
- **Independence:** Academic authors, no vendor sponsorship — independent of vendor interest. However, capped independence *relative to other AIDev-dataset-based sources in this project* (see above). Treat as one node in a shared-dataset cluster, not a fully independent corroboration.
- **Population:** 8,106 fix-related PRs (of 33,596 total AI-authored PRs in AIDEV-POP) across five agents: OpenAI Codex (4,338), GitHub Copilot (1,993), Devin (1,249), Cursor (411), Claude Code (115). Real-world GitHub repositories; specific repos/ecosystems/company sizes not disclosed in this paper. Qualitative subsample: 326 of 2,113 closed-but-unmerged PRs (stratification method not detailed beyond "randomly sample").
- **What this source can support:** directional, moderately confident claims about (a) how often AI-agent fix-PRs get merged vs abandoned across five specific tools as of the AIDEV-POP snapshot (Nov 2025), and (b) a structured taxonomy of *why* fix-PRs stall, with relative frequencies, at reasonable methodological rigour (inter-rater κ = 0.82).
- **What it cannot support:** causal claims about task characteristics driving failure (no codebase-context, language, or maturity breakdown given); comparison to human-authored PR merge/abandonment base rates (no control group); generalisation beyond the AIDEV-POP snapshot period; claims about developer/agent "seniority" (not applicable — no seniority dimension in this study); cost data (no token/dollar/reviewer-hours cost reported, only elapsed wall-clock time-to-merge).

## Full reading notes

### RQ1 — Integration outcomes and latency (n = 8,106 fix-related PRs)

Overall (Table 1, exact reproduction):

| Agent | Total PRs | Merged | Closed w/o merge | Open |
|---|---|---|---|---|
| OpenAI Codex | 4,338 | 3,539 (81.6%) | 616 (14.2%) | 183 (4.2%) |
| GitHub Copilot | 1,993 | 845 (42.4%) | 713 (35.8%) | 435 (21.8%) |
| Devin | 1,249 | 536 (42.9%) | 675 (54.0%) | 38 (3.0%) |
| Cursor | 411 | 281 (68.4%) | 84 (20.4%) | 46 (11.2%) |
| Claude Code | 115 | 66 (57.4%) | 25 (21.7%) | 24 (20.9%) |
| **Total** | **8,106** | **5,267 (65.0%)** | **2,113 (26.1%)** | **726 (8.9%)** |

Measurement basis: **measured** — outcome classification is a factual GitHub PR-state label (merged/closed/open) at time of data collection, not a survey or self-report. This is an objective telemetry measure, not perception data.

Time-to-merge (Fig. 1, box plot, log scale, hours; computed as closed_at − created_at for merged PRs only): no exact medians/IQRs are given in text, only a qualitative description — Codex shows the shortest and most tightly concentrated distribution; Copilot and Devin show broader distributions with heavier upper tails (longer, more variable delays). **No numeric effect size extractable beyond this qualitative ranking** — flagging as a quality/reporting gap: the paper does not tabulate median/IQR time-to-merge, only shows a figure.

### RQ2 — Failure-cause catalogue (qualitative sample: n = 326 of 2,113 closed-but-unmerged PRs; 95% CI, 5% margin of error; dual-coded, Cohen's κ = 0.82)

12 inductively-derived categories (Fig. 2, exact percentages/counts):

| Code | Category | % | n |
|---|---|---|---|
| R1 | Resolved by Another PR (RAPR) | 22.1% | 72 |
| R2 | Test Case Failures (TCF) | 18.1% | 59 |
| R3 | Incorrect or Incomplete Fixes (IIF) | 15.3% | 50 |
| R4 | Fix Rejected by Maintainers (FRM) | 4.9% | 16 |
| R5 | Deployment Failures (DF) | 3.1% | 10 |
| R6 | Build Failures (BF) | 2.1% | 7 |
| R7 | Low Priority or Obsolete Issue (LPO) | 8.0% | 26 |
| R8 | Incomplete Review Process (IRP) | 5.5% | 18 |
| R9 | Closed Due to Inactivity (CDI) | 9.2% | 30 |
| R10 | Closed Without Explicit Rationale (CWR) | 4.0% | 13 |
| R11 | No Review Conducted (NRC) | 4.6% | 15 |
| R12 | Other Reasons (OTH) | 3.1% | 10 |

Sums to 326/326 exactly. Measurement basis: **measured** via structured manual qualitative coding (not self-report; not survey — direct artefact analysis of PR description, code diff, review comments, commit history, closure context).

**Top two causes are the headline finding:** test-case failures (R2, 18.1%) and "resolved by another PR" (R1, 22.1%) are the two largest single categories — combined these two account for 40.2% of all unmerged-PR closures. Build failures (R6, 2.1%) and deployment failures (R5, 3.1%) are comparatively rare — the paper's own framing: "validation-related issues are more prevalent than build failures," i.e. agents more often produce something that compiles/deploys but fails correctness/test validation than something that fails to build at all.

### Author-paper's own three-bucket synthesis (stated in text, not just my aggregation)

The paper explicitly groups the 12 causes into three high-level buckets in its "Synthesis of Failure Causes" subsection:
- **Technical causes:** IIF, TCF, BF, DF (incorrect/incomplete fixes, failing tests, build/deploy failures) — limitations in agents' ability to generate fully correct, validation-ready fixes.
- **Process-related causes:** FRM, IRP, NRC, CWR, CDI (rejected after review, incomplete review, no review, no-rationale closure, inactivity) — breakdowns in review interaction, feedback handling, sustained engagement.
- **Priority-related causes:** RAPR, LPO (resolved elsewhere, deprioritised/obsolete) — redundancy and timing/prioritisation dynamics, not intrinsic technical flaws.

Arithmetic aggregation (my own sum of the paper's own category percentages, not separately stated as a summed figure by the authors): technical ≈ 38.6% (15.3+18.1+2.1+3.1), process-related ≈ 28.2% (4.9+5.5+4.6+4.0+9.2), priority-related ≈ 30.1% (22.1+8.0). Flagging this sum as **derived, not verbatim-stated** — the paper gives the bucket definitions and the per-category percentages but never states the three bucket totals as numbers.

### Agent-wise failure-cause breakdown (Table 2, closed-but-unmerged subsample only; n per agent: Claude 18, Copilot 148, Cursor 19, Devin 50, Codex 91 — sums to 326)

Selected agent-specific signatures (count / % within that agent's own unmerged cases):
- **OpenAI Codex** unmerged failures are dominated by **test case failures: 50/91 = 54.9%** — i.e. when Codex PRs do fail to merge, it is overwhelmingly a validation/correctness problem, not a process problem. Fix Rejected and Incorrect/Incomplete Fixes tie at 13/91 (14.3%) each as the next largest.
- **Devin** unmerged failures are dominated by **inactivity closures: 27/50 = 54.0%** — the paper interprets this as "challenges sustaining engagement during longer review cycles." This is the standout finding on abandonment (see below).
- **GitHub Copilot** unmerged failures are dominated by **resolved-by-another-PR: 47/148 = 31.8%** (note: body text states "31.7%" for this same figure — a minor internal rounding inconsistency in the paper itself between Table 2 and its prose; flagging as a quality note, not a substantive discrepancy). Incorrect/Incomplete Fixes is Copilot's second largest at 30/148 = 20.3%.
- **Cursor** unmerged failures are dominated by **closed without explicit rationale: 8/19 = 42.1%** — the largest closed-w/o-rationale share of any agent by a wide margin.
- **Claude Code** (smallest subsample, n=18): Resolved by Another PR 5/18 (27.8%) and Low Priority/Obsolete 4/18 (22.2%) are the top two; zero instances of test-case failures, incorrect/incomplete fixes, incomplete review, or fix-rejected recorded for Claude Code in this sample — but n=18 is a very small cell count, so absence of a category here should not be read as a strong null (wide plausible-range uncertainty at this sample size).

Measurement basis: **measured** (same manual-coding method as the overall RQ2 catalogue, just cross-tabulated by agent).

### Who abandons: agent-side vs reviewer/maintainer-side — explicit answer

The paper's 12-category taxonomy is **structurally reviewer/process-side**, not agent-initiated-abandonment-side: every category describes an outcome of the PR-review workflow (a maintainer decision, an automated inactivity timeout, a test/build system result, or another PR superseding it). The paper does **not** report a category for "the agent itself gave up / stopped responding to review feedback" as a distinct, directly-labelled cause — this is a gap, not a reported null.

The closest proxies to an abandonment/engagement-failure signal, both of which are ambiguous as to which party disengaged first:
- **CDI — Closed Due to Inactivity (9.2%, 30 PRs overall; but 54.0% of Devin's unmerged PRs specifically):** "no further updates within the project-defined time window," closed by repository automation. The paper does not disambiguate whether the agent stopped iterating, the maintainer stopped reviewing, or both. Given Devin's specific concentration here, and the paper's own interpretation ("challenges sustaining engagement during longer review cycles"), this reads as most plausibly an agent-side engagement failure for Devin specifically, but the paper does not verify this claim with direct evidence (e.g. checking whether the agent produced further commits after the last reviewer comment) — **this is the authors' interpretive gloss, not a directly measured attribution of blame.**
- **NRC — No Review Conducted (4.6%, 15 PRs):** explicitly reviewer-side — "closed without any reviewer engagement, even though AI agents explicitly requested review." This is the one category the paper explicitly attributes to the human/maintainer side (reviewers failing to engage despite an active request).
- **CWR — Closed Without Explicit Rationale (4.0%, 13 PRs overall; 42.1% of Cursor's unmerged cases):** maintainer-side (maintainer closes without explanation), reviewer/process opacity rather than agent failure.
- **FRM — Fix Rejected by Maintainers (4.9%, 16 PRs):** explicitly maintainer-side — agent did respond to feedback iteratively, but maintainer ultimately declined the final solution.

**Bottom line for "who abandons":** where attribution is possible at all, the paper's categories skew toward **maintainer/reviewer-side friction** (NRC, CWR, FRM, RAPR, LPO — together 22.1+8.0+4.9+4.0+4.6 = 43.6% of causes are process/maintainer-attributable) roughly matching **agent/technical-side failure** (TCF, IIF, BF, DF — 38.6%), with inactivity (CDI, 9.2%) as an unattributed middle category the authors lean toward agent-engagement-fatigue for Devin specifically without direct proof.

### Threats to validity / limitations (as stated or implied by the paper)

The paper does not include a dedicated "Threats to Validity" section (unusual for an MSR paper, likely compressed given the 5-page length limit). Limitations that are evident from the methodology as reported:
- No repository/ecosystem/language breakdown — cannot assess brownfield vs greenfield split (relevant gap for RQ3/RQ5 in this project).
- No control group of human-authored fix-PRs in the same repos, so absolute merge rates cannot be benchmarked against a human baseline from within this paper.
- Single dataset snapshot (AIDEV-POP, Nov 2025) — a point-in-time census; PRs marked "open" (8.9% overall, but 21.8% for Copilot and 20.9% for Claude Code) may later merge or close, meaning current tallies could shift for those two agents in particular given their much higher open-share.
- Qualitative coding sample (n=326) is well-justified statistically (95% CI, 5% margin of error) but the per-agent breakdown cells get small (Claude Code n=18, Cursor n=19) — agent-specific percentages for these two carry much wider uncertainty than the headline percentages.
- Minor internal inconsistency: Table 2 reports Copilot RAPR as 47 (31.8%) while body prose states "31.7%" for the same cell — negligible but noted as a quality flag.

### Null/negative results

No explicit null-hypothesis test is reported (this is a descriptive/qualitative study, not a hypothesis-testing one). The closest thing to a "negative" finding: build failures (2.1%) and deployment failures (3.1%) are explicitly reported as *comparatively rare* relative to validation-related failures (TCF 18.1%, IIF 15.3%) — recorded here with equal diligence per CLAUDE.md evidence rule 3, since this is itself a directionally important finding (agents are usually not producing broken builds; they are producing plausible-but-invalid or superseded fixes).

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
unmerged-fix-prs-2026	2026	B	E3	Large-scale telemetry census (n=8106 PRs) from AIDEV-POP dataset	8106 fix-related PRs, 5 AI coding agents (Codex 4338, Copilot 1993, Devin 1249, Cursor 411, Claude Code 115), real-world GitHub repos, ecosystem/repo count not disclosed	T8	fix-PR integration outcome (merged / closed-without-merge / open)	65.0% merged (5267/8106); 26.1% closed w/o merge (2113/8106); 8.9% open (726/8106)	mixed (majority positive but over a quarter unmerged)	measured	not reported (no token/dollar cost; only elapsed wall-clock time-to-merge, non-tabulated)	not applicable (no human developer seniority dimension; agent identity substitutes)	real-world GitHub repos, maturity/language/ecosystem unspecified	shares AIDEV-POP/AIDev dataset provenance with other project sources — not independent for triangulation	no control group of human-authored fix-PRs; single snapshot (Nov 2025) may understate merges for high-"open"-share agents (Copilot 21.8% open, Claude Code 20.9% open)	4
unmerged-fix-prs-2026	2026	B	E3	Large-scale telemetry census (n=8106 PRs) from AIDEV-POP dataset	Agent-wise subset of same 8106 PRs	T8	fix-PR merge rate by agent	Codex 81.6% (3539/4338); Cursor 68.4% (281/411); Claude Code 57.4% (66/115); Devin 42.9% (536/1249); Copilot 42.4% (845/1993)	agent-dependent, large spread (81.6% to 42.4%)	measured	not reported	not applicable	real-world GitHub repos, unspecified	shares AIDEV-POP/AIDev dataset provenance with other project sources	single-snapshot; smallest agent sample (Claude Code n=115) carries widest uncertainty	4
unmerged-fix-prs-2026	2026	B	E3	Manual qualitative coding, dual-rater, open coding, n=326 stratified random sample of 2113 closed-unmerged PRs (95% CI, 5% margin of error), Cohen's kappa=0.82	326 closed-but-unmerged fix-related PRs across 5 agents	T8	distribution of failure-cause categories for unmerged fix-PRs	RAPR 22.1%(72); TCF 18.1%(59); IIF 15.3%(50); CDI 9.2%(30); LPO 8.0%(26); IRP 5.5%(18); FRM 4.9%(16); NRC 4.6%(15); CWR 4.0%(13); OTH 3.1%(10); DF 3.1%(10); BF 2.1%(7)	n/a (taxonomy, not single-direction effect)	measured	not reported	not applicable	real-world GitHub repos, unspecified	shares AIDEV-POP/AIDev dataset provenance; qualitative-coding layer itself is original/independent	high inter-rater reliability (kappa=0.82); validation-related failures (TCF+IIF=33.4%) far exceed build/deploy failures (BF+DF=5.2%)	5
unmerged-fix-prs-2026	2026	B	E3	Same qualitative coding, cross-tabulated by agent (Table 2)	Per-agent unmerged subsamples: Claude n=18, Copilot n=148, Cursor n=19, Devin n=50, Codex n=91	T8	dominant failure-cause per agent, within-agent %	Codex: test case failures 54.9%(50/91); Devin: inactivity closures 54.0%(27/50); Copilot: resolved-by-another-PR 31.8%(47/148, prose states 31.7%); Cursor: closed w/o rationale 42.1%(8/19); Claude Code: resolved-by-another-PR 27.8%(5/18) and low-priority/obsolete 22.2%(4/18) tied top	agent-specific failure signatures diverge sharply (validation vs engagement vs redundancy vs opacity)	measured	not reported	not applicable	real-world GitHub repos, unspecified	shares AIDEV-POP/AIDev dataset provenance	small cell sizes for Claude Code (n=18) and Cursor (n=19) — wide uncertainty; zero-count cells for Claude Code should not be read as strong nulls	4
unmerged-fix-prs-2026	2026	B	E3	Same qualitative coding; category NRC explicitly defined as reviewer non-engagement despite agent's explicit review request	326-PR sample, NRC subset = 15 PRs (4.6% overall)	T8	reviewer-side disengagement despite agent requesting review	4.6% (15/326) of unmerged PRs = "No Review Conducted" — reviewers never engaged though agent explicitly requested review	negative (reviewer-side failure, not agent-side)	measured	not reported	not applicable	real-world GitHub repos, unspecified	shares AIDEV-POP/AIDev dataset provenance	one of the few categories the paper explicitly attributes to the human/maintainer side rather than the agent; directly relevant to RQ3 "bottleneck displacement" tension (§5.6)	4
unmerged-fix-prs-2026	2026	B	E3	Telemetry, time-to-merge = closed_at - created_at (hours), merged PRs only, log-scale box plot (Fig 1), no numeric medians/IQR reported in text	5267 merged PRs across 5 agents	T8	merge latency (time-to-merge) distribution shape by agent	no exact numbers reported; qualitative only: Codex shortest and most concentrated; Copilot and Devin broadest distributions with heaviest upper tails	agent-dependent latency variability	measured	not reported	not applicable	real-world GitHub repos, unspecified	shares AIDEV-POP/AIDev dataset provenance	reporting gap: paper shows only a figure, no tabulated median/IQR/mean — cannot be cited as a precise effect size, only directional	2
