# Source: duolingo-2026-risk-bot

## Identity
- Title: Teaching Engineers, Trusting AI: How Education Enabled Autonomous Code Review
- Speaker: Sarah Deitke, software engineer, Duolingo (DevEx AI team)
- Venue: QCon London 2026, talk dated Wednesday 18 March 2026 (QCon session page); recording published on InfoQ 16 September 2026 (duration 40:07)
- URL: https://www.infoq.com/presentations/duolingo-ai-literacy-code-review/
- QCon page: https://qconlondon.com/presentation/mar2026/teaching-engineers-trusting-ai-how-education-enabled-autonomous-code-review
- Search for a Duolingo engineering-blog post or slide deck on the PR-risk bot: none found. The only Duolingo link surfaced was an unrelated arXiv paper (2511.21964) mentioning Duolingo interest in a diff-risk tool; not this bot.

## What this document is
A practitioner conference talk with Q&A and a transcript, describing Duolingo's AI-literacy programme and an LLM pull-request risk-scoring bot that auto-approves low-risk PRs. Numbers come from internal dashboards and from the speaker's recollection in Q&A.

Fetch limitation (important): the transcript was read through WebFetch, which returns model-summarised output and would not reproduce the full text. Quotes below are short fragments returned by the tool (capped at ~125 characters); surrounding context is paraphrase. Several targeted passes were made, but this is NOT a verified verbatim full read. The orchestrator may wish to have the transcript read directly before any figure reaches the exec brief.

## Full notes
**1. Org context**
- "our engineering org is only 300 people and not 300,000 people." "We have about 200 pull requests that go through a day".
- AI-tool adoption: "we've hit the tail end of getting to 100% AI tool usage adoption"; "Before that, it had been 80%". Timeframe about a year (summary). "around 50% of you are using some agentic coding" (an audience-directed remark).
- Tracking: AI observability dashboards. "We started with just doing a daily active user chart for one or two vendors"; later expanded to functions (engineering, design, finance), communities (iOS, Android, backend), IDEs and languages, token usage, cost and model family. No spend figures given.
- Literacy programme: hands-on lab workshops (MCP servers, Cursor rules, batching LLM requests, evals), office hours ("a 15-minute time slot"), shared-learning channels. "95% of our engineering org reported learning something new" (survey, self-reported).
- Code-owner structure: "we typically have 5 or 6 people that own one codebase, and maybe 20 or 30 people contribute"; "Eighty percent of the code changes in that repo are already from the small group of people".

**2. The bot**
- Inputs: "the PR title, the verification steps, what the actual diff is", plus a user prompt "you are grading this code change on its risk levels". Output: low / medium / high plus a risk explanation; diffs exceeding the token limit get "undetermined".
- Model/vendor: NOT named in the transcript ("Sends that to an LLM"). Project described as "vibe coded".
- Auto-approval of low-risk PRs that meet further criteria. Guardrails: code-owner opt-in only ("only those 5 or 6 people would have the option to turn this on"); directory include/exclude; disabled for AWS resource changes (a preference of most of the org, occasionally debated); "disabled legally for repos that have higher auditing requirements, like SOX or ISO"; "restricted it to new engineers during their onboarding period"; opt-in notifications capped per day.
- Feedback loop: Slack channel proj-pr-risk-score where people report inaccuracies; reports become an eval list labelled by expected risk with keywords from the explanation; used to tune the risk prompt (backward-compatible; she says "fine-tune the risk prompt", read as prompt iteration, not model training).

**3. Outcomes**
- Basis for bucketing: low-risk classification correlated with changes already signed off without comments; "We have like 30% of our code changes with no feedback".
- Merge time: baseline "steady at about 18 hours per pull request"; median "dropping from about 18 hours per pull request to about 12 hours", over about a year, while bot share "climbs from about 0% to about 10% over like the last 6-ish months". She calls it "the correlation"; also describes a "cascading effect" (faster low-risk merges helping other PRs), which leans causal but has no controlled analysis.
- Opt-out: "maybe like 20% to 30% is just ballpark numbers" of authors decline auto-approval and request human review, often for mentorship.
- Reverts: "maybe one or two of those are reverts of the auto approve bot requests" (of ~200 PRs/day). She says it is hard to tell how many reverts were due to lacking a human reviewer, and some reverts are deliberate experiments.
- Defects (Q&A): asked whether any change in defect rate was discerned between auto-approved and manually approved PRs: "For the most part, no." She added the project would likely have been shut down almost immediately had a significant defect rate appeared. This rests on informal revert observation, not a controlled measure.
- Incidents: the bot "to my knowledge, has never been involved in like a side incident" (transcript artefact; probably "site incident").

