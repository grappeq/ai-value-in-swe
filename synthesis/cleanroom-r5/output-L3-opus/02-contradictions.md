# 02 — The five strongest contradictions

Selection criteria: each contradiction has Tier A or B evidence on both sides, bears directly on RQ1, RQ2 or RQ5, and would change a recommendation depending on how it resolves. Sides are presented separately and never averaged. Independence groups (G-numbers) refer to `05-independence-map.md`.

---

## C1 — Do E3 tools speed up experienced developers in mature codebases (T4)?

**Side A: slowdown or null**

| Source | Tier / era | Basis | Finding |
|---|---|---|---|
| metr-2025-rct | A; E3 at the early-IDE-agent end (E2/E3 boundary) | Measured | Completion time +19% (S=0.188, 95% CI 0.013–0.395); +34% unadjusted. 16 developers with about 5 years each on their own ~1.1M-LOC repositories. The record rules out extrapolation to unfamiliar or greenfield code and to late-2025 agents. |
| he-2026-2x-mandate | A, E3 | Measured | Legacy (pre-2022) repositories +12%, not significant. Post-2022 repositories +44%. The difference is significant (p<0.01). |
| agents-vs-ides-2026 | A, E3 | Measured | Cohort with prior AI-IDE use: commits +3.06% (n.s.), reversing to about −35% by month 6. |
| stanford-denisov-blanch | B, mostly E1/E2 | Measured | Brownfield, high-complexity work +0–10%. Gains fall with codebase size. Pre-agentic. |
| genai-productivity-meta-2026 | A, mixed era | Measured | Open-source subgroup g=0.01 (p=0.975). It pools metr-2025-rct, so it is not independent. |
| metr-2026-uplift / metr-2026-design-change | C / B, E3 | — | −18% (CI −38 to +9) and −4% (CI −15 to +9). Both cross zero. The authors call the data "unreliable" because 30–50% of developers declined to do some tasks without AI. **Uninformative, not a slowdown.** |

**Side B: speed-up**

| Source | Tier / era | Basis | Finding |
|---|---|---|---|
| he-2026-2x-mandate | A, E3 | Measured | PRs per developer 1.46× (preferred specification), 1.72× (baseline), 1.99× by month 9; raw ratio 2.09×. One self-selected, young firm that the authors call an "upper envelope". |
| microsoft-cli-agents-2026 | B, E3 | Measured | Merged PRs +21.3% [19.6, 23.0] by synthetic control; Microsoft studying its own tools. |
| agents-vs-ides-2026 | A, E3 | Measured | Cohort with no prior AI use: commits +36.25%, lines +76.59%. |
| denisov-blanch-2026-ramp | B, E3 | Measured | Commits +28–38%. A re-analysis of the agents-vs-ides panel, so it is not new evidence. |
| heilman-2026-microsoft | A by design, **E1/E2** | Measured | PRs +40.5%. The record says it is "NOT an E3 comparator", so it is excluded from Side B under the era-transfer rule. |

**Independence.**
- Side A has one independent E3 task-time voice: METR (G4), whose follow-ups are not replications.
- Side B has two voices: the CMU/Stanford lineage (G3), which also supplies the Side A legacy-repository nulls, and Microsoft (G6).

**Reconciliation.**
- The two sides largely measure different constructs. Side A measures time per task. Side B measures PR and commit counts per period.
- he-2026-2x-mandate itself reports a +22% cycle-time premium per AI PR. stanford-denisov-blanch reports PRs +14% with "effective output" flat.
- Every measured subgroup restricted to legacy or mature code (METR, he-2026-2x-mandate legacy, agents-vs-ides cohort with prior AI use) is null or negative.
- No reliable late-E3 task-time study exists for experienced developers on mature code.

**Status: contested.** Measured throughput counts rise in E3, but the only clean task-time trial on familiar mature code shows an early-E3 slowdown, and its intended replication failed on design grounds.

