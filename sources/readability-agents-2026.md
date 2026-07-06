# readability-agents-2026 — Do AI Agents Really Improve Code Readability?

## Citation & version

Horikawa, K., Horikawa, K., Kashiwa, Y., Uwano, H., & Iida, H. (2026). *Do AI Agents Really Improve Code Readability?* 23rd International Conference on Mining Software Repositories (MSR '26). arXiv:2603.13723 [cs.SE], v1, submitted 14 March 2026. 5 pages (short/mining-track paper). DOI: 10.48550/arXiv.2603.13723.

- **Version read:** arXiv v1 full text (HTML). Journal reference on the arXiv page states acceptance at MSR '26; the arXiv preprint is the version extracted — no camera-ready diff could be checked. Recorded per the §3 preprint substitution rule.
- **Affiliations:** National Institute of Technology, Nara College (K. Horikawa, Uwano) and Nara Institute of Science and Technology (K. Horikawa, Kashiwa, Iida) — both Japan, academic.
- **Verification status:** VERIFIED. Title, authors, venue, and abstract confirmed on arXiv abstract page and full-text HTML (fetched 2026-07-06). Published <12 months ago, so no supersession check required.

## Design

Repository-mining study of commits authored by autonomous coding agents, asking whether commits *claiming* readability improvement actually improve automated readability/quality metrics.

- **RQ1 (theirs):** prevalence of readability-related commits among agent-generated commits.
- **RQ2 (theirs):** what issues these commits address — manual card sorting into the eight readability-improvement categories of Oliveira et al. (2025, "Understanding code understandability improvements in code reviews"), three independent raters, Cohen's kappa 0.80; multi-labelling permitted.
- **RQ3 (theirs):** before/after change in automated metrics — Wilcoxon signed-rank tests (significance threshold p<0.01) with Cliff's delta effect sizes.

**What is compared against what:** agent-authored readability commits are compared (a) before-vs-after on automated metrics, and (b) against a *human* baseline distribution of readability-change categories taken from Oliveira et al. (2025) — a different dataset and study, not a matched within-study human control. There is **no** human-rater assessment of the agent code's readability and no matched human-commit metric comparison.

**Metrics** (computed with the Radon Python library): Maintainability Index (MI, higher better), Cyclomatic Complexity (CC, lower better), LOC / SLOC / LLOC, Halstead Volume / Difficulty / Effort, and comment-line counts (single- and multi-line). Automated metrics only; no human readability ratings.

**Dataset provenance:** derives from the **AIDev dataset** (Li et al., 2025, "The Rise of AI Teammates in Software Engineering (SE) 3.0", arXiv:2507.15003; SAIL Research) — a known shared dataset of PRs authored by five coding agents (in AIDev v1: OpenAI Codex, Devin, GitHub Copilot, Cursor, Claude Code). The snapshot used here contains 932,791 PRs from >61,000 repositories (larger than AIDev's originally announced ~456k PRs, i.e. an expanded release); the authors supplemented it via the GitHub REST API to reach 1,382,314 agentic commits. The paper itself does not name the five agents nor break results down by agent.

**Sampling flow (n):** 1,382,314 agent commits → 4,115 contain readability keywords (case-insensitive: readability, readable, understandability, understandable, clarity, legibility, easier to read, comprehensible) ≈ 0.3% → 577 modify Python files → **403** with valid pre/post states parsed for metric analysis (RQ3). For category card sorting (RQ2): **231** commits randomly sampled from the 577 (95% confidence, 5% margin of error).

## Findings

All findings **measured** (automated metrics / manual classification of artefacts), not self-reported. Era E3 throughout (autonomous PR agents). Task types: primarily **T5** (refactoring/readability commits), with the documentation category touching **T10**.

**F1 — Prevalence (their RQ1).** Readability-related commits are ~0.3% of all agent commits (4,115 / 1,382,314). "Readability" is the dominant keyword (50.1% of matched commits). *Direction: descriptive.*

**F2 — What agents change (their RQ2, n=231).** Category shares (multi-label, may exceed 100%): Complex/Long/Inadequate Logic 42.4%; Incomplete/Inadequate Code Documentation 24.2%; Bad Identifier 14.3%; Inconsistent/Disrupted Formatting 14.3%; Inadequate Logging & Monitoring 12.6%; Unnecessary Code 10.0%; Wrong/Missing/Inadequate String 6.1%; Missing Constant Usage 2.6%.

**F3 — Agent vs human focus (similarity AND difference).** Against Oliveira et al.'s human baseline: *similar* on documentation (agents 24.2% vs humans 22.3%); *different* on logic complexity (agents 42.4% vs humans 18.2% — agents over twice as concentrated) and identifiers (agents 14.3% vs humans 20.3%). Authors: human contributions are "relatively evenly distributed across several categories" while agents prioritise logic and documentation over surface-level aspects. Caveat: cross-study comparison, different populations and codebases.

**F4 — Metrics after "readability" commits mostly worsen (their RQ3, n=403; headline negative result).** Wilcoxon signed-rank, Cliff's delta:

| Metric | Mean Δ | Median Δ | p | Cliff's δ |
|---|---|---|---|---|
| Lines of Code | +27.61 | +6.00 | <0.001 | 0.64 |
| Cyclomatic Complexity | +3.13 | 0.00 | <0.001 | 0.63 |
| Multi-line comments | +2.10 | 0.00 | <0.001 | 0.63 |
| Source Lines of Code | +18.47 | +2.60 | <0.001 | 0.60 |
| Logical Lines of Code | +12.18 | +1.00 | <0.001 | 0.54 |
| Halstead Volume | +43.60 | 0.00 | <0.001 | 0.50 |
| Halstead Effort | +321.49 | 0.00 | <0.001 | 0.42 |
| Halstead Difficulty | +0.31 | 0.00 | <0.001 | 0.35 |
| Comment lines | +1.67 | 0.00 | <0.001 | 0.30 |
| Single-line comments | +0.73 | 0.00 | 0.022 | 0.17 |
| **Maintainability Index** | **−3.25** | **−0.12** | **<0.001** | **−0.35** |

Deterioration rates: MI decreased in **56.1%** of commits; CC increased in **42.7%**; LOC increased in **71.5%**. *Direction: negative for the claimed intent (readability commits worsen conventional quality metrics on balance).*

**F5 — Partially benign reading (recorded with equal diligence).** Median LOC growth (+6.00) exceeds the median executable-code growth, and comment counts rise significantly — some of the added volume is documentation/formatting rather than logic. Documentation-focused changes are a plausibly genuine readability gain that MI/CC penalise (MI penalises volume). Zero medians on CC, Halstead, and comment metrics indicate the typical commit leaves those unchanged; the negative aggregate is driven by a sub-population (consistent with 42.7% CC-increase vs implied ~57% no-increase/decrease). The paper does not quantify the improving minority separately.

**F6 — Authors' interpretation.** "Current agents lack a robust understanding of effective readability improvements"; they recommend quality-checking mechanisms on agent output — while conceding in threats that MI/CC "may not fully capture all aspects of readability, such as clarity of intent and logical flow". Both readings (agents fail vs metrics inadequate) are live; the study cannot separate them without human ratings.

## Heterogeneity

Essentially none reported: no per-agent breakdown (despite five agents in the dataset), Python only, no stratification by repository maturity, commit size, or category (e.g. whether documentation-category commits behave differently on MI than logic-category ones — the obvious follow-up — is not run).

## Authors' limitations (as stated)

- Manual RQ2 classification is subjective (mitigated by three raters, kappa 0.80).
- Tangled commits: readability keywords may co-occur with unrelated changes bundled in the same commit.
- MI/CC may not fully capture readability (clarity of intent, logical flow).
- Strict keyword filtering yields a small, possibly unrepresentative sample (0.3% of commits); keyword matching misses readability commits that don't say so.
- Python-only; generalisability to other languages unknown.

Unstated but relevant: no counterfactual (what would a human's "improve readability" commit do to the same metrics on the same code?); metric direction conventions make "more comments" mechanically reduce MI-style scores; no assessment of whether the PRs were merged or later reverted.

## Grading

- **Era:** **E3** — autonomous PR/coding agents (AIDev population: Codex, Devin, Copilot agent, Cursor, Claude Code class), tagged by modality studied.
- **Tier:** **B** — structured observational mining study, peer-reviewed (MSR '26), shared public dataset, no randomisation or counterfactual; modest analysed n (403) and short-paper depth keep it at the weaker end of B. Carries claims with caveats.
- **Independence / COI:** No vendor conflict. Academic authors; funded by JSPS KAKENHI (JP24K02921, JP25K21359), JST PRESTO (JPMJPR22P3), ASPIRE (JPMJAP2415), and AIP Accelerated Program (JPMJCR25U7). No agent-vendor funding disclosed. **COI flag: none.**
- **Population:** open-source GitHub repositories accepting agent PRs; Python subset; no seniority dimension (authors are agents).
- **Measurement basis:** measured (automated metrics; manual artefact classification). No self-report anywhere.

**Can support:** the claim that agent commits *labelled* as readability improvements frequently worsen conventional maintainability metrics in OSS Python (quality-debt signal, RQ3/RQ4 flavour); that agents concentrate readability effort on logic restructuring and documentation more than humans do.
**Cannot support:** any claim about actual human-perceived readability (no human ratings of the code), per-agent differences, non-Python code, brownfield/greenfield splits, or overall agent code quality (readability commits are 0.3% of activity).

**Relevance to us:** 3/5 — a clean measured E3 negative/quality-debt signal for refactoring-type tasks (T5), directly relevant to the churn/duplication tension and to instrumenting agent-refactor quality; limited by metric-only measurement and narrow scope.
