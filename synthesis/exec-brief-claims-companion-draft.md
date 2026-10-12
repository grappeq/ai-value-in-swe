# Ten Claims You Will Hear About AI Coding Tools — Checked

**One-page companion to the exec brief · October 2026 (12 Oct) · generated from the brief's positions; every verdict traces to a graded row in `evidence/evidence-table.tsv`**

How to read each entry: the **claim** as you will hear it in a meeting; the **verdict** — TRUE · PARTLY TRUE · FALSE · UNKNOWN — with our confidence (high / medium / low); the **strength** of the evidence behind it ([A] rigorous experiment · [B] large-scale data without an experiment · [C] credible company account · [D] vendor material), how many *independent* voices support it (shared authors, data or funding count once), and whether it concerns today's agents (E3) or older tools (pre-agentic); and one line of **context** that changes what you should do with it.

---

**1. "Today's AI coding agents have been tested in rigorous trials."**
**FALSE (high).** Strength: our base holds seven randomised trials on working developers from three research groups [A]; none measured a present-day agent conclusively — the best-known found early-2025 agents made experienced developers 19% slower, and its late-2025 re-run was inconclusive. Two independent reviews found the same hole.
Context: what exists for agents is quasi-experimental work from three research groups (one firm's causal study; open-source panels; a 500,000-developer activity panel on Microsoft data) — real evidence, not trials, and none of it measures delivery.

**2. "Developers can tell you how much AI is helping them."**
**FALSE (high).** Strength: four paired designs, four independent voices [A/B], era-independent — self-estimates off by 20–40 points in *both* directions, individual guesses uncorrelated with measured change.
Context: surveys measure morale; they never measure what happened. Budget decisions built on self-reported multiples rest on nothing.

**3. "The AI productivity numbers in the press are reliable."**
**FALSE (high).** Strength: twenty-four documented cases, each with a source record, of numbers corrupted between source and citation — a consultancy report that does not exist, two vendors whose viral multiples appear nowhere in their own reports, one company's cost figure re-attributed to another.
Context: trace every number to its primary; for preprints, cite the version — headline effects have moved 40–200% between revisions.

**4. "Companies know what their AI coding spend buys."**
**FALSE (medium on the pattern).** Strength: organisations that publish spend almost never publish outcomes [C, two organisations plus press]; the one exception pairs a ~20× Claude-only spend rise with a ~1.5–1.7× throughput gain [A, one firm]; Uber's COO says the link "is not there yet" [C].
Context: budgets changed shape in 2026 — seat licences ($100–500 per developer per *year*) gave way to token bills ($200–500 per developer per *month* for a quarter of leaders) [D, spread only], and consumption grows even at flat prices.

**5. "Agents raise individual output."**
**TRUE (medium).** Strength: [A] one firm, causal (PRs per developer 1.46–1.72×) and [B] 500,000 open-source developers (commits +153% for interactive agents) — two voices, both E3, one on Microsoft data with figures that moved between revisions.
Context: output means commits and pull requests, not delivered software (see 6). The one-firm result is self-described as an upper envelope.

**6. "Writing code faster means shipping faster."**
**FALSE (high that the bottleneck moved; medium that it is review specifically).** Strength: [B] commits +153% but releases +20% across 500,000 developers; [A] one firm's output tripled while AI-written changes shipped 22% *slower* and human review coverage fell from 89% to 68%; echoed by three vendors and six other companies; no source shows the opposite.
Context: the 500,000-developer study measures no review time, so testing and sign-off are equally consistent with the data; cheap AI review clears the queue but, where measured, carried little usable signal [B].

**7. "The gains compound with practice — be patient."**
**UNKNOWN (contested).** Strength: the one firm's ≈1.5–1.7× gain built up over nine months [A], but its own data cannot separate practice from newer models, the largest study credits model vintage rather than learning [B], and several panels show gains fading within months [A/B].
Context: do not budget for compounding; measure whether your own gains persist past month three.

**8. "AI works best on new code and worst on old, familiar codebases."**
**PARTLY TRUE (medium — unanimous direction, size contested, one research lineage behind the sharpest numbers).** Strength: [A] one firm (post-2022 repositories +44% vs legacy +12% not significant); [B, pre-agentic] telemetry; [C, self-reported] professionals rate boilerplate and tests suitable (25:0, 19:2) and legacy integration unsuitable (3:17). Mature familiar code: early-2025 agents made experts slower [A]; the re-run was inconclusive [B] — "no demonstrated gain", not a proven loss.
Context: the exception inside old code is mechanical, well-specified change (migrations, upgrades) on self-reported or vendor numbers [C/D, low-medium]; requirements and internal tooling have no outcome evidence at all.

**9. "Agent-written code costs more to maintain."**
**TRUE on direction (medium); size and any effect on defects UNKNOWN.** Strength: [A] two independent studies — complexity and warnings rise and persist; agents resolve follow-on tasks on agent-written code up to 13 points less often; [B] agent merges draw follow-up fixes at 1.6× the odds (low absolute rate). Against: an independent architecture study found no damage beyond code growth [B]; no trustworthy defect-rate number exists.
Context: duplication ("copy-paste spaghetti") is mixed for agents and a watch item; agents with production access have caused real damage in three organisations [C ×3] — existence proofs, not rates.

**10. "Our quality dashboards would catch an AI-driven quality drop."**
**UNPROVEN — do not assume it (medium).** Strength: two documented misses on different data — the maker of Claude Code twice failed to detect user-visible regressions with its own evals (user complaints were the alarm) [D, against interest]; in a lab, routine tool updates with the model unchanged spiked token costs 50–130% and cut solve rates, and every one passed 300+ automated tests [A, lab]. Neither tests dashboards.
Context: keep an explicit complaint and anomaly channel; the companion proposal lists six things to track in cost/outcome pairs and nine metrics to refuse ("% of code written by AI" among them — one 15,000-developer survey's self-reported shares sum to 112%).

---

*Omitted on purpose: "AI helps juniors most" (never statistically significant; the two agent-era measurements disagree — not enough evidence) and whether AI erodes skills over time (two small single-session trials found a comprehension cost; no professional long-horizon study exists — open). Every verdict above mirrors the narrative brief; where that brief changes, this page changes with it.*