---

## C2 — Are E3 throughput gains durable or transient?

**Side A: durable or growing**
- **he-2026-2x-mandate** (A, E3, measured).
  - Adoption jump +0.143 log; accumulating-use slope adds up to +0.45 log by April 2026.
  - 1.99× by month 9.
  - A fabricated "placebo" release moved the outcome as much as real releases did, so the model-vintage channel cannot be identified.
- **demirer-2026-writing-vs-shipping** (B, E3, measured).
  - Synchronous-agent commits grow over weeks 1–30: +81.3%, +98.5%, +153.2%.
  - The authors attribute the growth to model vintage, not learning.
  - Downstream measures are much smaller: releases only +19.8%.
- **microsoft-cli-agents-2026** (B, E3). +29.4% in February, +20.0% in March–April, with overlapping intervals. A 16-week window only.

**Side B: transient**
- **cursor-velocity-quality-2025** (A, E3 with a boundary caveat, measured).
  - Commits +55.4% in month 1, +14.5% in month 2, about 0 in months 3–6.
  - Pooled commits +2.63% (n.s.).
  - Complexity predicts lower future velocity (GMM −0.718).
- **agents-vs-ides-2026** (A, E3). Cohort with prior AI-IDE use reverses to about −35% commits by month 6. *However*, the agent-first cohort holds at +36%, so this source is split.
- **quispe-2026-claude-frontier** and **quispe-2026-agentic-delegation** (B, E3; one voice; Microsoft–GitHub-adjacent).
  - Commit effect at adoption, then months 1 and 2: +40.7, +24.0, +13.3.
  - The agentic-delegation estimate is flagged as "decaying".
- **demirer-2026-writing-vs-shipping**, asynchronous-agent arm. +138.5%, then +70.2%, then +60.7%. Decaying.

**Independence.**
- he-2026-2x-mandate, cursor-velocity and agents-vs-ides share authors (G3). Much of this contradiction is therefore a tension within one research lineage, despite the distinct datasets.
- demirer-2026-writing-vs-shipping (G5) and the quispe pair (G5-adjacent) are independent of G3, but each carries a Microsoft/GitHub link.

**Reconciliation.** None of these candidates has been tested directly:
- setting: a mandated, funded firm versus self-selected open-source repositories, where adoption may not mean continued use;
- prior AI exposure;
- model vintage;
- unit of measurement: repository-month commits versus developer-month PRs;
- feedback from accumulated debt.

**Status: contested.** Tier A/B measured evidence points both ways, and no study compares the plausible moderators directly.

---

## C3 — Does AI turn code review into a bottleneck and erode scrutiny, or does AI review make it faster without loss?

**Side A: bottleneck and erosion**
- **he-2026-2x-mandate** (A, E3, measured).
  - Each AI PR: review lead +20%, pickup +15%, total cycle +22%.
  - Organisation level: PR volume 3.1× against a reviewer pool of 1.5×; reviewer load about 2×.
  - Human review coverage fell from 89% to 68%; substantive human review from about 39% to about 21%.
- **review-agents-reality-2026** (B, E3, AIDev). PRs reviewed only by AI review agents merge at 45.20%, against 68.37% for human-only review. 60% of AI-reviewer comments are low-signal.
- **Vendor telemetry** (D, directional only, COI):
  - faros-2026-whiplash: time in review +441%; unreviewed merges +31%.
  - linearb-2026-benchmarks: P75 pickup 5.25× for agentic PRs.
- **xu-2025-maintenance-burden** (B, E1). Core contributors' reviews +6.1%. Mechanism only.

**Side B: faster without loss**
- **atlassian-2026-ai-review** (B, E3; 10 of 11 authors from Atlassian, evaluating their own tool).
  - Median PR cycle time −30.8%.
  - Human comments −35.6%.
