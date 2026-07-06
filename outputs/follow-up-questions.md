# Open Questions for Follow-Up Research

**July 2026 · updated after refresh cycle R1 and the spend hunt (originally drafted post-Phase-5) · planning material, not findings**

Status key: **OPEN** unchanged · **SHARPENED** new evidence narrowed it · **PARTIALLY ANSWERED** · **DISCHARGED** the underlying work was done.

## A. Tensions inside our own findings

1. **Can the −19% and the +1.5–1.7× both be true today? — OPEN, transience now corroborated.** Still no METR-style RCT on 2026 agents. R1 added an independent datapoint (Quispe, Caltech, own pipeline): Claude Code adopters show a commit spike that decays fast (+40.7 → +13.3 by month two) — the first corroboration of the transient-gain pattern from outside the CMU/AIDev clusters. The reconciliation candidates (tool generation, practice duration, task familiarity) remain untested head-to-head. *Chase: METR's hinted autonomous-agent work; any 2026-agent RCT.*
2. **Heavy use predicts gains, but heavy use also underperforms — OPEN, urgency up.** The spend hunt made this operational: NVIDIA is normalising token budgets at ~half of salary while Uber caps at $1,500/month and Microsoft pulled licences entirely. Two opposite policies are now running as natural experiments on exactly this question. *Chase: any output data from capped vs uncapped orgs; usage-pattern (not volume) studies.*
3. **Does quality debt ever cash out in defects/incidents? — OPEN, narrowed.** R1 narrowed the question: the duplication leg is now contradicted (four designs), so the live legs are complexity growth and downstream agent-on-agent cost; Mao added a measured absorption signal (AI-commit handoff latency 28 vs 11 days, longer stabilisation). Still no org publishing defect/incident rates pre/post agentic adoption. *Chase: the unextracted Amazon outage material; SlopCodeBench-class multi-step drift; any incident-rate disclosure.*

## B. Gaps we knowingly left — status changed for all three

4. **Skill-formation sweep — DISCHARGED; hole CONFIRMED.** The dedicated sweep ran in R1: the promising longitudinal candidate (Sergeyuk) turned out pre-agentic and cohort-level; the biometrics study is students-only (mechanism background). No longitudinal, professional, agentic-era skill-retention study exists. The question is now "wait for the literature" rather than "we haven't looked" — and the comprehension-check instrument in the measurement proposal remains precautionary. *Watch: replications of Shen & Tamkin with agentic tools.*
5. **Unmeasured task types — PARTIALLY ANSWERED.** Five became three: T11 (build/CI) and T10 (docs) gained first thin evidence in R1; T1 (requirements), T2 (architecture), T9 (internal tooling) are confirmed dry by targeted hunting. *Chase: weight any further effort by our own spend on the three dry types.*
6. **Seniority — SHARPENED from scarcity to disagreement.** The hunt found the missing E3 study (Microsoft CLI agents: C-shaped pattern — juniors and senior managers gain most), and it disagrees with he-2026's flat gradient. Meanwhile the labour market acts on the unsupported "juniors obsolete" story anyway. *Chase: a third E3 seniority split independent of both Microsoft and the He/Denisov-Blanch group — none exists.*

## C. Questions about the strongest findings

7. **What made the 2×-mandate firm work? — OPEN, untouched.** The enabling-conditions question (codebase health, tooling, review culture) remains the highest-value unanswered detail about the best E3 result. *Chase: second/third enterprise DiD studies; re-read he-2026's context sections.*
8. **Can the review bottleneck be fixed? — OPEN, sharpened to "queue vs function".** R1's intervention hunt found one measured case (Atlassian: cycle time −30.8%) — but human review volume *fell* 35.6% with AI comments resolving less often, and no case anywhere shows substantive coverage being *restored*. The emerging answer: automation absorbs the queue, not yet the function. *Chase: any org showing restored substantive review at sustained throughput.*
9. **Is the J-curve real? — OPEN; hole now documented.** A targeted R1 hunt found no dip-then-recovery in any organisation's own longitudinal data — only the DORA analogy and commentary on it. The claim remains asserted everywhere, demonstrated nowhere. *Chase: longitudinal adoption datasets; our own pilot (Q10).*

## D. New questions raised since the original list

10. **Run our own pilot — unchanged, still first.** Now answers questions 2, 3, and 9 from our own data; the spend instrument is stronger post-hunt (consumption units, date-stamped benchmarks).
11. **NEW — What do the spend caps do to output?** Uber (cap) and Microsoft (withdrawal) created the first natural experiments on constraining agentic spend. If gains compound with sustained heavy use (he-2026) but caps bind exactly there, caps may cost more than they save — or the death-valley effect means they're free. Nobody has measured either. *Chase: any follow-up reporting on post-cap Uber / post-cutover Microsoft engineering output.*
12. **NEW — Does consumption keep doubling?** Anthropic's per-day estimate doubled in three months at constant prices; Gartner forecasts salary-crossing by 2028. Whether that curve bends determines whether today's ROI arithmetic survives 2027. *Chase: vendor telemetry updates; the token-price/efficiency trend.*
13. **NEW — The independence crisis as a research topic in its own right.** This project repeatedly found "convergence" that collapsed to one voice: one lab behind three papers, one dataset under four, one company's number laundered across others' names, a vendor inflating its own measurement. A short methods piece on independence auditing in AI-productivity evidence would be genuinely novel — our corpus is effectively the dataset for it. *Chase: nothing external — this one we could write.*

*The ledger's Queued table still holds the triaged, unextracted leads that map onto these questions; any follow-up starts warm.*
