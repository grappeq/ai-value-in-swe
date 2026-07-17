# Independent Review — outputs/internal-measurement-proposal.md and outputs/follow-up-questions.md

**Reviewer role:** independent, not involved in production. Checked against sources/*.md, evidence/evidence-table.tsv, synthesis/*.md (RQ memos, tension verdicts, contradictions.md, rederivation-r1.md, rederivation-r3.md), LEDGER.md, PROTOCOL.md. Cross-checked against outputs/exec-brief.md where the task required it. No edits made to the reviewed outputs; no git commands run.

Method note: every quantitative or attributable claim in both documents was traced to its source record via Grep + full-text read. Findings below are only the ones that failed verification, were imprecise, or created inconsistency — a large majority of claims checked out exactly (he-2026's 89%→68%/2.0×/+22%/9-month figures, the d=0.738 skill finding, the METR <44% acceptance and 47% LOC figures, the Uber leaderboard/spend figures, the Stanford 350-engineer PR+14%/rework 2.5× figures, the "time to first review comment" mechanism, the corruption count and source-count headers, the "Six things to track" and DoD adopt/reject-count structure) and are not repeated here.

---

## Findings

### 1. [BLOCKER] Agent PR rejection stat inverted: a confirmed floor is presented as a confident ceiling

**Text at issue** (`outputs/internal-measurement-proposal.md`, reject-metric #8):
> "Agent PR merge/rejection rate — in the largest open-source data, **at most a third** of rejected agent PRs actually failed for code reasons; the rest died of process (nobody reviewed them, duplicates, silent closes)..."

**What the record says** (`sources/agentic-pr-merge-reject-2026.md`, finding F1):
> "Of 353 manually-coded rejected PRs, only 126 (**35.7%**) reflected a clear, observable agentic failure... 117 (33.1%) had no observable decision rationale at all ('Unknown'...). **Cannot support:** a claim about the *true* underlying agentic failure rate, since the 33.1% 'Unknown' bucket is large and conservatively assigned — **the true AF share could be anywhere between 35.7% and ~69%** depending on how Unknowns resolve."

35.7% is the paper's own stated *floor* (confirmed, observed failures only); the paper explicitly declines to put a ceiling on it and flags that the ceiling could be roughly double the floor. "At most a third" claims the opposite — a confident upper bound — which is not what the source supports. The proposal also collapses two of the paper's three categories ("Non-Agentic Failure" 31.2%, i.e. process, and "Unknown" 33.1%, i.e. no recorded reason at all) into a single "died of process," when the paper deliberately keeps them separate because Unknown could hide further agent failures.

**Why it matters:** this sits inside the proposal's own reject-metrics list, i.e. it is being used to justify a concrete instrumentation decision (don't trust raw agent-PR merge/rejection rate). Getting the direction of the uncertainty backward changes the message from "we can't rule out that most rejections are real agent failures" to "we know most rejections aren't" — the opposite epistemic stance, on a load-bearing evidence-rule point (CLAUDE.md rule 1: never state an effect size without a source_id that actually supports the stated bound).

**Suggested fix:** "...only about a third of rejected PRs show a *confirmed* code-level failure — and because a third of cases have no recorded reason at all, the true failure share could be as high as two-thirds. Most of the rest are process closures (duplicates, abandoned work) or simply unexplained."

---

### 2. [MAJOR] Same inversion, milder framing, in follow-up-questions.md

**Text at issue** (`outputs/follow-up-questions.md`, item 8):
> "rejections are coordination-dominated (**≤36% agent failure**)"

**What the record says:** as above — 35.7% is a floor, not a ceiling; source explicitly states the true share "could be anywhere between 35.7% and ~69%."

This phrasing is inherited verbatim from `synthesis/rederivation-r3.md` ("≤36% of rejections are agent failures") and `synthesis/contradictions.md`'s T6 index entry (same "≤36%"), so the error originates upstream in the R3 synthesis step, not in follow-up-questions.md itself — but it is carried into the output uncorrected, and a reader of follow-up-questions.md has no way to know the "≤" is backward without pulling the primary source.

**Suggested fix:** change "≤36%" to "only a confirmed 35.7% (true share uncertain, could run to ~69%)" here and propagate the correction back to rederivation-r3.md and contradictions.md's T6 entry, since both currently carry the same inversion.

---

### 3. [MAJOR] Skill-erosion caveat understates that *both* underlying studies are pre-agentic

**Text at issue** (`outputs/internal-measurement-proposal.md`, closing "Honest limits" section):
> "The skill-erosion check (#6) rests on deliberately thin evidence — two studies, found incidentally, **one of them from the pre-agent era** — because we chose not to do a full evidence sweep on that theme."

**What the record says** (`synthesis/rq6-measurement.md`, metric #8 row, evidence column):
> "`shen-2026-coding-skills`: d=0.738 comprehension loss with no speed offset; `vella-blincoe-2026`: self-reported productivity and self-reported experience are statistically decoupled... **Both are E2/self-report-only evidence**; treat as sentinel checks, not magnitude evidence..."

Per LEDGER.md's own era tags: shen-2026-coding-skills = "E2 chat — NOT agentic; era-transfer caveat applies"; vella-blincoe-2026 = "E1/E2-dominant, unstratified encroaching E3 — NOT confirmed E3." Neither source is agentic-era. Saying "one of them" is pre-agent implies the other is not — the natural reading is that one study is agentic-era corroboration, which does not exist. This is precisely the kind of era-mislabelling PROTOCOL §2 is written to prevent ("Every effect-size claim... must rest on E3-era evidence or carry an explicit 'pre-agentic' label"), and it appears in the one paragraph of the proposal whose entire job is to state the limits honestly.

**Suggested fix:** "...two studies, found incidentally, **both from before the agentic era** — because we chose not to do a full evidence sweep on that theme."

---

### 4. [MAJOR] "3% regression, twice, seven months apart" attaches one incident's magnitude to both incidents

**Text at issue** (`outputs/follow-up-questions.md`, item 3(c)):
> "Detectability — the new blocker: Anthropic itself failed to detect **a 3% quality regression** via internal evals, **twice, seven months apart**; detection was user complaints both times."

**What the record says** (`sources/anthropic-postmortem-quality.md`):
> Sept 2025 incident: infrastructure bugs affecting the Claude API, magnitude reported as "peaked at 16% of Sonnet 4 requests at worst; ~30% of Claude Code users reportedly hit at least one degraded response overall."
> April 2026 incident: three separate product-layer issues; **only one of the three (the verbosity-limit change) has a quantified figure: "a 3% quality drop for both Opus 4.6 and 4.7 — the only quantified effect size in the postmortem."**

The 3% figure belongs to one sub-issue inside the April 2026 postmortem only. The September 2025 incident, seven months earlier, had a different and much larger reported magnitude (16%/30%), not 3%. What genuinely recurred twice, seven months apart, is the *pattern* (evals missed user-perceived degradation; user complaints were the detection channel) — not the specific 3% figure. This same conflation appears in `synthesis/rederivation-r3.md` ("Anthropic itself could not detect a 3%-magnitude Claude Code quality regression through internal evals in two postmortems seven months apart") and in `LEDGER.md`'s R3 gate summary ("Anthropic's own evals missed a 3% regression twice") — an upstream synthesis error that follow-up-questions.md inherits uncorrected.

**Suggested fix:** "Anthropic failed to catch user-perceptible quality regressions via internal evals twice, seven months apart (Sept 2025: ~16-30% of requests/users affected; Apr 2026: three issues, one quantified at a 3% drop) — detection was user complaints both times."

---

### 5. [MAJOR] "Doubled in three months" — timeframe not present in the source record

**Text at issue** (`outputs/internal-measurement-proposal.md`, metric #5):
> "Expect consumption to grow at constant prices (**one vendor's own per-day estimate doubled in three months**)."

Same claim, same wording pattern, appears in `outputs/exec-brief.md`: "Anthropic's own per-day cost estimate doubled in three months with no price change."

**What the record says** (`sources/ai-spend-landscape-2026.md`, item 3):
> "average $13/developer/active day... The **estimate silently doubled (~$6→$13/day) in April 2026**, attributed by Anthropic to Opus 4.7 usage patterns with 'no pricing change'..."

The source states the doubling happened "in April 2026" but never gives a start date for the prior ~$6/day figure, so "three months" cannot be traced to this record (or to `synthesis/rq4-cost-profile.md`'s addendum, which uses the same undated phrasing: "its own per-day estimate silently doubling in Apr 2026"). This may well be accurate (Anthropic's docs pages typically carry a "last revised" date), but as written it is a specific, quantified claim with no source_id behind the specific number, which is exactly what CLAUDE.md rule 1 prohibits.

**Suggested fix:** either locate and cite the prior revision date, or soften to "doubled within months" / "doubled by April 2026, from an undated earlier baseline."

---

### 6. [MAJOR] Cross-document count mismatch: "Nine metrics to refuse" vs exec-brief's "eight"

**Text at issue** (`outputs/internal-measurement-proposal.md`, section header and list): "## Nine metrics to refuse" — list runs 1–9 (LOC, commit/PR counts, suggestion acceptance, "% AI-generated," token/usage volume, self-reported multipliers, "time to first review comment," agent PR merge/rejection rate, any single number). Count verified: **nine**, correctly matching its own header.

**What the companion document says** (`outputs/exec-brief.md`, "What we should do" section):
> "The companion proposal lists six things to track and **eight popular metrics to refuse**."

**What the ground truth says** (`synthesis/rederivation-r3.md`, section D, "Output revisions applied"):
> "internal-measurement-proposal.md: **reject metric #9** (raw agent-PR merge rate)..."

R3 explicitly added a ninth reject-metric to the proposal and recorded doing so — but the corresponding count in exec-brief.md's summary line was not updated from eight to nine. The proposal itself is internally correct; the inconsistency sits in the companion document, but it is precisely the kind of cross-document contradiction the review brief asked to be checked (proposal numbers must not contradict the exec brief's), and a reader moving between the two documents will hit a direct numeric conflict on the headline count of the proposal's own reject list.

**Suggested fix:** update exec-brief.md's "eight popular metrics" to "nine."

---

### 7. [MINOR] "9 months to peak" overstates what he-2026 shows, and is offered as support for a pattern the source explicitly says is unproven

**Text at issue** (`outputs/internal-measurement-proposal.md`, pilot design section):
> "Expect things to get worse before better — but verify it. The 'dip then rise' story is plausible (**the best study took ~9 months to peak**) but no one has actually proven the rise follows the dip."

**What the record says** (`sources/he-2026-2x-mandate.md`, finding 2):
> "...rising to **1.99× by nine months on tool** in the month-by-month event study."

Two issues: (a) "nine months to peak" implies a plateau was reached and observed; the source only reports the value at the nine-month mark, which is close to the maximum horizon the data allows (Claude Code telemetry starts Jul 2025; the panel ends Apr 2026) — nothing in the record shows growth stopping there rather than data simply running out. (b) he-2026's event study shows a monotonic step-up after adoption with no dip at all (flat pre-adoption trend, then rising) — it is evidence for the "rise," not for any "dip." Citing it in parentheses right after "the dip then rise story is plausible" reads as partial evidential support for the dip, when `outputs/follow-up-questions.md` item 9 (drawing on the same evidence base) is explicit that no dip has ever been observed anywhere: "Nothing in R3's 20 sources shows dip-then-recovery in any organisation's own longitudinal data... demonstrated nowhere." The proposal's own hedge ("no one has actually proven the rise follows the dip") is honest, but the parenthetical it's attached to muddies exactly that point.

**Suggested fix:** separate the two claims — "Gains can keep compounding for months (the best-documented company was still climbing at the nine-month mark, the longest window measured). Whether there's an initial *dip* before that rise is a different, unproven claim — no source in this research shows one."

---

### 8. [MINOR] "differ 2× for workflow reasons alone" is an approximation not directly reported by the source

**Text at issue** (`outputs/internal-measurement-proposal.md`, reject-metric #8):
> "...and per-agent rates differ 2× for workflow reasons alone."

**What the record says** (`sources/agentic-pr-merge-reject-2026.md`, F3): Codex 47.8% vs Devin 24.2% "Agentic Failure" share among rejections (≈1.97×); Non-Agentic-Failure ("workflow") share: Devin 45.1% vs Codex 16.8% (≈2.68×). No sentence in the source or in `synthesis/rederivation-r3.md` ("per-agent rates driven by process signatures") states a "2×" figure. The closest matches to "2×" and to "workflow reasons" belong to different pairs of numbers (2.0× is the *agentic-failure* ratio, not workflow; the *workflow*/Non-Agentic-Failure ratio is closer to 2.7×).

