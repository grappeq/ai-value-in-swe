# agent-maintainability-2026 — CodeThread: controlled agent-vs-human authorship comparison on downstream maintainability

**source_id:** agent-maintainability-2026
**Date verified:** 2026-07-06 (Phase 1 FETCH+EXTRACT)
**RQs fed:** RQ3 (failure map — task-type-stratified failure mode, refactoring hardest); RQ2 (measurement methods — a construct-validity finding: static metrics vs behavioural/task-based measurement of "maintainability" diverge); PROTOCOL §5 tension 4 (quality debt — direct E3 corroboration test, flagged in Phase 0/in `sources/gitclear-2025.md` follow-up leads as the candidate independent academic leg)

## Citation

Patel, S.\*, Hou, B. L.\*, Purohit, A., Xu, K., Pan, J., He, H., & Chen, V. (2026). *Is Agent Code Less Maintainable Than Human Code?* arXiv:2606.21804v1 [cs.SE]. Submitted 19 June 2026 (23:56 UTC).

- Affiliations (from the PDF masthead): Patel, Hou, Purohit, Xu, Pan, and "He He" are **New York University** (affiliation 1); Chen is **Carnegie Mellon University** (affiliation 2). \* denotes equal contribution (Patel and Hou).
- Correspondence: spp9399@nyu.edu, betty.li.hou@nyu.edu
- Code and data: https://github.com/shaswatpatel123/CodeThread
- **Status: preprint.** The PDF's own footer states "Preprint." on page 1; no journal-ref, no conference acceptance notice, no DOI. Confirmed via a direct WebFetch of the arXiv abstract page: **single version only** — "[v1] Fri, 19 Jun 2026 23:56:14 UTC (6,647 KB)" — no v2, no comments field indicating venue. This paper is ~2.5 weeks old at verification; well within the 12-month recency-check threshold, so the mandatory recency search (CLAUDE.md rule 8) was not triggered, but a light WebSearch was run anyway given how central it may be to tension 4 — no retraction, no critique, no replication found; the paper does not yet appear to have generated secondary discussion.

## Author/dataset overlap verdict — the check this record was specifically commissioned to make

**Clean. No author overlap and no dataset overlap with the CMU lab (Vasilescu/He/Agarwal/Miller/Kästner) or the AIDev dataset.**

- The CMU lab already in this evidence base (`cursor-velocity-quality-2025.md`, `agents-vs-ides-2026.md`, `he-2026-2x-mandate.md`) consists of **Hao He**, Shyam Agarwal, Bogdan Vasilescu, Courtney Miller, and Christian Kästner.
- This paper's author list contains **"He He"** (NYU) and **Valerie Chen** (CMU, second affiliation). Neither is the same person as Hao He of the Vasilescu group — **"He He" and "Hao He" are different individuals with confusingly similar transliterated names; this was checked explicitly because the task brief flagged the risk.** He He (NYU) works in NLP/ML (known for prior work on grounded language and evaluation, not software-repository mining); this is corroborated by the institutional split (NYU vs CMU) and by the complete absence of any of Hao He/Agarwal/Vasilescu/Miller/Kästner from this paper's author list or acknowledgments.
- Valerie Chen is CMU-affiliated but is not one of the five names in the existing CMU cluster — a different research group within the same university, nothing more. Institutional co-location (CMU) is not authorial overlap.
- **Dataset overlap: none.** This paper does not use AIDev (Zhang et al., arXiv:2602.09185, the PR-attribution dataset underlying `agents-vs-ides-2026`), GitClear's proprietary telemetry, or any GHArchive/SonarQube pipeline (the CMU DiD papers' own-collected but methodologically similar pipeline). It instead **constructs its own synthetic two-step task chains** from four independent SWE-agent benchmarks (SWE-Bench Verified, SWE-Bench Multilingual, SWE-Bench Pro, FeatBench) that are themselves unrelated to AIDev or GitClear.
- **Consequence for this evidence base:** this is the **first genuinely independent academic voice** on tension 4 identified so far — independent of GitClear (commercial, COI-flagged) and independent of the CMU Vasilescu-lab trio (same authors, same broad methodology family, not independent of each other per the existing overlap note in `cursor-velocity-quality-2025.md`). It is also methodologically unlike both: a **controlled quasi-experiment** (authorship is manipulated within a matched task, not observed in the wild), not a population-level correlational telemetry study.

