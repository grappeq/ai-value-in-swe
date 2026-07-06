# Tension 4 — Quality Debt Signals: Verdict

## 1. The tension as pre-registered

PROTOCOL §5.4: "Quality debt signals. GitClear's multi-year analyses report rising code churn and duplication and declining refactoring in the AI era. Cross-check against defect-rate studies (e.g., Uplevel's contested +41% bug-rate finding)."

## 2. Six separable legs

**(a) CHURN — contested, leaning null pre-agentic.** gitclear-2025 (Tier B, dual-vendor COI, era-unsegmented) reports 2-week churn +15% (16.1%→18.6%), but the entire rise sits in one 2024→2025 step that coincides with an undisclosed ~3.3–3.8× jump in the underlying per-signal sample size — an unaddressed composition confound. churn-151-repos-2025 (Tier A, RDD+placebo, independent academia, E1/E2 only — explicitly excludes Claude Code) finds pooled churn *fell* (line-based 0.68→0.50, file-based 0.17→0.06, both p<0.05); ~80% of repos show no RDD discontinuity; the one real positive finding is that churn concentrates in generation tasks specifically. Adjudicated in contradictions.md as contested, leaning Side B for the pre-agentic claim. **Neither side has tested E3.**

**(b) DUPLICATION — weakest leg.** GitClear reports +81% (Tier B, COI). Three independent, better-controlled E3 designs disagree: agents-vs-ides-2026 (AF +7.92% ns, IF −0.94% ns), cursor-velocity-quality-2025 (+7.03% ns), and agent-maintainability-2026 (duplication-adjacent metrics non-significant as predictors). GitClear's population-level positive is the outlier once any counterfactual design is applied.

**(c) COMPLEXITY/STATIC WARNINGS — best-supported, but only two voices.** cursor-velocity-quality-2025 (warnings +30.3%, complexity +41.6%, Tier A, E3, persistent 6 months) and agents-vs-ides-2026 (warnings +18%, complexity +35–43%, Tier A, E3) are the **same CMU lab** (Vasilescu/He/Agarwal) — one evidentiary voice by their own admission, despite independently-collected datasets. GitClear's declining moved/refactor lines (−70 to −82%) and rising obfuscation (+47%) are a different construct (Tier B, COI) but directionally consistent. Total: two voices, not three.

**(d) DOWNSTREAM MAINTENANCE COST of agent code — the single strongest, cleanest E3 leg.** agent-maintainability-2026 (Tier A, NYU+CMU-Chen, no author/dataset overlap with the Vasilescu lab or GitClear) manipulates authorship directly: agent-on-agent code drops task-resolve rate up to 13.1pp vs human-authored precursors, refactoring hit hardest (−8.21% avg) vs bug-fixing (−4.05%). Genuinely independent. **But its central result is a null**: static metrics (cyclomatic/cognitive complexity, Halstead, LOC) do not predict which side of the gap wins (McFadden R²=0.069); only behavioural input/error-contract drift and PR2 verbosity are significant, and drift explains only 20.6% of a sub-cohort.

**(e) REWORK — concrete but single-source and construct-mismatched with (a).** stanford-denisov-blanch (Tier B, talk-only): gross gains of 30–40% net down to 15–20% on average — roughly half eaten by rework; a named 350-person case shows PRs +14%, quality score −9%, rework 2.5×, effective output flat. Vivid and specific, but one unpublished research programme, and its "rework" (model-scored) is not the same construct as churn-151's line-revision-within-14-days — not a direct contradiction of leg (a), but not confirmed convergence either.

**(f) DEFECT RATE — contested and thin.** uplevel-2024 (Tier D, COI, E1): +41% bugs, no bug definition, access-not-usage confound. cui-2024-copilot-field (Tier A, E1): build success rate −5.53% pooled (ns), −17.4% significant at Accenture — a real but modest signal sitting between Uplevel and vendor counter-claims. **No clean E3 defect study exists anywhere in this evidence base.**

## 3. The mechanism problem

Leg (c)'s metric family — complexity, static warnings, duplication — is exactly what agent-maintainability-2026 shows does *not* predict leg (d)'s actual cost (task-resolve-rate collapse). Quality debt is probably real, but the popular proxies may be measuring a correlate of rising agent authorship, not its cause. Complexity/duplication dashboards risk under-detecting the real failure mode (behavioural-contract drift). This is a direct input to RQ6.

## 4. Era + independence audit

CMU trio (cursor-velocity-quality-2025, agents-vs-ides-2026, and he-2026-2x-mandate per their own cross-referenced overlap note) = one lab, three datasets, **one voice**. GitClear = Tier B, dual-vendor COI, proprietary non-auditable classifier, undisclosed sample-composition jump. Genuinely independent voices: agent-maintainability-2026 (leg d) stands alone and cleanly E3; leg (b)'s null is corroborated by CMU (one voice) + agent-maintainability-2026 (second voice) against GitClear's outlier. Legs (a) and (f) have no E3 evidence at all on either side.

## 5. VERDICT

**Contested-but-substantiated. Confidence: medium.** A real, persistent quality/maintainability cost from agentic coding is supported by genuinely independent evidence on the two best legs — complexity/warnings growth (CMU, Tier A) and downstream maintenance cost (agent-maintainability-2026, Tier A, clean E3) — but magnitude, defect-rate translation, and the validity of the static-metric proxies remain open. The popular churn/duplication framing — GitClear's own headline — is the *least*-supported version of the claim once independent, controlled designs are applied.

## 6. What would change the verdict

A non-CMU replication of the complexity/warnings finding (removes the one-voice cap on leg c); an E3-only churn study on agentic adoption (settles leg a); a multi-step extension of CodeThread testing compounding drift (settles leg d's ceiling); any rigorous E3 defect-rate study (closes leg f); confirmation that GitClear's 2024→2025 jump is a customer-onboarding artefact (would further weaken legs a and, by extension, the refactoring-decline framing).

## 7. Feeds exec brief as

AI-assisted coding carries a real, measured maintainability tax — rising complexity and static-analysis warnings that persist after velocity gains fade, and agent-authored code that is measurably harder for the next agent to build on — but this cost is poorly captured by the popular "churn" and "duplication" metrics, and its translation into defect rates remains unmeasured in the agentic era.
