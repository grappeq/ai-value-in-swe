# review-agents-reality-2026 — "From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests"

**source_id:** review-agents-reality-2026
**Date verified:** 2026-07-06 (Phase 1 FETCH+EXTRACT)
**RQs fed:** RQ1 (T7 code review value map), RQ2 (claims-vs-reality / hype-baseline correction — this is the job description), T7 primary

## Citation

Chowdhury, K., Banik, D., Ferdous, K. M., & Shamim, S. I. (2026). *"From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests."* Proceedings of the 23rd International Conference on Mining Software Repositories (MSR 2026) — **Mining Challenge track** (poster presentation, Mon 13 Apr 2026, Session 2 – Posters). DOI: 10.1145/3793302.3793614.
arXiv preprint: [2604.03196](https://arxiv.org/abs/2604.03196), v1 only, submitted Fri 3 April 2026, 17:15:15 UTC. No v2 found.

**Authors and affiliations:**
- Kowshik Chowdhury — Kennesaw State University, Marietta, Georgia, USA
- Dipayan Banik — Quanta Technology, Raleigh, North Carolina, USA
- K M Ferdous — Kennesaw State University, Marietta, Georgia, USA
- Shazibul Islam Shamim — Kennesaw State University, Marietta, Georgia, USA

**CMU-lab / AIDev-authorship overlap check:** No overlap on either count. None of the four authors appears on the He/Agarwal/Vasilescu CMU-lab papers already in this evidence base (he-2026-2x-mandate, agents-vs-ides-2026, cursor-velocity-quality-2025). None is a co-author of the AIDev dataset paper itself (Li et al. 2025, "The rise of AI teammates in software engineering (SE 3.0)" — cited in this paper's related work as the dataset's origin, not as a self-citation). This is a genuinely third-party analysis of AIDev, authored by a small US-university team plus one industry co-author (Quanta Technology, a grid/power-engineering consultancy — no plausible AI-tooling vendor interest). **Independent voice**, subject only to the dataset-provenance caveat below, not an authorship-overlap caveat.

## Verification status

**VERIFIED — full text obtained via WebFetch of the arXiv HTML rendering (arxiv.org/html/2604.03196), cross-checked against the abstract page (arxiv.org/abs/2604.03196) and the MSR 2026 conference programme page.** This is a full-text read: section-level detail was extracted for methodology, all result tables, the signal-ratio formula, the per-CRA-tool breakdown, limitations/threats-to-validity, and related work — not an abstract-only pull. One nuance surfaced only via the conference programme page, not the arXiv listing: the paper is published in MSR 2026's **Mining Challenge track** (poster), not the main technical-papers track. It carries a DOI and is described as peer-reviewed, but the Mining Challenge track at MSR is historically a lighter-weight, shorter-paper venue (designed around a shared "mining challenge" dataset — here, AIDev) than the main research track; this is recorded as a tier-relevant nuance below, not a disqualifier.

## Dataset provenance (AIDev — dependency-hub caveat)

**Source dataset:** AIDev, created by Li et al. (2025), hosted on HuggingFace, containing PR review data from open-source repositories with AI-agent-generated code. This is the same dataset family already flagged in LEDGER.md as a provenance hub for MSR 2026 agentic-PR studies (task-stratified-agents-2026 and unreviewed-ai-prs-2026 in this evidence base both draw on it).

**Exact slice used by this paper** (traced through the filtering pipeline, distinct from the other two AIDev-derived sources already extracted):
1. Starts from the `PRReviewComment` table: **19,450** individual PR-review-comment records (this is the "19,450 AIDev PRs" figure in the triage note — more precisely, 19,450 is a comment-record count, not a PR count, before enrichment).
2. Enriched/aggregated by joining against the `PullRequest` and `PRReview` tables to reconstruct one row per unique PR → **3,177 unique PRs**.
3. Bot-filtering pass removes CI/CD bots (e.g. `github-actions[bot]`) that are not code-review agents, retaining only genuine CRAs → **3,109 unique PRs** (matches the triage note exactly).
4. Of those 3,109, the reviewer-composition/merge-rate analysis is run specifically on the **2,456 PRs in the "Commented" review state** (281 CRA-only + 1,176 human-only + 117 mixed-CRA-dominant + 278 mixed-human-dominant + 604 mixed-equal = 2,456) — PRs with formal APPROVED/CHANGES_REQUESTED review states are handled separately, since "CRAs provide feedback without making explicit merge decisions" (i.e. CRA-only PRs structurally can only appear in the Commented bucket).

**Slice relationship to sibling AIDev sources in this evidence base:** this paper's unit of analysis is PR-review-comment threads filtered down to a Commented-state subset; unreviewed-ai-prs-2026 works from a different AIDev slice (the creators' own pre-curated population, per its existing ledger note) and task-stratified-agents-2026 uses yet another cut (per-agent-tool PR outcomes). **These are not the same 3,109/2,456 PRs as either sibling source** — they overlap in ultimate dataset origin (AIDev) but the specific populations differ by filtering criteria. Any cross-source comparison must treat this as "same dataset family, different slices," not "same sample," per the shared-population caveat this task was briefed to apply.

