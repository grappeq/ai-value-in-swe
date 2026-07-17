# Source: Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub

**source_id:** `failed-agentic-prs-2026`

## Identity (verified)

- **Title:** "Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub"
- **Authors:** Ramtin Ehsani, Sakshi Pathak, Shriya Rawal, Abdullah Al Mujahid, Mia Mohammad Imran, Preetha Chatterjee
- **Affiliations:** Drexel University (Philadelphia, PA, USA); Missouri University of Science and Technology (Rolla, MO, USA)
- **arXiv ID:** 2601.15195 (v1, submitted 21 January 2026)
- **Venue/status:** Accepted at **MSR '26 — 23rd International Conference on Mining Software Repositories**, April 2026, Rio de Janeiro, Brazil. Header confirms acceptance; text is the camera-ready/preprint version (footer timestamp 21 Jan 2026).
- **Subject categories:** cs.SE (Software Engineering), cs.AI
- **Full text obtained via:** arXiv HTML (arxiv.org/html/2601.15195v1). No paywall — preprint substitution rule not needed.
- **Structure:** Introduction, Methodology, Results, Conclusion, References. **No dedicated Limitations / Threats to Validity section** — unusual for an MSR paper; some limitation-adjacent language appears folded into the Conclusion only (see Quality notes below).

## Dataset provenance (independence flag — read before trusting any triangulation)

The paper does **not** collect its own PR corpus. It draws a subset — the **"AIDev-pop"** dataset — from **AIDev**, a large public dataset built by **Hao Li, Haoxiang Zhang, and Ahmed E. Hassan (Queen's University, SAIL Research group)**, published as "The Rise of AI Teammates in Software Engineering (SE) 3.0" (arXiv:2507.15003, July 2025). The parent AIDev corpus spans ~456,000 PRs by the same five agents across ~61,000 repositories and ~47,000 developers; "AIDev-pop" is the filtered subset restricted to repos with ≥100 GitHub stars (33,596 PRs).

**Independence flag:** this paper's authors (Drexel / Missouri S&T) have no visible overlap with the AIDev dataset creators (Queen's University) — so the *analysis* is independent. But the *underlying data* is shared and public: at least two other 2026 papers found during this extraction reuse the same AIDev corpus — "AIDev: Studying AI Coding Agents on GitHub" (arXiv:2602.09185) and "Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance" (arXiv:2602.08915). **Any apparent convergence between this paper and other AIDev-derived papers is not independent triangulation** per PROTOCOL §3 (same population, same PR-identification/labelling pipeline, same potential biases in how "agent-authored" was determined) — it should be treated as one data source analysed multiple ways, not as 2–3 independent Tier B/C sources. Flag this explicitly if any future synthesis cites this paper alongside 2602.08915 or 2602.09185 as corroborating evidence.

The paper does not describe (and does not need to, since it inherits it from Li et al. 2025) the original PR collection date range or GitHub search/filtering criteria for identifying "agent-authored" — that methodology lives in the parent AIDev paper, not this one. This is a **dependency**, not a flaw in this paper per se, but it means this paper's population is only as trustworthy as AIDev's original agent-authorship detection method, which this extraction did not independently verify (out of scope — would require reading arXiv:2507.15003).

## Research questions (as stated in the paper)

- **RQ1:** How do merged and not-merged agent-authored PRs differ in task types, code changes, CI outcomes, and review interactions?
- **RQ2:** What patterns lead to agent-authored PRs not being merged in real-world software repositories?

## Methodology

- **RQ1 (quantitative):** Cliff's δ effect sizes, kernel density estimation, and a logistic regression predicting merge outcome from LOC changed, files changed, failed CI checks, review comment count, review revision count. N = 33,596 PRs.
- **RQ2 (qualitative):** Stratified random sample of 600 rejected/not-merged PRs (stratified by agent, "95% confidence and ±5% margin of error"); 38 PRs were inaccessible (deleted/private), leaving **562** coded. Two authors independently open-coded each PR's primary rejection reason; initial Cohen's κ = 0.55, refined to **κ = 0.91** after taxonomy iteration (arithmetic check: the 11 taxonomy category counts reported below sum to exactly 562, confirming internal consistency).

## Full reading notes

