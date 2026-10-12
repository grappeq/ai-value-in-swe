# AI Coding Tools: Twenty Claims, Checked — DRAFT in statement format

**Draft for review · October 2026 · based on 101 sources and 569 extracted findings · a proposed replacement format for the exec brief; the current narrative brief remains the published version until you decide**

How to read each entry: **the claim** as you would hear it; a **verdict** (TRUE · PARTLY TRUE · FALSE · UNKNOWN); the **strength of evidence** — the best tier behind it ([A] rigorous experiment · [B] large-scale data · [C] credible company account · [D] vendor material), how many *independent* voices (shared authors, data or funding count once), and whether it concerns today's agents (E3) or older tools (pre-agentic); then the **context** that changes what you should do with it.

---

## A. How much do we actually know?

**1. "The productivity effect of AI coding agents has been rigorously measured."**
**Verdict: FALSE.** Strength: high confidence in the *absence* — two independent systematic reviews ([A], different methods) found two and zero agent-era productivity measurements respectively; fewer than ten randomised trials exist across five programmes, none on a mature present-day agent.
Context: what exists for agents is one firm's causal study [A, one company] and a 500,000-developer activity study [B, Microsoft data, revised figures unstable]. Real evidence, not trials. Treat every agent-era velocity number as provisional.

**2. "Experienced developers get slower with AI on code they know well."**
**Verdict: PARTLY TRUE (and dated).** Strength: [A], one trial, early-2025 agents, 16 developers — the famous −19% [CI +2%, +39%].
Context: the same lab's late-2025 re-run erased the slowdown but was statistically inconclusive, and the design was abandoned because developers refuse to work without AI. Direction for mature, familiar code remains "no demonstrated gain"; the number itself should not be quoted as current.

**3. "Developers can tell you how much AI is helping them."**
**Verdict: FALSE.** Strength: [A/B], four independent paired designs, era-independent — self-estimates were off by 20–40 points, in *both* directions, and individual guesses were uncorrelated with measured change.
Context: two new datapoint kinds arrived in 2026 — people who accurately rate their own lower comprehension still prefer the agent, and users rate a diagnostic tool below its expert-measured accuracy. Surveys measure morale; they never measure what happened.

**4. "The AI productivity numbers in the press are reliable."**
**Verdict: FALSE.** Strength: high — twenty-five documented cases of numbers corrupted between source and citation: a consultancy report that does not exist, two vendors whose viral multiples ("5×", "4.6×") appear nowhere in their own reports, a company's cost figure re-attributed to another company, preprints whose headline effects moved 40–80% between versions.
Context: trace any number to its primary before acting on it; when a preprint has versions, cite the version.

## B. Where it helps

**5. "Agents raise individual output."**
**Verdict: TRUE.** Strength: [A] one firm (PRs per developer 1.46–1.72×, causal) and [B] 500,000 open-source developers (commits +153% for sync agents) — two voices, both E3, one of them Microsoft-funded.
Context: output means commits and pull requests, not delivered software (see 9). The one-firm result is self-described as an upper envelope.

**6. "The gains compound with practice — be patient."**
**Verdict: UNKNOWN (contested).** Strength: [A/B] but confounded — the firm's own data cannot separate practice from newer models (a placebo release moved the outcome as much as a real one); the largest study credits model vintage, not learning; several panels show gains fading within three to six months.
Context: do not budget for compounding. Measure whether your own gains persist past month three.

**7. "AI works best on new code in clean, newer codebases."**
**Verdict: TRUE on direction, contested on size.** Strength: [A] one firm (post-2022 repositories +44% vs legacy +12% not significant) plus [B] telemetry and professionals' own suitability ratings (boilerplate 25:0, tests 19:2 suitable; legacy integration 3:17 unsuitable) — unanimous direction, but the sharpest numbers come from one research lineage.
Context: the struggle zone is open-ended feature work in old systems needing context the agent lacks; mechanical, well-specified changes inside old code (migrations, upgrades) are the exception, on self-reported or vendor numbers [C/D, low-medium].

**8. "AI helps with requirements, architecture, and internal tooling."**
**Verdict: UNKNOWN.** Strength: high confidence in the absence — requirements and internal tooling have no measured evidence at all after deliberate hunting; architecture has usage data only (what people ask chat tools), no outcome.
Context: not evidence that AI fails there; nobody has checked. Weight your own pilots by your spend on these task types.

## C. Does it ship?

**9. "Writing code faster means shipping faster."**
**Verdict: FALSE.** Strength: [B] 500,000 developers — commits +153% but releases +20%; [A] one firm — output tripled while AI-written changes took 22% *longer* to ship; [D] ~400 companies — delivery +8% while AI use grew 65%. Seven named organisations, three vendors and the two measured studies all point one way; no source shows the opposite. High confidence that the bottleneck moved.
Context: "release" in the big study is a GitHub release object, not a customer delivery; whether the attenuation is steeper or flatter inside enterprise pipelines is the open question.

**10. "The bottleneck is code review."**
**Verdict: PARTLY TRUE.** Strength: medium — one firm measured review coverage falling from 89% to 68% and substantive review halving [A]; agentic pull requests wait 5× longer for a first reviewer and are reviewed slower once picked up [D]; AI-reviewer involvement speeds decisions without improving a quality proxy [B, independent data].
Context: the 500,000-developer study measures no review time, so "review specifically" is inferred, not shown. Testing, verification and sign-off bottlenecks are equally consistent with the data (one bank saw lead time per story unchanged because of homologation).