## Verification status

**VERIFIED — full text read from the primary PDF, not the abstract.** Sequence: WebFetch of the arXiv abstract page (title/authors/date only) → WebFetch of the PDF via an AI summarisation pass (used only for triage, treated as provisional — it introduced two errors on cross-check, see below) → **the actual PDF binary saved by the fetch tool was converted locally with `pdftotext -layout` and read in full** (all ~21 pages including appendices A–D, the reference list, the LR feature table, and the LLM-judge attribution tables). All facts and figures below are drawn from this full-text read, not the AI-summarised pass.
- **Correction to the intermediate AI-summarised pass:** it initially reported the four benchmarks as "SWE-Bench Verified, SWE-Bench Multi, SLOP CodeBench, [unspecified]" — this is wrong. The actual four benchmarks (confirmed from Table 1 of the full text) are **SWE-Bench Verified, SWE-Bench Multilingual, SWE-Bench Pro, and FeatBench**. SlopCodeBench is cited only in Related Work as a different (unused) benchmark for a different kind of study (long-horizon behavioural drift measurement). Flagging this because it is exactly the kind of "extracted from an AI-compressed pass and presented as a full read" error CLAUDE.md rule 2 warns against — recorded here, not repeated in the extraction below. The four-agent list (Claude 4.5 Sonnet, GPT-5, GLM 4.7, MiniMax M2.5) from the intermediate pass was, on cross-check, correct.

## Tier, era, independence

- **Tier: A.** This is not telemetry-with-counterfactuals in the DiD sense (PROTOCOL §3's Tier A example), but it meets the "rigorous" bar by a different, arguably stronger route for the specific causal question at hand: **authorship (agent vs human) is directly and controllably manipulated within a matched task** — the same downstream Follow-On Issue, on the same repository, with the same PR2 author (always an agent), varying only whether PR1 was written by a human (the benchmark's own ground-truth contributor) or an agent. This eliminates the task-mix confound that limits every population-level source in this evidence base (GitClear's correlational trend; the CMU DiD papers' self-selected real-world adoption). Read as a **controlled comparative experiment on code artefacts**, not a randomised trial on human subjects — there is no random assignment of developers to conditions, but there is controlled, matched assignment of the *object under test* (which piece of code an agent must build on). One notch different in kind from an RCT, but not weaker in internal validity for the specific "does prior authorship affect downstream buildability" question; weaker than an RCT only in that it says nothing about real developers' experience (see Limitations).
- **Era: E3, clean and unambiguous — the cleanest E3 attribution encountered so far in this evidence base.** Unlike the Cursor `.cursorrules`-detection or AIDev bot/branch-heuristic attribution methods used elsewhere (which infer authorship indirectly and admit contamination risk), here **agent authorship is definitional by construction**: the "agent" condition literally is the output of running Claude 4.5 Sonnet, GPT-5, GLM 4.7, or MiniMax M2.5 through the SWE-Agent (Yang et al., 2024) scaffold on the task. All four are 2026-era frontier models run as autonomous multi-step coding agents (step budget 250, cost cap $3/instance, high reasoning effort) — squarely PROTOCOL §2's E3 plan–execute–verify modality. No modality-mixing risk of the kind that affects Cursor-based sources.
- **Independence:** Academic (NYU + CMU), no vendor affiliation, no funding disclosure beyond "NYU IT High Performance Computing resources, services, and staff expertise" (Acknowledgments). No Anthropic/OpenAI/GitHub grant or partnership disclosed, despite the paper's dependence on Claude and GPT-5 API access — the authors are testing these vendors' products as subjects, not being funded by them, as far as the acknowledgments and the fetched text reveal. **No Tier D flag.** The paper's own "LLM/Agent Usage Disclosure" section states LLMs were used only for literature search and tooling/debugging assistance during the study itself, not for computing primary quantitative results (except where explicitly using LLM-as-judge for two secondary, disclosed sub-analyses) — a transparency practice worth noting for RQ2/RQ6 methodology purposes.

