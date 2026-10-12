# Count Voices, Not Papers: How AI-Productivity Evidence Shrinks When You Check Who's Actually Speaking

**October 2026 · a methods piece from the AI-value evidence base · every example has a source record in this repository**

## The short version

The evidence on AI coding productivity looks plentiful: dozens of papers, reports and company write-ups, many agreeing with each other. But agreement only means something when the sources are independent. While building a graded evidence base (99 sources with findings, 569 extracted findings, collected between July and October 2026), we kept a record every time "several sources agree" turned out to be one voice echoing. It happened constantly.

By the end we had documented **twenty-four cases of numbers being corrupted in transit**, three large clusters where whole groups of "independent" studies share one lab, one dataset or one funder, and two further ways a number can go wrong before it ever leaves its own paper. When you count voices instead of papers, the AI-productivity literature shrinks by more than half. Anyone using this literature to make decisions, and anyone tempted to say "multiple studies confirm", needs to do this counting.

This piece shows what we found, how much the literature shrinks, and the checklist we now use. Our own mistakes are included, because we made the same errors we're warning about, and then had someone check us.

## Eight ways evidence turns out to be fewer voices than it looks

### 1. One lab, many papers

Three of the strongest rigorous studies of agentic coding tools — the enterprise "2× mandate" study, the agents-versus-IDE comparison, and the Cursor velocity-and-quality study — come from the same Carnegie Mellon group. Three papers, three datasets, one research team with one methodology and one view of the world. They tell a consistent story (fast gains, slow quality costs), but that consistency is within-group, not replication.

In August 2026 the picture simplified further, in the wrong direction. The CMU group and the Stanford telemetry programme, which had already shared an author, co-wrote a paper that reuses the CMU panel and estimator unchanged. Five of the most-quoted telemetry studies in this field are now one provenance. Microsoft's internal studies likewise share authors, and the biggest new study of 2026 — a panel of 500,000 GitHub developers — runs on Microsoft data with two Microsoft-paid consultants among its authors, which puts it in the same cluster as the original Copilot trials.

None of this is misconduct. Labs publish repeatedly on their specialty; that's normal science. The error is downstream, when readers count the papers as separate confirmations.

### 2. One dataset, many papers

The fastest-growing corner of this literature — studies of pull requests written by autonomous agents — looks like a thriving independent field: different universities, different countries, different questions. It is almost entirely **one dataset**: AIDev, a public collection of agent-written pull requests. Eleven of the sources in our evidence base stand on it, plus more we didn't extract.

The dataset's method for deciding which PRs are agent-written has no published validation, it over-represents one agent (Codex was around 90% of early volume) and under-represents the tools most companies actually use. The one "validation" paper we found used the dataset's own labels as its ground truth. So when four papers "independently agree" about agent PRs, what has actually been tested once is the dataset's labelling.

By October the monoculture had started contradicting itself. On the same corpus, one group finds that agent-written files receive *less* maintenance than human-written ones; another finds that agent-written merges receive *more* follow-up fixes (1.6 times the odds). Both are right about their own yardstick. Neither can be cited as "what happens to agent code".

### 3. One company's number, wearing other companies' names

Uber's real AI spending figure (around $2,000 a month for heavy users) circulated widely attributed to Microsoft, which never published one. A news site attributed the analytics vendor Faros's throughput numbers to Agoda, a Faros customer mentioned nearby. Four figures that circulate as LinearB's (pull requests up 98%, review time up 91%, PR size up 154%, 1.7 times more issues per PR) are not in LinearB's report at all: three are Faros's and one is CodeRabbit's. Each borrowed number then gets cited as a second, corroborating data point — the same fact counted twice under two names.

### 4. Vendors inflating their own measurements

Three cases where a company's marketing contradicts the company's own research:

- **Atlassian** measured its AI reviewer's effect in a peer-reviewed paper: cycle time down 30.8%. Its blog says 45% — its own result, inflated by half, by itself.
- **Opsera's** viral claim that senior engineers capture about five times the gains of juniors appears nowhere in Opsera's own 19-page report. The report contains one vague sentence with no number. The "5×" exists only in the landing-page marketing.
- **LinearB's** website says agentic pull requests wait 4.6 times longer for review and are reviewed twice as fast once picked up. Its own 48-page report says 5.25 times longer, and reviewed *more slowly*.

