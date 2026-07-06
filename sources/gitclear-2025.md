# gitclear-2025 — GitClear AI code quality report family (2024, 2025, 2026 editions)

One record for the family; the most recent edition (2026, "The Maintainability Gap") is the primary record, but the 2025 edition is the only one whose full text was readable, so exact figures below are anchored there and the 2026 public-page figures are recorded with an access caveat.

## Citation(s)

**2026 edition (primary, most recent):**
Harding, W. (Bill). (2026). *The Maintainability Gap: 2026 AI Code Quality Research.* GitClear.
- Canonical URL: https://www.gitclear.com/the_ai_code_quality_maintainability_gap
- Publication date: not stated on the public page. Data is described as running to "year-to-date 2026" (copy/paste at 15.7% of changed lines in H1 2026), which implies a mid-2026 release; GitClear's separate January 2026 piece ("AI Coding Tools Attract Top Performers — But Do They Create Them?") is referenced as prior work, so the Maintainability Gap post-dates January 2026. Exact date UNCONFIRMED.
- Full report: **email-gated** (business email + name + job title required). No freely hosted PDF found (the S3 naming pattern used for the 2025 PDF returns 403 for guessed 2026 names).

**2025 edition (full text read):**
Harding, W. (William), Lead Researcher & CEO. (2025, 4 February). *AI Copilot Code Quality: Evaluating 2024's Increased Defect Rate via Code Quality Metrics — 211m lines of analyzed code + projections for 2025.* Alloy.dev Research / GitClear. Version v2025.2.5.
- Landing page (headline variant "AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones"): https://www.gitclear.com/ai_assistant_code_quality_2025_research
- Freely downloadable PDF (34 pp., read in full for this record): https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf
- The report's own Updates section: "No updates have been made since publication on February 4, 2025."

**2024 edition (first in series; verified to exist, landing page only):**
GitClear (Harding, W.). (2024, January). *Coding on Copilot: 2023 Data Suggests Downward Pressure on Code Quality (incl 2024 projections).* GitClear. 153M changed lines, Jan 2020–Dec 2023.
- https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality

## Verification status

**2025 edition: VERIFIED** — full 34-page PDF fetched and read; figures below are quoted from the PDF body and appendices.
**2026 edition: PARTIALLY VERIFIED** — the report exists and its landing page (with all eight headline deltas and several exact baselines) was read directly, but the full PDF is email-gated, the publication date is not stated on the public page, and the author byline is inferred from third-party coverage naming GitClear founder Bill Harding. Could NOT read: error-masking construct definition, churn baseline percentages for the +15% figure, per-year tables, methodology appendices, and the authors' caveats section.
**2024 edition: VERIFIED to exist** (landing page read); not extracted in depth — superseded by later editions.

## Tier & era & independence

- **Tier: B, with a mandatory COI flag.** PROTOCOL §3 places "multi-company code-quality analyses" (large-scale telemetry without randomisation) in Tier B, and this is exactly that: ~1bn lines classified, 211M–623M meaningful changes analysed, mixed private-corporate and open-source population. However, GitClear **sells the code-analysis product that produces every metric in the report** — the reports are top-of-funnel marketing, the Diff Delta / operation-classification method is proprietary and not independently auditable, and the report body contains explicit product promotion (Appendix A3 is a sales pitch). Treat as **Tier B (COI-flagged, vendor-published)**: carries claims with caveats, but should never carry an exec-brief claim without independent corroboration. One line: graded B not D because the underlying data is genuine multi-company telemetry at scale, not opinion or survey marketing — but the COI flag is non-negotiable.
- **Era: trendline spanning E1→E3; findings are era-aggregate, not modality-segmented.** GitClear telemetry does not identify which lines were AI-authored or which tool modality produced them; every finding is a year-over-year population trend correlated with the era of AI adoption. 2025 edition (data Jan 2020–Dec 2024): **E1/E2** — the report itself estimates GitHub Copilot (41.2% usage, ~4–8k context window) as the dominant assistant of 2024, i.e. autocomplete-era. Admissible as historical baseline/trendline only. 2026 edition (data 2023–H1 2026): **E2/E3 blend with E3-era endpoints** — the 2025–2026 data points fall in the agentic era, making this the family's only E3-relevant evidence, but the modality mix within it is unmeasured.
- **Independence flags:** vendor-published (COI); population is GitClear's own customer base (~2/3 private corporations opted into anonymised sharing) plus ~1/3 large open-source repos (Chromium, React, VS Code, Kubernetes, Postgres, cpython, etc.) — selection is "orgs that buy code-analytics tooling + megaprojects", not a random sample; dataset composition shifts year to year (the report admits "our line counts this year were not identical to the numbers that our database produced at the beginning of 2024"); **no causal identification** — no counterfactual, no AI-attribution of lines, so layoffs, team churn, and repo-mix drift are unexcluded confounders.