- **zhong-2026-agentic-review** (B, E3, no control group). −2.5 to −4.5 days per KLOC in the agent era, but review smells rose.
- **unreviewed-ai-prs-2026** (B, E3, AIDev). AI PRs are reviewed *more* often than human PRs (71.1% against 65.5%), but human-only review is 8% against 25%.
- **duolingo-2026-risk-bot** (C, E3, one organisation). Time to merge fell from about 18h to about 12h. "No" change in defects, self-reported.
- **cloudflare-2026-ai-review** (C). Reports cost and latency only, with no outcomes, so it **cannot support Side B**.

**Independence.**
- review-agents-reality and unreviewed-ai-prs are one AIDev voice (G1).
- atlassian and the three Tier D sources carry vendor COI in opposite directions.
- Side B's Tier C evidence is a single source (duolingo), below the three-source threshold.

**Reconciliation.**
- The two sides measure different things:
  - Side A measures the latency of **AI-authored** PRs, which queue when volume outruns reviewers.
  - Side B measures the latency effect of **AI reviewers**, which drain the queue.
- Both can hold at once.
- On scrutiny, every source that measures substance agrees: human scrutiny falls (he-2026-2x-mandate, atlassian, zhong, unreviewed-ai-prs).

**Status: partly resolved.**
- The latency disagreement is a mismatch of constructs, and that part is **resolved**.
- Erosion of human scrutiny is consistent across sources, which is also **resolved** as to direction.
- Whether that erosion harms quality is **insufficient evidence**. Defect data is absent or self-reported, and he-2026-2x-mandate reports fewer reverts.

---

## C4 — Does AI-generated code accumulate quality debt?

**Side A: degrades**
- **cursor-velocity-quality-2025** (A, E3). Warnings +30.26% [17.3, 44.4]; cognitive complexity +41.64%; both persist for six months.
- **agents-vs-ides-2026** (A, E3). Warnings about +18%; complexity about +39%.
- **denisov-blanch-2026-ramp** (B, E3). Complexity +27–53%.
- **agent-maintainability-2026** (A, E3, independent). Follow-on task resolution is lower on agent-authored code, by up to −13.1 pp (refactoring −8.2% on average), in 12 of 16 cells.
- **who-finishes-the-job-2026** (B, E3, AIDev). Verified follow-up fix within 30 days: OR 1.62 [1.10, 2.39], i.e. 3.68% against 2.34%.
- **more-code-less-reuse-2026** (B, E3, AIDev). Semantic redundancy about 1.87×.
- **readability-agents-2026** (B, E3, AIDev). Maintainability Index −3.25.
- **gitclear-2025** (B, vendor, no AI attribution). 2-week churn 3.1% to 5.7% (2020–24); duplicated blocks +81%.
- **Tier D:** uplevel-2024 (bugs +41%, E1) and faros-2026-whiplash (incidents per PR +243%).

**Side B: null or improves**
- **churn-151-repos-2025** (A/B, E1/E2, independent). Uses GitClear's own 14-day churn definition.
  - File-based churn fell from 0.17 to 0.06.
  - About 80% of repositories show no discontinuity.
- **borg-2026-echoes** (A, E1/E2, CodeScene COI). No downstream maintainability difference.
- **arch-quality-agentic-2026** (B, E3, independent). Raw architectural smell count +1.1% (p=0.82).
- **mao-2026-code-metrics** (B, E2). AI code is less duplicated (14.3% against 27.6%) with fewer alerts, but shows more churn at 30–90 days.
- **cotroneo-2025-defects** (B, E2). AI code is simpler.
- **he-2026-2x-mandate** (A, E3). AI PRs are reverted 6.7 pp less.
- **demirer-2026-writing-vs-shipping** (B). Bug-fix share unchanged.
- **metr-2025-rct** (A). PR quality similar.

**Independence.**
- The E3 static-metric rises are one voice (G3).
- The AIDev findings are one voice (G1).
- agent-maintainability-2026 and arch-quality-agentic-2026 are independent of both and point in opposite directions, but on different constructs.

