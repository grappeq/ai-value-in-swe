# Re-derivation after refresh cycle R3 (2026-07-17)

Pre-registered method (LEDGER, R3 header): after all R3 extractions land, affected open-question statuses, tension verdicts, and memos are re-examined against the FULL refreshed table (362 rows, 74 sources), asking "what would we conclude from scratch?", not "does the new source fit?". Movements below; outputs revised last. R3 added 20 sources (R3.1–R3.4) and 155 rows.

## A. Movements on the open questions (outputs/follow-up-questions.md — statuses applied there)

**Q1 (−19% vs 1.5–1.7×) → PARTIALLY ANSWERED.** From scratch, the corridor is now explicit and the reconciliation is no longer mysterious:
- Floor: METR's own late-2025 re-run erases the slowdown — point estimates −18% time (n=10, CI [−38,+9]) and −4% (n=47, CI [−15,+9]), both non-significant, self-read by METR as a *lower bound* on quantified selection effects (30–50% task refusal without AI). METR is abandoning the design; no clean RCT anchor will come from that channel (metr-2026-design-change, B).
- Ceiling: METR's transcript analysis models a soft upper bound of 1.5–13× (n=7, LLM-judge counterfactual; metr-2026-transcript-bound, C).
- he-2026's causal 1.46–1.72× sits inside this corridor; the meta-analysis setting gradient (lab g=0.73 / enterprise 0.19 ns / OSS 0.01 ns; genai-productivity-meta-2026, A) independently shows effect sizes are setting-dependent, which is the same lesson at pool level.
- Verdict: the two famous numbers are not in contradiction — they sit at different points of (tool generation × setting × horizon × selection). What remains missing is any *significant* causal E3 point estimate; that scarcity is confirmed, not resolved.

**Q3 (does quality debt cash out?) → OPEN, substantially narrowed.** Three channels now separately characterised:
1. *Catastrophic tail*: real but thin — 0.07% hard-to-reverse episodes in 16,118 validated misalignment episodes (dev-agent-misalignment-2026, B, new provenance); existence proofs at the destructive end (Replit; Grigorev — where the destroy was human-APPROVED: automation bias, not agent autonomy). Amazon's incident trend is document-based journalism vs an on-record corporate denial — unresolved, and reporting went quiet by June 2026.
2. *Structural debt*: the architecture leg comes back a null-to-artefact — smell density −6.7% is a denominator effect (raw counts flat, volume +12.8%), worst-case Lee bounds include zero (arch-quality-agentic-2026, B strong-end, independent provenance). The duplication leg gets a weak E3 revival (semantic redundancy 1.87×, single repo, AIDev). The maintenance question split into two constructs that must not be conflated (volume received vs cost-when-touched — contradiction logged) with one convergent fact: humans still perform 83% of maintenance on agent-authored files.
3. *Detectability*: the decisive new finding — Anthropic itself could not detect a 3%-magnitude Claude Code quality regression through internal evals in two postmortems seven months apart; detection was user complaints both times (anthropic-postmortem-quality, D fault-admitting). If the vendor cannot instrument this, no customer dashboard should claim to.
- Still true from scratch: NO organisation publishes defect/incident rates pre/post agentic adoption. The pilot (Q10) remains the only route to a denominator.

**Q6 (seniority) → CLOSED as "confirmed dry at E3".** Targeted hunting (two searches + the Opsera full read) found no third independent E3 split. The circulating "seniors capture 5×" is untraceable inside Opsera's own 19-page report — marketing-layer only (corruption instance #17); the report carries one unquantified direction sentence. xu-2025-maintenance-burden looked like E3 counter-evidence but is E1 (June-2021 Copilot preview) — its real contribution is the measured burden-*shift* mechanism onto core contributors (more review, less own output), which feeds tensions 5 and 6 with a pre-agentic label. The E3 evidence remains exactly two disagreeing datapoints (he-2026 flat; microsoft-cli-agents C-shape). Stop chasing; wait for the literature.

**Q7 (what made the 2×-mandate firm work?) → PARTIALLY ANSWERED from our own record + convergent practitioner detail.** Enabling conditions, evidence-graded:
1. Young codebase composition — the gain concentrates in post-2022 repos (+44% vs +12% n.s. legacy) [A, single firm];
2. Uncapped consumption — 20× token-spend growth tolerated ($42→$856/dev/mo) [A, single firm];
3. Mandate as catalyst only — its residual direct effect ≈0; the channel is adoption + accumulated use, compounding ~9 months to ~2× [A, single firm];
4. Absorption "solved" by routing around substantive human review (auto-approval; substantive review roughly halves) — an enabling condition that is also the cost [A, single firm];
5. Convergent task-shape detail from Salesforce (C, COI-flagged): narrow agent scope (one class at a time), structurally homogeneous template-like targets, a verification harness (coverage tooling), and mandatory human review — echoing the T5-mechanical-migration pattern from R1.
Missing externally: any second enterprise DiD; still none exists.

**Q8 (review bottleneck: queue vs function) → SHARPENED again; answer unchanged in direction.** New function-degradation signals, all pointing the same way: reviewer sentiment does not track measured redundancy (silent debt passes review; more-code-less-reuse-2026); 79.1% of merged agentic PRs show no visible human feedback loop; only 35.7% of agentic-PR rejections reflect agent failure (the rest is process/abandonment/unknown); humans retain 83% of downstream maintenance. Caveat: the PR-side findings are one voice (AIDev cluster). No case of *restored* substantive review at sustained throughput was found anywhere — the R1 formulation "automation absorbs the queue, not the function" survives from scratch and gains mechanism detail.