## Method & population/dataset

- **Measurement basis: measured (telemetry)** throughout — server-side classification of git commits. The only self-reported numbers quoted are secondary (Stack Overflow 2024: 63% of professional developers use AI, 14% plan to).
- **2025 edition dataset:** 211 million meaningful changed lines, Jan 2020–Dec 2024, from a ~10,000-repo sample; ~2/3 private corporations (e.g. NextGen Health, Bank of Georgia named as customers), ~1/3 open source (25 named repos + ~80 more). Roughly half of raw "lines changed" (GitHub-style counting) are excluded as no-op/auto-generated before analysis. **2026 edition dataset:** 623 million analysed changes, 2023–2026 (composition detail behind the email gate).
- **Operation definitions (2025 PDF, Appendix A0):** every changed line is classified as one of seven operations — **Added** (new distinct lines), **Deleted** (removed, not re-added within two weeks), **Moved** (cut-and-pasted to a new file or function, content unchanged — "the signature of code reuse"/refactoring), **Updated** (existing line modified by roughly three words or less), **Find/Replaced** (same string substituted in 3+ locations), **Copy/Pasted** (identical line contents, excluding language keywords, committed to multiple files or functions **within a single commit**), **No-op** (excluded). **Churn** (not an operation): a line "authored, pushed to the git repo, and then reverted or substantially revised within the subsequent two weeks" — glossed as changes "either incomplete or erroneous" when first pushed.
- **Duplicate block detection (2025, Appendix A8):** any region of 5+ contiguous repeated lines (ignoring blank/keyword lines), Type-1 clones; pre-2024 years backfilled by scanning the 1,000 largest commits per repo — a method the authors argue biases *toward* finding duplication in earlier years, i.e. against their own conclusion.
- SQL/ActiveRecord queries for the headline tables are printed in the 2025 appendix; the underlying line-level data and the Diff Delta classifier are not public.

## Key findings

All measured (telemetry). Primary task-type tag **T5** (refactoring/tech debt — moved-lines and legacy-maintenance metrics are direct T5 measures); duplication/churn findings are cross-cutting quality-debt signals affecting **T4** (maintainability of mature codebases); none of the findings are per-task-type.

### 2025 edition (data 2020–2024; era E1/E2 baseline)

1. **Moved (refactored) lines collapsed:** 24.1% of changed lines (2020) → 20.5% (2022) → 15.8% (2023) → **9.5% (2024)**; −39.9% YoY 2023→2024. "2024 marked the first year GitClear has ever measured where the number of 'Copy/Pasted' lines exceeded the count of 'Moved' lines." [T5; measured]
2. **Copy/pasted lines rose:** 8.3% (2020) → 10.6% (2023) → **12.3% (2024)**; +17.1% YoY. (Appendix percentages differ by decimals from the body table: 8.86% → 12.32%; body table quoted here.) [T5/T4; measured]
3. **Duplicated blocks (5+ lines) surged:** percent of scanned commits containing a duplicate block: 0.70% (2020), 0.45% (2022), 1.80% (2023), **6.66% (2024)** — the landing-page "4x growth in code clones" is 1.80→6.66; the body also describes "an 8-fold increase in the frequency of code blocks with 5+ duplicated lines during 2024" (total blocks found 20,448 → 63,566 against a smaller rise in commits scanned) and "approximately 10x higher than two years prior". Record all three phrasings; they use different denominators. [T4; measured]
4. **Two-week churn rose:** 3.1% (2020) → 3.3% (2022) → 4.5% (2023) → **5.7% (2024)**; +26% YoY. Note: this **undershot** GitClear's own 2024 projection of 7.1% — their prior-year prediction that churn would double vs 2021 did not materialise (they acknowledge: "Thankfully, short-term churn has not yet reached 7%"). New-lines-only churn (Appendix A7, 45M lines): revised within 2 weeks 4.78% (2020) → 7.04% (2024); revised within a month 5.49% (2020) → 7.91% (2024) — i.e. "a 20–25% increase [vs 2021] in the percent of new lines that get revised within a month". (Secondary summaries citing "7.9% churn" are quoting this revised-within-a-month figure, not the headline churn series.) [T4; measured]
5. **Added code share grew:** 39.2% (2020) → **46.2% (2024)** of changed lines; find/replaced +16.7% YoY (credited partly to lint-autofixing IDEs like Cursor). [measured]
6. **Age of revised code shifted sharply newer:** lines revised within 2 weeks of authorship: ~60% (2020–2023) → **69.7% (2024)**; changes touching code over a year old fell (24.7% → 16.9% for <1 year-old bucket shrinking, 2+ year-old code at ~1%). Only ~20% of 2024 modified lines touched code older than a month (vs ~30% in 2020). [T5; measured]
7. **Defects — indirect only.** The 2025 edition, despite its title, contains **no direct defect measurement**. Its defect argument is: (a) its own 2024-edition prediction that Google DORA 2024 would show quality decline "came true" — DORA 2024 modelled a **7.2% decrease in delivery stability per 25% increase in AI adoption** (quoted from DORA, not GitClear data); (b) the code-clone literature (Mo/Zhang 2023: 57.1% of co-changed clones involved in bugs; Mondal 2017 and Wagner 2016: 17–18% propagated-bug/fault rates in clones) implies rising duplication ⇒ rising defects. Chain of inference, not measurement. [measured-by-others; do not cite as a GitClear defect finding]
8. **2025 projections (not measurements):** moved 3.1%, copy/paste 13.9%, churn 6.9% (Appendix A1 "2025" row). Their 2024 projections got direction right, magnitude wrong in both directions (moved fell faster than projected; churn rose slower).

