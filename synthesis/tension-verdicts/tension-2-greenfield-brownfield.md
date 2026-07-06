# Tension 2 — Greenfield vs. Brownfield Split

## 1. The tension as pre-registered

PROTOCOL §5.2: "Early Copilot RCTs (Peng et al. 2023, ~55% faster) used standardized greenfield tasks; telemetry work (e.g., Stanford / Denisov-Blanch) suggests gains concentrate in low-complexity/greenfield code and shrink toward zero or negative in complex legacy systems. This is the crux of RQ5."

## 2. Strongest evidence for the split

- **peng-2023-copilot-rct** — Tier A (vendor-COI-flagged), E1, greenfield contrast anchor: 55.8% measured completion-time reduction on a standardised, no-context task (95% CI [21%, 89%]).
- **stanford-denisov-blanch** — Tier B, E1/E2-dominant-mixed, talk-grade (unpublished, no CIs, n=136 teams/27 companies): quadrants greenfield-low-complexity +30–40%, greenfield-high-complexity +10–15%, brownfield-low-complexity +15–20%, brownfield-high-complexity 0–10%.
- **he-2026-2x-mandate** — Tier A, E3, single firm: +44% (significant) in post-2022 repos vs +12% (n.s.) in pre-2022 legacy repos — an objective repo-age operationalisation, but **not independent** of Stanford (shared co-author Denisov-Blanch).
- **metr-2025-rct** — Tier A, E3/early-boundary, independent of the above cluster: −19% measured slowdown on mature, highly familiar, 1M+ LOC repos — the brownfield-negative pole, though a single population/task-design with no greenfield arm of its own.

## 3. Complications and counter-evidence

- **google-rct-2024** — Tier A candidate, E1/E2, single-firm-COI: a genuinely brownfield T4 task (editing an existing 10-file/474-line changelist inside Google's internal stack) found a ~21–26% speedup (one covariate spec significant p<.05, the preferred spec NS, p=.086). This is a **brownfield positive**, undercutting any claim that brownfield reliably nets to zero — even pre-agentically.
- **agents-vs-ides-2026** — the IF-cohort reversal (−35% commits, −61% LOC by month 6) is a moderator of *prior AI-IDE exposure*, not of codebase maturity; repos aren't split by age/complexity at all. Rival explanation: part of what reads as a "brownfield penalty" elsewhere may really be a tooling-novelty/exposure effect, which this source shows operates independently of maturity.
- **cursor-velocity-quality-2025** — explicitly reports no repo-age/size heterogeneity; repo age is a matching covariate only, never an analysed moderator. Must not be cited for this tension (confirmed by its own record).
- **task-stratified-agents-2026** — its task axis is kind-of-change (feat/fix/docs/chore…), not codebase maturity; all 7,156 PRs come from established ≥100-star OSS repos with no within-sample maturity contrast constructed. Must not be cited either (confirmed by its own cross-ref note).
- **Construct instability:** "brownfield" is operationalised at least four different ways — Stanford's self-reported team complexity/greenfield classification; he-2026's objective repo-creation-date cohort; METR's familiarity/size/age of the maintainer's own large OSS repo; agents-vs-ides's prior-tool-exposure proxy (not maturity at all). These correlate loosely but are not the same construct, so a single "brownfield discount" figure cannot be quoted across sources.

## 4. Era audit

The quantitatively strongest evidence is either E1/E2 (Stanford's quadrant, built on 2022–2025 telemetry dominated by autocomplete/chat) or single-firm E3 (he-2026) that shares an author with Stanford. METR is independent E3(-boundary) but supplies only the brownfield-negative pole, with no matched greenfield arm in the same design. **No independent, multi-firm E3 dataset reproduces the full quadrant.** Honest conclusion: independent E3 evidence for the *split as a pattern* — as opposed to isolated brownfield-negative or greenfield-positive data points — is thin to absent.

## 5. Independence audit

stanford-denisov-blanch and he-2026-2x-mandate share Denisov-Blanch; he-2026's own record explicitly disclaims this as "not an independent replication... same research group's output on a different dataset." agents-vs-ides-2026 and cursor-velocity-quality-2025 add the same CMU lab (He, Agarwal, Vasilescu) into the mix — three of the newer E3 sources trace to one lab. What remains genuinely independent: metr-2025-rct (independent non-profit), google-rct-2024 (Google-only), peng-2023-copilot-rct (Microsoft/GitHub) — three distinct organisations, but all either pre-agentic or single-population.

## 6. Verdict

**Contested on magnitude and mechanism; not contested on direction.** Confidence: **medium**. Every source measuring a greenfield/brownfield-style contrast (Peng vs. METR; Stanford's own quadrant; he-2026's repo-age split) points the same way — value concentrates where context is smaller, newer, or less encumbered — and no source shows brownfield outperforming greenfield. But the two sources that quantify the split most directly (Stanford, he-2026) are not independent of each other; google-rct-2024 shows a real brownfield task producing a positive result, so "brownfield ≈ zero" is not universal even pre-agentically; and "brownfield" is measured four incompatible ways, so no single effect size travels across the evidence base. What can be claimed: the *direction* is robust across eras, designs, and labs. What cannot be claimed: a precise magnitude, or that codebase age/complexity — rather than developer familiarity, tool novelty, or task scoping, all confounded here — is the actual mechanism. For RQ5: this supports "local speedup shrinks as context grows" as a real, high-confidence directional finding, but any exec claim of a specific brownfield discount percentage would overstate what the (largely non-independent, largely E1/E2) evidence base can bear.

## 7. What would change the verdict

An independent (non-CMU/Stanford) multi-firm E3 study replicating a repo-age or complexity moderator with objective measures; a brownfield RCT using genuinely agentic tooling (Google's was E1/E2); or a design that cleanly separates codebase maturity from tool-exposure novelty (the agents-vs-ides-2026 confound) would materially sharpen this.

## 8. Feeds exec brief as

AI's gains are real but shrink as codebase context grows — the size of that shrinkage, and whether it stems from the code's age or the team's inexperience with the tool, is not yet settled by independent evidence.