**Overall outcome.** "Across all agents, 71.48% of PRs (24,014) are successfully merged." (33,596 total PRs, 24,014 merged — arithmetic checks out.)

**Per-agent merge rate (large spread — this is one of the most decision-relevant numbers in the paper):**
| Agent | PRs | Merged | Merge rate |
|---|---|---|---|
| OpenAI Codex | 21,799 | 18,004 | 82.59% |
| Copilot | 4,970 | 2,139 | 43.04% |
| Devin | 4,827 | 2,595 | 53.76% |
| Cursor | 1,541 | 1,005 | 65.22% |
| Claude Code | 459 | 271 | 59.04% |

(Sum of merged: 18,004+2,139+2,595+1,005+271 = 24,014 — matches the reported overall total, internally consistent.) Note the very small Claude Code sample (n=459, ~1.4% of the corpus) relative to Codex (n=21,799, ~65% of the corpus) — the overall 71.48% figure is heavily dominated by Codex's volume and merge behaviour, not a balanced cross-agent average.

**Merge rate by task type:** highest — documentation 84%, CI 79%, build 74%; lowest — fix 64%, performance 55%. Full taxonomy used: feature, fix, performance, refactoring, style, documentation, test, chore, build, CI, other. Per-task PR counts are shown only in a figure, not stated in body text — could not be extracted verbatim; treat the percentages as approximate category summaries, not confirmed via raw counts. Agent-specific breakdown: Codex leads across most categories (documentation 92%, CI 86%, build 87%); Copilot weakest overall (feature 38%, test 37%, performance 27%).

