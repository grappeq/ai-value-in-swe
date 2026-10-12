# AI Coding Tools: What the Evidence Actually Says

**Two pages · October 2026 (revised 12 Oct) · based on 99 sources (101 records) and 569 extracted findings · everything traceable in this repository**

How to read the tags: **[A]** = rigorous experiment, **[B]** = large-scale data without an experiment, **[C]** = credible company account, **[D]** = vendor material (they have something to sell). Plus how sure we are: high / medium / low.

---

## The big picture: today's AI agents have barely been measured — and never conclusively in a trial

Almost every famous number — "55% faster", "26% more output" — comes from old autocomplete tools (the 55% was a toy web server built from scratch), not today's agents doing real work.

Our evidence base holds seven randomised trials of AI coding productivity on working developers, from three research groups; none measured a present-day agent conclusively. The best-known, by the research lab METR, found experienced developers on codebases they knew well got **19% slower** with early-2025 agents, while convinced they were 20% faster [A, high]. Its late-2025 re-run lost the slowdown but was inconclusive, and the design has been abandoned because enough developers now refuse some tasks without AI that the comparison broke down [B, medium]. Beyond trials, today's agents have quasi-experimental evidence from three research groups — one firm's causal study and open-source panels from the same Stanford–CMU lineage, Microsoft-data studies including a 500,000-developer panel, and one independent panel: real, but no trial and no delivery outcome. Two independent reviews found the same hole: a 10,000-study screen had two agent-era productivity measurements, and a 45-paper review named no agentic tool at all [A, high].

Rule one, then: treat every AI velocity claim — vendor, press, or your own gut — with suspicion.

## Three things we're genuinely sure about

1. **Don't trust what developers say about their own AI gains — including your own team's.** Four studies paired what people said against what was measured (three on AI gains, one on self-assessment generally). People were off by roughly 20–40 points, in both directions, and individual guesses were basically uncorrelated with reality [A/B, high]. Surveys tell you how people feel — never what happened.
2. **Numbers get mangled as they travel.** We caught twenty-four cases of press, vendors and aggregators corrupting numbers: a consultancy "benchmark report" that doesn't exist, a vendor whose marketing inflates its own peer-reviewed measurement by half, two others whose viral stats ("5×", "4.6×") appear nowhere in their own reports. The "$2,000/month at Microsoft" you may have seen is Uber's number. Rule: never act on an AI number that hasn't been traced to its original source — and, for preprints, its version, since headline effects have moved 40–200% between versions [high].
3. **Companies are spending without checking what they get back — and the spending changed shape.** Seat-licence budgets (typically $100–500 per developer per *year* in 2025) are colliding with token-era bills: a quarter of tech leaders now report $200–500 per developer per *month*, and 6% exceed $2,000 [D — we use only the spread]. Consumption grows even at flat prices: Anthropic's own per-day cost estimate doubled with no price change. Yet organisations that publish costs almost never publish what the money bought — the one exception is a single firm's study, where Claude-only spend rose ~20× over a period in which throughput rose ~1.5–1.7×; Uber's own COO says the productivity link "is not there yet" [C, medium on the pattern].

## Where AI helps, and where it doesn't

**Best case:** new code in clean, newer codebases [A/B, medium — one research lineage]. The gains are real; whether they *last* is contested. The best-documented company's ≈1.5–1.7× throughput gain built up over about nine months — but its own data cannot separate practice from newer models, the largest study credits model vintage rather than learning, and several panels show gains fading within months [A/B, contested].

**Worst case:** big, old, complicated codebases that developers already know inside out. The one rigorous trial in that setting found early-2025 agents made people slower [A]; the late-2025 re-run lost the slowdown but was inconclusive [B]. Treat it as "no demonstrated gain", not a proven loss. Rare languages, messy codebases and performance work also do badly [B, medium — partly pre-agentic].

