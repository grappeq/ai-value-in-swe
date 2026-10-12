# 01 — Verdicts on RQ1–RQ6

Conventions used throughout:
- **Tier (A–D) and era (E1/E2/E3)** follow PROTOCOL.md §2–3.
- **"Measured" and "self-reported"** are kept apart.
- **E1/E2 effect sizes** are labelled *pre-agentic* and are not carried over to E3.
- **One voice:** sources in the same independence group (see `05-independence-map.md`) are counted once.

---

## RQ1 — Value map: where does AI deliver measurable value?

**Verdict.**
- **Overall:** in E3, AI measurably raises *activity and throughput*: PRs, commits and lines.
  - The strongest case is one firm at 1.46–1.72× PRs per developer within-developer (he-2026-2x-mandate; A, E3).
  - Next is +21% merged PRs (microsoft-cli-agents-2026; B, E3).
  - Last is +36% commits in agent-first repositories (agents-vs-ides-2026; A, E3).
  - Measured *task-level* value in E3 is confined to newer code. The evidence does not establish value for most task types.
- **By task type:**

| Task type | Finding | Source tiers and eras |
|---|---|---|
| **T3** greenfield / new code | Supported | **E3:** he-2026-2x-mandate, +44% in post-2022 repositories (A, E3, measured). **E1, pre-agentic:** peng-2023-copilot-rct, 55.8% faster on a greenfield task (A, E1, vendor COI). |
| **T4** mature codebases | Contested; see `02-contradictions.md` C1 | **Against:** metr-2025-rct (A, E3), +19% slower; he-2026-2x-mandate, +12% n.s. in legacy repositories. **For:** rising PR and commit counts, as in the overall verdict. |
| **T5** refactoring | Migration speed is self-reported by a single organisation; measured quality is adverse | **Speed:** google-migrations-2025 (C). **Quality:** agent-maintainability-2026 (A, E3), refactoring resolve rate −8.2%; readability-agents-2026 (B, E3). |
| **T6** tests | Directional only | salesforce-2026-cursor-tests (C); uber-autocover-2026 (B/C, COI). Two independent organisations fall short of the three-source rule. |
| **T7** review | Faster cycle times, at the cost of human scrutiny | atlassian-2026-ai-review (B, COI); zhong-2026-agentic-review (B, E3). |
| **T8** debugging / root cause | No E3 field value measured | rca-failures-2026 (A, lab only): best accuracy 0.36. google-autodiagnose-2026 and zalando-2025-postmortems (C, E2). |
| **T1, T2, T9, T10, T11** | No measured value | Merge-rate proxies only, for T10 and T11: failed-agentic-prs-2026, task-stratified-agents-2026 (B; one AIDev voice). |

- **Satisfaction** is high but self-reported (dora-2025, stackoverflow-survey-2025; B).

**Confidence: medium.** Activity gains are measured at Tier A in E3 but come from one research lineage and one firm. Most task-type cells are empty, or rest on proxies that do not track delivered value.

---

## RQ2 — Measurement methods: how trustworthy, and how large is the self-report gap?

**Verdict.**
- **Self-report is not a valid substitute for measurement.**
  - The within-study gaps are large and do not share a direction:
    - about 40 pp of overestimation, with the sign inverted (metr-2025-rct; A, E3);
    - about 21 pp of underestimation (peng-2023-copilot-rct; A, E1, pre-agentic).
  - Individual calibration is close to zero:
    - stanford-denisov-blanch (B): about 30 percentile points of miscalibration;
    - stray-2026-nav (B, E1): ρ≈0.17, n.s.
  - The error varies in sign, so no correction factor rescues self-report.
  - Perception-only surveys report 75–90% positive (dora-2024, dora-2025, space-of-ai-2025). Perceived markers are more positive than objective ones: 71.1% against 54.5% (wittig-2026-fragmented-markers).
- **Measured telemetry is only as good as its proxy and its counterfactual.**
  - Placebo-tested quasi-experiments hold up: heilman-2026-microsoft (A, E1/E2); he-2026-2x-mandate (A, E3). Pre-trend checks also hold in he-2026-2x-mandate.
  - Raw LOC, commits, acceptance and merge rates do not hold up:
    - pooled outcomes give I²=99% (genai-productivity-meta-2026; A);
    - AIDev attribution has never been validated (aidev-dataset-2026).
