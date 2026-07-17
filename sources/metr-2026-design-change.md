# Source: metr-2026-design-change

## Identity

- **Title:** "We are Changing our Developer Productivity Experiment Design"
- **Publisher:** METR (Model Evaluation & Threat Research), independent non-profit AI evaluations organisation
- **Authors:** Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud
- **Published:** 24 February 2026
- **URL:** https://metr.org/blog/2026-02-24-uplift-update/ (also mirrored on METR's Substack, https://metr.substack.com/p/2026-02-24-uplift-update)
- **Format:** Informal blog/website post — **not** a peer-reviewed paper and, as of this post, not itself an arXiv preprint. It references the *original* early-2025 study's published paper (arXiv 2507.09089) but the late-2025 follow-up described here has no equivalent paper yet — only this blog write-up plus an open data/analysis repo.
- **Companion resources fetched:**
  - GitHub — early-2025 dataset: `METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs`
  - GitHub — late-2025 dataset + analysis code: `METR/Measuring-Late-2025-AI-on-OSS-Devs`. README does not itself state effect sizes (points to `regression.py`); it independently corroborates the blog post's core caveat verbatim: *"Due to changes in expectations of AI usefulness, we believe these new results are subject to increased selection that renders the results hard to interpret,"* urging readers to *"interpret these results with a major grain of salt."*
