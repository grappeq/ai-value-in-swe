# Source: mao-2026-code-metrics

## Citation

Mao, T., Zhao, D., Tang, H., Wang, X., Zhang, H. (2026). *A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories* (title as it appears on the v3 PDF/HTML — see Verification status below for a title discrepancy). arXiv:2603.27130 [cs.SE]. v1: 28 Mar 2026; v2: 3 Apr 2026; v3 (read): 1 Jul 2026. License CC BY 4.0. Affiliation: authors traced to Indiana University (Xiaofeng Wang matches dblp "XiaoFeng Wang 0001," a security researcher at Indiana University Bloomington); full institutional footnotes were not extractable from the fetched text — flagged below, not independently confirmed against the PDF affiliation block.

Version read: **arXiv v3 (1 Jul 2026), fetched directly from arxiv.org/html and arxiv.org/pdf** — full text, not abstract-only. No paywall; no preprint-substitution needed (arXiv is the primary venue, no separate published version found).

## Verification status

- Paper **confirmed to exist** at the given arXiv ID, with the given (approximate) author list. Author order/full name spelling confirmed as: Tianhao Mao, Dongfang Zhao, Haixu Tang, Xiaofeng Wang, Hang Zhang — matches the task's "Mao, Zhao, Tang, Wang, Zhang" ordering.
- **Title discrepancy, unresolved:** the arXiv abs-page search snippet and one HTML mirror (`arxiv.org/html/2603.27130`, and the search-engine cached title for the abs page) render the title as *"A Large-Scale Empirical Study of AI-Generated Code in Real-World Repositories"* (matching the task brief). Direct WebFetch of both `arxiv.org/abs/2603.27130` and `arxiv.org/pdf/2603.27130` (v3) returned the title as *"A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories"*. This looks like a genuine title change somewhere across v1→v3 (v1's arXiv listing title was "...Comprehensive Measurement...") that isn't fully propagated across arXiv's own mirrors/caches, rather than two different papers — same arXiv ID, same author list, same abstract content, same section structure (RQ1–RQ5) in every fetch. **Flagging for human attention** per escalation norms rather than silently picking one title; citation above uses the version this extraction actually read.
- **Relationship to the ResearchGate item — confirmed NOT the same study.** "Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity" is a **separate, unrelated paper**: arXiv:2508.21634 (submitted Aug 2025), authors Cotroneo, Improta, et al. (a different research group; also published at IEEE Xplore, doc 11229706). It is not a sibling pre-registration or companion paper of Mao et al. — it studies a different question with a different design (controlled generation: comparing ~500k human code samples against code freshly generated from scratch by three named LLMs — ChatGPT, DeepSeek-Coder, Qwen-Coder — for defined tasks, classified via Orthogonal Defect Classification and CWE). Mao et al. instead detects **naturally occurring** AI-attributed commits in live GitHub repositories and compares them to matched human commits in the *same* repos. Both papers land on the same general topic (AI vs human code: defects/vulnerabilities/complexity) and both note AI code trends simpler/more repetitive with elevated risk in some vulnerability classes, which is a useful cross-check, but they are independent studies with non-overlapping authorship, data sources, and methodology. Do not merge their extraction records.
- **No sighting of a peer-reviewed/journal version** of the Mao et al. paper as of this check; treated as an arXiv preprint throughout.

## Tier & era & independence

- **Tier: B (structured observational).** Large-N (tens of thousands of files/commits), non-randomised, no counterfactual/causal design — a matched-sample observational comparison within the same repositories. Fits "large-scale telemetry without randomisation, multi-company code-quality analyses" in PROTOCOL §3. Not Tier A: no experimental manipulation, and the "AI-generated" label itself is inferred (see validation figures below), not ground truth.
- **Era: mixed, predominantly E2, not separable by the study's own data.** The AI-tool mix behind the "AI-involved" label is ChatGPT 83.3%, Copilot 10.8%, DeepSeek 2.2%, Gemini 1.7%, Cursor 1.3%, others 0.7%. ChatGPT-dominated commit-comment attribution strongly suggests chat-assisted copy-paste workflows (E2); Copilot could be E1 (classic autocomplete) or E2/E3 depending on version and cannot be disambiguated from the data given; Cursor AI (1.3%) is E3-agentic but a small slice. The study does **not** break any finding out by tool or by modality, so per the CLAUDE.md era rule ("tag by tool modality actually studied... splitting into separate findings if necessary") **no single finding in this source can be cleanly tagged E3** — treat the whole source as **E2-weighted, mixed-era**, and do not let any of its effect sizes stand in for E3-agentic evidence in the exec brief without this caveat attached.
- **Independence:** academic authors (Indiana University, based on the Xiaofeng Wang match), no vendor/consultancy affiliation found, no funding statement recoverable from the fetched text (flagged as unconfirmed, not as evidence of a COI — most likely a standard academic-grant acknowledgement that wasn't captured by the extraction tooling). No COI flag warranted on current evidence, but the funding line should be checked directly against the PDF if this becomes an exec-brief-supporting source.

## Method & population

**Goal:** compare AI-generated and human-written code as it actually appears in public GitHub repositories (not lab-generated code), on both code-level and commit-level dimensions.

**AI-code attribution method (the load-bearing design choice):**
1. **Seed search:** 11 AI tool names (ChatGPT, Copilot, Tabnine, CodeWhisperer, Llama, Claude, Gemini, DeepSeek, Grok, Qwen, Cursor AI) × 6 prefix words ("by/with/use/used/using/from") = 66 keyword combinations, searched against GitHub commit messages/comments through 31 Dec 2025 → 44,616 unique code files across 31,726 commits.
2. **Rule-based filtering** (keyword normalisation, semantic-attribution pattern matching e.g. "generated by"/"written by"/"enhanced by", removal of files where the AI mention refers to an auxiliary task not the code itself) → 8,268 AI-involved files / 4,882 commits. **Manual validation on 100 sampled files: TP=88/100, TN=95/100.**
3. **LLM-assisted classification** (GPT-4o-mini used to adjudicate uncertain cases) → 10,932 files / 7,877 commits, plus 683 more added by manual labelling. **Second validation round: TP=85/100, TN=93/100.**
4. **Deduplication** → final set of 19,816 AI-involved files across 12,749 commits.
5. **Code-unit extraction:** AI-hinting comments are associated with specific code scopes (file/function/type-declaration level) to isolate the actually-AI-authored portion rather than the whole file → 42,792 sub-file units + 9,843 file snapshots. **Validated on 100 function-level + 100 file-level samples: 87/100 and 98/100 true positives respectively.**
6. **Matching:** each AI unit/file is paired with a human-written control from the **same repository**, drawn from "pre-AI and stable-period" code, matched on language, path, and code size (±20% LOC).
7. **Final matched dataset:** 36,855 AI-generated units + 7,471 file snapshots, matched against 65,391 human-written units + 15,424 files.

**This is entirely comment/attribution-based detection**, i.e. it only captures code where a developer *explicitly said* an AI tool was involved (in a commit message, code comment, or similar). The method has real, reported validation (precision in the 85–98% true-positive range across three separate manual-validation rounds at different pipeline stages), which is more rigorous than most attribution schemes in this space, but it structurally **cannot see silent/undisclosed AI use**, which the authors do not attempt to estimate and which is a first-order threat to how representative the sample is of "AI-generated code" as a whole.

**Population:** GitHub public repos, through Dec 2025. Languages: Python 41.7%, JavaScript 15.4%, Java 8.6%, C++ 7.8%, TypeScript 7.8%, C# 4.8%, Swift 3.8%, C 3.7%, others 6.4%. Tool mix as above. No explicit repository-selection/sampling strategy beyond "repos where the keyword search hit" — i.e., a convenience sample of repos where developers happen to disclose AI use in-band, not a random or stratified sample of GitHub.

## Key findings

All figures **measured** (static analysis / code metrics / clone detection / commit-log analysis over the matched dataset above) — this source contains no self-report data, so the measured/self-reported distinction that CLAUDE.md requires is trivially satisfied (everything here is "measured"; flagged explicitly per rule 4 so it isn't mistaken for an omission).

**Code-level structure — mostly similarity, not difference (the headline the abstract emphasises):**
- Lines-of-code metrics (PLOC, SLOC, CLOC): no statistically significant AI/human difference. BLOC differs significantly but with small effect size.
- Token-level metrics: statistically different but low Cohen's d — authors explicitly call this "no practical separation despite statistical significance."
- Structural complexity: many metrics statistically different but small Cohen's d; case count, nesting depth, boolean-expression count, decision-point count are non-significant.
- OOP metrics: C++ — human code has deeper inheritance (DIT, Cohen's d = −0.223); Java — no significant differences, negligible effect sizes; Python — small differences in WMC, CBO, RFC (d = 0.060–0.132).
- Blank-line ratios: "nearly identical" between AI and human code.
- Within-file duplication: "low and similar across both groups."

**Code-level differences that are real:**
- Comments: AI-generated code has statistically significantly more comments.
- Code duplication (the clearest quality-debt-relevant delta): human-written 27.57% duplicated lines vs AI-generated 14.29%; human 41% duplicated intervals vs AI 22.93%; cross-file duplication human 26.62% vs AI 13.22% — **in this dataset AI code is less duplicated than human code**, the opposite direction from the GitClear churn/duplication narrative (§5.4 tension) — record as a genuine contradiction candidate, not a confirmation.

**Security/defect density:**
- Overall static-analysis alert density: AI 10.04 alerts/KLOC vs human 13.56 alerts/KLOC (AI lower overall).
- High-risk alerts specifically: AI 0.514 vs human 0.52 per KLOC — essentially indistinguishable.
- Language-dependent reversal: C — AI has higher alert density than human; C#/JavaScript — similar; most other languages — human higher.
- CWE distribution: both dominated by the same two categories (CWE-563, CWE-561 — unused code constructs); human 51.0% vs AI 44.6% share in top categories; AI relatively over-represented in CWE-248 (exception handling) and CWE-390; human over-represented in CWE-208 and CWE-772 (resource lifecycle).
- Hardcoded secrets: **human-written code contains more hardcoded sensitive information** (passwords/API keys/tokens/private keys) than AI-generated code in this dataset — notable because it runs opposite to the popular narrative that AI tools are especially prone to leaking hardcoded secrets.

**Commit-level (RQ1–RQ5 in the paper's own numbering, not this protocol's RQs):**
- Timing: AI-involved commits slightly more likely outside working hours (0.372 vs 0.358) and less frequent in the 30 days before a release (0.622 vs 0.694).
- Change size: AI commits are substantially smaller in scope — fewer files touched, significantly lower line churn per commit.
- Post-commit evolution: short-term (7-day) differences are limited; at 30–90 days, AI-touched code shows more follow-up activity — higher touch frequency, more participating authors, greater accumulated churn, slightly higher fix-commit likelihood, and significantly longer time-to-stabilisation. Authors caveat that "low mean values suggest effects concentrated in [a] subset of commits" — i.e. this is a heavy-tail effect, not a uniform shift.
- Collaboration/handoff: AI-involved code has a much longer handoff latency — 28.28 days vs 11.23 days for human code — with more follow-up contributors over time and more frequent merge commits.

## What this can and cannot support

**Can support:** a Tier B, mixed/E2-weighted, code-metric-and-commit-metric data point for RQ3 (failure/quality-debt map) and RQ5 (does local AI use translate to system-level stability), specifically: (a) evidence that at the code-metric level, differences between AI and human code in the wild are mostly small/non-significant, which cuts against strong "AI code is structurally worse" claims; (b) evidence for a real, sizeable **handoff-latency and stabilisation-time gap** (28.28 vs 11.23 days; longer time-to-stabilise at 30–90 days) — directly relevant to the bottleneck-displacement tension (§5.6): code lands fast but takes longer to actually stabilise/get fully integrated, which is a stability-cost signal even without a throughput claim; (c) a genuine counter-data-point to the GitClear duplication narrative (AI code *less* duplicated here, not more) that should go straight into `contradictions.md` when this is cross-referenced, not be quietly reconciled.

**Cannot support:** any E3-agentic-specific claim (the tool mix is ChatGPT-dominated and not modality-separated); any claim about causally attributing the commit-level effects to "AI made code worse/better" (the design is observational, matched but not randomised, and residual context/contributor/maturity confounds are explicitly acknowledged by the authors); any claim about task type (T1–T11) — the paper does not tag by task, and this extraction does not force a tag onto it; any claim about developer seniority (not measured); and it cannot stand in for a study of *undisclosed* AI-generated code, since the detection method is attribution-based and structurally blind to silent AI use — the authors do not quantify this gap, and neither should we.

## Follow-up leads

- The paper's own comparison point, arXiv:2508.21634 (Cotroneo, Improta et al., "Human-Written vs. AI-Generated Code," IEEE, Aug 2025) — worth a full extraction in its own right (different design: controlled generation vs three named LLMs, ODC + CWE classification, ~500k samples, Python/Java) since it converges on "AI code simpler/more repetitive" but appears to diverge on vulnerability direction (reports AI code more prone to command-injection/hardcoded-secret CWEs — the opposite of Mao et al.'s hardcoded-secrets finding) — a candidate contradiction worth cross-referencing carefully once both are extracted.
- arXiv:2606.24429 ("Detecting AI Coding Agents in Open Source: A Validated Multi-Method Census of 180 Million Repositories") surfaced in the same search — a much larger-scale attribution/detection study, potentially useful for validating or contesting Mao et al.'s attribution methodology and tool-mix figures.
- arXiv:2603.28592 ("Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild") — near-identical arXiv ID and near-identical title, submitted one day after Mao et al.'s v1; worth checking whether this is an independent competing study or a renamed/duplicate submission, given the title-discrepancy issue already flagged above for the primary source.
- Worth checking whether v3 (1 Jul 2026, the version read here) added the RQ4/RQ5 collaboration-latency material versus v1/v2 — if the numeric findings changed materially across versions, that itself would be a useful methodology note.

## Recency check notes

Source is 5 days old at time of extraction (v3: 1 Jul 2026; today: 6 Jul 2026) — the 12-month recency check in CLAUDE.md rule 8 does not strictly apply, but given how fresh this is, no citations, replications, or critiques exist yet to check against. Re-verify in a later batch if this source is promoted to an exec-brief-supporting role, since a paper this new could still be revised again (already on its third version in ~3 months) or draw post-publication critique.