## Tier, era, independence

- **Tier: B — large-N observational mining study, no counterfactual/randomisation, no experimental manipulation.** Consistent with the tier already assigned to task-stratified-agents-2026 and unreviewed-ai-prs-2026, the other two AIDev-derived MSR 2026 sources in this base. Downward nuance not present in those two: **Mining Challenge track / poster, not main research track** — this is a real but modest quality discount within Tier B (shorter paper, lighter peer-review bar than a full MSR research-track submission), not a demotion to Tier C, since it still reports a defined dataset, explicit methodology, a statistical test, and a threats-to-validity section.
- **Era: E3, confirmed.** The reviewed entities are code review agents (CRAs) — Copilot, GitHub Advanced Security bot, Cursor bot, ellipsis-dev, entelligence-ai, codefactor-io, aikido, semgrep-code-assistant, and others — operating as autonomous or semi-autonomous reviewers on PRs, many of which are themselves agent-authored. Squarely agentic-review-of-agentic-output, matching §2's E3 definition. No E1/E2 modality is in scope.
- **Independence:** independent of AIDev's creators and of the CMU lab cluster (see above). **The claims under test are explicitly vendor claims** — that is the paper's whole point, not an incidental COI: Qodo (2025, a CRA vendor) and Greptile (2025, a CRA vendor, via a company-blog piece by "Butler") are the two cited sources for the "~80%" and related figures, and the paper treats them as motivating industry rhetoric to be checked empirically, not as data to be trusted. **COI flag on the tested claims, not on this paper's authors** — worth stating precisely in any synthesis use: this paper is not vendor-funded, but its object of study is vendor marketing.

## Industry claims tested (quoted, with sources)

1. **Qodo (2025)**, cited as a survey of 609 developers: **"81% of CRA users see quality improvements and 69% see speed improvements"**; and, the sharper claim: **"80% of PRs receiving no human comments when CRAs are enabled."** This is the specific number behind the triage note's "~80% of PRs handled unassisted" framing.
2. **Greptile company blog (Butler, 2025)**: **"82% of developers use CRAs daily or weekly."** (An adoption-frequency claim, not an outcome claim — the paper does not directly test this one empirically; it is cited as context for how normalised CRA use has become, alongside the OpenAI Codex "400,000+ PRs in two months" scale claim used to motivate the study.)
3. **Paper's own framing of the tested claim, verbatim**: "industry reports and blogs suggest CRAs can handle most PRs with minimal human oversight."

## Empirical findings — exact numbers

**How "handled unassisted" is operationalised:** the paper does not adopt Qodo's exact construct ("PRs receiving no human comments"). Instead it classifies each of the 2,456 Commented-state PRs by **reviewer composition** — CRA-only (zero human reviewers present in the thread), human-only, or one of three mixed categories (CRA-dominant / human-dominant / equal, presumably by comment-count share, though the exact mixed-category cutoff proportions are not stated in the extraction obtained) — and then asks what happens to PRs in each bucket, rather than asking what share of all PRs receive zero human comments. **This is a meaningfully different operationalisation from Qodo's "80% received no human comments" framing**: Qodo's claim is about *incidence* of human-free review; this paper's headline numbers are about *outcomes conditional on* being human-free. The paper does not report what share of its 3,109 (or 19,450-comment-derived) PRs are CRA-only in the first place, so it cannot directly confirm or refute Qodo's 80%-incidence figure on an apples-to-apples basis — it tests a related but distinct claim (do CRA-only PRs succeed at comparable rates to human-reviewed ones), which is the more decision-relevant question for RQ1/RQ2 purposes anyway.

