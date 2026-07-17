# Count Voices, Not Papers: How AI-Productivity Evidence Shrinks When You Check Who's Actually Speaking

**July 2026 · a methods piece from the AI-value evidence base · every example traceable to a source record in this repository**

## The short version

The evidence on AI coding productivity looks plentiful: dozens of papers, reports, and company write-ups, many agreeing with each other. But agreement only means something when the sources are actually independent. While building a graded evidence base (74 sources, 362 extracted findings), we kept a record every time "several sources agree" turned out to be one voice echoing. It happened constantly.

By the end we had documented **seventeen cases of numbers being corrupted in transit** and three large clusters where whole groups of "independent" studies share one lab, one dataset, or one funder. When you count voices instead of papers, the AI-productivity literature shrinks by more than half. Anyone using this literature to make decisions — and anyone tempted to say "multiple studies confirm" — needs to do this counting.

This piece shows what we found, how much the literature shrinks, and the checklist we now use. Our own mistakes are included, because we made the same errors we're warning about.

## Six ways "independent" evidence turns out to be one voice

### 1. One lab, many papers

Three of the strongest rigorous studies of agentic coding tools — the enterprise "2× mandate" study, the agents-vs-IDE comparison, and the Cursor velocity-and-quality study — come from the same Carnegie Mellon group. Three papers, three datasets, one research team with one methodology and one view of the world. They tell a consistent story (fast gains, slow quality costs), but that consistency is *within-group*, not replication. The 2×-mandate paper also shares an author with the Stanford telemetry programme — so when "CMU" and "Stanford" agree that gains shrink in older codebases, that is partly the same person agreeing with himself. Microsoft's two internal studies likewise share an author.

None of this is misconduct. Labs publish repeatedly on their specialty; that's normal science. The error is downstream, when readers count the papers as separate confirmations.

### 2. One dataset, many papers

The fastest-growing corner of this literature — studies of pull requests written by autonomous agents — looks like a thriving independent field: different universities, different countries, different questions. It is almost entirely **one dataset**: AIDev, a public collection of agent-written pull requests. **Ten of the sources in our own evidence base stand on it**, plus more we didn't extract.

Worse, the dataset's method for deciding which PRs are agent-written has *no published validation*, it over-represents one agent (Codex was ~90% of early volume) and under-represents the tools most companies actually use. The one "validation" paper we found used the dataset's own labels as its ground truth — circular. So when four papers "independently agree" about agent PRs, what has actually been tested once is the dataset's labelling.

### 3. One company's number, wearing other companies' names

Uber's real AI spending figure (~$2,000/month for heavy users) circulated widely attributed to *Microsoft* — Microsoft never published one. A news site attributed the analytics vendor Faros's throughput numbers to *Agoda*, a Faros customer mentioned nearby. Each borrowed number then gets cited as a second, corroborating data point — the same fact counted twice under two names.

### 4. Vendors inflating their own measurements

Two cases where a company's marketing contradicts the company's own research:

- **Atlassian** measured its AI reviewer's effect in a peer-reviewed paper: cycle time down 30.8%. Its blog says 45% — its own result, inflated by half, by itself.
- **Opsera's** viral claim that "senior engineers capture ~5× the gains of juniors" appears **nowhere in Opsera's own 19-page report**. The report contains one vague sentence with no number. The "5×" exists only in the landing-page marketing.

Lesson: even when the vendor is the primary source, the *marketing layer* and the *report* are two different documents. Only the report counts.

### 5. Sources that don't exist

The strangest category. A "Bain Agentic AI Benchmark 2026" was cited across the web with specific percentages — **no such document exists**; the citation chain dead-ends at SEO content farms citing each other. A story that ~1,500 Amazon engineers signed a petition against an AI-tool mandate traces back to a single social-media post, recycled through blogs until it looked like established fact. Phantom sources are especially dangerous because they can't be checked against a primary — there's nothing to check.

### 6. Numbers corrupted in ordinary transit

The everyday version — small distortions from summarising:

