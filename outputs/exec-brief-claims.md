# Ten Claims You Will Hear About AI Coding Tools — Checked

**Companion to the exec brief · October 2026 (12 Oct) · mirrors the brief's positions; every verdict traces to graded rows in `evidence/evidence-table.tsv` or a recorded derivation in `synthesis/`**

Each entry: the **claim**; the **verdict** (TRUE · PARTLY TRUE · FALSE · UNKNOWN) with our confidence (high / medium / low); the **evidence** behind it ([A] rigorous experiment · [B] large-scale data, no experiment · [C] credible company account · [D] vendor material; voices sharing authors, data or funding count once; pre-agentic evidence labelled); and one line of **context**.

---

**1. "Today's AI coding agents have been tested in rigorous trials."**
**FALSE (high).** Our base holds seven randomised trials on working developers from three research groups [A]; none measured a present-day agent conclusively — the best-known found early-2025 agents made experienced developers 19% slower; its re-run was inconclusive. Two independent reviews found the same hole.
Context: agent-era evidence is quasi-experimental, from three groups — one firm's causal study plus open-source panels from the same Stanford–CMU lineage, Microsoft-data studies including a 500,000-developer panel, and one independent academic panel. Real evidence, not trials; it measures output, not delivery.

**2. "Developers can tell you how much AI is helping them."**
**FALSE (high).** Four paired designs, four independent voices [A/B] — three on AI gains, one on self-assessment generally. Self-estimates were off by 20–40 points in *both* directions; individual guesses were uncorrelated with measured change.
Context: surveys measure morale, never what happened.

**3. "The AI productivity numbers in the press are reliable."**
**FALSE (high).** Twenty-four documented cases of numbers corrupted between source and citation: a consultancy report that does not exist, two vendors whose viral multiples appear nowhere in their own reports, one company's cost figure re-attributed to another.
Context: trace every number to its primary; for preprints, cite the version — headline effects have moved 40–200% between revisions.

**4. "Companies know what their AI coding spend buys."**
**FALSE (medium).** Organisations that publish spend almost never publish outcomes [C, two organisations plus press]; the one exception reports ~20× Claude-only spend growth over a period in which throughput rose ~1.5–1.7× (different windows, not a ratio) [A, one firm]; Uber's COO says the link "is not there yet" [C].
Context: seat licences ($100–500 per developer per *year*) are colliding with token bills ($200–500 per developer per *month* for a quarter of leaders) [D, spread only]; consumption grows even at flat prices.

**5. "Agents raise individual output."**
**TRUE (medium).** [A] one firm, causal (PRs per developer 1.46–1.72×; self-described upper envelope) and [B] 500,000 open-source developers (commits +153% for interactive agents; Microsoft data, figures moved between revisions) — two voices. Against: the one trial on experts in familiar code found no gain [A].
Context: output means commits and pull requests, not delivered software (see 6).

**6. "Writing code faster means shipping faster."**
**PARTLY TRUE — only a fraction carries through (high that the bottleneck moved; medium that it is review specifically; low on size).** [B] commits +153% but releases +20% across 500,000 developers; [A] one firm's output tripled while AI-written changes shipped 22% *slower* and human review coverage fell from 89% to 68%; echoed by three vendors and six other companies; no source shows the opposite.
Context: that study measures no review time, so testing and sign-off fit the data equally; cheap AI review clears the queue but, where measured, carried little usable signal [B].

**7. "The gains compound with practice — be patient."**
**UNKNOWN (contested; low).** The one firm's gain built up over nine months [A], but its data cannot separate practice from newer models; the largest study credits model vintage [B]; several panels show gains fading within months [A/B].
Context: do not budget for compounding; measure whether yours persist past month three.

**8. "AI works best on new code and worst on old, familiar codebases."**
**PARTLY TRUE (medium — direction unanimous, size contested, one lineage behind the sharpest numbers).** [A] one firm (post-2022 repositories +44% vs legacy +12%, not significant); [B, pre-agentic] telemetry; [C, self-reported] professionals rate boilerplate and tests suitable (25:0, 19:2), legacy integration unsuitable (3:17). On mature familiar code the only trial found early-2025 agents made experts slower [A]; the re-run was inconclusive [B] — "no demonstrated gain", not a proven loss.
Context: the exception inside old code is mechanical, well-specified change (migrations, upgrades), on self-reported or vendor numbers [C/D, low-medium]. Requirements and internal tooling have no outcome evidence at all.

**9. "Agent-written code costs more to maintain."**
**TRUE on direction (medium); size and any effect on defects UNKNOWN.** [A] two independent studies — complexity and warnings rise and persist; agents resolve follow-on tasks on agent-written code up to 13 points less often; [B] agent merges draw follow-up fixes at 1.6× the odds (low absolute rate). Against: an independent architecture study found no damage beyond code growth [B]; no trustworthy defect-rate number exists.
Context: duplication is mixed for agents — a watch item. Agents with production access have been linked to serious incidents at three organisations [C ×3], one (Amazon) disputed by the company itself — existence proofs, not rates.

**10. "Our quality dashboards would catch an AI-driven quality drop."**
**UNPROVEN — do not assume it (medium).** Two documented misses on different data: the maker of Claude Code twice failed to detect user-visible regressions with its own evals (user complaints were the alarm) [D, against interest]; in a lab, routine tool updates with the model unchanged spiked token costs 50–130% and cut solve rates, all passing 300+ automated tests [A, lab]. Neither tests dashboards.
Context: keep an explicit complaint channel; the measurement proposal lists six things to track in cost/outcome pairs and nine metrics to refuse — "% of code written by AI" among them (one 15,000-developer survey's self-reported shares sum to 112%).

---

*Omitted on purpose: "AI helps juniors most" (never statistically significant; the two agent-era measurements disagree) and whether AI erodes skills over time (two small single-session trials — experienced developers with chat-era AI; students with an early agent versus a chatbot — both found a comprehension cost; no professional long-horizon study exists). Where the brief changes, this page changes with it.*
