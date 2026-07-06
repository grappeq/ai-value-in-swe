# stanford-denisov-blanch — Stanford Software Engineering Productivity study (Denisov-Blanch et al.)

**source_id:** stanford-denisov-blanch
**Date verified:** 2026-07-06 (Phase 0 anchor verification)
**RQs fed:** RQ5 (primary), RQ1, RQ3, RQ2; PROTOCOL §5 tension 2 (greenfield vs brownfield)

## Citation(s)

The "source" is a multi-year research programme, not a single paper. Artefacts, most substantive first:

1. **Denisov-Blanch, Y. (2025).** *"Does AI Actually Boost Developer Productivity? (100k Devs Study)."* Conference talk, AI Engineer World's Fair, San Francisco, June 2025. Video: YouTube (via [Class Central listing](https://www.classcentral.com/course/youtube-does-ai-actually-boost-developer-productivity-100k-devs-study-yegor-denisov-blanch-stanford-469765)). **This is the widely-circulated talk the seed refers to and the origin of the greenfield/brownfield quadrant figures.**
2. **Denisov-Blanch, Y. (2025).** *"Can you prove AI ROI in Software Engineering? (120k Devs Study)."* Conference talk, AI Engineer Code Summit, New York, November 2025. Video: [YouTube](https://www.youtube.com/watch?v=JvosMkuNxF8). Latest public wave of the same telemetry.
3. **Denisov-Blanch, Y. (2025).** *"Will AI Replace Software Engineers?"* Slides, The AI Conference, September 2025. [PDF](https://aiconference.com/wp-content/uploads/2025/09/Yegor-Denisov-Blanch-Will-AI-Replace-Software-Engineers_-.pptx.pdf) (image-only PDF; not machine-readable in this session).
4. **Denisov-Blanch, Y., Ciobanu, I., Obstbaum, S., & Kosinski, M. (2024).** *"Predicting Expert Evaluations in Software Code Reviews."* arXiv preprint [arXiv:2409.15152](https://arxiv.org/abs/2409.15152). **The methodology paper** for the measurement model underlying all the talks. Not peer-reviewed.
5. Study programme site: [Stanford Software Engineering Productivity Research (SWEPR)](https://softwareengineeringproductivity.stanford.edu/) — "Since 2022, we've worked with 600+ Organizations", "120K+ Engineers". Researcher site: [yegordb.com](https://www.yegordb.com/).

**Important distinction (per task brief):** the underlying study is ongoing cross-company telemetry (2022–present, now 120k+ developers); the famous figures come from *talks about it*. **No peer-reviewed paper reports the AI-impact effect sizes.** Only the measurement model (item 4) is written up, as a preprint.

## Verification status

**PARTIALLY VERIFIED.** The study, researcher, dataset scale, methodology paper, and talks all verifiably exist, and the quadrant findings are consistently reported across multiple independent secondary write-ups. However: (a) the headline effect sizes exist only in talk/slide form, never in a citable paper; (b) the slides PDF is image-only and could not be read directly, so exact figures below are taken from secondary write-ups of the talks ([marvinzhang.dev](https://www.marvinzhang.dev/blog/ai-productivity), [htek.dev](https://htek.dev/articles/stanford-study-ai-roi-in-engineering), [brgr.one](https://www.brgr.one/blog/ai-roi-software-engineering), [Eichhorst 2026](https://ingoeichhorst.medium.com/state-of-ai-coding-efficiency-2026-1abfa0ab7434)); (c) secondary write-ups disagree on the single headline number (see Key findings). Direct viewing of the talk videos would upgrade this to VERIFIED.

## Tier, era, independence

- **Tier: B.** Large-scale multi-company telemetry (120k+ developers, 600+ organisations, tens of millions of commits) without randomisation — squarely the PROTOCOL §3 Tier B definition. Not A: no counterfactual design, and the substantive findings are unreviewed talk material; the only written methodology is a non-peer-reviewed preprint. Caveat within B: effect sizes are talk-only and should be quoted as ranges with that label attached.
- **Era: mixed E1/E2, with 2025–2026 waves reaching E3.** Telemetry spans 2022–2026. The June 2025 quadrant figures aggregate "AI coding tools" that over that window were predominantly Copilot-class autocomplete and chat assistants (E1/E2); the talks do not split findings by tool modality, so the quadrant numbers **cannot be cleanly tagged E3**. The November 2025 wave, the claimed December 2025 "inflection point", and the July 2026 spin-off paper (arXiv:2607.01904) do cover agentic tooling (E3). Tag the quadrant findings E1/E2-dominant-mixed; tag the 2026 material E3.
- **Independence:** Academic group (Stanford; Kosinski is GSB faculty), no identified tool-vendor funding — **not Tier D**. Flags: (1) participating companies self-select by trading Git repository access for free productivity insights/dashboards ("real-time performance transparency" per the study site) — population skews to organisations of 50+ engineers that want measurement; (2) co-author Obstbaum is a former industry CTO; the offering resembles a commercial DevProd product, though no startup or licensing arrangement was found in this verification pass; (3) the group's earlier "ghost engineers" claim was publicised via X/press before any paper, drawing junk-science criticism — a pattern of findings-by-talk that applies to this source too.

## Method & population/dataset

- **Population:** ~120,000 developers (was >50k in Nov 2024, ~100k in June 2025), 600+ companies, tens of millions of commits, private repositories, since 2022. Cross-industry; participation requires 50+ engineers.
- **Method:** A panel of 10–15 expert engineers rated commits on quality/maintainability/complexity/time; a model was calibrated to reproduce those ratings (reported r = 0.82 for coding time, r = 0.86 for implementation time; ICC2,k 0.78–0.82 across raters — arXiv:2409.15152). The model then scores every commit in participating repos, measuring "functionality delivered over time" rather than commit counts or LOC. AI impact is inferred by comparing output across adoption status and time — **observational, no randomisation**.
- **Measurement basis:** measured (telemetry + model-scored commits) throughout. Not self-report. The talks explicitly contrast this with developers' perception ("developers felt like they were delivering more because volume of code and commits was higher" while much of it was rework) — a perception-vs-measured delta relevant to RQ2/§5 tension 1, though not quantified as a paired estimate the way METR's is.
- **Known methodological critiques (collect for RQ2/RQ6):**
  - Model reportedly trained/calibrated on a small ground-truth set — cited as ~70 Java commits rated by expert panels, 18 engineers ([Jellyfish critique](https://jellyfish.co/blog/ghost-engineers/), of the same model behind the "ghost engineers" claim) — generalisation across languages/domains unproven.
  - Commit-output-only lens: invisible work (mentoring, review, design, incident response) is uncounted; an engineer's value is equated to scored commit deltas ([HN threads](https://news.ycombinator.com/item?id=42284502), [DevOps.com](https://devops.com/code-busters-are-ghost-engineers-haunting-devops-productivity/)).
  - Core analyses unpublished/un-reviewed; effect sizes not accompanied by CIs or model uncertainty in any public artefact.
  - Jellyfish is itself a DevProd analytics vendor — its critique carries its own COI; the HN critiques are independent.

## Key findings (exact as reported; all **measured** unless stated)

All from talk write-ups; treat as ranges, talk-grade. Era tag E1/E2-mixed unless noted.

1. **Greenfield vs brownfield × complexity quadrants** (June 2025 talk; the §5 tension 2 crux; T3 vs T4):
   - Greenfield, low complexity (T3): **+30–40%** productivity gain
   - Greenfield, high complexity (T3): **+10–15%**
   - Brownfield, low complexity (T4/T5): **+15–20%**
   - Brownfield, high complexity (T4): **+0–10%**
2. **Rework/churn** (T4/T5 adjacent; RQ4-relevant): AI initially increases delivered code volume ~**+30–40%**, but "roughly half of gross gains get eaten by rework" (fixing AI-introduced bugs, hallucinated logic, convention mismatches), leaving **net ~15–20%** average gain.
3. **Headline average — inconsistently reported across write-ups (do not average, per rules):** net **15–20%** average ([marvinzhang.dev](https://www.marvinzhang.dev/blog/ai-productivity), of the June 2025 talk); **median ~10%** / "10–15% median lift" ([brgr.one](https://www.brgr.one/blog/ai-roi-software-engineering), [htek.dev](https://htek.dev/articles/stanford-study-ai-roi-in-engineering), of the Nov 2025 talk); **~7–9%** "for Copilot-class assistants" ([getcoai summary](https://getcoai.com/video/does-ai-actually-boost-developer-productivity-100k-devs-study-yegor-denisov-blanch-stanford/)). Plausibly different statistics (mean vs median) from different waves/tool classes, but unresolvable without the primary videos — flagged for contradictions tracking if it survives a watch of the talks.
4. **Language ecosystem split:** high-popularity languages ~**+20%** (low-complexity) / **+10–15%** (high-complexity) tasks; low-popularity languages **minimal or negative** gains.
5. **Codebase size:** gains "drop sharply" as codebase grows from ~10k to ~10M LOC (no exact curve published).
6. **Team variance** (Nov 2025 wave): top-quartile teams **+20–30%**; bottom-quartile **0% or negative**; gap between AI-adopting and non-adopting teams widened **4.8% → 19%** between April 2023 and July 2025 (via [Eichhorst 2026](https://ingoeichhorst.medium.com/state-of-ai-coding-efficiency-2026-1abfa0ab7434)).
7. **Codebase cleanliness moderator** (Nov 2025 wave; RQ3): cleanliness index (tests, docs, modularity, typing) correlates with AI productivity gain at **R² ≈ 0.40**; in high-entropy codebases AI "can actually accelerate technical debt".
8. **Adoption learning curve:** initial slowdown of **~30–100 hours** before gains materialise.
9. **December 2025 "inflection point"** claimed on [yegordb.com](https://www.yegordb.com/) with no public detail found — unextracted lead, likely E3.

## What this can and cannot support

Can support (with Tier B caveats and an era label): the *pattern* that measured AI gains are moderate on average, concentrate in greenfield/low-complexity work, shrink to ~0–10% in complex brownfield work, and are partially offset by rework — the strongest single quantitative anchor for RQ5/§5-tension-2. Cannot support: precise effect sizes (talk-only, no CIs, contested headline number), E3-specific claims from the pre-2025 waves, or any causal reading (self-selected population, no randomisation).

## Corrections vs the seed description (PROTOCOL §6)

- Seed: "gains... shrink toward zero **or negative** in complex legacy systems." As reported, the brownfield/high-complexity quadrant is **0–10% (positive floor at zero)**; *negative* outcomes are reported only for low-popularity languages, bottom-quartile teams, and high-entropy codebases — the seed slightly overstates the headline quadrant. Direction confirmed.
- Seed says "cross-company telemetry" — correct, but note it is **talk-published, not paper-published**; tier grading must reflect that.
- Dataset has grown past the seeded "100k+": now 120k+ developers, 600+ companies (site, 2026).
- The group's newest relevant output is a proper preprint (arXiv:2607.01904, July 2026) — the seed predates it.

## Follow-up leads (not extracted)

- **He, H., Agarwal, S., Denisov-Blanch, Y., Azaletskiy, P., Koyejo, S., Vasilescu, B. (2026). "AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate."** [arXiv:2607.01904](https://arxiv.org/abs/2607.01904), 2 July 2026. Single enterprise, 802 devs, 196,212 PRs, Jan 2024–Apr 2026, staggered diff-in-diff; throughput 2.09x baseline; gains "concentrated in newer code"; automated review surpassed human review. **E3, quasi-experimental — strong candidate for its own extraction (RQ5, §5 tension 6).**
- December 2025 "inflection point" claim — find the artefact behind it (likely a 2026 talk: GitLab Transcend or AI Engineer Code Summit 2026 per yegordb.com).
- [Aviator podcast interview](https://www.aviator.co/podcast/ai-developer-productivity-stanford-study) with Denisov-Blanch — primary-adjacent, may resolve the headline-number discrepancy.
- Denisov-Blanch et al., "Measuring Determinism in LLMs for Software Code Review", [arXiv:2502.20747](https://arxiv.org/abs/2502.20747) — methodology-adjacent (RQ2).
- "Ghost engineers" coverage + [Jellyfish rebuttal](https://jellyfish.co/blog/ghost-engineers/) + [HN thread](https://news.ycombinator.com/item?id=42284502) — RQ2/RQ6 anti-metrics material on the same measurement model.
- yegordb.com lists an ASE 2026 paper: "Repository AI Configuration Is Associated with Three-Fold Differences in Code Quality After Agent Adoption" — E3, RQ3/RQ5 relevant; locate it.
- [Eichhorst, "State of AI Coding Efficiency (2026)"](https://ingoeichhorst.medium.com/state-of-ai-coding-efficiency-2026-1abfa0ab7434) (Apr 2026) — secondary aggregation, useful as a map not a source.

## Recency check notes

Checked 2026-07-06. The June 2025 talk (13 months old) is superseded in scale but not contradicted by the November 2025 wave; both remain the group's canonical public statements of the quadrant findings. No retraction found. The group is actively publishing through July 2026 (arXiv:2607.01904); expect further E3-wave artefacts during Phase 1.
