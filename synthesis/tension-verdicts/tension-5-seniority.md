# Tension 5 — Seniority asymmetry: verdict

## 1. The tension as pre-registered

PROTOCOL §5.5: "**Seniority asymmetry.** Field experiments (Cui et al., Microsoft/Accenture) found gains concentrated in junior developers. **Strategic implication differs radically depending on whether AI lifts the floor or the ceiling.**"

## 2. The E1 baseline is weaker than commonly cited

The "junior developers gain more" claim is repeated as settled fact across secondary write-ups, but the primary sources behind it do not support that confidence:

- **cui-2024-copilot-field** (Tier A, E1, Microsoft-only sub-sample): short-tenure devs +27–39%, long-tenure +8–13%; junior +21–40%, senior +7–16%. The paper's own figure reports **p-values of ~0.13–0.77** — the authors are explicit these heterogeneity estimates are "noisy" and **not statistically significant at conventional levels**. The pattern is directionally consistent across three outcome measures within one company, which is real triangulation *within* a single paper, but it is not a statistically confirmed result.
- **peng-2023-copilot-rct** (Tier A, vendor-COI, E1): heterogeneity comes from Table 1 covariates on a single toy greenfield HTTP-server task, n≈70 completers. Programming-experience coefficient is only marginal (p=0.063); the significant covariates are daily-coding-hours and age-band, not experience/seniority directly. The authors' own interpretation ("less experienced... benefit more") is a reasonable read of the coefficient pattern but rests on one small, non-representative population doing one task.
- **google-rct-2024** (Tier A-candidate, E1/E2 boundary): the seniority × AI interaction is **null (p=.706)** and, where it points anywhere, points in the **contrary** direction (more senior engineers benefiting somewhat more) — the opposite sign from the junior-gains story. The authors themselves caution the study is underpowered for interaction effects and do not treat this as evidence against the seniority-asymmetry literature.

Taken together, the field-experiment case for "gains concentrate in juniors" rests on **directional, underpowered, largely non-significant evidence from one company's tenure split (Cui) plus one small toy-task covariate table (Peng)**, with a same-era study finding a null/contrary interaction (Google). This is a Phase 0/2 finding of this project: the seniority-asymmetry claim, as usually stated, overstates what the E1 literature actually shows.

## 3. The E3 evidence

Exactly one measured E3 datapoint exists:

- **he-2026-2x-mandate** (Tier A, E3, single firm, DiD with developer fixed effects): IC +27%, Senior +42%, Staff +39%, Principal +38% (n=16, imprecise) — a **flat gradient**, statistically indistinguishable across the IC-to-Principal ladder. The one outlier is Management (+86%), read by the authors as a "re-entry" effect, not a seniority effect. This is directly relevant but is a single, self-selected, favourable-site case study explicitly framed by its own authors as an "upper envelope," and it shares an author (Denisov-Blanch) with other sources in this evidence base — it is not independently replicated.

Alongside it, **prageng-2026-survey** (Tier C, self-report, n=906, senior-skewed newsletter readership) provides adoption/sentiment signal only: Staff+ adopt agents most (63.5% vs 49.7% regular engineers), seniors describe AI as an "amplifier," juniors describe it as stressful with higher rework and token costs. This is directionally consistent with a reversal (seniors extracting more leverage), but it measures adoption and sentiment, not output — it cannot confirm or refute Cui's numeric claim, and its own EM/lead datapoint (lowest adoption at 46.1%) shows the pattern is not even monotonic by role within this sample.

The practitioner "seniors extract more leverage from agents" hypothesis therefore remains a hypothesis: one non-independent case study plus adoption/sentiment correlation, not a powered measured-output comparison.

## 4. The two-sided complication

