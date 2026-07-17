# AI Coding Tools: What the Evidence Actually Says

**Two pages · July 2026 (refreshed 17 Jul) · based on 74 sources and 362 extracted findings · everything traceable in this repository**

How to read the tags: **[A]** = rigorous experiment, **[B]** = large-scale data without an experiment, **[C]** = credible company account, **[D]** = vendor material (they have something to sell). Plus how sure we are: high / medium / low.

---

## The big picture: nobody has properly measured today's AI agents yet

Almost every famous number you've heard — "55% faster", "26% more output" — comes from **old autocomplete tools timed on artificial lab tasks** (the "55% faster" was writing a toy web server from scratch), not today's agents doing real work. This does *not* mean autocomplete beat agents: those old numbers never measured real-world value either — stopwatch speed on toy problems doesn't survive contact with a real codebase. Today's agents simply haven't had an equivalent rigorous test at all, so nobody holds a trustworthy productivity figure for *either* generation doing real work.

In the entire world, only three rigorous (randomised) trials of AI coding *productivity* exist — and none tested a mature present-day agent. One of them found something remarkable: experienced developers working on codebases they knew well got **19% slower** with early AI agents, while being convinced they were 20% faster [A, high]. **2026 update:** the same lab re-ran the trial with late-2025 agents: the slowdown disappeared, but the new estimates are statistically inconclusive, and the lab is abandoning the design — developers now refuse to work without AI. The famous −19% is out of date; nothing rigorous has replaced it [B, medium]. An independent screen of 10,000+ studies confirms the hole: only two productivity measurements exist for today's agent-class tools [A, high].

We suspected the evidence might be this thin before we started, and wrote that expectation down. It turned out to be true. So the first rule is: treat every AI velocity claim — from vendors, from the press, from our own gut feeling — with suspicion.

## Three things we're genuinely sure about