## Method & population

**CodeThread framework — how agent vs human authorship is identified and matched (this is the paper's central methodological contribution):**

1. **PR0 (skeleton):** starting from an existing single-issue SWE benchmark instance (issue text, base commit, human ground-truth patch, test suite), the target function bodies are stripped out, preserving signatures — producing a skeleton code state.
2. **Implementation Task, PR0→PR1:** an LLM-generated issue asks an author (human or agent) to restore the missing functionality. **PR1 is filtered** to require passing all Pass-to-Pass tests (original functionality restored) while still failing all Fail-to-Pass tests (the benchmark's actual downstream issue not yet incidentally solved) — this keeps PR1 a "reasonable, functionally complete but not-yet-issue-resolving" implementation, comparable across human and agent authors. The **HH condition's PR1 is the benchmark's own original human-authored ground-truth patch** (i.e., real developers, not recruited-for-this-study developers).
3. **Follow-On Issue, PR1→PR2:** the *original, unmodified* benchmark issue and test suite are applied on top of whatever PR1 state exists. **PR2 is always written by the agent under test** — authorship of PR1 is the only thing varied. Three conditions result: **HH** (human PR1, human PR2 — baseline), **HA** (human PR1, agent PR2), **AA** (agent PR1, agent PR2). The paper's central comparison is **AA vs HA**: holding the follow-on author (agent) and the follow-on task fixed, does the identity of who wrote the code being built upon (human vs agent) change the agent's success rate on the same downstream issue? **This directly neutralises the task-mix confound that limits every other source on tension 4 in this evidence base** — the downstream task is literally identical in both arms.
4. **AH (human on top of agent code) was not studied** — see Limitations.

**Sample (Table 1, filtered to instances requiring function-level edits):**

| Benchmark | Total | Filtered | Repos | Languages | Task types |
|---|---|---|---|---|---|
| SWE-Bench Verified | 500 | 441 | 12 | 1 | Bug fixing (BF) |
| SWE-Bench Multilingual | 300 | 171 | 34 | 7 | BF |
| SWE-Bench Pro | 731 | 641 | 11 | 4 | BF, feature implementation (FI), refactoring (RF) |
| FeatBench | 156 | 124 | 22 | 1 | FI |
| **Total** | **1,687** | **1,377** | 78 | 10 (unique) | — |

**Agents (models), scaffold, and run protocol:** four frontier models — **Claude 4.5 Sonnet** (Anthropic), **GPT-5** (OpenAI), **GLM 4.7** (Z.ai, open-weight), **MiniMax M2.5** (open-weight) — all run through the **SWE-Agent** scaffold (Yang et al., 2024) with a shared configuration: 250-step budget, $3/instance cost cap, high reasoning effort. Each (model × condition × instance) combination is run **once** — not repeated/sampled — "to maintain tractable computational costs." This is a genuine statistical-power caveat the authors state plainly but do not otherwise mitigate (no variance/noise estimate from repeated runs).

**Analysis subset:** because the number of instances passing the PR1 filter differs by model, headline comparisons (Table 2, Table 3) use the **shared-instance subset common to all four models within each benchmark**; a supplementary table (Table A1) reports the same comparison on the **full, non-shared per-model dataset** and finds "a similar pattern" — consistency check the authors themselves ran and reported, not something this record independently re-derived.

## Key findings

**1. Headline result — agent code is harder to build on than human code, but not universally (measured; Table 2, shared-instance subset).**
Across 16 model × benchmark cells, AA underperforms HA in most cells, with the **largest single drop of 13.1 percentage points** (GLM 4.7 on SWE-Bench Pro: HA 45.2% → AA 32.0%). Full cell-level results:

| Benchmark | Claude Δ | GPT Δ | GLM Δ | MiniMax Δ |
|---|---|---|---|---|
| SWE-Bench Verified | −5.1 | −1.0 | −3.0 | −6.1 |
| SWE-Bench Multilingual | −3.1 | +3.1 | −3.1 | −3.1 |
| SWE-Bench Pro | −7.7 | +0.8 | **−13.1** | −6.9 |
| FeatBench | **+6.2** | −12.5 | −6.2 | 0.0 |

**Four of sixteen cells show AA matching or exceeding HA** (GPT +3.1 Multilingual, GPT +0.8 Pro, Claude +6.2 FeatBench, MiniMax 0.0 tie FeatBench) — recorded here with the same diligence as the negative cells, per CLAUDE.md rule 3. GPT-5's smaller SWE-Bench-variant gaps may partly reflect a lower HA baseline rather than genuine robustness to agent code (authors' own caveat). The pattern replicates on the full non-shared dataset (Table A1).

**2. Task-type stratification — refactoring hit hardest (measured; Table 3, shared-instance subset).**

| Task type | n | Avg. Δ (HA→AA) across 4 models |
|---|---|---|
| Bug fixing (BF) | 210 | **−4.05%** |
| Feature implementation (FI) | 104 | −6.25% |
| Refactoring (RF) | 70 | **−8.21%** (largest) |
| FI + RF combined | 22 | −6.82% |

The authors read this as consistent with prior findings that refactoring and multi-file edits are harder for agents than localised fixes generally (citing Xu et al. 2025; Gautam et al. 2025) — this study adds a *maintainability-specific* version of that pattern: not just "agents are worse at refactoring," but "agents are worse at refactoring **that was already started by another agent**."

**3. The central null result — static maintainability metrics do NOT explain the AA-vs-HA gap (measured; Table 4, logistic regression on the 405-instance discordant cohort).**
Restricting to the 454 "discordant" instances where HA and AA produce different pass/fail outcomes on the identical downstream issue (HA wins 64.3%, AA wins 35.7%; 405 after dropping incomplete-feature cases), the authors fit a logistic regression with four static-metric deltas (Cyclomatic Complexity, Cognitive Complexity, Halstead Volume, Logical LOC — each at both PR1 and PR2), two patch-localisation Jaccard overlaps (file-level, function-level), one behavioural-drift indicator (IEC, defined below), and a leave-one-out instance-difficulty control, plus benchmark and model fixed effects. Overall model fit: **McFadden R² = 0.069, LR χ²(18) = 36.1, p = 0.007** — a modest but statistically reliable signal, reported candidly by the authors as such (not oversold).

**Not significant** (none of the traditional static maintainability metrics predict which side of the discordant pair wins):
- Cyclomatic complexity, PR1 delta: OR 0.92 (95% CI 0.53–1.61), p=0.779
- Cognitive complexity, PR1 delta: OR 1.00 (0.67–1.48), p=0.981
- Halstead volume, PR1 delta: OR 1.03 (0.69–1.53), p=0.885
- LLOC, PR1 delta: OR 0.92 (0.53–1.61), p=0.780
- Cyclomatic complexity, PR2 delta: OR 0.71 (0.38–1.31), p=0.271
- Cognitive complexity, PR2 delta: OR 0.97 (0.69–1.37), p=0.866
- Halstead volume, PR2 delta: OR 0.93 (0.69–1.25), p=0.615
- File-level Jaccard overlap: OR 0.77 (0.58–1.01), p=0.061 (marginal, not significant at conventional threshold)
- Function-level Jaccard overlap: OR 1.22 (0.93–1.60), p=0.144

**Significant** (all three tilt the outcome toward HA winning / AA losing):
- **IEC — PR1 behavioural drift (input/error-contract), binary, LLM-judged:** OR 1.83 (95% CI 1.15–2.92), p=0.011. When the agent's PR1 alters input-validation or error-handling behaviour relative to what a human would have written, the odds of HA winning (AA failing) are 1.83× higher.
- **LLOC delta at PR2:** OR 1.88 (95% CI 1.02–3.46), p=0.042. When AA's downstream patch adds more code than HA's, HA is more likely to win — i.e. agents building on agent code tend to over-edit downstream, and that over-editing itself predicts failure.
- **Instance difficulty (leave-one-out score):** OR 1.42 (95% CI 1.12–1.78), p=0.003. Easier instances are more likely to be HA-only wins — a difficulty-control finding, not itself a maintainability signal, but confirming the regression is doing sensible work.

The authors' own framing, confirmed from the full text: "static maintainability metrics show near-identical distributions across HA-wins and AA-wins, while IEC drift, LLOC-PR2, and instance resolve rate show the clearest visual separation between the two groups." **This is the paper's most important finding for tension 4:** the exact metric family that GitClear's proprietary classifier and the CMU papers' SonarQube pipeline rely on (complexity, size/verbosity proxies, duplication) does not, in this controlled design, explain why agent-built-on-agent code fails more often downstream.

**4. What does explain it — behavioural drift, not structure (measured, with a partial causal-attribution follow-up).**
A ten-category taxonomy (Table A5, four groups: functionally-compatible / behavioural-divergence / scope / agent-failure) captures subtle differences between agent and human PR1s not visible in aggregate static metrics — e.g. an agent silently substituting `dict.get(k, default)` for what a human would have written as an explicit `raise`, or adding/removing an early-exit input check. This IEC (input/error-contract) drift is LLM-judged (DeepSeek V4 Pro) across all 2,517 model×benchmark×instance records.

**Does the drift actually cause the downstream failure, per-instance (not just population-level)?** A second LLM-judge attribution pass, run on the 262 HA-wins discordant instances with a genuine PR1 divergence (excluding 30 EQUIVALENT/STYLE cases):
- **Drift survival into PR2:** unchanged/survived 85.9% (225/262); partially corrected 7.3% (19/262); rewrote/corrected 6.9% (18/262). **The drift almost always carries through unaltered** — PR2 agents rarely notice or fix it.
- **Did the failure trace back to the drift?** Yes, compounding-confirmed: **20.6%** (54/262). No, unrelated failure: **74.4%** (195/262). Unclear: 4.6%. Not applicable: 0.4%.

Recorded with full diligence: **this specific, verified mechanism accounts for only about a fifth of the discordant-cohort failures.** The majority (74.4%) of cases where building on agent code caused a downstream failure are **not explained by IEC drift either** — the authors explicitly say they "leave this analysis to future work." This is an important self-limiting null alongside the paper's own positive finding: IEC drift is the clearest signal found, but it is far from a complete explanation.

**5. No longitudinal/multi-step degradation component — explicitly out of scope, flagged by the authors as the primary limitation.**
CodeThread as built only chains **two** steps (PR1→PR2). The authors state directly: "we consider only two-step pull request chains... this setup is sufficient to study whether the quality of an intermediate patch affects a downstream modification, [but] does not capture longer-horizon development trajectories, where technical debt may compound over multiple successive edits." They further note the 85.9% drift-survival rate "suggests that on long-horizon tasks... this drift could compound across PRs and degrade downstream resolve rates further," but state plainly: **"Our setup cannot test this directly."** **Answering the task brief's question directly: this paper does not measure whether agent code degrades faster over multiple generations or gets fixed more often over time — it measures only a single downstream step, and is explicit that this is a gap, not a finding.** The closest proxy available is the drift-survival rate above (code tends to stay as agents left it rather than being corrected by the next agent), which is suggestive of compounding but is not itself a multi-step measurement.

## Nulls and negatives (collected in one place per CLAUDE.md rule 3)

- Four of sixteen model×benchmark cells show AA ≥ HA (see Key finding 1) — agent-on-agent building is not universally worse.
- All eight static-metric coefficients (complexity ×2, volume ×2, LOC at PR1) are non-significant predictors of the AA/HA discordance direction (Key finding 3) — the paper's central null.
- File-level Jaccard overlap is only marginally significant (p=0.061) and function-level Jaccard is fully non-significant (p=0.144) — patch-localisation similarity does not clearly predict outcome.
- 74.4% of the drift-verified discordant cohort's failures are *not* attributable to the one behavioural mechanism the paper does manage to isolate — the paper's own explanatory model is honestly reported as incomplete (McFadden R²=0.069).
- No AH condition (human building on agent code) was tested — an absence, not a null, but relevant to what can and cannot be claimed.

## Confounders and task-mix (addressed directly, per the task brief's question)

**This is the paper's chief methodological strength relative to every other tension-4 source in this evidence base.** The Follow-On Issue (PR2's task) is byte-for-byte the same benchmark issue and test suite in both the HA and AA arms — task-mix is held fixed by design, not merely matched statistically (contrast with GitClear's population-level correlational design and the CMU papers' propensity-score-matched but still observational DiD designs). Residual confounders that remain, all explicitly discussed by the authors:
- **PR1 selection/filtering bias:** PR1 must fail the Fail-to-Pass tests (i.e., not already solve the Follow-On Issue) to enter the analysis — this could, in principle, select for a non-representative slice of agent behaviour, though the authors report the filter "retains a large majority of instances" and that incidental solving is rare.
- **Single run per (model, condition, instance):** no repeated-sampling noise estimate — a real but modest limitation given typical agent output variance.
- **Instance-difficulty imbalance:** controlled for via a leave-one-out covariate (and found significant, OR 1.42) rather than eliminated by design — difficulty is not literally identical across HA and AA (both see the same instance, but agents may find PR1's specific implementation easier or harder to build on for reasons difficulty alone doesn't capture).
- **Scaffold-specificity:** all four models are run through one scaffold (SWE-Agent); results may not generalise to other agent harnesses (Claude Code's own loop, Cursor's agent mode, OpenHands, Devin) not tested here.

