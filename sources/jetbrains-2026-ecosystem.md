# Source: jetbrains-2026-ecosystem

## Identity
- Title: JetBrains Developer Ecosystem Survey 2026 (10th edition), AI sections as published in two JetBrains Research blog posts
- Posts: (1) "AI coding agent adoption 2026", blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ (Mikhail Bogdanov, Aug 2026); (2) "How Much Code Do Developers Really Let Agents Write?", blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/ (Aug 2026). Context: (3) "Which AI Coding Tools Do Developers Actually Use at Work?", April 2026 (January 2026 AI Pulse wave); (4) Developer Ecosystem methodology page.
- Publisher: JetBrains (vendor; sells JetBrains AI, Junie, Air, JetBrains Central)
- Fielding: May-July 2026; "over 15,000 professional developers"; eight languages
- Access note: pages were read through the WebFetch summariser (small-model paraphrase), not as raw HTML; question wording and figures below are as relayed by that tool and cross-checked across two fetches where possible. Re-verify exact numbers against the live pages before they reach the exec brief.
- Not found: the survey's own AI chapter (jetbrains.com/lp/devecosystem-2026/ai/ returned 404) and a 2026 methodology page. The survey-side data pages were therefore NOT read; all 2026 figures come from the blog posts. The "How much code" post says it was the survey chapter's companion; trust, satisfaction, productivity-perception and "why not" items were not found anywhere and may not yet be published (a search result states more agentic-practice findings are "still to come").

## What this document is
A vendor-published survey readout. Post 1 reports tool adoption (work use) and a headline agent-use rate. Post 2 reports self-estimated share of work code produced last month by agents, with AI assistance, or manually, plus a cluster segmentation and breakdowns by tool, language, region and seniority. No outcome, quality, productivity, trust or cost measures.

## Full notes

### 1. Methodology
- Sample: "over 15,000 professional developers worldwide" (no exact n). Subgroup Ns (tool, language, region, seniority, segment, US) are not given anywhere.
- Fielding: May-July 2026 (no exact dates found).
- "Professional developers": six roles - Developer/Programmer/Software Engineer; AI/ML Engineer; DevOps/Infrastructure; Architect; Data Scientist/Engineer/Analyst; QA Engineer. About 90% are Developer/Programmer/SWE.
- Localised into eight languages; regional quotas proportional to estimated developer populations; statistically reweighted by region, employment status, programming language, and familiarity with JetBrains products (per posts 1 and 2). Weighting procedure itself (raking? targets?) is not described for 2026. By analogy only: the 2025 edition (n=24,534, 194 countries, April-June 2025) was balanced by geography, employment, languages and JetBrains product use, and JetBrains itself cautions JetBrains users may have been more likely to respond.
- Recruitment channels for 2026 not found. The January 2026 AI Pulse wave (post 3) used Instagram ads, Zhihu in China, and about 16% from the JetBrains research panel; promotion did not mention AI or JetBrains; raking to the 2025 survey on region, coding experience and JetBrains familiarity. Not a probability sample.
- Comparison wave: January 2026 "AI Pulse" wave, "over 10,000" professional developers (post 3). Post 1 does NOT itself describe that wave; the link is inferred from matching figures (Claude Code 18%, Codex 3%/27% awareness, Cursor 18%/69% awareness, all appear in post 3). Note also a September 2025 AI Pulse wave exists. Wave weighting differs in variables: January weights on region/coding experience/JetBrains familiarity; May-July on region/employment/language/JetBrains familiarity. Composition effects across waves cannot be excluded.
- Data cleaning (post 2): dropped "unrealistic" code-share answers (sum of lower bounds >150% or sum of upper bounds <80%).