**Code-change characteristics, not-merged vs merged (Cliff's δ, Table 1):**
- Verbatim: "the difference in total lines of code changes is 17%, and the difference in the number of changed files is 10%" — reported as Cliff's δ = -0.17 (LOC) and δ = -0.10 (files), i.e. not-merged PRs are larger and touch more files (small-to-medium effect for LOC, small for files).
- Verbatim: "Cliff's δ of 24% indicates a moderate effect size, showing that not-merged PRs tend to experience more CI failures."
- Review comments: ~5% higher on not-merged PRs (small effect); review revisions: ~3% more (small effect). Not-merged PRs show a wider/heavier right tail — some are extensively debated before rejection, not simply ignored.

**Logistic regression predicting merge:**
- Verbatim: "each additional failed CI check decreases the odds of a merge by about 15%" — the single strongest, most significant predictor.
- Each additional LOC changed: ~1% decrease in merge odds.
- Each additional file changed: ~1% decrease in merge odds.
- Review comments and review revisions: **non-significant** predictors in the regression (p ≈ 0.48 and p ≈ 0.67 respectively) — despite showing up as (small) univariate differences, they do not independently predict merge outcome once other variables are controlled. This is a genuine null result and is recorded as such.

**RQ2 — rejection-reason taxonomy (562 coded PRs), four top-level buckets, 11 leaf categories:**

| Level | Category | n | % | Definition |
|---|---|---|---|---|
| Reviewer | Abandoned / Not Reviewed | 228 | 38% | No meaningful human engagement; PR goes stale or is auto-closed |
| Pull Request | Duplicate PR | 142 | 23% | Equivalent work already exists in another PR |
| Pull Request | Unwanted Feature | 24 | 4% | Change misaligned with project goals/roadmap |
| Pull Request | Non-Functional | 13 | 2% | Setup/configuration only, no substantive change |
| Pull Request | Wrong Task Description | 7 | 1% | PR lacks meaningful context/description |
| Pull Request | Wrong Branch | 2 | <1% | Opened against the wrong branch |
| Code | CI/Test Failure | 99 | 17% | Automated build/tests fail and are not fixed |
| Code | Incorrect Implementation | 19 | 3% | Technically wrong despite addressing the right task |
| Code | Incomplete Implementation | 15 | 2% | Missing required logic |
| Agentic | Misalignment | 9 | 1% | Agent repeatedly fails to follow reviewer instructions |
| Agentic | License Issues | 4 | <1% | CLA / IP ownership concerns the agent cannot resolve |

(Counts sum to 562 exactly — internally consistent with the "562 accessible" qualitative sample size.)

Illustrative quotes captured by the paper: duplicate-PR closures such as "Superseded by PR #715 which consolidates all GFQL code changes into a single PR"; CI-failure closures such as "@copilot fix the merge conflicts; if you cannot fix these then close the PR"; unwanted-feature closures such as "Too old already superseded by more recent pushes" and "This is a LOT to review, would really prefer smaller granular PRs."

**Authors' three-way framing of failure causes (Conclusion):**
1. Workflow misalignment — CI/CD failures, inability to detect pre-existing/duplicate work
2. Expectation misalignment — oversized changes, unwanted features, task misunderstanding
3. Coordination failure — reviewer abandonment / lack of engagement or reviewer priority

Recommendation: agent PRs should be "small, focused, and limited to a single coherent change"; agents should better detect existing work, adhere to project norms, decompose tasks, and validate against CI before opening a PR.

## What this source does *not* contain (checked explicitly, per protocol nulls-with-diligence rule)

- **No cost data.** No token spend, no compute cost, no reviewer time-in-hours, no rework-time figures. Nothing usable for RQ4.
- **No developer/reviewer seniority split.** The paper does not tag reviewers or maintainers by seniority.
- **No self-reported measure of any kind.** Every metric (merge status, LOC, files changed, CI outcome, comment/revision counts, rejection-reason coding) is derived from GitHub telemetry or human coding of the actual PR artefact — there is no survey, no perception measure, and therefore **no perceived-vs-measured gap to report** from this source. This is itself worth noting: unlike much of the RQ2 literature base, this is a source with zero self-report content, which is a methodological strength but means it cannot speak to the perception–reality gap (§5 tension 1).
- **No explicit Threats to Validity / Limitations section**, which is unusual for an MSR-venue paper. The population is entirely public GitHub repos with ≥100 stars — open source only; no proprietary/enterprise codebases, so findings about "mature codebase" friction should be read as open-source-community mature, not necessarily enterprise-mature (a real difference in review norms, CI rigour, and reviewer incentive structure).

## Grading (per PROTOCOL §2–§3)

- **Tier: B** — large-scale (n=33,596) observational telemetry study without randomisation or counterfactual, published at a peer-reviewed MSR venue. Fits §3's Tier B definition ("large-scale telemetry without randomisation... multi-company [here: multi-repo] code-quality analyses") precisely. Not Tier A: the regression is correlational/predictive, not causal, and there is no controlled comparison condition. Not Tier C/D: this is an academic peer-reviewed empirical study, not a practitioner blog or vendor report.
- **Era: E3 (agentic)** — all five studied systems (OpenAI Codex, GitHub Copilot [agent/coding-agent mode], Devin, Cursor, Claude Code) are autonomous PR-generating agents performing multi-file plan-execute-submit workflows against real repositories, not autocomplete or chat-panel copy-paste. Unambiguous E3 by tool modality.
- **Independence:** analysis is independent (Drexel/Missouri S&T, no overlap with AIDev's Queen's University creators); underlying dataset is shared/public and reused by other concurrent papers (see provenance section above) — flag on any triangulation claim, not on the finding itself. No vendor funding disclosed; not COI-flagged as Tier D.
- **Population:** 33,596 PRs / 5 agents / public GitHub repos with ≥100 stars, for RQ1; stratified random subsample of 562 coded rejected PRs for RQ2.
- **What this source can support:** Strong, E3-era, large-N evidence for RQ3 (failure map) — which task types agents fail on (performance, fix, worst; documentation/CI/build, best) and a well-powered, high-agreement (κ=0.91) taxonomy of *why* agentic PRs get rejected in the open-source wild, dominated by socio-technical/coordination failure (38% abandonment, 23% duplicate) rather than pure code-quality failure (only ~22% combined across CI-failure/incorrect/incomplete implementation). Also usable for RQ6 (anti-metrics): LOC and file-count are weak, near-noise predictors of merge outcome (~1% odds change each) once CI status is controlled — a caution against LOC-based productivity/quality metrics.
- **What this source cannot support:** RQ4 (cost — no data at all), RQ2's perception-reality tension (no self-report present to compare against), seniority-asymmetry tension (§5.5 — no seniority data), enterprise/proprietary brownfield claims (open-source only, ≥100-star repos, external/community contribution norms rather than internal team norms), or causal claims about *why* task type predicts merge rate (correlational only, task type is a coarse label applied post hoc, not a designed manipulation).

## Surprises / notes for cross-referencing

- The 38%+23% = **61% of all rejections are not code-quality problems at all** — they are coordination/socio-technical failures (abandonment, duplication). This complicates any simple "agents write bad code" narrative and is directly relevant to RQ3's "task characteristics predict failure" framing: the predictive task characteristic here is arguably *reviewer/maintainer capacity and PR redundancy risk*, not code correctness.
- The regression finding that review comments/revisions are non-significant predictors, despite not-merged PRs showing higher raw comment/revision counts, is a genuine tension worth flagging for cross-referencing: it suggests comment volume is a *symptom* of PRs already heading toward rejection (extensive back-and-forth before giving up) rather than a *cause*, and that raw "engagement" metrics could mislead if read causally — relevant to §5 tension 6 (bottleneck displacement) and RQ6 anti-metrics.
- Agent-level merge-rate spread (43% to 83%) is large enough that any claim of the form "agentic coding tools have an X% success rate" without naming the agent is not meaningful — this source is strong ammunition against agent-agnostic effect-size claims elsewhere in the evidence base.
- The AIDev/AIDev-pop shared-dataset issue (above) should be checked against every other AIDev-derived source before this paper's findings are used to "confirm" anything from a sibling AIDev paper.

## Proposed evidence rows (unverified)

failed-agentic-prs-2026	2026	B	E3	Large-N observational study (n=33,596 agent-authored GitHub PRs, AIDev-pop subset); Cliff's delta + logistic regression	33,596 PRs by 5 coding agents (Codex n=21,799, Copilot n=4,970, Devin n=4,827, Cursor n=1,541, Claude Code n=459) against public GitHub repos with >=100 stars	T3,T4,T5,T6,T7,T8,T9,T10,T11 (mixed real-world PR tasks, task-typed post hoc)	overall PR merge rate	71.48% (24,014/33,596) merged	positive (majority merge) but large unexplained variance	measured	not reported	not reported	open-source GitHub repos, >=100 stars, external/community contribution context	Dataset (AIDev-pop) is subset of shared public AIDev corpus (Li/Zhang/Hassan 2025, Queen's Univ) reused by other 2026 papers (2602.08915, 2602.09185) - not independent triangulation if cited alongside those	Peer-reviewed MSR '26 accepted paper; no Limitations/Threats-to-Validity section; overall figure dominated by Codex volume (65% of corpus)	5
failed-agentic-prs-2026	2026	B	E3	Same study, per-agent breakdown	Same population, split by agent	T3,T4,T5,T6,T7,T8,T9,T10,T11	merge rate by agent	Codex 82.59% (18,004/21,799); Copilot 43.04% (2,139/4,970); Devin 53.76% (2,595/4,827); Cursor 65.22% (1,005/1,541); Claude Code 59.04% (271/459)	large negative spread, Copilot lowest	measured	not reported	not reported	same as above	same as above	Claude Code sample is small (n=459, ~1.4% of corpus) - low precision relative to Codex	5
failed-agentic-prs-2026	2026	B	E3	Same study, merge rate by task category	Same population, PR-level task-type label (feature/fix/performance/refactor/style/doc/test/chore/build/CI/other)	T10,T11	merge rate by task type (documentation, CI, build highest)	documentation 84%; CI 79%; build 74%	positive (high success)	measured	not reported	not reported	same as above	same as above	Per-task PR counts shown only in figure, not in body text - percentages not independently count-verified	5
failed-agentic-prs-2026	2026	B	E3	Same study, merge rate by task category	Same population	T5,T8	merge rate by task type (performance, fix lowest)	performance 55%; fix 64%	negative (low success)	measured	not reported	not reported	same as above	same as above	Same caveat on per-task counts not shown in text	5
failed-agentic-prs-2026	2026	B	E3	Same study, Cliff's delta comparison merged vs not-merged	Same population	T3,T4,T5,T6,T7,T8,T9,T10,T11	code-change size (LOC, files changed), not-merged vs merged	LOC delta ~17% (Cliff's delta=-0.17); files-changed delta ~10% (Cliff's delta=-0.10)	negative (larger/more diffuse changes associated with rejection)	measured	not reported	not reported	same as above	same as above	Small-to-medium effect sizes per Cliff's delta conventions	4
failed-agentic-prs-2026	2026	B	E3	Same study, Cliff's delta comparison merged vs not-merged	Same population	T3,T4,T5,T6,T7,T8,T9,T10,T11	CI failure count, not-merged vs merged	Cliff's delta = 0.24 (moderate effect)	negative (more CI failures associated with rejection)	measured	not reported	not reported	same as above	same as above	Largest of the three Cliff's delta effects reported	5
failed-agentic-prs-2026	2026	B	E3	Same study, logistic regression predicting merge outcome	Same population	T3,T4,T5,T6,T7,T8,T9,T10,T11	odds ratio per failed CI check	~15% decrease in merge odds per additional failed CI check	negative, strongest predictor	measured	not reported	not reported	same as above	same as above	Reported as most significant coefficient in the model; exact p-value/CI not quoted in extracted text	5
failed-agentic-prs-2026	2026	B	E3	Same study, logistic regression predicting merge outcome	Same population	T3,T4,T5,T6,T7,T8,T9,T10,T11	odds ratio per LOC / per file changed	~1% decrease in merge odds per LOC changed; ~1% decrease per file changed	negative, weak	measured	not reported	not reported	same as above	same as above	Weak effects despite univariate Cliff's delta of 17%/10% - illustrates surface-metric vs regression-controlled discrepancy	4
failed-agentic-prs-2026	2026	B	E3	Same study, logistic regression predicting merge outcome (null result)	Same population	T3,T4,T5,T6,T7,T8,T9,T10,T11	review comments / review revisions as merge predictors	non-significant (p approx 0.48 for comments, p approx 0.67 for revisions)	null	measured	not reported	not reported	same as above	same as above	Genuine null result recorded with same diligence as positive findings per protocol rule 3; contradicts naive reading of univariate 5%/3% comment/revision deltas as causal	4
failed-agentic-prs-2026	2026	B	E3	Qualitative open-coding of rejected PRs (RQ2), stratified sample	600 sampled rejected PRs (562 coded, 38 inaccessible), stratified by agent, 95% CI +/-5% margin, Cohen's kappa=0.91 after refinement	T3,T4,T5,T6,T7,T8,T9,T10,T11	rejection-reason taxonomy: Reviewer Abandoned/Not Reviewed	228/562 = 38%	negative (top rejection cause is non-code coordination failure)	measured (human-coded from PR artefacts, not self-report)	not reported	not reported	same as above	same as above	Single largest rejection category; strong inter-rater reliability (kappa 0.91)	5
failed-agentic-prs-2026	2026	B	E3	Qualitative open-coding of rejected PRs (RQ2)	Same 562-PR coded sample	T3,T4,T5,T6,T7,T8,T9,T10,T11	rejection-reason taxonomy: Duplicate PR	142/562 = 23%	negative	measured	not reported	not reported	same as above	same as above	Second largest category; reflects agents' inability to detect pre-existing/parallel work	5
failed-agentic-prs-2026	2026	B	E3	Qualitative open-coding of rejected PRs (RQ2)	Same 562-PR coded sample	T3,T4,T5,T6,T7,T8,T9,T10,T11	rejection-reason taxonomy: CI/Test Failure	99/562 = 17%	negative	measured	not reported	not reported	same as above	same as above	Third largest category; only code-correctness-adjacent category in top three	4
failed-agentic-prs-2026	2026	B	E3	Qualitative open-coding of rejected PRs (RQ2)	Same 562-PR coded sample	T3,T4,T5,T6,T7,T8,T9,T10,T11	rejection-reason taxonomy: remaining minor categories (Unwanted Feature 4%, Incorrect Implementation 3%, Incomplete Implementation 2%, Non-Functional 2%, Misalignment 1%, Wrong Task Description 1%, License Issues <1%, Wrong Branch <1%)	Unwanted Feature 24/562=4%; Incorrect Impl 19/562=3%; Incomplete Impl 15/562=2%; Non-Functional 13/562=2%; Misalignment 9/562=1%; Wrong Task Desc 7/562=1%; License 4/562=<1%; Wrong Branch 2/562=<1%	negative, all minority causes	measured	not reported	not reported	same as above	same as above	Combined these 8 minor categories = 18% of rejections; "Misalignment" (agent ignores explicit reviewer feedback across rounds) most directly evidences agent-specific (vs generic contributor) failure mode	3
