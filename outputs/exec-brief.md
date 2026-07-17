# AI Coding Tools: What the Evidence Actually Says

**Two pages · July 2026 (refreshed 17 Jul) · based on 74 sources and 362 extracted findings · everything traceable in this repository**

How to read the tags: **[A]** = rigorous experiment, **[B]** = large-scale data without an experiment, **[C]** = credible company account, **[D]** = vendor material (they have something to sell). Plus how sure we are: high / medium / low.

---

## The big picture: nobody has properly measured today's AI agents yet

Almost every famous number you've heard — "55% faster", "26% more output" — comes from old autocomplete tools (the "55% faster" was a timed toy web server built from scratch), not today's agents doing real work. Those old numbers say little about agents either way; agents simply haven't had an equivalent test.

Only three randomised trials have tested AI coding productivity on working developers — and none tested a mature present-day agent. One found something remarkable: experienced developers on codebases they knew well got **19% slower** with early AI agents, while convinced they were 20% faster [A, high]. **2026 update:** the same lab re-ran the trial with late-2025 agents: the slowdown disappeared, but the new estimates are statistically inconclusive, and the lab is abandoning the design — enough developers now refuse to do tasks without AI that the comparison group collapsed. The famous −19% is out of date; nothing rigorous has replaced it [B, medium]. An independent screen of 10,000+ studies found the same hole in its own pool: only two of its productivity measurements covered today's agent-class tools [A, high].

We predicted this thinness in writing before we started. So rule one: treat every AI velocity claim — vendor, press, or our own gut — with suspicion.

## Three things we're genuinely sure about

1. **Don't trust what developers say about their own AI gains — including ours.** Four studies paired what people said against what was measured (three on AI gains specifically, one on developers' self-assessment generally). People were off by roughly 20–40 points, in both directions, and individual guesses were basically uncorrelated with reality [A/B, high]. Surveys tell you how people feel — never what happened.
2. **Numbers get mangled as they travel.** We caught seventeen cases of press, vendors, and aggregators corrupting numbers: a consultancy "benchmark report" that doesn't exist, a vendor whose marketing inflates its own peer-reviewed measurement by half, another whose viral "5×" stat appears nowhere in its own report. The "$2,000/month at Microsoft" you may have seen is Uber's number. Rule: never act on an AI number that hasn't been traced to its original source [high].
3. **Companies are spending without checking what they get back — and the spending changed shape.** Seat-licence budgets (typically $100–500 per developer per *year* in 2025) are colliding with token-era bills: a quarter of tech leaders now report $200–500 per developer per *month*, 6% exceed $2,000, and Gartner forecasts AI coding spend passing an average developer's salary by 2028 [D — we use only the spread, not any single number]. Consumption grows even at flat prices: Anthropic's own per-day cost estimate doubled between successive published estimates with no price change. It is already forcing policy — Uber capped spend at $1,500 per tool per month; one Microsoft division pulled its Claude Code licences over cost. Yet every organisation that publishes costs publishes **nothing** about what the money bought; Uber's own COO says the productivity link "is not there yet" [C, high on the pattern].

## Where AI helps, and where it doesn't

**Best case:** new code in clean, newer codebases. The gains are real and *grow with practice* — the best-documented company measured a genuine ≈1.5–1.7× throughput gain, but it took about nine months of daily use [A, one company, medium].

**Worst case:** big, old, complicated codebases that developers already know inside out. The one rigorous trial in that setting found people got slower [A, high on direction]. Rare languages, messy codebases, and performance work also do consistently badly [B, medium — partly pre-agentic evidence].

**One exception inside old code:** mechanical, well-specified changes — migrations, dependency upgrades — are where agents report their best results, though those numbers are self-reported or vendor-told [C/D, low-medium]. The struggle zone is open-ended feature work needing context the agent doesn't have.

**Unknown:** three of the eleven kinds of software work (requirements, architecture, internal tooling) have **no measured evidence at all** — we hunted and documented the dry holes [high on the absence]. Not proof AI fails there; nobody has checked.

## The key insight: writing code faster ≠ shipping faster

Individual coding gains are real. But whole-organisation delivery barely moves: across ~400 companies, delivery rose about 8% while AI usage grew 65% (vendor-measured; trust the direction, not the figure [D]).

Why the gap? **The bottleneck moved.** Code gets written faster; reviewing, testing, and absorbing it didn't speed up. In the one company measured end to end: output tripled, human review coverage fell from 89% to 68%, meaningful review halved, each reviewer's load doubled — and AI-written changes took 22% *longer* to ship than comparable human-written ones [A, one company; the pattern is echoed by two vendors and two other companies — medium-high that it's real, low on size].

Can AI review its own output? Cheaply, yes (about $1 per review at Cloudflare [C]) — but where quality was measured, AI-only-reviewed changes were accepted 23 points less often and most AI reviews carried no usable signal [B]. And people still do 83% of the later fixes to agent-written code [B]. Automation clears the queue; it doesn't yet replace the judgement.

**Quality:** agent-written code carries a real maintenance cost — two independent rigorous studies show complexity creeping up and agents struggling to build on other agents' code [A, medium]; a controlled trial of the *older* tools found no such cost, so this looks agent-era [A]. But the claim has limits: an independent architecture study found no damage beyond what sheer code growth explains [B], and no trustworthy bug-rate number exists anywhere [not enough evidence]. A sobering new fact: when Claude Code's own maker shipped quality-degrading changes (one drop later measured at 3%), its internal testing missed them twice, months apart — user complaints were the alarm both times [D, against its own interest]. Small quality drops won't show on our dashboards either; the measurement proposal adds a complaint channel for exactly this.

## Popular claims to stop repeating

- **"Developers report 2–3× gains"** — a feeling, not a measurement; the feelings grow every year while the measurements don't.
- **"AI helps juniors most"** — never statistically significant, and the only two agent-era measurements contradict each other [not enough evidence].
- **"X% of our code is AI-generated"**, lines of code, acceptance rates, token usage — all gameable or meaningless; each has a documented case of pointing the wrong way (see the measurement proposal).
- **"AI is creating copy-paste spaghetti"** — contradicted by measurement: four studies from three independent groups found no duplication increase, and the largest real-world comparison found AI-attributed code *less* duplicated than human code. (One 2026 study found agents reuse existing code less — but it rests on a single repository; a watch item, not a comeback.)

## What we should do

1. **Push AI adoption where the evidence supports it** — new and clean-codebase work — and be patient: the gains compound over months. For old, complex codebases, don't assume either way; measure our own.
2. **Invest in review and verification capacity, not just AI licences.** That's the proven bottleneck. Scaling code generation without scaling absorption just builds a queue.
3. **Measure ourselves.** The companion proposal lists six things to track and nine popular metrics to refuse. Published evidence cannot tell us whether AI works *for us* — on today's data, it can't tell anyone.

*One honest gap: whether AI use erodes engineers' skills over time rests on just two studies — one found a real comprehension cost from chat-style AI assistance (pre-agentic tools), with no speed benefit to offset it. We deliberately didn't do a full evidence sweep here. Treat all skill-formation claims, positive or negative, as open questions.*