### 2. Adoption (post 1; work use; "professional developers")
- AI coding agents "in one form or another (local agents or remote cloud agents)": 90% use at least weekly at work; 68% daily. "Agent" is not defined and not separated from assistants; no question wording or base N given. Comparison: January 2026 wave reported 90% "regularly use at least one AI tool" for coding (any AI tool, post 3). The same 90% figure therefore appears for two different constructs.
- Claude Code: 39% worldwide (May-Jul 2026) vs 18% (January 2026); US 47% (no base; January wave US and Canada combined was 24%); "most used AI coding tool for 31% of developers"; post calls 31/39 "an almost 80% conversion rate" from regular use to single most-used tool; "used twice as often as GitHub Copilot" (39% vs 21%).
- Codex: 16% vs 3% (January 2026); awareness 27% -> 65%. January 3% pre-dated the Codex desktop app launch.
- GitHub Copilot: 21% (May-Jul 2026) vs 29% "a year ago"; awareness 79% (86-90% in Europe, UK, US); 39% of its users use it in JetBrains IDEs. Post 3 reports Copilot at 29% in January 2026, so the "a year ago" 29% is plausibly the January 2026 wave (a ~6-month comparison), not a 12-month one; the post does not name the prior wave.
- Cursor: 12% vs 18% (January 2026, 6 months); awareness 69% -> 75%; China 28% -> 16%.
- OpenCode: 7% adoption, 42% mindshare (no prior wave).
- Google Antigravity: 6%, stable (awareness 29% -> 47%; India 15% from 10%).
- JetBrains AI (IDE) and/or Junie: about 9% (January wave: 11% combined, i.e. down 2 points; not stated in post 1).
- Product promotion: Claude Agent, Codex, Copilot, OpenCode available in JetBrains AI chat; Cursor etc. via Agent Client Protocol; Air (preview) and JetBrains Central promoted.

