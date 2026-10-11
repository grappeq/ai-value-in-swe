# Source: github-2026-agent-scale

## Identity
Combined record of GitHub's own 2026 statements on agent-scale activity and agent PR review.
- (A) Brian Celenza (Principal Software Engineer), "Building Git infrastructure for agent-scale development", GitHub Engineering blog, published 6 Oct 2026, updated 7 Oct 2026. https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/
- (B) Andrea Griffiths (Senior Developer Advocate), "Agent pull requests are everywhere. Here's how to review them.", GitHub blog, 7 May 2026. https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/
- (C) Searches for Octoverse 2026 and The Information's PR figures; (D) search for the ninefold claim. Both secondary only (see below).

Note: fetched via a summarising fetch tool, not raw HTML; quotations are as returned by that tool.

## What this document is
Two vendor blog posts. (A) justifies infrastructure investment with platform-wide load figures. (B) is a developer-advocate guide to reviewing agent PRs, with a few Copilot review volume figures and otherwise prescriptive advice.

## Full notes
(A) Figures, exact wording:
- "In September alone, developers and agents made 7.38 billion commits on GitHub": Sept 2026, "more than five times as many as a year earlier"; prior-year count not given.
- "Pushes grew 4.9x year over year, from 0.69 billion to 3.35 billion per month" (ratio computes to ~4.86x).
- PR merges "nearly 4x" their volume a year ago; no absolute numbers.
- Git activity rose "from 218.2 billion events per month to 473.3 billion" between Sept 2025 and Aug 2026 (~2.17x, "more than 2x").
- "GitHub Actions alone ran 3.26 billion times in September, more than 4x as many as a year ago."
- "The busiest repository on GitHub saw roughly a billion requests in August" (Aug 2026).
- "In internal benchmarks, it has delivered up to 35 times higher write throughput": a benchmark ceiling, not production.
- No figure separates agent from human activity; all are aggregate totals.

(B) Figures and guidance:
- "GitHub Copilot code review has processed over 60 million reviews, growing 10x in less than a year."
- "More than one in five code reviews on GitHub now involve an agent." The post does not define "involve an agent"; per the fetch it refers to the automated review pass. Whether this means Copilot only or any bot is unresolved. Denominator and period of measurement not stated.
- No numeric figures on agent-PR abandonment, PR size or merge rates. One qualitative claim: "Larger pull requests with no structured plan correlate strongly with agent abandonment or misalignment" (no data).
- Guidance (prescriptive, not evidence): check CI first ("Any change that weakens CI is a blocker"); look for duplicated utilities; trace one critical path and require a test that fails on pre-change behaviour; check the plan before deep review; audit LLM-calling workflows for prompt injection, token permissions and unvalidated output; run automated review first; authors self-review; request a smaller PR when it spans many unrelated files (rule of thumb: more than five), purpose cannot be stated in a sentence, plan is missing, or CI fails with only test files changed.

(C) Octoverse 2026: no official report found as of 11 Oct 2026; only third-party posts restating Octoverse 2025. The Information figure (agent-opened PRs ~4M in Sept 2025 to >17M in Mar 2026): original article not found; reported only by an AI-news blog (AI2Work) and echoed in aggregators. Secondary, definition unconfirmed. The same blog's "28-fold in ten months" headline is also unverified.

(D) "Agent PRs grew ninefold in size over eight months, citing GitHub data": found only on Digg (16 Sept 2026), described as "reportedly". No GitHub primary located. Unverifiable.

## Tier & era grading
Tier D: vendor self-report; COI (GitHub sells Copilot and benefits from volume and agent-adoption narratives). Era E3 by topic, but volume figures are platform-wide and NOT split by agent versus human; the post says "developers and agents". Independence: none.

## Measured vs self-reported
Platform telemetry is measured, but definitions (commit, push, "involve an agent", event) are the vendor's and not published. The 35x figure is an internal benchmark. The abandonment claim is an unsupported assertion. No self-reported survey data.

## Can / cannot support — verdicts
Can: hype-baseline context (the scale of activity GitHub claims); evidence that review volume is a growing platform concern; a prescriptive review checklist worth comparing with independent sources.
Cannot: any claim about value, productivity, quality or agent share of activity. Volume is not value: more commits, pushes and Actions runs may reflect more output, more automation noise, or retries. Cannot support bottleneck-displacement conclusions (no review latency or queue data). Review checklist is advice, not evidence.

