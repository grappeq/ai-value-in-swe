# Source: google-autodiagnose-2026

## Identity
- **Title:** LLM-Based Automated Diagnosis of Integration Test Failures at Google (tool name in text: Auto-Diagnose; the arXiv HTML render calls it AutoDebug in places)
- **Authors:** Celal Ziftci, Ray Liu, Spencer Greene, Livio Dalloro (all Google, New York)
- **Venue / version:** arXiv 2604.12108v1 [cs.SE], 13 Apr 2026; ICSE 2026 Software Engineering in Practice (SEIP) track. One web search found no later version or independent critique; only a vendor-friendly news recap (MarkTechPost, 17 Apr 2026) repeating the abstract numbers. A Technical Disclosure Commons entry describes a different, baseline-run-comparison approach.
- **Read:** full text from the PDF. Note: the arXiv HTML render contains unfilled LaTeX placeholders in place of most numbers (e.g. total accuracy, token counts, feedback counts); all figures below come from the PDF.
- **Source URL:** https://arxiv.org/abs/2604.12108

## What this document is
An industry-track case study of one internal tool. Auto-Diagnose reads the logs of a failed hermetic functional integration test and posts a root-cause summary into Critique (Google's code review system) within about a minute. Evidence is three parts: a 71-failure expert review, an observational deployment since May 2025 with opt-in button feedback, and 11 interviews. There is no control arm.

## Full notes
**1. What the system does.**
- Trigger: automatic on every hermetic functional integration-test failure during a code change; no developer action needed.
- Inputs: test-driver and system-under-test component logs at INFO and above, joined across data centres, processes and threads and sorted by timestamp into one stream, plus component metadata in a CONTEXT section. It does not take source code, the change list or diffs.
- Model: Gemini 2.5 Flash, temperature 0.1, top-p 0.8, not fine-tuned. One prompt, iterated by hand against real failures: step-by-step reasoning, strict negative constraints (use only the failed component's logs; do not conclude by guessing; ask for more logs if absent; ignore the normal SIGINT line), fixed output format.
- Output: a Critique finding with Conclusion, Investigation Steps and Most Relevant Log Lines (linked). It diagnoses; it does not propose or apply a fix.
- Architecture: a single LLM call. No tools, no multi-step loop, no retrieval, no code access. This is log summarisation, not an agent.

**2. Deployment and design.**
- Launched May 2025 to all integration-test failures on code changes across Google's repository. Reported totals: 91,130 code changes, 22,962 distinct authors, 224,782 executions, 52,635 distinct failing tests. The paper does not give an end date or total duration, nor the share of all failures covered.
- Failing tests: median 16 log files and 2,801 log lines (mean 26 and 11,058).
- Design: retrospective expert evaluation plus uncontrolled observational rollout plus interviews. Not an A/B test, no counterfactual, no per-failure-class breakdown.

**3. Quantitative outcomes (exact).**
- Expert accuracy: 64/71 = 90.14% (3 experts, 5+ years, from the integration-test infrastructure team; consensus after discussion; success if the Conclusion or any listed log line gave accurate root-cause context; 71 random failures from 39 teams). No confidence interval, no agreement statistic.
- Misses: 7/71. All were investigated: 4 where test-driver logs were not saved after a driver crash, 3 where component logs were not saved after a component crash. Both were infrastructure bugs, reported to the owners.
- Feedback: 517 events from 437 developers (458 code changes). 436 Please fix (84.3%, 370 reviewers), 51 Helpful (9.9%, 43 authors), 30 Not helpful (5.8%, 28 authors). Helpfulness rate 51/(51+30) = 62.96%. Ranked #14 of 370 tools posting findings in Critique (top 3.78%) on helpfulness; ranked #134 on feedback rate (0.0023 versus median 0.0012, mean 0.1042). Internal guideline: a tool must keep not-helpful below 10% to keep posting.
- Latency: p50 56 s, p90 346 s to post a finding.
- Cost: mean 110,617 input and 5,962 output tokens per execution. Called 'highly cost effective' with no monetary figure or comparison.
- Time: not measured. The paper contrasts tool latency with Survey-2 (116 developers, self-reported) where manual diagnosis took 'often more than an hour, sometimes longer than a day'. EngSat (6,059 developers): integration-test diagnosis a top-five complaint. One interviewee recalled 10-15 minutes for the day's debugging.
- Interviews: 11 participants; excerpts mostly positive, with a demand for fixes and one frustration with a 'more information is needed' output. About 20 such outputs to date.

**4. Nulls, negatives, caveats the authors report.**
- Abstains (by prompt design) when the failed component's logs are absent; about 20 such diagnoses, all traced to the same infrastructure log-saving bugs. Developers found these frustrating.
- Recovered ERROR-level log lines mislead both developers and the model; listed as future work, no mitigation evaluated.
- Helpfulness rate (63%) is well below expert accuracy (90%); the authors attribute this to negativity bias in who clicks, untested.
- Developers want fixes, not diagnoses; fix generation is future work.
- Generalisability: single company, one model, one prompt, model drift during the study possible, log quality varies.

**5. What is absent.** No hallucination or wrong-but-confident rate; no precision/recall; no breakdown by failure class, team or log size; no comparison with a non-LLM or grep-style baseline; no time-to-fix, time-to-green or re-run counts; no cost in money or comparison with developer time; no seniority data; no duration or adoption-over-time curve.

## Tier & era grading
- **Tier: C (practitioner signal), with Tier D-style COI flag.** Real numbers and a stated measurement method, at very large scale, but no control, no counterfactual, and the evaluating parties are the tool builders at the tool's owner. Not B: telemetry here is usage and opt-in feedback, not an outcome measure with a comparator.
- **COI (flag):** Google authors evaluating a Google-internal tool on Google engineers, in an industry-track venue; Gemini is a Google model. The paper uses the favourable framing 'highly successful' / 'highly effective' that the data (no comparator, 0.5% feedback coverage) does not strictly bear.
- **Era: E2.** Single-pass LLM call over supplied text, no tool use, no plan-execute-verify loop. By PROTOCOL §2 the era follows modality, not the 2025 deployment date, so it supports baselines, methodology and era-independent points only, not E3 effect-size claims. (Contrast with agentic debugging systems.)
- **Independence:** single organisation; the same rollout is the only source for all numbers.

## Measured vs self-reported
| Outcome | Basis | Value |
|---|---|---|
| Root-cause accuracy | Measured (expert panel, consensus) | 64/71 = 90.14% |
| Misses attributed to infrastructure bugs | Measured (manual investigation) | 7/7 |
| Usage scale | Measured (telemetry) | 224,782 executions, 52,635 tests, 91,130 changes |
| Latency | Measured | p50 56 s, p90 346 s |
| Token usage | Measured | 110,617 in / 5,962 out (mean) |
| Helpful / Not helpful | Self-reported, opt-in | 62.96% helpful, 5.8% not-helpful (of all feedback events) |
| Manual diagnosis time | Self-reported survey (N=116) | often over 1 hour, sometimes over a day |
| Time saved by tool | Not measured | no figure |
| Interview sentiment | Self-reported | positive, 11 participants, self-selected |

The measured-versus-self-reported delta is internal to the tool: 90.14% expert accuracy versus 62.96% user helpfulness (about 27 points). The authors explain it with negativity bias; it could equally reflect different success criteria (experts counted any accurate log line as success) or selection of who clicks. It is not a perception-versus-reality gap in the METR sense, because no one reported a productivity belief that was then tested.

## Can / cannot support — verdicts
**Can support (directional, Tier C, single source):**
- A single-pass LLM over merged logs can identify the relevant root-cause log context in a large majority of sampled Google integration-test failures (90% in a 71-failure expert review), at low latency (median under a minute) and moderate token volume.
- Embedding the output automatically in the existing review workflow produced sustained use at scale (224,782 executions) without breaching the internal 10% not-helpful ceiling.
- Failure modes in this task are driven by input quality (missing logs), and an abstain-when-uncertain prompt converts missing evidence into 'need more info' rather than invented causes. A mechanism hypothesis, not a measured hallucination rate.
- Debugging/log triage (T8) now has at least one large-scale measured accuracy datum; useful as an E2 baseline.

**Cannot support:**
- Any time-to-diagnose, time-to-fix or productivity claim (not measured).
- Any E3 claim: the system is not agentic and does not read code or propose fixes.
- Generalisation to non-hermetic tests, other organisations' logging quality, other models, or incident response in production (this is pre-merge test failure on code changes, not operations incidents).
- Any claim about hallucination rates, or about the 90% figure being stable over time or across failure classes.
- Cost-benefit: no money or time-cost comparison.

## Red flags / things the orchestrator should know
1. **Do not cite the arXiv HTML.** It contains unfilled placeholders instead of numbers; the PDF has them. Verify against PDF if a reader checks.
2. **No time-saved evidence.** The 'significantly faster' claim compares machine latency with recollected human durations; it must not enter the evidence table as a speed-up.
3. **Success criterion is lenient and the accuracy panel is not independent:** infrastructure-team evaluators, consensus after discussion, any accurate log line counts, N=71, no CI.
4. **Helpfulness rate is mislabelled-prone:** 62.96% is Helpful/(Helpful+Not helpful) on 81 votes, not satisfaction of all users; the 5.8% not-helpful figure is over all 517 events, 84% of which are 'Please fix' clicks. Quote both denominators.
5. **Feedback coverage is tiny:** 458 of 91,130 changes (about 0.5%).
6. **Rank claims (#14 of 370) compare against mostly deterministic linters**, not other AI tools.
7. **Naming inconsistency:** Auto-Diagnose (PDF) versus AutoDebug (HTML); same paper.
8. **Fit with taxonomy:** the work is T8 (log interpretation) with a T6 flavour (test failure triage); no taxonomy change proposed. Production incident response is a different setting and is still unmeasured here.
9. **Scarcity note:** this is likely the best-scaled debugging datum available, and it is E2, Tier C with COI. Do not use it to imply agentic debugging evidence exists.
10. No contradiction with other sources was checked (blind extraction).

## Proposed evidence rows (unverified)
```tsv
source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
google-autodiagnose-2026	2026	C	E2	Design and deployment description: single-pass Gemini 2.5 Flash call over merged test-driver and component logs, auto-triggered on integration-test failure in Google's Critique code review; launched May 2025 on all hermetic functional integration test failures during code changes	Google engineers; 22,962 distinct code-change authors, 91,130 code changes, 52,635 distinct failing tests, 224,782 executions (reported); seniority not reported	T8;T6	Deployment scale and mode of operation (not an effect)	N=224,782 executions on 52,635 distinct tests across 91,130 code changes; median 16 log files and 2,801 log lines per failing test (mean 26 and 11,058); no control arm	n/a (descriptive)	measured (telemetry counts)	Mean 110,617 input tokens and 5,962 output tokens per execution; no dollar figure; p50 56 s and p90 346 s to post finding	none reported	Google monorepo; hermetic functional integration tests only (performance, security, reliability tests excluded); internal Critique and test infrastructure	Google authors evaluating Google's own tool; no external replication; observational rollout with no A/B arm or counterfactual	Single LLM call with no tools, no code or change-list input and no fix output, so it is log summarisation rather than agentic debugging; E2-equivalent modality (single-pass LLM) despite 2025 deployment	4
google-autodiagnose-2026	2026	C	E2	Retrospective manual evaluation: 3 expert developers (each 5+ years, integration-test infrastructure team) judged whether Conclusion or any Most Relevant Log Line gave accurate root-cause context; disagreements settled in a meeting	71 randomly selected real integration-test failures from 39 teams; evaluators did not own the failing code	T8	Root-cause diagnosis accuracy (expert-judged)	64 of 71 accurate = 90.14% (N=71; no confidence interval, no inter-rater statistic, no baseline comparator)	positive	measured (expert panel, consensus labels)	none	none	Google; failures sampled across teams; evaluators from the infrastructure team	Authors' own team-adjacent evaluators; lenient success criterion (any listed log line giving accurate context counts); small N; sampling frame and selection of 'random' not described; no precision or recall	Of the 7 misses, 4 were test-driver logs not saved on driver crash and 3 were component logs not saved on component crash (infrastructure bugs), so none are attributed to model reasoning error by the authors	4
google-autodiagnose-2026	2026	C	E2	Observational rollout feedback via Critique buttons (Helpful / Not helpful / Please fix) over the deployment period	517 feedback events from 437 distinct developers on 458 code changes (about 0.5% of 91,130 code changes); 30 Not helpful from 28 authors; 51 Helpful from 43 authors	T8	Developer-rated usefulness of findings	Not-helpful rate 5.8% (30/517); helpfulness rate 62.96% (51 Helpful vs 30 Not helpful, N=81 author votes); Please fix 436 (84.3%) from 370 reviewers; helpfulness rank #14 of 370 tools (top 3.78%); feedback-rate rank #134 of 370 (0.0023 vs median 0.0012, mean 0.1042)	positive (mixed: 63% helpful vs 90% expert accuracy)	self-reported (in-workflow button clicks, opt-in)	none	none reported	Google Critique; compared with 370 other Critique tools, mostly deterministic lint, style and test checks, not LLM tools	Self-selected respondents; Google-on-Google	Only 81 of 517 events are the helpful/not-helpful signal and 436 are a different action (reviewer asks author to act); 10% not-helpful internal guideline is the benchmark; authors attribute the 63% vs 90% gap to negativity bias without testing it	3
google-autodiagnose-2026	2026	C	E2	Semi-structured in-person interviews with developers who had given feedback	11 interviewees (code-change authors and reviewers who clicked Useful, Not useful or Please fix); seniority not reported	T8	Perceived usefulness and workflow fit; anecdotal time saved	Qualitative; one interviewee (P-1) recalled the debugging as taking 10-15 minutes versus 'over an hour' for typical issues; no counts of positive versus negative interviewees given	positive (qualitative)	self-reported	none	none reported	Google Critique workflow	Self-selected from feedback givers; no neutral or non-using group; Google-on-Google	Single anecdotal time figure is recollection, not a measurement; developers expect fixes, not only diagnoses (P-3); one found a 'more information is needed' output frustrating (P-9)	3
google-autodiagnose-2026	2026	C	E2	Latency comparison of tool turnaround against survey-reported manual diagnosis durations; no direct time-to-diagnose or time-to-fix measurement	Tool: 224,782 executions; manual-duration baseline: Survey-2, 116 developers (self-reported); EngSat survey 6,059 developers ranked integration-test diagnosis a top-5 complaint	T8	Time to produce a diagnosis versus reported manual diagnosis time	Tool p50 56 s, p90 346 s to post finding (measured, N=224,782); manual diagnosis 'often more than an hour and sometimes longer than a day' (self-reported, N=116); no measured time saved, no counterfactual	not established (latency favourable; saving unmeasured)	both (tool latency measured; manual baseline self-reported)	Tool latency and token figures only; no human time or cost-per-diagnosis comparison	none reported	Google	Google-on-Google; manual baseline is survey recall	Compares a machine latency to human recall of the whole diagnosis episode; says nothing about whether developers reached a fix faster; the paper claims 'significantly faster' without an experimental comparison; do not cite as a productivity gain	4
google-autodiagnose-2026	2026	C	E2	Failure-mode and negative-result observations from manual evaluation, deployment and interviews	7 of 71 evaluated failures judged not accurately diagnosed; approximately 20 deployed diagnoses returned 'more information is needed'	T8	Failure modes and non-diagnoses	7/71 = 9.86% misses (all traced to missing logs from infrastructure bugs); about 20 'more information is needed' outputs to date (denominator not given)	negative/null (limits)	measured (manual investigation) and self-reported (interviews)	none	none reported	Google test infrastructure	Google-on-Google; authors' own investigation	Prompt forbids guessing when the failing component's logs are absent, so missing-log cases abstain by design; no hallucination rate reported; recovered ERROR-level noise acknowledged as misleading but no fix evaluated; no per-failure-class breakdown; developers 'highly sensitive' to unhelpful automatic findings	4
google-autodiagnose-2026	2026	C	E2	Authors' stated threats to validity and generalisability	n/a	T8	Limitations and external validity	n/a (qualitative)	n/a	n/a	none	none reported	Single company, internal infrastructure; one model (Gemini 2.5 Flash, temperature 0.1, top-p 0.8, not fine-tuned), one prompt; model may have drifted during study; log quality varies by component	Google authors; no external review of data; deployment duration not stated beyond launch in May 2025	arXiv HTML render shows unfilled template placeholders for most numbers (figures here are from the PDF); no precision/recall, failure-class breakdown, hallucination audit, ablation or non-LLM log baseline	3
```
