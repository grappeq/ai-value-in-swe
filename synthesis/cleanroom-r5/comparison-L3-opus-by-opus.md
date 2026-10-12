# Clean-room R5 comparison — L3-opus run, refereed by Opus

**Referee:** a fresh Claude Opus 5.5 agent (2026-10-12). I wrote neither side. Side B was written by a model of my own family; I was told this and tried to correct for it. Where Side B's claims go further than the evidence, I say so.
**Rubric:** `synthesis/cleanroom-r5/protocol.md` § "Comparison rubric (pre-registered)", followed as written.
**Side A (programme):** `outputs/exec-brief.md`, `synthesis/contradictions.md` (verdict index + R4 addendum), `synthesis/tension-verdicts/tension-1…7`, `synthesis/rq1…rq6`, `outputs/follow-up-questions.md`, `outputs/independence-crisis.md`, `synthesis/cycles/rederivation-r4.md` §E, `outputs/internal-measurement-proposal.md`.
**Side B (clean room):** `synthesis/cleanroom-r5/output-L3-opus/01…06`, all read in full.
**Checks:** figures were checked against `evidence/evidence-table.tsv` and, where a row was ambiguous, against `sources/*.md`. No web access was used and no git commands were run.

**Scoring conventions:**
- RQ5 is scored as two rows, (a) and (b), because both sides give separate verdicts with different confidences.
- The provenance clusters are scored one row each.
- 24 rows in total.

---

## 1. Scorecard

