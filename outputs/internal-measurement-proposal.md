# Internal Measurement Proposal: Knowing Whether AI Works For Us

**July 2026 · companion to the exec brief · evidence base: synthesis/rq6-measurement.md and the seven tension verdicts**

The published evidence cannot answer whether AI tooling works *for us* — it can only tell us what to instrument and what to avoid. Three design facts drive everything below: (1) individual-level gains dilute severely at system level, so we must measure delivery, not activity [Tier A internal evidence + Tier D direction]; (2) no published organisation pairs cost telemetry with outcome telemetry — the single most repeated measurement failure [high confidence]; (3) self-report is uninformative about magnitude in every paired test ever run [high confidence].

## Six metrics to adopt (organised as three cost/outcome pairs plus two guards)

| # | Metric | What it detects | Design notes (from the evidence) |
|---|---|---|---|
| 1 | **Controlled task/PR throughput per developer** — within-team trend, fixed effects, anti-gaming exclusions | Real velocity change net of calendar drift, hiring, and commit-splitting | The raw version is rejected (metric R2 below); only the controlled version survives. Date adoption *per team*, compare within-team before/after — calendar-trend comparisons are confounded (he-2026; churn-151's design lesson) |
| 2 | **Review absorption**: human review coverage %, substantive-review share, and review latency/queue depth | The bottleneck-displacement early warning — the best-evidenced failure mode in the literature | In the one firm measured, coverage fell 89%→68% and substantive review halved while output doubled; watch composition (agent-steering replacing evaluation), not just coverage |
| 3 | **Stability pair**: revert rate + change-failure rate, tracked together | Whether faster merging costs production stability | The two constructs disagree in the literature (flat reverts vs rising incidents) — we need both, on our own data |
| 4 | **Rework share on AI-touched work** — % of changes substantially revised within 2–4 weeks, with per-team adoption dating | The "gross gains eaten by rework" effect (~half of gross volume in the best telemetry account) | Attribution must be adoption-dated, not calendar-dated; the era's biggest churn controversy was a dataset-composition artefact |
| 5 | **AI spend per developer, paired with metrics 1–3 in the same dashboard** | Cost-to-value ratio — the pairing no published company has done | Expect heavy-tail spend (org averages $150–250/mo; power users $500–2,000/mo; caps are the emerging control). A cost meter without an outcome meter is explicitly rejected |
| 6 | **Experience & skill track, kept separate from productivity claims**: periodic developer-experience survey (sentiment only) + comprehension spot-checks for learning-heavy AI use | Wellbeing/trust trend; the skill-formation risk | Self-report is legitimate here *only because it claims nothing about output*; the comprehension check follows the one RCT showing a measured learning cost (d=0.738) with no speed gain |

Deferred as not yet feasible: downstream-maintenance signal on agent-authored code (the strongest quality-cost evidence, but no practical instrument exists today).

## Seven metrics to reject (each with its documented failure)

1. **Lines of code / volume** — rewards scope creep and bloat; rose 47% in the study where developers got measurably slower.
2. **Raw commit/PR counts** — a 350-person case showed PRs +14% while effective output stayed flat and rework hit 2.5×; counts improved exactly as the process degraded elsewhere too.
3. **Suggestion acceptance rate** — developers accepted <44% of suggestions *while being slowed down*; acceptance and value move independently.
4. **"% of code AI-generated"** — no validated attribution method exists even in academia; the vendor versions disclose no methodology at all.
5. **Token/usage volume as a value proxy** — usage correlates with productivity at only r≈0.2, with a documented "death valley" where heavy usage underperforms; usage leaderboards caused one company's budget blow-out.
6. **Self-reported productivity multipliers** — wrong in both directions in every paired test; inflating over time.
7. **Any single metric alone** — the foundational SPACE warning; every metric above is gameable in isolation, which is why the adopt-list is built as pairs.

## Pilot design principles

- **Within-team, adoption-dated comparisons** — never company-wide calendar trends.
- **Pre-register the outcome metrics** before the pilot starts; do not switch mid-flight.
- **Expect a J-curve but don't assume it**: the "gains take months to compound" claim has one good study behind it (~9 months to peak) and the "dip is temporary" narrative has none — let our data decide.
- **Run it long enough to see decay**: velocity gains in open-source data spike then fade to nothing by month 3–6 in some populations; a 4-week pilot would catch only the spike.
- **Self-report only for sentiment and adoption**, clearly labelled as such, never aggregated into a productivity figure.

## Scope note

The skill-formation instrument (metric 6's comprehension component) rests on deliberately thin evidence — two incidental studies, one E2-era RCT — because the dedicated evidence sweep for this theme was deferred. Treat it as a precautionary instrument, revisit when the theme's literature matures, and never quote the underlying study's absolute quiz percentages (use the effect size, d=0.738).
