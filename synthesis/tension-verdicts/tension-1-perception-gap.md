# Tension 1 — Perception–reality gap: verdict

## 1. The tension as pre-registered

PROTOCOL §5.1: "**Perception–reality gap.** The METR 2025 RCT found experienced open-source devs were ~19% *slower* with AI while believing they were ~20% faster. **If replicated, this invalidates self-report surveys as impact evidence** and is the single most important input to RQ6."

The pre-registered condition is specific and narrow: *replication of METR's design and direction* — over-estimation of AI's benefit by experienced developers — is what was set up to license the strong claim.

## 2. Strongest evidence the gap is real and large

Four independent, paired (self-report vs measured, same people/study) datapoints:

- **metr-2025-rct** — Tier A, E3 (early IDE-agent, boundary caveat). Experienced OSS devs: measured 19% *slower* (S=0.188); believed ~20% faster post-hoc (pre-study forecast 24% faster). **~39–43pp swing**, over-estimate.
- **peng-2023-copilot-rct** — Tier A (vendor-COI), E1. Upwork freelancers: measured 55.8% *faster*; self-estimated only ~35% faster. **~21pp under-estimate** — opposite sign to METR.
- **stanford-denisov-blanch** (the 43-developer experiment) — Tier B, talk-grade, era-indeterminate. Self-rated productivity percentile vs measured percentile: off by **~30 percentile points** on average, "almost as good as flipping a coin," only 1-in-3 within own quartile. Not AI-specific; general self-assessment miscalibration.
- **stray-2026-nav** — Tier B, E1, cleanest independence. Individual-level *change-score* pairing on the same 25 developers: self-reported productivity change vs measured commit-activity change, **ρ≈0.17 (p=0.406, ns)** across six metrics; no adopter reported a decrease despite several showing measured decline.

Each is a genuinely paired design (not a survey compared to a different study's average): METR and Peng compare belief-vs-measured at the group level within the same RCT; Stanford compares self-rank-vs-measured-rank cross-sectionally; Stray compares within-person *deltas* longitudinally. Three different statistical objects, same qualitative conclusion.

## 3. Strongest counter-evidence / complications

- **No independent replication of METR's specific design (direction: experienced devs, familiar brownfield code, over-estimating) exists.** METR's own Feb 2026 follow-up wave attempted one and judged its own data unreliable (selection bias, pay differences, tracking problems) — it neither confirms nor replicates the original.
- **Direction is inconsistent across settings**, so "developers always overestimate AI" is *not* supported: Peng's freelancers on a short greenfield task under-estimated by ~21pp — the mirror image of METR. The gap's *existence* is robust; its *sign* is population/task/setting-dependent (brownfield/familiar-code overestimation vs greenfield/toy-task underestimation is the leading candidate reconciliation, per contradictions.md, but unconfirmed as causal).
- **Vella-Blincoe-2026** (Tier B) is perception-only — no measured comparator at all — so it cannot be paired into this contradiction; it only shows self-report constructs (productivity vs cognitive load/flow) decouple *from each other*, a related but distinct RQ2 finding.
- **metr-2026-survey** (weak Tier C, self-report only) shows self-reported multipliers *growing more extreme* in 2026 (median 3x speed, 1.4–2x value) with no measured comparator — METR itself cites its own RCT's ~40pp overestimate as a reason for scepticism about its own new numbers, and METR staff report *lower* gains than external respondents. This strengthens the "self-report is untethered" reading but adds no new paired datapoint.
- No source in this base reports self-reported *learning/comprehension* matching measured comprehension in a way that would counter the gap; the Shen/Tamkin comprehension-loss material (measured, not self-report-paired on this axis) is not a counter-example here.

## 4. Era audit

Only **metr-2025-rct** is E3 (early IDE-agent, with an explicit E2/E3-boundary caveat — Cursor Pro agent/chat, largely pre-Claude-4 models). The other three paired datapoints are pre-agentic: Peng is E1 (pure autocomplete, pre-GA, no chat existed), Stray is E1 (pre-agent-mode Copilot, 2022–2024 telemetry), Stanford is E1/E2-mixed (talk aggregates tooling across 2022–2025 without modality splitting). PROTOCOL §2 lists perception gaps as a *candidate* era-independent effect (alongside bottleneck displacement and seniority asymmetry). The evidence here supports that candidacy: the *pattern* (self-report magnitude/direction is decoupled from measured outcome) recurs identically in three pre-agentic designs and one early-agentic one, using three different statistical methods, which is exactly the signature of an era-independent effect rather than an artefact of one tool generation.

## 5. Independence audit

The four datapoints are genuinely independent: **metr-2025-rct** (non-profit research org, US, OSS developers, RCT), **peng-2023-copilot-rct** (GitHub/Microsoft-affiliated, freelancers, RCT — vendor-COI flagged, but the measured outcome is objective/automated), **stanford-denisov-blanch** (Stanford academic group, cross-company telemetry, talk-grade), **stray-2026-nav** (University of Oslo/SINTEF, Norwegian public-sector org, no vendor ties — the cleanest independence line in the whole evidence base). Different countries, different populations (OSS maintainers / Upwork freelancers / 100k+-developer cross-company panel / Norwegian public-sector devs), different research teams with no shared authorship, different statistical designs. This is one of the few claims in the base with genuine four-way triangulation, not restatement.

## 6. VERDICT

**Contested on direction; resolved on the broader methodological claim.** Confidence: **high** that self-report magnitude/direction is uninformative about measured productivity change — justified by four independent designs, different populations and methods, converging on the same conclusion despite disagreeing on sign. Confidence: **low** that the specific pre-registered condition (experienced devs systematically over-estimate AI benefit) is a general rule — justified by Peng's opposite-direction result and the absence of any independent replication of METR's exact design/population.

Precision on what is and is not resolved: the §5.1 "if replicated" condition, read literally as *METR's specific direction replicating*, is **unmet** — no independent study replicates over-estimation by experienced devs on familiar brownfield code, and one study (Peng) shows the opposite sign in a different setting. But the *operative consequence* §5.1 draws from that condition — that self-report magnitude cannot serve as impact evidence — is supported anyway, via a different and arguably stronger route: four methodologically distinct pairings all show self-report decoupled from measured outcome, regardless of sign. The narrow pre-registered trigger failed; the substantive conclusion it was meant to license holds independently.

**For RQ2/RQ6:** self-report surveys (DORA, Vella-Blincoe, metr-2026-survey, vendor "X% report productivity gains" claims) cannot be treated as impact evidence on AI's effect on productivity — no exec-brief effect-size claim should rest on a bare self-report percentage. They remain legitimately useful for what they *do* measure: sentiment, adoption/trust trends, tool-usage patterns, and perceived-experience dimensions (cognitive load, flow) as constructs in their own right, provided they are never translated into an implied productivity number.

## 7. What would change the verdict

An independent RCT or matched-telemetry study on late-2025/2026 agentic tooling that reproduces METR's specific over-estimation direction in a different population would resolve the narrow §5.1 condition. A second brownfield/familiar-code population showing under-estimation (mirroring Peng-style results outside greenfield) would instead confirm the "setting determines sign" reconciliation over "population determines sign." Absent either, the verdict on the broader claim is unlikely to move — it is already load-bearing on four legs.

## 8. Feeds exec brief as

Self-reported AI-productivity gains — from any survey, including our own future internal ones — cannot be trusted as a magnitude or even a directional signal of real impact; four independent studies show self-report decoupled from measured outcome, though not always in the same direction.
