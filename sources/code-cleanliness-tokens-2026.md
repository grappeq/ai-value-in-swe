# Source: code-cleanliness-tokens-2026

## Identity (verified)

- **Title:** "Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study"
- **Authors:** Priyansh Trivedi, Olivier Schmitt
- **Affiliation:** SonarSource (both authors) — maker of SonarQube, a commercial static-analysis / code-quality product
- **Venue/status:** arXiv preprint, arXiv:2605.20049v1, submitted 19 May 2026. No indication of peer-reviewed venue acceptance found.
- **Confirmed vs briefing:** matches the brief closely (minimal-pair design, Claude Code, ~7–8% token delta on cleaner code). Confirmed directly from HTML/PDF full text, not abstract alone.

## Design summary

- **Minimal-pair construction:** six repositories (3 public, 3 private), Java and Python, ~26k–134k non-comment lines of code. Two pipelines: "Slopify" (degrade clean code by introducing SonarQube rule violations while keeping tests green) and "Vibeclean" (clean up messy code by resolving analyzer-flagged issues). Public repos identified in the accessible text: Apache Commons BCEL, Netflix Genie, CKAN; the remaining three (private) are not named.
- **Cleanliness operationalisation:** "SonarQube rule violations as a proxy for cleanliness" — i.e. the independent variable is defined and measured using SonarSource's own commercial product's rule-set. This is a direct methodological entanglement between the measurement instrument and the vendor's product, not just a funding relationship.
- **Agent/model:** Claude Sonnet 4.6 via the Claude Code agent (E3 — genuinely agentic, multi-file, plan-execute-verify).
- **Trials:** 33 tasks × 2 cleanliness conditions × 10 repetitions = 660 trials. Three task tracks: 13 "cognitive-hotspot" tasks (dense single-method complexity), 14 "multi-module" tasks (changes spanning modules), 6 "calibration" tasks (designed to be cleanliness-insensitive, i.e. a built-in negative control).
- **Outlier handling:** trials >50% off the median of their 10 repetitions are dropped before averaging; this removed 9.7% of trials in practice.
- **Metrics:** 10 metrics across four categories — pass rate; footprint (input tokens, output tokens, reasoning characters); trajectory (turns, turns-before-first-edit, characters-before-first-edit); navigation (files read, file revisitations, lines edited).
- **Robustness check:** a comment-volume ablation (to rule out "cleaner code just has fewer distracting comments" as the driver) — the cleaner-side token advantage persisted or increased after normalisation in the case examined.
- **Statistical rigour:** I could not find confidence intervals, standard errors, or p-values for the headline effects in the accessible HTML/PDF extraction. One PDF-extraction pass surfaced a second, seemingly inconsistent pass-rate figure ("clean 50% vs messy 45%" on what appears to be a sub-slice, not the dataset aggregate) alongside the dataset-level figure below — I was not able to fully reconcile these from tool-mediated extraction and flag this as needing a human check against the primary PDF/HTML before the pass-rate number is treated as precise.

## Findings

### F1 — Pass rate: no effect of cleanliness on task success (null result, measured)

Dataset-level pass rate: clean condition 0.913, messy condition 0.921 (delta **−0.9 pp**, clean side *lower*, i.e. a genuine null/no-clear-direction result, not a positive effect for cleanliness). Paper's own framing: "the agents seem to accomplish the given tasks consistently, regardless of whether working on cleaner or messier code." No significance test located in accessible text.
**Can support:** a null result — codebase cleanliness (as SonarQube-defined) did not move agent task-success rate in this sample. **Cannot support:** any claim that cleanliness affects whether agentic tasks succeed; also cannot rule out an effect the study was underpowered to detect, since no CI/power analysis was recoverable.

### F2 — Token footprint reduction on cleaner code (measured) — headline finding

Input tokens **−7.1%**, output tokens **−8.5%** on the cleaner-code condition vs the messier condition, dataset-level average across all 660 trials (net of the 9.7% outlier trim).
**Can support:** a direct, agentic-era (E3), measured (not self-reported) data point that codebase cleanliness affects AI-agent token cost even when it doesn't affect success — directly responsive to RQ4's cost-per-task-type question, and about as rare as PROTOCOL §1 predicted such data would be.
**Cannot support:** dollar cost, review overhead, or rework cost — this is token count only, on one model.

### F3 — Secondary footprint/trajectory metrics move together with tokens (measured)