The same thing happens outside vendors. Stack Overflow's 2026 survey hub quotes a trust figure that the survey's own data tables don't contain and that contradicts the survey's own headline. A conference publisher's summary turned a speaker's "for the most part, no" (on whether defect rates changed) into "without increasing defect rates", and an 18-hour-to-12-hour change into "halves wait times". Even when the organisation is the primary source, the marketing layer and the report are two different documents. Only the report counts.

### 5. Sources that don't exist

The strangest category. A "Bain Agentic AI Benchmark 2026" was cited across the web with specific percentages. No such document exists; the citation chain dead-ends at SEO content farms citing each other. A story that around 1,500 Amazon engineers signed a petition against an AI-tool mandate traces back to a single social-media post, recycled through blogs until it looked like established fact. A widely repeated claim that agent pull requests "grew ninefold in size over eight months, citing GitHub data" has no GitHub primary behind it; GitHub has published no PR-size figure. And a newsletter headline, "Uber thinks Claude Code makes you 5% better", sits above a post that contains no 5% anywhere. Phantom sources are especially dangerous because they can't be checked against a primary. There's nothing to check.

### 6. Numbers corrupted in ordinary transit

The everyday version: small distortions from summarising.

- METR's famous "developers 19% slower" study had its uncertainty range misquoted in secondary coverage.
- "Developers spend 16% of their time coding" cites a Microsoft paper that actually says about 11%.
- Two agents' merge rates (61.6%, 77.9%) circulated as 42.9% and 81.6%; the 81.6% belongs to a different paper measuring something else.
- "84% of AI PRs go unreviewed" is true, but human PRs in the same repositories go unreviewed at the same rate. A missing baseline, not a scandal.
- A study's adoption-month peak (+41 commits) was quoted as its steady-state effect, which is about half that and fading.
- A famous "21% faster" figure is statistically non-significant in the study's own main model, a caveat that almost never travels.
- DORA renamed its own 2024 construct in 2025 ("stability reduction" became "instability increase"), quietly changing what the number means.
- A survey vendor compared its summer 2026 wave to "a year ago" when the comparison figure appears to be its own January wave, six months earlier.

Each distortion is small. But they compound: a hedged, caveated primary becomes a clean bold claim within two retellings.

### 7. Numbers that move between versions of the same paper

This one isn't transit corruption, because the source itself changes, so we don't count it among the twenty-four. It may matter more. The 500,000-developer study changed its headline cumulative effects from 40/140/180% to 30/180/240%, and its "projects" effect from 50% to 80%, between its May and September 2026 versions, with no change log. Another study's headline effect tripled between v1 and v2 after a measurement rebuild, and the same revision added a GitHub-employed co-author and disclosed Microsoft–GitHub funding. A third hardened its abstract from "limited productivity change" to "spurious" with no new data. A fourth escalated its title from "may decrease" to "decreases".

Preprints move faster than review, and most readers meet only one version. Cite preprints by revision, and treat any effect size that exists in only one version as provisional.

### 8. Papers that disagree with themselves

Four of the papers and reports we read in the autumn carry two incompatible numbers for the same quantity inside one document: an abstract saying "more than 15%" of commits introduce an issue over a body saying 9.1%; prose saying "64% weekly" over a figure implying 64% daily; three productivity percentages that cannot all be true of the same 57 respondents; two different sets of figures for the same token spike. We don't count these either. But they are where transit corruption starts: a downstream writer picks whichever number suits, and from then on it has a citation.

## How much does the literature shrink? Three worked examples

**The agent-PR field:** eleven-plus papers become effectively **one voice** (the AIDev dataset), whose labelling method has never been independently validated and which now disagrees with itself on maintenance.

**"AI code creates quality debt":** six apparent lines of evidence become **two genuinely independent rigorous ones** once the Stanford–CMU papers are merged into one voice and the vendor-conflicted sources are set aside. The claim survives, but as "two independent studies, medium confidence", not the chorus it appears to be. A fourth leg we added in October, a lab study showing that agent-tool updates can degrade quality while passing every automated test, turned out on closer reading to share two authors with the AIDev papers: independent data, but not an independent voice.

**"Juniors benefit most" (or is it seniors?):** what looks like several voices becomes **two real agent-era measurements that contradict each other**, plus one vendor number that isn't in the vendor's own report. The honest answer is "unknown".

This is the general pattern: the direction of major findings often survives the audit; the confidence and the magnitude rarely do.

