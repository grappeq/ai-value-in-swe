# AI in Software Engineering: What the Evidence Actually Says

**Two-page brief · July 2026 · based on 42 sources, 181 extracted findings, 7 adjudicated controversies · full evidence base in this repository**

Every claim below carries its evidence grade: **[A]** rigorous experiment, **[B]** large-scale observational, **[C]** credible practitioner account, **[D]** vendor material (conflict of interest), plus a confidence level.

---

## The headline: the agentic era has not yet been rigorously measured

Almost every famous number in circulation ("55% faster", "26% more output") comes from studies of **autocomplete-era tools on artificial tasks**, not today's agents on real work. Only three randomised trials of AI coding productivity exist anywhere, all pre-agentic or early-boundary, and one of them found experienced developers got **19% slower** on their own mature codebases — while believing they were 20% faster [A, high]. For current agentic tools, rigorous evidence amounts to a handful of single-company studies. This scarcity was pre-registered as a possible outcome of this research; it is the finding, and it should temper every velocity claim we hear or make.

## Three things we can say with high confidence

1. **Developers' own estimates of AI benefit are unreliable — in both directions.** Four independent studies paired what people *said* against what was *measured*: estimates were wrong by 20–40 percentage points, overshooting in some settings, undershooting in others, and essentially uncorrelated with reality at the individual level [A/B, high]. Self-report surveys measure sentiment, never impact.
2. **Second-hand numbers in this field are routinely corrupted.** This research caught ten instances of press, newsletters, and vendors misquoting confidence intervals, attributing one company's figures to another, and inventing statistics that appear in no primary source. Rule: never act on an AI-productivity number that hasn't been traced to its original study [high].
3. **Companies spend on AI without measuring what it returns.** Every organisation with published cost data (token bills growing 20× in a year at one firm; $150–2,000 per engineer per month at Uber, which then capped spend) publishes **no paired outcome data** — and Uber's COO says on record the productivity link "is not there yet" [C, high on the pattern].

## Where AI helps — and where it doesn't (the value and failure maps)

**Helps most:** fresh code in clean, well-tested codebases; the gains are real and *compound with sustained use* — the best-run enterprise measured a causal 1.5–1.7× throughput gain that took ~9 months of tool tenure to build [A, single firm, medium]. **Helps least or hurts:** large, mature, complex codebases that developers know intimately — the one rigorous trial there found a measured slowdown [A, high on direction]; low-popularity languages, messy codebases, and performance-critical work also consistently underperform [B, medium]. Five of eleven software-lifecycle task types (requirements, architecture, internal tooling, documentation, ops) have **no measured value evidence at all** — only usage statistics [high on the absence].

## The strategic answer: local speedup ≠ delivery speedup

Individual coding gains are genuine, but organisation-level delivery moves far less: cross-company telemetry shows single-digit-to-low-teens percentage improvements against usage growth of 65% (vendor-measured, direction only [D]), and even the best-case firm's raw "2×" shrinks to ~1.5× once statistical artefacts are removed [A]. The reason is now well-evidenced in direction: **the bottleneck has moved from writing code to reviewing and absorbing it**. In the one firm measured end-to-end, human review coverage fell from 89% to 68%, substantive review halved, reviewer load doubled — and cycle time *rose* 22% even as output doubled [A, single firm; corroborated in direction by two vendor telemetry sets and two practitioner accounts, medium-high on mechanism, low on magnitude]. Automated review absorbs the queue cheaply (~$1 per review at Cloudflare [C]) but not demonstrably the *function*: agent-only-reviewed changes merge 23 points less often and are mostly noise where measured [B].

**Quality:** a real maintainability cost of agent-written code is supported by two independent rigorous studies (complexity rises persistently; agents work measurably worse on top of agent-written code) [A, medium], and notably a controlled pre-agentic trial found *no* such cost — this is an agent-era phenomenon [A]. But no trustworthy defect-rate number exists in either direction: the viral claims (both "+41% bugs" and vendor rebuttals) are all conflicted sources measuring incomparable things [insufficient evidence].

## What the hype gets wrong — expectation-setting corrections

- "Developers report 2–3× gains" — sentiment, not measurement; self-reported multipliers are inflating over time with no comparator.
- "AI helps juniors most" — the founding evidence was never statistically significant, and the only two agentic-era measurements disagree with each other on the pattern [insufficient evidence].
- "X% of our code is AI-generated" and lines-of-code, acceptance-rate, or token-volume metrics — gameable or meaning-free; every one has a documented failure case (see measurement proposal).
- "Quality debt is churn and copy-paste" — the popular framing is the *least*-supported version; three independent studies find no duplication effect.

## What we should do

1. **Push adoption** where evidence supports it: greenfield and clean-codebase work, with patience for the ~months-long compounding curve; treat mature-codebase work as a split decision requiring our own measurement, not an assumption.
2. **Fund absorption, not just generation:** review and verification capacity is the binding constraint; instrument it before scaling agent output.
3. **Measure ourselves** — the companion proposal names six instruments and rejects seven popular metrics. External evidence cannot settle whether AI works *for us*; on current published data, nobody's can.

*Scope note: the long-term effect of AI on engineers' skill formation rests on two incidental studies (one showing a measured comprehension cost of AI-assisted learning, effect size d=0.738, with no speed gain); a dedicated evidence sweep was deliberately deferred. Treat skill-formation claims in either direction as open.*