Even where task-speed gains for juniors are real, **shen-2026-coding-skills** (Tier A-candidate RCT, E2) found AI-assisted learners scored significantly worse on a comprehension quiz (d=0.738, p=0.010) with no significant time saving — a measured comprehension cost of AI-assisted work. The authors flag this as plausibly a *lower bound* for agentic tools (more offloading, not less). Two important caveats: the sample was **majority-experienced by tenure** (55.8% at 7+ years), not junior, so it does not directly test junior developers; and the "juniors delegate more, so juniors lose more learning" half of the argument is an imported mechanism hypothesis, not this paper's own finding. Still, it means a floor-lifting story on task speed may trade against capability formation — a cost that would fall disproportionately on juniors if they are the ones delegating most. **metr-2025-rct** cuts the other way for seniors: its slowdown was concentrated in *experienced* developers working on *highly familiar* code, driven partly by high familiarity itself as a moderator — suggesting seniors do not uniformly benefit even where they might extract more "leverage" in the abstract.

## 5. Era + independence audit

- **E1:** cui-2024-copilot-field, peng-2023-copilot-rct — both non-significant/marginal heterogeneity.
- **E1/E2 boundary:** google-rct-2024 — null, contrary-direction interaction.
- **E2:** shen-2026-coding-skills — comprehension-cost RCT, not seniority-specific by design.
- **E3:** he-2026-2x-mandate (measured, single firm) — flat gradient. metr-2025-rct (E2/E3 boundary) — familiarity (correlated with, not identical to, seniority) moderates toward more slowdown.
- **E3 adoption/sentiment:** prageng-2026-survey — directional reversal signal, self-report only.

Independence is thin on the E3 side: he-2026-2x-mandate is the only measured-output E3 source and is a single self-selected firm; no independent E3 study replicates or contradicts it with a powered seniority split.

## 6. VERDICT

**Insufficient evidence.** Confidence: **high** that the commonly-cited "field experiments found junior gains" claim overstates the E1 evidence (Cui's own p-values, Peng's single-task covariates, and Google's null/contrary interaction jointly show this — a straightforward reading of primary sources). Confidence: **low** on any claim about the agentic era specifically, in either direction — one non-independent, self-selected case study (flat gradient) and one self-report adoption/sentiment survey (reversal-consistent but not output data) do not constitute a powered test. Neither "AI lifts the floor" nor "AI lifts the ceiling" is establishable for E3 on current evidence, and the two-sided skill-formation complication means even a confirmed floor-lift would not straightforwardly be good news. The E1 junior-gains story should not be repeated as established fact in the exec brief.

## 7. What would change the verdict — UPDATED 2026-07-06 (audit remediation)

The original draft asserted no E3 study with a powered seniority split existed; the audit-mandated bounded hunt found one published 1 July 2026, now extracted: **microsoft-cli-agents-2026** (Murphy-Hill/Butler/Savelieva, arXiv:2607.01418; Tier B, E3-clean — Claude Code + Copilot CLI; tens of thousands of engineers; synthetic control + within-person designs; Microsoft-on-Microsoft COI, and NOT independent of heilman-2026-microsoft via shared authorship). Its output-impact heterogeneity is a verbally-described **C-shape** — junior ICs and senior managers gain more than the IC4 mid-level reference (only reference-group CIs are numerically quotable: IC4 +21.3% [19.6, 23.0]); its widely-quotable numbers (+22% / −13% / −14% odds) are **adoption** findings, not impact findings — do not conflate.

**Effect on the verdict: sharpened, not changed.** Two single-firm, COI-flagged E3 datapoints now exist and they disagree on the *shape* of the effect (he-2026's flat IC→Principal gradient vs Microsoft's C-shape), while an unextracted Tier D vendor claim (Opsera: seniors ~5x juniors) contradicts both. Insufficient evidence stands — now because the only E3 datapoints actively disagree, not merely because they were scarce. What would change it: a study independent of BOTH the He/Denisov-Blanch group AND Microsoft, with a powered seniority split on measured output — none found in this programme's search as of July 2026 (an existence claim bounded by our search, not a universal negative).

## 8. Feeds exec brief as

The widely-repeated claim that AI helps junior developers most rests on non-significant pre-agentic evidence, and the two agentic-era measured datapoints disagree with each other on the shape of the effect (flat gradient vs C-shape) — treat "does AI lift the floor or the ceiling" as unresolved, not as a settled input to career-ladder or team-composition strategy.
