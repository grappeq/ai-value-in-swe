# ghaleb-2026-fingerprinting — Ghaleb, "Fingerprinting AI Coding Agents on GitHub" (MSR '26)

**source_id:** ghaleb-2026-fingerprinting
**Date verified:** 2026-07-06 (remediation extraction, audit finding 7a — adjudicates whether this paper validates the AIDev attribution heuristic)
**RQs fed:** RQ2 (primary — measurement methodology: can agent attribution be trusted, and what would validating it require); indirectly every RQ that consumes AIDev-derived figures (RQ1/RQ3/RQ5 via `agents-vs-ides-2026`, `task-stratified-agents-2026`, `unreviewed-ai-prs-2026`, `review-agents-reality-2026`)

## Citation

Ghaleb, T. A. (2026). *"Fingerprinting AI Coding Agents on GitHub."* In *Proceedings of the 23rd International Conference on Mining Software Repositories (MSR '26)*, Rio de Janeiro, Brazil, 13–14 April 2026. ACM, 5 pages. arXiv:2601.17406v1 [cs.SE], submitted 24 Jan 2026. Single author. DOI stub still placeholder in the arXiv copy ("10.1145/nnnnnnn.nnnnnnn", "978-x-xxxx-xxxx-x") — same pre-camera-ready state as the AIDev MSR '26 paper itself. Replication package: https://github.com/Taher-Ghaleb/AIAgentsFingerprinting-MSR2026.

**Affiliation:** Taher A. Ghaleb, Department of Computer Science, **Trent University, Peterborough, Ontario, Canada** (taherghaleb@trentu.ca). Funding disclosed: **NSERC RGPIN-2025-05897** (Canadian federal research council — no vendor money).

**Independence from the Queen's AIDev lab — the decisive question, answered in two parts:**

1. **Institutionally: yes, distinct.** Trent University, not Queen's; Li/Zhang/Hassan are not authors; sole-authored.
2. **But not at arm's length historically.** The paper's own reference list contains a prior co-authorship between Ghaleb and **Ahmed E. Hassan** (AIDev's senior author): ref [15], Ghaleb, Da Costa, Zou & Hassan (2019), *"Studying the impact of noises in build breakage data,"* IEEE TSE 47(9) — cited, notably, as the paper's authority for "noise misleads empirical analyses." This is a paper-stated fact (the reference itself); the natural inference that Ghaleb is a former Queen's-orbit researcher (PhD-era collaboration with Hassan and Zou) is background inference, flagged as such. So: no current authorship overlap, but this is a former collaborator of the AIDev lab head analysing the AIDev lab's dataset — closer to "friendly neighbour" than "independent auditor."

## Verification status

**VERIFIED — full text read directly.** The arXiv PDF (584 KB) was fetched and converted with `pdftotext -layout` and read in full: all five pages, both results tables, the confusion-matrix figure text, threats to validity, related work, references, and the acknowledgments/funding line. Title, author, venue, and date cross-checked against the arXiv abstract page (consistent; v1 only, no revisions). No paywall; no abstract-only extraction anywhere in this record.

## Tier, era, independence

- **Tier: B.** Peer-reviewed (MSR '26, ACM), large-N (33,580 PRs), methodologically careful within its own frame (5-fold stratified CV, held-out-fold reporting, two-step feature-reduction with stated thresholds, per-class metrics, EPV checks, no SMOTE inflation). Not Tier A: it is a classifier study on observational labels with **no independent ground truth** (see the crux below), no causal question, and — for the purpose we care about — a circular validation design. A short 5-page paper, single-authored.
- **Era: E3.** The five agents fingerprinted (OpenAI Codex, GitHub Copilot agent mode, Devin, Cursor, Claude Code) are autonomous PR-submitting agents; the PRs are agentic-era artefacts.
- **Independence:** institutionally independent of Queen's, NSERC-funded, no vendor COI. Prior Ghaleb–Hassan co-authorship noted above. **Dataset independence: none — this paper is itself a member of the AIDev provenance cluster** (its entire empirical base is AIDev-pop; see below). It cannot serve as an independent triangulation leg for any AIDev-derived claim.

## Dataset & method

- **Data:** AIDev-pop, **Oct 28 2025 update** (a vintage detail not previously in our AIDev record — the 33,596-PR curated subset existed as a HuggingFace dataset update months before the Feb 2026 MSR paper describing it), 33,596 agentic PRs; 16 PRs dropped for incomplete commit metadata → **final N = 33,580**. Class distribution: OpenAI Codex 21,793 (64.9%), GitHub Copilot 4,967 (14.8%), Devin 4,822 (14.4%), Cursor 1,540 (4.6%), **Claude Code 458 (1.4%)**. Note the curated subset is far less Codex-dominated than the ~90%-Codex full corpus, but still heavily imbalanced.
- **Features:** 53 extracted across five categories — commit-message patterns (9: count, conventional-commit ratio, length stats, **multiline ratio**, capitalisation), PR structure (9: title/body length, checklists, code blocks, links, bullets), code changes (16: files changed, extensions, test/config/doc ratios, directory depth, operations, additions/deletions, change-concentration Gini), patch-level code (15: line counts/lengths, whitespace, indentation, comment/import density, functions/classes/conditionals/loops), temporal (4: hour, weekend/business-hours, day of week). Reduced to **41** via correlation clustering (|r| ≥ 0.70) plus R² > 0.90 redundancy analysis. Feature reduction costs only 0.2pp F1 (97.4% → 97.2%).
- **Models:** multi-class XGBoost (max depth 6, 100 estimators) and Random Forest (depth 10), 5-fold stratified CV, performance reported on held-out folds only; SMOTE tried and rejected (distorted the natural distribution). One-vs-rest binary XGBoost per agent for agent-specific feature importance.
- **Ground truth — THE CRUX:** the agent labels are **AIDev's own labels**, i.e. the output of the very branch-prefix / bot-account / co-author-trailer heuristic our evidence base needs validated. There is **no manual audit of any PR's true authorship, no independently-collected labelled sample, no self-disclosure cross-check, no external label source of any kind**. The 5-fold CV holds data out from the *model*, not from the *labelling process* — every "ground-truth" label in every test fold was produced by the same unvalidated heuristic.

## Key findings — exact numbers

### RQ1 (theirs): agent identification performance (XGBoost, 5-fold CV, Table 2)

| Agent | N | Precision | Recall | F1 |
|---|---|---|---|---|
| OpenAI Codex | 21,793 | 0.99 | 0.99 | 0.99 |
| GitHub Copilot | 4,967 | 0.99 | 0.98 | 0.99 |
| Devin | 4,822 | 0.93 | 0.96 | 0.94 |
| Cursor | 1,540 | 0.88 | 0.83 | 0.85 |
| **Claude Code** | **458** | **0.82** | **0.57** | **0.67** |
| Weighted avg. | 33,580 | 0.97 | 0.97 | 0.97 |

- Headline **97.2% F1** (XGBoost; Random Forest 94.9%). **This is the weighted average, dominated by the 64.9% Codex class.** The macro-average F1 across the five classes is ~0.89 by arithmetic on Table 2 — see internal-consistency note below.
- **Claude Code recall is 57%**: 137 of its 458 PRs are misclassified as Devin and 28 as Codex. Cursor is confused with Codex (121) and Devin (113). The two locally-run tools — exactly the pair AIDev's own authors flag as underrepresented — are the classifier's two weakest classes.
- Fold-to-fold F1 variance ±0.1%.

### RQ2 (theirs): what distinguishes agents

- Global importance: **commit-message characteristics dominate — multiline commit ratio alone 44.7%**, change-concentration Gini 10.1%, average commit-message length 2.3%. Code-content features rank low: *how agents communicate changes is more distinctive than what they change.*
- Agent signatures (one-vs-rest): Codex — multiline commit messages (67.5%); Copilot — long PR bodies (38.4%), change concentration (24.9%); Cursor — bullet points (17.2%), links (12.8%); Devin — multiline commits (48.9%), distributed file changes (8.2%); Claude Code — conditional density (27.2%), comment density (19.8%).
- Contrast with human code-stylometry literature (their ref [7]): for humans, code style dominates attribution; for agents, version-control/communication conventions do. Behaviourally plausible — and also exactly what one would expect if the labels themselves derive from version-control metadata conventions (see leakage note below).

### The paper's own view of AIDev

The implications section explicitly argues AIDev's **"human" comparison set (6,618 PRs) is plausibly contaminated** by undisclosed agent use, "introducing noise that can mislead empirical analyses on code quality, bug density, or development velocity," and tells researchers to "(1) apply fingerprinting to validate labels, (2) note contamination as a limitation, or (3) use pre-agent datasets." So the paper itself treats AIDev's labels as suspect on the human side while consuming them as ground truth on the agent side.

## Nulls, gaps and negative results

1. **The advertised use case is untested.** The abstract/conclusion claim the method enables "detection of… human-submitted PRs with agent-generated code," but the paper never applies the classifier to a single human-account PR with known agent involvement — that validation is explicitly deferred: "Future work includes… validating on human-submitted PRs containing agent-generated code to test provenance claims." The classifier has only ever been scored on PRs the AIDev heuristic already caught.
2. **No estimate of AIDev's attribution precision or recall against true authorship** — the one number our evidence base needs remains unmeasured.
3. Temporal stability untested (cross-sectional; no time-split validation — the author names this).

## Limitations

**Author-stated (§4):** fingerprints may drift as agents evolve (no temporal validation); class imbalance drives Claude Code's 57% recall; public-GitHub-only, no private repos or other platforms; adversaries could mimic patterns.

**Inferable, not stated:**

1. **Circular ground truth** (the crux, above): the design can measure *label recoverability* — how well 41 behavioural features reconstruct AIDev's heuristic labels — but not *label accuracy*. Systematic heuristic errors are invisible to it: a false positive that entered AIDev via a `codex/` branch prefix would very likely carry Codex-like metadata and be "correctly" classified as Codex; a real agent PR the heuristic missed is absent from both train and test sets and can never be scored as a false negative.
2. **Possible feature–label leakage, undiscussed:** AIDev labels Claude Code via the "Co-Authored-By: Claude" trailer *in commit messages*, and Devin via bot-account authorship — while the classifier's dominant features are commit-message length/multiline statistics. Whether trailers were stripped before feature extraction is never stated. If not, part of the separability is the labelling signal echoing through the features rather than genuine behavioural signature. (Claude Code's *low* recall despite the trailer suggests the literal string was not exploited, but the paper leaves this unexamined.)
3. **The selection problem is untouched:** agents used locally whose output reaches GitHub without the heuristic's signatures (disabled trailer, renamed branch, squash-merge, human-account submission) are absent from the training population entirely. A classifier trained only on disclosed usage cannot certify anything about undisclosed usage — the paper's governance framing quietly assumes fingerprints generalise from disclosed to undisclosed populations, which is untested.

## What this can and cannot support

**Can support:** (a) the methodological point that agentic tools leave strong, machine-detectable *communication-style* signatures (commit-message and PR-structure conventions) that differ sharply by vendor — useful for RQ2/RQ6 as evidence that "AI-generated %" instrumentation keyed to metadata conventions is fragile and vendor-specific; (b) weak, indirect corroboration that AIDev's five label classes are *internally coherent* — the labelled populations are behaviourally separable on features largely distinct from the labelling signals, which is more consistent with the heuristic capturing five real, distinct tool populations than with heavy random cross-contamination; (c) a documented, citable statement (from within the MSR community itself) that AIDev's human/agent boundary is unvalidated and its "human" set plausibly contaminated.

**Cannot support:** any precision/recall claim about AIDev's attribution heuristic against true authorship (not measured); any claim that undisclosed agent usage can currently be detected at a known accuracy (untested); any claim about local-first Cursor/Claude Code usage (blind spot inherited wholesale, and the classifier is weakest on exactly those two classes); any triangulation leg for AIDev-derived findings (same dataset, same provenance cluster).

## Cross-ref adjudication (for orchestrator review — nothing else edited)

**Question:** does this paper validate the AIDev attribution heuristic well enough to relax the one-voice cap on `agents-vs-ides-2026` / `task-stratified-agents-2026` / `unreviewed-ai-prs-2026` / `review-agents-reality-2026`?

**Verdict: NO — HOLD the cap. The validation is circular, not independent.**

1. **What "validation" would have required:** ground truth for agent authorship established *outside* the heuristic — a manually audited PR sample, self-disclosure surveys, vendor telemetry, or at minimum labels from a second, differently-constructed detector. Ghaleb's ground truth is AIDev's own heuristic output, wholesale. The 97.2% F1 therefore measures how well behavioural features *reproduce the heuristic's decisions*, not how often the heuristic's decisions are *correct*. Held-out folds are held out from the model, not the labelling process. This is a consistency check, not a validation.
2. **What it genuinely adds (small, real):** the five labelled populations are behaviourally coherent and separable on 41 features mostly orthogonal to the detection signals — mild comfort against a *gross-contamination* failure mode of the heuristic (if AIDev's classes were heavily polluted with random misattributions, near-perfect majority-class separation would be less likely). It says nothing about systematic errors, which would replicate faithfully through this design.
3. **What it cannot fix and does not claim to fix:** the self-disclosure selection problem. AIDev only ever contained agent PRs that left a discoverable signature; Ghaleb trains and tests only on that population. Non-disclosing usage (disabled Claude trailer, renamed Codex branch, agent output pushed from a human account and workflow) is absent from both the dataset and the evaluation — no classifier evaluated only on the disclosed population can bound the undercount. Indeed the paper *deepens* the concern in one direction: it argues AIDev's 6,618-PR "human" baseline is itself plausibly agent-contaminated, which mildly *worsens* the position of any dependent source using AIDev's human set as a comparison group (`unreviewed-ai-prs-2026`'s RQ2 human baseline; noting that source's authors already manually removed 1,044 bot/agent PRs from it, partially anticipating this).
4. **Cluster membership, not cluster audit:** Ghaleb runs on the identical 33,596-PR (→33,580) AIDev-pop bundle and therefore *joins* the AIDev provenance cluster rather than auditing it from outside. Combined with the prior Ghaleb–Hassan co-authorship, this source should be counted as another voice *inside* the cluster for §3 purposes.
5. **One asymmetric detail worth carrying forward:** the classifier is near-perfect on Codex/Copilot/Devin (F1 0.94–0.99) but weak on Cursor (0.85) and poor on Claude Code (0.67, recall 0.57) — the confusability of the locally-run tools' *disclosed* PRs with other agents adds a small extra caution against any downstream cross-agent comparison that leans on Cursor/Claude Code rates specifically (e.g. per-agent acceptance-rate gradients in `task-stratified-agents-2026` and Rahman et al. when extracted).
6. **Net recommendation:** keep the one-voice triangulation cap on the AIDev cluster exactly as recorded in `aidev-dataset-2026`; add Ghaleb to that cluster's membership list; cite Ghaleb, if at all, as (a) methodology evidence for RQ2/RQ6 on the fragility of metadata-based AI-attribution metrics and (b) the in-community statement that AIDev's labels are unvalidated — never as an independent validation of them. The genuine validation study our evidence base wants (heuristic labels vs manually-audited or externally-disclosed ground truth) still does not exist as of this check.

## Follow-up leads (not extracted)

- Tian et al. (2023), arXiv:2304.11938 (ref [24]) — 93% accuracy separating ChatGPT-generated from human code via perplexity/burstiness; the *code-level* (not metadata-level) detection line that could, in principle, be combined with behavioural fingerprinting for a non-circular check.
- Bisztray et al. (2025), "I Know Which LLM Wrote Your Code Last Summer" (AISec workshop, ref [3]) — LLM code stylometry for authorship attribution; same potential use.
- Golzadeh et al. (2022), "On the accuracy of bot detection techniques" (ref [17]) — the bot-detection accuracy literature is the nearest existing template for what a real AIDev-heuristic audit would look like.
- Replication package (features, scripts): https://github.com/Taher-Ghaleb/AIAgentsFingerprinting-MSR2026 — would allow re-running the classifier with commit-trailer/metadata features ablated, the cheapest available probe of the leakage question in inferable limitation 2.

## Notes on internal consistency

§2.4.2 states "We report macro-averaged precision, recall, and F1-score," but the headline 97.2% matches Table 2's **weighted** average (macro F1 from the per-class figures is ~0.89: (0.99+0.99+0.94+0.85+0.67)/5). The abstract and conclusion quote 97.2% without the "weighted" qualifier. Not a substantive error — Table 2 discloses everything — but anyone citing "97.2% F1" should say *weighted* F1, majority-class-dominated, with Claude Code at 0.67. Recorded because the AIDev provenance record (`aidev-dataset-2026`) relayed the abstract's "97.2% F1" without this qualifier, reasonably, as full text had not then been read.

## Recency check notes

Submitted 24 Jan 2026; verified 2026-07-06, ~5.5 months old — inside the CLAUDE.md rule 8 twelve-month threshold, so no dedicated supersession search was required. MSR '26 (13–14 April 2026) has taken place; this is a peer-reviewed, conference-accepted version (arXiv copy pre-dates final DOI substitution). v1 only; no erratum or critique surfaced during verification.
