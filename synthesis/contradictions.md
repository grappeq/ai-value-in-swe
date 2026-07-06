# Contradictions

Appended at discovery time (operating-loop CROSS-REF step), never deferred to synthesis. One entry per contradiction:

```
## <short title>
- Side A: <source_id> — claim, effect size, tier, era
- Side B: <source_id> — claim, effect size, tier, era
- Plausible reconciliation (population / era / method / metric differences), or "unresolved"
- Related §5 tension: <number or "none">
```

Never average conflicting results; never pick the convenient one.

---

## Churn rise in the AI era: real or artefact?
- Side A: gitclear-2025 — two-week churn rose 3.1%→5.7% (2020→2024), framed as AI-driven quality decline; Tier B (COI: vendor telemetry), E1/E2 trendline. Note: undershot GitClear's own 7.1% projection.
- Side B: churn-151-repos-2025 (Xiao et al., IEEE TSE / arXiv:2507.10422) — EXTRACTED, Tier A (RDD + placebo checks, per-repo adoption dating), E1/E2. Pooled churn *fell* post-adoption (line-based 0.68→0.50, p<0.05); ~80% of repos show no discontinuity; churn definition deliberately matches GitClear's 2-week window, so definition is NOT the source of disagreement. Non-null nuance: churn rises specifically for GenAI code-*generation* tasks, not optimisation/maintenance.
- Adjudication (2026-07-06, both full texts read): **CONTESTED, leaning Side B** for the pre-agentic claim. Decisive differences: identification (Xiao has per-repo adoption dates + quasi-experiment; GitClear has only a population calendar trend riding an undisclosed ~3.3–3.8x composition jump) and population (enterprise customer base vs general OSS). Caveats against over-reading the null: self-admission proxy lags/understates adoption. **Both sides are E1/E2 — the E3/agentic version of the churn question is untested by either.**
- Update (2026-07-06, full 2026 PDF read, human-supplied): GitClear's side **weakened**. The 2026 edition's Appendix A1 shows churn rose 16.1%→18.6% (+15%) with nearly the entire rise in one 2024→2025 step — the same step where record counts behind all eight signals jump ~3.3–3.8× uniformly, consistent with undisclosed customer-base composition change. Dataset-composition drift is now a live, unaddressed alternative to an AI-driven churn increase. Detail in sources/gitclear-2025.md ("Churn contradiction assessment").
- Related §5 tension: 4 (quality debt signals)

## DORA throughput association: negative (2024) vs positive (2025)
- Side A: dora-2024 — AI adoption associated with delivery throughput −1.5% and delivery **stability −7.2%** per 25% adoption increase (primary text says "stability reduction"; DORA 2025's own paraphrase renames it "instability increase" — same direction, inverted construct name; cite the 2024 framing). Tier B, E1/E2 (2024 instrument had no agent-mode concept at all).
- Side B: dora-2025 — throughput association flipped positive (standardised betas, chart-only, 89% CrI); **the stability leg did NOT flip** — negative stability association persisted; Tier B, mixed era weighted pre-agentic; all outcomes self-reported.
- Plausible reconciliation: three live candidates, unresolved from primary texts alone — (a) real effect change with adoption maturity (DORA's own reading); (b) construct redefinition: 2024 itself introduced the throughput/stability two-factor split, with stability including a brand-new "rework rate" item (confirms RedMonk's comparability critique); (c) modality-mix shift between waves. Both waves are self-report throughout.
- Update (2026-07-06, dora-2026-roi extracted): DORA's 2026 interim ROI report recasts the persistent instability finding as a temporary "J-curve" tuition cost — but this is a **reframe, not a resolution** (Tier D: no new data; J-curve borrowed by analogy from transformation literature; single-wave cross-sectional data cannot show dip-then-rise). DORA 2025 itself tested and rejected the moderation this narrative implies ("found no evidence... instability still has significant detrimental effects"). The instability leg of tension 3 remains unresolved on evidence; treat "it's temporary" as vendor narrative until longitudinal data exists.
- Related §5 tension: 3 (throughput vs stability)

## Perception–reality gap: direction is not consistent
- Side A: metr-2025-rct — experienced OSS devs believed AI made them ~20% faster while measured 19% slower (over-estimate); Tier A, E3 (early IDE-agent).
- Side B: peng-2023-copilot-rct — freelancers in both arms self-estimated ~35% speedup while the measured treatment effect was 55.8% (under-estimate); Tier A (COI: GitHub/Microsoft), E1.
- Plausible reconciliation: self-report is miscalibrated in *both* directions depending on setting — experienced devs on familiar brownfield code overestimate AI benefit; freelancers on greenfield toy tasks underestimate it. Either way, self-report is an unreliable magnitude instrument (RQ2/RQ6); the gap itself, not its direction, is the robust finding so far.
- Adjacent evidence (transcript-verified Nov 2025): stanford-denisov-blanch 43-developer experiment — self-rated vs measured productivity percentile "almost as good as flipping a coin", off by ~30 percentile points, 1-in-3 within own quartile; supports "miscalibration, not uniform inflation". Tier B, talk-grade.
- Related §5 tension: 1 (perception–reality gap)

## Magnitude of AI throughput gains in vendor telemetry: Faros vs DX
- Side A: faros-2026-whiplash — task throughput/dev +33.7%, epics/dev +66.2%, PR merge rate/dev +16.2% between lowest- and highest-adoption quarters; Tier D (COI), E2/E3 blend; within-team before/after design with unaddressed time-trend confounders; several magnitudes denominator-sensitive.
- Side B: DX/Reock (Mar 2026, queued) — 400-company telemetry reportedly finds PR throughput +7.76% against AI usage +65%, i.e. gains ~4–8x smaller. NOT YET EXTRACTED — entry provisional.
- Plausible reconciliation: different estimands (within-team adoption-quarter contrast vs cross-company longitudinal trend), different metrics (task/epic vs PR throughput), different denominators. Both Tier D telemetry vendors; neither carries a claim alone. Both agree direction is positive-but-modest at the delivery level, and both show the review/absorption bottleneck.
- Related §5 tension: 6 (bottleneck displacement)

## Copilot defect-rate: +41% bugs vs vendor counter-claims
- Side A: uplevel-2024 — +41% bug rate in PRs for the Copilot-access group; Tier D (COI: vendor marketing), E1; no bug definition, CI, or significance test published; measures access not usage; observational, no randomisation.
- Side B: GitHub/Accenture (Nov 2024) counter-research — opposing quality findings; Tier D (COI: vendor of the product). NOT YET EXTRACTED — queued; entry provisional.
- Adjacent evidence: cui-2024-copilot-field (Tier A, E1) found build success rate −5.53% pooled, −17.4% significant at Accenture — a measured mild quality-debt signal sitting between the two vendor narratives; gitclear-2025 offers no defect measurement despite its title.
- Plausible reconciliation: both sides are Tier D with opposing COIs and non-comparable metrics ("bug rate in PRs" vs curated quality metrics). The Tier A adjacent evidence suggests a real but much smaller quality cost than Uplevel's headline. Unresolved pending Side B extraction.
- Related §5 tension: 4 (quality debt signals)
