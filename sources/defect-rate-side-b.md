# defect-rate-side-b — Copilot defect-rate contradiction, Side B (two Tier D vendor documents)

Combined record per remediation task (audit finding 6): fills the "Side B — NOT YET EXTRACTED" gap in `synthesis/contradictions.md` ("Copilot defect-rate: +41% bugs vs vendor counter-claims"). Covers (a) GitHub/Accenture-family Copilot code-quality research (Nov 2024, updated Feb 2025, plus its companion May 2024 Accenture piece) and (b) CodeRabbit's "State of AI vs Human Code Generation" report (Dec 2025). Both fetched and read as primary web pages (not abstract-only); no full-text PDF exists for either — see verification status per document.

---

## (a) GitHub Copilot code-quality study

### Citation

GitHub Customer Research team (statisticians credited: Lizzie Redford, Sida Peng). (2024, 18 November; updated 2025, 6 February). *Does GitHub Copilot improve code quality? Here's what the data says.* GitHub Blog.
- URL: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/
- Fetched and read directly (not search-synthesis) 2026-07-06. Live, no paywall.

**Companion source, distinct study, same vendor family (referenced in Uplevel's follow-up leads as if one document — it is two):**
GitHub, with Accenture. (2024, 13 May). *Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture.* GitHub Blog.
- URL: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/
- Fetched and read directly 2026-07-06.
- **Correction to the task brief / Uplevel follow-up-leads note:** this piece is dated **13 May 2024**, not November 2024. The November 2024 (updated Feb 2025) date belongs only to the code-quality study above. The two are frequently conflated in secondary write-ups because GitHub cross-links them; they are separate studies with separate designs and are extracted separately below.

### Verification status

**VERIFIED as primary, full read for both.** Both are GitHub-hosted blog posts, freely accessible, fetched directly (not via search-engine synthesis, not abstract-only). No academic paper, dataset, or appendix accompanies either — these are the fullest versions publicly available, structurally the same "marketing blog is the primary artefact" pattern already documented for Uplevel. No PDF gate exists for either (unlike Uplevel's and CodeRabbit's landing-page gating).

### (a-i) Code-quality study — design, population, findings

- **Tier: D (COI-flagged).** GitHub's own Customer Research team studying GitHub's own product. Direct vendor COI: a finding of improved code quality is commercially favourable to Copilot sales; the piece is explicitly framed (in its own text) as a rebuttal to "other studies" that found no quality improvement (implicitly Uplevel and similar).
- **Era: E1/E2.** Task was single-function Python API-endpoint writing with Copilot's IDE inline-suggestion/chat features (2024-era Copilot); no multi-file, plan-execute-verify agentic loop is described. Tagging E1/E2 blend rather than pure E1 because Copilot Chat was part of the 2024 product surface, but the study exercise itself is a bounded single-artefact writing task, not agentic. Not E3 under any reading — inadmissible for E3 claims without an explicit "pre-agentic" label, per PROTOCOL §2.
- **Design: randomised, but small and task-narrow.** Phase 1: 243 developers recruited (≥5 years Python experience), 202 valid submissions retained (104 with Copilot, 98 without) — developers "randomly assigned" to treatment. Task: write API endpoints for a web server. Phase 2: 25 independent developers conducted 1,293 blind pairwise code reviews of the Phase 1 submissions (reviewers did not know which submissions used Copilot).
- **Population:** externally recruited developers (not disclosed as GitHub employees); specific company affiliations not stated. This is a **lab task**, not telemetry on real production PRs — a materially different population/context from Uplevel's (real enterprise PR telemetry) and from CodeRabbit's (real open-source PRs).
- **Measurement basis: measured**, via three independent instruments — automated unit tests (functionality), a defined error-category rubric applied by human reviewers (readability/error density), and blind human approval ratings — not self-report survey.
- **Exact quality claims:**
  - Functionality: Copilot-assisted submissions **53.2% more likely to pass all 10 unit tests** (p<0.01)
  - Readability: **+3.62%** (p=0.003)
  - Reliability: **+2.94%** (p=0.01)
  - Maintainability: **+2.47%** (p=0.041)
  - Conciseness: **+4.16%** (p=0.002)
  - Errors-per-line-of-code: 18.2 lines/error (Copilot) vs 16.0 lines/error (no Copilot) — reported by GitHub as "13.6% more lines of code" needed to produce one error, i.e. fewer errors per line
  - Blind reviewer approval: reviewers **5% more likely to approve** Copilot-assisted code (p=0.014)
  - Error taxonomy scored: inconsistent naming, unclear identifiers, excessive line length, excessive whitespace, missing documentation, repeated code, excessive branching/loop depth, insufficient functionality separation, variable complexity — a readability/maintainability taxonomy, **not** a functional-defect or production-bug taxonomy.
- **Stated limitations (GitHub's own text):** the effect sizes on readability/reliability/maintainability/conciseness are explicitly flagged by GitHub itself as small ("1–3%") despite statistical significance; task was narrowly "writing API endpoints for a web server" with no discussion of generalisation beyond Python/web-API contexts. GitHub offers a speculative, self-serving explanation for why other studies (i.e. Uplevel) found the opposite: those developers "may have lacked the opportunity or incentive to focus on quality" — an unfalsified hypothesis about Uplevel's population, not a methodological critique of Uplevel's design.
- **No COI statement disclosed** on the page itself (no standard disclosure boilerplate); COI is structural and undisclosed rather than acknowledged.
- Does **not** mention Uplevel by name, nor the companion Accenture piece, in the fetched text.

### (a-ii) Accenture enterprise study — design, population, findings

- **Tier: D (COI-flagged, two-vendor: GitHub + Accenture, both with commercial stakes** — GitHub sells Copilot; Accenture markets itself as an AI-transformation consultancy and had a case-study/marketing interest in the engagement's success).
- **Era: E1/E2** — real-world enterprise Copilot IDE usage in 2024, no agentic tooling described.
- **Design: NOT an RCT despite loose secondary characterisation.** No random assignment described; this is an adoption/telemetry study of Accenture's own Copilot rollout, paired with a voluntary survey. No control group with random assignment is described — telemetry compares before/after adoption and survey responses are cross-sectional post-adoption. (Uplevel's follow-up-leads note calling this a "counter-research… 55% faster" figure was itself imprecise: the 55%-faster figure belongs to the unrelated Peng et al. 2023 RCT, which this Accenture piece cites as prior literature rather than reproducing.)
- **Population:** "developers who engage in a variety of software development tasks daily, including engineering, design, and testing," spanning "entry-level roles to team management positions." **No total n disclosed** for developers or PRs analysed — a material transparency gap, worse than Uplevel's (which at least had a secondary-sourced n, even if not confirmed from Uplevel's own primary text).
- **Measurement basis — kept separate per CLAUDE.md rule 4:**
  - **Measured (telemetry):** PR volume **+8.69%**; PR merge rate **+15%**; successful build rate **+84%**; suggestion acceptance rate **~30%**; day-1 IDE-extension installation **81.4%**; same-day acceptance among installers **96%**.
  - **Self-reported (survey):** 95% "enjoyed coding more"; 90% "felt more fulfilled"; 43% found it "extremely easy" to use; 70% reported reduced mental effort. These are perception measures, not quality or defect measures, and are recorded here as self-report per the rule, not folded into the "measured" figures above.
- **No explicit "confidence in code quality" percentage or defect/bug-rate figure was located in this piece** — the "85% more confident in code quality" figure attributed to GitHub/Accenture in Uplevel's follow-up-leads note was not found on this page as fetched; it likely originates from a different GitHub survey product (the annual GitHub octoverse/developer-survey line) and should not be attributed to this Accenture study without a direct citation. Flagging rather than repeating the unverified figure.
- **Stated limitations: none disclosed** on the page — no discussion of selection effects, confounds, or the access-vs-usage issue that undermined Uplevel's telemetry.
- **Critically: none of the (a-ii) figures are defect-rate or bug-rate measures at all** — they are volume/throughput/build-success/sentiment measures. "Successful builds +84%" is the closest proxy to a quality signal, but a successful build is a much weaker construct than "bug in PR" (Uplevel) or "issue flagged in review" (CodeRabbit) — it only confirms the code compiles/passes its build pipeline, not that it is defect-free.

---

## (b) CodeRabbit — "State of AI vs Human Code Generation Report"

### Citation

Loker, D. (CodeRabbit). (2025, 17 December). *State of AI vs Human Code Generation Report* (blog write-up of the whitepaper). CodeRabbit.
- Blog URL (fetched and read in full): https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
- Full whitepaper URL (lead-gen form, gated — **not** independently retrieved): https://www.coderabbit.ai/whitepapers/state-of-AI-vs-human-code-generation-report
- Press coverage used only for methodology triangulation, not as primary source: The Register (17 Dec 2025); Businesswire/VMblog press-release mirrors (both returned HTTP 403/ECONNRESET on fetch attempt, not used); Cybernews (403 on fetch, not used).

### Verification status

**PARTIALLY VERIFIED — same gating pattern as Uplevel.** The blog post is the fullest version accessible without submitting contact details; the whitepaper itself is gated behind a lead-generation form and was not retrieved. The blog post was fetched directly and read in full (confirmed byline "David Loker", 17 December 2025, "8 min read"). One figure surfaced only via an AI web-search synthesis ("Poisson rate ratios with 95% confidence intervals") was **checked directly against the primary blog text and found NOT to be present** — the blog's only stated statistical method is the unspecific "we used statistical rate ratios to compare how often different types of problems appeared in each group," with no CI, no p-values, no significance test disclosed anywhere in the fetched text. This is recorded as a caution against trusting search-engine-synthesised methodology claims; the primary text was the deciding source per the evidence rules.

### Tier, era, independence

- **Tier: D (COI-flagged).** CodeRabbit sells AI-assisted code review tooling; a finding that AI-authored code carries more risk directly motivates purchase of an AI code-review product. The blog post's own closing pitches CodeRabbit as the mitigation: "An AI code review tool like CodeRabbit helps by standardising code reviews… reducing the time and cognitive labor needed for reviews." No formal COI disclosure statement is present on the page — the COI is structural, not acknowledged.
- **Era: cannot be reliably assigned — flagged as a methodological gap, not resolved by assumption.** The report does not name which AI coding tools produced the 320 "AI-coauthored" PRs (no mention of Copilot, Cursor, Claude Code, Devin, or any agent/autocomplete distinction). Given the report's December 2025 vantage point and open-source population, the true mix is very plausibly majority E2/E3 (chat-assisted and agentic tools are now the OSS-contribution norm), but this is an inference, not a disclosed fact — the report itself supplies no tool-modality breakdown to tag against PROTOCOL §2's "tag by modality actually studied" rule. **Recorded as UNTAGGABLE/mixed rather than assumed E3** — do not cite this source for an E3-specific claim.
- **Independence: none.** Single-vendor-authored, uses the vendor's own proprietary review tool as the sole measurement instrument (see below), and closes with a product pitch.

### Method & population

- **Population: 470 open-source GitHub pull requests** — 320 labelled "AI-coauthored", 150 labelled "human-only". No repository names, no time window/date range for PR collection, and no sampling method (random? convenience? curated?) are disclosed anywhere in the fetched text or in secondary coverage checked.
- **AI-authorship labelling — a self-acknowledged, unresolved confound:** the report states, in its own words: *"Since it was impossible to directly confirm authorship of each PR of a large enough OSS dataset, we checked for signals that a PR was co-authored by AI and assumed that those that didn't have it were human authored."* The detection signals themselves are not specified. CodeRabbit explicitly concedes: *"we cannot guarantee all the PRs we labelled as human authored were actually authored only by humans."* This is a labelling confound of the same character as Uplevel's access-vs-usage confound: the comparison groups are not verified ground truth, only proxy-detected, and mislabelled "human" PRs (if actually AI-touched) would bias the reported gap **toward zero**, not away from it — i.e., the true gap (if the underlying effect is real) could be larger, or the effect could equally be partly an artefact of noisy labelling. Either direction is possible; the report does not quantify labelling error, so no correction is possible from the text.
- **Issue-detection instrument: CodeRabbit's own automated review tool ("CodeRabbit's structured issue taxonomy"), not independent human reviewers and not a neutral third-party static-analysis tool.** This is the single most important COI mechanism in the record: the vendor's own product is simultaneously (a) the thing being marketed and (b) the measurement instrument generating the headline statistic. No inter-rater reliability, no human-adjudicated ground truth, and no comparison against an independent linter/SAST tool is described.
- **Measurement basis: measured** (automated tool output), not self-report — but "measured by the vendor's own product being marketed on the back of the finding" is a distinct and more severe independence problem than ordinary telemetry COI (contrast with Uplevel and the GitHub/Accenture telemetry figures above, which at least used the platforms' own git/CI data rather than a bug-detection product with a direct commercial stake in finding bugs).

### Exact headline claims

- **Overall: AI-coauthored PRs carry ~1.7x more issues than human-only PRs** — raw rates **10.83 issues/PR (AI) vs 6.45 issues/PR (human)**.
- **Severity split:** "1.4x more critical issues and 1.7x more major issues" in AI-coauthored PRs (exact tiering/definition of critical vs major not further specified in fetched text).
- **Category multipliers reported:**
  - Logic/correctness: **75% more common** (≈1.75x)
  - Readability: **~3x** more common ("spiked more than 3x" per secondary coverage; blog itself frames it as a multiple in the same range)
  - Security vulnerabilities: **up to 2.74x** higher (The Register specifies this includes XSS vulnerabilities specifically: "2.74x more likely to add XSS vulnerabilities")
  - Formatting: **2.66x** more common
  - Error handling/exception-path gaps: **~2x**
  - Concurrency/dependency correctness: **~2x**
  - Excessive I/O (performance): **~8x** (largest single multiplier reported, on what is likely the smallest base-rate category — no denominator given)
- No confidence intervals, p-values, or significance tests are stated for any of these figures in the primary text as fetched (see Verification status above on the discrepancy with the search-synthesis claim of "Poisson rate ratios with 95% CI" — not corroborated against the primary page).

### Stated limitations (CodeRabbit's own text)

- Cannot guarantee "human-only" labelled PRs are actually human-only (labelling confound, above)
- Open-source only — explicitly a different population from enterprise/proprietary codebases; the report does not claim enterprise generalisation
- Imbalanced group sizes (320 vs 150) with no disclosed correction
- No AI-tool-modality breakdown (autocomplete vs agentic) — a gap the report does not itself acknowledge but which matters directly for era-tagging under this protocol

### Independent commentary found

The Register (17 Dec 2025) notes without further detail that "contrasting research from University of Naples (August 2025) and Monash/Otago universities (January 2025) reaches different conclusions" on AI code quality — flagged here as a lead for a possible independent Tier A/B check, **not extracted** (out of scope for this remediation task; queue for Phase 1/2 if pursued).

---

## What this combined record can and cannot support

**Can support:** (a) two additional, mutually independent-of-each-other Tier D vendor datapoints on Copilot/AI-code quality, each with a COI running in the opposite commercial direction from Uplevel's and from each other (GitHub benefits from "quality improves"; CodeRabbit benefits from "AI code is riskier, buy review tooling"); (b) a second worked example (alongside Uplevel's access-vs-usage confound) of a labelling/measurement confound undermining a vendor defect-rate claim — CodeRabbit's unverified AI/human PR labels; (c) a demonstration that "vendor's own product is the measurement instrument" (CodeRabbit) is a more acute independence problem than "vendor's own telemetry platform measures adjacent metrics" (GitHub/Accenture, Uplevel) — useful nuance for RQ2/RQ6 on measurement trustworthiness.

**Cannot support:** any load-bearing exec-brief defect-rate or code-quality effect size. The GitHub code-quality study's own figures are small (1–3%) lab-task readability/maintainability effects on a bounded single-function task, not a defect/bug-rate measure comparable to Uplevel's "+41% bugs" or CodeRabbit's "1.7x issues" — the three sources are measuring three non-comparable constructs (self-defined "bug" in real PRs; a researcher-defined readability/maintainability rubric on lab-task code; an off-the-shelf AI review tool's own issue taxonomy on OSS PRs). The Accenture piece supplies no defect/bug/quality figure at all, only volume/throughput/build-success/sentiment — it should stop being cited in this contradiction as if it were opposing quality evidence; at most it is opposing *adoption/throughput* evidence. None of these three documents can be triangulated into a single number; none is era-comparable to another (E1/E2 lab task vs E1/E2 enterprise telemetry vs untaggable-likely-E2/E3 OSS PRs).

## Relation to the existing contradiction entry (synthesis/contradictions.md, "Copilot defect-rate")

The existing entry's Side B was a placeholder ("NOT YET EXTRACTED") attributing to GitHub/Accenture a single bundled set of figures ("55% faster, 85% more confident in code quality, 8.69% more PRs, 15% higher merge rate, 84% increase in successful builds") as if from one document. Full reading shows this bundle actually spans **at least three distinct GitHub-family artefacts** (the unrelated Peng et al. 2023 RCT for "55% faster"; the May 2024 Accenture piece for the throughput/build/adoption figures; the Nov 2024/Feb 2025 study for the only genuine quality-construct figures, none of which is "85% more confident in code quality" — that specific figure was not located in either document read). The "85% more confident" figure should be treated as unverified/misattributed until a source is found; it is not being carried forward as extracted here. This record adds CodeRabbit as a second, independent-COI Side B datapoint not previously in the ledger at all.

## Recency check

Both are within the 12-month window as of 2026-07-06 (Nov 2024/May 2024/Feb 2025 update, and Dec 2025) or borderline; no retraction found for either. No 2026 successor or replication was located for the GitHub code-quality study in the course of this fetch; CodeRabbit's report is recent enough that no successor is expected yet.
