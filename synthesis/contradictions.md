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
- Side B: arXiv 2507.10422 (peer-reviewed, 151 repos) — reportedly found *no* general churn increase after GenAI adoption. NOT YET EXTRACTED — queued high priority; entry provisional until full-text cross-ref.
- Plausible reconciliation: different populations (GitClear customer base + megaprojects vs 151 sampled repos), different churn definitions, different adoption-attribution methods. Unresolved.
- Related §5 tension: 4 (quality debt signals)

## DORA throughput association: negative (2024) vs positive (2025)
- Side A: DORA 2024 (queued, not yet extracted) — AI adoption associated with reduced delivery throughput (−1.5% per 25% adoption increase) and reduced stability (+7.2% instability), as quoted within dora-2025; Tier B, E1/E2.
- Side B: dora-2025 — throughput association flipped positive (standardised betas, chart-only, 89% CrI); **instability association persisted**; Tier B, mixed era weighted pre-agentic; all outcomes self-reported.
- Plausible reconciliation (DORA's own): 2024 measured earlier-stage adoption; ecosystem adaptation (tooling maturity, team practices) since. Alternative: different instruments/samples across years; both waves self-report. Note the stability leg did NOT flip — only throughput did.
- Related §5 tension: 3 (throughput vs stability)

## Perception–reality gap: direction is not consistent
- Side A: metr-2025-rct — experienced OSS devs believed AI made them ~20% faster while measured 19% slower (over-estimate); Tier A, E3 (early IDE-agent).
- Side B: peng-2023-copilot-rct — freelancers in both arms self-estimated ~35% speedup while the measured treatment effect was 55.8% (under-estimate); Tier A (COI: GitHub/Microsoft), E1.
- Plausible reconciliation: self-report is miscalibrated in *both* directions depending on setting — experienced devs on familiar brownfield code overestimate AI benefit; freelancers on greenfield toy tasks underestimate it. Either way, self-report is an unreliable magnitude instrument (RQ2/RQ6); the gap itself, not its direction, is the robust finding so far.
- Related §5 tension: 1 (perception–reality gap)