**4. Not measured / not stated**
- No defect rate, change-failure rate or incident data for bot-approved vs reviewed PRs; no clean attribution of reverts.
- No review-quality measure (what reviewers would have caught on bot-approved PRs).
- No cost of the bot (tokens, latency, maintenance); tokens appear only in dashboard context.
- No quantified productivity gain from the literacy programme (answers were qualitative).
- No model/vendor, no accuracy/precision/recall of risk classification, no false-negative rate.

**5. Caveats and framing gap**
- Speaker's own caveats: correlation not causation; ballpark numbers; revert attribution hard; "to my knowledge".
- InfoQ summary says the case study claims education plus guardrails "sped up delivery without raising defect rates" ("speeds up delivery without increasing defect rates"). The transcript supports only an informal "for the most part, no" and a 1-2 per day revert count. Gap recorded as a red flag. The QCon abstract also says the bot "halves developer wait times", a stronger claim than 18h to 12h median time to merge (about a one-third reduction) and attributes the effect to the bot.

## Tier & era grading
- Tier C: named-organisation practitioner talk with some real numbers, mostly informal. Single source supports directional claims and mechanism hypotheses only (PROTOCOL §3).
- Era: E3 for the bot, which is an LLM pipeline acting autonomously on PRs (approving them without human review), though it is a single-pass classifier rather than a multi-step plan-execute-verify agent; strictly it is autonomous LLM triage plus approval, so E3 on what it does (autonomous merge decision) and E2-like in mechanism (single prompt). The engineers' own coding tools (Cursor etc., ~50% some agentic use) are a separate, unsplit matter and are not what the evidence rows measure.
- COI: no named vendor product for the bot. Speaker is the builder/owner of the programme; self-promotional conference context. Vendor partnerships (early beta access) are mentioned but not tied to the bot. Independence: not independent of the organisation.
- Recency: 2026 talk; nothing to supersede within 12 months.

## Measured vs self-reported
Dashboard-measured (per the talk, method not shown):
- Median time to merge ~18h to ~12h; bot-merged share ~0% to ~10% of PRs; AI tool adoption ~80% to ~100%.
Speaker ballpark / recollection / survey (self-reported):
- ~30% of changes with no feedback; 20-30% opt-out; 1-2 reverts per day; "for the most part, no" defect signal; no known incident; 95% learned something new; ~300 engineers and ~200 PRs/day (descriptive).
Deltas: none reported between perceived and measured outcomes.

## Can / cannot support - verdicts
Can support (directional, Tier C):
- Feasibility of guardrailed LLM auto-approval of low-risk PRs at ~300-engineer scale; guardrail design patterns; a feedback loop via an eval set; evidence that a share of review effort falls on changes that attract no comments (a T7 bottleneck-displacement mechanism).
- Concurrent trend of shorter median time to merge as bot share rose (association only).
Cannot support:
- Any claim that auto-approval does not increase defects or incidents (no controlled or quantified measure).
- Causal attribution of the merge-time change to the bot (AI adoption rose concurrently).
- Cost-benefit (no cost data).
- Transfer to other orgs without the code-owner structure, or to higher-risk codebases.
- Confidence: low-to-medium for the existence of the pattern; low for outcomes.

## Red flags / things the orchestrator should know
1. Summary-vs-transcript gap: InfoQ summary asserts delivery speed-up "without increasing defect rates"; transcript offers "For the most part, no" from informal revert counts. Cite the transcript only.
2. Not a verified full verbatim read: fetch tool returned summaries and short fragments. Re-read directly if a figure is to be quoted in output.
3. Model and vendor unnamed; no classifier accuracy or false-negative rate.
4. Revert count (1-2/day) has no comparison rate for manually reviewed PRs and no denominator for bot-approved PRs (at ~10% of ~200 PRs, roughly 20 per day is an inference, not stated); that would imply a revert rate of order 5-10% of bot-approved PRs, which the speaker does not interpret and which cannot be compared. Treat with caution.
5. Concurrent AI adoption (80% to ~100%) confounds the merge-time trend.
6. Selection: bot restricted to code owners (who author ~80% of changes in a repo), opt-in, excludes new engineers, AWS changes and SOX/ISO repos, so the low-risk population is pre-filtered and favourable.
7. Speaker owns the project; success framing ("would have been shut down").
8. Single organisation: counts as one Tier C source for triangulation.