**One exception inside old code:** mechanical, well-specified changes — migrations, dependency upgrades — are where agents report their best results, though on self-reported or vendor-told numbers [C/D, low-medium]. The struggle zone is open-ended feature work needing context the agent doesn't have.

**Unknown:** requirements and internal tooling have no outcome evidence at all; architecture and documentation have only usage data; debugging has no agent-era measurement [high on the absence]. Not proof AI fails there; nobody has checked.

## The key insight: writing code faster ≠ shipping faster

Individual coding gains are real. But whole-organisation output barely moves: across ~400 companies, pull-request throughput rose about 8% while AI usage grew 65% [D, direction only].

Why the gap? **The bottleneck moved.** The largest measurement yet (500,000 open-source developers) found agents raised commits ~150% but releases only ~20% [B; Microsoft data, figures unstable between revisions]. In the one company measured end to end: output tripled, human review coverage fell from 89% to 68%, meaningful review halved, each reviewer's load doubled — and AI-written changes took 22% *longer* to ship than comparable human-written ones [A, one company; echoed by three vendors and six other companies — high that the bottleneck moved, medium that it is review specifically, low on size].

Can AI review its own output? Cheaply, yes (about $1 per review at Cloudflare [C]) — but where quality was measured, AI-only-reviewed changes were accepted 23 points less often and most carried little usable signal [B]. Who does the later clean-up is contested — two studies on the same data give opposite readings by different yardsticks [B]. Automation clears the queue; it doesn't yet replace the judgement.

**Quality:** agent-written code carries a real maintenance cost — two independent rigorous studies show complexity creeping up and agents struggling to build on other agents' code [A, medium]; a trial of the *older* tools found no such cost, so this looks agent-era [A]. But an independent architecture study found no damage beyond what code growth explains [B], and no trustworthy bug-rate number exists [not enough evidence]. Agents with production access have caused real damage — a deleted production database, a human-approved Terraform destroy, Amazon's contested outages — existence proofs, not rates [C ×3]. And quality drift is hard to see: Claude Code's own maker twice missed user-visible regressions with its internal testing (user complaints were the alarm), and a lab study found routine tool updates, model unchanged, spiking token costs and cutting solve rates while passing 300+ automated tests [D, against interest; A, lab, medium]. Don't assume your dashboards would catch small drops either; the measurement proposal adds a complaint channel for exactly this.

## Popular claims to stop repeating

- **"Developers report 2–3× gains"** — a feeling, not a measurement [C, one survey]; self-reported multiples have risen faster than any measured gain.
- **"AI helps juniors most"** — never statistically significant, and the only two agent-era measurements contradict each other [not enough evidence].
- **"X% of our code is AI-generated"**, lines of code, acceptance rates, token usage — all gameable or meaningless; one 15,000-developer survey's self-reported code shares add up to 112% (see the measurement proposal).
- **"AI is creating copy-paste spaghetti"** — not supported for the older tools (one study found AI-attributed code *less* duplicated); for agents the evidence is mixed — one research group's estimates go both ways on the same data, and a single-repository study found more redundancy. A watch item, not settled either way.

## What to do with this

1. **Push AI adoption where the evidence supports it** — new and clean-codebase work — and don't bank on gains compounding: several studies show them fading, so measure whether yours persist. For old, complex codebases, don't assume either way; measure your own.
2. **Invest in review, testing and sign-off capacity, not just AI licences.** That's where the bottleneck has moved; which of them binds for you is worth measuring.
3. **Measure yourself.** The companion proposal lists six things to track and nine popular metrics to refuse. Published evidence cannot tell you whether AI works for *your* teams — on today's data, it can't tell anyone.

*One honest gap: whether AI use erodes engineers' skills over time rests on two small randomised trials — one on experienced developers using chat-style AI (pre-agentic), one on students using an early agent compared with a chatbot — both found a real comprehension cost; the agent arm was faster than the chatbot arm, and participants preferred the agent anyway. No professional, long-horizon study exists. Treat all skill-formation claims, positive or negative, as open questions.*
