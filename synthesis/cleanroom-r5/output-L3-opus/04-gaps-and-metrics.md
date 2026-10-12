# 04 — Evidence gaps and metrics

## Part 1 — The three task types with the least evidence

**How we counted.** We extracted explicit T-codes from column 7 of `evidence/evidence-table.tsv`, counting each row once per code it carries. Range phrases such as "T1–T11" were excluded because they mean "not assignable". 158 of 569 rows carry no T-code. A row is "focused" if it carries three codes or fewer; this guards against broad multi-tagging inflating a count.

| Type | Rows | Tier A/B rows | E3 rows | Distinct sources | A/B sources | Tier A sources | Focused rows / sources / A/B sources |
|---|---|---|---|---|---|---|---|
| T1 Requirements | 7 | 2 | 6 | 6 | 2 | 1 | 4 / 3 / **0** |
| T2 Design/architecture | 15 | 2 | 7 | 7 | 2 | 1 | 12 / 5 / **1** |
| T3 Greenfield | 72 | 46 | 43 | 25 | 16 | 7 | 39 / 17 / 11 |
| T4 Mature-codebase features | 197 | 136 | 134 | 49 | 32 | 14 | 167 / 42 / 27 |
| T5 Refactoring | 91 | 69 | 72 | 27 | 17 | 6 | 58 / 20 / 14 |
| T6 Tests | 51 | 27 | 39 | 16 | 8 | 1 | 22 / 8 / 2 |
| T7 Code review | 83 | 46 | 70 | 30 | 14 | 2 | 64 / 26 / 11 |
| T8 Debugging/incidents | 101 | 48 | 80 | 28 | 12 | 4 | 70 / 21 / 8 |
| T9 Internal tooling | 39 | 27 | 27 | 13 | 6 | 3 | 18 / 7 / 2 |
| T10 Documentation | 31 | 21 | 21 | 10 | 7 | 1 | 3 / 3 / 3 |
| T11 Ops/infra/CI | 57 | 20 | 40 | 17 | 7 | 2 | 40 / 12 / 4 |

The three thinnest task types are T1, T2 and T10. T9 and T6 are close behind: each has only two focused Tier A/B sources. That matters because protocol RQ5 lists internal tooling (T9) as a "demonstrated" win, yet this evidence base contains no outcome study of T9.

### T1 — Requirements, specs, user stories
- **No source measures an outcome.**
- **Usage only:** 49% of AI users apply AI to "analysing requirements" (dora-2025; B, mostly E1/E2, self-reported).
- **Mechanism hypotheses, single organisations:**
  - Vague specifications produced "unusable outputs" (one-developer-squad-2026; C, E3, n=1).
  - The constraint moves to specification (agoda-2026-bottleneck; C, narrative, no numbers).
- **Perception only:** stackoverflow-survey-2026 (C); dx-reock-2026 (D).
- **Verdict:** insufficient evidence. The value or harm of AI in specification work is unknown.

### T2 — System design and architecture
- **Only outcome study:** arch-quality-agentic-2026 (B, E3, measured).
  - Architectural-smell density fell 6.7% (p=0.004).
  - The raw smell count was unchanged (+1.1%, p=0.82) while code size grew 12.8%, so the density fall is largely a denominator effect.
- **Descriptive only:** llm-software-design-2026 (C, E2) states that no outcome was measured. Architecture conversations needed the most rounds (median 11).
- **Practitioner positions, no outcomes:** dont-vibe-control-2026 (C, E3) reports practitioners keeping design in human hands.
- **Self-reported usefulness:** 59.1% find AI useful for architecture, the lowest of the code-adjacent stages (stackoverflow-survey-2026, C).
- **Verdict:** insufficient evidence on value; one Tier B null on raw architectural quality.

### T10 — Documentation and knowledge
- **Row count is inflated.** Broad multi-tagging is responsible, for example failed-agentic-prs-2026 and enterprise-ai-assistants-2026; only 3 rows are focused.
- **Acceptance proxies, AIDev data (one voice):** documentation PRs are merged 84% of the time (failed-agentic-prs-2026; B, E3) and accepted 82.1% of the time (task-stratified-agents-2026; B, E3).
- **Quality measure, negative:** the documentation subset of agent "readability" commits worsened the maintainability index (readability-agents-2026; B, E3; also AIDev).
- **Self-reported quality:** documentation quality +7.5% per 25% increase in adoption (dora-2024; B, E1/E2, self-reported).
- **Verdict:** nothing measures documentation quality or time saved. Merge rate is the only signal, and agentic-pr-merge-reject-2026 shows that merge outcomes mostly reflect coordination, not code.

## Part 2 — Three metrics we would refuse

