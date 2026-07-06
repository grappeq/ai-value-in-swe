# plandek-2026-benchmarks

## Citation

Ponsonby, Charlie (Co-founder & CEO, Plandek). "2026 Engineering Productivity Benchmarks: What AI Is Really Changing in Software Delivery." Plandek blog, March 2026 (page shows 17 March 2026; companion press release issued 5 March 2026).
https://plandek.com/blog/what-ai-is-really-changing-in-software-delivery

Related artefacts examined:
- Press release: "AI Helps Low-Performing Engineering Teams 4x More Than High-Performing Ones, New Benchmarks Show," Plandek Limited via GlobeNewswire, 5 March 2026. https://www.globenewswire.com/news-release/2026/03/05/3250201/0/en/AI-Helps-Low-Performing-Engineering-Teams-4x-More-Than-High-Performing-Ones-New-Benchmarks-Show.html
- Fuller report landing pages (both **gated** — see Access, below): https://plandek.com/resources/2026-software-delivery-benchmark-report/ and https://plandek.com/resources/2026-engineering-productivity-benchmarks-report
- Companion gated report: "AI Adoption & Impact Benchmarks 2026," https://plandek.com/resources/ai-adoption-impact-benchmarks-2026

## What the source is

Plandek is a delivery-analytics vendor (DORA-style dashboards over Jira/GitHub/GitLab/CI-CD data, now selling an "AI impact" measurement module). The benchmark data is **its own customer platform telemetry** — organisations that have already bought delivery analytics. This is exactly the "DX / LinearB / Swarmia / Faros-class published customer analysis" category that PROTOCOL §6 instructs to grade **Tier D** when vendor-published.

## Access record (what was and was not readable)

- **Readable in full:** the blog post (primary public artefact) and the GlobeNewswire press release.
- **Gated, not readable:** the full "2026 Engineering Productivity Benchmarks Report" — both landing pages offer it only via "Book a demo" / "Free trial" CTAs; no email-gated PDF or direct download was found. The companion "AI Adoption & Impact Benchmarks 2026" report is likewise gated.
- Consequence: all figures below come from the vendor's own public summaries of a report whose underlying tables, definitions, and methods could not be inspected. This is a summary-of-a-summary extraction and is graded accordingly.

## Verification of the claims given at dispatch

| Claim to verify | Status | As actually stated |
|---|---|---|
| Lead-time-to-value ~50% improvement for lower-quartile AI teams vs matched non-AI teams | **Confirmed as reported, with one wording caveat** | "Lower-performing teams using AI improved delivery speed dramatically, reducing Lead Time to Value by nearly 50% compared to **similar** teams not using AI." The word "matched" overstates what is disclosed: Plandek says "similar," and no matching procedure is described anywhere public. |
| "2,000+ teams" of platform telemetry | **Confirmed** | "More than 2,000 software engineering teams worldwide" (blog, press release, and report landing page). Note: the companion AI Adoption report cites "1,800+ engineering teams" across "130+ organisations" plus "136 engineering leaders" surveyed — the relationship between the 2,000+ and 1,800+ populations is not explained. |
| PR-merge-time ~35 h bottom quartile | **Confirmed** | Bottom-quartile teams take "more than 35 hours on average to merge pull requests"; top performers "under 21 hours." |

## Findings (one record per finding; §4 schema fields)

All findings: year 2026 (data window Q4 2025 per press release) · tier D · method: vendor customer telemetry, cross-sectional benchmark, no randomisation · population: 2,000+ engineering teams on Plandek's platform (self-selected delivery-analytics buyers; seniority/size/geography not broken down) · measurement_basis: **measured** (platform telemetry), except F8 · independence_flags: vendor-published, COI, population = own customers · task_types: none — all metrics are system-level delivery outcomes, not task-typed (see Taxonomy fit).

