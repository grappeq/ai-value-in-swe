# How To Tell Whether AI Is Working For Us

**July 2026 · companion to the exec brief · full reasoning in synthesis/rq6-measurement.md**

Published research can't answer whether AI helps *our* teams. What it can do is tell us how to find out — and which mistakes every other company has already made so we don't repeat them. Three lessons drive this whole proposal:

1. **Individual gains shrink dramatically at company level** — so measure delivery, not activity.
2. **Nobody pairs cost data with results data.** Not one published company. That's the single most common failure, so every cost meter here comes glued to an outcome meter.
3. **What people say tells you nothing about what happened** — proven in every study that ever checked. Surveys are for morale, never for productivity numbers.

## Six things to track

Built as three cost/result pairs plus two safety checks — deliberately, so no number ever stands alone.

| # | What to track | What it tells us | How to do it right |
|---|---|---|---|
| 1 | **Work shipped per developer — properly controlled** (within-team trend, adjusted for hiring and gaming) | Whether velocity actually changed | Raw counts are on the reject list below. Compare each team against *its own* pre-adoption baseline, dated to when *that team* actually started using AI — company-wide calendar trends are how other people fooled themselves |
| 2 | **Review absorption**: how much code still gets meaningful human review, and how long review takes | The early-warning light for the bottleneck problem | In the best-studied company, review coverage fell 89%→68% and meaningful review halved while output tripled. Watch what *kind* of review is happening, not just whether any happened |
| 3 | **Stability pair**: reverted changes + failed deployments, tracked together | Whether shipping faster is costing us production stability | The two published signals point in opposite directions at different companies — only our own data can settle it for us |
| 4 | **Rework on AI-touched code**: share of changes substantially rewritten within 2–4 weeks | The hidden tax — one dataset suggests rework eats about half the apparent gains | Date it to team adoption, not the calendar; the era's biggest churn scare turned out to be a data artefact |
| 5 | **AI spend per developer — on the same dashboard as #1–3, tracked in consumption units** | Whether the money buys anything | Budget in tokens, not seats: 2025-style annual seat budgets ($100–500/dev/yr) are an order of magnitude below 2026 token-era reality ($150–500/dev/month averages; power-user tail $500–2,000+). Expect consumption to grow at constant prices (one vendor's own per-day estimate doubled in three months). Date-stamp and unit-label any benchmark you compare against — and a spend number without a results number next to it is banned by design |
| 6 | **People track, kept separate from productivity**: a morale/experience survey (labelled as sentiment) + occasional comprehension checks where AI is used for learning | Whether the team is healthy, and whether skills are quietly eroding | Surveys are fine *here* because they claim nothing about output. The skill check follows the one trial showing AI-assisted learners understood significantly less (effect size d=0.738) while going no faster |

One thing we'd like to measure but can't yet: how maintainable AI-written code is over time. The evidence says this is the real cost, but no practical off-the-shelf way to track it exists today. Revisit in a year.

## Eight metrics to refuse — each has already burned someone

1. **Lines of code** — rewards bloat; grew 47% in the very study where developers got slower.
2. **Raw commit/PR counts** — one 350-person team saw PRs rise 14% while real output stayed flat and rework hit 2.5×. Their dashboards said "great"; the truth said "negative ROI".
3. **Suggestion acceptance rate** — developers accepted under 44% of suggestions *while being slowed down*. Acceptance and value simply aren't related.
4. **"% of code that's AI-generated"** — no validated way to compute it exists, even in academia. Vendor versions don't even say how they counted.
5. **Token/usage volume as a success measure** — usage barely correlates with results (r≈0.2), heavy use can *underperform* moderate use, and one company's token leaderboard directly caused its budget blow-out.
6. **Self-reported productivity multipliers** — wrong in both directions every time they've been checked, and inflating year on year.
7. **"Time to first review comment"** — becomes automatically zero (and meaningless) the moment an AI comments on every PR; one vendor's rollout demonstrates exactly this. Watch *substantive* review measures instead.
8. **Any single number by itself** — every metric above can be gamed alone; that's exactly why the adopt-list comes in pairs.

## How to run the pilot

- **Each team compared with its own past**, from the date that team actually adopted — never a company-wide before/after.
- **Decide the success metrics before starting**, in writing. No switching mid-pilot.
- **Expect things to get worse before better — but verify it.** The "dip then rise" story is plausible (the best study took ~9 months to peak) but no one has actually proven the rise follows the dip. Let our data decide.
- **Run long enough to see the fade.** In open-source data, velocity gains sometimes spike and then vanish by month 3–6. A four-week pilot would catch only the spike and declare victory.
- **Surveys measure mood, and are labelled that way.** They never feed a productivity figure.

## Honest limits

The skill-erosion check (#6) rests on deliberately thin evidence — two studies, found incidentally, one of them from the pre-agent era — because we chose not to do a full evidence sweep on that theme. Treat it as a precaution, not a proven risk, and revisit when better research lands. (And if anyone quotes that study's raw quiz scores at you: those specific percentages never checked out — the effect size, d=0.738, is the number that's safe to use.)