**11. "AI can review its own output."**
**Verdict: PARTLY TRUE — it clears the queue, not the judgement.** Strength: [C] cheap (about $1 per review); [B] AI-only-reviewed changes accepted 23 points less often, most AI review comments carrying no usable signal; no organisation anywhere has documented substantive human review *restored* at agentic throughput.
Context: every "fix" found so far routes around review (auto-approval of low-risk changes) rather than restoring it.

## D. What does it cost?

**12. "Companies know what their AI coding spend buys."**
**Verdict: FALSE.** Strength: high on the pattern — organisations that publish spend almost never publish outcomes; the single exception pairs a 20× spend increase with a 1.5–1.7× throughput gain [A, one firm]; Uber's COO says the link "is not there yet" [C].
Context: budgets changed shape in 2026 — seat licences ($100–500 per developer per *year*) gave way to token bills ($200–500 per developer per *month* for a quarter of leaders; 6% above $2,000) [D, spread only]. Consumption rises even at flat prices: one tool's tokens per task rose 70% across its own releases with the model unchanged [A, lab].

**13. "Agent-written code costs more to maintain."**
**Verdict: PARTLY TRUE.** Strength: [A] two independent studies — complexity and warnings rise and persist; agents resolve follow-on tasks on agent-written code up to 13 points less often; [B] agent merges draw follow-up fixes at 1.6× the odds (low absolute rate, 4.5% in 30 days).
Context: an independent architecture study found no damage beyond what code growth explains [B]; a controlled trial of older tools found no maintainability cost [A], so this looks agent-era. No trustworthy defect-rate number exists anywhere.

**14. "AI is creating copy-paste spaghetti."**
**Verdict: UNKNOWN (mixed).** Strength: three measured studies from two groups found no duplication increase for older tools (the largest found AI-attributed code *less* duplicated); the one agent-era re-analysis found significant increases in agent-first repositories [B, one voice].
Context: a watch item, not a settled claim in either direction.

**15. "Our quality dashboards would catch an AI-driven quality drop."**
**Verdict: FALSE.** Strength: two data provenances — the maker of Claude Code twice failed to detect user-visible regressions with its own evals (one later measured at 3%; user complaints were the alarm both times) [D, against interest]; in a lab, routine tool updates with the model unchanged spiked token costs 50–130% and cut solve rates, and every one passed 300+ automated tests [A, lab].
Context: keep an explicit complaint and anomaly channel; small regressions are invisible to test suites and dashboards alike.

**16. "Agents with production access are safe enough."**
**Verdict: FALSE as stated — the failure mode is real; its rate is unknown.** Strength: [C ×3] a production database deleted during a code freeze, a Terraform destroy that a human approved, and Amazon's contested outage series; [B] about 0.1% of observed agent–developer misalignment episodes were hard to reverse (imprecise: eleven cases on the weakest-validated axis).
Context: existence proofs, not rates. Automation bias (approving the destroy) is part of the failure mode.

## E. People

**17. "AI helps juniors most."**
**Verdict: UNKNOWN.** Strength: never statistically significant in any era; the only two agent-era measurements disagree on the shape of the effect.
Context: a pre-agentic study suggests "seniors lose output" may really be seniors absorbing review load — a workload effect, not a capability one.

**18. "Using AI erodes engineers' skills."**
**Verdict: PARTLY TRUE for comprehension in the short term; UNKNOWN long term.** Strength: [A] two small randomised trials from independent groups, both on students, one with an early agent — comprehension lower (d>0.8) even where the agent arm was faster; participants preferred the agent anyway.
Context: no professional, long-horizon study exists. Treat all skill-formation claims, positive or negative, as open.

**19. "Claude Code has become the default agent."**
**Verdict: TRUE (as an adoption fact).** Strength: three non-overlapping self-report surveys in 2026 [C/D] — 65% of agent users (Stack Overflow), top tool (Pragmatic Engineer), 39% work use with Copilot falling 29%→21% (JetBrains).
Context: adoption says nothing about value; the same surveys show trust for important decisions at 6.6%.

**20. "Percent of code written by AI is a useful metric."**
**Verdict: FALSE.** Strength: high — no validated way to compute it exists; one 15,000-developer survey's self-reported shares (agent-written, AI-assisted, manual) sum to 112%; lines of code, acceptance rate and token volume each have a documented case of pointing the wrong way.
Context: the companion measurement proposal lists six things to track in cost/outcome pairs, and nine metrics to refuse.

---

## What to do with this

1. Push adoption where claims 5 and 7 hold — new and clean-codebase work — and measure whether your gains persist past month three (claim 6).
2. Invest in review, verification and sign-off capacity, not just licences (claims 9–11).
3. Measure yourself, in cost/outcome pairs, with a complaint channel for the regressions dashboards miss (claims 12, 15, 20). Published evidence cannot tell you whether AI works for *your* teams — on today's data, it can't tell anyone.

*Format note for the reviewer: every verdict above maps onto a graded row in `evidence/evidence-table.tsv`; a clean-room re-derivation by an analyst who saw only the evidence reproduced 23 of 24 of these positions. The two-page cap is respected at ~1,500 words; cutting to sixteen claims would bring it under 1,250.*
