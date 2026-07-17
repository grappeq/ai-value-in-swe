# Source: METR — "Analyzing coding agent transcripts to upper bound productivity gains from AI agents"

**source_id:** `metr-2026-transcript-bound`
**URL:** https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/
**Author:** Amy Deng (METR)
**Publication date:** 17 February 2026 (confirmed against primary text; matches the date implied by the task)
**Type:** METR research note (blog-style, not a peer-reviewed paper)
**Fetched:** via three targeted WebFetch passes on the live page (full text + two follow-up passes for verbatim quotes on headline figures, RCT comparison, and task-type/cost detail). Not paywalled; no preprint substitution needed.

**Identity check:** confirmed. Title, author, date, and URL match the task brief exactly. This is a genuine METR publication, distinct from (but explicitly building on and referencing) METR's July 2025 human-uplift RCT (the "−19%" study already anchored in PROTOCOL §5, tension 1).

---

## Method summary (verify-first)

METR analysed **5,305 Claude Code transcripts** generated in **January 2026 by 7 METR technical staff** (internal employees, confidential transcripts excluded). For each transcript they computed a **"time savings factor"**:

```
time savings factor = (LLM-judge-estimated hours an experienced, high-context engineer
                        would need to produce the net successful output)
                        / (measured time-with-AI)
```

- **Time-with-AI** = sum of 10-minute windows containing ≥1 user-typed message; concurrent agent sessions in the same window counted once, not multiplied.
- **Time-without-AI** = estimated by an LLM judge (GPT-5, reading GPT-4o-compressed transcripts), explicitly instructed to exclude: failed tasks (0 min), agent overhead/session management (0 min), abandoned/pivoted work (0 min), self-explanation of same-session code (0 min), spurious agent-introduced-bug correction (0 min), and to estimate only time-to-design (not full documentation) for verbose planning.
- Per-person point estimates use **bootstrapping over the daily time savings factor**.

This is **explicitly not an RCT and not a measured outcome**: there is no control condition, no randomisation, and the counterfactual ("how long would this have taken without AI") is itself a model-generated estimate, not an observed one. It sits in a third category the schema doesn't natively have a slot for: **modelled/estimated counterfactual**, distinct from both "measured" (e.g. telemetry-observed task completion time in an RCT arm) and "self-reported" (a human's own estimate). Recorded as such throughout below — do **not** file this under "measured."

---

## Grading

