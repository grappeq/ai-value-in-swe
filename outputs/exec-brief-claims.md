# Ten things people say about AI coding tools, checked against the evidence

**Companion to the exec brief · October 2026 · same evidence base, same verdicts; every number here has a source record in this repository**

For each claim we say whether it holds up, how sure we are, and what the evidence actually is. Evidence grades: **A** a proper experiment · **B** large-scale data without an experiment · **C** a credible company account · **D** something from a vendor with a product to sell. Where two studies share authors, data or funding, we count them once.

---

### 1. "Today's AI coding agents have been properly tested."

**No. We're confident about this.**

We found seven randomised trials of AI coding tools on working developers, from three research groups. None of them gives a clear answer about current agents. The best-known trial found that early-2025 agents made experienced developers 19% *slower* on code they knew well. The same lab ran it again with late-2025 agents and got an inconclusive result. Two separate literature reviews looked for agent-era evidence and found almost none.

What does exist is a handful of careful observational studies from three groups: one company's internal study, some open-source panels from the same Stanford–CMU lineage, and a 500,000-developer panel built on Microsoft data. Real evidence, but not trials, and they measure code output rather than what gets shipped.

*Evidence: A (seven trials, no clear agent-era result), B.*

### 2. "Just ask the developers how much faster they are."

**No. We're confident.**

Four studies compared what developers said against what was measured (three about AI specifically, one about self-assessment in general). People were wrong by 20 to 40 percentage points, in both directions, and an individual's guess bore almost no relation to the measured change. Surveys tell you how people feel. They don't tell you what happened.

*Evidence: A and B, four independent sources.*

### 3. "The productivity numbers in the press are reliable."

**No. We're confident.**

We traced the numbers we kept meeting back to their sources and found twenty-four cases where they had been bent along the way: a consultancy report that doesn't exist, two vendors whose viral multiples appear nowhere in their own reports, one company's cost figure attributed to another company. Preprints are a separate problem: headline effects have shifted by 40 to 200% between versions of the same paper.

So: trace every number to where it came from, and if it's a preprint, note which version.

### 4. "Companies know what their AI spend is buying them."

**No, with medium confidence.**

Companies that publish what they spend almost never publish what they got for it. We found one exception, a single firm whose Claude spend rose roughly 20-fold over a period when its throughput rose 1.5 to 1.7 times (the two figures cover different windows, so don't treat that as a ratio). Uber's COO has said the link between spend and output "is not there yet".

Meanwhile the bills changed shape in 2026. Seat licences of $100 to $500 per developer per *year* are giving way to token bills of $200 to $500 per developer per *month* for a quarter of the tech leaders surveyed, and usage keeps growing even when prices don't.

*Evidence: C for the pattern, A for the one exception, D for the spend figures (we use the spread, not any single number).*

### 5. "Agents make individual developers more productive."

**Yes, with medium confidence, as long as "productive" means code written.**

One company's causal study put the gain at 1.46 to 1.72 times more pull requests per developer, and describes itself as a best case. A panel of 500,000 open-source developers found commits up 153% for interactive agents (Microsoft data; the figures moved between versions of the paper). Against that, the one trial on experts working in familiar code found no gain at all.

Output means commits and pull requests. It does not mean delivered software. See the next claim.

*Evidence: A (one firm), B (500,000 developers), two sources.*

### 6. "If code gets written faster, software ships faster."

**Partly. Only a fraction of the gain carries through.**

Across those 500,000 developers, commits rose 153% but releases rose 20%. At the one company measured end to end, output tripled while changes written by AI took 22% *longer* to ship, and the share of code getting human review fell from 89% to 68%. Three vendors and six other companies describe the same pattern. Nobody has published the opposite.

We're confident the bottleneck has moved. We're less sure it has moved to code review specifically: the big study doesn't measure review time, so testing and sign-off would fit the data just as well. And we have no good estimate of the size of the effect. Cheap AI review clears the queue, but where anyone measured its quality it added little.

*Evidence: B (500,000 developers), A (one firm), C (six companies), D (three vendors).*

### 7. "The gains compound. Be patient."

**Nobody knows. Low confidence either way.**

The one company's gain did build up over nine months. But its own data can't separate "people got better at using the tool" from "the tool got better", because a placebo release moved the numbers as much as a real one did. The largest study credits newer models rather than practice, and several panels show gains fading within a few months.

Don't budget for compounding. Check whether your own gains are still there after month three.

*Evidence: A and B, all pointing at the same confound.*

### 8. "AI is great on new code and bad on old, complicated codebases."

**Partly. The direction is right; the size is anyone's guess.**

Every source points the same way. At the one firm with causal data, repositories created after 2022 gained 44%; older ones gained 12%, which wasn't statistically significant. Professionals asked where agents help say boilerplate and tests (25 votes to 0, 19 to 2) and where they don't say legacy integration (3 to 17). On mature code that developers know well, the only trial found early-2025 agents made experts slower, and the re-run was inconclusive. Call that "no demonstrated gain", not a proven loss. The sharpest numbers come from one research lineage, so don't lean on the exact figures.

The exception inside old code is mechanical, well-specified work such as migrations and dependency upgrades, though those numbers are self-reported or vendor-told. For requirements work and internal tooling there is no outcome evidence at all.

*Evidence: A (one firm), B (older-tool telemetry), C (self-reported suitability).*

### 9. "Code written by agents costs more to maintain."

**Yes on direction, with medium confidence. How much, and whether it turns into bugs, is unknown.**

Two independent studies found complexity and static-analysis warnings rising and staying up, and agents solving follow-on tasks on agent-written code up to 13 percentage points less often. In another dataset, changes merged by agents needed a follow-up fix 1.6 times as often as human changes, though the absolute rate was low. On the other side, an independent study of architecture found no damage beyond what you'd expect from more code, and nobody has a trustworthy defect rate.

Two things to keep in mind. Duplication ("copy-paste spaghetti") is genuinely mixed for agents; treat it as a watch item. And agents with access to production have been linked to serious incidents at three organisations, one of which (Amazon) disputes the link. Those are proofs that it can happen, not rates.

*Evidence: A (two studies), B (two), C (three incident accounts).*

### 10. "Our quality dashboards would catch it if AI made the code worse."

**Unproven. Don't assume it.**

Two documented misses, from different kinds of data. The maker of Claude Code twice failed to notice that it had shipped a worse version until users complained; its own evaluations didn't catch it. In a lab study, routine updates to an agent's tooling, with the model unchanged, pushed token costs up 50 to 130% and solve rates down, and every one of those updates passed the project's 300-plus automated tests. Neither study tested a dashboard, which is the point: nothing has shown that one would catch this.

Keep a simple channel for people to report "the AI got worse", and read it. The measurement proposal lists six things worth tracking and nine metrics to refuse, "percentage of code written by AI" among them: in one survey of 15,000 developers the self-reported shares added up to 112%.

*Evidence: D (the vendor's own postmortems, against its interest), A (lab study).*

---

*Two claims we left out on purpose. "AI helps juniors most" has never been statistically significant and the two agent-era studies disagree. Whether AI erodes skills over time rests on two small single-session trials, both of which found a comprehension cost, and no long-term study of working professionals exists. When the exec brief changes, this page changes with it.*