### 3. Code share (post 2)
- Question: "What percentage of the code that you produced last month for work was ..." (a) "Fully generated by AI agents"; (b) "Written by you with some AI assistance"; (c) "Fully written by you without any AI assistance". Buckets 0%, 1-20%, 21-40%, 41-60%, 61-80%, 81-99%, 100%, "I don't know". Midpoints used: 0, 10.5, 30.5, 50.5, 70.5, 90, 100.
- Means: agent-generated ~47%; AI-assisted ~38%; fully manual ~27%. These sum to ~112%; the post attributes this to bucket midpoints and self-report error. Over half write under 20% manually; about one in five writes nothing without AI; ~22% generate over 80% with agents ("minority").
- Seniority: about a quarter of senior developers generate over 80% with agents; juniors lean towards AI-assisted. No junior figure, no definitions, no Ns.
- By tool (share of that tool's users): Claude Code ~32% generate >80% with agents; Codex 42% (37% write no code without AI); Cursor mean 58% agent-generated, 28% >80%. Author's interpretation (speculative): Claude Code's audience less dominated by advanced agent users; Codex users possibly drawn by value for money and higher quotas. Heavy Claude Code and Codex users: only 46-57% are "agentic coders".
- By language: Go/JS/TS 54-55% agent-generated; Java/Python 48-51%; C/C++ least agentic (38% manual).
- By region: East Asia (China, Japan, South Korea) 32-35% generate >80% with agents, about twice Europe/UK (~16%).
- Clusters (Ward, Euclidean, unstandardised midpoints): agentic coders ~31% (agent ~84%, assisted ~15%, manual ~6%); AI-assisted ~47% (agent ~40%, assisted ~60%, manual ~20%); manual ~23% (agent ~10%, assisted ~25%, manual ~75%). Cluster shares sum to 101%.
- Stated caveat: self-reports "may not always be fully accurate".

### 4. Not found
No trust, satisfaction, productivity-perception, review/acceptance, "why not", problems/limitations items. No cost, budget or limits data beyond the author's qualitative remark about Codex quotas/value for money. A JetBrains executive is quoted by press (Gulf News) saying more generated code does not automatically make an engineering organisation more efficient (secondary, unread).

### 5. Comparability
- Item wording for the adoption questions is not published, so re-wording cannot be assessed. Different weighting variables and recruitment between waves (see 1). The "agent" construct in the 90%/68% figure is undefined. The sums-over-100% problem is built into the code-share question.

## Tier & era grading
- Tier: D (vendor survey; COI). Large N and a reweighting scheme add reach but do not make it B: self-report, non-probability recruitment, no published instrument, no subgroup Ns.
- Era: adoption items naming Claude Code, Codex, Cursor, OpenCode, Antigravity: E3 (tool-named agents). The headline 90% weekly/68% daily "AI coding agents" is E3 by label but the construct is unspecified (local or cloud, no assistant/agent boundary), so treat as E3-labelled, modality unverified. Copilot 29%->21% is a product-share figure, unsplit by modality (autocomplete, chat and agent modes all possible). Code-share items are E3 by wording ("fully generated by AI agents") but the "AI-assisted" category is unsplit E1/E2/E3.

## Measured vs self-reported
All self-reported. Nothing is measured: no telemetry, no code inspection, no outcome data. Code-share percentages are bucketed recall of "last month" work code; the 112% sum is direct evidence of reporting noise. No self-reported vs measured delta is available from this source.

## Can / cannot support - verdicts
- Can support (directional, with COI label): a hype/adoption baseline for the exec narrative - what developers say they use, tool-share movement between January and May-July 2026, and that heavy agent-generated code share is self-reported by roughly a fifth to a third of respondents.
- Can support: trend direction (Claude Code and Codex up; Copilot, Cursor down) as one independent-ish data point against other tool-share surveys.
- Cannot support: any value, productivity, quality or cost claim; the claim that agents "write 47% of code" as a fact (it is a self-estimate with a >100% sum); causal or "conversion" claims; seniority effects (no Ns or junior figures); trust or satisfaction (items absent).
- RQ relevance: RQ2 (self-report characteristics, internal inconsistency of the instrument); RQ6 (a "AI-generated %" metric as an anti-metric, PROTOCOL §5.7 - this source shows the instrument's noise); adoption context for RQ1/RQ5 background only.

## Red flags / things the orchestrator should know
1. Blog-vs-survey: the survey's own AI chapter and a 2026 methodology page could not be read (404 / not found). Every 2026 number is blog-only and unverified against the survey pages. Fetches were via a summariser; verify exact figures.
2. "A year ago" Copilot 29% coincides with the January 2026 wave's 29%; the YoY label is probably a six-month comparison, or the post is using a different earlier wave without saying so. Cursor 18% -> 12% and Claude Code 18% -> 39% are Jan -> May-July 2026 (about 4-6 months), not annual.
3. "Twice as often as Copilot": 39/21 = 1.86 on adoption share, i.e. "about 1.9x"; it is adoption prevalence, not frequency of use. "Almost 80% conversion rate": 31/39 = 79.5%; it is a cross-sectional ratio of "most used" to "used", not a conversion of individuals over time, and the denominator is Claude Code's own user base. Also, "used at work" is not mutually exclusive across tools.
4. Same "90%" appears in January ("regularly use at least one AI tool") and in August ("use agents at least weekly"); different constructs, easy to conflate. The agent/assistant boundary is not defined; the 90% weekly agent figure sits suspiciously close to the any-AI-tool figure, suggesting respondents' notion of "agent" is broad.
5. US Claude Code 47% (May-Jul) vs 24% US and Canada (January): geography differs, base not given.
6. Weighting differs between waves (coding experience in January; employment status and language in May-July), so trend comparisons carry composition risk; January wave recruitment via Instagram/Zhihu/panel and a de-branded, AI-silent frame. May-Jul recruitment unknown.
7. Self-selection direction: respondents partly from JetBrains' user base and research panel; weighting on JetBrains familiarity mitigates but does not remove. Likely direction: skewed towards engaged, tool-using developers, so adoption is more likely overstated than understated for the general developer population; Copilot's JetBrains-IDE users (39%) and Cursor's decline may reflect JetBrains-ecosystem composition (JetBrains IDEs integrate Claude Agent, Codex, Copilot). Magnitude unknown.
8. Product promotion: the posts promote JetBrains AI, Junie, Air, Central, ACP; JetBrains AI is itself reported at about 9% (down from 11%), an unflattering figure the vendor chose to publish - a point in favour of candour, not independence.
9. 47/38/27 sums to 112%; 31/47/23 cluster shares sum to 101%. "Agentic coders" cluster is defined by code-generation share only.
10. Subgroup claims (seniority, tool, language, region) have no Ns; Claude Code vs Codex "value for money" explanation is the author's speculation.

## Proposed evidence rows (unverified)
Columns: source_id, year, tier, era, method, population, task_types, metric, effect_size, direction, measurement_basis, cost_data, seniority_split, codebase_context, independence_flags, quality_notes, relevance_to_us.

```tsv
jetbrains-2026-ecosystem	2026	D	unsplit	online survey, non-probability, reweighted	over 15000 professional developers (about 90% developer/SWE), fielded May-Jul 2026; comparison wave Jan 2026 AI Pulse over 10000	—	survey methodology and comparability	n>15000 (exact n not published); May-Jul 2026; reweighted by region, employment, language, JetBrains familiarity; Jan 2026 wave raked on region, coding experience, JetBrains familiarity; subgroup Ns not given	n/a	self-reported	none	none	not stated	vendor (JetBrains); respondents partly from JetBrains users and research panel; Jan wave recruited via Instagram ads, Zhihu, 16% panel	Weighting variables differ between waves; 2026 methodology page and survey AI chapter not read; item wording not published	3
jetbrains-2026-ecosystem	2026	D	E3 (label; modality unverified)	online survey	professional developers, May-Jul 2026, n>15000 (base for item not given)	—	use of AI coding agents at work (local or cloud)	90% at least weekly; 68% daily (May-Jul 2026; question wording and item base not published)	n/a (adoption)	self-reported	none	none	not stated	vendor survey; agent not defined or separated from assistants	Jan 2026 wave had 90% regularly using any AI tool - different construct, same number	3
jetbrains-2026-ecosystem	2026	D	E3	online survey, two waves	professional developers, Jan 2026 (n>10000) vs May-Jul 2026 (n>15000)	—	Claude Code work use	18% (Jan 2026) to 39% (May-Jul 2026) worldwide; US 47% (May-Jul; Jan US and Canada 24%); most-used tool for 31% of developers; 39% vs Copilot 21% (ratio 1.86)	up	self-reported	none	none	not stated	vendor survey; waves differ in weighting and recruitment; US base not given	Post's 'almost 80% conversion' is 31/39 cross-sectional; '2x Copilot' is prevalence not frequency of use	3
jetbrains-2026-ecosystem	2026	D	unsplit (product-level)	online survey, two waves	professional developers, Jan 2026 vs May-Jul 2026	—	GitHub Copilot and Cursor work use	Copilot 29% ('a year ago'; Jan 2026 wave also 29%) to 21% (May-Jul 2026); Cursor 18% (Jan 2026) to 12% (May-Jul 2026); Cursor China 28% to 16%; awareness Copilot 79%, Cursor 69% to 75%	down	self-reported	none	none	not stated	vendor survey; JetBrains IDEs integrate several rivals; Copilot 'year ago' wave unnamed	Copilot and Cursor intervals are about 4-6 months, not 12; modality (autocomplete vs agent) not split	2
jetbrains-2026-ecosystem	2026	D	E3	online survey, two waves	professional developers, Jan 2026 vs May-Jul 2026	—	OpenAI Codex, OpenCode, Antigravity, JetBrains AI work use	Codex 3% (Jan 2026) to 16% (May-Jul 2026), awareness 27% to 65%; OpenCode 7%; Antigravity 6% (stable); JetBrains AI and/or Junie about 9% (Jan 2026: 11%)	up (Codex); flat (Antigravity); down (JetBrains AI)	self-reported	none	none	not stated	vendor reports own product share; Jan Codex 3% pre-dated desktop app launch	No question wording; Ns not given	2
jetbrains-2026-ecosystem	2026	D	E3 (agent items); AI-assisted unsplit	online survey, bucketed recall	professional developers, May-Jul 2026, n>15000 (item base not given); code produced last month for work	—	self-estimated share of work code: agent-generated, AI-assisted, fully manual	means 47% agent-generated; 38% AI-assisted; 27% manual (sum about 112%); about 22% generate over 80% with agents; about 1 in 5 write no code without AI; clusters agentic 31%, AI-assisted 47%, manual 23%	n/a (descriptive)	self-reported	none	about a quarter of seniors generate over 80% with agents; juniors lean AI-assisted (no figures or Ns)	not stated	vendor survey; JetBrains-skewed sample	Sum over 100% shows reporting noise; AI-generated percentage is an anti-metric candidate (PROTOCOL 5.7); no outcome data	4
jetbrains-2026-ecosystem	2026	D	E3	online survey, bucketed recall	users of each tool, May-Jul 2026 (subgroup Ns not given)	—	share of tool users generating over 80% of code with agents	Codex 42%; Claude Code about 32%; Cursor 28% (mean 58% agent-generated); by language Go/JS/TS 54-55% agent-generated, C/C++ 38% manual; East Asia 32-35% over 80% vs Europe/UK about 16%	n/a (descriptive)	self-reported	Codex vs Claude Code gap speculated by author to reflect quotas and value for money (no data)	not stated	not stated	vendor survey; Ns absent	Interpretations are author speculation; 'heavy' Claude Code and Codex users only 46-57% agentic coders	3
```

## R5 verification (2026-10-12)
The companion post ("How Much Code Do Developers Really Let Agents Write?") was re-fetched on 2026-10-12: question wording "What percentage of the code that you produced last month for work was …?" with three options; reported means "~47% of their code is fully written by agents", "~38% is written with some AI assistance", "~27% is written fully manually"; the post itself notes the averages "could exceed 100%" because of bucket midpoints and self-report error. The 112% exhibit is therefore verified for exec-brief use.