**Reconciliation.**
- **Churn sub-question.** Resolved against a general rise for E1/E2. The definition is the same, and the independent quasi-experiment finds no rise. GitClear has no AI attribution, and the record notes a 3–4× jump in its sample size coinciding with the rise.
- **Era.** Most nulls are E1/E2 and cannot rebut E3 findings.
- **Construct.** agent-maintainability-2026 shows that static-metric deltas do **not** predict downstream maintenance outcomes, while behavioural drift does (OR 1.83). The E3 static rises are therefore not yet shown to be debt.

**Status: contested.**
- The E1/E2 churn sub-claim is **resolved** toward "no general increase", at medium confidence.
- For E3, the measured outcome evidence (agent-maintainability-2026; who-finishes-the-job-2026) leans adverse but is modest.
- he-2026-2x-mandate's revert data runs the other way.

---

## C5 — Do developers overestimate AI's productivity effect?

**Side A: overestimate**
- **metr-2025-rct** (A, E3 boundary, independent).
  - Forecast −24% time; post-hoc belief −20%; measured +19%. A swing of about 40 pp.
  - Experts forecast a 38–39% speed-up.
- **stray-2026-nav** (B, E1, independent). No user reported a decrease, but several declined in measured activity. Perceived–measured correlation ρ≈0.17 (n.s.).
- **wittig-2026-fragmented-markers** (A for method, E1/E2). Perceived markers are 71.1% positive, against 54.5% for objective markers. Corpus-level, and it pools METR and Peng.

**Side B: underestimate or calibrated**
- **peng-2023-copilot-rct** (A, E1, vendor COI). Self-estimate about 35% against a measured 55.8% speed-up.
- **metr-2026-transcript-bound** (C, E3). Self-estimates fall below a *modelled* 1.5–13× ceiling. That ceiling is not a measured outcome.
- **impaired-programming-2026** (A, E3) and **shen-2026-coding-skills** (A-candidate, E2). Self-rated understanding moved in the same direction as measured comprehension. This concerns comprehension, not speed.
- **stanford-denisov-blanch** (B). Self-ratings miss by about 30 percentile points, with no fixed direction.

**Independence.**
- METR contributes to both sides (G4).
- Peng belongs to G5.
- Wittig is not independent of either side (G17).

**Reconciliation.**
- On productivity, the measured studies independent of vendors (METR, Stray) show self-report that is more positive than, or decoupled from, outcomes.
- The only measured underestimate (Peng) comes from E1, a vendor-affiliated team and a single greenfield task.
- The E3 "underestimate" compares self-reports with a model ceiling, not with a measurement.

**Status: contested as to direction; resolved as to reliability.**
- The direction of the error is contested.
- That self-report is unreliable for estimating AI's productivity effect is **resolved**: every paired source shows large error, in either direction.

---

### Considered but not ranked in the top five

**Seniority asymmetry.** Do juniors gain more?
- **Yes:** cui-2024-copilot-field and peng-2023-copilot-rct (A, E1; one G5 voice; heterogeneity not statistically significant).
- **No (flat, or seniors not lower):**
  - he-2026-2x-mandate (A, E3): flat.
  - google-rct-2024 (A, E1/E2): interaction p=.706.
- **C-shaped:** microsoft-cli-agents-2026 (B, E3): reported in narrative only.

No source reports a statistically significant seniority interaction on measured output. **Status: insufficient evidence.** It was left out of the top five because neither side has a significant estimate.

**Org-level delivery stability.**
- **Adverse:** dora-2024 (B, self-reported, E1/E2), stability −7.2% per 25% adoption; faros-2026-whiplash (D), lead time +480%.
- **Favourable:** he-2026-2x-mandate, fewer reverts.

**Status: insufficient evidence.** There is no Tier A/B E3 measurement of delivery stability. See RQ5 in `01-rq-verdicts.md`.
