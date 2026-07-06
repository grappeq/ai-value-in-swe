# AI Coding Tools: What the Evidence Actually Says

**Two pages · July 2026 · based on 42 sources and 181 extracted findings · everything traceable in this repository**

How to read the tags: **[A]** = rigorous experiment, **[B]** = large-scale data without an experiment, **[C]** = credible company account, **[D]** = vendor material (they have something to sell). Plus how sure we are: high / medium / low.

---

## The big picture: nobody has properly measured today's AI agents yet

Almost every famous number you've heard — "55% faster", "26% more output" — comes from studies of **old autocomplete tools doing artificial tasks**. Not today's agents doing real work.

In the entire world, only three rigorous trials of AI coding productivity exist. All predate modern agents. And one of them found something remarkable: experienced developers working on codebases they knew well got **19% slower** with AI — while being convinced they were 20% faster [A, high].

We suspected the evidence might be this thin before we started, and wrote that expectation down. It turned out to be true. So the first rule is: treat every AI velocity claim — from vendors, from the press, from our own gut feeling — with suspicion.

## Three things we're genuinely sure about

1. **Don't trust what developers say about their own AI gains — including us.** Four separate studies compared what people *said* AI did for them against what was *measured*. People were off by 20–40 percentage points. Some overshot, some undershot, and at the individual level guesses were basically uncorrelated with reality [A/B, high]. Surveys tell you how people feel. They never tell you what happened.
2. **Numbers get mangled as they travel.** While doing this research we caught ten cases of press articles, newsletters, and vendors misquoting studies — wrong error margins, one company's figures attributed to another, statistics that appear in no original source at all. Rule: never act on an AI number that hasn't been traced back to the original study [high].
3. **Companies are spending without checking what they get back.** Every organisation that has published its AI costs (one firm's token bill grew 20× in a year; Uber pays $150–2,000 per engineer per month and had to cap it) has published **nothing** about what those costs bought. Uber's own COO says the productivity link "is not there yet" [C, high on the pattern].

## Where AI helps, and where it doesn't

**Best case:** new code in clean, well-tested codebases. The gains are real and they *grow with practice* — the best-documented company measured a genuine 1.5–1.7× throughput gain, but it took about nine months of daily use to get there [A, one company, medium].

**Worst case:** big, old, complicated codebases that developers already know inside out. The one rigorous trial in that setting found people got slower [A, high on direction]. Rare programming languages, messy codebases, and performance-tuning work also do consistently badly [B, medium].

**Unknown:** for five of the eleven kinds of software work (requirements, architecture, internal tools, documentation, ops) there is **no measured evidence at all** — only stats about how often people use AI for them [high on the absence]. Not evidence AI fails there. Just nobody has checked.

## The key insight: writing code faster ≠ shipping faster

Individual coding gains are real. But whole-organisation delivery barely moves in comparison: across hundreds of companies, delivery improved by single digits to low teens percent while AI usage grew 65% (vendor-measured, so trust the direction, not the exact number [D]).

Why the gap? **The bottleneck moved.** Code gets written faster, but reviewing it, testing it, and absorbing it didn't speed up. In the one company measured end to end: code output tripled, human review coverage dropped from 89% to 68%, meaningful review halved, each reviewer's load doubled — and things actually took 22% *longer* to ship [A, one company; the pattern is echoed by two vendors and two other companies, medium-high that it's real, low on exact size].

Can AI review its own output? It can do it cheaply (about $1 per review at Cloudflare [C]) — but where anyone measured quality, AI-only-reviewed changes got accepted 23 points less often and most of the review comments were noise [B]. So automation clears the queue; it doesn't yet replace the judgement.

**Quality:** agent-written code does carry a real maintenance cost — two independent rigorous studies show complexity creeping up and agents struggling to build on top of other agents' code [A, medium]. Interestingly, a controlled trial of the *older* tools found no such cost — this looks like a new, agent-era problem [A]. But there's no trustworthy bug-rate number anywhere: the viral claims in both directions come from conflicted sources measuring different things [not enough evidence].

## Popular claims to stop repeating

- **"Developers report 2–3× gains"** — that's a feeling, not a measurement, and the feelings are getting bigger every year while the measurements aren't.
- **"AI helps juniors most"** — the original evidence was never statistically significant, and the only two agent-era measurements contradict each other [not enough evidence].
- **"X% of our code is AI-generated"**, lines of code, acceptance rates, token usage — all of these are gameable or meaningless. Each has a documented case of pointing the wrong way (see the measurement proposal).
- **"AI is creating copy-paste spaghetti"** — actually the *weakest*-supported version of the quality concern; three independent studies found no duplication increase.

## What we should do

1. **Push AI adoption where the evidence supports it** — new and clean-codebase work — and be patient: the gains compound over months. For old, complex codebases, don't assume either way; measure our own.
2. **Invest in review and verification capacity, not just AI licences.** That's the proven bottleneck. Scaling code generation without scaling absorption just builds a queue.
3. **Measure ourselves.** The companion proposal lists six things to track and seven popular metrics to refuse. Published evidence cannot tell us whether AI works *for us* — on today's data, it can't tell anyone.

*One honest gap: whether AI use erodes engineers' skills over time rests on just two studies (one found a real comprehension cost from AI-assisted learning, with no speed benefit to offset it). We deliberately didn't do a full evidence sweep on this. Treat all skill-formation claims, positive or negative, as open questions.*