**Merge-rate table (Commented-state PRs, n=2,456):**

| Reviewer composition | n | Merged | Merge rate | Closed (unmerged) | Closure rate | Stalled |
|---|---|---|---|---|---|---|
| CRA-only | 281 | 127 | **45.20%** | 98 | 34.88% | 56 |
| Human-only | 1,176 | 804 | **68.37%** | 254 | 21.60% | 118 |
| Mixed (CRA-dominant) | 117 | 74 | 63.25% | 17 | 14.53% | 26 |
| Mixed (human-dominant) | 278 | 189 | 67.99% | 41 | 14.75% | 48 |
| Mixed (equal) | 604 | 369 | 61.09% | 128 | 21.19% | 107 |

**Headline gap: CRA-only merge rate is 23.17 percentage points lower than human-only (45.20% vs 68.37%).** Chi-squared test of independence across the full table: χ² = 83.0319, df = 8, **p < 0.001** — statistically significant association between reviewer composition and outcome (merged/closed/stalled), though the paper explicitly notes in its own validity section that this is an association, not a causal claim ("correlation does not imply causation").

**Signal-quality analysis (98 closed CRA-only PRs — i.e. the subset of the 281 CRA-only PRs that reached a closed, non-merged state):**

Signal ratio formula: Signal Ratio = (Tier-1 count + Tier-2 count) / Total comments, where Tier 1 = critical signal (runtime errors, crashes, compilation failures, API-breaking changes, security vulnerabilities) and Tier 2 = important signal (architectural problems, performance issues, maintainability concerns) — implying an unstated Tier 3/residual = noise (style nits, restatement, non-actionable commentary), classified via keyword-based rules validated manually by two researchers.

| Signal range | n (of 98) | % |
|---|---|---|
| 0–30% (predominantly noisy) | 59 | **60.2%** |
| 31–59% (more noise than signal) | 14 | 14.3% |
| 60–79% (more signal than noise) | 7 | 7.1% |
| 80–100% (high-quality) | 18 | 18.4% |

**Per-CRA-tool breakdown (13 unique bots identified; n and average signal ratio where reported):**

| CRA tool | PRs | Avg signal ratio |
|---|---|---|
| github-advanced-security[bot] | 36 | 27.62% |
| Copilot | 24 | 19.79% |
| ellipsis-dev[bot] | 11 | not specified in extraction |
| entelligence-ai-pr-reviews[bot] | 7 | 52.29% |
| cursor[bot] | 5 | 43.40% |
| codefactor-io[bot] | unspecified n | 0.00% |
| aikido-pr-checks[bot] | unspecified n | 20.00% |
| semgrep-code-assistant-ws[bot] | unspecified n | 25.00% |
| semgrep-code-getsentry[bot] | 1 | 100.00% |
(four further bots named as making up the 13 total were not itemised in the extraction pass obtained)

**Headline: 12 of 13 CRAs (92.31%) show average signal ratios below 60%.** Only the n=1 outlier (semgrep-code-getsentry[bot], 100%) and entelligence-ai-pr-reviews[bot] (52.29%, still below 60% despite being the best multi-PR performer) approach a majority-signal profile; the two most-used tools by volume in this sample — GitHub Advanced Security bot (n=36) and Copilot (n=24) — are also two of the *lowest*-signal tools (27.62% and 19.79% respectively), i.e. volume and quality are inversely related in this sample, though n is small throughout and no confidence intervals are reported for any per-tool figure.

