# Google — two same-org papers on LLM-assisted code migration (combined record)

Covers, as one record per the assignment brief:
- **(a)** Nikolov, Codecasa, Sjövall, Tabachnyk, Chandra, Taneja, Ziftci — "How is Google using AI for internal code migrations?" arXiv:2501.06972 (Jan 2025)
- **(b)** Ziftci, Nikolov, Sjövall, Kim (Bo), Codecasa, Kim (Max) — "Migrating Code At Scale With LLMs At Google." arXiv:2504.09691 (Apr 2025)

## Citation (with version history)

- **(a)** Stoyan Nikolov, Daniele Codecasa, Anna Sjövall, Maxim Tabachnyk, Satish Chandra, Siddharth Taneja, Celal Ziftci. "How is Google using AI for internal code migrations?" arXiv:2501.06972 [cs.SE], submitted 12 Jan 2025 (v1, checked — no later version found). Peer-reviewed and published at **ICSE 2025, Software Engineering in Practice (SEIP) track**. The arXiv copy and the ICSE SEIP version are the same paper; arXiv is the accessible copy used for this extraction (no paywall issue — ICSE proceedings are behind ACM/IEEE but the arXiv preprint is the identical text per the authors' own cross-reference in paper (b)).
- **(b)** Celal Ziftci, Stoyan Nikolov, Anna Sjövall, Bo Kim, Daniele Codecasa, Max Kim. "Migrating Code At Scale With LLMs At Google." arXiv:2504.09691 [cs.SE, cs.AI], submitted 13 Apr 2025 (v1). Peer-reviewed and published at **FSE 2025 (33rd ACM International Conference on the Foundations of Software Engineering), Industry Papers / Companion track**, Trondheim, June 2025 (DOI 10.1145/3696630.3728542). CC BY 4.0.
- Both papers are **industry/practice-track**, not research-track, at their respective venues — i.e. they went through peer review, but the bar for an industry-track submission is "is this a credible, well-described experience report," not "does this meet research-methodology standards." Paper (a) explicitly disclaims research-study status itself (see below).
- No later versions, corrections, or retractions found for either arXiv ID as of this check (July 2026).

## Verification status

**VERIFIED, not blocked.** Both papers exist, are exactly as titled, are openly accessible on arXiv (no preprint-substitution needed), and are confirmed as peer-reviewed industry-track papers at ICSE 2025 and FSE 2025 respectively (cross-checked against conf.researchr.org and dl.acm.org listings). Headline figures (80% AI-authored, 50% time saving on the int32→int64 migration; 74.45%/69.46% LLM-generated share and the 39-ID/595-change/93,574-edit scale in paper (b)) are corroborated by independent third-party coverage (The Register, 16 Jan 2025) and by a companion Google Research blog post ("Accelerating code migrations with AI") — all report the same numbers, indicating internal consistency rather than drift across restatements.

**Recency check (both sources are 15–18 months old as of July 2026, over the 12-month threshold):** one search cycle run. No retraction, erratum, or substantive critique found. Both papers are cited positively and uncritically by 2026 code-migration papers (e.g. a ReCode '26 benchmark paper and an "Environment-in-the-Loop" agentic-migration paper both cite Ziftci et al. as prior art without disputing its numbers). Treat as stable and unsuperseded.

## What kind of documents these are

**Paper (a) explicitly and verbatim disclaims being a research study.** Direct quote from the paper itself:

> "It is not a research study, in the sense that we do not carry out comparisons against other approaches or evaluate research questions/hypotheses."

and:

> "Rather, we share our experiences in applying LLM-based code migration in an enterprise context across a range of migration cases, in the hope that other industry practitioners will find our insights useful."

This is a **self-declared experience report / practice-track write-up**, not a controlled study. It should never be cited as if it carries the evidentiary weight of a study with a comparison condition.

**Paper (b) is a narrower, more instrumented follow-up on one of (a)'s four case studies** (the int32→int64 migration), submitted three months later. It does not carry the same explicit "not a research study" disclaimer, and it is materially more rigorous in method: it reports an explicit "Threats to Validity" section, uses a measured proxy metric (Levenshtein edit distance) for one of its two headline numbers, and flags its own self-report limitation in-text (see Measurement basis below). It is best characterised as a **case study with partial instrumentation**, one step more rigorous than a pure experience report but still well short of Tier A/B — no control group, no counterfactual condition, single organisation, single migration type, three developers.

## Independence relationship between (a) and (b) — graded explicitly

**Not independent — same organisation, overlapping authorship, same underlying case.** This is a single evidentiary data point presented as two publications, not two corroborating sources:

- **Author overlap:** Nikolov, Sjövall, and Codecasa appear on both papers; Ziftci is lead author on (b) and a co-author on (a). Only Tabachnyk, Chandra, Taneja (paper a) and Bo Kim, Max Kim (paper b) are non-overlapping.
- **Same case study, different depth:** paper (b) is explicitly framed by its own authors as an elaboration of the same effort introduced in (a). Direct quote from (b): "We previously shared high-level information about this work (Nikolov and Taneja, 2024; Nikolov et al., 2025), in this paper we discuss our approach, success metrics, results and learnings in great detail." Paper (b)'s entire case study (the int32→int64 ID migration at Google Ads, three developers, headline "50% time saving" / "80% AI-authored") is very likely the *same underlying migration programme* as paper (a)'s "Case 1," now reported with twelve months of accumulated telemetry (39 distinct ID migrations, 595 changes, 93,574 edits) rather than the single-snapshot figures in (a).
- **Non-overlapping content:** paper (a) additionally covers three migrations not present in (b) at all — JUnit3→JUnit4, Joda-Time→java.time, and an experimental-flag cleanup effort. Paper (b) covers only the int32→int64 case, in much greater quantitative and methodological detail.
- **Practical implication for triangulation (§3):** treat this pair as **one organisation, one rollout family** for the purposes of the protocol's "three independent Tier C sources" rule — it cannot on its own satisfy that bar, and should be counted as a single vendor-adjacent data point when cross-referenced against other companies' migration write-ups.

## Tier, era, independence, COI

- **Tier: C**, with the caveat above that (b) is closer to the top of Tier C than (a). Neither is Tier A/B — no control condition, no randomisation, and (a) explicitly disclaims hypothesis-testing.
- **Era: E3 (agentic-ish, bespoke pipeline)** by tooling modality, not by publication year. This is not a chat-assistant workflow (E2) — the described system is a **multi-stage, largely autonomous pipeline**: automated discovery of change locations (Kythe/Code Search/AST/regex), automated LLM-based edit generation, an automated validate→repair loop (build/test execution with optional ML-powered fix retry, "pass@k" ranking across parallel prompt variants), with humans in the loop only at final code review and rollout. The authors themselves note a deliberate choice *against* general LLM-agent planning: "We discovered that LLM planning capabilities are often not needed and add a layer of complexity that should be avoided when possible." This is best tagged **E3 by modality (plan→execute→verify loop) but explicitly *not* a general-purpose coding agent** — it is a bespoke, task-specific automation pipeline with an LLM component for the generation step only, fine-tuned Gemini for code generation/validation. Flag this nuance wherever the record is used: it is agentic in structure (autonomous multi-step loop with verification) but not an instance of "Claude Code / Cursor-style general agent" E3 tooling — a distinct sub-category worth carrying into RQ1/RQ3 tooling taxonomy discussions.
- **COI flag: YES — vendor self-report.** Both papers are written by Google engineers about Google's own internal tooling and Google's own migration outcomes, using Google's own internal LLM (fine-tuned Gemini) and Google's own infrastructure (Kythe, internal code search). There is no external author, no independent auditor, and the authors who built the system are largely the same people evaluating it and (in paper b) the same people interviewed for satisfaction/time-saving self-reports (see Limitations below — the authors flag this bias themselves). Grade as **Tier D-adjacent in spirit** (vendor-about-its-own-practice) even though it sits in Tier C by the protocol's formal definition (practitioner case study with real numbers) — record both gradings so downstream synthesis doesn't lose the nuance.

## Method & population

- **Design:** non-controlled, retrospective case studies of internal migration efforts at Google, described by the engineers who built and ran the tooling and (in paper b) by structured post-migration interviews with the three developers who used it.
- **Population:** (a) multiple migration efforts across Ads and other Google product areas, scale not consistently quantified per case beyond individual migration statistics. (b) exactly **three developers**, performing **39 distinct ID migrations** over **twelve months**, reviewed by 306 distinct reviewers across 149 teams, 37 offices, 12 time zones (breadth-of-review context, not breadth of the core population studied).
- **Task-type tag: T5 (refactoring / tech debt — migrations, dependency upgrades)** for all case studies in both papers. Cross-cutting note: these are near the mechanical end of T5 — well-specified, mechanically verifiable transformations (type widening, API-shape changes, library swaps) rather than open-ended design work; see task-nature discussion below.

## Migration case studies — exact numbers as reported

### Paper (a) — four cases

**1. int32→int64 ID migration (Google Ads, ~500M+ line codebase per third-party coverage):**
- Scale: "tens of thousands of code locations across thousands of files"; full manual-effort estimate "hundreds of software engineering years."
- Time saving: "reduced by an estimated **50%**."
- AI-authorship: "**80%** of the code modifications in the landed CLs were fully AI-authored, and the rest were human-authored or edited from the AI suggestions."
- Measurement basis: **AI-authorship (80%) = measured** (automated diff tracking — "The first version (known internally as snapshot) of the changelist is the one generated by the LLM-powered tooling. The version actually committed to the repo is compared to this and a per-character difference is calculated.") **Time saving (50%) = self-reported** ("estimated ... as reported by the engineers doing the migration, when compared to a similar exercise carried out without LLM assistance" — no counterfactual measurement, an engineer estimate against a remembered/inferred manual baseline).

**2. JUnit3→JUnit4:**
- Scale: "migrated **5,359 files** modifying more than **149,000 lines of code** in **3 months**."
- AI quality: "**∼87%** of the code generated by AI ended up committed without any change."
- Measurement basis: scale figures = **measured** (tooling telemetry, direct counts). The 87% figure's precise computation is not spelled out as explicitly as the int32→int64 diff method, but is consistent with the same snapshot-vs-committed diffing approach described elsewhere in the paper — treat as **measured**, with the caveat that the paper does not restate the methodology for this specific case.

**3. Joda-Time→java.time:**
- Time saving: "**∼89%** of the time it would have taken humans to do the change in the small clusters."
- Measurement basis: **self-reported** — "The number is calculated across multiple changes where human experts (team technical leads) have compared their experience with the AI-powered tooling to the previous purely-manual approach." Status: explicitly "still ongoing" at time of writing, with known unresolved issues (see Limitations).

**4. Experimental-flag / dead-experiment-code cleanup:**
- No numeric effect size given — "thousands of runtime experiments" is a scale statement only. Explicitly flagged as having the hardest remaining technical problems (impure test cleanup) of the four cases.

**Cross-cutting threshold statement:** "The measure of success we adopt is whether there is *at least a 50% acceleration* in task completion rate in an ongoing project" — i.e. 50% is a pre-set internal success bar as much as an empirical finding, which should be borne in mind when the 50% figure recurs across both papers.

### Paper (b) — one case, in much greater depth (int32→int64, likely the same underlying programme as paper (a) case 1)

- Scale: "**39 distinct migrations** undertaken by **three developers** over **twelve months**"; "**595 code changes** with **93,574 edits** have been submitted"; "**74.45%** of the code changes and **69.46%** of the edits were generated by the LLM"; review footprint of 306 reviewers / 149 teams / 37 offices / 12 time zones.
- Time saving: developers "reported ... an estimated **50% reduction** on the total time spent on the migration compared to earlier manual migrations."
- Human-only fallback: **25.55%** of code changes and **30.54%** of edits were human-authored/human-fixed — i.e. the LLM-failure/inapplicability rate, including hallucination cases the authors describe developers as having to "manually handle."
- Measurement basis: **74.45%/69.46% LLM-generated share = measured**, via a defined proxy metric — "We track every code change in both categories, calculate the total edits across all files in all code changes related to the migration of an ID, and compare the LLMΔ and HumanΔ for the entire ID," using Levenshtein edit distance "as a proxy to measure the effort required." **50% time saving = self-reported, and the paper says so itself**, explicitly under a "Threats to Validity" heading: "the reported 50% time savings is based on developer perception and estimations, and not on precise time tracking data. Although their estimations are in line with the proportion of automatically generated code changes and edits, there may be potential inaccuracies in their assessment of efficiency gains." This is the clearest self-flagged measured-vs-self-reported delta in either paper and should be the anchor quote used wherever this pair is cited for RQ2.
- Developer satisfaction: qualitative only — "reported high satisfaction" from post-migration interviews with the three developers; no quantitative scale reported.

### Measurement-basis summary table

| Finding | Value | Basis | How measured / quote |
|---|---|---|---|
| (a) int32→int64 AI-authored share | 80% | Measured | Per-character diff, snapshot vs. committed CL |
| (a) int32→int64 time saving | 50% | Self-reported | Engineer estimate vs. remembered/inferred manual baseline, no counterfactual |
| (a) JUnit3→4 scale | 5,359 files / 149k LOC / 3 months | Measured | Tooling telemetry (implicit) |
| (a) JUnit3→4 unmodified-commit rate | ~87% | Measured (methodology not restated for this case) | Consistent with snapshot-diff method used elsewhere |
| (a) Joda→java.time time saving | ~89% | Self-reported | Tech-lead expert comparison of "their experience," no time-tracking data |
| (b) int32→int64 LLM-generated share (changes/edits) | 74.45% / 69.46% | Measured | Levenshtein-distance proxy (LLMΔ vs HumanΔ), automated telemetry over 12 months |
| (b) int32→int64 time saving | 50% | Self-reported (explicitly flagged by the authors as a "threat to validity") | Developer perception/estimation, "not ... precise time tracking data" |
| (b) developer satisfaction | qualitative, "high" | Self-reported | Post-migration structured interviews, no numeric scale |
| (b) human-fallback rate | 25.55% changes / 30.54% edits | Measured | Same telemetry/diff tracking as the LLM-share figures |

**No effect size in either paper should ever be quoted without this basis tag attached** — the two headline "50%" figures (one per paper, likely describing overlapping or identical underlying work) are both self-reported, un-instrumented estimates, while the AI-authorship/LLM-share percentages are the only genuinely measured headline numbers.

## Task nature — mechanical vs. open-ended (T5 characterisation)

All five case studies (four in (a), one — in more depth — in (b)) sit toward the **mechanical/repetitive end of T5**, not the open-ended end:
- int32→int64: a type-widening transformation with a well-defined target state, applied at scale across many structurally similar call sites; discovery is automatable via static analysis (Kythe reference-graph traversal), and correctness is largely checkable by build/test.
- JUnit3→JUnit4: a well-specified API-shape migration between two known library versions.
- Joda-Time→java.time: a library-swap migration with a documented target API.
- Experimental-flag cleanup: the *one* case explicitly flagged by the authors as harder and less mechanical — it requires judging which tests are "pure" versus which silently depend on removed experiment states, which the authors say "are very difficult for humans as well."
- The authors themselves draw the mechanical/open-ended distinction explicitly, favouring deterministic AST tooling over LLM "planning": "AST-based tooling has the advantage [of being] 'always correct' ... We discovered that LLM planning capabilities are often not needed and add a layer of complexity that should be avoided when possible." This is a direct practitioner statement that **their** LLM value-add is narrowly in the edit-generation step of an otherwise mechanical, deterministic pipeline — not in open-ended reasoning or planning.

## Tooling and era by modality

- **Not a general chat assistant, not a general autonomous agent.** A **bespoke, task-specific migration pipeline** with these stages (both papers describe essentially the same architecture, paper (b) in more implementation detail specific to the ID migration):
  1. **Discovery** — Kythe cross-reference graph traversal (paper b: direct + indirect references up to graph-distance 5) plus Code Search, regex, and AST-based filtering/categorisation (buckets: Not-migrated / Irrelevant / Relevant / Left-over in paper b).
  2. **Generation** — a **fine-tuned Gemini model** ("a version of the Gemini model that we fine-tuned on internal Google code and data"), using language-appropriate prompts, with a "pass@k" strategy trying multiple prompt variants in parallel and ranking them.
  3. **Validation/repair loop** — automated build/test execution with an optional ML-powered repair retry; paper (b) specifies six ordered validation gates (Success, Whitespace, AST parser, Punt, Build, Test) — a file failing any gate is discarded from automation and routed to manual migration.
  4. **Review/rollout** — explicitly and repeatedly flagged by the authors as **still human-driven and the emergent bottleneck**: "Code reviews and change rollouts still require a human operator and can quickly become bottlenecks ... We needed to slow down some of the migration work to avoid overwhelming the teams that had to do the reviews."
- **Era classification:** tag as **E3 by modality** — an autonomous, multi-step, plan→execute→verify(→repair) loop, not single-shot inline suggestion (E1) or manual copy-paste chat (E2) — but explicitly **sub-tag as "bespoke pipeline," distinct from general-purpose coding agents** (Claude Code/Cursor/Devin-class). The authors' own framing supports this distinction: they deliberately avoided giving the LLM open-ended planning autonomy, confining it to the generation step within a deterministic scaffold. Any use of this source for RQ1/RQ3 tooling comparisons should preserve this bespoke-vs-general-agent distinction rather than lumping it in with general-agent E3 evidence.

## Limitations, caveats, and unvalidated claims (authors' own words)

- **(b), Threats to Validity, self-report limitation (the single most important caveat in either paper):** "the reported 50% time savings is based on developer perception and estimations, and not on precise time tracking data."
- **(b) effort-metric validity:** "The study uses Levenshtein edit distance as a measure of developer effort, which may not fully capture the cognitive load and complexity involved in code modifications."
- **(b) generalisability, three separate statements:** "Our case study was conducted within the specific context of Google's development environment and infrastructure, which may limit the generalizability of the findings to other organizations." / "Our case study focuses on a specific type of code migration, migrating identifiers from 32-bits to 64-bits. Our results may not generalize to other types of migrations." / "the generalizability of our results on migrations to other LLMs may be limited."
- **(b) sample size:** "39 ID migrations conducted by three developers, which may not be representative of the full range of other types of code migration tasks and developer experiences."
- **(b) self-selection/insider bias, explicitly acknowledged:** "The developers involved in the case study were also involved in the development of the system by providing feedback, potentially introducing bias in their assessment of the system's effectiveness."
- **(b) known technical failure modes:** context-window overflow on large files causing "Success" gate failures; poor Dart support ("the LLM was not trained on enough Dart code"); non-determinism across runs; hallucinations requiring manual handling, constituting the 25.55%/30.54% human-fallback share.
- **(a) Joda-Time migration, still-open problems:** "we have challenges to solve. Sometimes, huge clusters arise and require us carefully ordering the changes and synchronizing with code reviewers. We need to improve some of the call-graph logic as connections are sometimes missed when components depend on each other through Guice."
- **(a) experimental-flag cleanup, explicitly the hardest case:** "The most challenging part is cleaning up the right tests ... in some cases the tests are not 'pure' ... Such cleanups are very difficult for humans as well ... Addressing these unit tests cleanup is a future area of research for the team."
- **(a) code-quality impact — explicitly marked as unvalidated/unknown:** "Currently the quality is assured through the manual review process of the code - same as for purely human-generated code. Whether there is a long-term impact on quality remains to be seen." This is a direct authorial admission that no long-term quality/defect data exists for AI-authored migration code — should be carried into RQ3/RQ4 as an explicit evidence gap, not filled in by inference.
- **(a) measurement-rigour admission, general:** "For fully completed migrations, we were able to estimate accurately the time savings (mostly based on historical data), while for some of the ongoing ones ... we relied on the expert engineers estimating a time-saving ... and we extrapolated from that" — i.e. even the "more solid" time-saving figures rest on historical-record estimation rather than a designed counterfactual, and the "ongoing" ones are explicitly extrapolated from expert guesses.
- **(a) failure/revert admission:** "we discovered that in most cases, the human needed to revert at least some changes the model made that were either incorrect or not necessary" — a direct qualitative signal of non-trivial rework, with no quantification offered.
- **(a) explicit model-vs-business-metric caveat:** "Bad model-level performance can compromise business-level outcomes, but good model-level performance does not guarantee good business-level outcomes, since the ML model is only one part of a complex transformation task" — the authors' own warning against over-reading model-quality metrics as business-value proof.

**No number in either paper is presented with a confidence interval, statistical test, or comparison/control condition.** Every effect size is a point estimate from a single organisation's internal case study.

## What this can and cannot support

**Can support:** (1) a Tier C, T5-tagged directional signal that mechanical, well-specified migration/refactoring tasks are a favourable use case for LLM-assisted automation *when embedded in a deterministic discovery/validation scaffold*, with review/rollout as the emergent human bottleneck (relevant to §5 tension 6, bottleneck displacement); (2) a methodology exemplar for RQ2 — paper (b) is one of the few practitioner sources that explicitly separates a measured proxy (LLM-generated edit share via Levenshtein distance) from a self-reported outcome (50% time saving) and flags the latter as unvalidated in its own text, making it a clean illustration of the measured/self-reported gap the protocol is tracking; (3) an example of a genuinely E3-by-modality (autonomous plan→execute→verify loop) but deliberately non-general-agent architecture, useful for refining the E3 tooling taxonomy in RQ1/RQ3.

**Cannot support:** (1) any claim about open-ended feature development, design work, or brownfield tasks requiring judgement beyond mechanical transformation (T4-style claims) — both papers are explicit that their tasks are narrow and well-specified, and that LLM planning autonomy was deliberately avoided; (2) any quantified code-quality or defect-rate claim — the authors themselves say long-term quality impact "remains to be seen" and is assessed only via ordinary human code review, identical to non-AI code; (3) any claim that the 50% time-saving figure is a validated, counterfactual-measured effect — it is self-reported in both papers, and paper (b) says so explicitly; (4) generalisation beyond Google's own infrastructure, this one migration type (b), or beyond n=3 developers (b) — the authors state all three limits themselves; (5) triangulation weight as if these were two independent organisations — they are one organisation's rollout, told twice, with overlapping authorship and (very likely) an overlapping underlying case.