- METR's famous "developers 19% slower" study had its uncertainty range misquoted in secondary coverage.
- "Developers spend 16% of their time coding" cites a Microsoft paper that actually says ~11%.
- Two agents' merge rates (61.6%, 77.9%) circulated as 42.9% and 81.6% — the 81.6% belongs to a different paper measuring something else.
- "84% of AI PRs go unreviewed" — true, but human PRs in the same repositories go unreviewed at the same rate (a missing baseline, not a scandal).
- A study's adoption-month *peak* (+41 commits) was quoted as its steady-state effect (~half that, fading fast).
- A famous "21% faster" figure is statistically non-significant in the study's own main model — a caveat that almost never travels.
- DORA renamed its own 2024 construct in 2025 ("stability reduction" became "instability increase"), quietly changing what the number means.

Each distortion is small. But they compound: a hedged, caveated primary becomes a clean bold claim within two retellings.

## How much does the literature shrink? Three worked examples

**The agent-PR field:** ten-plus papers → effectively **one voice** (the AIDev dataset), whose labelling method has never been independently validated.

**"AI code creates quality debt":** six apparent lines of evidence → **two genuinely independent rigorous ones** once the CMU papers are merged into one voice and the vendor-conflicted sources are set aside. The claim survives, but as "two independent studies, medium confidence" — not the chorus it appears to be.

**"Juniors benefit most" (or is it seniors?):** what looks like several voices → **two real agent-era measurements, which contradict each other**, plus one vendor number that isn't in the vendor's own report. The honest answer is "unknown".

This is the general pattern: the *direction* of major findings often survives the audit; the *confidence* and the *magnitude* rarely do.

## It happened to us too

We are not writing from a position of immunity:

- We graded one study "independent of all clusters". Its next preprint version added a GitHub-employed co-author and disclosed Microsoft–GitHub funding — and its headline effect *tripled* after a measurement change. We had to retract our own independence grading.
- We inherited the 42.9%/81.6% misattribution into our own notes before full reads caught it.
- When we had our final documents independently reviewed, the reviewer found our own summaries had drifted the same way secondary coverage does: a "22% shipping delay for AI-written changes vs comparable human ones" had become "things took 22% longer to ship"; one incident's measured 3% quality drop had attached itself to two incidents.

That last finding names the mechanism precisely: **shortening a claim quietly widens it.** Nobody sets out to distort; summarising does it for you. Which means vigilance is not a fix — *process* is.

## The checklist

What we now do before believing (or repeating) any AI-productivity claim:

1. **Trace the number to its primary document.** Never cite from a summary, a news story, or another paper's related-work section. In this literature, secondary coverage is unreliable as a class.
2. **Count voices.** For any set of "agreeing" sources ask: shared authors? shared dataset? shared funder or vendor relationship? Merge everything that shares any of these into one voice before counting.
3. **Read the report behind the marketing.** If a vendor number isn't in the vendor's own full document, it doesn't exist.
4. **Check preprint version history.** Titles that escalate ("may decrease" → "decreases"), affiliations that appear, headline numbers that jump between versions — all are warnings.
5. **Ask "compared to what?"** Alarming rates often dissolve against a matched baseline.
6. **Ask "when?"** Adoption-month spikes are not steady states; many gains fade by month three.
7. **Check significance and uncertainty.** Several of this field's most-quoted numbers are non-significant in their own primary analysis.
8. **Treat aggregators as pointers, never as sources.** If a claim can't be walked back to a primary, drop it — however often it's repeated.

## Why this keeps happening

Not fraud, mostly structure. Rigorous field data requires telemetry access that only a few labs and companies have — so the few who have it publish repeatedly, and everyone else re-analyses the one public dataset. Vendors fund and publish much of the rest, with marketing teams downstream of their own researchers. Preprints move faster than review, so version drift is invisible. And SEO content farms recycle statistics endlessly, giving every number — real or phantom — a long second life detached from its source.

None of these forces is going away. The auditing burden is therefore permanent, and it belongs to the reader.

## Honest limits

This is one research programme's corpus, assembled to answer specific questions — not a random sample of the literature; the seventeen documented corruption cases are a *lower bound*, since we only caught what we happened to trace. We are not alleging misconduct in any named case: nearly everything here is ordinary compression, copying, and marketing doing what they always do. That is exactly the point — it takes no bad actors for a literature to end up sounding far more certain, and far more numerous, than it is.

*Every example above has a source record and grading in this repository (`sources/`, `synthesis/contradictions.md`, `synthesis/rq2-measurement-methods.md` §4). The evidence rules that generated them are in `PROTOCOL.md` §3.*