**Measured vs self-reported:** every number in this paper is **measured** (derived from AIDev's stored PR/review/comment records), in direct contrast to the **self-reported** industry figures it tests (Qodo's 609-developer survey, Greptile's blog claim). This paper is itself the "measured" side of a measured-vs-self-reported delta that CLAUDE.md rule 4 requires be recorded explicitly: Qodo's self-reported "80% no-human-comments" / "81% quality improvement, 69% speed improvement" vs this paper's measured 45.20% CRA-only merge rate and 92.31%-of-CRAs-below-60%-signal finding. The two are not measuring identical constructs (see operationalisation note above), which somewhat softens direct comparison, but the directional contrast — vendor survey reports broad satisfaction/coverage, independent PR-mining finds a substantial success-rate and signal-quality shortfall — is exactly the pattern CLAUDE.md rule 4 exists to surface.

## Nulls, negatives, and positives (equal diligence)

**Negative findings for CRAs (the paper's headline):**
- 45.20% vs 68.37% merge-rate gap, CRA-only underperforming human-only by 23.17pp
- 34.88% closure (non-merge) rate for CRA-only vs 21.60% for human-only
- 60.2% of closed CRA-only PRs fall in the lowest (0–30%) signal band
- 92.31% of individual CRA tools average below 60% signal ratio
- A cited secondary finding (Gan et al., 2025, not independently verified by this task) that human comments are addressed far more often (60%) than CRA comments (0.9%–19.2%) — reported by this paper as corroborating context, not as its own primary data

**Positive findings for CRAs (recorded with equal diligence per CLAUDE.md rule 3):**
- Mixed-review categories (any human + CRA combination) all land at 61–68% merge rates — statistically indistinguishable from or only modestly below human-only (67.99% human-dominant is within ~0.4pp of the 68.37% human-only rate) — implying CRA presence *alongside* human review is not obviously harmful and mixed-human-dominant review is essentially as effective as human-only
- Specialised/narrow-scope tools (entelligence-ai, cursor[bot], the n=1 semgrep-getsentry case) show meaningfully higher signal ratios than broad/high-volume tools (GitHub Advanced Security, Copilot), a positive finding for specialised CRA design even though the paper does not frame it as such explicitly
- The paper's own conclusion is not "CRAs are useless" but that they **should complement, not replace, human oversight** — a moderate, non-hype-driven takeaway

**Null/ambiguous:**
- No time-to-merge or cycle-time data reported at all (a direct gap relative to he-2026-2x-mandate's cycle-time finding and relative to what CLAUDE.md's operating loop would want for RQ5/bottleneck cross-referencing)
- No distinction offered between "PR abandoned because CRA feedback was unhelpful" and "PR abandoned for unrelated reasons while a CRA happened to be the only reviewer" — the causal mechanism behind the merge-rate gap is not established, only the association
- Causation explicitly disclaimed by the authors themselves in the validity section

## Limitations / threats to validity (as stated by the authors)

- **Construct validity:** keyword-based signal classification may miss actionable feedback that doesn't use expected keywords, or may mislabel keyword-containing-but-irrelevant comments as signal; mitigated (per the authors) by manual validation from two researchers with discussion of disagreements
- **Conclusion validity:** manual validation itself introduces potential bias; chi-squared association is not causal evidence
- **External validity:** the 3,109-PR sample is drawn entirely from open-source repositories with AI-generated code in AIDev; the authors flag this may not generalise to proprietary/closed-source repositories, non-GitHub platforms, or projects that don't use CRAs at all — though they note the dataset does span a range of project domains, sizes, and maturity levels as a partial mitigating strength

## Cross-reference assessment (for orchestrator review — synthesis/contradictions.md NOT edited)

**1. vs. cloudflare-2026-ai-review (cost-without-effectiveness):** this is a productive complement, not a contradiction, and closes exactly the gap the Cloudflare record flagged. Cloudflare's post reports rich cost/volume/latency telemetry for its own seven-agent review pipeline but explicitly zero outcome data — no catch-rate, no acceptance/dismissal rate, no merge-velocity comparison. This paper supplies precisely that missing outcome layer, albeit for a different population (public AIDev PRs, not Cloudflare's internal GitLab MRs) and different tools (Copilot, GitHub Advanced Security, Cursor bot, etc., not Cloudflare's Opus/Sonnet/Kimi-based OpenCode pipeline). The two cannot be pooled into one organisation's cost-to-value ratio, but together they demonstrate the shape of the evidence gap across this evidence base: **cost data and outcome data for CRAs are being generated by entirely different organisations/methods and have not yet been jointly measured on the same system.** The Cloudflare record's own cross-ref section (written before this extraction) speculated that this paper might "name or characterise company blog posts like [Cloudflare's] as the pattern it studied" — **that speculation does not hold on a full read**: this paper cites only two industry sources (Qodo's survey, Greptile's blog) and does not discuss company engineering blogs as a class or single out Cloudflare-style operational writeups; it is narrower and more quantitative than the Cloudflare record anticipated, testing one specific vendor-survey number against PR-mining data rather than surveying the industry-claims landscape broadly.

**2. vs. unreviewed-ai-prs-2026 (same AIDev dataset family — shared-population caveat applies):** both papers use AIDev but different derived slices (see Dataset provenance above) and answer different questions. unreviewed-ai-prs-2026's headline finding — that the "84% of AI PRs unreviewed" claim dissolves once matched against a human baseline (AI 30.1% vs human 30.8% review participation in the same repos) — is about review *incidence/coverage*, i.e. whether AI PRs get reviewed at all. This paper's finding — CRA-only-reviewed PRs merge at a 23.17pp lower rate and produce mostly low-signal comments — is about review *outcome quality conditional on being reviewed by a CRA*. **These are not competing claims about the same construct** and should not be pooled or treated as replicating one another; both should be read as separate rungs of the same larger claims-vs-reality ladder (coverage claims, then outcome claims), each independently correcting a different piece of industry rhetoric about CRAs. Flagging this distinction matters because a careless synthesis pass could conflate "PRs get reviewed at normal rates" (unreviewed-ai-prs-2026's finding) with "CRA review works as well as human review" (this paper's finding, which is negative) — they do not imply each other.

**3. vs. he-2026-2x-mandate's "automated review overtakes human, ~19%→84%" finding:** He et al. measured *adoption/coverage* shift (automated review becoming the dominant *path*, coverage falling 89%→68% for substantive human review) inside one enterprise's internal pipeline, with cycle time *rising* ~22% despite the shift. This paper measures *outcome quality* of CRA-only review specifically in a cross-organisational open-source sample, finding materially worse merge outcomes and low signal quality when CRAs review alone. **The two studies are consistent with, and mutually reinforcing of, the same underlying worry from different angles**: He et al. shows that as automated review scales up and displaces human coverage, overall cycle time does not improve (bottleneck redistributed, not resolved); this paper shows a plausible *mechanism* for why that might be the case — CRA-only review is measurably less effective at getting PRs to a successful merged state and generates comments that are mostly noise two-thirds of the time. Neither paper directly measures the other's specific numbers (no shared metric), so this is triangulation-by-mechanism, not replication, but it is a coherent joint story worth flagging for the RQ1/tension-6 synthesis: **displacing human review coverage with CRA-only review appears to come with a real quality/outcome cost, not just a coverage-composition change.**

**4. Does the claims-vs-reality gap echo the accumulating citation-hygiene/hype pattern?** Yes, cleanly, and this paper is one of the more direct empirical demonstrations of that pattern found in this project to date — more direct than most because the paper's *explicit stated purpose* is to test a named vendor claim against measured data, rather than incidentally revealing a hype gap as a side effect (contrast with, e.g., Noda's "16%" misquote or the Faros-attributed-to-Agoda mix-up already logged in the ledger, which are citation-chain errors rather than tested claims). The specific pattern: a CRA vendor (Qodo) surveys its own users (a self-selected, already-adopting population) and reports high satisfaction and near-universal human-comment-free operation; independent PR-mining on public data finds CRA-only review success rates over 20 points below human-only and review comments that are mostly noise for the majority of tools. This is structurally identical to the Uplevel-vs-GitHub/Accenture contradiction and the "84% unreviewed" claim already logged elsewhere in this evidence base: **a vendor-adjacent self-report/survey number, taken at face value, does not survive contact with independent measured data.** Worth flagging for RQ2 synthesis as a fifth or sixth instance of this now-recurring shape, and for RQ6 as a caution against trusting vendor-reported CRA adoption/satisfaction metrics as proxies for actual review effectiveness.