1. **Lines of code, commits or raw PR counts as a success measure (activity volume).**
   - **Attenuation from activity to delivery.** In demirer-2026-writing-vs-shipping (B, E3, measured), activity rose sharply while releases barely moved:

     | Measure | Change |
     |---|---|
     | Lines | +957% |
     | Commits | +153% |
     | PRs | +86% |
     | Releases | +19.8% |

   - **Gains decay while quality worsens.** cursor-velocity-quality-2025 and agents-vs-ides-2026 (A, E3; one voice, G3) show:
     - commit gains fading to roughly zero within 3–6 months;
     - static-analysis warnings up about 18–30%;
     - complexity up about 39–42%.
   - **Activity does not track how productive developers feel.** stray-2026-nav (B, E1) found commit and LOC changes uncorrelated with self-reported productivity.
   - **Outcomes pool badly.** Commit, LOC and time outcomes in genai-productivity-meta-2026 (A) pool with I²=99%; the measures are not interchangeable.
   - **Under a mandate, volume metrics invite gaming.** This is a hypothesis drawn from the gameability flags in the quispe-2026-claude-frontier and dx-reock-2026 records.

2. **Self-reported time saved or perceived productivity, used as impact evidence.**
   - **Perceived speed-up, measured slowdown.** In metr-2025-rct (A, E3), developers believed they were 20–24% faster but were measured 19% slower.
   - **Underestimation in E1.** In peng-2023-copilot-rct (A, E1), self-estimates were about 35% against a measured 55.8%.
   - **Poor calibration with no fixed sign.** Self-ratings miss by about 30 percentile points on average (stanford-denisov-blanch, B).
   - **A correction factor cannot fix it.** Because the error varies in both size and sign, no adjustment makes it usable.
   - **Perception-only surveys skew positive.** They report 75–90% positive results (dora-2024, dora-2025, space-of-ai-2025). Perceived markers are more often positive than objective ones: 71.1% against 54.5% (wittig-2026-fragmented-markers, A-for-method).

3. **AI-authored code share, usage/adoption share, suggestion-acceptance rate or token spend, used as value measures.**
   - **Attribution is unvalidated.** The AIDev heuristic has no precision/recall validation (aidev-dataset-2026), and attribution misses undisclosed use (mao-2026-code-metrics, B).
   - **High AI share has no visible link to outcomes.**
     - At Uber, 65–72% of code is AI-generated, yet leadership says it is "very hard to draw a line" to outcomes (uber-2026-claude-cost, C).
     - Usage rose 65% while PR throughput rose 7.76% (dx-reock-2026, D).
     - Organisations with more AI PRs "rarely outperform" others (linearb-2026-benchmarks, D).
     - The opsera-2026-benchmark vendor itself says acceptance does not predict success (D).
   - **Spend rises far faster than output.** At one firm, spend rose about 20× ($42→$856 per developer-month) against roughly 2× PRs (he-2026-2x-mandate, A, E3).
   - **Usage share describes interaction style, not value** (anthropic-economic-index, D).
   - **These remain legitimate inputs.** We would track them as cost and adoption *inputs*, never as outcomes.

## Part 3 — Three metrics we would adopt

1. **Counterfactual, delivery-weighted throughput.**
   - **What:** a within-team staggered-adoption or difference-in-differences design with a non-adopter or not-yet-adopted comparison group. Measure merged PRs **and** releases or shipped changes, split by repository age.
   - **Why:**
     - The only E3 effects that survive placebo or pre-trend checks come from such designs (he-2026-2x-mandate, A, E3).
     - heilman-2026-microsoft (A, E1/E2) shows the same with a flat placebo gradient.
     - demirer-2026-writing-vs-shipping (B, E3) shows that the delivery end of the chain moves far less than the activity end.
     - he-2026-2x-mandate found gains of +44% in new repositories against +12% (not significant) in legacy ones, so pooled figures would hide the difference that matters most for T4.

2. **Review flow and review coverage.**
   - **What:** pickup time, review lead time, total cycle time, the share of PRs merged without substantive human review, and reviewer load.
   - **Why:**
     - The bottleneck moves to review (he-2026-2x-mandate, A, E3). Review lead time for AI PRs rose 20%. Human review coverage fell from 89% to 68%, and reviewer load doubled.
     - The direction is corroborated by vendor telemetry (faros-2026-whiplash, linearb-2026-benchmarks; D, directional only).
     - Coverage and substantiveness diverge (unreviewed-ai-prs-2026, B; atlassian-2026-ai-review, B). Counting reviews alone is therefore insufficient.

3. **Stability and rework over a 30–90-day horizon, plus a periodic comprehension check.**
   - **What:** change failure rate, revert rate, follow-up fixes to merged changes, and maintenance-task success on AI-touched code. A light comprehension probe for developers working on delegated code.
   - **Why:**
     - Static-analysis proxies do not predict maintenance failure, whereas behavioural measures do (agent-maintainability-2026, A, E3).
     - Follow-up fixes are more frequent after agent PRs: OR 1.62 (who-finishes-the-job-2026, B, E3).
     - Revert rates moved the other way at one firm (he-2026-2x-mandate). The metric is contested, so it needs to be measured locally rather than assumed.
     - Comprehension falls under delegation, with d>0.8 and d=0.74 in two independent RCTs (impaired-programming-2026, A, E3; shen-2026-coding-skills, A-candidate, E2). Neither result would appear in throughput metrics.
