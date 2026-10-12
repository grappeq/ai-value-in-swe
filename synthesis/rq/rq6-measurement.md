# RQ6 — Internal Measurement: What to Instrument, What to Avoid

**Question (PROTOCOL §1):** Given RQ1–RQ5, what should we instrument internally to know whether AI is working for us, and which popular metrics should be avoided?

## 1. Headline answer

The five sibling memos converge on one instrumentation logic, not five separate ones. RQ1/RQ5 show individual-level gains (1.46–1.99×, `he-2026-2x-mandate`) dilute severely at system level — the cross-company figure (+7.76% PR throughput against +65% usage growth, `dx-reock-2026`) is Tier D direction-only evidence, and the Tier A witness is he-2026's own raw-vs-causal gap (2.09× → 1.46×) — so anything we instrument must measure delivery and absorption at the system level, not individual activity, or we will re-learn the dilution gap the hard way. RQ2/tension-1 show self-report is decoupled from measured outcome in every paired design found (`metr-2025-rct`, `stanford-denisov-blanch`), in both directions — so self-report may capture sentiment but must never be read as a magnitude. RQ4 shows cost and outcome telemetry are never published together by the same source (`he-2026-2x-mandate`, `uber-2026-claude-cost`, `cloudflare-2026-ai-review` each publish one half) — so every cost meter we build needs an outcome meter attached from day one, or we reproduce the exact gap this research found at three separate companies. RQ3 adds that failure concentrates in review absorption and skill formation, both of which are invisible to throughput counts alone.

## 2. Metrics to adopt (candidate set — Phase 5 cuts to ≤6)

| # | Metric | What it detects | Evidence it does real work | Pitfalls |
|---|---|---|---|---|
| 1 | **PR/task throughput per developer, with within-team fixed effects and anti-gaming exclusions** | Real velocity gain net of calendar drift, hiring, and split-commit gaming | `he-2026-2x-mandate`'s DiD design isolates 1.46–1.99× from a 2.09× raw ratio bundling calendar drift; `dx-reock-2026`'s population trend shows raw counts alone dilute to near-meaninglessness without controls | Raw counts alone are on the reject list below; only the *controlled* version survives |
| 2 | **Review coverage % + substantive-review share** | Early warning that generation is outrunning absorption capacity | `he-2026-2x-mandate`: human-review coverage 89%→68%, substantive review ~halved (39%→21%) while PRs grew 3.1× — the clearest quantified bottleneck signal in the base (tension 6) | Needs a "substantive" definition (not just "reviewed") or it collapses into a gameable rubber-stamp count |
| 3 | **Review latency / reviewer queue depth** | Whether the bottleneck has moved from generation to review | Tension 6's five-org convergence; `he-2026-2x-mandate`'s cycle time +22% despite throughput doubling | Confounded by headcount/org growth unless normalised per reviewer |
| 4 | **Revert rate + change-failure rate, paired, never alone** | Stability cost of higher throughput | `he-2026-2x-mandate`: flat-to-improving reverts (−0.059 to −0.067***) paired with cost/review data — credible only because paired; DORA's CFR gives the industry-standard partner metric | A revert-rate null with no throughput/cost pairing proves nothing (this is exactly why it's paired here) |
| 5 | **Rework share / churn on AI-touched work, with per-repo adoption dating** | Genuine rework cost, not a calendar artefact | `churn-151-repos-2025`'s design lesson: per-repo self-adoption dating with RDD/placebo checks overturned a population-level calendar trend (`gitclear-2025`); Stanford's 350-engineer case found rework 2.5× despite PRs +14% | Calendar-trend churn metrics are unreliable (see reject list); date adoption per team/repo, not by policy-rollout date |
| 6 | **Downstream-maintenance signal on agent-authored code** | Whether agent output degrades future velocity, not just present-day metrics | `agent-maintainability-2026`: task-resolve rate drops up to 13.1pp building on agent code, driven by behavioural-contract drift invisible to static metrics | **Feasibility flag:** the one rigorous study used a controlled benchmark harness; no source shows how to instrument this on a live production codebase — treat as a research question, not a ready-made dashboard, for now |
| 7 | **Token/licence spend per developer, paired with an outcome metric on the same unit of work** | Cost blow-out and the cost-without-outcome gap RQ4 found everywhere | `uber-2026-claude-cost`'s 20×-ramp/leaderboard-driven blow-out and `he-2026-2x-mandate`'s $42→$856/dev-month ramp both lack a paired outcome figure in the literature — don't repeat that gap internally | A cost meter with no adjacent outcome meter is worse than no meter — it invites exactly the "tokenmaxxing" incentive Uber describes |
| 8 | **Comprehension/skill spot-checks (learning-heavy work) + wellbeing/experience tracking, kept separate from productivity claims** | Skill atrophy and experience cost that speed metrics cannot see | `shen-2026-coding-skills`: d=0.738 comprehension loss with no speed offset; `vella-blincoe-2026`: self-reported productivity and self-reported experience are statistically decoupled (p=0.313) — track them as separate constructs, never combine into one productivity number | Both are E2/self-report-only evidence; treat as sentinel checks, not magnitude evidence, and never fold into a throughput score |

