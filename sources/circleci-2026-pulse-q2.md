# Source: circleci-2026-pulse-q2

## Identity
- Title: 2026 State of Software Delivery, Q2 Pulse Report (CircleCI). Cover: "2026 | Q2 Pulse Report: State of Software Delivery".
- Authors: Jacob Schmitt, Ron Powell (editor Gillian Kieser). Publisher: CircleCI (CI/CD vendor).
- Date: blog post 8 Jul 2026; PDF created 7 Jul 2026.
- URLs: https://circleci.com/blog/five-takeaways-2026-q2-pulse/ ; https://circleci.com/landing-pages/assets/2026-q2-state-of-software-delivery-report.pdf (25 numbered pages, mostly design).
- Follow-up to the February 2026 annual "2026 State of Software Delivery" (blog 18 Feb 2026), which the Pulse calls "Q1".
- Access: exists and fully readable. The standard pdftext.py returned nothing (per-glyph Type0 fonts); I recovered the text by decoding the fonts' ToUnicode maps from the content streams. Charts were read from their printed text labels, not visually; the success-rate line chart (2023-2026) has no recoverable data labels beyond the prose. Blog post read in full via curl. All prose below is from the primary.

## What this document is
A short vendor telemetry report: five findings from CircleCI's own platform data for March 2026, plus a cost-model chapter and a product chapter promoting "Chunk sidecars" (inner-loop validation for coding agents). Parts: velocity gap; habits of high performers (output per contributor, trigger mix, MER); cost; product; methodology.

## Full notes
**Dataset and method (Methodology page).** "over 20 million CircleCI workflows within the first 28 days of March 2026", compared year-over-year with the identical window in 2025 (1-28 March). Baseline population metrics are restricted to "projects with more than one contributor and workflows that ran at least 4 times" (the PDF text renders it as "1 contributor" and "4 runs"; the prose reading is >1 and >=4). Aggregate-volume metrics omit these filters. Standard exclusions: test accounts, abusive projects, internal CircleCI activity. "Branch designations reflect the branch status at the time each pipeline ran." Industry from Clearbit, incomplete. No inferential statistics, no confidence intervals, no number of organisations or projects (except the Top 20).

**Definitions.** Main-branch throughput = "the number of workflows run on the default branch, indicating production-bound code". Feature-branch throughput = "the number of workflows run on isolated development branches". Main success rate is shown as a 2023-2026 line (y-axis 70-82) with no formal definition. p50/p95 are bands of the distribution of the per-unit workflow rate (unit not stated precisely; prose says "across all users"); they are not tracked teams. The "Top 20" is a different construction: the 20 anonymised organisations with the highest main-branch throughput, measured as organisation totals (CircleCI: "not an exact comparison to the percentile figures").

**Headline figures.**
1. Velocity gap on main: p50 1.7 workflows/day in both Q1 and Q2; p95 13.4 (Q1) and 15.6 (Q2); described as 8x then 9x. Arithmetic gives 7.9x and 9.2x. The executive summary says the top 5% "ship validated code 9x faster", which overstates what is measured (workflow runs on main, not deployments or merged changes).
2. Branch split: median-team feature-branch throughput +7.7% YoY; main-branch "stayed entirely flat" YoY. The annual report found main-branch throughput declining; the Pulse calls flat "a modest improvement".
3. Main-branch success 76.7% (Q2) vs 70.8% (Q1), "well below the mid-80s results of 2023-2024" and below the 90% CircleCI benchmark.
4. Top-20 cohort: about 2,165 main workflows/day on average, +72% YoY; 20 to 1,400 active contributors (median about 290). Per contributor per day: p50 1.1, p95 3.1, Top 20 11.8 (text "12"; 6.5 a year earlier).
5. "Scale myth": within headcount bands (2-5 to 101-250) p95/p50 is 3.9x to 4.6x, against 9x overall. CircleCI concludes the edge is "not about size". Tension: if within-band ratios are about 4x while the pooled ratio is 9x, headcount composition accounts for a large part of the pooled gap; the report does not discuss this.
6. Trigger mix: VCS-push share of pipelines is nearly 100% (median), 83% (p95), 68% (Top 20).
7. MER (new): feature-branch workflow runs per main-branch run. Median 3.9 (about 5 total runs), p95 2.6, Top 20 1.3; Top 20 1.62 to 1.28 (-21% YoY); median "barely budged".
8. CI credits per shipped change (vendor-estimated): Top 20 -31% YoY, median +13% YoY; Top 20 about 51% below median per change; Top 20 total CI spend +62%.
9. Modelled agentic cost: $25 to $6 per change, about $900K to about $200K per year for 50 developers. Hypothetical.