## What this can and cannot support

**Can support:** a measured (not self-reported), statistically tested (χ²=83.03, p<0.001) finding that CRA-only PR review is associated with materially worse merge outcomes than human-only review (45.20% vs 68.37%) in a cross-organisational open-source sample of 2,456 AIDev PRs; a measured finding that the majority (92.31%) of individual CRA tools studied produce average comment-signal ratios below 60%, and that most (60.2%) closed CRA-only PRs fall in the lowest signal band; a direct empirical rebuttal, on a related-but-not-identical construct, of a specific vendor claim (Qodo's ~80%/81%/69% figures) about CRA effectiveness; a T7/RQ1 data point that mixed human+CRA review (any composition) outperforms CRA-only review and approaches human-only performance, supporting a "complement, don't replace" framing for internal T7 tooling decisions.

**Cannot support:** any causal claim about *why* CRA-only PRs merge less often (association only, authors' own caveat); any claim about proprietary/enterprise codebases (100% open-source AIDev sample); any time-to-merge, cycle-time, or velocity comparison (not measured in this paper); any claim that Qodo's specific "80% receive no human comments" incidence figure is false (this paper tests outcomes-conditional-on-CRA-only, not incidence-of-CRA-only, and does not report what share of all PRs are CRA-only); any per-tool claim beyond directional signal at very small n for most individual bots (several tools have single-digit or n=1 samples); any generalization to CRA tools not among the 13 identified (e.g. CodeRabbit, Qodo's own product, are not named in the per-tool breakdown obtained in this extraction — worth a follow-up check of the full PDF table for completeness); and no claim this represents a "full research track" MSR paper — it is a Mining Challenge poster, a real but lighter-weight peer-review bar.

## Follow-up leads (not extracted)

- **Qodo (2025) developer survey (609 developers)** — primary source of the "80%"/"81%"/"69%" figures this paper tests. Not yet independently fetched/verified in this evidence base; if used in the exec brief as "the industry claim," should be sourced and COI-flagged directly (Tier D, vendor) rather than only via this paper's secondhand quotation.
- **Greptile company blog (Butler, 2025)**, source of the "82% of developers use CRAs daily/weekly" adoption claim — same treatment, Tier D vendor source, not yet independently checked.
- **Gan et al. (2025)**, cited within this paper for the "human comments addressed 60% vs CRA comments 0.9%–19.2%" figure — a potentially valuable standalone RQ2/RQ7 data point on comment-addressal rates; worth chasing as its own source if comment-actionability becomes a synthesis focus.
- **arXiv 2605.22534, "Why Are Agentic Pull Requests Merged or Rejected? An Empirical Study"** — already queued in LEDGER.md (RQ3, medium priority); surfaced again independently in this task's search as a closely adjacent MSR 2026 paper, worth prioritising given the direct topical overlap with this source's merge/reject outcome data.
- **arXiv 2604.24450, "On the Footprints of Reviewer Bots Feedback on Agentic Pull Requests in OSS GitHub Repositories"** — new lead, not previously in the ledger; surfaced in this task's search results as a closely related bot-feedback study, potentially another AIDev-family or adjacent-dataset source for T7.
- **arXiv 2606.13175, "The End of Code Review: Coding Agents Supersede Human Inspection"** — new lead, not previously in the ledger; title suggests a directly opposing thesis to this paper's "complement, don't replace" conclusion — high-value for the T7/tension-6 contradiction hunt if it turns out to make a stronger claim than He et al.'s adoption-share finding.
- **A dedicated check of the full arXiv PDF (not just the HTML rendering)** for the four unnamed CRA tools in the 13-tool roster and the unspecified n's for codefactor-io, aikido-pr-checks, and semgrep-code-assistant-ws — this extraction's per-tool table has gaps that a direct PDF table read could close.
- **Post-publication reception check (Hacker News, X/Twitter, dev.to)** was not run as part of this task (out of scope per the task's instructions — extraction and cross-ref only); worth a quick check later given the paper's Mining Challenge/poster format may mean less scrutiny than a full research-track paper would attract.

## Recency check notes

Published (arXiv v1) 2026-04-03; MSR 2026 poster session 2026-04-13; verified 2026-07-06, ~3 months old — well inside the CLAUDE.md rule 8 twelve-month threshold, so a full supersession/retraction search was not mandatory, but a targeted search was run regardless given the topic's fast-moving literature (per CLAUDE.md rule 8's spirit). No v2, erratum, or retraction found. No critique or rebuttal piece specifically targeting this paper was found; two closely related MSR-2026-era papers on adjacent topics (arXiv 2604.24450 on reviewer-bot footprints; arXiv 2606.13175 on coding agents "superseding" human inspection) surfaced during the search and are logged above as follow-up leads rather than treated as critiques, since neither was confirmed to directly engage with this paper's findings.
