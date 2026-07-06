# Contradictions

## §5 tension verdicts (Phase 3, 2026-07-06) — full memos in synthesis/tension-verdicts/

| # | Tension | Verdict | Confidence |
|---|---|---|---|
| 1 | Perception–reality gap | SPLIT: METR's specific direction NOT replicated (Peng runs opposite); the operative claim — self-report magnitude is uninformative about measured change — RESOLVED on four independent paired designs | high (operative claim) / low (direction generality) |
| 2 | Greenfield vs brownfield | CONTESTED on magnitude/mechanism; direction unanimous (no source shows brownfield > greenfield); sharpest quantifications non-independent; construct unstable across sources | medium |
| 3 | Throughput vs stability | CONTESTED: DORA's flip sits inside one redefined self-report instrument; measured stability proxies conflict on non-comparable constructs; "temporary J-curve" has zero longitudinal support | medium |
| 4 | Quality debt | CONTESTED-BUT-SUBSTANTIATED on two independent Tier A legs (complexity growth; downstream agent-code maintenance cost); churn/duplication is the WEAKEST-supported version; static-metric proxies don't predict the real cost | medium |
| 5 | Seniority asymmetry | INSUFFICIENT EVIDENCE for the agentic era; secondary finding: the E1 "juniors gain most" claim overstates its own statistics | — (secondary finding: high) |
| 6 | Bottleneck displacement | CONFIRMED in direction — five independent orgs converge, no dissenting source; magnitude unresolved (one unreplicated firm + two COI'd telemetry sets disagreeing 2–8x); automation absorbs the review queue but not clearly the function | medium-high (mechanism) / low-medium (magnitude) |
| 7 | Bad-metric traps | RESOLVED: seven-metric anti-metrics table with per-metric evidence; no source defended any §5.7 metric as impact evidence | high |

---

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
- Fourth datapoint (2026-07-06): stray-2026-nav — individual-level pairing on the same 25 developers: change in self-reported productivity vs change in measured commit activity correlates at ρ≈0.17 (p=0.406, ns across all six metrics); no adopter reported a decrease despite several showing measured decline. Not an over/under-estimate — a near-zero correlation. Tier B, E1 (pre-agentic), cleanest independence in the base. Net across four datapoints: self-report magnitude is uninformative about measured change in every era tested; direction of error varies by setting.
- Addendum (2026-07-06): metr-2026-survey — self-reported multipliers are growing more extreme in 2026 (median 3x "speed", 1.4–2x "value"; 2.5x forecast for 2027) with NO measured comparator; METR itself cites its own RCT's ~40pp overestimate as reason for scepticism, and METR's own staff report lower gains than external respondents. Weak-C, ~25% SWE sample. Treat as evidence about the hype baseline, not about productivity.
- Related §5 tension: 1 (perception–reality gap)

## Magnitude of AI throughput gains in vendor telemetry: Faros vs DX
- Side A: faros-2026-whiplash — task throughput/dev +33.7%, epics/dev +66.2%, PR merge rate/dev +16.2% between lowest- and highest-adoption quarters; Tier D (COI), E2/E3 blend; within-team before/after design with unaddressed time-trend confounders; several magnitudes denominator-sensitive.
- Side B: dx-reock-2026 — EXTRACTED. ~400 companies, Nov 2024–Feb 2026, org-level longitudinal: AI usage +65% (metric undefined), PR throughput +7.76%; essentially no disclosed methodology (no significance tests, no defined usage metric, sample selection undisclosed).
- Adjudication (2026-07-06, both extracted): **largely dissolves on inspection**. The "4–8x" gap compared different units of work — PR-to-PR (Faros +16.2% merge rate/dev vs DX +7.76%) the gap is ≈2x, within what estimand and window differences can absorb. Disclosure asymmetry noted: Faros discloses a statistical procedure, DX essentially none. Both remain Tier D, direction-convergent (modest delivery-level gains + review bottleneck). Also checked: DX's +7.76% coexists with he-2026-2x-mandate's 1.46–1.72x within-adopter effect — population-average dilution vs best-case single-firm causal effect, an expected signature, not a contradiction.
- Related §5 tension: 6 (bottleneck displacement)
- Tension-6 voice tally (2026-07-06, post-P1.5): mechanism-existence has three converging independent orgs (he-2026 measured; Agoda and Zendesk narrative-only — the Zendesk piece is a prescriptive proposal, not a rollout report). Magnitude rests ONLY on Tier D vendor telemetry (Faros, DX) plus one unreplicated Tier A single-firm study (he-2026). OSS data (unreviewed-ai-prs-2026) complicates the coverage-collapse leg: matched-baseline review participation is equal for AI and human PRs; what shifts is composition (agent-steering displaces evaluation).

## Copilot defect-rate: +41% bugs vs vendor counter-claims
- Side A: uplevel-2024 — +41% bug rate in PRs for the Copilot-access group; Tier D (COI: vendor marketing), E1; no bug definition, CI, or significance test published; measures access not usage; observational, no randomisation.
- Side B: defect-rate-side-b — EXTRACTED (2026-07-06, audit remediation). Two independent-COI Tier D counter-claims: GitHub's own lab study (randomised, n=202, narrow Python task, E1/E2: +53.2% test-pass likelihood, small readability/approval gains — GitHub itself flags effects as small) and CodeRabbit (470 OSS PRs: 1.7x more issues in AI-coauthored PRs — measured by CodeRabbit's own product, era untaggable). Correction: the "Accenture" piece contains NO defect/quality figure at all — it was miscast as quality counter-evidence in circulation.
- Adjacent evidence: cui-2024-copilot-field (Tier A, E1) found build success rate −5.53% pooled, −17.4% significant at Accenture — a measured mild quality-debt signal sitting between the two vendor narratives; gitclear-2025 offers no defect measurement despite its title.
- ADJUDICATED (2026-07-06, both sides read): **insufficient evidence — no trustworthy defect-rate estimate exists in either direction.** The dispute is not "vendor vs vendor" but four non-comparable constructs across four COI'd Tier D sources (Uplevel's undefined "bug rate"; GitHub's narrow lab task; CodeRabbit's own-tool issue counts; Accenture's nothing). The only Tier A-adjacent signal remains Cui's build-success decline (−5.53% pooled / −17.4% Accenture, E1) — small, measured, and sitting between the vendor narratives.
- Related §5 tension: 4 (quality debt signals) — leg (f) re-verdicted accordingly