Reasoning characters **−11.1%**, conversation message count **−7.0%**, both lower on cleaner code.
**Can support:** internal consistency of the token-cost finding (F2) — the effect shows up across multiple correlated cost proxies, not just one metric, which strengthens confidence it's a real signal rather than a metric artefact.
**Cannot support:** wall-clock time or dollar cost (neither reported).

### F4 — File revisitation: largest single effect (measured)

File revisitations **−33.8%** on cleaner code — the largest effect of any metric in the study, exceeding the token effects by roughly 4–5×.
**Can support:** a specific mechanism hypothesis for *why* clean code is cheaper for agents — less re-reading/re-orienting, not just shorter outputs. Relevant to RQ3's "task characteristics predict failure/cost" question (navigation cost as a codebase-maturity marker) even though pass rate itself was flat (F1).
**Cannot support:** any claim about human developer navigation behaviour — this is agent-specific instrumented telemetry.

### F5 — Files read and lines edited: small, mixed-direction effects (measured)

Files read **+3.2%** (slightly *more* files read on cleaner code), lines edited **−3.2%** (slightly fewer lines edited).
**Can support:** a caution against assuming cleanliness uniformly improves every navigation metric — some move the "wrong" way, small in magnitude. Worth noting for RQ6 (don't over-interpret single navigation metrics as clean success signals).
**Cannot support:** a strong directional claim on its own — these are small effects, no CI given.

### F6 — Effect is task-type dependent, not uniform (measured) — important moderation finding

Per-track breakdown:
- **Multi-module track** (changes spanning modules — closer to brownfield/T4-style work): input tokens **−10.7%**, file revisitations **−50.8%** — cleanliness effect is stronger here than the dataset average.
- **Cognitive-hotspot track** (dense single-method complexity): input tokens **+1.8%** (token-neutral to mildly *reversed*), files read **+11.2%** (agents read more locations but edit less) — cleanliness effect is essentially absent or inverted here.

**Can support:** the headline "7–8% fewer tokens" figure is a dataset-level average masking real heterogeneity — the benefit concentrates in multi-module/cross-file work and roughly vanishes for concentrated single-method complexity. This is directly relevant to RQ3 (task characteristics moderating AI value) and cautions against quoting the aggregate number without the task-type caveat.
**Cannot support:** a single scalar "cleanliness saves X% tokens" claim without qualification by task structure.

### F7 — Substantial trial-to-trial variance (measured) — measurement-precision caution

"The most expensive trial in a group typically costs around 2.5× the cheapest." Task-to-task spread on input tokens ranges from **−47% to +44%**, median **−4.5%**.
**Can support:** a methodological point for RQ2/RQ6 — even a well-instrumented, controlled, telemetry-based study of a single model shows wide trial variance, meaning single-run or small-N agent cost comparisons (common in vendor blog posts) are unreliable without repetition. Reinforces the value of the ≥3-independent-source triangulation approach this project already uses.
**Cannot support:** precise point-estimate claims beyond the aggregated means reported (no CIs recoverable from the accessible text to quantify this precisely).

### F8 — Comment-volume ablation: effect not explained by comment stripping (measured, robustness check)

After normalising for comment volume/suppression markers on one repository (sonar-caas-poc), the cleaner-side token advantage persisted or increased (reported as moving from "+1.2% → −18.0%" after normalisation, i.e. the clean-side advantage got *stronger*, not weaker, once comments were controlled for).
**Can support:** rules out the most obvious confound (clean code simply has fewer comment tokens to process) for at least one repository — modest additional confidence in F2's causal interpretation.
**Cannot support:** generalisation beyond the one repository this ablation was run on (not stated as applied dataset-wide in the accessible extraction).

### F9 — Case studies: cleanliness effect is not monotonic — decomposition can backfire (measured, qualitative)

Two contrasting worked examples: extracting "god methods" into named helpers in commons-bcel reduced input tokens **−35%**; but in Netflix Genie, a change that spread logic across *more* methods (nominally "cleaner" by decomposition) *increased* input tokens **+8%**.
**Can support:** an important nuance for any internal cleanliness/refactoring push — "clean" is not a single dial; over-decomposition (many small methods) can raise agent navigation cost even as it improves conventional readability metrics. Relevant to RQ6 if we ever consider "reduce SonarQube violations" as a proxy metric for AI-readiness.
**Cannot support:** a general rule for when decomposition helps vs hurts — two illustrative cases, not a systematic sub-analysis.

## Grading

- **Tier: D**, despite a methodologically rigorous, controlled minimal-pair experimental design that would otherwise merit Tier A/B consideration. Downgraded per PROTOCOL §3's vendor rule because: (a) both authors are SonarSource employees with no independent co-authors; (b) the independent variable ("cleanliness") is operationalised entirely via SonarQube's own commercial rule-set — the measurement instrument and the product being validated are the same artefact; (c) no funding/COI disclosure statement was found in the accessible text despite this being a textbook case for one; (d) the conclusion ("traditional maintainability principles remain highly relevant... shaping computational cost") directly supports SonarSource's commercial value proposition (sell a tool that reduces rule violations → agents get cheaper to run). Per CLAUDE.md rule 7, COI-flagged accordingly. **This is a case worth a human sanity-check**: the experimental rigour (minimal pairs, 660 trials, outlier trimming, ablation robustness check, built-in calibration/negative-control track) is well above typical Tier D output and above much Tier C practitioner material — the tier-D placement is driven by independence/COI, not by design quality, and the two should not be conflated when this source is cited.
- **Era: E3** — Claude Sonnet 4.6 via Claude Code, genuinely agentic multi-file tool-use loop. No E1/E2 material in this source.
- **Task types:** T4 (feature dev in mature/brownfield codebases) is the best fit for the overall design — real, sizeable (26k–134k LOC) established codebases, implicit-context-heavy multi-module work. The "cognitive-hotspot" track (F6) shades toward T8-adjacent (complexity-dense single-method work) but is not debugging per se. Cross-cutting: this is squarely about **codebase-state as a cost driver**, which is the RQ4-relevant angle the taxonomy doesn't have a dedicated code for — tag as T4 with a codebase_context note rather than forcing a new type.
- **Measurement basis:** measured (instrumented telemetry) throughout — no self-report component at all. This is a clean measured-only source, useful as a contrast set for RQ2's measured-vs-self-reported gap discussion, though it has no self-reported figures to compare against internally.
- **Seniority split:** not applicable — agent-only experiment, no human developers involved. Flag this explicitly: none of these findings speak to human developer seniority effects, and translating "agent token cost" savings into human-developer cost/time savings is not something this source supports.
- **Cost data:** token counts only (input tokens, output tokens, reasoning characters, message counts). No dollar cost, no wall-clock time, no review/rework cost, no licence cost. This is exactly the "literature-level, not bespoke cost model" character PROTOCOL §1/§Scope expects, and it is one of the only sources likely to give RQ4 a direct, measured, agentic-era cost number rather than an absence-of-evidence result — but it should not be over-claimed as a full cost picture.

## Red flags / things to watch

1. **Vendor-instrument circularity** is the central issue: SonarSource defining "clean" as "few SonarQube violations" and then showing SonarQube-clean code is cheaper for agents is close to tautological marketing validation, even though the *experimental mechanics* (paired repos, blinded-ish trial repetition, outlier trimming, calibration track, ablation check) are genuinely well-built. Treat the direction of the finding as plausible (it's mechanistically sensible — less to re-read is less to re-read) but do not treat the magnitude as vendor-independent.
2. **No CI/significance figures were recoverable** through the fetch tooling used here (HTML render + one PDF pass). Before this source is used to anchor an exec-brief number, a human should pull the PDF directly and confirm whether §4/§5 of the paper (results tables) report CIs or p-values that the tool-mediated extraction missed.
3. **Possible pass-rate figure inconsistency** (F1's dataset aggregate of −0.9pp vs. a possibly-per-subset "50% vs 45%" figure surfaced in a second extraction pass) is unresolved — flagged rather than silently reconciled, per the "record nulls with diligence" and "don't guess" rules.
4. **Single model tested** (Claude Sonnet 4.6); the paper reportedly excluded Haiku results as too noisy — so this cannot speak to whether the cleanliness effect holds, shrinks, or grows for smaller/cheaper models, which is directly relevant if we're costing out different model tiers internally.
5. **Author-curated tasks** — the paper's own limitations section acknowledges the 33 tasks were author-selected, not drawn from an independent benchmark, which is an additional (self-disclosed) source of potential selection effects on top of the vendor-instrument issue above.

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, 660 trials (33 tasks x 2 conditions x 10 reps), Claude Sonnet 4.6 via Claude Code	agent-only; no human subjects; 6 repos (3 public incl. Apache Commons BCEL, Netflix Genie, CKAN; 3 private), Java/Python, 26k-134k LOC	T4	pass rate (clean vs messy)	-0.9pp (0.913 vs 0.921); no CI/p-value found	null / no clear direction	measured	tokens only, no dollar cost	N/A - agent-only, no human devs	established OSS + private repos, 26k-134k LOC, Java/Python	vendor-authored (SonarSource, both authors); cleanliness proxy = vendor's own SonarQube ruleset; no COI statement found	rigorous minimal-pair design with calibration/negative-control track and outlier trimming (9.7% dropped), but tier held to D on vendor-independence grounds despite design quality; possible inconsistency with a "50%/45%" figure elsewhere in the paper not reconciled	4
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, 660 trials, Claude Sonnet 4.6 via Claude Code	agent-only; 6 repos, Java/Python, 26k-134k LOC	T4	input/output token count	input -7.1%, output -8.5% (dataset-level average)	negative (cleaner code cheaper)	measured	direct token cost data; no dollar/time/review cost	N/A - agent-only	established OSS + private repos, 26k-134k LOC	vendor-authored (SonarSource); cleanliness measured via vendor's own product's ruleset	headline finding of the paper; corroborated by secondary footprint metrics (reasoning chars, message count) moving the same direction	5
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, 660 trials	agent-only; same 6 repos	T4	reasoning characters; conversation message count	reasoning chars -11.1%, messages -7.0%	negative (cleaner code cheaper)	measured	token/message-count cost proxies only	N/A - agent-only	established OSS + private repos	vendor-authored (SonarSource)	secondary metrics moving with F2, strengthens internal consistency of the token-cost finding	3
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, 660 trials	agent-only; same 6 repos	T4	file revisitation count	-33.8%	negative (cleaner code = fewer revisits)	measured	navigation-cost proxy, not dollar cost	N/A - agent-only	established OSS + private repos	vendor-authored (SonarSource)	largest single effect in the study, ~4-5x the token effect size; plausible mechanism for why cleaner code is cheaper	4
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, 660 trials	agent-only; same 6 repos	T4	files read; lines edited	files read +3.2%, lines edited -3.2%	mixed (small, one metric moves each direction)	measured	navigation-cost proxies only	N/A - agent-only	established OSS + private repos	vendor-authored (SonarSource)	small effects, no CI given; caution against assuming every navigation metric improves with cleanliness	2
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, per-track subgroup analysis	agent-only; multi-module track (14 tasks) vs cognitive-hotspot track (13 tasks)	T4	input tokens; file revisitations; files read, by task track	multi-module: tokens -10.7%, revisits -50.8%; cognitive-hotspot: tokens +1.8%, files read +11.2%	negative for multi-module; near-null/reversed for cognitive-hotspot	measured	token/navigation cost proxies, split by task structure	N/A - agent-only	established OSS + private repos	vendor-authored (SonarSource)	key moderation finding: the headline 7-8% figure is a dataset average masking large task-type heterogeneity - benefit concentrates in cross-module work, vanishes for single-method complexity	5
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, trial-level variance analysis	agent-only; same 6 repos, 10 reps per task per condition	T4	trial-to-trial and task-to-task variance in input tokens	within-group: costliest trial ~2.5x cheapest; across-task: -47% to +44%, median -4.5%	n/a (variance/precision finding, not a directional effect)	measured	cost-measurement precision/variance, not a cost figure itself	N/A - agent-only	established OSS + private repos	vendor-authored (SonarSource)	methodological caution: even a controlled, well-instrumented single-model study shows wide trial variance - single-run agent cost comparisons are unreliable without repetition	4
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, comment-volume ablation on one repo (sonar-caas-poc)	agent-only; single repo subset	T4	input tokens, comment-normalised	clean-side advantage moved from +1.2% to -18.0% after normalising for comment volume	negative (advantage strengthened after controlling for comments)	measured	token cost, ablation-adjusted	N/A - agent-only	one repo (sonar-caas-poc), not stated as dataset-wide	vendor-authored (SonarSource)	robustness check ruling out comment-stripping as the sole driver of the token effect, but run on only one repository	3
code-cleanliness-tokens-2026	2026	D	E3	controlled minimal-pair experiment, two illustrative case studies	agent-only; commons-bcel and Netflix Genie	T4	input tokens, worked examples of decomposition changes	commons-bcel (god-method extraction): -35%; Genie (logic spread across more methods): +8%	mixed (decomposition helped in one case, hurt in the other)	measured	token cost, case-level, qualitative illustration	N/A - agent-only	Apache Commons BCEL, Netflix Genie (named OSS repos)	vendor-authored (SonarSource)	demonstrates cleanliness effect is not monotonic; over-decomposition can raise agent navigation cost despite improving conventional readability metrics - relevant caution if "reduce SonarQube violations" is ever used as an AI-readiness proxy metric	3