### 2026 edition (data 2023–H1 2026; E2/E3; public landing page only — full report unread)

Eight quality signals, headline deltas as stated on the public page:
1. **Refactoring line moves down ~70% vs 2022**; moved code at **3.8% of changed lines year-to-date 2026** (page cites 21% in 2022 — note this disagrees slightly with the 2025 PDF's 20.5% for 2022; dataset composition drift). Copy/paste now ~5x more prevalent than refactoring, vs a 2x relationship pre-AI. [T5; measured]
2. **Within-commit copy/paste +41%**, reaching **15.7% of changed lines in H1 2026**. [T4/T5; measured]
3. **Code block duplication +81%:** 40.3 per million changed lines (2023) → **73.0 year-to-date 2026** — highest on record. [T4; measured]
4. **Cross-file function calls (reuse/connectivity) down 35% since 2023:** 343 → **223 method calls per thousand changed lines** — a new metric in this edition. [T4/T5; measured]
5. **Long-term update percent down 74%:** share of changes touching code last modified 12+ months ago fell from 1.7% (2023) → **0.46% (YTD 2026)** — legacy maintenance increasingly not happening. [T5; measured]
6. **Error-masking constructs +47%** — definition not on the public page (behind email gate). Potentially the most defect-relevant new signal; unverifiable at present. [T8-adjacent; measured; UNVERIFIED detail]
7. **Two-week code churn +15%** — baseline and endpoint percentages not public. [measured; UNVERIFIED detail]
8. Framing quote from the page: "The headline is not 'AI writes bad code'" but that the "default AI workflow is incentivized to deliver atomic code… while quietly taxing the invisible and the deferred."

### Authors' own caveats (2025 PDF)

- "This is not to say that AI isn't incredibly useful."
- Dataset composition evolves year to year as customers change; line counts are not stable across report vintages.
- Duplicate-block backfill favoured large commits (argued to bias against their conclusion).
- The study includes commented lines and does not split test vs non-test code ("future research").
- Their own prior projections missed (churn overshoot documented above) — to their credit, recorded in the report.

## What this can and cannot support

Can support: directional, era-aggregate claims that refactoring/code-reuse activity has collapsed and duplication has risen sharply across a large multi-company codebase population coinciding with AI adoption (with corroboration required per COI flag). Cannot support: causal attribution to AI, per-line AI authorship claims, any defect-rate effect size (GitClear measures none directly), modality-specific (E3 agentic) effects, or generalisation beyond code-analytics-buying orgs and megaproject OSS.

## Corrections vs the seed description (PROTOCOL §6)

- Seed "GitClear 2025–2026 code quality reports — churn/duplication in the agentic era": **partially correct.** The 2025 report's data ends December 2024 and is dominated by autocomplete/chat-era tooling (Copilot at 41.2% usage, ~4–8k context) — it is **pre-agentic (E1/E2)** and only supports baselines. Only the 2026 "Maintainability Gap" edition (data to H1 2026) reaches the agentic era, and its full text is email-gated.
- A 2026 edition **does exist**: *The Maintainability Gap* (GitClear, mid-2026; exact date unconfirmed). There is also a separate January 2026 GitClear research piece ("AI Coding Tools Attract Top Performers — But Do They Create Them?") — distinct publication, not the annual quality report.
- "Rising churn" is the **weakest** leg of the seed claim: GitClear's own 2024 churn (5.7%) undershot their doubling prediction (7.1%), the 2026 delta (+15%) is the smallest of their eight signals, and a peer-reviewed study of 151 OSS repos found **no general churn increase** after GenAI adoption (see leads). Duplication growth and refactoring decline are the stronger, better-evidenced legs.
- "Declining refactoring ('code reuse')": **confirmed and quantified** — moved lines 24.1% (2020) → 9.5% (2024) → 3.8% (YTD 2026); plus new 2026 connectivity (−35%) and long-term-maintenance (−74%) metrics.
- The widely quoted "defect rate" framing of the 2025 edition's title is **not** a GitClear measurement — it rests on Google DORA 2024 and older clone-defect literature.

## Follow-up leads (for Phase 1 queue — not extracted)

1. **arXiv 2507.10422 — "Self-Admitted GenAI Usage in Open-Source Software"** — https://arxiv.org/abs/2507.10422 — 151 OSS repos with self-admitted GenAI use; finds **no general increase in code churn** after adoption (average file-based churn 0.17→0.06; line-based 0.68→0.50) — direct contradiction of the churn narrative; candidate for `synthesis/contradictions.md` once extracted.
2. **arXiv 2606.21804 — "Is Agent Code Less Maintainable Than Human Code?"** — https://arxiv.org/abs/2606.21804 — direct E3-era test of the maintainability question with agent attribution; potentially the independent corroboration/refutation the COI flag demands.
3. **arXiv 2603.28592 — "Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild"** — https://arxiv.org/abs/2603.28592 — tracks technical debt inside confirmed AI-authored commits; notes causal attribution is not possible in observational cohorts.
4. **arXiv 2603.27130 — "A Large-Scale Empirical Study of AI-Generated Code in Real-World Repositories"** — https://arxiv.org/abs/2603.27130 — independent repo-level telemetry on AI-code quality.
5. **arXiv 2601.16809 — "Will It Survive? Deciphering the Fate of AI-Generated Code in Open Source"** — https://arxiv.org/abs/2601.16809 — line-survival analysis of AI-authored code; complements churn/durability questions.
6. **Google DORA 2024/2025** (already an anchor) — GitClear's defect argument leans entirely on DORA 2024's −7.2%-stability-per-25%-adoption model; when extracting DORA, check whether 2025/2026 editions still support that figure (PROTOCOL §5 tension 3).
7. **Uplevel (2024) +41% bug rate** (PROTOCOL §5 tension 4) — GitClear provides **no independent defect measurement** that corroborates Uplevel; its duplication findings are only mechanism-level support. Caution: the 2026 GitClear report's "+41% copy/paste" figure coincidentally matches Uplevel's "+41% bug rate" — do not conflate the two numbers in synthesis.
8. **LeadDev, "How AI generated code compounds technical debt"** — https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt — Feb 2025 practitioner coverage of the 2025 edition (Tier C commentary, useful for reception).
9. **devclass, "AI is eroding code quality states new in-depth report"** — https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250 — trade-press coverage with some critical framing.
10. **Rob Bowley blog (17 Feb 2025)** — https://blog.robbowley.net/2025/02/17/gitclears-latest-report-indicates-genai-is-having-a-negative-impact-on-code-quality/ — uncritical endorsement but raises the tech-layoffs confounder; evidence of how the report is consumed.
11. **GitClear (Jan 2026), "AI Coding Tools Attract Top Performers — But Do They Create Them?"** — separate 2026 GitClear research; queue for RQ1/RQ3 triage (same COI flag).

## Recency check notes

- Checked 2026-07-06. The 2025 edition (Feb 2025, >12 months old at next review) is **superseded** by the 2026 Maintainability Gap edition for current-state claims; retain the 2025 PDF for its exact tables, definitions, and E1/E2 baseline. No retraction of any edition found; the 2025 PDF's own Updates section confirms no post-publication revisions.
- Standing critique landscape (no single canonical takedown found): black-box proprietary methodology; customer-base selection; year-to-year dataset drift admitted by the authors; correlation-only design (layoffs and repo-mix as live confounders); and the peer-reviewed churn contradiction (lead 1). No published methodological rebuttal from GitClear to that study was found.
- **Escalation item:** the 2026 full report is email-gated. If Tier B treatment requires the full text (error-masking definition, churn baselines, methodology appendix), a human should register for the PDF — one email-form step; everything else in this record is verifiable from public pages plus the 2025 PDF.