- **Verification:** identity and date corroborated by independent third-party discussion (Rob Bowley's blog, Hacker News thread, treycausey.com, jasonmoon.dev) found via web search; no evidence of retraction or correction found. Fetched twice with different extraction prompts; numbers were consistent across fetches.

## What this document is

A self-report by the same research team, updating their own earlier RCT. It presents preliminary regression output from a second, larger wave of the same experimental paradigm, then argues at length that the second wave's data is *not* trustworthy as a clean causal estimate, and proposes redesigns. It is transparent about its own limitations to an unusual degree — this is a methodology-correction post, not a results-announcement post — but that also means the topline numbers should not be lifted out and cited as if they were a validated finding.

## Full notes

### Original (early-2025) study — restated in this post for comparison
- AI caused tasks to take **19% longer**, CI **[+2%, +39%]** (does not cross zero — statistically significant slowdown). Paid $150/hour.
- This is the well-known "−19%" METR RCT already anchored elsewhere in this project; restated here only as the baseline the new wave is compared against.

### New (late-2025 → early-2026) experiment — design
- Conducted August 2025 through early 2026; blog post published 24 Feb 2026.
- **57 total developers**: 10 returning from the original 2025 panel + 47 newly recruited, drawn from "a more diverse set of open-source projects."
- **143 repositories, 800+ tasks.**
- Paid **$50/hour** — a large cut from the original $150/hour.
- Design otherwise replicates the original paradigm: developers pre-specify real tasks on real repos, are randomised task-by-task into AI-allowed vs AI-disallowed, and self-report completion time (the post's own description of the method — no mention of independent telemetry/screen-recording verification for this wave).
- Tools: the post frames the redo as motivated by wider adoption of agentic tools since the original study, naming "Claude Code and Codex" as examples of that shift; it does not state precisely which tools/models each participant used.
- Observational aside: the post cites that "approximately 4% of GitHub commits are authored by Claude Code" as market-context motivating the redo, not as part of the RCT itself.

### New effect estimates
- **Original-panel subset (n=10, late-2025 wave):** speedup of **−18%**, CI **[−38%, +9%]**. (Negative = AI-allowed condition faster = benefit direction.) CI crosses zero — not statistically significant.
- **Newly-recruited subset (late-2025 wave):** speedup of **−4%**, CI **[−15%, +9%]**. CI crosses zero — not statistically significant.
- Both point estimates read as productivity *benefits* (18% and 4% faster respectively), a reversal in sign from the original 19%-slower finding, but neither is statistically distinguishable from zero, and the CIs still admit slowdowns as large as 9% (upper bound) is actually a *speedup* bound in their sign convention — re-check: CI upper bounds of +9% in a "speedup" framing where negative=faster means +9% would be a slowdown. So both intervals span from a sizeable benefit to a modest slowdown.

### Why METR says the new estimate is biased low (selection-effect argument)
Two acknowledged, compounding selection mechanisms:
1. **Recruitment selection:** despite the $50/hour rate, "an increased share of developers say they would not want to do 50% of their work without AI." METR states this means the sample is "systematically missing developers who have the most optimistic expectations about AI's value" — i.e., the most bullish/highest-uplift developers self-select out of a study that would sometimes deny them AI.
2. **Task selection:** "30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI" — meaning the tasks that do get randomised are disproportionately ones where AI's edge is perceived as low, "systematically missing tasks which have high expected uplift from AI."
3. Additional acknowledged confounds: some developers attempted different task types depending on condition; quality differences between AI-allowed and AI-disallowed submissions; some AI-disallowed tasks not completed at all; difficulty cleanly measuring "time spent" when multiple concurrent agents are running.
4. METR's own conclusion: **"Together, these effects make it likely that our estimate reported above is a lower-bound on the true productivity effects of AI on these developers,"** and separately that they are "likely missing data on the most active adopters of AI, who may be of most interest."
5. Softer, non-quantified claim: "based on conversations with study participants," the authors *believe* developers are more sped up now than their early-2025 estimates suggested — but they explicitly flag this belief as resting on weak evidence given the selection problems, not as a validated finding.

### What changed between the 2025 design and this one (reconciliation-relevant)
| Dimension | Early-2025 RCT | Late-2025 follow-up |
|---|---|---|
| Result | +19% slower, CI [+2%,+39%] (significant) | −18% (panel) / −4% (new), both CIs cross zero (not significant) |
| Pay | $150/hr | $50/hr |
| Population | original panel only | 10 original panel + 47 new devs = 57 total, "more diverse" OSS projects |
| Repos/tasks | not restated in this post | 143 repos, 800+ tasks |
| Tool generation | pre-agentic-wave Copilot/early Claude/Cursor-class tooling (as originally classified) | explicitly framed against "increase in the use of agentic tools among open-source developers" in 2025, citing Claude Code / Codex as the market shift |
| Randomisation unit | task-level | task-level (same) — **developer-level randomisation proposed as a future fix**, not yet implemented |
| Control-group viability | intact | **broken**: control-group refusal/non-compliance documented and quantified (30–50% task refusal) |

### Planned design changes ("what METR says it will do next")
Six alternative approaches under consideration, none yet committed to as the sole replacement:
1. More intensive experiments — higher compliance, shorter duration, possibly higher pay to reduce refusal.
2. Observational data on real-world AI use in software development (e.g., the ~4%-of-GitHub-commits statistic as a category of evidence, not RCT).
3. Questionnaires/surveys with more careful design, plus time-use studies.
4. Fixed-task experiments — reverting to giving all developers identical tasks rather than letting them self-select, to remove task-selection bias.
5. Agent capability evaluations — task-based evals of autonomous agent performance (METR's core AI-safety-eval competency) as a proxy/complement.
6. **Developer-level randomisation** — randomise AI access per participant (all tasks or none) rather than per task, which would remove the task-selection escape hatch (though not necessarily the recruitment-selection one).

No single design is announced as adopted; the post reads as "we are aware this is broken, here is the menu of fixes we are evaluating," not "here is our new protocol."

## Tier & era grading

**Era: E3 (agentic).** Tools invoked are Claude Code and Codex, explicitly framed as the "agentic tools" whose adoption grew through 2025 — squarely the tool modality this project's E3 tag targets. The restated early-2025 baseline is likewise treated as E3 per its existing project classification (agentic-tooling era at time of study), not re-graded here.

**Tier: B, with an explicit caveat that the source itself disputes even that standard for its topline numbers.**

Justification: nominally this is a randomised, task-level controlled experiment with a regression-estimated effect and CI — the design pattern of a Tier A source ("RCTs, controlled field experiments... carries claims on its own," §3). But per CLAUDE.md's instruction to grade on what the post actually is (an RCT report vs. an interim self-report of one): **this is an interim self-report of a compromised RCT.** The authors themselves state the randomisation's core exchangeability assumption is broken by differential, non-random attrition in both recruitment and task submission, and explicitly characterise their own data as giving "an unreliable signal of the current productivity effect" and, per the companion repo, warn to "interpret these results with a major grain of salt." That is a stronger self-disclaimer than ordinary Tier B "carries claims with caveats" — it is closer to the authors pre-emptively withdrawing the topline number as a standalone effect-size claim while still vouching for the honesty and transparency of the reporting (open data, open regression code, explicit bias mechanism named and partially quantified). Net grading: **Tier B for the methodological/selection-effect findings** (these are well-evidenced, quantified, and directly useful for RQ2/RQ3), but **the −18%/−4% topline numbers should be treated as sub-Tier-B / directional-only** — do not cite as "METR found a 4–20% AI productivity benefit" without immediately attaching the non-significance and selection-bias caveats. Independence: METR is an independent non-profit AI-evaluations organisation, not a tool vendor; no vendor sponsorship disclosed in this post. Worth noting for the record (context, not asserted by the post itself) that METR's broader work involves capability evaluation partnerships with frontier AI labs, which is a structural adjacency worth the orchestrator's awareness even though this specific post discloses no funding conflict.

## Measured vs self-reported (separated per CLAUDE.md rule 4)

- **Completion-time metric underlying both effect sizes:** per the post's own method description, this is **self-reported** completion time by developers (no mention of independent telemetry/screen-recording verification for this wave), fed into a randomised-assignment regression. This is a different measured/self-reported split from the original study's famous "measured −19% vs. perceived +20%" gap — here there isn't a separately reported "perceived speedup" percentage for the late-2025 wave to compare against; the closest analogue is the qualitative, unquantified claim that, "based on conversations," developers are believed to be more sped up now, which the authors explicitly hold at arm's length from the regression estimate.
- **Selection-effect claims** (recruitment bias, task-refusal rate): these are **self-reported** by participants (survey/interview responses about their preferences and refusals) and then **quantified** by METR (the 30–50% task-refusal figure is a measured tabulation of self-reported refusals, not itself a self-report of impact) — flagged as "both" in the schema.
- **"Our estimate is a lower bound" claim:** this is METR's own **interpretive judgement**, not a measured quantity — recorded as self-reported/authors' assessment, not a data point.

## Can / cannot support — verdicts

- **CAN support:** (1) a documented, quantified real-world instance of control-group refusal/selection bias emerging as agentic tools become widely preferred — directly relevant to RQ2 (measurement validity) and RQ3 (what breaks study designs); (2) a directional signal, self-flagged as weak, that the sign of the original 19%-slowdown finding may not hold under 2025-generation agentic tools; (3) evidence that METR itself no longer trusts task-level-randomised OSS-developer RCTs as currently designed to produce clean causal estimates in the current adoption environment — a meta-methodology finding for RQ6 (what to instrument, what to stop trusting).
- **CANNOT support:** a standalone claim that "AI now gives experienced developers a 4–20% productivity benefit." Both new CIs cross zero (not statistically significant), the authors explicitly call their own data unreliable/a lower bound of unknown size, and the completion-time input is self-reported rather than independently verified. This post should never be exec-briefed as "METR confirmed a productivity reversal" — the accurate framing is "METR's attempted replication broke down due to selection bias, preliminary numbers point (non-significantly) toward smaller slowdown or modest benefit, and METR is redesigning the study because it doesn't trust this number either."
- **Relationship to PROTOCOL §5 tension 1 (perception–reality gap):** this source complicates but does not resolve that tension. It is not a clean replication in either direction; flagging for orchestrator cross-referencing into `synthesis/contradictions.md` rather than resolving it here, since this subagent's brief is FETCH+EXTRACT only.

## Red flags / things the orchestrator should know

- Both new headline numbers are **not statistically significant** (CIs cross zero) — easy to lose in a soundbite version of "4–20% benefit."
- Pay dropped 3x ($150→$50/hr) between waves — a confound the post does not explore (lower pay could itself change who participates and how carefully tasks are done), separate from the selection-effect story the authors do tell.
- The post's own companion GitHub repo is more blunt about unreliability than the blog prose ("major grain of salt").
- No peer review, no preprint yet for the late-2025 wave — purely a blog post plus open data/code. Treat as an interim community update, not a finished research output; a citable paper may follow and should be searched for in future refresh cycles.
- The six proposed redesigns are options under consideration, not a committed protocol — nothing here should be reported as "METR's new methodology is X."

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
metr-2026-design-change	2026	A (restated baseline; not re-graded here)	E3	RCT (task-level randomised, restated from original 2025 study for comparison)	experienced OSS devs, original 2025 panel	T4 (brownfield feature/bug work in mature OSS repos, per original study design)	task completion time	+19% longer, CI [+2%, +39%]	negative (AI slower)	self-reported time, randomised assignment	participants paid $150/hr	all experienced (median ~10y); no split given in this post	real mature open-source repos	independent non-profit (METR); no vendor sponsorship disclosed	restated in this post purely as the comparison baseline for the late-2025 follow-up; CI does not cross zero (significant)	3
metr-2026-design-change	2026	B (method nominally RCT; self-disclaimed as unreliable — see quality_notes)	E3	RCT (task-level randomised), original-panel subset of late-2025 follow-up	10 returning developers from original 2025 panel	T4 (brownfield feature/bug work in mature OSS repos)	task completion time	speedup -18%, CI [-38%, +9%]	positive (AI faster / benefit), but not statistically significant	self-reported time, randomised assignment	participants paid $50/hr (down from $150/hr in original study)	all experienced (median ~10y); subset only, no further split	real mature open-source repos, 143 repos / 800+ tasks pooled across full late-2025 sample	independent non-profit (METR); no vendor sponsorship disclosed	CI crosses zero (not significant); authors explicitly say control-group refusal/selection bias likely biases this toward understating true AI benefit; self-report time metric, no telemetry verification stated	4
metr-2026-design-change	2026	B (method nominally RCT; self-disclaimed as unreliable — see quality_notes)	E3	RCT (task-level randomised), newly-recruited subset of late-2025 follow-up	47 newly recruited OSS developers, "more diverse" set of projects	T4 (brownfield feature/bug work in mature OSS repos)	task completion time	speedup -4%, CI [-15%, +9%]	positive (AI faster / benefit), but not statistically significant	self-reported time, randomised assignment	participants paid $50/hr	all experienced OSS contributors; no further split given	real mature open-source repos, 143 repos / 800+ tasks pooled across full late-2025 sample	independent non-profit (METR); no vendor sponsorship disclosed	CI crosses zero (not significant); same selection-bias caveat as panel subset; smaller point estimate than panel subset, unexplained by post	4
metr-2026-design-change	2026	B	E3	participant survey/interview, tabulated by researchers	late-2025 follow-up participants (57 devs)	T4 (context: same OSS task pool)	% of offered tasks declined without AI	30% to 50% of developers declined to submit some tasks without AI	N/A (mechanism finding, not an outcome effect)	both (self-reported refusals, tabulated/measured by METR)	n/a	not broken out	real mature open-source repos	independent non-profit (METR); no vendor sponsorship disclosed	direct quantification of the task-selection-bias mechanism; core evidence for why the RCT control group is judged non-representative	5
metr-2026-design-change	2026	C (qualitative/self-reported researcher observation)	E3	participant survey, described narratively (not tabulated with a number)	late-2025 follow-up participants (57 devs)	T4	stated unwillingness to work without AI	"an increased share" of developers say they would not want to do 50% of their work without AI, even at $50/hr	N/A (mechanism finding)	self-reported (participant statements)	participants paid $50/hr despite this stated preference	not broken out	real mature open-source repos	independent non-profit (METR); no vendor sponsorship disclosed	recruitment-side selection-bias mechanism; no baseline comparison number given for "increased share" (vague quantifier)	4
metr-2026-design-change	2026	C (authors' own interpretive judgement, not a measured quantity)	E3	researcher interpretation / argument, not a new measurement	late-2025 follow-up sample	T4	direction and likely bias of the -18%/-4% estimates	"our estimate reported above is a lower-bound on the true productivity effects of AI on these developers"	positive bias correction implied (true effect judged more positive/beneficial than measured)	self-reported (authors' stated belief/interpretation)	n/a	n/a	n/a	independent non-profit (METR); self-assessment, not independently verified	central interpretive claim of the whole post; explicitly caveated by the authors as resting on weak evidence; must not be presented as a quantified correction	4
metr-2026-design-change	2026	n/a (design/methodology record, not an empirical finding)	E3	methodology comparison across two RCT waves of the same programme	both study waves (2025 original + late-2025 follow-up)	T4	design parameters (pay rate, population, repo/task counts, tool generation)	pay $150/hr to $50/hr; population 1 panel-only wave to 57 devs (10 panel + 47 new) across 143 repos / 800+ tasks; tool framing shifted to explicitly agentic (Claude Code, Codex) market context	N/A	n/a (design record)	pay-rate cut itself is an unexamined confound the post does not explore	n/a	real mature OSS repos in both waves	independent non-profit (METR); no vendor sponsorship disclosed	reconciliation-relevant: documents exactly what changed between the two waves so future sources can be compared on a like-for-like basis; pay cut is a confound worth flagging to the orchestrator	4
metr-2026-design-change	2026	n/a (methodology/forward-looking record, not an empirical finding)	E3	researcher-proposed redesign options (not yet implemented)	future study (not yet run)	T4	six candidate redesigns: (1) higher-compliance/higher-pay intensive experiments, (2) observational data on real-world AI use, (3) improved questionnaires/time-use studies, (4) fixed (non-self-selected) tasks, (5) agent capability evaluations, (6) developer-level randomisation	N/A	N/A	self-reported (stated intentions, no commitment to a single option)	n/a	n/a	n/a	independent non-profit (METR); no vendor sponsorship disclosed	directly feeds RQ6 (what to instrument, what to stop trusting) and RQ2 (measurement methods evolving); nothing here is a committed new protocol, only a menu under consideration	4