## It happened to us too

We are not writing from a position of immunity.

- We graded one study "independent of all clusters". Its next preprint version added a GitHub-employed co-author and disclosed Microsoft–GitHub funding, and its headline effect tripled. We had to retract our own independence grading.
- We inherited the 42.9%/81.6% misattribution into our own notes before full reads caught it.
- When our final documents were independently reviewed in July, the reviewer found our summaries had drifted the way secondary coverage does: "22% longer to ship for AI-written changes versus comparable human ones" had become "things took 22% longer to ship"; one incident's measured 3% quality drop had attached itself to two incidents.
- In October we labelled the lab study above "a genuinely new voice" in our own independence map; a reviewer caught the shared authors. We described both skill-formation trials as run "on students"; one was run on experienced developers. And the first version of this count was twenty-five: one case had no source record behind it, and one was the authors' own revision, which belongs under pattern 7, not pattern 6. The number you are reading is the one that survived review.

That last point names the mechanism precisely: **shortening a claim quietly widens it.** Nobody sets out to distort; summarising does it for you. Vigilance is not a fix. Process is.

## We checked whether our conclusions were ours or the evidence's

Five cycles of reading and re-reading can build a frame that then reads itself into every new source. So in October we ran a test: a fresh analyst, a different model from the one that wrote our synthesis, was given only the extraction records and the evidence table, with the research questions but none of our tensions, verdicts, outputs or git history, in a directory with no network access. It had to find the fault lines itself.

It reproduced 23 of our 24 scored positions in the same direction, rebuilt all four provenance clusters nearly member for member, and was never more confident than we were. Two referees scoring its output against ours, from different model families, returned identical scorecards. Where it differed from us, it was right: we had let "gains compound with practice" into our brief when our own memos said the evidence was confounded, and we had kept a "high" confidence after the evidence under it had been reduced to Tier C. Both are fixed. The lesson is the same one as the rest of this piece: the direction held; the confidence had drifted upward on its own.

## The checklist

What we now do before believing (or repeating) any AI-productivity claim:

1. **Trace the number to its primary document.** Never cite from a summary, a news story or another paper's related-work section. In this literature, secondary coverage is unreliable as a class.
2. **Count voices.** For any set of "agreeing" sources ask: shared authors? shared dataset? shared funder or vendor relationship? Merge everything that shares any of these into one voice before counting.
3. **Read the report behind the marketing.** If a number isn't in the organisation's own full document, it doesn't exist.
4. **Check preprint version history, and name the version.** Titles that escalate, affiliations that appear, headline numbers that jump between versions are all warnings, and a number without a version is a number without a date.
5. **Ask "compared to what?"** Alarming rates often dissolve against a matched baseline.
6. **Ask "when?"** Adoption-month spikes are not steady states; many gains fade by month three.
7. **Check significance and uncertainty.** Several of this field's most-quoted numbers are non-significant in their own primary analysis.
8. **Treat aggregators as pointers, never as sources.** If a claim can't be walked back to a primary, drop it, however often it's repeated.
9. **Have someone outside the work re-derive your conclusions from your evidence.** It is the only check that catches your own framing.

## Why this keeps happening

Not fraud, mostly structure. Rigorous field data requires telemetry access that only a few labs and companies have, so the few who have it publish repeatedly, and everyone else re-analyses the one public dataset. Vendors fund and publish much of the rest, with marketing teams downstream of their own researchers. Preprints move faster than review, so version drift is invisible. And SEO content farms recycle statistics endlessly, giving every number, real or phantom, a long second life detached from its source.

None of these forces is going away. The auditing burden is permanent, and it belongs to the reader.

## Honest limits

This is one research programme's corpus, assembled to answer specific questions, not a random sample of the literature. The twenty-four documented corruption cases are a lower bound, since we only caught what we happened to trace, and the count itself was revised once after review. We are not alleging misconduct in any named case: nearly everything here is ordinary compression, copying and marketing doing what they always do. That is exactly the point. It takes no bad actors for a literature to end up sounding far more certain, and far more numerous, than it is.

*Every example above has a source record and grading in this repository (`sources/`, `synthesis/contradictions.md`, `synthesis/rederivation-r4.md` §E, `synthesis/cleanroom-r5-protocol.md`). The evidence rules that generated them are in `PROTOCOL.md` §3.*