## Limitations (authors' own, near-verbatim from the fetched text)

- **No longer-horizon chains** — two-step only; technical-debt compounding across more than one downstream edit is untested (see Key finding 5).
- **PR1 filtering may introduce selection bias** relative to agents' "natural" behaviour across the full benchmark, though argued to be minor.
- **No AH condition** (human building on agent code) — "would require recruiting developers to author PR2 across [benchmark-scale instances], which is infeasible in our current setting"; the paper therefore cannot speak to whether *human* maintainers, as opposed to agent maintainers, face the same downstream penalty building on agent-authored code.
- **Model/version/scaffold scope:** four frontier models via a single scaffold (SWE-Agent); no test of alternative scaffolds or of smaller/older models.
- **LLM-as-judge dependency** for both the IEC behavioural-drift label and the compounding-attribution label (DeepSeek V4 Pro in both cases) — no human-rater agreement check reported in the fetched text.
- **External validity:** all four benchmarks are GitHub-issue-resolution style tasks on (mostly) open-source Python/multi-language repositories; no claim is made about proprietary enterprise codebases, and the authors do not claim otherwise.

## What this can and cannot support

**Can support:** a controlled (not merely correlational) demonstration that, holding the downstream task and downstream agent fixed, code written by a frontier coding agent is on average harder for a subsequent agent to build on successfully than code written by a human, with task-resolve-rate drops of up to 13.1 percentage points, concentrated most heavily in refactoring tasks (−8.21% average) and least in bug-fixing (−4.05% average). Can support, with high confidence given the explicit statistical reporting, that **traditional static maintainability metrics (cyclomatic complexity, cognitive complexity, Halstead volume, LOC) do not explain this gap** — a genuine, well-evidenced null result. Can support, at more modest confidence (McFadden R²=0.069, and only explaining 20.6% of a sub-cohort), that subtle behavioural drift in input-validation/error-handling contracts is *part* of the mechanism, and that this drift persists into downstream code the large majority of the time (85.9%) rather than being caught and corrected by the next agent.