- **F1 — AI × baseline-performance interaction (headline).** Lower-performing teams using AI reduced Lead Time to Value by "nearly 50%" vs similar non-AI teams; top-performing teams improved only "around 10–15%" — framed by Plandek as "roughly a 4x difference in impact." Direction: positive, concentrated at the low end. Metric: Lead Time to Value (undefined publicly — see Constructs). RQ1/RQ5; echoes the DORA 2025 "amplifier" framing but inverts it (here AI lifts the floor, not amplifies existing capability) — worth a cross-ref by the orchestrator.
- **F2 — PR merge time spread.** Bottom-quartile teams: >35 h average to merge PRs; top performers: <21 h. Not an AI effect — a benchmark spread; AI adoption's relation to this gap is not quantified publicly. RQ1 baseline / RQ6.
- **F3 — Ship-time spread.** Top teams ship in <22.5 days on average; bottom quartile >62 days (~3x). Same status as F2: benchmark distribution, not an AI effect size. (Metric start/end points undefined publicly.)
- **F4 — Sprint predictability spread.** High performers complete more than two-thirds of planned sprint work; lower performers less than half. Benchmark spread, not an AI effect.
- **F5 — Focus/time-allocation spread.** High performers spend >41% of time on roadmap delivery; lower performers <21%, described as "trapped in rework, tech debt, and unplanned work." Benchmark spread, not an AI effect.
- **F6 — Bottleneck displacement (negative/nuanced).** "AI accelerates development, but it does not automatically fix the underlying delivery system"; where AI is adopted without system-level change, "bottlenecks shift, but overall delivery outcomes barely change," and "AI does not fix broken flow — systemic constraints still determine long-term performance." Direction: null at system level absent process change. Directly feeds §5 tension 6 (bottleneck displacement) and RQ5. No figures attached.
- **F7 — Bottleneck-fixing multiplier.** Press release: AI-using teams that addressed delivery bottlenecks "delivered 2x+ output per engineer." "Output per engineer" is undefined; no counterfactual described. Treat as marketing-grade until the gated report defines it.
- **F8 — Adoption depth (from the gated companion report's public summary).** Most organisations remain in "basic assist" mode rather than deep AI integration; "AI adoption alone doesn't guarantee success." Measurement basis: mixed — survey of 136 engineering leaders plus telemetry; the split is not disclosed. Self-reported component flagged.

## Constructs measured and how they are defined

- **Lead Time to Value** — the headline metric is **not publicly defined anywhere located** (blog, press release, landing pages, or Plandek's public metrics glossary). The glossary defines "Lead Time" (creation to deployment) and "Lead Time for Change" (PR opened → merged or deployed, per DORA), but "Lead Time to Value" does not appear as a named, defined metric. The endpoint implied by "to value" (deployment? release? usage?) is unknown. This materially weakens F1.
- **PR merge time** — not formally defined; plainly time from PR opened to merged, but start/end points and outlier handling undisclosed.
- **Ship time (22.5/62 days), sprint completion, roadmap-time share** — construct names only; definitions withheld to the gated report ("metric definitions included in report").
- Framework: Plandek's "four pillars" — Focus, Speed, Predictability, Quality — undefined publicly.

## Methodology inventory (disclosed vs absent — item by item)

| Item | Status |
|---|---|
| Sample size | **Present**: 2,000+ teams (org count not given; companion report says 1,800+ teams / 130+ orgs, unreconciled) |
| Data source | **Present**: anonymised platform telemetry from Jira, GitHub, GitLab, CI/CD, and AI dev tools |
| Time window | **Present (press release only)**: Q4 2025 |
| AI-adopter identification | **Absent** — how a team counts as "using AI" is never stated (tool telemetry? survey? licence data?) |
| Matching / comparison-group construction | **Absent** — "similar teams not using AI" is asserted, with no matching variables, procedure, or balance evidence |
| Quartile construction | **Absent** — quartiles of which metric, computed over what population, is not stated |
| Metric definitions | **Absent** for the headline metric (Lead Time to Value); others deferred to the gated report |
| Statistical testing / uncertainty | **Absent** — no significance tests, confidence intervals, or effect-size machinery anywhere public |
| Tool-type / era split | **Absent** — Cursor, Claude, and Devin are name-checked; no autocomplete/chat/agentic breakdown, no per-tool results |
| Selection-bias discussion | **Absent** — no acknowledgement that the population is Plandek's own customer base |

## Era (§2)

**Era-unclear; plausibly E2/E3 mix, unsplit.** Data window is Q4 2025 and the tools named (Cursor, Claude, Devin) are chat/agentic-era, so the finding set is post-autocomplete; but the material never distinguishes agentic from earlier modalities, and "AI use" is undefined, so no finding can be cleanly tagged E3 by the modality-actually-studied rule. For the evidence table: era = E2/E3 (unsplit, modality undisclosed). Under the era-transfer rule this cannot serve as clean E3 effect-size evidence.

## Tier, COI, and grading

- **Tier: D** (vendor-published customer analytics; PROTOCOL §6 explicit rule for LinearB/Swarmia/Faros-class material). Not Tier B despite the large N: no counterfactual design is disclosed, the comparison-group construction is opaque, and the full report is gated.
- **COI: flagged.** Plandek sells delivery-analytics and an AI-impact-measurement product; the report's thesis ("you must measure delivery systemically to get AI value") is the product pitch. The press release is a marketing artefact.
- **Independence:** none — data, analysis, and publication are all the vendor's; population is self-selected customers.
- **One-line verdict:** can support directional signal that AI-linked delivery gains concentrate in lower-performing teams and that system-level outcomes lag local speedups (F1, F6), and supplies useful benchmark distributions (F2–F5); **cannot** support any exec-brief effect-size claim on its own (Tier D never carries a claim alone), nor any era-specific claim, nor any claim about the headline metric until "Lead Time to Value" is defined.

## Limitations

1. Headline effect (F1) rests on an undefined metric, an undisclosed AI-adopter classification, and an undisclosed comparison-group procedure — three unknowns stacked under one number.
2. Population is Plandek customers: organisations already investing in delivery measurement, likely unrepresentative of the wider industry in both maturity and motivation.
3. Regression-to-the-mean risk: "lower-performing teams improved most" is the expected artefact of quartile-based cross-sectional comparison even absent any AI effect; nothing disclosed rules this out.
4. Cross-sectional adoption comparison, not longitudinal or randomised: AI-adopting teams may differ systematically from non-adopters (staffing, funding, leadership attention).
5. Team-count discrepancy across Plandek's own 2026 artefacts (2,000+ vs 1,800+) is unexplained.
6. The primary artefact is gated; everything extracted here is the vendor's own public summary of its own report.

## Relevance to us

RQ1 (directional only), RQ5 (F6 is a clean practitioner-adjacent statement of bottleneck displacement — §5 tension 6), RQ6 (Lead Time to Value as a candidate metric is currently unadoptable because undefined; the F2–F5 spreads are usable as external benchmark context). Relevance 3/5.
