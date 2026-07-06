# sergeyuk-2026-evolving — JetBrains/UC Irvine two-year IDE telemetry, AI users vs non-users

**source_id:** sergeyuk-2026-evolving
**Date verified:** 2026-07-06
**RQs fed:** RQ2 (primary — perceived vs measured workflow change), RQ1 (secondary — value map, weak proxy metrics only), RQ4 (secondary — deletion/rework signal), RQ6 (secondary — what telemetry can and cannot see)
**Cross-cutting theme:** touches **skill formation & cognitive effects** (PROTOCOL v0.4) only obliquely — see the tagged note under Findings 2 and 6; this is *not* a skill-formation study.

## Citation

Sergeyuk, A., Huang, E., Karaeva, D., Serova, A., Golubev, Y., & Ahmed, I. (2026). *Evolving with AI: A Longitudinal Analysis of Developer Logs.* Accepted to the ICSE 2026 Research Track (12 pages, 5 figures, 1 table).

- arXiv: [2601.10258](https://arxiv.org/abs/2601.10258) — **v1: 15 January 2026; v2: 30 March 2026**. Version read for this record is **v2** (presumed camera-ready; the abstract page does not itemise changes between v1 and v2 — recorded per the PROTOCOL §3 substitution rule, since the ICSE proceedings version was not fetched).
- Categories: cs.SE, cs.HC.
- Affiliations as printed: Sergeyuk and Golubev — JetBrains Research (Belgrade, Serbia); Karaeva — JetBrains (Paphos, Cyprus); Serova — JetBrains (Amsterdam, Netherlands); Huang and Ahmed — University of California, Irvine, USA.

## Verification status

**VERIFIED — full text read** (arXiv HTML v2), not abstract-only. Title, authors, venue acceptance (ICSE'26 Research Track), n=800, and the 62-respondent survey all confirmed against the task brief. Methodology, results, and limitations were extracted across three targeted fetch passes with overlapping questions; the headline slope coefficients were reproduced consistently across two independent passes and are treated as verified. **Numeric caveat:** the paper reports per-group slope coefficients and states a p < 0.05 threshold, but exact p-values were only surfaced for two metrics (debugging non-users p < 0.001; pastes p = 0.03) and confidence intervals were not extractable from the HTML fetches — complete statistical output appears to sit in supplementary material. The group×month interaction terms are described as significant in the fetched text, but the exact interaction statistics were not independently pinned down; do not quote interaction p-values from this record.

## Tier, era, independence

- **Tier: B.** Large-scale longitudinal telemetry (151.9M events, 800 devices, 24 months) without randomisation and without a counterfactual design — squarely the PROTOCOL §3 Tier B description ("large-scale telemetry without randomisation"). Peer-reviewed (ICSE Research Track), which supports the grade; the self-selection design (below) is why it carries claims only with caveats.
- **Era: E1/E2 mixed — pre-agentic.** AI use is defined as any interaction with **JetBrains AI Assistant**, which in the studied window (usage identified April–October 2024) bundled "code completion, AI chat, code generation, and documentation features" — i.e. inline completion (E1) plus in-IDE chat (E2). No agentic modality is involved (the study window closes in October 2024, before JetBrains' agent products), and the logs do not split usage by feature, so the findings **cannot be attributed to completion vs chat** and must be tagged E1/E2-blended. Under the era-transfer rule (PROTOCOL §2), this source supports baselines, measurement-methodology points, and plausibly era-independent effects (the perception–telemetry gap) — not E3 effect-size claims.
- **Independence / COI — FLAGGED.** Four of six authors are JetBrains or JetBrains Research employees; the telemetry is JetBrains' own product telemetry; the AI tool studied is JetBrains' own AI Assistant; the survey panel is JetBrains' internal research panel. This is vendor research about the vendor's own product, published through peer review. Mitigating: the findings are not promotional — the headline pattern (more code produced *and* more code deleted; workflow restructuring users do not perceive) is at best neutral for the product, and the paper openly reports the self-selection confound. The university co-authorship (UC Irvine) adds some independence at the analysis level but the data pipeline is entirely vendor-controlled and unauditable. Treat as Tier B **with a vendor-data COI flag**; do not let it carry a claim jointly with other JetBrains-sourced material as if independent.

## Method & population

- **Design:** Retrospective longitudinal cohort comparison on IDE telemetry. **24-month window, October 2022 – October 2024** (trend analysis over October 2022 – September 2024), aggregated **monthly per device**; 151,904,543 logged events across four JetBrains IDEs (IntelliJ IDEA, PyCharm, PhpStorm, WebStorm). Months with no instances of an action were filled with 0.
- **Groups (n = 800 devices, 400/400):**
  - **AI users:** devices that "consistently interacted with JetBrains AI Assistant … at least once per month, from April 2024 to October 2024."
  - **AI non-users:** devices that "never interacted with JetBrains AI Assistant during the studied two years."
  - Both groups required IDE activity in both October 2022 and October 2024 (survivorship filter).
- **Population verdict (task brief asked for this explicitly):** the unit is the **device, not a verified person** — "800 developers" is really 800 anonymised devices. They are JetBrains IDE users drawn from the general (opted-in) telemetry population; professional status is *presumed from the product context, not verified* for the telemetry sample. The **survey** sample (n = 62, from 67 completions after excluding 5 non-AI-users; 1,231 invitations, 76 clicks) *is* verifiably professional and skews senior: 22 respondents with 16+ years' experience, 14 with 11–15, 17 with 6–10, 8 with 3–5, 1 with 1–2; roles (multi-select) 56 developers, 16 team leads, 10 architects, 10 DevOps. Recruited from a JetBrains-maintained consented research panel. Five follow-up semi-structured interviews (30 min).
- **Metrics (proxy operationalisations — all five are single-event-count proxies):** productivity = typed characters in the editor; code quality = debugging instances (debug hotkey/contextual actions); code editing = deletions (delete keystrokes, backspaces, undos, etc.); code reuse = external pastes (pastes not preceded by an in-IDE copy); context switching = IDE window activations (switches from another window back to the IDE).
- **Analysis:** mixed linear model per metric, `count_action ~ group × n_month + (1|id_device)` (random intercept per device), p < 0.05 threshold. Normality rejected (Kolmogorov–Smirnov); variance homogeneity rejected (Bartlett). No matching, no difference-in-differences.
- **Design caveat that governs interpretation of every "trajectory" below:** AI-user status is defined by usage in the **final seven months** (April–October 2024), but the slopes are estimated over the **full 24 months** — most of which predates the identified AI usage (and JetBrains AI Assistant's general availability, late 2023). The reported "trends" are therefore **between-group slope differences among self-selected cohorts**, not a within-person before/after adoption time-course. The paper's own internal-validity section concedes this (see Limitations).

## Key findings

All telemetry findings are **measured**; all survey findings are **self-reported**. One record per finding, per §4.

### 1. Productivity proxy (typed characters) — measured
- AI users: **+587 characters/month** trend (significant); non-users: **+75 characters/month** (significant) — a **~7.8× steeper** rise for AI users. Both groups trend upward over the whole 24 months.
- **Trajectory shape as the paper gives it:** monotone linear upward for both groups, AI users steeper throughout. No dip, plateau, or novelty-decay shape is reported — but note the model is linear in month, so **non-linear shapes could not have been detected**; "flat-vs-rising" is the finest resolution this design offers.
- **Construct caveat:** "typed characters" is a keystroke proxy; the paper does not resolve whether accepted AI completions count as typed characters, and more characters is not more value delivered. Grade this as an *activity* finding, not a productivity finding, for RQ1 purposes.

### 2. Code quality proxy (debugging instances) — measured; contains the study's clearest null
- AI users: **no statistically significant trend** over the two years (record as **null** per CLAUDE.md rule 3). Non-users: **−0.46 debugging instances/month, p < 0.001** — a significant decline.
- So the *divergence* is driven by non-users debugging progressively less while AI users' debugging held flat. The paper does not establish why non-users' debugging declined.
- **Skill-formation tag (weak, mechanism-adjacent only):** flat debugging alongside sharply rising output among AI users is *consistent with* effort shifting from authoring to verifying/revising AI output — the authors note the pattern "echo[es] earlier findings that developers often spend substantial time verifying and revising AI outputs" — but the study measures no comprehension or skill outcome, so this supports nothing beyond a mechanism hypothesis.

### 3. Code editing (deletions) — measured
- AI users: **+102 deletions/month** (significant); non-users: **+7.6 deletions/month** (significant) — **~13.4× steeper** for AI users. Both linear upward, AI users elevated throughout.
- Authors' interpretation: "Developers produce more but also discard more, possibly due to iterative refinement of sometimes inefficient AI-generated suggestions."
- **RQ4 relevance:** this is a within-IDE analogue of the churn/rework cost signal — produced-then-deleted work is cost, not output. Directional only; no time or money quantification.

### 4. Code reuse (external pastes) — measured
- AI users: **+1 paste/month** (significant, **p = 0.03**); non-users: **+0.4 pastes/month** (significant) — ~2.5× steeper for AI users. Both linear upward. Small absolute magnitudes.

### 5. Context switching (IDE window activations) — measured; the one bi-directional divergence
- AI users: **+6.4 activations/month** (significant, rising); non-users: **−7.6 activations/month** (significant, falling). The only metric where the two groups move in **opposite directions** over the window: AI users switch into/out of the IDE more and more over time; non-users progressively less.
- Plausibly reflects chat-panel/browser round-trips, but the telemetry cannot see what the switched-to window was — mechanism unidentified.

### 6. Perceived vs measured — the survey side (self-reported; the delta is itself a finding, per CLAUDE.md rule 4)
- **Productivity:** 82.3% report productivity increased slightly/significantly; 56.5% report coding time decreased; only 2 respondents report any decrease.
- **Quality:** 48.4% perceive quality up, 9.7% down; readability 43.5% up, 6.5% down, 50% no change. (Telemetry counterpart: AI users' debugging flat — neither confirms nor refutes.)
- **Editing:** 50% perceive **no change** in editing frequency (43.5% up) — against a measured 13.4× slope difference in deletions.
- **Reuse:** 43.5% perceive no change (37.1% up, 19.4% down) — against a measured 2.5× slope difference.
- **Context switching:** 53.2% perceive no change (25.8% up, 21.0% down) — against measured opposite-direction trends.
- Authors' framing: "telemetry shows what developers do, surveys show what developers recognize"; the results "reveal structural changes in workflow that are not always visible to users themselves"; "AI-assisted workflows appear to reconfigure where effort occurs, rather than how much effort is perceived" — the abstract's phrase is the "**silent restructuring of software workflows**."
- **Caveat on the comparison itself:** the survey sample (62 senior-skewed panel members) is *not* the telemetry sample (800 anonymised devices), and the survey administration date is not stated in the paper. The perceived-vs-measured contrast is between two different populations measured differently — weaker than a within-subject perception–reality delta (METR-style). Grade the gap as **suggestive, not measured on the same people**.
- **Skill-formation tag (metacognitive angle):** the specific pattern — developers clearly perceive the *headline* benefit (productivity) but mostly fail to perceive the *behavioural* changes (editing, switching) that telemetry shows — is evidence that self-perception has poor resolution for workflow-level change. Feeds RQ6 (don't instrument by asking) and, weakly, the cognitive-effects theme (limited self-awareness of AI-induced behaviour change).

### 7. Baseline group difference — measured, descriptive
- "AI users are generally more active in the IDE than AI non-users … for most actions, AI users do more of them." The paper treats this descriptively and concedes it reflects self-selection. Any reading of the slope differences as *caused by* AI adoption is confounded by whatever makes active developers adopt AI.

### Heterogeneity
- None reported in the telemetry: no splits by seniority, language, IDE, codebase, or task type — device-level anonymisation precludes them. Survey seniority distribution is reported but Likert results are not broken down by seniority. **Task-type resolution: none** — all findings are whole-workflow IDE activity; no T1–T11 tag fits, and per CLAUDE.md this is recorded as-is rather than stretched into a category (general implementation activity spanning tasks; no taxonomy change proposed since the source makes no task claims at all).

## Authors' stated limitations (threats to validity, near-verbatim)

- **Construct:** single commercial IDE provider; AI usage defined solely by integration with the proprietary JetBrains AI Assistant — "developers using other AI tools or AI tools outside the IDE may be misclassified as non-users, potentially underestimating true adoption" (this plausibly *dilutes* the group contrast: the "non-user" arm likely contains ChatGPT/Claude-in-browser users, an era-relevant contamination given E2 workflows are copy-paste workflows). Telemetry "does not capture developer intent or task context"; surveys capture "holistic, retrospective perception but not actual behavior."
- **Internal:** AI users "likely differ not only in AI usage but also in baseline motivation, experience, or task profiles"; "cross-group differences reflect both AI adoption and unmeasured characteristics that predict adoption." Self-selection, openly conceded.
- **External:** "Findings may not generalize to all development environments or interface paradigms" beyond JetBrains IDEs.

## What this can and cannot support

**Can support (Tier B, E1/E2, COI-flagged):** that over 2022–2024, developers who adopted an in-IDE completion+chat assistant show measurably steeper growth in code output *and* code deletion, rising context switching against a declining non-user baseline, and flat debugging activity; and that developers' self-reports register the perceived productivity gain while largely missing these behavioural shifts. Strongest use: **RQ2/RQ6 methodology evidence** — single-proxy telemetry and retrospective self-report see different things, and self-report has poor resolution below the headline; plus a **directional RQ4 rework signal** (produce-more-discard-more).

**Cannot support:** any causal effect of AI adoption (self-selected cohorts, no counterfactual, baseline activity differences); any E3/agentic claim (pre-agentic modalities only); any productivity *value* claim (typed characters is an activity proxy); any within-person adoption trajectory ("how effects evolve over months of sustained use" — the design compares group slopes over a window that mostly *predates* the identified AI usage, and the linear model cannot express non-linear time-courses); any task-type or seniority split (none measured); a clean perception–reality delta (survey and telemetry populations differ).

## Cross-reference assessment (report only)

- **PROTOCOL §5 tension 1 (perception–reality gap):** consistent in spirit but weaker in kind — this is perceived-change-vs-measured-change across *different samples*, not METR's within-subject speed miscalibration. Adds the useful nuance that the blind spot here is about *workflow shape* (editing, switching), while the headline perception (productivity up) is at least directionally aligned with the activity telemetry. Does not, on its own, warrant a contradictions.md entry.
- **PROTOCOL §5 tension 4 (quality-debt signals):** the deletions finding (13.4× steeper growth for AI users) is an independent, non-GitClear, in-IDE convergence point for the rising-churn pattern — different instrument (keystrokes vs repo diffs), different vendor, same direction. Flag for the tension-4 evidence assembly in Phase 3.
- **PROTOCOL §5 tension 6 (bottleneck displacement):** flat debugging + rising output + rising context switching among AI users is weakly consistent with effort displacement from authoring to verification/orchestration, but the telemetry cannot identify what the switched-to activity was. Mechanism-hypothesis grade only.

## Follow-up leads (not extracted)

1. Supplementary material / replication package for the exact mixed-model tables (interaction coefficients, CIs) — needed before any slope number is quoted with an interaction p-value.
2. The ICSE'26 proceedings version, to confirm v2 = camera-ready and check for post-review changes.
3. Prior Sergeyuk et al. JetBrains work (in-IDE AI survey research) — same group, useful for triangulating the survey instrument but **not independent** of this source for COI purposes.
4. Any independent (non-JetBrains) IDE-telemetry longitudinal study with the same design shape — would break the single-vendor dependency of this evidence line.

## Recency check notes

Paper is ~4–6 months old at verification (Jan/Mar 2026 → Jul 2026) — inside the 12-month threshold, so no mandatory recency search; ICSE'26 acceptance is stated on the arXiv page and v2 (30 Mar 2026) is the latest version. No retraction or superseding follow-up encountered during the fetch passes. Treat as current.