## Proposed evidence rows (unverified)
```tsv
duolingo-2026-risk-bot	2026	C	E3	Practitioner conference talk (QCon London 2026) plus Q&A; dashboard charts shown; informal counts	Duolingo, ~300 engineers, ~200 PRs/day; LLM PR-risk bot with opt-in auto-approval of low-risk PRs	T7	Design of autonomous PR risk-scoring and auto-approval (LLM grades title, verification steps, diff; low/medium/high/undetermined plus explanation)	Descriptive: ~10% of all PRs merged via the bot after ~6 months; model/vendor not named	n/a	self-reported (design description)	None given for bot (no token or licence spend)	Auto-approval restricted to code owners (5-6 per codebase); blocked for new engineers during onboarding; disabled for AWS resource changes and SOX/ISO repos	Single org; ~20-30 contributors per codebase; ~80% of changes in a repo come from owners; project described as vibe coded	Single org; speaker is the builder; no named vendor product for the bot; no independent measurement	Design detail useful for guardrail patterns; model unnamed; transcript fetched via summarising tool so wording is paraphrase-grade	4
duolingo-2026-risk-bot	2026	C	E3	Speaker recollection from bucketing research (no method given)	Duolingo code changes before the bot	T7	Share of code changes receiving no review feedback	'We have like 30% of our code changes with no feedback' (speaker recollection; no denominator or period)	n/a (baseline)	self-reported (informal)	None	None (pre-bot baseline across org)	Duolingo-wide; low-risk bucket correlated with changes already signed off without comments	Single org; basis for the bot's design so motivated reasoning possible	Suggests review effort on trivial changes is substantial; not an audited figure	3
duolingo-2026-risk-bot	2026	C	E3	Dashboard time series (median time to merge; bot share of PRs); speaker explicitly calls it a correlation; no control	Duolingo PRs org-wide (~200/day)	T7	Median time to merge	About 18h to about 12h over about a year while bot-merged share rose ~0% to ~10% over ~6 months (speaker: 'the correlation'; also describes a 'cascading effect' on medium/high-risk PRs)	Decrease in time to merge (association only)	measured (dashboard; exact method not described)	None	Org-wide; new engineers excluded from auto-approval but included in median	Concurrent AI adoption rising 80% to ~100% is a confound; no pre/post or control group	Same speaker; co-trending confounders (AI adoption, review culture, other tooling)	Correlation only; no causal design; median only, no variance; coincident AI tool adoption not controlled	3
duolingo-2026-risk-bot	2026	C	E3	Speaker ballpark in Q&A	Duolingo authors offered auto-approval	T7	Share of authors declining auto-approval and requesting human review	'maybe like 20% to 30% is just ballpark numbers'	Mixed: opt-out usage, often cited for mentorship	self-reported (ballpark, not measured)	None	Opt-in by code owners; others can still request review	Org-wide	Same speaker	Informal; denominator unclear (PRs vs authors); relevant to review-as-mentoring cost	3
duolingo-2026-risk-bot	2026	C	E3	Informal count in Q&A	Bot-approved PRs at Duolingo (~200 PRs/day overall)	T7	Reverts of bot-approved PRs	'maybe one or two of those are reverts of the auto approve bot requests' per day (informal); speaker says attribution is hard and some reverts are deliberate experiments	No clear direction (no human-reviewed comparison rate)	self-reported (informal count)	None	Org-wide	No comparison revert rate for manually reviewed PRs; some reverts would have occurred anyway	Same speaker	Not a defect-rate measure; no denominator for bot-approved PRs (about 20 per day at 10% share, inferred, not stated); no baseline	3
duolingo-2026-risk-bot	2026	C	E3	Audience Q&A answer; no controlled comparison	Auto-approved vs manually reviewed PRs at Duolingo	T7	Defect-rate difference between auto-approved and manually reviewed PRs	'For the most part, no.' (answer to whether any change in defect rate was discerned); she adds the project would likely have been shut down quickly given a significant defect rate; incident: 'to my knowledge' none involving the bot	Null / no signal observed (informal)	self-reported (informal; rests on revert observations)	None	Org-wide	Same org; no defect metric presented	Speaker is project owner; qualified answer; no incident or defect data shown	Absence of observed signal, not a measured null; low sensitivity; do not cite as 'no increase in defects'	4
duolingo-2026-risk-bot	2026	C	E3	Dashboard adoption tracking plus post-workshop survey	Duolingo engineering org (~300)	T7	AI tool adoption and workshop perceived learning (context for bot trust)	AI tool adoption about 80% to nearly 100% ('tail end of getting to 100%'); 95% reported learning something new from workshops	Increase (adoption); self-reported learning	both: adoption from AI observability dashboards (DAU, vendors, tokens, cost, model family); learning self-reported survey	Dashboards track token usage and cost but no figures given	Org-wide	Org-wide; roughly 50% using some agentic coding (speaker, audience-directed)	Same speaker; workshops are the intervention she advocates	Adoption is usage, not value; 95% is a satisfaction-type survey; no productivity quantification offered	2
duolingo-2026-risk-bot	2026	C	E3	Comparison of InfoQ summary with transcript	InfoQ summary vs speaker statements	T7	Framing gap: 'speeds up delivery without increasing defect rates' vs transcript	Summary asserts no increase in defect rates; transcript supports only 'For the most part, no', informal reverts (1-2/day) and 'to my knowledge' no incident	Overstated by summary	n/a (editorial framing)	None	n/a	n/a	Secondary summarisation by InfoQ; do not cite the summary line as evidence	Red flag: cite the transcript wording only; the summary is not an independent finding	5
```
