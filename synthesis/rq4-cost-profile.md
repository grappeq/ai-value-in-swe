# RQ4 — Cost Profile

**RQ4 (PROTOCOL §1):** What does cost look like per task type — licence/token spend, review overhead, rework, verification time, quality debt? Where is the cost-to-value ratio favourable vs inverted? *Pre-registered expectation: literature-level cost data is thin; if RQ4 saturates at "insufficient evidence," that scarcity is the finding.*

## 1. Headline answer

The pre-registered expectation held: publishable cost data remains scarce. Across the whole evidence base, only four sources carry any real cost figure at all (he-2026-2x-mandate, uber-2026-claude-cost, cloudflare-2026-ai-review, plus one illustrative model from dora-2026-roi). That is the primary finding, not a gap to explain away.

But the sparse points that do exist are consistent in **shape**, not magnitude: a low, seat-licence-like baseline that balloons under heavy or incentivised use, with the tail running many multiples of the average (he-2026-2x-mandate; uber-2026-claude-cost). No two sources measure the same unit the same way, so none of this triangulates a number — only a curve.

The deeper finding is structural, not statistical: **cost telemetry and outcome telemetry are never published by the same source for the same task.** Three organisations exhibit this gap in three different shapes — he-2026-2x-mandate has outcome data (throughput, review load) but only thin authoring-cost data and no review-cost data; cloudflare-2026-ai-review has precise review-cost data and zero effectiveness data; uber-2026-claude-cost has cost and adoption data with an explicit, on-record COO admission that the ROI link "is not there yet." Three independent instances of the identical omission is itself the RQ4 finding, and it feeds directly into RQ6.

## 2. What we actually have, by cost category

| Category | Datapoints | Quality |
|---|---|---|
| **(a) Token/licence spend** | he-2026-2x-mandate: $42→$856/developer-month, ~20× over Jul 2025–Apr 2026 (Claude-only lower bound). Uber (press-disclosed): $150–250/mo average, $500–2,000/mo power-user tier, $1,500/mo/tool cap imposed afterward. Cloudflare: $0.98 median cost **per review run** (a different unit — event, not monthly rate). | he-2026 = Tier A telemetry, single firm, self-described "upper envelope." Uber = single paywalled press interview, no disclosed methodology, numeric drift already observed between outlets. Cloudflare = Tier C strong-end, genuinely instrumented, single org, one month of data. Böckeler's $380/day→$91,200/yr figure is **excluded**: it is one anonymous, unverified social-media anecdote arithmetically extrapolated by the speaker, not a population statistic — a hygiene exemplar of anecdote-to-soundbite inflation, not a datapoint. |
| **(b) Review/verification overhead** | METR: ~9% of developer time spent reviewing/cleaning AI output, <44% generation-acceptance rate. he-2026: per-reviewer load ~2×, total cycle time +22%, substantive human review roughly halved. Faros: review-time growth (median PR-review time +441.5%, direction only — magnitude confounded by organisational growth). | METR = Tier A, measured, but E3-boundary/pre-agentic scoping. he-2026 = Tier A, measured, single firm. Faros = Tier D, COI, direction-only. |
| **(c) Rework** | Stanford/Denisov-Blanch: gross gains 30–40% net down to 15–20% — roughly half eaten by rework; named 350-person case: PRs +14%, quality score −9%, rework 2.5×, effective output flat. | Talk-grade, Tier B, unpublished; concrete numbers but a single research programme. |
| **(d) Quality debt as deferred cost** | Tension-4 cross-ref: complexity/static-warning growth persists after velocity gains fade (Tier A, one lab); downstream agent-on-agent maintenance cost drops task-resolve rate up to 13.1pp, refactoring hit hardest (Tier A, independent, clean E3). | Real but the popular proxies (churn, duplication) don't predict the measured cost — a mechanism gap, not just a data gap. |
| **(e) Modelled/illustrative** | DORA's instability-tax formula and worked 39%-ROI/$8.37m-investment/500-person example. | Tier D, explicitly hypothetical inputs, "meant to spark a conversation... not a rigid mathematical formula." Usable only as a template for what an internal cost model could contain (headcount-reinvestment value, J-curve tuition cost, instability-tax line item) — never as an effect size. |