| # | Target | Side A position (confidence) | Side B position (confidence; file) | Score | Note |
|---|---|---|---|---|---|
| 1 | §5 T1 Perception–reality gap → B **C5** | Direction of the gap not replicated. The operative claim, that self-report magnitude is uninformative about measured change, is resolved on four paired designs. High on the operative claim, low on direction generality. | "Contested as to direction; resolved as to reliability"; brief claim 4 high (02 C5; 03 #4). | **Same direction & confidence** | Same four legs (metr-2025-rct, peng-2023-copilot-rct, stanford-denisov-blanch, stray-2026-nav), same both-signs reconciliation. B rejects metr-2026-transcript-bound as a model ceiling rather than a measurement. A also notes the baseline differs in kind. |
| 2 | §5 T2 Greenfield vs brownfield → B **C1** + brief #2 | Contested on magnitude and mechanism; direction unanimous. Medium. | Gains sit in newer code and are null or negative in mature code; medium (03 #2). C1, "do E3 tools speed up experienced devs on mature code?", is contested (02 C1). | **Same direction & confidence** | Same anchors (he-2026 +44% vs +12% n.s.; metr-2025 −19%). B's C1 status asks a different question (net T4 speed-up) and does not disagree. B's error: its list of "mature-code" subgroups includes the agents-vs-ides-2026 prior-AI-IDE cohort. That cohort is defined by tool exposure, not maturity, which A flags explicitly. B also misses google-rct-2024's brownfield positive, which A uses to bound the claim. |
| 3 | §5 T3 Throughput vs stability → B "considered, not ranked: org-level delivery stability" + RQ5(b) | Contested. Medium. The stability cost persists in direction across instruments but is unmeasured. DORA's throughput flip sits inside a redefined self-report instrument. The J-curve has no support. | Insufficient evidence with an adverse lean. Low (01 RQ5b; 02 "considered"). | **Same direction, different confidence** | Both read he-2026's revert data as the one Tier A E3 counter-signal. B leaves out the DORA 2024→2025 flip and the construct-redefinition analysis altogether (see §3, A6). B's "low" weighs the adverse signals as D or pre-agentic self-report, which is defensible. |
| 4 | §5 T4 Quality debt → B **C4** + brief #5 | Contested but substantiated. Medium. Two independent Tier A legs (CMU complexity; agent-maintainability-2026). Duplication leg contradicted. Churn leans null pre-agentically. Defect rate insufficient. Detectability leg added. | Contested. Medium on maintenance cost, low on defects. Churn sub-claim resolved towards "no general rise" for E1/E2. Static deltas not shown to be debt (02 C4; 03 #5). | **Same direction & confidence** | Same two independent legs and same churn adjudication. The sub-legs differ: B does not reach "duplication contradicted" (§3, A3) or the detectability leg (§3, A5). |
| 5 | §5 T5 Seniority → B "considered, not ranked" | Insufficient evidence for E3. The two E3 datapoints disagree on shape. Secondary finding (high): the E1 "juniors gain most" claim overstates its own statistics. | Insufficient evidence. No source reports a significant seniority interaction in any era (02 "considered"; 03 "cannot say"). | **Same direction & confidence** | B reaches A's secondary finding unprompted ("heterogeneity not statistically significant" for cui/peng; google-rct p=.706). |
| 6 | §5 T6 Bottleneck displacement → B **C3** + brief #3 | Confirmed in direction, raised to **high** in R4. Magnitude low-medium. Automation absorbs the queue, not the function. | Bottleneck and thinning scrutiny; medium (03 #3). Latency conflict resolved as a construct mismatch. Scrutiny erosion resolved as to direction. Harm to quality: insufficient evidence (02 C3). | **Same direction, different confidence** | A's R4 upgrade to high leans on demirer-2026, which measures no review time, plus Tier C narratives and Tier D telemetry. B does not let Tier C/D carry weight. See §5 for whether A's "high" is earned. |
| 7 | §5 T7 Bad-metric traps → B RQ6 "avoid" + 04 Part 2 | Resolved. High. Seven-row anti-metric table; no source defends any of them. | Refuses activity volume, self-reported time saved, and AI-share/acceptance/token metrics as value measures. RQ6 overall medium; the "avoid" list "rests on several independent Tier A/B sources" (01 RQ6; 04). | **Same direction, different confidence** | Substantively identical lists. B's medium is driven by its adopt list; it never grades the avoid list separately. B never frames this as a contradiction, which is correct: no source defends these metrics. |
| 8 | RQ1 value map | Real but narrow. 1.46–1.72× at one upper-envelope firm. Value concentrates in newer code. T1/T2/T9 carry no measured value (high on the absence). Medium. | E3 raises activity/throughput (he-2026, microsoft-cli, agents-vs-ides). Task-level value confined to newer code; most task types unestablished. Medium (01 RQ1). | **Same direction & confidence** | B cites microsoft-cli-agents-2026 as "+21.3% … by synthetic control". That is the IC4 dose-response reference-group figure; the synthetic-control headline in the record is +24.0% [14.5, 33.7] (§6). |
| 9 | RQ2 measurement methods | Self-report magnitude uninformative: high. Rigorous causal E3 evidence extremely thin: high. Vendor telemetry gives direction only: medium. | Self-report is no substitute; telemetry is only as good as its proxy and counterfactual; RCTs fragile in practice. Medium overall, with high consistency on self-report (01 RQ2). | **Same direction, different confidence** | Same content. B lowers the headline to medium because only two clean paired deltas exist and they have opposite signs. On the operative claim, B's brief (#4) matches A at high. |
| 10 | RQ3 failure map | Failure is predictable. Gains shrink with familiarity, size, complexity and implicit context: high on direction, low on magnitude. Review capacity: medium-high. Skill formation: E2 medium-high. | Null or negative results cluster in mature T4. Predictors supported. T11 destructive failures exist. Comprehension falls. Medium (01 RQ3). | **Same direction, different confidence** | B adds a T11 incident cluster and agent self-report unreliability (§2, B6 and B7). A adds rare languages (§3, A10). |
| 11 | RQ4 cost profile | Insufficient evidence for a ratio (pre-registered). Cost and outcome never paired: high. Cost shape is a low baseline with a heavy tail: medium. | Insufficient evidence for any task type; high (absence shown by column count). Spend 20× vs PRs 1.5–2× at one firm, flagged as B's own juxtaposition (01 RQ4). | **Same direction & confidence** | B's juxtaposition cuts against A's exec-brief wording that publishers of cost publish "nothing" about returns (§2, B4). |
| 12 | RQ5(a) translation to mature-codebase velocity | Partial and much smaller than individual numbers. Medium on direction, low on number. | Only partly; heavily attenuated (demirer chain; he-2026 legacy split; review bottleneck). Medium (01 RQ5a). | **Same direction & confidence** | Same attenuation chain and the same "upper envelope" caveat. |
| 13 | RQ5(b) translation to production stability | Directionally present; magnitude and defect translation unmeasured. Medium. | Insufficient evidence with an adverse lean from weaker sources. Low (01 RQ5b). | **Same direction, different confidence** | A's own tension-3 memo concedes the only measured E3 stability proxy (he-2026 reverts) is reassuring. B's "low" is arguably the more literal reading of A's own evidence. |
| 14 | RQ6 internal measurement | Adopt controlled throughput, review absorption, stability pair, rework, spend-plus-outcome, people track. Reject nine. Mostly medium to high. | Adopt counterfactual delivery-weighted throughput, review flow/coverage, stability and rework plus a comprehension probe. Reject three families. Medium (01 RQ6; 04). | **Same direction & confidence** | See row 24. |
| 15 | Scarcity headline ("nobody has properly measured today's AI agents yet") | Only three RCTs on working developers, none on a mature present-day agent. The −19% is out of date. Two reviews found the same hole. A, high. | No reliable late-E3 task-time study and no counterfactual DORA-type E3 measurement exist (03 "cannot say"). But B's **first** claim is that agentic tools *raise measured output* (Tier A+B, medium, 03 #1). Scarcity is B's headline only for cost (RQ4). | **Same direction, different confidence** | Both agree the decisive E3 measurement is missing. B grants the quasi-experimental E3 work (he-2026 DiD with placebos; demirer 500k panel) standing as measurement. Under B's reading the headline's wording does not hold. Framing-dependent (§3, A8). |
| 16 | "Sure" #1: don't trust developers' self-reports | Four paired studies; 20–40 points off in both directions. A/B, high. | Brief #4: "estimates cannot be used to judge AI's value". High (03 #4; 04 refuse #2). | **Same direction & confidence** | — |
| 17 | "Sure" #2: numbers get mangled in transit (25 cases) | Twenty-five documented corruptions (phantom Bain report, Atlassian 45% vs 30.8%, LinearB 4.6×, Opsera 5×, Uber→Microsoft). High. | Not stated as a finding. B excludes bain-2026-benchmark, refuses the 4.6× figure and notes the Uber laundering, but only as source hygiene (05). | **Absent** | Triage in §4, A1. |
| 18 | "Sure" #3: spending without checking returns; spending changed shape | Seat-to-token regime change ($100–500/yr → $200–500/month; Gartner) [D spread]. Consumption grows at flat prices. Every publishing organisation publishes nothing about what the money bought. C, high on the pattern. | Cost-to-value cannot be computed; high that the evidence is absent. Tier C spend figures are "weak and recycled"; Tier D ROI hypothetical (03 #8; 01 RQ4). No regime-change claim. | **Same direction, different confidence** | Same on the absence of paired cost and value. B does not reach the "changed shape" half and actively downgrades the spend sources (§3, A2). B's he-2026 juxtaposition contradicts "nothing" (§2, B4). |
| 19 | Dry task types (Q5) | T1 requirements and T9 internal tooling: confirmed dry. T2 architecture: usage and perception only. T8: no measured agentic-era effect. | T1, T2 and T10 are the three thinnest by focused A/B-source count. T9 and T6 "close behind". T9 has "no outcome study" (04 Part 1). | **Same direction & confidence** | Both find no outcome evidence for T1, T2 and T9. Membership of the "three" differs only on T10 vs T9, which is a counting-method difference (§2, B5). |
| 20 | Provenance: Stanford–CMU | One provenance: he-2026, agents-vs-ides-2026, cursor-velocity-quality-2025, stanford-denisov-blanch, denisov-blanch-2026-ramp. | G3: the same five sources, same reason (05). | **Same direction & confidence** | Exact match. |
| 21 | Provenance: Microsoft–GitHub | peng, cui, heilman, microsoft-cli-agents, quispe (v2), demirer, hoffmann: one cluster. | G5 (peng, cui, hoffmann, demirer, both quispe) + G6 (heilman, microsoft-cli), with "combine with G5 and G7 when counting Microsoft sources"; soft links G18 (05). | **Same direction & confidence** | B also catches the quispe table-vs-record independence conflict that A had already retracted. |
| 22 | Provenance: AIDev | About ten sources in the base form one voice; the attribution heuristic is unvalidated; the cluster now contradicts itself (NAIST vs Deakin). | G1: 13 sources plus ramp indirectly; one voice; heuristic unvalidated (05). | **Same direction & confidence** | B correctly places agents-vs-ides-2026 in G1 too (its data is a matched AIDev subset; record line 10). B adds a Queen's authorship group (§2, B2). B never states the intra-cluster maintenance contradiction (§3, A9). |
| 23 | Provenance: Anthropic | Anthropic-tagged triage cluster: anthropic-economic-index, anthropic-postmortem-quality, shen-2026 (COI). | G12: the same three, "one vendor voice"; shen's COI "in both directions" (05). | **Same direction & confidence** | — |
| 24 | Adopt/reject metrics | 6 adopt / 9 reject (proposal). | 3 adopt / 3 reject families (04 Parts 2–3). | **Same direction & confidence** | B's three adopt metrics map onto A's #1, #2 and #3–4 plus #6. B adds a repo-age split and release-weighting. A adds spend paired with outcome, a complaint channel, and two specific rejects (time to first review comment; agent merge rate). Neither contradicts the other. |

## 2. Side B reached, Side A did not

These are items where Side B states a conclusion that Side A does not state, or states differently in its current outputs. Some apparent "new" items turned out to be already shared with Side A, and are listed at the end of this section, not counted.

- **B1. Whether E3 throughput gains last is contested, and the growth that does appear may come from newer models rather than practice.**
  - *Side B's claim:* 02 C2.
    - Tier A/B measured evidence runs both ways.
    - he-2026's placebo "release" moved the outcome as much as the real model releases did, so the model-vintage channel "cannot be identified".
    - demirer attributes the growth to model vintage, not learning.
  - *Contrast with Side A:* the exec brief says the gains "*grow with practice*" and advises "be patient: the gains compound over months".
  - *Assessment: supported.* The evidence I checked:
    - The he-2026 table row's quality note records the placebo.
    - `sources/he-2026-2x-mandate.md:39` says the genuine release coefficients sign-flip.
    - The demirer-2026-writing-vs-shipping row: "model improvement, not learning, drives growth".
    - Decay: cursor-velocity-quality-2025, commits +55.4% → ~0 by months 3–6.
    - Decay: agents-vs-ides-2026, prior-AI-IDE cohort → −35%.
    - Decay: quispe-2026-claude-frontier, +40.7 → +13.3.
    - Decay: demirer's asynchronous arm.
  - Side A has the decay evidence in `rq5-translation.md` and the measurement proposal ("velocity gains sometimes spike and then vanish by month 3–6"). The exec brief does not carry it.
- **B2. A Queen's University author group links harness-evolution-2026 and zhong-2026 to the AIDev creators.**
  - *Side B's claim:* 05 G2.
  - *Contrast with Side A:* `rederivation-r4.md` §E lists both harness-evolution-2026 and zhong-2026 as "genuinely new voices".
  - *Assessment: partly supported.*
    - harness-evolution-2026's authors are Ben Sghaier, **Li, Adams, Hassan** (record lines 3–4). AIDev's authors are **Li, Zhang, Hassan** (aidev-dataset-2026 record). That is two shared authors.
    - zhong-2026 shares Adams with harness-evolution, and Queen's University with AIDev. Its record says the data are its own mining, with only the taxonomy borrowed.
    - So harness-evolution is new *data* from the same research group, not a new author voice. zhong is new data from an adjacent group.
    - B's own G2 wording ("shared authors … Hassan, Li, Adams") is loose for zhong, which shares only Adams, and only with harness-evolution.
- **B3. One firm reports both a spend figure and an output figure.** At he-2026, Claude-only spend rose about 20× ($42→$856 per developer-month) while PRs rose 1.5–2×.
  - *Side B's claim:* 01 RQ4, 04 Part 2 #3, flagged as B's own juxtaposition.
  - *Contrast with Side A:* the exec brief says "every organisation that publishes costs publishes **nothing** about what the money bought".
  - *Assessment: supported as a fact about the record.* he-2026 has both rows (table rows for spend and for throughput). A's own RQ4 memo is more careful ("only thin authoring-cost data").
  - The juxtaposition itself is weak as a *ratio*: the time windows differ, the spend is Claude-only, and the base is small. B says as much.
- **B4. T10 documentation is among the three least-evidenced task types; T9 is "close behind".**
  - *Side B's claim:* 04 Part 1.
  - *Assessment: a counting artefact as much as a finding.*
    - B's T9 count (39 rows) is inflated by broad multi-tags: failed-agentic-prs-2026 ×10; xu-2025-maintenance-burden (E1); harness-evolution-2026 (a lab study of harness tooling, not of AI value for internal tools).
    - B concedes T9 has "no outcome study".
    - T10 has merge-rate proxies only (AIDev one voice) plus a negative readability subset.
  - Neither type has a measured value outcome, so the substantive disagreement is small.
- **B5. T11 ops: three independent Tier C organisations show that destructive incidents occur when agents have unguarded production access.** Rates are unknown. Medium (01 RQ3; 03 #7).
  - *Contrast with Side A:* Side A holds this only in `follow-up-questions.md` Q3(a) and `rederivation-r3.md` ("existence proofs at the destructive end … Grigorev — where the destroy was human-APPROVED"). `rq3-failure-map.md:29` is stale: it still lists Replit and the misalignment study as unextracted leads.
  - *Assessment: existence is supported; "three independent" is generous.*
    - amazon-2026-outages is disputed on AI causation. B notes the dispute but still counts the source towards the three-source rule.
    - grigorev's own record says "the human being told before the destroy ran", so "unguarded" means no deletion protection, not no human in the loop.
- **B6. Agents misreport their own work, and a low capacity to verify it predicts failure.**
  - *Side B's claim:* dev-agent-misalignment-2026, "22.6% of episodes contain inaccurate self-reports … agent self-corrects only 2.99%" (01 RQ3).
  - *Contrast with Side A:* Side A uses this source only for the 0.07% catastrophic tail.
  - *Assessment: supported in direction, overstated in scope.* In the table:
    - 22.58% is the share of the 16,118 *already-misaligned* episodes, not of all episodes.
    - 2.99% is computed on the 1,504 episodes with a visible outcome, only 9.33% of misaligned episodes; 90.67% have unknown resolution.
    - Neither caveat appears in B.

**Shared, not counted.** These looked like Side B-only items but Side A already holds them:
- the construct split in C3 (A's "queue vs function");
- agents-vs-ides-2026 being AIDev-derived (A's aidev-dataset-2026 record);
- RCT fragility in METR's 2026 wave (A's exec brief);
- seniority non-significance (A's tension 5);
- the quispe independence conflict (A retracted it in the independence-crisis piece).

## 3. Side A reached, Side B did not

For each item: whether the export Side B worked from contained the cue, or whether the conclusion depended on material Side B could not see.

- **A1. "Numbers get mangled as they travel": twenty-five documented corruptions (exec brief "sure" #2).**
  - *The cue is present, but only piecemeal.* Individual instances sit in the records:
    - the 45% vs 30.8% contrast (atlassian-2026-ai-review mentions "45%" 13 times);
    - the bain-2026-benchmark phantom report;
    - LinearB's 4.6× vs 5.25× (linearb-2026-benchmarks);
    - Opsera's 5× (opsera-2026-benchmark);
    - the Uber figure attributed to Microsoft (ai-spend-landscape-2026);
    - the DevX "55% myth" lead (peng-2023-copilot-rct record).
  - 53 record lines carry "phantom / laundered / untraceable / not in its own report" language. Side B used several of these as hygiene (05 "Single-event retellings", "Possible shared figure").
  - *What Side B could not see:* the **count** and the **framing as a top-three certainty**. Both live in Side A synthesis (`independence-crisis.md`, `rq2-measurement-methods.md`, Q13). The word "corruption" appears in only two source records. The cluster-tagged triage that made this a research theme is in LEDGER.md, which was not exported.
- **A2. "Spending changed shape" (seat-to-token regime change) and "consumption grows at flat prices" (exec brief "sure" #3).**
  - *The cue is present:* `sources/ai-spend-landscape-2026.md:9` is headed "The headline structural finding: a seat→token regime change during 2026".
  - Side B read the cluster and judged the Tier C spend figures "weak and recycled". It judged dora-2026-roi hypothetical, and Uber one voice laundered through several outlets.
  - The flat-price consumption cue (harness-evolution-2026 token rows) was also present. Side B did not use harness-evolution-2026 outside G2.
- **A3. "AI is creating copy-paste spaghetti" is contradicted by measurement: "four studies from three independent groups found no duplication increase."**
  - *The cue is present:* agents-vs-ides-2026 (AF +7.92% n.s.); cursor-velocity-quality-2025 (+7.03% n.s.); mao-2026-code-metrics (AI 14.29% vs human 27.57%).
  - Side B instead put more-code-less-reuse-2026 (1.87×) and gitclear-2025 on the "degrades" side and mao-2026 on the "null" side, without a duplication-specific verdict.
  - *The evidence also contains a counter-cue that Side A has not absorbed.* denisov-blanch-2026-ramp re-estimates the *same* agents-vs-ides panel. It finds duplicated-line density **+15.44% (L1, p<0.05) and +14.23% (L2+, p<0.01)** within agent-first repositories (record Table 5). That was extracted in R4, yet the R4 exec brief still says "no duplication increase". See §4.
- **A4. Mechanical, well-specified changes (migrations) are the exception inside old code [C/D, low-medium].**
  - *The cue is present:* google-migrations-2025 (C; 74–80% AI-authored changes measured, time savings self-reported); nubank-devin-2025 (D; 12×, estimate-based).
  - Side B read the same rows as "migration speed self-reported by a single organisation". It paired them with a "measured quality adverse" citation that does not measure migrations: agent-maintainability-2026's −8.21% is the success rate of *refactoring tasks performed on agent-authored code*.
- **A5. Detectability: standard test suites and vendor evals miss agent-quality drift.**
  - *Side A's sources:* anthropic-postmortem-quality, plus harness-evolution-2026 ("35 releases … passed >300 CI tests"). Two provenances; medium.
  - *The cue is fully present* in both records and their table rows. Side B missed it. Both sources appear in B only as members of independence groups (G12, G2).
- **A6. DORA's throughput flip sits inside a redefined self-report instrument; the "J-curve" has zero longitudinal support (tension 3 internals).**
  - *The cue is present:* dora-2024, dora-2025 and dora-2026-roi rows. Side B noted that dora-2026-roi has "no new data collection" and re-models dora-2025 (05 G9).
  - It never analysed the flip, probably because B ranked the stability question below its top five.
- **A7. Who does the follow-up work on agent code is contested within AIDev:** 83.21% human maintenance commits (agent-code-maintenance-2026) vs 69.6% same-agent fix PRs (who-finishes-the-job-2026).
  - *The cue is present* in both records. Side B cites who-finishes only for OR 1.62.
- **A8. The scarcity headline as the lead message, and "we predicted this thinness in writing".**
  - *Partly dependent on material Side B could not see.* The pre-registered scarcity clause (PROTOCOL §8) was cut with everything from §5 onward. The audit that invoked it is in `synthesis/`. RQ4's own "insufficient evidence" expectation *was* visible, and B honoured it.
  - B's evidence-only reading puts "agentic tools raise measured output" first. It reserves "the evidence cannot say" for task time on mature code, delivery and stability.
- **A9. "Gains grow with practice; be patient"** — not reached by B, which reached the opposite. See §2, B1.
- **A10. Rare languages do badly (stanford-denisov-blanch: Cobol/Haskell/Elixir).**
  - *The cue is present* in the stanford record.
  - It is pre-agentic and talk-grade. Side B's omission is minor.

## 4. Discrepancy triage

No scorecard row is "different direction". One row is "absent" (row 17, covered by A1 below). Every item from §2 and §3 is triaged; A9 is triaged together with B1.

Recommendation codes:
- **(i)** Side B right, Side A wrong → correction to Side A's outputs.
- **(ii)** Side A right, Side B missed evidence → name the cue Side B needed.
- **(iii)** genuine judgement call → record both positions.

### B1 / A9: do agentic gains grow with practice, or are they transient or model-driven?

**Case for Side A.**
- he-2026-2x-mandate is the only enterprise causal panel. Its accumulating-use slope (+0.45 log points) is the *larger* share of the effect, and it reaches 1.99× by month 9.
- The open-source decay results (cursor-velocity-quality-2025, agents-vs-ides-2026) come from self-selected repositories where "adoption" may not mean continued use.
- The brief scopes the claim to "the best-documented company" and labels it "one company, medium".

**Case for Side B.**
- The same he-2026 record says a fabricated placebo release moved the outcome as much as the real releases did. The authors decline exact causal attribution.
- demirer-2026-writing-vs-shipping, the largest panel, attributes growth over time to model vintage, "not learning".
- Four Tier A/B E3 sources show decay or reversal: cursor-velocity-quality-2025, agents-vs-ides-2026 (prior-AI-IDE cohort), quispe-2026-claude-frontier, and demirer's asynchronous arm.
- "Grow with practice" names a mechanism that the source itself says it cannot identify. "Gains compound" generalises one firm against four contrary panels.

**Recommendation: (i) correction.** Rewrite exec-brief §"Best case" and action 1. Suggested wording: "at one firm, gains kept growing for nine months, but whether from practice or from newer models cannot be told apart; in open-source panels, gains often faded within 3–6 months".
- Side A already holds this evidence in RQ5 and in the measurement proposal; the brief did not carry it.
- Add durability to `contradictions.md` as its own entry. It is a real contradiction that no §5 tension covers.

### B2: is harness-evolution-2026 a new voice?

**Case for Side A.**
- harness-evolution-2026 is a lab study on its own harness and benchmark. It shares no data with AIDev.
- Its role in the detectability leg is to be independent of *Anthropic*, which it is.

**Case for Side B.**
- Two of its four authors (Li, Hassan) wrote AIDev. The programme's own rule (CLAUDE.md: "share authors … count as one voice") makes it the same research voice as the AIDev creators.
- `rederivation-r4.md` §E lists it as "genuinely new".

**Recommendation: (i) correction, narrow.**
- Re-label harness-evolution-2026 in §E as "new data, AIDev-author group (Queen's)".
- Keep zhong-2026 as new data from an adjacent institution.
- The detectability verdict does not change.

### B3: does anyone publish both cost and outcome?

**Case for Side A.**
- No source publishes cost *per unit of outcome for the same task*.
- he-2026's spend is Claude-only, has no review cost, and covers a different window from the throughput estimate.
- RQ4's memo states this precisely.

**Case for Side B.**
- The brief says publishers of costs publish "nothing" about returns. he-2026 publishes a per-developer spend series and a causal throughput estimate in the same paper.
- That is not "nothing". A non-engineer reading the brief would be misled about the state of disclosure.

**Recommendation: (i) correction, wording.** Change the brief sentence to "no organisation publishes what the money bought per unit of spend; the one firm that reports both shows spend rising far faster than output". Keep RQ4 as it is.

### B4: T9 or T10 among the three driest task types?

**Case for Side A.**
- Targeted hunts for T9 outcomes came back dry.
- T10 has at least merge-rate and readability evidence.
- Ranking by row count rewards broad multi-tagging, which B itself corrected for with "focused rows".

**Case for Side B.**
- Even on focused rows, T9 has only two A/B sources and T10 three, and T10's evidence is one AIDev voice plus a negative readability subset.
- Neither type has a measured value outcome.

**Recommendation: (iii) judgement call.** Record both. Q5 should say: "T1, T2, T9 and T10 have no measured value outcome; T1 and T9 have nothing at all".

### B5: T11 destructive incidents

**Case for Side A.**
- The existence of the failure mode is already held in Q3(a), with the nuance that the Grigorev destroy was human-approved (automation bias, not autonomy).
- Its rate is "of the order of 0.1%, imprecise" (dev-agent-misalignment-2026).
- It belongs in follow-up questions, not in a two-page brief.

**Case for Side B.**
- Three named organisations: grigorev-2026-terraform-db, replit-db-deletion-2025, amazon-2026-outages.
- For a reader deciding whether to grant agents production access, the existence of the failure mode is decision-relevant.
- `rq3-failure-map.md` still says these are "queued but not yet extracted". That memo is stale.

**Recommendation: (iii) judgement call** on whether this belongs in the brief, plus a **housekeeping correction** to `rq3-failure-map.md` §3. Side B's "three independent" should read "two uncontested existence proofs plus one disputed case".

### B6: agent self-report unreliability

**Case for Side A.**
- dev-agent-misalignment-2026's denominators are conditional and mostly unobserved (90.67% unknown resolution).
- Side A used the source only for what it can bear.

**Case for Side B.**
- Inaccurate agent self-reports are a measured symptom class (22.58% of misaligned episodes), and the share is rising.
- It bears directly on RQ6: if the agent's own summary is unreliable, verification capacity is the binding constraint.

**Recommendation: (iii) judgement call.** Side B's figures must carry their denominators. Side A could add it to RQ3 as a low-confidence mechanism.

### A1 / row 17: "numbers get mangled as they travel"

**Case for Side A.**
- The instances are individually documented to source-record standard: Atlassian 45% vs 30.8%; LinearB 4.6× vs 5.25×; Opsera 5×; bain-2026-benchmark phantom; ai-spend-landscape-2026 Uber→Microsoft.
- It is a methodology finding that no single source makes, so only a synthesis can reach it. High confidence on "it happens" is earned.

**Case for Side B.**
- Its absence from B is mostly not a miss. The aggregation lives in synthesis files B could not see, and B applied the hygiene instance by instance anyway.
- Whether this is one of the *three things we are most sure about* for an executive reader is a framing choice. It is about the information environment, not about AI's value.

**Recommendation: (ii) Side A right on substance; legibility cue needed.** A per-record field, "transit check: primary figure vs circulating figure", would let a blind analyst count. The *placement* as "sure" #2 is a framing decision; note it as framing-dependent (see §5).

### A2: seat-to-token regime change

**Case for Side A.**
- `ai-spend-landscape-2026` triangulates the regime change across DX, Gartner, Pragmatic Engineer interviews and vendor list prices.
- The brief already says "we use only the spread".

**Case for Side B.**
- The comparison spans two different surveys and populations: DX 2025 per-year vs Gartner 2026 per-month.
- Most of its components are Tier D, and the Uber figure is one voice retold.
- "C, high on the pattern" grades a Tier D-dominated cluster above its parts.

**Recommendation: (iii) judgement call, with a calibration note.** The direction (consumption pricing, growing bills) is plausible and Side B did not dispute it. A's "high" should be "medium": the pattern rests on cross-survey comparison, not on a panel.

### A3: duplication "contradicted by measurement"

**Case for Side A.**
- No study with per-repository AI attribution finds GitClear's population-trend rise.
- The two CMU DiDs are null.
- mao-2026-code-metrics finds AI-attributed code less duplicated.
- GitClear has a documented composition jump.

**Case for Side B.**
- The "four studies, three independent groups" count does not survive inspection:
  - agents-vs-ides-2026 and cursor-velocity-quality-2025 are one voice;
  - agent-maintainability-2026 measures duplication as a *predictor* of maintenance cost, not whether duplication rose;
  - mao-2026 is E2-weighted.
- denisov-blanch-2026-ramp re-estimates the same agents-vs-ides panel and finds **significant duplication increases** in agent-first repositories (+15.44%, +14.23%).
- more-code-less-reuse-2026 finds 1.87× semantic redundancy.
- For E3, the measured picture is mixed, not contradicting.

**Recommendation: (i) correction.**
- Replace the brief's bullet with: "the duplication scare is not supported for older tools; for agents the evidence is mixed: one research group's estimates go both ways on the same data".
- Update the tension-4 duplication leg to absorb the ramp result.
- Side B did not reach the corrective conclusion either, but its refusal to call the leg is the better-calibrated position.

### A4: migrations as the exception inside old code

**Case for Side A.**
- google-migrations-2025 measures 74–80% AI-authored change share, a measured instrument.
- The direction matches the practitioner perception map (dont-vibe-control-2026).
- A grades it low-medium.

**Case for Side B.**
- Time saved is self-reported.
- Nubank's 12× is an estimate from a vendor-told rollout.
- Two organisations fall below the three-source Tier C rule.

**Recommendation: (iii) judgement call.** A's grade is honest.
- Side B's adverse-quality citation (agent-maintainability-2026 refactoring −8.21%) is a **construct error**: it measures maintaining agent-authored code, not agent-performed migrations. It should not stand as T5 evidence.

### A5: detectability leg

**Case for Side A.**
- Two provenances independent of each other: anthropic-postmortem-quality (D, against interest) and harness-evolution-2026 (A for rigour, lab).
- Both show standard tests and evals missing quality drift.
- This directly informs RQ6.

**Case for Side B.**
- One source is a vendor postmortem and the other is one harness with one open-weight model. Internal number conflicts are flagged in its own record.
- Not ranking it in the top five is defensible.

**Recommendation: (ii) Side A right; Side B missed evidence that was in its inputs.** Cue needed: the harness-evolution-2026 rows' relevance column should name the "passed >300 CI tests" result as a measurement-validity finding (RQ2/RQ6), not only as a T9 tooling result.

### A6: DORA flip and the J-curve

**Case for Side A.**
- The dora-2024 and dora-2025 rows show the throughput sign change.
- dora-2024 introduced the rework-rate item into stability.
- dora-2025 tested and rejected the maturity moderation that the J-curve implies.

**Case for Side B.**
- All three are self-report or no-data sources. Side B already refuses to let any of them carry a stability claim, so the flip does not change its RQ5(b) verdict.

**Recommendation: (ii), minor.** Cue needed: a stability-construct note on dora-2025's row ("throughput factor redefined 2024").

### A7: who does follow-up work on agent code

**Case for Side A.** Both records are in the export, and the disagreement (83.21% vs 69.6%) is the clearest intra-AIDev contradiction.

**Case for Side B.** Both papers are one AIDev voice. B already reports the stronger of the two outcomes (OR 1.62), and different units make "who" uninterpretable.

**Recommendation: (ii), minor.** The cue was present. Side B's one-voice discount explains why it was not ranked.

### A8: scarcity as the headline

**Case for Side A.**
- No randomised or quasi-randomised study measures task time or delivery for a mature present-day agent on realistic work. B concedes this ("cannot say").
- METR's 2026 redesign is abandoned.
- The two systematic reviews (genai-productivity-meta-2026; wittig-2026-fragmented-markers) found almost no agent-class measurements.

**Case for Side B.**
- Side A itself grades he-2026 Tier A E3 and demirer Tier B E3 and quotes both as measured.
- A headline saying "nobody has properly measured today's AI agents yet" is in tension with A's own "genuine ≈1.5–1.7× throughput gain".
- "Only three randomised trials have tested AI coding productivity on working developers" omits cui-2024-copilot-field: three randomised field experiments on 4,867 employed developers, Tier A, E1. A's R3 reviewer had already flagged the count as over-scoped.
- The headline's prominence traces to the PROTOCOL §8 scarcity clause, which B never saw.

**Recommendation: (iii) judgement call on emphasis, with (i) on the count.**
- Correct "only three randomised trials … on working developers" to count cui-2024's field experiments, or narrow the wording.
- Soften "nobody has properly measured" to "nobody has yet measured present-day agents on delivery outcomes or on mature code".

### A10: rare languages

**Case for Side A.** stanford-denisov-blanch gives a clean mechanism (training-data scarcity).

**Case for Side B.** The source is talk-grade and pre-agentic, and its quadrant is one voice with he-2026.

**Recommendation: (iii).** Low stakes; A's "B, medium — partly pre-agentic" label is fair.

## 5. Summary statistics

| Score | Count | Rows |
|---|---|---|
| Same direction & confidence | **15** | 1, 2, 4, 5, 8, 11, 12, 14, 16, 19, 20, 21, 22, 23, 24 |
| Same direction, different confidence | **8** | 3, 6, 7, 9, 10, 13, 15, 18 |
| Different direction | **0** | — |
| Absent | **1** | 17 |
| **Total** | **24** | |

- **Same direction: 23 of 24 targets (96%).** Same direction and same confidence: 15 of 24 (63%).
- **The confidence differences all run one way.** In all eight rows Side A is the more confident side, by one step (high vs medium, or medium vs low). Side B is never more confident than Side A.
- **How the tensions map onto Side B's contradictions.**
  - Four of the seven §5 tensions appear among Side B's top five: T1 → C5, T2 → C1, T4 → C4, T6 → C3.
  - Two more appear in its "considered" list: T3 and T5.
  - T7 appears as a metrics verdict rather than a contradiction, which is correct: no source defends those metrics.
  - One of Side B's top-five contradictions, C2 (whether throughput gains last), has no §5 counterpart.
- **Triage outcomes across §§2–3 (15 items):**

| Outcome | Count | Items |
|---|---|---|
| (i) Side A should correct | 5 | B1/A9 durability; B2 harness-evolution's voice; B3 the "nothing" wording; A3 duplication; part of A8, the RCT count |
| (ii) Side A right, Side B missed a cue | 4 | A1, A5, A6, A7 |
| (iii) Judgement call | 7 | B4, B5, B6, A2, A4, A10, plus A8 on emphasis |

**Overall reading.** On direction, the programme's conclusions follow from the evidence. A blind analyst with no sight of the tensions, the synthesis or the ledger:
- re-found the same direction on 23 of 24 targets;
- rebuilt the four provenance clusters almost member for member;
- reached the same pre-registered RQ4 outcome.

Where the two sides differ, the gap comes from framing that built up over five cycles. Side A's evidence is not wrong in those places; the framing goes past it. The framing-dependent conclusions are:
- **The headline.** Making scarcity the lead message ("nobody has properly measured today's AI agents yet") traces to the PROTOCOL §8 clause, and the RCT count in it is too narrow.
- **"Sure" #2.** Placing corruption in transit among the three surest things is a programme theme the records support only piecemeal.
- **"Sure" #3, second half.** The "high" on the spend regime change rests on cross-survey Tier D comparison.
- **"Grow with practice … gains compound".** This line contradicts evidence Side A itself holds.
- **"Copy-paste spaghetti is contradicted by measurement".** This was not updated after the R4 RAMP re-estimate.
- **A uniform one-step confidence premium,** most visibly tension 6's R4 upgrade to high. That upgrade leans on a study (demirer-2026-writing-vs-shipping) that measures no review time.

**Caveat on what this agreement can show.** Most of the agreement is evidence-driven. It cannot fully separate "the tensions are real" from "the evidence base was collected in their shape":
- the searches that built `sources/` followed the §5 query plans;
- the records keep RQ tags and extractor "can / cannot support" verdicts written with the tensions in view.

So agreement on *which* contradictions exist is weaker evidence than agreement on *how they resolve*. Side B's one new top-five contradiction, the durability of gains, is the clearest sign of what the §5 framing left out.

## 6. Referee notes

### Spot-checks of Side B's figures against `evidence/evidence-table.tsv`

18 figures checked. Rows are identified by source_id.

| # | Side B figure | Table / record | Result |
|---|---|---|---|
| 1 | he-2026 PRs 1.46× / 1.72×; $42→$856 per developer-month | he-2026 rows "total +0.54 log pts = 1.72x (baseline) / 1.46x (preferred)"; "$42 -> $856 … ~20x" | **Match** |
| 2 | demirer lines +957%, commits +153%, PRs +86%, releases +19.8% | demirer-2026-writing-vs-shipping: +957.5 / +153.2 / +86.0 / +19.8 (SE 2.9) | **Match** |
| 3 | cursor-velocity warnings +30.26% [17.3, 44.4], complexity +41.64%; commits +55.4% → +14.5% → ~0 | cursor-velocity-quality-2025 rows, identical | **Match** |
| 4 | agent-maintainability up to −13.1 pp; refactoring −8.2% | "Up to -13.1pp … refactoring avg -8.21%" | **Figures match.** The placement under T5 value (01 RQ1) is a construct error: these are follow-on tasks on agent-authored code. |
| 5 | who-finishes OR 1.62 [1.10, 2.39]; 3.68% vs 2.34% | "OR 1.62 (95% CI 1.10-2.39, p=0.015) … 3.68% (74/2,012) vs 2.34%" | **Match** |
| 6 | review-agents-reality 45.20% vs 68.37% | "45.20% (CRA-only, n=281) vs 68.37% (human-only, n=1,176)" | **Match** |
| 7 | churn-151 file-based 0.17→0.06; ~80% no discontinuity | "file-based churn 0.17→0.06 … ~80% show no significant discontinuity" | **Match** (Side A quotes the line-based 0.68→0.50; both are in the row) |
| 8 | arch-quality raw smells +1.1%, p=0.82 | "β=0.0108 … p=0.82; +1.1%" | **Match** |
| 9 | quispe-frontier +40.7 / +24.0 / +13.3 | "+40.708 … +24.004 … +13.277" | **Match** |
| 10 | agents-vs-ides prior-AI-IDE cohort +3.06% n.s., → −35% by month 6 | identical | **Figures match.** Classifying this cohort as "legacy or mature code" (02 C1, Reconciliation) is not supported: the row and the record define it by prior tool exposure, and the record says there is "no explicit greenfield-vs-brownfield design axis". |
| 11 | microsoft-cli merged PRs "+21.3% [19.6, 23.0] by synthetic control" | Only row: "reference-group estimates: IC4 +21.3% [19.6, 23.0]" | **Mislabelled.** +21.3% is the dose-response IC4 reference-group lift at 3 days/week. The synthetic-control headline in `sources/microsoft-cli-agents-2026.md:47` is **+24.0% [14.5, 33.7]**. Side B's direction is right and the error is small. The table has one row for this source and it omits the headline, which is a legibility gap in the table. |
| 12 | dev-agent-misalignment 22.6% inaccurate self-reports; 2.99% self-correction | "S7 inaccurate self-report 22.58% (of n=16,118 [misaligned episodes])"; "RV1 … 2.99% (n=1,504; … 90.67% have unknown/unobserved resolution)" | **Figures match; denominators dropped** (see §2, B6) |
| 13 | stray ρ≈0.17 | "Spearman ρ≈0.17, p=0.406" | **Match** |
| 14 | unreviewed-ai-prs AI 71.1% vs human 65.5% reviewed | "AI 71.08% … vs human 65.48%" | **Match** |
| 15 | wittig 71.1% vs 54.5% | "64/90 positive (71.1%) … 42/77 (54.5%)" | **Match** |
| 16 | metr-2026 −18% (CI −38 to +9), −4% (CI −15 to +9) | metr-2026-uplift rows | **Match** |
| 17 | 99 source_ids in the table; 2 records without rows | 99 distinct ids, 101 files in `sources/` | **Match.** ghaleb-2026-fingerprinting and end-of-code-review-2026 are deliberately row-less (instrument check; position paper) per LEDGER. The cost is that Side B missed ghaleb's "AIDev validation is circular" finding, though it reached the same conclusion from aidev-dataset-2026. |
| 18 | 76 of 569 rows carry substantive cost data | A crude filter on column 12 (excluding none / n/a / not reported variants) gives ~71 | **Consistent within definitional noise** |

**Spot-check summary:** 16 of 18 figures are exact. One is mislabelled as to design (#11). One carries the right figures without their denominators (#12). There are two classification errors (#4, #10). I found no fabricated figure.

### Did Side B see Side A material?

I found no sign of leakage. Side B uses none of Side A's own phrasing:
- "corruption in transit"
- "queue vs function"
- "absorption"
- "Stanford–CMU" as a merged label
- "J-curve" as a critique
- tension numbers
- "dry holes"
- "upper envelope" outside its source attribution

Its method notes state the access boundary, and the protocol records config-level enforcement (execution note 3). The resemblance of its contradiction set to §5 is fully explained by the accepted residual leakage (RQ wording, T3/T4 taxonomy notes, extractor "can/cannot support" text) and by the tension-shaped search that built the corpus.

### The redaction was broader than intended

It removed substantive, non-conclusion lines. Examples from `synthesis/cleanroom-r5/redaction-log.txt`:
- `he-2026-2x-mandate.md` lines 48–49 (the newer-code and review numbers headings), line 63 (seniority) and line 68 ("Can support");
- `peng-2023-copilot-rct.md:59` (the self-report-vs-measured finding);
- `google-rct-2024.md:41` (seniority heterogeneity).

Side B recovered all of these from table rows. This probably cost it google-rct-2024's brownfield-positive nuance (row 2). Execution note 3 already records the problem; I confirm it.

### Side A internal inconsistencies found while refereeing

These are not discrepancies with Side B:
- **`internal-measurement-proposal.md` "Honest limits"** says the skill-erosion evidence is "two studies … both from the pre-agent era". The R4 exec brief says "one chat-era, one with an early agent" (impaired-programming-2026). The proposal was not refreshed.
- **`rq3-failure-map.md:29`** still lists Replit and the misalignment study as unextracted leads.
- **The exec brief's RCT count** omits cui-2024-copilot-field (see §4, A8).
- **The exec brief's duplication bullet** predates absorption of denisov-blanch-2026-ramp (see §4, A3).

### What I could not resolve

- **Whether tension 6's R4 upgrade to high is earned.** On "generation outpaces delivery" I would grade it medium-high. On "the bottleneck is *review* specifically" I would grade it medium: the review-specific measures are one firm (he-2026), Tier D telemetry and narratives, and demirer measures no review time. The human should adjudicate. The second referee's view on this row matters.
- **Whether durability of gains deserves promotion to a standing tension.** I recommend recording it as a contradiction (§4, B1). Making it a new §5-level tension is a protocol decision for the human.
- **How much of the 96% same-direction rate reflects the evidence and how much reflects the corpus being collected to the §5 query plans.** This run cannot separate the two. The L3-fable run measures inter-analyst variance, not corpus framing.
