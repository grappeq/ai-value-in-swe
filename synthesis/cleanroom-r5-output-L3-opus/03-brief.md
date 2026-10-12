# 03 — Brief: where AI coding tools deliver measurable value

*Basis: 569 graded findings from 99 sources. Each source cluster (shared authors, data or organisation) is counted once. Effect sizes are E3 (agentic) unless labelled pre-agentic.*

**1. Agentic tools raise measured output, but most of the gain is lost before anything ships.**
- Within one firm, PRs per developer rose 1.46–1.72× (he-2026-2x-mandate).
- In a large open-source panel, the gain shrank at each step towards shipping: lines +957%, commits +153%, PRs +86%, releases +19.8% (demirer-2026-writing-vs-shipping).

*Tier A + B · E3 · Confidence: **medium**.* Two independent measured studies agree; the firm describes itself as an upper bound.

**2. Gains concentrate in newer code. In mature, familiar codebases they are null or negative.**
- Repositories created from 2022 onwards gained +44%; older ones gained +12% (not significant) (he-2026-2x-mandate).
- Experienced developers working in their own large repositories were 19% slower (CI 1–40%) (metr-2025-rct).
- METR's attempt to replicate this failed on design grounds (metr-2026-design-change).

*Tier A · E3 · Confidence: **medium**.* Two independent Tier A sources point the same way, but neither covers late-2025 agents in mature code.

**3. Review becomes the bottleneck, and human scrutiny thins.**
- At one firm, PR volume rose 3.1× while the reviewer pool rose 1.5×.
- Review lead time for AI PRs rose 20%.
- Substantive human review fell from about 39% to about 21% (he-2026-2x-mandate).
- Independent sources show human review being displaced by AI review (atlassian-2026-ai-review, zhong-2026-agentic-review, unreviewed-ai-prs-2026).

*Tier A + B · E3 · Confidence: **medium**.* The direction is consistent across independent sources; the size comes from one firm.

**4. Developers' own estimates cannot be used to judge AI's value.**
- In metr-2025-rct, developers believed they were 20% faster and were measured 19% slower.
- Pre-agentic: in peng-2023-copilot-rct the error ran the other way, with developers underestimating their gain by about 21 pp.

*Tier A · E3 and E1 (an effect that does not depend on era) · Confidence: **high**.* Every paired measurement shows a large error, in either direction.

**5. Agent-written code is harder to maintain. Whether this becomes production defects is unknown.**
- Follow-on tasks on agent-authored code resolved up to 13.1 pp less often (agent-maintainability-2026).
- Static-analysis warnings and complexity rose 18–42% and persisted (cursor-velocity-quality-2025, agents-vs-ides-2026; one research group).
- Follow-up fixes were more common after agent PRs (OR 1.62) (who-finishes-the-job-2026).
- Against this, AI PRs at one firm were reverted less often (he-2026-2x-mandate).

*Tier A + B · E3 · Confidence: **medium** for maintenance cost, **low** for any effect on defects.*

**6. Heavy delegation lowers immediate comprehension.**
- Two independent randomised trials found comprehension or skill drops of d≈0.74–0.8+ (impaired-programming-2026; shen-2026-coding-skills, E2).
- Speed benefits were inconsistent: faster on the initial task but no difference on the follow-on extension task in one trial, and not significant in the other.
- Both tested learners on short tasks.

*Tier A · E3/E2 · Confidence: **medium** for the immediate effect, **low** for durable professional deskilling.*

**7. Agents with unguarded production access have caused destructive incidents.**
- Three independent organisations report deleted databases or outages (grigorev-2026-terraform-db, replit-db-deletion-2025, amazon-2026-outages).
- Amazon disputes that AI caused its incident.

*Tier C ×3 · E3 · Confidence: **medium** that the failure mode exists.* No source gives a rate.

**8. Cost-to-value cannot be computed for any task type.**
- Only one Tier A/B source reports spend. At that firm, Claude spend rose about 20× ($42→$856 per developer-month) while PRs rose about 1.5–2× (he-2026-2x-mandate).
- No source reports review overhead in money.

*Tier A (single firm) · E3 · Confidence: **high** that the evidence is absent; **low** on the ratio itself.*

### What the evidence cannot say
- **Whether E3 agents speed up feature delivery in mature production codebases.** No reliable late-E3 task-time study and no counterfactual DORA-type measurement (deployment frequency, lead time, change failure rate, recovery) exist.
- **Whether AI changes production stability or incident rates.** All such data is Tier D, pre-agentic self-report, or contested.
- **What anything costs per unit of value**, including review hours and token spend across firms.
- **Anything measured about requirements (T1), design (T2), documentation (T10) or internal tooling (T9).** The "internal tooling win" is unmeasured here.
- **Whether juniors or seniors benefit more.** No significant interaction has been measured in any era.
- **Whether quality-debt proxies turn into real defects**, or whether comprehension loss persists in professional settings.
