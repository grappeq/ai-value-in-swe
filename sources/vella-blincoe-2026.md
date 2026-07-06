# vella-blincoe-2026 — Two-wave longitudinal survey of professional developers' AI-assisted work

**source_id:** vella-blincoe-2026
**Date verified:** 2026-07-06 (Phase 1)
**RQs fed:** RQ2 (primary — perception/self-report methodology), RQ6 (secondary — anti-metric/instrument candidates), §5 tension 6 (bottleneck displacement, secondary)
**Cross-cutting theme:** Skill formation & cognitive effects (PROTOCOL v0.4) — cognitive load and flow-state erosion findings feed this theme directly.

## Citation

Vella, A., & Blincoe, K. (2026). *The Impact of AI Coding Assistants on Software Engineering: A Longitudinal Study.* arXiv preprint.

- arXiv: [2605.23135](https://arxiv.org/abs/2605.23135) — v1, submitted 22 May 2026 (`arXiv:2605.23135v1 [cs.SE]`). Version read for this record: v1 (only version available).
- Affiliations (as printed): both authors, University of Auckland, New Zealand.
- Status: **preprint, not peer-reviewed.** No venue/journal submission mentioned in the text. Likely derives from Vella's Master of Engineering research at Auckland under Blincoe's supervision (thesis link not located/confirmed in the paper itself — reported by secondary sources, not verified against a primary thesis record; treat as probable, not confirmed).
- Funding: **Marsden Fund Council, from Government funding, administered by the Royal Society Te Apārangi (New Zealand)** — found via secondary source (WebSearch snippet), not directly quoted from the PDF text in this session (the acknowledgements section fell outside the fetch tool's extracted range both times it was tried). No vendor or tool-company funding identified in any pass.

**Author-name verification (per task brief's flag):** triage note's authors are correct as given — **Annie Vella and Kelly Blincoe**, no correction needed.

## Verification status

**VERIFIED — full text read**, via two independent WebFetch passes over the arXiv HTML rendering (`arxiv.org/html/2605.23135v1`) plus a WebSearch cross-check. Not abstract-only: methodology, statistics (means, deltas, p-values, effect sizes, Holm-Bonferroni correction, Fisher's exact attrition tests), limitations, and tool-adoption tables were all retrieved from body sections (Results, Discussion §5.3, Limitations), not the abstract. **One gap:** the acknowledgements/funding statement and the exact Likert-item wording were not returned by the fetch tool (paper directs readers to an "online replication package" for the full instrument, which was not located/fetched this session) — flagged as a follow-up lead, not treated as verified from primary text.

## Tier, era, independence

- **Tier: B.** Two-wave matched-panel survey with real statistical rigour for a self-report instrument: paired significance tests with effect sizes (rank-biserial r), Holm-Bonferroni correction for multiple comparisons across task-focus items, and an explicit attrition-bias check (Fisher's exact, no significant demographic skew found). This is the "well-instrumented self-report → B" case per CLAUDE.md, not the "informal → C" case. **Held back from A** because: no objective/measured comparator of any kind (no telemetry, commits, PRs, or code-quality data); non-probability convenience/referral sampling (LinkedIn/X/Facebook/Discord/Slack, 33 orgs approached, 9 agreed to distribute); single-item Likert constructs for most measures (explicit respondent-burden trade-off, acknowledged by the authors); low internal consistency where multi-item scales were used (Creation-task α = 0.40–0.49, Verification-task α = 0.56–0.57 — authors themselves flag these as "low"); 40% Q1→Q2 attrition (60% retention to the matched n=95).
- **Era: correction to the ledger's provisional tag.** LEDGER.md's queue line tags this "(B, E3)". **That tag is not supported by the paper and should be revised.** The instrument does not mention "agentic" or "agent" anywhere, does not distinguish autocomplete/chat/agentic modality, and does not stratify any finding by tool capability. Tool adoption at Q1→Q2: GitHub Copilot 70%→58%, ChatGPT 70%→58%, Cursor 16%→29% (Cursor is capable of agentic use but the paper does not establish participants used it agentically, nor separates its effect). Correct tag: **E1/E2-dominant** (Copilot-classic + ChatGPT chat-copy-paste are the majority pattern throughout both waves), **with an encroaching-but-unstratified E3 signal** (Cursor's rising share, general "tool diversification" toward "coding-specialised tools"). Per PROTOCOL §2's mixing rule, since the study does not split findings by modality, none of its quantitative findings can be cleanly assigned E3 and should not be used to satisfy the DoD's E3-evidence bar. This also means the task brief's parenthetical "(E3)" and the ledger's provisional tag should both be read as **not confirmed** — flag for ledger correction at next update.
- **Independence:** Academic, New Zealand government research-council funding (Marsden Fund) per secondary-source confirmation; no tool-vendor or consultancy funding found. Clean of COI as far as verified. Caveat: funding statement itself not directly quoted from primary text this session (see Verification status) — treat as probable rather than fully primary-confirmed.

## Method & population

- **Design:** Two-wave longitudinal online questionnaire (Qualtrics), ~15-minute target completion, mixed methods: Likert-scale items (1–5), multiple-choice, ranking tasks, and open-ended questions (analysed via reflexive thematic analysis). **Entirely self-report — no diary, telemetry, interview, or code-artefact component of any kind.**
- **Waves:** Q1 October 2024 (224 total responses → 158 eligible), Q2 April 2025 (111 total responses → 101 eligible), six months apart. Matched longitudinal cohort: **95** (≈60% retention from Q1's 158; the task brief's "158→101→95" figure is confirmed exactly).
- **Recruitment:** Convenience + referral-chain sampling via LinkedIn, X, Facebook, Discord, Slack developer communities; 33 organisations approached, 9 agreed to distribute internally.
- **Population:** 85% male / 12% female / 1% non-binary; experience mix 13% junior / 49% mid-career / 37% senior; roles 36% fullstack, 23% backend, 15% manager/architect, 8% mobile, 9% specialised; 28 countries (41% New Zealand). Professional engineers, not students — a stated advantage over much prior survey literature.

## Headline findings, exact numbers

**Productivity (perceived, self-report only):**
- 84% reported improvement at **both** Q1 and Q2 (identical topline rate across waves).
- Among matched participants, 77% gave an *identical* productivity rating Q1→Q2; 14% decreased in stated intensity, 9% increased; **no participant crossed into net-negative territory** at either wave.

**Developer-experience dimensions (matched cohort, n=94; DevEx-framework-derived constructs):**
- Feedback loops: improved significantly, Δ mean = +0.21, p = 0.038, rank-biserial r = 0.38 (33% improved / 18% declined).
- Cognitive load: declined, but **not statistically significant** — Δ mean = −0.15, p = 0.195, r = −0.26 (19% improved / 29% declined).
- Flow state: declined, also **not statistically significant** — Δ mean = −0.18, p = 0.195, r = −0.24 (27% improved / 35% declined).
- Composite: the proportion of matched participants reporting **worsened experience on at least one dimension** grew from 14% (Q1) to 27% (Q2) — this is the headline "productivity-experience paradox" number and it is a real, reported shift, but it sits alongside two dimension-level tests (cognitive load, flow) that individually fell short of significance. Both things are true at once: the *composite any-worsening* share roughly doubled, while the *mean-level* cognitive-load and flow-state deltas were directional but non-significant. Do not over-round this to "cognitive load rose significantly" — the paper itself does not make that claim.
- **Decoupling finding (important for RQ2/RQ6):** no significant correlation between changes in any developer-experience dimension and changes in self-reported productivity (smallest adjusted p = 0.313). I.e., even within pure self-report, "I feel more productive" and "my day-to-day experience got worse" are statistically independent in this sample — people are not simply rationalising a felt cost against a felt gain; the two self-report constructs move separately.

**Task-focus / "supervisory engineering work" shift (matched n=88):**
- Writing code: 82% report spending **less** time by Q2; matched mean 1.93 (below the neutral midpoint of 3.0).
- Reviewing code: the **only** task-focus item above neutral at *both* waves (Q1 mean 3.03, Q2 mean 3.15; trend +0.23... reported elsewhere in the same section as "not significant" — the paper's own wording on this specific delta's significance was not fully resolved across fetch passes; treat the *direction* (reviewing holds/rises while writing falls) as the load-bearing claim, not the exact non-significant p-value).
- Testing: trended upward (Δ mean +0.25) but stayed below neutral.
- **Creation-to-verification balance score:** rose from 0.26 (Q1) to 0.53 (Q2), a statistically significant shift (p = 0.006, r = 0.39, "moderate" effect per the authors) — the clearest single quantitative anchor for the "supervisory work" reframing.
- Fine-grained crossover: 42% increased testing/reviewing time; 20% decreased writing time while increasing verification time; 17% increased *both* creation and verification; 42% were stable on at least one dimension.
- **Null result within this same construct:** no significant *individual-level* longitudinal change was detected for writing, refactoring, reviewing, debugging, or designing considered one at a time (all Holm-Bonferroni-adjusted p > 0.05), despite visibly large *cross-sectional* swings (e.g. the 82% writing-less figure) — the authors are explicit that the aggregate balance-score shift is where the significant signal lives, not the individual task items. Record this null with the same weight as the positive composite finding, per CLAUDE.md rule 3.

**"Supervisory engineering work" construct (qualitative + the quantitative shift above):** defined by the authors as the emerging bundle of directing AI, evaluating its output, and correcting errors. Thematic-analysis labels supporting it: "compressing routine creation work" (boilerplate, small fixes absorbed by AI), "from doing to supervising AI-generated code", "verification and trust calibration" reframed as a supervisory responsibility rather than an incidental QA step. This is qualitative/interpretive scaffolding around the quantitative creation→verification balance shift, not a separately measured construct.

## Measured vs self-reported (CLAUDE.md rule 4)

**Everything in this paper is self-reported.** There is no measured/telemetry/objective side at all — no commits, PRs, code-quality scores, deployment data, or observed time-on-task. The authors state this plainly as a limitation (below). This is the single most important framing point for how this source can be used: it is a rich, well-instrumented *perception* study, not a perception-vs-reality comparison.

| Finding | Basis |
|---|---|
| 84% productivity improvement (both waves) | Self-reported |
| Feedback loop / cognitive load / flow-state deltas | Self-reported |
| Task-focus shift (writing↓, reviewing steady, verification↑) | Self-reported |
| "Supervisory work" qualitative themes | Self-reported (open-ended, thematically coded) |
| Attrition/demographic bias check (Fisher's exact) | Measured, but about *survey methodology*, not about AI impact |

## Nulls / negative results

- No significant individual-task-level longitudinal change (writing, refactoring, reviewing, debugging, designing) once corrected for multiple comparisons — the paper's clearest null, sitting right next to its most-quoted positive finding (the balance-score shift). Both belong in any summary.
- Cognitive load and flow-state mean-level declines were **directional but non-significant** (p = 0.195 for both) — the "rising cognitive-load complaints" framing in the task brief is a fair characterisation of the *direction* and of the composite any-worsening figure (14%→27%), but overstates the dimension-level statistical result if quoted as "cognitive load rose significantly."
- No correlation between developer-experience change and productivity change (decoupling, smallest adjusted p = 0.313).
- No significant demographic skew in the 40% attrition (Fisher's exact) — the authors use this to argue the matched cohort is not obviously biased by who dropped out, while simultaneously (see limitations) flagging that the test cannot rule out *attitudinal* dropout (disillusioned engineers leaving the panel) since attitude/sentiment wasn't measured at Q1 for non-returners.

## Stated limitations (authors' own)

- Selection bias: convenience/referral sampling, not a probability sample.
- 40% attrition Q1→Q2; authors explicitly flag that demographic parity (tested) does not rule out **attitudinal dropout** (untested) — disillusioned engineers may have left the panel disproportionately, which would bias the longitudinal findings toward *overstating* stability and *understating* negative trajectories. This is a self-aware, non-trivial caveat the authors raise against their own headline stability finding.
- Cross-sectional/early-research framing: short six-month window against a fast-moving tool landscape.
- Single-Likert-item constructs (respondent-burden trade-off), limiting psychometric validation.
- Low internal consistency for multi-item task groupings (Creation α = 0.40–0.49; Verification α = 0.56–0.57), acknowledged as weak despite use.
- No objective productivity/quality/velocity measurement of any kind — self-report only, explicitly acknowledged.
- Professional (not student) sample is a stated strength versus prior literature, but cross-organisation generalisability is untested.

## What this can and cannot support

**Can support**, at Tier B with the era correction above: that in a matched-panel of professional developers surveyed six months apart (Oct 2024–Apr 2025, tool mix dominated by Copilot/ChatGPT with a rising but minority/unstratified Cursor share), self-reported productivity perceptions were stable and positive (84% both waves) while a meaningful and growing minority (14%→27%) reported worsened experience on at least one dimension (cognitive load, flow, or feedback loops); that the balance of self-reported task focus shifted significantly from creation toward verification/supervision (p=0.006); and that, within self-report alone, productivity and experience ratings are statistically decoupled — a methodologically useful signal for RQ6 (single self-reported productivity items may not capture developer-experience cost even when both are measured in the same instrument, at the same time, from the same people).

**Cannot support:** any claim about the *direction or magnitude of actual productivity change* (no measured comparator exists in this study — it cannot be used to confirm or extend the METR/Peng-style perception-reality gap, because there is no reality side to compare against here); any claim specific to agentic/E3 tooling (modality unstratified, term never used); precise causal attribution of the task-focus shift to any specific tool or tool generation; or generalisation beyond a self-selected, LinkedIn/community-recruited sample skewed 85% male and 41% New Zealand-based.

## Cross-reference assessment (report only — not written to contradictions.md)

- **§5 tension 1 (perception–reality gap) / `synthesis/contradictions.md` "Perception–reality gap: direction is not consistent":** this source **does not add a third datapoint** to that contradiction entry. The existing entry is specifically about *self-reported magnitude vs measured magnitude* (METR: over-estimate; Peng: under-estimate; Stanford: general miscalibration against a measured productivity score). Vella & Blincoe have no measured side at all, so there is no gap to place on either side of that ledger. What it *does* contribute to RQ2 is adjacent but distinct: evidence that self-report is internally incoherent even without a ground truth to compare against — a stable/positive productivity self-report and a worsening experience self-report can coexist, uncorrelated, in the same people at the same time. This is a reason to distrust single-item self-reported productivity as a sufficient instrument on its own terms, independent of whether it's miscalibrated against reality. Recommend treating it as a **separate, complementary RQ2/RQ6 finding** ("self-report constructs decouple from each other"), not a merge into the existing contradiction entry. Escalation not required — this is a fit judgement, not a contradiction discovery.
- **shen-2026-coding-skills (Anthropic RCT, chat-based GPT-4o, comprehension quiz, d=0.738 measured comprehension loss):** that source's own cross-ref section (written when it was extracted, queuing this paper) already characterises the relationship as "complementary, not contradictory" and tags Vella & Blincoe as "(Tier B, E3)" — **this session's extraction revises that era tag** (see Tier/era section above: E1/E2-dominant, unstratified encroaching E3, not confirmed E3). With that correction, the relationship still holds directionally: Shen & Tamkin supply a **causal, measured** mechanism candidate (heavy AI reliance degrades measured comprehension/debugging skill in a controlled one-hour setting) that is *consistent with* but does not *prove* Vella & Blincoe's field-reported flow/cognitive-load erosion and "supervisory work" reframing — different era-confidence (Shen is a clean E2 RCT; Vella & Blincoe is field self-report, era-unstratified), different outcome type (measured comprehension vs self-reported experience), no shared authorship or population. Triangulation value: medium, unchanged by the era correction — the two studies were already at different eras before the correction (E2 lab vs claimed-E3 field); now they're both more clearly pre-agentic/unstratified rather than one clean-E2-one-E3, which if anything *tightens* the era alignment between them rather than loosening it.
- **stanford-denisov-blanch (43-developer self-rated-vs-measured productivity-percentile miscalibration, "almost as good as flipping a coin"):** thematically adjacent (both RQ2, both about self-report reliability) but methodologically orthogonal — Stanford's finding is precisely the perception-vs-measured comparison Vella & Blincoe lack. The two together make a stronger combined RQ2 case than either alone: Stanford shows self-report is miscalibrated *against a measured score*; Vella & Blincoe shows self-report is internally *inconsistent even without* a measured score to be miscalibrated against. Recommend citing both in the RQ2/RQ6 synthesis memo as separate, mutually reinforcing cautions about single-item self-reported productivity metrics, not as one finding.
- **Bottleneck displacement (§5 tension 6):** the creation→verification balance-score shift (0.26→0.53, p=0.006) and "reviewing is the only task-focus item above neutral at both waves" are a genuine, independent (non-vendor, academic) practitioner-adjacent data point for the bottleneck-displacement story already built from Agoda/Faros/Zendesk/GitLab material — but it is a **self-reported time-allocation shift**, not a measured queue-depth, cycle-time, or review-load metric, so it is weaker evidence than that existing telemetry-based cluster. Treat as corroborating colour for tension 6, not a new load-bearing number.
- **DevEx framework overlap (space-dx-core4, already extracted):** Vella & Blincoe explicitly derive their developer-experience constructs (feedback loops, cognitive load, flow state) from the DevEx framework literature. Worth noting in RQ6 synthesis as an instance of DevEx-style constructs being operationalised as single Likert items in the wild — informative for the "what to instrument" question, i.e. a worked example of the trade-off between respondent burden and psychometric robustness that RQ6 will need to take a position on.

## Follow-up leads (not extracted)

1. **Online replication package** (referenced by the paper, not located this session) — would resolve the exact Likert-item wording for cognitive load/flow-state/productivity and the acknowledgements/funding text directly from source rather than via secondary confirmation.
2. **Vella's Master of Engineering thesis at Auckland** (probable underlying document, unconfirmed) — may contain fuller methodological detail, the full instrument, and possibly additional analyses not condensed into the arXiv preprint.
3. **DevEx framework primary sources** (Forsgren et al., already partially covered via space-dx-core4) — worth a direct pairwise comparison of how "cognitive load" and "flow state" are defined/operationalised across the two sources, for RQ6 instrument recommendations.
4. **Citation/critique tracking** — paper is ~1.5 months old at verification (22 May → 6 Jul 2026); no independent citations, critiques, or replications found via WebSearch. Re-check later in Phase 1/2 as the literature catches up.
5. **Annie Vella's other writing** (annievella.com; a "The Future of AI-Driven Software Engineering" ACM TOSEM 2025 piece surfaced in search) — possible companion/context piece by the same first author, not yet checked for overlap or additional data.
6. **Tool-modality re-analysis:** if the replication package includes a per-tool breakdown, it would let a future pass split findings by Copilot/ChatGPT vs Cursor and potentially recover a genuine E3-vs-E2 comparison from within this same dataset — currently not possible from the published aggregate figures.

## Recency check notes

Paper is ~6 weeks old at verification (22 May 2026 → 6 Jul 2026) — well within the 12-month threshold, so the CLAUDE.md mandatory recency search was not strictly triggered, but a light WebSearch check was run anyway given the ledger's high-priority queue flag. No retraction, errata, or independent replication/critique found. Only one arXiv version (v1) exists. Treat as current; re-check if a v2 appears or if citations accumulate.

## Ledger correction flagged for orchestrator

LEDGER.md's Queued-table line for this source currently reads era as "(B, E3)". Recommend updating to something like **"B, E1/E2-dominant (unstratified encroaching E3 — Cursor share only; no agentic framing in the paper itself)"** when this record is moved from Queued to Done, so the E3-evidence-share accounting in the DoD (§8) is not inflated by a source that does not actually isolate agentic-tool effects.