## 3. Metrics to reject (compressed from `tension-7-bad-metrics.md`)

| Metric | One line of evidence |
|---|---|
| **LOC / lines added** | Rewards scope creep; `metr-2025-rct` +47% LOC alongside *worse* (+19%) completion time |
| **Commit/PR counts alone** | Stanford's 350-engineer case: PRs +14%, quality −9%, rework 2.5×, effective output flat |
| **Suggestion acceptance rate** | `metr-2025-rct`: <44% acceptance while measured 19% *slower* — acceptance and value move opposite ways |
| **"AI-generated %" of code** | `uber-2026-claude-cost`'s ~70% figure has no disclosed methodology; the academic version (`aidev-dataset-2026`) is an unvalidated heuristic with no precision/recall estimate |
| **Token/usage volume as a value proxy** | `stanford-denisov-blanch`: r≈0.20 with a "death valley" around 10M tokens/month — heavy users underperformed moderate ones |
| **Self-reported productivity multipliers** | Four independent paired designs (tension 1) show self-report decoupled from measured change, in either direction |
| **"Time to first review comment"** *(added, re-derivation R1)* | Becomes definitionally zero and meaning-free once an AI auto-comments on every PR (`atlassian-2026-ai-review` demonstrates the mechanism) — pair review-latency metrics with substantive-review measures or they will be gamed by auto-commenting |
| **Any single metric used alone** | `space-dx-core4`'s verbatim, tri-confirmed claim: productivity "cannot be measured by a single metric or dimension" |

## 4. Design principles for the internal pilot (from RQ2)

- Prefer **within-team/within-developer** comparisons with fixed effects over calendar trends — a population trend without adoption dating cannot separate genuine effect from dilution or composition drift (`dx-reock-2026` vs `he-2026-2x-mandate`; `churn-151-repos-2025` vs `gitclear-2025`).
- **Date adoption per team/repo**, not by rollout announcement — `he-2026-2x-mandate`'s own decomposition shows the policy mandate contributed ~zero once adoption and accumulated use are separated.
- **Pre-register the outcome metric** before the pilot starts, paired with whatever cost metric is tracked — RQ4's core finding is that this pairing has never once been done in the published literature.
- **Expect a J-curve, but don't assume one** — `cursor-velocity-quality-2025` and `agents-vs-ides-2026` both find gains *decaying*, one reversing to strongly negative by month 6; don't pre-commit to "gains build over time" without checking our own trajectory.
- **Self-report only for sentiment/adoption/trust**, never for magnitude — and keep it structurally separate from any productivity number, per `vella-blincoe-2026`'s internal decoupling.

## 5. Claims list with confidence

1. System-level delivery metrics will show a fraction of any pilot's individual-level gain; instrumenting only the individual level will substantially overstate impact (the specific ratio is not citable — the cross-company side is Tier D only). **Medium** for direction — Tier A internal evidence (he-2026's raw-vs-causal gap) plus consistent Tier D shape; magnitude not triangulated.
2. No popular single metric (LOC, PR/commit counts, acceptance rate, "AI-generated %", token volume, self-report) should anchor an internal impact claim. **High** — tension-7, sourced failure mode against every named metric.
3. A cost meter without a paired outcome meter reproduces a documented failure mode (Uber's leaderboard-driven blow-out). **High** — three independent organisations show the identical omission.
4. Review coverage/latency is the single best-evidenced early-warning instrument for bottleneck displacement. **Medium-high for the mechanism, low-medium for any magnitude** — per the tension-6 verdict: five organisations converge but they comprise one measured firm, two COI'd vendor telemetry sets, and two zero-number narratives.
5. Downstream-maintenance signal on agent code is real but not yet practically instrumentable in production. **Medium** — one clean controlled study, no field-deployable method demonstrated anywhere in this evidence base.

## What this means for us

Phase 5 should carry forward a shortlist built around three pairs, not eight standalone dashboards: (i) controlled throughput **paired with** review coverage/latency, so a speedup never gets reported without its absorption cost; (ii) revert/change-failure rate **paired with** the same throughput figure, so stability is never assumed; (iii) token/licence spend **paired with** whichever outcome metric it is meant to justify. Comprehension and wellbeing checks ride alongside as sentinel, non-productivity signals. Everything else on the candidate list — per-repo adoption-dated rework, downstream-maintainability spot-checks — is a second-wave addition once the first three pairs are running, not a day-one requirement. The single discipline this whole evidence base argues for is: never publish a number from one side of a pair.