## Red flags / things the orchestrator should know
- Ninefold PR-size claim: Digg aggregator only; no GitHub primary. Do not use.
- 4M to 17M agent PRs: attributed to The Information via a secondary blog; primary not found; definition unknown. Do not use as GitHub data.
- "Involve an agent" is undefined; it may include Copilot review requests on human PRs, so it is not the share of agent-authored PRs.
- No agent/human split anywhere; growth is not attributable to agents.
- Octoverse 2026 not published as of 11 Oct 2026; recheck late Oct/Nov.
- Post (A) was updated after publication (7 Oct); figures may change.
- Abandonment-vs-size statement has no data behind it.

## Proposed evidence rows (unverified)
Columns: source_id, year, tier, era, method, population, task_types, metric, effect_size, direction, measurement_basis, cost_data, seniority_split, codebase_context, independence_flags, quality_notes, relevance_to_us.

```tsv
github-2026-agent-scale	2026	D	E3	vendor platform telemetry (blog)	GitHub-wide, all users, humans and agents combined; Sept 2026 vs Sept 2025	—	commits/month; pushes/month; PR merges (YoY)	7.38B commits in Sept 2026 (>5x YoY); pushes 0.69B to 3.35B per month (4.9x YoY); PR merges nearly 4x YoY (no absolute figures)	increase (volume)	measured (vendor definitions)	none	none	platform-wide, no repo or codebase split	vendor self-report; GitHub sells Copilot; commit count combines developers and agents	volume is not value; no agent/human split; denominators for YoY not given	2
github-2026-agent-scale	2026	D	E3	vendor platform telemetry (blog)	GitHub Actions, all users; Sept 2026 vs Sept 2025; Git events Sept 2025 to Aug 2026	T11	Actions runs per month; Git events per month; busiest-repo requests	Actions 3.26B runs in Sept 2026 (>4x YoY); Git events 218.2B to 473.3B per month (Sept 2025 to Aug 2026, ~2.17x); busiest repo ~1B requests in Aug 2026	increase (volume)	measured (vendor definitions)	none	none	platform-wide	vendor self-report; load figures framed to motivate infra work	Actions runs include non-agent CI; demand-side load not outcome	2
github-2026-agent-scale	2026	D	E3	internal benchmark (blog)	GitHub Git storage write path, internal benchmarks	T11	write throughput	up to 35x higher write throughput (internal benchmarks; ceiling not production)	increase	measured (benchmark)	none	none	GitHub infrastructure	vendor self-report; benchmark not production	engineering result, not about developer value	1
github-2026-agent-scale	2026	D	E3	vendor blog (Copilot code review telemetry)	Copilot code review users on GitHub; published 7 May 2026	T7	Copilot code review volume; share of reviews involving an agent	over 60M reviews, growing 10x in less than a year; more than one in five code reviews on GitHub now involve an agent	increase (volume)	measured (vendor definitions)	none	none	platform-wide	vendor self-report; 'involve an agent' undefined, appears to cover automated review pass; denominator unstated	review volume not review quality or defect catch; ambiguity on bot vs Copilot	3
github-2026-agent-scale	2026	D	E3	vendor blog (qualitative)	GitHub guidance on reviewing agent PRs	T7	agent PR abandonment vs size	no number; 'larger pull requests with no structured plan correlate strongly with agent abandonment or misalignment' (qualitative)	larger PR associated with abandonment (unquantified)	unspecified	none	none	not stated	vendor assertion without data; review checklist is prescriptive not evidence	do not cite as an effect size	2
github-2026-agent-scale	2026	D	E3	absence finding	both GitHub posts	—	agent vs human split of activity	no figure separates agent from human activity in either post; commits described as made by 'developers and agents'	n/a	n/a	none	none	n/a	vendor; platform totals only	volume growth cannot be attributed to agents from this source	4
github-2026-agent-scale	2026	—	E3	existence check (web search, 11 Oct 2026)	GitHub Octoverse 2026	—	report availability	not found as of 11 Oct 2026; only third-party posts restating Octoverse 2025	n/a	n/a	none	none	n/a	negative search result, not proof of absence	recheck late Oct/Nov 2026	1
github-2026-agent-scale	2026	—	E3	verification attempt (web search)	agent PRs ~4M (Sept 2025) to >17M (Mar 2026), attributed to The Information; 'ninefold PR size growth over eight months' (Digg, 16 Sept 2026)	—	agent-opened PR count; agent PR size	unverified	unverified	unverified	none	none	n/a	secondary only (AI2Work blog, Digg aggregator); no GitHub or The Information primary found	do not cite as findings; the ninefold figure has no GitHub primary located	3
```