- **Tier: C** (practitioner/internal-org signal, with above-average methodological transparency for the tier — bootstrapped CIs, an explicit LLM-judge validation exercise, and enumerated limitations). It does not qualify for Tier A (no randomisation, no true counterfactual measurement) or Tier B (not large-N in the sense that matters here — 5,305 transcripts sounds large, but the population is 7 individuals at a single organisation in a single month; person-level N is what determines generalisability, and 7 is small). Per CLAUDE.md instruction, graded on method: an exploratory single-org modelled-counterfactual analysis, not a controlled study.
- **Era: E3** (agentic). Unambiguous — Claude Code, multi-file/multi-session agent use, explicit discussion of "concurrency" across simultaneous agent sessions is a distinctly agentic-era phenomenon with no E1/E2 analogue.
- **Independence / COI flag:** METR is an independent AI-safety evaluation nonprofit, not a vendor selling coding tools, and its prior work (the 2025 RCT) was if anything *unflattering* to AI-agent productivity claims — this cuts against treating it as promotional. However, flag two things: (1) METR conducts paid safety evaluations for and receives model access from frontier labs including Anthropic, whose product (Claude Code) is the sole tool studied here — a soft, non-financial-in-the-obvious-sense independence consideration worth noting, not a Tier D vendor case. (2) The population is METR's *own staff* studying their *own* usage — an internal case study, not a third-party audit. Not COI-flagged as Tier D, but independence caveat recorded in `independence_flags` below.
- **Population caveat:** 7 people, all at one AI-safety research org (not a typical software engineering shop — METR's work skews toward research infrastructure, evaluation harnesses, and experiment code), one month, one tool. Generalisability to typical enterprise SWE contexts is unclear and untested by the authors themselves.

---

## Findings (one record each)

### F1 — Headline time-savings-factor range (soft upper bound)
"Time savings factors between ~1.5x and ~13x on the tasks contained in the Claude Code transcripts" across the 7 staff (individual point estimates from the results table: 2.11x–11.62x; the ~1.5x–13x range appears to reflect the width including bootstrapped CI tails). The authors are explicit this is a **ceiling, not an estimate of true productivity uplift**: "I believe the time savings factor overestimates AI-enabled productivity gains" and "I believe that the empirically measured time savings factor for an individual serves as a soft upper bound for both their productivity multiplier on Claude Code-assisted tasks and across all work."
- **Measurement basis:** modelled/estimated counterfactual (neither measured-outcome nor self-report — the numerator is an LLM judge's estimate, not an observed baseline).
- **Can support:** an upper-bound ceiling on plausible task-level time compression from Claude Code, for the specific population studied, to be triangulated against lower-bound/measured evidence (e.g. the 2025 RCT).
- **Cannot support:** any point estimate of actual productivity uplift, any claim about typical enterprise engineers, any claim about full-workday throughput, or any causal comparison across individuals (concurrency correlation is explicitly flagged as non-causal).

### F2 — Per-individual results table
| Staff | Time savings factor | Avg main-agent concurrency | Avg total concurrency | Active days |
|---|---|---|---|---|
| A | 11.62x | 2.32 | 2.74 | 26 |
| B | 6.34x | 1.52 | 1.57 | 19 |
| C | 5.08x | 1.4 | 1.48 | 18 |
| D | 3.9x | 1.17 | 1.25 | 11 |
| E | 3.33x | 1.19 | 1.29 | 20 |
| F | 3.15x | 1.26 | 1.38 | 20 |
| G | 2.11x | 1.05 | 1.07 | 11 |

No overall/aggregate single point estimate (e.g. geometric mean across all 7) is given anywhere in the note — only the range and this per-person table.
- **Measurement basis:** modelled/estimated counterfactual per person, bootstrapped.
- **Can support:** illustrating large between-individual variance (>5x spread) in even the *upper bound* — itself evidence against a single "the multiplier is X" narrative.
- **Cannot support:** population-level central tendency (no n, no mean/median reported); cannot be pooled into a single headline number responsibly.

### F3 — Concurrency correlates with time-savings factor
"Higher daily average concurrency (main and total) is associated with a higher time savings factor," with the authors immediately caveating causality cannot be established from this design.
- **Measurement basis:** modelled/estimated (correlational, non-causal per authors' own statement).
- **Can support:** a hypothesis that multi-agent/concurrent-session workflows are where the largest apparent gains cluster — relevant to RQ5/RQ6 as a mechanism to watch, not a proven driver.
- **Cannot support:** a causal claim that running more concurrent agents *causes* higher productivity; equally consistent with selection (staff who concurrency-multitask may also pick more parallelisable/lower-complexity tasks).

### F4 — Task substitution effect (counterfactual-value discount)
"With AI assistance, people sometimes complete tasks they wouldn't do otherwise, such as making nice-to-have tools. These tasks tend to deliver lower counterfactual value." Cites survey data (apparently drawing on Anthropic's own published productivity-conversation research, referenced in the note): **27% of Claude-assisted work "wouldn't have been done otherwise."**
- **Measurement basis:** self-reported (survey), cited by METR as an external supporting data point, not independently measured by METR in this transcript study.
- **Can support:** a specific, named mechanism (task substitution) by which time-savings factors overstate real productivity value — directly feeds RQ4 (cost/value profile: work done only because AI made it cheap is not free-standing value) and RQ6 (a caution against "time saved" as a sufficient metric).
- **Cannot support:** a precise quantification of how much this discounts METR's own 1.5x–13x figures — the 27% figure is an external, differently-scoped statistic, not applied arithmetically to METR's own data.

### F5 — Task selection bias
"People don't spend their entire workday using AI—they use it only on tasks where they expect it to be helpful... the time savings factor likely overestimates total AI-enabled uplift."
- **Measurement basis:** authors' own methodological reasoning (not itself a measured or self-reported figure — a stated limitation/assumption).
- **Can support:** the general RQ1/RQ5 caution that per-task multipliers on AI-selected tasks cannot be extrapolated to whole-workday or whole-team productivity.
- **Cannot support:** any specific discount factor — no number is attached.

### F6 — Worker specialisation confound
"Individuals typically do tasks they specialize in, and thus take less time than an experienced SWE on average. Therefore, the measured time savings factor probably overstates their actual time savings."
- **Measurement basis:** authors' methodological reasoning (stated limitation).
- **Can support:** a caution that the LLM judge's "experienced, high-context engineer" baseline may be a worse comparator than assumed, inflating the numerator and thus the ratio.
- **Cannot support:** any quantified correction.

### F7 — LLM-judge validation against human ground truth (n=34)
"On average, the LLM judge's predictions fall within 2-3x of human estimates" on 34 ground-truth labels. Correlation: LLM judge (GPT-5) r_log = 0.83, versus human-to-human r_log = 0.67, versus a Claude 4.5 Sonnet judge r_log = 0.46–0.48. Authors note "34 samples are small."
- **Measurement basis:** measured (judge output compared against actual human-labelled ground truth) — this sub-finding *is* a genuine measured comparison, unlike the headline multiplier itself.
- **Can support:** a data point on LLM-judge reliability for this kind of counterfactual-time-estimation task, relevant to RQ2 (measurement methods) as a methodology note about a genuinely new measurement technique (LLM-as-counterfactual-judge) entering the literature.
- **Cannot support:** confidence that the judge's estimates on the full 5,305-transcript dataset are within 2-3x of true values — validation set (n=34) is small and drawn from the same population, so it may not generalise, as authors themselves flag.

### F8 — Self-estimates undershoot the model's estimates (inverse perception–reality pattern)
"All self-estimates fell below the bootstrapped point estimate, with most falling below the 90% confidence interval" — i.e., when METR staff were asked how much faster Claude Code made them, their own self-estimated multiplier was *lower* than the transcript-derived modelled multiplier.
- **Measurement basis:** both — self-reported (staff estimate) vs modelled (LLM-judge-derived point estimate), explicitly reported as a delta per CLAUDE.md rule 4.
- **Note on directionality — important cross-reference:** this is the **opposite direction** from the canonical METR 2025 RCT perception–reality gap (PROTOCOL §5 tension 1: developers there *believed* they were faster than they measurably were). Here, self-report is *more conservative* than the model's estimate. This is not necessarily a contradiction of tension 1 — the two studies measure different things (perceived-vs-RCT-measured speed, versus perceived-vs-LLM-modelled-upper-bound speed) — but it is a data point worth flagging to `synthesis/contradictions.md` at cross-referencing time: it suggests self-report is not uniformly optimistic relative to all other measurement bases: here it undershoots a *ceiling* estimate, which is the expected direction if the ceiling is a true ceiling (self-report should fall below an upper bound) but is the opposite pattern to self-report exceeding a *measured* baseline. **Not a genuine contradiction of tension 1 on inspection — it is consistent with tension 1 if self-report tracks true uplift reasonably well and the model estimate is, as claimed, inflated above true uplift.** Recording here for the orchestrator to confirm at cross-ref stage rather than silently resolving it.
- **Can support:** indirect corroboration that the 1.5x–13x range is inflated relative to what practitioners themselves perceive, i.e. supports the authors' own "soft upper bound, not a point estimate" framing.
- **Cannot support:** a quantified "true" multiplier — no number for the self-estimates is given in the note, only their relation to the CI.

### F9 — Relationship to METR's 2025 human-uplift RCT (design comparison, not a replication)
Stated motivation: "Human uplift studies like the one we did in 2025 are becoming more expensive as working without AI becomes increasingly costly. In this post, I investigate whether coding agent transcripts could serve as a cheaper alternative for estimating uplift." And: "METR's human uplift RCT randomized developers to complete issues one at a time, with or without AI." The note argues this RCT design "may understate AI's potential impact" by not permitting the concurrent multi-agent workflows observed in the transcript data (linking to F3).
- **Measurement basis:** authors' own argument/reasoning, not a new measurement of the RCT.
- **Important scope note (verified via targeted re-fetch):** the note does **not** restate or re-analyse the 2025 RCT's actual effect size (the −19%/"20% believed faster" figures are not quoted anywhere in this note) and does **not** claim to replicate or overturn it. It only argues, in the abstract, that the RCT's single-task-at-a-time design is a *structural* reason the RCT might understate agentic-era gains relative to real-world concurrent usage. No quantified reconciliation of the two studies is attempted — flagged explicitly by the author as future work ("Validate methodology against RCT uplift study — How well does the estimated time savings factor compare to the actual uplift ratio?").
- **Can support:** an explicit, author-acknowledged open question about whether the 2025 RCT and this 2026 upper-bound note are measuring compatible things — relevant context for tension 1, but **not** a resolution, extension, or contradiction of it as it stands.
- **Cannot support:** any claim that the RCT's −19% finding has been superseded, replicated, or invalidated by this note. Any exec-brief use of tension 1 must not cite this note as evidence the RCT finding no longer holds.

### F10 — Task composition (qualitative only, unweighted)
Transcripts "span feature additions, code exploration, greenfield projects, refactoring, and bug fixes" — no proportion/count breakdown by category, and no task-type-level effect sizes given.
- **Measurement basis:** descriptive/qualitative, not quantified.
- **Task-type tagging for this source:** T3 (greenfield), T4 (feature additions — though context is a research org, not a typical brownfield enterprise codebase, so T4 applicability is uncertain), T5 (refactoring), T8 (bug fixes), plus likely T9 (internal tooling/research infra, standard METR output) — assigned on inference, not stated proportions. **Flag: cannot support any task-type-differentiated effect-size claim** — the range (1.5x–13x) is pooled across all task types per person, so it cannot feed RQ1's task-type breakdown with any granularity finer than "mixed."

### F11 — No cost/token-spend data
The note contains no mention of licence cost, token spend, or dollar cost associated with the AI usage studied.
- **Relevance:** a further (negative) data point for RQ4's pre-registered expectation that cost data is thin in the literature — this Tier C source, despite unusually granular time-based telemetry, reports zero cost figures.

### F12 — Explicit "exploratory" self-framing and stated future work
Repeated hedges throughout: "soft upper bound" (used multiple times), "should be interpreted as approximate rather than precise," "While causality can't be established," "This likely does not significantly affect the results" (re: possible confusion between model-generated and human-typed messages in advanced multi-session workflows). Stated follow-up work: expand beyond Claude Code to other agents; build a better-validated LLM judge on a larger ground-truth set; explicitly validate the transcript methodology against RCT-style uplift measurement; survey developers on value delivered (not just time spent); analyse task-type success rates by category.
- **Can support:** treating this entire note as a methodology pilot / proof-of-concept for a new measurement technique (LLM-judge-derived counterfactual time estimation from agent transcripts), not as a settled productivity estimate — feeds RQ2 (measurement methods) as a *new candidate method*, with the method itself flagged as unvalidated at scale.
- **Cannot support:** treating any number in this note as final; the authors themselves have not yet done the RCT-cross-validation they identify as the key open question.

---

## Overall one-line verdict

**Can support:** an author-labelled *soft upper bound* (~1.5x–13x, wide between-person variance) on Claude Code task-level time compression for a small, atypical population (7 AI-safety researchers, one month), useful as a ceiling anchor and as a methodology pilot for LLM-judge-based counterfactual estimation (feeds RQ2); explicitly named mechanisms (task substitution, task selection, worker specialisation, judge-validation uncertainty) by which any single time-savings number overstates true productivity value (feeds RQ4/RQ6 caution list).

**Cannot support:** any point-estimate productivity multiplier for typical enterprise engineers or brownfield codebases; any task-type-differentiated effect size; any cost/ROI figure; any claim that this note replicates, updates, or resolves METR's 2025 RCT finding (it explicitly does not attempt that comparison numerically); any claim of measured (as opposed to modelled) time savings.

---

## Proposed evidence rows (unverified)

metr-2026-transcript-bound	2026	C	E3	Exploratory transcript analysis; LLM-judge (GPT-5) counterfactual time estimation on 5,305 Claude Code transcripts, bootstrapped per-person point estimates; no randomisation/control	7 METR technical staff, internal, 1 organisation, January 2026	T3,T4,T5,T8,T9 (unweighted, no per-type breakdown)	Time savings factor (counterfactual hours without AI / measured hours with AI)	~1.5x-13x across 7 individuals (person range 2.11x-11.62x); author-labelled "soft upper bound"	positive (AI faster), magnitude explicitly overstated per authors	modelled (LLM-judge-estimated counterfactual; not measured, not self-reported)	none reported	none reported (population is METR technical staff, not graded by seniority)	AI-safety research org internal codebases/research infra, not typical enterprise brownfield	Independent nonprofit (not tool vendor) but studies own staff on Anthropic's Claude Code; soft non-financial link to Anthropic via safety-eval relationship; single-org, N=7	Author explicitly frames as exploratory soft upper bound, not a productivity estimate; enumerates 3 named overestimation mechanisms (task substitution, task selection, worker specialisation) plus judge-validation uncertainty (n=34, r_log 0.83); does not quantify net correction; does not reconcile numerically with METR 2025 RCT	3
metr-2026-transcript-bound	2026	C	E3	Same as above; correlational sub-analysis within same dataset	7 METR technical staff	T3,T4,T5,T8,T9	Concurrency (avg simultaneous agent sessions) vs time savings factor	Positive association: higher concurrency staff show higher factor (e.g. 2.32 main-concurrency -> 11.62x; 1.05 -> 2.11x)	positive correlation, non-causal per authors	modelled/correlational (not measured causal effect)	none reported	none reported	AI-safety research org	Same as above	Authors explicitly state causality cannot be established from this design; plausible reverse-selection confound (staff who parallelise may pick more parallelisable/simpler tasks)	2
metr-2026-transcript-bound	2026	C	E3	Author-cited external survey figure (originating from Anthropic's own productivity research, not independently measured by METR here)	Unspecified Claude-assisted work population (external, cited)	Cross-cutting (counterfactual value discount, not task-type specific)	Share of AI-assisted work that would not have been done otherwise (task substitution)	27%	negative implication for counterfactual value of measured time savings	self-reported (survey, external source cited by METR)	none reported	none reported	Unspecified (external citation)	Tier D-adjacent origin (Anthropic-sourced figure) cited within a Tier C METR note - COI-flag the underlying figure as vendor-originated even though METR itself is not the vendor	Cited as supporting rationale for why time-savings factors overstate value; not independently verified by METR; not applied arithmetically to METR's own 1.5x-13x figures	3
metr-2026-transcript-bound	2026	C	E3 (methodology, not a productivity claim)	LLM-judge validation exercise: GPT-5 counterfactual-time judge vs 34 human ground-truth labels, compared to human-to-human and Claude-4.5-Sonnet-judge baselines	34 ground-truth labelled tasks, human labellers plus 2 LLM judges compared	Not task-differentiated (methodology validation)	Judge-vs-human estimate agreement: r_log correlation; also "within 2-3x" typical spread	GPT-5 judge r_log=0.83 vs human-human r_log=0.67 vs Claude 4.5 Sonnet judge r_log=0.46-0.48; predictions typically within 2-3x of human estimate	directional: LLM judge outperforms both human-human agreement and an alternative LLM judge on this small set, but with wide (2-3x) typical error	measured (judge output vs actual human-labelled ground truth)	none reported	none reported	N/A - methodology validation	Independent nonprofit methodology exercise; small n	Authors explicitly flag "34 samples are small" and caution against generalising; this is the most genuinely "measured" sub-finding in the whole note, useful for RQ2 as evidence about a new measurement technique's reliability, not about productivity itself	4
metr-2026-transcript-bound	2026	C	E3	Comparison of staff self-estimated speedup vs the note's own bootstrapped LLM-judge-derived point estimate, same population	7 METR technical staff (subset who gave self-estimates, n not specified)	T3,T4,T5,T8,T9 (mixed, unweighted)	Self-estimated speedup vs modelled time-savings-factor point estimate	All self-estimates below the bootstrapped point estimate; most below the 90% CI lower bound (no absolute numbers given)	self-report undershoots model estimate (opposite direction to canonical METR 2025 RCT perception gap; see quality_notes)	both (self-reported vs modelled), reported as an explicit delta per protocol rule 4	none reported	none reported	AI-safety research org	Same population/independence caveats as F1	Direction differs from the 2025 RCT perception-reality gap (there, self-report exceeded measured reality; here, self-report falls short of a modelled ceiling) - flagged for cross-ref/contradictions review, not a resolved contradiction on its face since the two studies compare self-report against different baselines (measured floor vs modelled ceiling)	4
