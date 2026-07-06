# RQ1 — The Value Map

**Question:** Where across the SDLC does AI deliver measurable value, by task type, and on which metrics?

## 1. Headline answer

The measured E3 picture is real but narrow, and it does not travel intact from individual to system. The strongest causal estimate in this base is he-2026-2x-mandate's within-developer gain at one self-selected, best-case firm: 1.46–1.72x, rising toward 1.99x by month nine — the authors themselves call it an "upper envelope," not an industry average. Cross-company telemetry shows a far smaller population effect: dx-reock-2026's +7.76% PR throughput against +65% AI-usage growth across ~400 companies, consistent with dilution by non-adopters and legacy-bound work, not a contradiction of he-2026. Pre-agentic RCTs supply the sweet-spot baseline the exec narrative usually quotes: peng-2023-copilot-rct's 55.8% (greenfield toy task, CI [21%,89%]) and cui-2024-copilot-field's pooled 26.08% (three brownfield enterprises). And one Tier A E3-boundary source measured the opposite sign: metr-2025-rct found experienced OSS maintainers 19% *slower* with early agentic tools on their own large, mature repos, while believing themselves 20% faster. These are four populations and eras answering different questions, not one contradiction to resolve. Summary: AI delivers real, sometimes large, individual speedup that shrinks as context and review load grow; system-level throughput moves by single digits even where usage grows by dozens.

## 2. The map by task type

| Task type | Evidence density | Best effect estimate (tier / era / source_id) | Direction |
|---|---|---|---|
| T1 Requirements/specs | None — task-share only | Anthropic Economic Index usage-share, no effect size (D, mixed) | n/a |
| T2 System design/architecture | None — task-share only | No dedicated effect-size source | n/a |
| T3 Greenfield/prototyping | Rich | +55.8% completion time, CI [21%,89%] (A, E1, peng-2023-copilot-rct); Stanford greenfield-low-complexity +30–40% (B, E1/E2, stanford-denisov-blanch) | Positive, largest of any task type |
| T4 Brownfield feature dev | Rich | he-2026 within-developer causal 1.46–1.72x (A, E3) vs metr-2025-rct −19% (A, E3-boundary) on mature familiar repos; cui-2024 pooled +26.08% PRs (A, E1); google-rct-2024 +21–26%, non-robustly sig. (A, E1/E2) | Contested — positive on average, negative in the highest-familiarity slice |
| T5 Refactoring/tech debt | Mixed, thin | task-stratified-agents-2026: chore-type acceptance 84.0% vs feat 66.1% (B, E3, acceptance≠quality); Stanford cleanliness R²≈0.40 (B, E3). Salesforce "26→4 eng-days/repo" figure is a queued, unextracted lead only | Positive lead, evidentially thin |
| T6 Test authoring/maintenance | Thin | No dedicated source; folds into T5/T8 aggregates only | n/a |
| T7 Code review | Rich as AI *target*; effectiveness contested | Cost: median $0.98/run, 3m39s latency (C strong, E3, cloudflare-2026-ai-review) — zero effectiveness data. Outcome: CRA-only PRs merge 45.20% vs 68.37% human-only (B, E3, review-agents-reality-2026); he-2026: substantive review halved | Cost positive (cheap, fast); effectiveness negative where measured |
| T8 Debugging/incident response | Emerging | Zalando: analysis days/weeks→hours (C, E2 pipeline); ~10% misattribution persists; one agentic attempt abandoned (E3 negative). task-stratified-agents-2026: Devin weaker on fix tasks (45.6% vs Codex 83.0%) | Positive for augmented RCA; unresolved for autonomous |
| T9 Internal tooling/automation | None — task-share only | No dedicated effect-size source | n/a |
| T10 Documentation/knowledge | None — task-share only | task-stratified: docs 82.1% vs feat 66.1% acceptance (B, E3) — acceptance, not value | n/a |
| T11 Ops/infra/CI | None — task-share only | No dedicated effect-size source | n/a |

This table is the deliverable: task types not listed with a real effect size have **no measured value claim** in this evidence base, only usage-share survey data (Anthropic Economic Index, Stack Overflow) that says people *use* AI on these tasks, not that it *helps*.

## 3. Moderators that matter more than task type