- **RCTs are now fragile in practice.** In METR's own 2026 wave, 30–50% of developers refused the no-AI arm, and the authors call the estimates unreliable (metr-2026-design-change; B, E3).

**Confidence: medium.** That self-report is unreliable is supported with high consistency across independent Tier A/B sources. But only two clean within-subject paired deltas exist, from different eras and with opposite signs, so the *size and direction* of the gap cannot be stated in general.

---

## RQ3 — Failure map: where is AI useless or net-negative, and what predicts failure?

**Verdict.**
- **Net-negative or null results cluster in mature, familiar, large codebases (T4).**
  - metr-2025-rct (A, E3): +19% time.
  - he-2026-2x-mandate (A, E3): legacy repositories +12%, n.s.
  - stanford-denisov-blanch (B, pre-agentic): brownfield 0–10%, with gains falling as codebase size grows. Same voice as he-2026-2x-mandate.
- **Agent bug-fix and performance work** is merged least often: 55–64% against 84% for documentation (failed-agentic-prs-2026, task-stratified-agents-2026; B, E3, one AIDev voice). But only 35.7% of rejections are attributable to the agent (agentic-pr-merge-reject-2026; same voice).
- **Maintenance of agent-written code** fails more often: up to −13.1 pp (agent-maintainability-2026; A, E3).
- **Comprehension falls under delegation:**
  - impaired-programming-2026 (A, E3): d>0.8;
  - shen-2026-coding-skills (A-candidate, E2, Anthropic COI): d=0.74.
  - Both cover learners on short tasks only.
- **Predictors with support:**
  - codebase age and size, and developer familiarity (metr-2025-rct, he-2026-2x-mandate);
  - codebase cleanliness (stanford-denisov-blanch R²≈0.40; cursor-velocity-quality-2025: debt predicts later velocity loss);
  - large, diffuse changes and failing CI (failed-agentic-prs-2026);
  - low verification capacity, including unreliable agent self-reports: 22.6% of episodes contain inaccurate self-reports, and the agent self-corrects only 2.99% of the time (dev-agent-misalignment-2026; B, E3, independent).
- **T11 ops and infrastructure:** three independent Tier C organisations converge on the *existence* of destructive failures when agents have unguarded production access. Rates are unknown. Sources:
  - grigorev-2026-terraform-db;
  - replit-db-deletion-2025;
  - amazon-2026-outages (C, E3). Amazon disputes AI causation in Tier D statements.
- **No failure evidence at all:** T1, T2, T10.

**Confidence: medium.** Each failure zone rests on at least one Tier A/B E3 source. But the large-N E3 evidence is concentrated in two non-independent clusters (AIDev, CMU), and the outcomes are mostly proxies.

---

## RQ4 — Cost profile: is the cost-to-value ratio favourable or inverted?

**Verdict: insufficient evidence for a cost-to-value ratio for any task type.** As the protocol anticipated, this scarcity is the finding.
- **Cost data is sparse.** Only 76 of 569 rows carry substantive cost data, and many of those record its absence.
- **Spend figures:**
  - **Tier A/B:** only one source, a single firm. Claude-only spend rose from $42 to $856 per developer-month, about 20×, a lower bound against roughly 1.5–2× PRs (he-2026-2x-mandate; A, E3). The ratio is ours; the paper does not compute it.
  - **Tier C:** spend figures are weak and recycled through other outlets (uber-2026-claude-cost, ai-spend-landscape-2026).
  - **Tier D:** dora-2026-roi's ROI figures come from a hypothetical model.
  - **Excluded:** bain-2026-benchmark, judged a phantom citation.
- **Review overhead** is measured only as time or coverage, never in money:
  - review lead time +20% for AI PRs, with human review coverage falling from 89% to 68% (he-2026-2x-mandate; A, E3);
  - about 9% of task time spent reviewing AI output (metr-2025-rct; A).