**Not in the Pulse.** MTTR/recovery, workflow duration, any AI-adoption or tool variable, any defect or incident measure. The annual report's recovery-time figure is not updated.

**AI framing (quoted).** "AI is pushing code volume up almost everywhere, but the productivity gains aren't landing evenly across organizations"; "Software delivery has shifted from a code generation problem to a code validation problem. AI makes writing code faster...". The dataset has no AI variable; these are assertions. Token spend appears only as a model assumption.

**Changes vs the February annual report.** Branch-based throughput and success-rate definitions appear to carry over. Differences: (a) data window is 1-28 March 2026 vs the identical 2025 window (annual report window not re-checked here); (b) new metrics: MER, trigger mix, per-contributor throughput, CI credits per change, Top 20 cohort; (c) no formal restatement, but the Pulse's "Q1" comparators (13.4/day, 8x, 70.8%) are not tied to a stated period, so it is unclear whether Q1 and Q2 are different periods or different cuts. The note that 70.8% referred to September 2025 is not confirmed by this document, which only says "Q1"; check against the annual-report record. The annual "-7% median main throughput" and the Pulse "flat" are YoY on different windows/populations.

**COI.** CircleCI sells CI plus "Chunk", "Chunk sidecars", a CLI "built for agentic development" and a Data Explorer. The thesis (the bottleneck is validation) maps directly onto its products; Part 4 is a product chapter and the $700K saving is a sales model.

## Tier & era grading
- Tier D (vendor telemetry, direct product COI). Large N but observational, no counterfactual, no AI variable, no inferential statistics, vendor selects and interprets its own data.
- Era: UNSPLIT (no AI-tool modality in the dataset). Any E3 reading is CircleCI's interpretation and must not be tagged as E3 effect evidence.

## Measured vs self-reported
- Measured (platform telemetry): workflow counts by branch and percentile, success rate, MER, trigger mix, credit spend, cohort composition.
- Self-reported: none (no survey).
- Modelled: the $900K/$200K estimate and sidecar efficiency claims (5x tokens, 30x compute; "in our testing", no method).
- Interpretation, not measured: that AI causes feature-branch growth or main-branch stagnation.

## Can / cannot support — verdicts
- Can support (low confidence, directional): a vendor-customer baseline that in March 2026 feature-branch CI activity grew while main-branch activity was flat, with main success at 76.7%; that rework cycles (MER) differ strongly by throughput band; consistent with the bottleneck-displacement pattern (tension 6) with AI as an untested explanation.
- Cannot support: any causal AI claim; deliveries or features shipped (workflow runs are not deliveries); the $900K/$700K figures as evidence of AI cost or saving; a causal reading of the top-vs-median gap (outcome-selected cohort, filters, size composition).
- Per Tier D rule, nothing here carries an exec-brief claim alone.