- **Codebase context/maturity.** Tension-2 verdict (medium, direction only): Peng vs. METR, Stanford's quadrant, and he-2026's repo-age split (+44% post-2022 repos vs +12% n.s. pre-2022 legacy, same firm) all point the same way — nothing shows brownfield beating greenfield. But Stanford and he-2026 share an author, "brownfield" is operationalised four incompatible ways, and google-rct-2024 shows a real brownfield task with a fragile positive result. Direction solid; magnitude/mechanism not.
- **Accumulating use, not one-off adoption.** he-2026's decomposition: the adoption jump contributes +0.14 log points, accumulating-use +0.45 (the larger share), rising to ~1.99x by month 9; the mandate itself contributed ~zero once adoption/use are controlled for (θ≈−0.05, n.s.). Gains build with tenure on the tool, not the policy that introduced it.
- **Prior tool exposure, not codebase age per se.** agents-vs-ides-2026's IF-cohort reversal: repos with prior AI-IDE history bump +16–28% commits (months 0–2) then reverse to −35%/−61% LOC by month 6; agent-first repos hold flat-to-positive. Some "brownfield penalty" elsewhere may really be tool-novelty re-adaptation cost.
- **Usage depth vs. mere access.** Stanford's maturity ladder (identical tooling/spend, one BU ~40% AI-driven vs the other far behind) and heilman-2026-microsoft's dose-response (+21% Low → +40.5% High, [37.4%,43.5%] CI — **E1/E2, pre-agentic**) show usage depth predicts outcomes far better than seat access — consistent with dx-reock-2026's wedge (+65% usage vs +7.76% throughput; Tier D, direction only).

## 4. Claims list with confidence levels

1. **Individual gains under favourable conditions can approach 1.5–2x, accumulating over ~9 months.** he-2026-2x-mandate (A, E3). **Medium** — rigorous DiD/placebos, but one self-selected firm, no replication, self-disclaimed upper envelope.
2. **Cross-company average agentic-era gain is far smaller — roughly +7–8%, not 1.5–2x.** dx-reock-2026 (D), cross-checked against Faros (~+16.2%). **Low** — Tier D, undisclosed methodology/sample; consistent with dilution, not itself rigorous.
3. **Value concentrates in greenfield/newer code and shrinks, without reliably hitting zero, as context grows.** peng-2023-copilot-rct, stanford-denisov-blanch, he-2026-2x-mandate, metr-2025-rct, google-rct-2024 (A/B, E1–E3). **Medium** — direction robust across four designs/both eras; magnitude isn't, as the sharpest quantifications share an author.
4. **On mature, familiar codebases, agentic tooling can make experienced developers measurably slower while they believe themselves faster.** metr-2025-rct (A, E3-boundary). **High** — genuine RCT, task-level randomisation, 21-factor robustness check; one population, no matched greenfield arm.
5. **Review is AI's clearest target and cheapest to automate — effectiveness is contested wherever measured.** cloudflare-2026-ai-review (cost, zero effectiveness data), review-agents-reality-2026 (CRA-only merge 45.20% vs 68.37% human-only), he-2026 (substantive review halved). **Medium-high** on low cost; **low** on effectiveness — different orgs, never jointly measured.
6. **Debugging value is emerging via augmented, human-curated pipelines, not yet autonomous agentic RCA.** zalando-2025-postmortems (days→hours; ~10% misattribution persists; agentic attempt abandoned), task-stratified-agents-2026 (Devin weaker on fix tasks). **Low** — single-org account plus one proxy metric; thin, as anticipated.
7. **Usage depth and familiarity predict outcomes better than access, seats, or task type.** he-2026, heilman-2026-microsoft, stanford-denisov-blanch. **Medium** — under the one-voice rule this is two independent voices, not three (he-2026 and Stanford share an author), and the second voice (Heilman) is pre-agentic E1/E2 with an undisclosed all-Microsoft COI and no never-adopter control; Stanford's case is illustrative only.
8. **T1, T2, T9 carry no measured value claim — only usage-share survey data** *(narrowed from five task types in re-derivation R1: T11 now has direct thin evidence — ai-build-code-2026, B weak-end, AIDev cluster — and T10 has thin evidence via comment/readability quality studies)*. The T1/T2/T9 absence is now confirmed by targeted hunting (documented dry holes), which strengthens it. Verified against 202 evidence-table rows/50 sources. **High** on the absence itself; not a claim AI fails there, only unmeasured.

## 5. What this means for us

Push adoption hardest on **T3 (greenfield/prototyping)** and on accumulating use generally — expect gains that build over months, not at rollout, biggest where code is newest and smallest. **T4 (brownfield)** is not a blanket win: expect a split outcome, net positive on average but plausibly negative on the highly familiar, mature, high-review-bar slice — much of our production estate. Don't sell T4 gains uniformly.

Deprioritise chasing a system-level number to match pilot results: he-2026's 1.5–2x is a best-case ceiling, not a forecast; dx-reock's +7.76% is the more honest baseline. Treat **T7 (review)** as a cost play, not yet a bottleneck-relief play — automation is cheap, but cost and catch-rate have never been jointly measured, and the one outcome study available is unflattering. **T8 (debugging)** merits a bounded pilot in augmented, human-curated form, not an autonomous one — the sole autonomous RCA attempt found here was abandoned as infeasible. For **T1, T2, T5, T6, T9, T10, T11**, say so explicitly: no credible evidence AI helps or hurts yet, so any internal claim there is a hypothesis, not a result, until we generate our own data.