**Q4 (skill formation) → watch unchanged, one addition:** the meta-analysis learning pool (pre-agentic-dominant, zero E3) quantifies tool-dependence cleanly: g=0.76 when AI is allowed at assessment vs −0.06 when not — durable learning does not follow from assisted performance. Consistent with Shen & Tamkin; still no longitudinal professional agentic-era study.

**Q5 (unmeasured task types):** T8 (debugging/incident) gains its first substantial evidence — but lab-only, non-frontier models, no human baseline (rca-failures-2026: agentic workflows often underperform single-pass on RCA accuracy; +40–354% compute). T1/T2/T9 remain confirmed dry. No change to the three-dry-types conclusion.

**Q9 (J-curve):** nothing in 20 new sources shows a dip-then-recovery in any org's own longitudinal data. Unchanged: asserted everywhere, demonstrated nowhere.

**Q11 (spend caps → output):** confirmed that no post-cap output data exists for Uber or Microsoft (searches, July 2026). Stays a watch with richer policy context (95% monthly active engineers, ~10% agent-submitted code, COO's "token spend does not yet map to shipped features").

**Q12 (consumption curve):** not bending — Gartner's 24 Jun 2026 release (a real primary, unlike the phantom "Gartner Pulse") forecasts salary-crossing by 2028; corporate spend doubled since late 2025 despite ~90% token-price declines (Jevons pattern). Folded into ai-spend-landscape-2026's file as context; watch stands.

**Q13 (independence crisis):** the case strengthened materially in one cycle: AIDev cluster grew to ~8 dependent papers; Quispe's R1 "independent of all clusters" grading had to be retroactively corrected (v2 discloses Microsoft–GitHub funding + GitHub co-author, and its headline tripled on a measurement rebuild); corruption instances #16 (Kiro petition/mandate — aggregator smoke) and #17 (Opsera's 5× — vendor marketing inflating its own report) were added; xu's title escalated from hedged to unhedged causal across versions with unreconciled internal numbers. The proposed methods piece is now better-evidenced and remains ours to write if commissioned.

## B. Tension-verdict movements (addenda applied to memos + index)

- **T4 (quality debt): verdict stays CONTESTED-BUT-SUBSTANTIATED (medium); leg map updated.** New independent architecture leg is null-to-artefact with worst-case zero (bounds the debt claim from below); duplication leg gains a weak single-repo E3 counter-signal *against* the R1 "contradicted" call — recorded, not promoted (one repo, one-voice cluster); maintenance leg split into volume-vs-cost constructs (contradiction entry); detectability finding (Anthropic) added as a new leg: whatever debt exists, current instruments — including the vendor's own — cannot reliably see it at small magnitudes.
- **T5 (seniority): stays INSUFFICIENT EVIDENCE; chase formally closed.** Third-voice hunt exhausted (Opsera number untraceable; xu is E1). Secondary finding extended: the burden-shift mechanism (xu, E1) gives the seniority story a testable form — seniors may "lose" measured output because absorption work shifts to them — which links T5 to T6 rather than to capability.
- **T6 (bottleneck displacement): CONFIRMED in direction, unchanged; mechanism corroboration deepened** (83% maintenance share; coordination-dominated rejections; sentiment-blind review; RCA compute overhead). Magnitude still unresolved; new PR-side evidence is one voice (AIDev).
- **T1 (perception gap):** fifth datapoint appended at cross-ref (transcript-bound: self-estimates BELOW modelled ceiling — direction-variability corroboration on a different baseline kind).
- **T3 (throughput vs stability):** Amazon entry appended at cross-ref; verdict unchanged (contested; the one candidate incident-trend document is contested by the org itself and unresolved).
- **T7 (bad metrics): RESOLVED stands; one addition** — raw agentic-PR merge/rejection rate joins the reject list (composition-dominated: ≤36% of rejections are agent failures; 33% carry no observable rationale; per-agent rates driven by process signatures). Applied to the measurement proposal as reject metric #9.

## C. Conclusions that survived adversarial contact unchanged

1. The §8 scarcity headline — now *independently and systematically* confirmed: a pre-registered Tier A meta-analysis screening 10,186 records to Dec 2025 found only 2/16 productivity effect sizes (and 0/11 learning) from agentic-era tools. The scarcity is the literature's, not our search shape's.
2. "Self-report magnitude is uninformative about measured change" — untouched by five new self-report-adjacent datapoints.
3. The review-bottleneck direction — every new source that touches it corroborates; still no dissenting source anywhere.
4. RQ4's cost-without-outcome pairing gap — held in every single R3 source that carried cost data (token telemetry without outcomes; effort figures without quality; caps without output data). One rare paired-cost datapoint arrived (clean code cuts agent tokens −7–8%, revisits −34%) but it is vendor-circular (SonarSource, D).

## D. Output revisions applied (last, per pre-registration)

- follow-up-questions.md: all thirteen statuses updated per §A.
- exec-brief.md: header counts (74 sources / 362 findings); METR-update sentence added to the big-picture section; corruption count 15→17; architecture-null balancing clause and duplication-caveat added to the quality passages; maintenance-share clause added to the bottleneck section.
- internal-measurement-proposal.md: reject metric #9 (raw agent-PR merge rate); detectability principle added to the pilot section (complaint/anomaly channel — vendor postmortems show quality regressions surface through users, not dashboards, twice in seven months).