## Red flags / things the orchestrator should know
1. No AI measurement; AI framing is vendor interpretation. Do not tag E3.
2. Period ambiguity: Q2 data is 1-28 March 2026 vs the same 2025 window; "Q1" comparators come from the annual report with an unstated window. The +5.9 point success-rate change may not be like-for-like.
3. "9x" is workflow runs per day on main, p95 vs p50, not shipped code; printed values give 7.9x and 9.2x.
4. Within-size-band gap is about 4x vs 9x pooled, so size composition explains much of the pooled gap, against the report's framing.
5. Top 20 is outcome-selected and measured at organisation level; skew from a few very high-volume organisations is possible (an external critique of the annual report, Rob Bowley's blog, raised skew and implausibly short durations for the top band; not checked against this report).
6. Cost per shipped change and the 51% gap are derived from average credit prices times MER, not observed per-change spend.
7. The $900K model is product marketing on assumed token prices and a cold-cache assumption.
8. Missing: MTTR, duration, any quality or incident outcome, number of organisations.

## Proposed evidence rows (unverified)
```tsv
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor CI telemetry; observational; no AI variable	20M+ CircleCI workflows, 1-28 March 2026 vs same window 2025; population metrics limited to projects with >1 contributor and workflows with >=4 runs	T11	Main-branch throughput gap, p95 vs p50 (workflows run on default branch per day)	p50 1.7/day in Q1 and Q2; p95 13.4/day (Q1 report) to 15.6/day (Q2 report); ratio 8x to 9x per report text (15.6/1.7 = 9.2; 13.4/1.7 = 7.9)	gap widening (descriptive)	measured	none	none	CI-vendor customers only; multi-contributor filter	vendor-published (CI vendor, sells agent validation product); no independent replication	Workflow runs on main are not deliveries; 'ships 9x validated code' wording overstates; no AI-adoption measure; Q1 window not stated	3
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor CI telemetry; observational	Same dataset; median team YoY change by branch type, March 2026 vs March 2025	T11	Y/Y change in median throughput: feature-branch workflows vs main-branch workflows	Feature-branch +7.7% YoY; main-branch 0% (flat) YoY; annual report had main-branch decline YoY so flat described as modest improvement	feature up, main flat (bottleneck-displacement pattern; AI causation not tested)	measured	none	none	as above	vendor-published (CI vendor, sells agent validation product); no independent replication	AI attribution is CircleCI interpretation ('AI is pushing code volume up almost everywhere'); no dataset variable for AI use; branch status taken at pipeline run time	4
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor CI telemetry; observational	Main-branch workflows, March 2026 window; Q1 comparator is annual-report figure	T11	Main-branch workflow success rate	76.7% in Q2 report vs 70.8% in Q1 report (annual); mid-80s in 2023-2024 (CircleCI prose); CircleCI recommended benchmark 90%	modest recovery but below 2023-24 level	measured	none	none	as above	vendor-published (CI vendor, sells agent validation product); no independent replication	Success rate counts workflow outcomes, not defects or incidents; Q1 and Q2 windows and filters may differ so +5.9 points may not be like-for-like; no MTTR or duration in Pulse	4
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor CI telemetry; cohort of 20 highest-main-throughput organisations	20 anonymised organisations (about 20 to 1,400 active contributors, median about 290; 50% North America, 35% EMEA, 10% APAC) selected for highest main-branch throughput	T11	Top-20 cohort main-branch workflows per organisation per day and per contributor per day	Cohort mean about 2,165 main workflows/day per org, +72% YoY; 11.8 (text: 12) main workflows per contributor per day vs 6.5 a year earlier; p95 3.1, p50 1.1 per contributor per day	cohort pulling away (selected on outcome)	measured	none	none	org-level counts not comparable to percentile figures (CircleCI states this)	vendor-published (CI vendor, sells agent validation product); no independent replication	Selected on the outcome; no AI-use data on cohort; per-contributor counts workflow runs not merged changes	2
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor CI telemetry; derived ratio	Feature-branch workflow runs per workflow run on main (MER), March 2026 vs March 2025	T11	Merge Efficiency Ratio (MER) and YoY change	Median MER 3.9 (about 5 total runs incl. main); p95 2.6; Top 20 1.3; Top 20 MER 1.62 to 1.28 (-21% YoY); median MER 'barely budged' (no figure)	lower MER at the top; median flat	measured	CI credits only: Top 20 credits per shipped change -31% YoY, median +13% YoY; Top 20 about 51% fewer credits per change than median; Top 20 total CI spend +62%	none	as above	vendor-published (CI vendor, sells agent validation product); no independent replication	New vendor metric not in annual report; cost per change estimated (average per-workflow credit cost x MER runs + one main run); MER is a rework proxy and may reflect pipeline design not AI	3
circleci-2026-pulse-q2	2026	D	UNSPLIT	vendor model (assumption-based, not measured)	Hypothetical 50-developer team, about 3,000 changes/month, median MER (5 CI runs), 200,000-token context, cold-cache reload at about 10x input price	T11	Modelled delivery cost per shipped change with and without inner-loop validation (Chunk sidecars)	$25 to $6 per change; $75,000 to $18,000 per month; about $900,000 to about $200,000 per year (about $700,000 saving); sidecar microbuild feedback under 30 s vs about 5 min CI; about 5x token efficiency vs CI logs ('in our testing', no method)	vendor claims large saving	modelled (neither measured nor self-reported)	hypothetical, vendor-assumed (token input $6.25 vs $0.50 per million)	none	hypothetical mid-sized codebase	vendor-published (CI vendor, sells agent validation product); no independent replication	Direct product promotion; inputs unverified; no real customer cost data; hype-baseline only, not evidence of cost	1
```
