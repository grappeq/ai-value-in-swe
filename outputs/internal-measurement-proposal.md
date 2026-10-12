# How To Tell Whether AI Is Working For You

**October 2026 (first issued July 2026; revised 12 Oct) · companion to the exec brief · full reasoning in synthesis/rq6-measurement.md**

Published research can't answer whether AI helps *your* teams. What it can do is tell you how to find out — and which mistakes every other company has already made so you don't repeat them. Three lessons drive this whole proposal:

1. **Individual gains shrink dramatically at company level** — so measure delivery, not activity.
2. **Almost nobody pairs cost data with results data.** One published firm does (spend up ~20× over a period in which throughput rose ~1.5–1.7×); everyone else publishes one or the other. That's the single most common failure, so every cost meter here comes glued to an outcome meter.
3. **What people say tells you nothing about what happened** — shown in every study we found that paired the two (four paired studies so far). Surveys are for morale, never for productivity numbers.

## Six things to track

Built as three cost/result pairs plus two safety checks — deliberately, so no number ever stands alone.

| # | What to track | What it tells you | How to do it right |
|---|---|---|---|
| 1 | **Work shipped per developer — properly controlled** (within-team trend, adjusted for hiring and gaming) | Whether velocity actually changed | Raw counts are on the reject list below. Compare each team against *its own* pre-adoption baseline, dated to when *that team* actually started using AI — company-wide calendar trends are how other people fooled themselves |
| 2 | **Review absorption**: how much code still gets meaningful human review, and how long review takes | The early-warning light for the bottleneck problem | In the best-studied company, review coverage fell 89%→68% and meaningful review halved while output tripled. Watch what *kind* of review is happening, not just whether any happened |
| 3 | **Stability pair**: reverted changes + failed deployments, tracked together | Whether shipping faster is costing you production stability | The two published signals point in opposite directions at different companies — only your own data can settle it for you |
| 4 | **Rework on AI-touched code**: share of changes substantially rewritten within 2–4 weeks | The hidden tax — one dataset suggests rework eats about half the apparent gains | Date it to team adoption, not the calendar; the era's biggest churn scare is contested and may be a data artefact |
| 5 | **AI spend per developer — on the same dashboard as #1–3, tracked in consumption units** | Whether the money buys anything | Budget in tokens, not seats: 2025-style annual seat budgets ($100–500/dev/yr) are an order of magnitude below 2026 token-era reality ($150–500/dev/month averages; power-user tail $500–2,000+). Expect consumption to grow at constant prices (one vendor's own per-day estimate doubled with no price change). Date-stamp and unit-label any benchmark you compare against — and a spend number without a results number next to it is banned by design |
| 6 | **People track, kept separate from productivity**: a morale/experience survey (labelled as sentiment) + occasional comprehension checks where AI is used for learning | Whether the team is healthy, and whether skills are quietly eroding | Surveys are fine *here* because they claim nothing about output. The skill check follows two randomised trials: one (chat-era, experienced developers) found AI-assisted learners understood significantly less (d=0.738) while going no faster; a second (early agent, students) found them faster than a chatbot arm but again understanding less (d>0.8) — and preferring the agent anyway |

One thing you'd want to measure but can't yet: how maintainable AI-written code is over time. The evidence says this is the real cost, but no practical off-the-shelf way to track it exists today. Revisit in a year.

## Nine metrics to refuse — each has already burned someone

1. **Lines of code** — rewards bloat; grew 47% in the very study where developers got slower.
2. **Raw commit/PR counts** — one 350-person team saw PRs rise 14% while real output stayed flat and rework hit 2.5×. Their dashboards said "great"; the truth said "negative ROI". The largest study yet (500,000 open-source developers) saw interactive agents raise commits ~150% while releases rose ~20% (vendor-supplied data; figures shifted between versions).
3. **Suggestion acceptance rate** — developers accepted under 44% of suggestions *while being slowed down*. Acceptance and value simply aren't related.
4. **"% of code that's AI-generated"** — no validated way to compute it exists, even in academia. Vendor versions don't even say how they counted. A 15,000-developer survey's self-reported shares (agent-written, AI-assisted, manual) add up to 112%.
5. **Token/usage volume as a success measure** — usage barely correlates with results (r≈0.2), heavy use can *underperform* moderate use, and one company's own executives blamed its token leaderboard for its budget blow-out.
6. **Self-reported productivity multipliers** — wrong in both directions every time they've been checked, and inflating year on year.
7. **"Time to first review comment"** — becomes automatically zero (and meaningless) the moment an AI comments on every PR; one vendor's rollout demonstrates exactly this. Watch *substantive* review measures instead. Review *duration* is no better: in a large agent-PR dataset, once repository and PR size are controlled, time under review did not predict whether a merge later needed a fix — the number of commits did. And vendor "elite/good" benchmark tiers are customer percentile ranks, not outcome-validated targets.
8. **Agent PR merge/rejection rate** — in the largest open-source data, only about a third of rejected agent PRs demonstrably failed for code reasons; another third died with no recorded reason at all, and the rest died of process (nobody reviewed them, duplicates). So the true failure share is unknown — and per-agent rates differ 2× or more for workflow reasons alone. Either way, a merge rate measures the pipeline, not the agent.
9. **Any single number by itself** — every metric above can be gamed alone; that's exactly why the adopt-list comes in pairs.

## How to run the pilot

- **Each team compared with its own past**, from the date that team actually adopted — never a company-wide before/after.
- **Decide the success metrics before starting**, in writing. No switching mid-pilot.
- **Expect things to get worse before better — but verify it.** The "dip then rise" story is plausible (gains in the best study were still growing at nine months — though that study cannot tell practice from newer models) but no one has actually shown the rise follows a dip. Let your data decide.
- **Run long enough to see the fade.** In open-source data, velocity gains sometimes spike and then vanish by month 3–6. A four-week pilot would catch only the spike and declare victory.
- **Surveys measure mood, and are labelled that way.** They never feed a productivity figure.
- **Keep a standing complaint channel, and treat it as an instrument.** Twice in seven months, the maker of Claude Code shipped quality regressions its own internal testing missed — user complaints were the alarm both times — and it still took weeks for them to be attributed and acted on. Don't assume small quality drops will show up on your dashboards either; a low-friction "the AI got worse" report path, reviewed weekly, is the cheapest early-warning system that demonstrably works.

## Honest limits

The skill-erosion check (#6) rests on deliberately thin evidence — two small randomised trials on single sessions (one chat-era with experienced developers, one early-agent with students), neither on working professionals over time — because we chose not to do a full evidence sweep on that theme. Treat it as a precaution, not a proven risk, and revisit when better research lands. (And if anyone quotes the chat-era study's raw quiz scores at you: those specific percentages never checked out — the effect size, d=0.738, is the number that's safe to use.)