**Suggested fix:** either cite the specific ratio precisely ("Codex's confirmed failure share is roughly double Devin's; process-driven rejections vary even more, up to ~2.7× between agents") or drop the specific multiplier and keep the qualitative point (large, inconsistent per-agent variation).

---

### 9. [MINOR] "T8 gained its first substantial evidence in R3" overstates the prior gap

**Text at issue** (`outputs/follow-up-questions.md`, item 5):
> "T8 (debugging/incident response) **gained its first substantial evidence in R3** — but lab-only, non-frontier models, no human baseline..."

**What the record says** (`synthesis/rq1-value-map.md`, task-type table, pre-R3):
> "T8 Debugging/incident response | **Emerging** | Zalando: analysis days/weeks→hours (C, E2 pipeline)... task-stratified-agents-2026: Devin weaker on fix tasks (45.6% vs Codex 83.0%) | Positive for augmented RCA; unresolved for autonomous"

T8 was already tagged "Emerging" (distinct from T1/T2/T9's "None — task-share only") before R3, on the strength of zalando-2025-postmortems and task-stratified-agents-2026. Grouping T8 with the genuinely dry T1/T2/T9 in the same sentence, and calling rca-failures-2026 the type's "first substantial evidence," overstates the prior gap; rca-failures-2026 is better characterised as the first *rigorous lab* evidence, layered on top of existing thin practitioner/observational T8 evidence.

**Suggested fix:** "T8... gained its first *controlled/lab* evidence in R3 (on top of existing thin practitioner evidence) — but lab-only, non-frontier models, no human baseline..."

---

### 10. [MINOR] Terminology drift: "agent-failure episodes" vs the source's own "misalignment episodes"

**Text at issue** (`outputs/follow-up-questions.md`, item 3): "0.07% hard-to-reverse episodes in **16k validated agent-failure episodes**."

**What the record says** (`sources/dev-agent-misalignment-2026.md`): "16,118 of 29,896 (53.9%) as **validated [misalignment] episodes**." The paper's own construct is developer-agent *misalignment*, not "agent failure" — a related but not identical category (misalignment can include cases the developer corrected without the agent having "failed" in a code-correctness sense). The number (16,118 ≈ "16k") is accurate; the label attached to it has drifted.

**Suggested fix:** "16k validated misalignment episodes."

---

### 11. [MINOR] Uber "~10% of code is agent-submitted" cited without its own flagged uncertainty

**Text at issue** (`outputs/follow-up-questions.md`, item 11): "...~10% of code is agent-submitted, and the COO still says token spend doesn't map to shipped features."

**What the record says** (`sources/uber-2026-claude-cost.md`): the "~10% of committed code built by autonomous agents" figure is explicitly logged as a "CEO figure (possible discrepancy)... unclear whether this is meant to restate the ~11% backend-agent figure... or is a genuinely separate, lower estimate... flagged here as an unresolved cross-outlet inconsistency, not silently reconciled." Follow-up-questions.md states the figure as settled context; the source treats it as unresolved.

**Suggested fix:** add "(a figure the source itself flags as an unresolved cross-outlet inconsistency)" or use the better-attested 11% backend-agent figure instead.

---

## Editorial / readability observations (no severity — style, not correctness)

- `internal-measurement-proposal.md` reads well against the "plain words, point-first" bar: short declarative openers, concrete numbers, no hedging theatre, consistent British spelling (licence, organisation, labelled). One dense spot: the spend row (#5 in "Six things to track") packs four dollar ranges and two asides into one cell — a reader has to stop and re-parse it. Consider splitting the seat-vs-token comparison from the consumption-growth aside.
- `follow-up-questions.md` is written in a dense, acronym-heavy internal register (DiD, CS-DiD, TWFE, PSM, Callaway–Sant'Anna, g=/d=/ρ= notation) that would not clear the exec-brief's "non-engineer, five minutes" bar. This is very likely fine, since the document's own header calls it "planning material, not findings" for the research team's own use — but if it is ever handed to the same non-engineer audience as the exec brief, it will not be readable in its current form. Worth an explicit one-line audience note if that risk exists.

---

## Per-document verdicts

**`outputs/internal-measurement-proposal.md` — GO-WITH-FIXES.** Structurally strong (nine reject-metrics genuinely nine, six adopt-metrics faithfully consolidated from the eight RQ6 candidates, correct handling of the maintainability-metric feasibility gap, correct and precise use of the he-2026 bottleneck figures, the METR acceptance-rate figure, and the Stanford/350-engineer rework figures). One BLOCKER (finding 1) inverts a source's own stated confidence bound and should not stand as written; three further MAJOR findings (3, 5, 6) need correction before this is treated as final. Fix findings 1, 3, 5, 6 before distribution; the MINOR items (7, 8) are worth a pass but don't block.

**`outputs/follow-up-questions.md` — GO-WITH-FIXES.** Internally consistent with `synthesis/rederivation-r3.md` almost everywhere checked (Q1, Q6, Q7, Q9, Q12, Q13 all trace cleanly), and the header counts (74 sources, 362 findings, 20 R3 sources, 155 rows) all check out exactly. Its problems are inherited rather than invented: findings 2 and 4 are both R3-synthesis-level errors (the ≤36% inversion and the 3%-twice conflation) that were carried from `synthesis/rederivation-r3.md` and `LEDGER.md` into this output without being caught — worth fixing at the synthesis layer too, not just here, since other documents (contradictions.md, LEDGER.md) currently repeat the same errors. Findings 9, 10, 11 are minor precision/terminology slips. None of this undermines the document's core function as a research-continuity record.