## 3. The cost-to-value ratio question

No source in this evidence base provides a defensible cost-to-value ratio for any task type — none pairs its own cost figure with its own outcome figure. The shape of the evidence *suggests* a favourable ratio for shallow, greenfield-adjacent use (where token/licence cost is low and verification burden is light) and a plausibly inverted ratio wherever verification dominates — Cloudflare's cheap-but-unvalidated review layer, he-2026's rising cycle time despite falling substantive review, and tension-6's "automation absorbs the queue, not clearly the function" finding all point the same way. This is stated here as a **hypothesis**, not a finding: it rests on triangulating across sources that never measured cost and value together, which is exactly the inferential step the evidence does not support doing rigorously.

## 4. Verdict on RQ4

Per the pre-registration, RQ4 closes at **insufficient evidence for a cost-to-value ratio**, with two qualifications that are themselves substantive: (i) the handful of real cost datapoints converge on a consistent *shape* — low baseline, heavy tail, fast growth — even though they never converge on a number; (ii) the systematic absence of paired cost-and-outcome measurement, observed independently at three organisations, is not a null result to shrug off but a finding in its own right, and it feeds directly into RQ6's instrumentation recommendations.

## 5. Claims, with confidence

1. Per-developer/per-org agentic-coding cost grows fast and is concentrated in a heavy-usage tail, in every source that measures it (he-2026, Uber). **Medium** — two organisations, different measurement bases, consistent shape only.
2. No source pairs cost data with outcome/effectiveness data for the same task. **High** — three independent organisations (he-2026, Cloudflare, Uber), each missing a different half of the pair, is a clean pattern.
3. Rework and review-verification overhead materially discount gross productivity gains wherever measured (Stanford: ~half; METR: ~9% of time; he-2026: cycle time +22%). **Medium** — concrete numbers, but each from a single research programme or firm.
4. Popular quality-debt proxies (churn, duplication) do not predict the real downstream maintenance cost of agent-authored code. **Medium** — one clean independent E3 study, cross-checked against tension-4.
5. Uncapped, incentive-driven usage (leaderboards, unlimited budgets) is a demonstrated failure mode that produces the cost blow-outs seen in the record. **Medium** — a single but well-corroborated named case (Uber), consistent with he-2026's own 20× ramp.

## What this means for us

Budget for a heavy tail, not an average: whatever baseline licence/token cost is assumed, expect a subset of users or teams to run several multiples above it, and expect that multiple to grow with adoption depth, not just headcount. A hard per-tool spending cap (Uber's response) is the only concretely evidenced control mechanism in this literature — plan for one before a leaderboard or unlimited-budget rollout creates the incentive problem Uber describes.

The sharper instrumentation implication: do not deploy a cost meter without an adjacent outcome meter measuring the same unit of work. Every cost figure in this evidence base that could have been paired with a productivity, quality, or review-load figure from the same system, wasn't. If we instrument AI spend internally, the design brief should specify from day one which outcome metric is tracked alongside every cost metric — token spend without a paired quality/throughput/review-time signal reproduces exactly the gap this research found in three separate companies, including one whose own COO has already said, on record, that the link "is not there yet."

## Addendum (spend hunt R2, 2026-07-06)

A dedicated three-channel search on per-engineer spend (sources/ai-spend-landscape-2026.md) materially enriched category (a) licence/token spend: the 2026 picture is a **seat-to-token regime change** (DX 2025: modal $101-500/dev/YEAR seat-era budgets; Gartner Jun 2026: modal $200-500/dev/MONTH token spend, 6% >$2,000/month; Anthropic telemetry: $150-250/dev/month enterprise average, with its own per-day estimate silently doubling in Apr 2026 at constant prices). The $500-2,000/month tail is corroborated in shape by Gartner's distribution and PragEng ground-truth anecdotes ($500/day exists; one startup grew 15x in six months) - but the most-circulated second org-level datapoint (Microsoft) is Uber's figure laundered by aggregators; the Microsoft cost-driven policy EVENT is real, its number is not (corruption instance #15). Two things did not change: no invoice-grade multi-org dataset exists, and not one new item pairs cost with outcomes - the RQ4 closure stands, now with a much better-characterised cost side.