- **Quality-debt costs** are measured as proxies, not money:
  - warnings and complexity rise in E3 (cursor-velocity-quality-2025, agents-vs-ides-2026; A, one voice);
  - rework is higher after agent PRs, OR 1.62 (who-finishes-the-job-2026; B, E3);
  - see contradiction C4 for the counter-evidence.
- **Long-run skill and comprehension costs** are evidenced only in short-horizon learner RCTs (impaired-programming-2026, shen-2026-coding-skills). Professional deskilling over time is unmeasured.

**Confidence: high.** The absence is established by a column-level count and confirmed by the records' own statements that dollar, review-hour and invoice-grade data are missing.

---

## RQ5 — Translation: does local speed-up reach (a) mature-codebase feature velocity and (b) production stability?

**Verdict (a): only partly, and heavily attenuated.**
- **Activity gains shrink at each step towards shipping** (demirer-2026-writing-vs-shipping; B, E3):

  | Measure | Change |
  |---|---|
  | Lines | +957% |
  | Commits | +153% |
  | PRs | +86% |
  | Releases | +19.8% |

- **Gains are smallest in legacy code:** +12% n.s., against +44% in newer repositories (he-2026-2x-mandate; A, E3).
- **The bottleneck moves to review.** The organisation's PR volume rose 3.1× against a reviewer pool that grew 1.5×. Each AI PR carries a +22% cycle-time premium. Substantive human review fell from about 39% to about 21% (he-2026-2x-mandate; A, E3). Vendor telemetry points the same way but is Tier D (faros-2026-whiplash, linearb-2026-benchmarks).
- **Delivery metrics are unmeasured for E3.** No Tier A/B E3 source measures deployment frequency, lead time, change failure rate or recovery time against a counterfactual.

**Confidence for (a): medium.** One Tier A firm study and one independent Tier B large-N panel agree on attenuation, but the firm is a self-described "upper envelope" and no E3 DORA-type measurement exists.

**Verdict (b): insufficient evidence, with an adverse lean from weaker sources.**
- **Adverse:**
  - instability associations, self-reported and pre-agentic (dora-2024, dora-2025; B);
  - incidents per PR +243% (faros-2026-whiplash; D);
  - a contested organisational account (amazon-2026-outages; C).
- **Favourable or null:**
  - AI PRs reverted 6.7 pp less (he-2026-2x-mandate; A, E3);
  - bug-fix share unchanged (demirer-2026-writing-vs-shipping; B).

**Confidence for (b): low.** The adverse signals are Tier D, pre-agentic self-report or a single contested case, and the one Tier A E3 stability proxy points the other way.

---

## RQ6 — Internal measurement: what should we instrument, and what should we avoid?

**Verdict.**
- **Do not use as success measures:**
  - activity volume: LOC, commits, raw PR counts;
  - self-reported time saved;
  - AI-share, acceptance and token metrics.

  Why:
  - activity gains shrink by an order of magnitude before delivery (demirer-2026-writing-vs-shipping);
  - self-report errs in both directions (metr-2025-rct, peng-2023-copilot-rct, stanford-denisov-blanch);
  - AI attribution is unvalidated and AI share does not track outcomes (aidev-dataset-2026, uber-2026-claude-cost, dx-reock-2026).
- **Instrument instead:**
  - **Counterfactual, delivery-weighted throughput, split by repository age.** The design follows he-2026-2x-mandate and heilman-2026-microsoft.
  - **Review flow and coverage.** Track pickup, lead time, unreviewed-merge share and reviewer load (he-2026-2x-mandate, unreviewed-ai-prs-2026).
  - **Stability and rework over 30–90 days, plus a periodic comprehension probe.**
    - Behavioural maintenance outcomes predict failure where static metrics do not (agent-maintainability-2026; A, E3).
    - Rework rises after agent PRs (who-finishes-the-job-2026).
    - Comprehension loss is measured (impaired-programming-2026).
- Details are in `04-gaps-and-metrics.md`.

**Confidence: medium.** The "avoid" list rests on several independent Tier A/B sources including E3. The "adopt" list rests mainly on a single-firm Tier A study and on design principles, not on validation of those metrics against business outcomes.