**Cannot support:** any claim about proprietary/enterprise codebases (OSS benchmarks only); any claim about human developers' experience building on agent code (AH untested); any claim about multi-step (3+ generation) compounding of technical debt (explicitly out of scope, flagged by the authors as future work); any claim that agent-authored code has *more* structural complexity, duplication, or code smells than human code in an absolute sense (the paper does not compare PR1 static metrics between AA and HA arms as a headline finding — it tests whether metric *deltas* predict *downstream* discordance, which is a different and narrower question); any claim generalising beyond the SWE-Agent scaffold or beyond these four specific models; and no claim about why 74.4% of the drift-verified discordant failures occur — that mechanism remains unexplained by this study's own admission.

## Cross-reference assessment for tension 4 (for orchestrator — not written to contradictions.md)

**Verdict: confirms the headline, complicates the mechanism. This is not a clean "corroborates" or "refutes" — it is a genuine complication that the human should weigh carefully before treating tension 4 as settled.**

1. **Confirms the top-line pattern.** GitClear (population-level, correlational, COI-flagged) and the CMU DiD trio (`cursor-velocity-quality-2025`, `agents-vs-ides-2026`, `he-2026-2x-mandate` — one evidentiary voice per that record's own overlap note) both report that AI/agent-era code carries a real, measurable maintenance cost: rising static-analysis warnings (+18% to +30%), rising complexity (+35% to +42%), rising duplication/copy-paste (GitClear), declining refactoring activity (GitClear). This paper adds a **third, independent, and differently-designed** line of evidence pointing the same direction: agent-authored code is measurably harder to build on than human-authored code, holding the downstream task fixed. As the first source in this evidence base with (a) no author overlap with the CMU cluster and (b) no data overlap with GitClear or AIDev, **this is the independent academic leg the COI flag on GitClear has been asking for.**

2. **Complicates the mechanism significantly.** GitClear's eight signals and the CMU papers' SonarQube pipeline are exactly the static/structural metric family (complexity, duplication, warnings, verbosity) that CodeThread's own regression finds **does not predict** where the agent-vs-human authorship gap actually bites. If the true mechanism is subtle behavioural-contract drift (input validation, error handling) rather than structural bloat, then a research programme built entirely on static analysis (as GitClear's and the CMU trio's are) may be measuring a real but partially *different* phenomenon than the one that actually drives downstream task failure — or measuring a correlate of it rather than the cause. This does not refute GitClear/CMU's findings (their metrics genuinely do rise, and that is worth caring about in its own right, e.g. as a proxy for review burden or as a signal correlated with something real), but it means "rising complexity/duplication" and "agent code is harder to build on" should not be treated as the same claim with two different measurement methods — CodeThread suggests they may be two different claims that happen to correlate with the same underlying trend (increasing agent authorship) without one being a good proxy for the other.

3. **Construct-validity point for RQ2:** this is a clean illustration of the self-report-vs-measured-style methodological question, generalised — here it is "structural metric" vs "task-outcome/behavioural metric" as two different *measured* operationalisations of the same word, "maintainability," that diverge. Worth flagging in the RQ2 synthesis memo as a case where even fully measured (non-self-report) evidence can disagree because the underlying construct is being operationalised differently, not because either measurement is wrong.

4. **Task-type granularity is a genuine addition.** Every population-level source in this evidence base (GitClear: no task-type decomposition at all; the CMU DiD trio: repo-month aggregates explicitly flagged as "T-mixed/unresolved" in `agents-vs-ides-2026`) cannot decompose by task type. This paper can, and does: refactoring (T5) shows the largest average drop (−8.21%), bug-fixing the smallest (−4.05%). This is a useful, independent data point for RQ3's task-type failure map specifically for T5, converging with the general "refactoring/complex multi-file work is where agents struggle most" pattern already suggested by Stanford/Denisov-Blanch (tension 2) and the CMU papers' complexity findings, now from a controlled rather than observational design.

5. **Duplication specifically:** neither this paper nor `agents-vs-ides-2026` (duplicate density null in both AF/IF cohorts) nor `cursor-velocity-quality-2025` (duplicate density null, +7.03% n.s.) finds a significant duplication effect in a controlled/quasi-experimental design — three separate designs now agree that **duplication is the weakest leg of the quality-debt story once you move from GitClear's raw population telemetry to any design with tighter controls.** This paper doesn't measure duplication directly as an outcome (it's one of the non-significant PR1/PR2 predictors, not a headline metric), but it is consistent with, and adds a fourth data point to, a pattern worth flagging in synthesis: duplication rises in the raw population trend (GitClear) but does not clearly survive in every design that controls harder for confounders.

**Recommend for the human's contradictions/synthesis pass:** do not log this as a contradiction against GitClear or the CMU trio — the headline direction agrees. Instead, log it in the tension-4 synthesis memo as a **mechanism complication**: the specific static-analysis metrics used across most of this evidence base's "quality debt" sources are shown, by the one genuinely controlled design available, to not explain the maintainability cost they are typically invoked to represent. This affects how much weight RQ6's internal-measurement recommendations should put on static-analysis-metric monitoring (complexity/duplication dashboards) as an early-warning system for agent-code maintainability risk — this paper suggests such dashboards may under-detect the actual failure mode.

## Follow-up leads (for Phase 1 queue — not extracted)

1. **Cynthia, S. T., Muttakin, A., & Roy, B. (2026). "Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests."** arXiv:2601.20109. Cited in this paper's related work; directly on-topic for tension 4 and not yet in this evidence base's leads list.
2. **Huang, H. et al. (2026). "More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment Towards AI-Generated Pull Requests."** arXiv:2601.21276. New lead; the "reviewer sentiment" angle is relevant to RQ2/RQ6 (how maintainers perceive AI PRs) as well as tension 4.
3. **Paul, D. G., Zhu, H., & Bayley, I. (2025). "Investigating the Smells of LLM Generated Code."** arXiv:2510.03029. Static-analysis code-smell comparison; worth checking against this paper's null on structural metrics.
4. **Orlanski, G. et al. (2026). "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks."** arXiv:2603.24755. This is the paper that could plausibly supply the **longitudinal/multi-step degradation component CodeThread explicitly says it cannot test** — high-priority lead for closing that specific gap.
5. **Wang, Z. et al. (2025). "MaintainCoder: Maintainable Code Generation Under Dynamic Requirements."** arXiv:2503.24260. Prior work using synthetic requirement changes + static metrics (CC, AST similarity) on sequential tasks — a methodological sibling worth comparing CodeThread's design against.
6. **Chen, J. et al. (2026). "SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration."** arXiv:2603.03823. Uses test-pass-rate-over-iterative-edits as a maintainability proxy — another candidate for the longitudinal gap.
7. **arXiv:2605.20049 — "Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study"** (surfaced via WebSearch, not yet checked against this paper's authors/dataset). Tests the reverse-direction mechanism (does starting from clean vs messy code affect agent performance) — a natural complement to CodeThread's agent-vs-human authorship framing; queue for triage.
8. **arXiv:2606.13175 — "The End of Code Review: Coding Agents Supersede Human Inspection"** (surfaced via WebSearch). Title suggests direct relevance to T7 (code review) and possibly to tension 6 (bottleneck displacement); queue for triage, not yet read even at abstract level.
9. **Deng et al. (2025), SWE-Bench Pro (arXiv:2509.16941)** and **Chen, Li & Li (2025), FeatBench (arXiv:2509.22237)** — the two benchmark-construction papers underlying the largest and most agent-sensitive slices of this study's sample; worth a light check if the synthesis phase needs to understand what "SWE-Bench Pro" tasks actually look like (described in this paper only as "longer, multi-file edits drawn from professional codebases").
10. **The paper's own GitHub replication package** (https://github.com/shaswatpatel123/CodeThread) — not fetched in this pass; would let a future session verify the ten-category behavioural-drift taxonomy's inter-rater reliability or re-run the regression, if that level of verification is ever wanted.

## Recency check notes

Paper is ~2.5 weeks old at verification (19 Jun 2026 → 6 Jul 2026), far inside the 12-month threshold — the CLAUDE.md rule 8 mandatory recency search was not required, but one WebSearch was run anyway given the paper's likely centrality to tension 4. No retraction, no erratum, no v2, no secondary discussion or critique found; the arXiv abstract page confirms a single version. Given its freshness, treat as a genuinely live, unreviewed preprint — the absence of peer review is itself worth carrying into any exec-brief citation of this source (it has not yet been through venue review, unlike the MSR '26-accepted CMU papers already in this evidence base).