1. **Don't trust what developers say about their own AI gains — including us.** Four separate studies compared what people *said* AI did for them against what was *measured*. People were off by 20–40 percentage points. Some overshot, some undershot, and at the individual level guesses were basically uncorrelated with reality [A/B, high]. Surveys tell you how people feel. They never tell you what happened.
2. **Numbers get mangled as they travel — at every layer.** We caught seventeen cases of press, newsletters, vendors, and aggregators corrupting numbers: wrong error margins, an entire consultancy "benchmark report" that turns out not to exist, one vendor whose marketing headline inflates its own peer-reviewed measurement by half, another whose viral "5×" statistic appears nowhere in its own report — and a whole ecosystem pasting one company's real cost figure onto other companies' stories (the "$2,000/month at Microsoft" you may have seen is Uber's number; Microsoft never stated one). Rule: never act on an AI number that hasn't been traced back to the original source [high].
3. **Companies are spending without checking what they get back — and the spending just changed shape.** Budgets set in the seat-licence era (typically $100–500 per developer per *year* in 2025) are colliding with token-era bills: a quarter of tech leaders now report $200–500 per developer per *month*, 6% exceed $2,000/month, and Gartner forecasts AI coding spend passing the average developer's salary by 2028 [D, distribution-grade]. Consumption climbs even at flat prices — Anthropic's own per-day cost estimate doubled in three months with no price change — and it is already forcing policy: Uber capped spend at $1,500/month per developer, Microsoft pulled its Claude Code licences over cost. Yet every organisation that publishes costs publishes **nothing** about what those costs bought; Uber's own COO says the productivity link "is not there yet" [C, high on the pattern].

## Where AI helps, and where it doesn't

**Best case:** new code in clean, well-tested codebases. The gains are real and they *grow with practice* — the best-documented company measured a genuine 1.5–1.7× throughput gain, but it took about nine months of daily use to get there [A, one company, medium].

**Worst case:** big, old, complicated codebases that developers already know inside out. The one rigorous trial in that setting found people got slower [A, high on direction]. Rare programming languages, messy codebases, and performance-tuning work also do consistently badly [B, medium].

**A useful nuance from the refresh:** "old codebase" isn't one thing. Mechanical, well-specified transformations inside old code — migrations, dependency upgrades — are where agent pipelines report their best results (Google's internal migrations; a bank's 6M-line legacy migration), though those numbers are self-reported or vendor-told [C/D, low-medium]. The struggle zone is open-ended feature work that needs context an agent doesn't have.

**Unknown:** for three of the eleven kinds of software work (requirements, architecture, internal tooling) there is **no measured evidence at all** — and we know because we hunted specifically and documented the dry holes [high on the absence]. Documentation and build/CI work now have first thin evidence. Not proof AI fails in the unmeasured areas — just nobody has checked.

## The key insight: writing code faster ≠ shipping faster

Individual coding gains are real. But whole-organisation delivery barely moves in comparison: across ~400 companies, delivery rose about 8% while AI usage grew 65% (vendor-measured, so trust the direction, not the exact figure [D]).

Why the gap? **The bottleneck moved.** Code gets written faster, but reviewing it, testing it, and absorbing it didn't speed up. In the one company measured end to end: code output tripled, human review coverage dropped from 89% to 68%, meaningful review halved, each reviewer's load doubled — and things actually took 22% *longer* to ship [A, one company; the pattern is echoed by two vendors and two other companies, medium-high that it's real, low on exact size].

Can AI review its own output? It can do it cheaply (about $1 per review at Cloudflare [C]) — but where anyone measured quality, AI-only-reviewed changes got accepted 23 points less often and most of the review comments were noise [B]. And even when agents write the code, people still do 83% of the later fixes to it [B]. So automation clears the queue; it doesn't yet replace the judgement.

**Quality:** agent-written code does carry a real maintenance cost — two independent rigorous studies show complexity creeping up and agents struggling to build on top of other agents' code [A, medium]. Interestingly, a controlled trial of the *older* tools found no such cost — this looks like a new, agent-era problem [A]. The claim has limits, though: an independent study of software architecture found no damage beyond what the sheer growth in code volume explains [B]. But there's no trustworthy bug-rate number anywhere: the viral claims in both directions come from conflicted sources measuring different things [not enough evidence]. And a sobering new fact: when Claude Code's own maker shipped changes that measurably degraded its output by 3%, its internal testing missed it — twice, months apart; user complaints were the alarm both times [D, against its own interest]. Small quality drops won't show on our dashboards either; the measurement proposal now adds a complaint channel for exactly this.

## Popular claims to stop repeating

- **"Developers report 2–3× gains"** — that's a feeling, not a measurement, and the feelings are getting bigger every year while the measurements aren't.
- **"AI helps juniors most"** — the original evidence was never statistically significant, and the only two agent-era measurements contradict each other [not enough evidence].
- **"X% of our code is AI-generated"**, lines of code, acceptance rates, token usage — all of these are gameable or meaningless. Each has a documented case of pointing the wrong way (see the measurement proposal).
- **"AI is creating copy-paste spaghetti"** — the quality claim most clearly contradicted by measurement: four studies found no duplication increase, and the largest real-world comparison found AI-attributed code *less* duplicated than human code. (One 2026 study did find agents reusing existing code less than humans — but it rests on a single repository; a watch item, not a comeback.)

## What we should do

1. **Push AI adoption where the evidence supports it** — new and clean-codebase work — and be patient: the gains compound over months. For old, complex codebases, don't assume either way; measure our own.
2. **Invest in review and verification capacity, not just AI licences.** That's the proven bottleneck. Scaling code generation without scaling absorption just builds a queue.
3. **Measure ourselves.** The companion proposal lists six things to track and eight popular metrics to refuse. Published evidence cannot tell us whether AI works *for us* — on today's data, it can't tell anyone.

*One honest gap: whether AI use erodes engineers' skills over time rests on just two studies (one found a real comprehension cost from AI-assisted learning, with no speed benefit to offset it). We deliberately didn't do a full evidence sweep on this. Treat all skill-formation claims, positive or negative, as open questions.*
