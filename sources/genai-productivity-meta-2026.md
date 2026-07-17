# Source record: genai-productivity-meta-2026

## Identity (verified against full text, not abstract)

- **Title:** "A meta-analysis of the effect of generative AI on productivity and learning in programming"
- **Authors:** Sebastian Maier¹,², Moritz Gunzenhäuser¹ (joint first authors), Jonas Schweisthal¹,², Manuel Schneider¹, Stefan Feuerriegel¹,² (corresponding)
- **Affiliation:** ¹LMU Munich, ²Munich Center for Machine Learning (MCML)
- **arXiv ID:** 2605.04779v1 [cs.SE], submitted 6 May 2026
- **Venue/status:** arXiv preprint only. Pre-registered 4 Dec 2025 via PRISMA-P on OSF (https://osf.io/5h2s3). No evidence in the text of journal/conference acceptance — treat as preprint, not peer-reviewed-published, though the meta-analysis *of* peer-reviewed and preprint primary studies is itself methodologically rigorous (PRISMA 2020, RoB2/ROBINS-I, pre-registration).
- **Funding:** Swiss National Science Foundation (SNSF) grants 197485, 186932 (Feuerriegel). No industry/vendor funding declared.
- **COI:** "The authors declare no competing interests." No vendor/consultancy affiliation. **Not a Tier D source** — independent academic team.
- **Data/code:** publicly available (GitHub: SM2982/MetaanalysisGenAICoding).

## What this is

A systematic meta-analysis (not a single study) pooling **n = 23 studies / k = 27 effect sizes** on GenAI-assisted programming, split into two independent random-effects models:
- **RQ1 (their numbering) — Productivity:** k = 16 effect sizes from n = 14 studies (m = 3,535 participants + r = 6,355 repositories)
- **RQ2 (their numbering) — Learning:** k = 11 effect sizes from n = 10 studies (m = 1,069 participants)
(1 study contributed to both outcomes, hence 23 not 24 unique studies)

Search: ACM, arXiv, Scopus, Web of Science, Jan 2019–Dec 2025, plus backward/forward citation search. 10,115 + 71 = 10,186 records screened down to 23 included studies — a highly selective, well-documented PRISMA pipeline (flowchart reproduced in Fig. 9 of the paper). Effect sizes standardised as Hedges' g via multiple documented conversion formulas (Online Supplement D), random-effects REML pooling, formal risk-of-bias grading per study (RoB2 for randomised designs, ROBINS-I for non-randomised), Egger's test + trim-and-fill for publication bias, leave-one-out and three-level (effect-size-nested-in-study) sensitivity checks.

**Deliberate methodological choice relevant to RQ2 (measurement):** the authors excluded studies relying on *subjective/self-reported* productivity measures by design — "we... deliberately [decided] to exclude studies relying on subjective productivity measures, which capture a fundamentally different construct." **Every effect size in this meta-analysis is `measured`, not `self-reported`.** This means the paper cannot itself speak to the perceived-vs-measured gap (METR tension), but it does mean its numbers are not inflated by self-report bias.

## Grading (PROTOCOL §3)

**Tier: A**, with a load-bearing caveat. Justification: pre-registered, PRISMA-compliant systematic review; formal dual-rater risk-of-bias assessment per included study; random-effects pooling with REML; multiple robustness checks (leave-one-out, influence diagnostics, three-level modelling, publication-bias tests); fully open data/code; no vendor funding or COI. This is the most methodologically rigorous single document in the evidence base to date on this specific question.

**The caveat, and it is severe: I² = 99% for the productivity pooled estimate.** Heterogeneity this extreme means the single pooled number (g = 0.33) is not a meaningfully "typical" effect — it is an average across studies that do not measure comparable things. The paper's own study-setting moderator confirms this (lab g = 0.73 vs open-source g = 0.01, both far from the pooled mean). **Treat the headline g = 0.33 as a description of the evidence base's central tendency, not as a usable point estimate for any specific deployment context.** This is consistent with, and reinforces, PROTOCOL §5 tension 2 (greenfield/lab vs brownfield/real-world split).

## CRITICAL FINDING: era composition of the pooled evidence (the task's core question)

The paper does **not** moderate by tool generation (autocomplete/chat/agentic). Its only tool-related moderator is "GenAI interface: GitHub Copilot vs Other" (non-significant, QM(1)=0.21, p=0.644) — a binary that conflates autocomplete-era Copilot-classic with agentic-era Cursor and various bespoke chat tools all inside "Other." **This is exactly the risk flagged in this task's brief, and it is realised in the paper.**

I hand-classified each of the 16 productivity and 11 learning effect sizes by tool modality actually studied, per PROTOCOL §2's era-assignment rule (tag by modality studied, not publication year), using Table 1/Table 2 and Appendix E (moderator definitions/tool list) of the source:

**Productivity (16 effect sizes / 14 studies):**
| Era | Count | Studies |
|---|---|---|
| E1 (autocomplete: Copilot, Codex, NL2Code) | 10 | P001_R001, P001_R002 (Yeverechyahu, Copilot), P002 (Weber, Copilot), P004 (Kazemitabaar, Codex), P006 (Shihab, Copilot), P009 (Xu, Copilot/GPT-3), P010_R001, P010_R002 (Cui, Copilot/GPT-3), P011 (Xu 2022, NL2Code), P014 (Peng 2023, Copilot — the original anchor RCT) |
| E2 (chat-based: custom GPT-3.5/GPT-4o interfaces) | 2 | P005 (Nam, "GILT" on GPT-3.5-turbo), P007 (Piscitelli, "ClueBot" on GPT-4o) |
| E3 (agentic: Cursor) | 2 | **P008 (Becker/Rush/Barnes/Rein 2025, Cursor+Claude Sonnet — this is the METR "early-2025 AI" RCT, see cross-ref below), P012 (He et al. 2025, Cursor, diff-in-differences on real software projects)** |
| Ambiguous / tool unspecified | 2 | P003 (Paradis et al., tool not named in table — "–"), P013 (Gambacorta et al./BIS, "CodeFuse", an internal Ant Group assistant of unclear modality) |

**→ Only 2 of 16 productivity effect sizes (12.5%) are E3-era. Even the 2 ambiguous ones are unlikely to be agentic given their 2024 vintage and internal-tool framing — realistic E3 share is 12.5%, ceiling 25%.**

**Learning (11 effect sizes / 10 studies):**
| Era | Count |
|---|---|
| E1 (Codex) | 1 (L008, Kazemitabaar — same underlying study as P004) |
| E2 (ChatGPT / GPT-based tutoring) | 10 (L001–L007, L009, L010) |
| E3 (agentic) | **0** |

**→ Zero agentic-era evidence in the learning pool. The learning null result (g = 0.14, ns) is entirely an E1/E2-era finding and cannot be used, per PROTOCOL §2 era-transfer rule, to say anything about agentic-tool effects on skill formation — it can only serve as a pre-agentic baseline for the skill-formation cross-cutting theme.**

**Implication for RQ1/RQ5:** the pooled g = 0.33 productivity headline is overwhelmingly (87.5%) an E1/E2-era number. Per PROTOCOL §2's era-transfer rule, **this pooled estimate cannot itself support any E3/agentic-era claim in the exec brief.** It is admissible only as (a) a pre-agentic historical baseline, or (b) evidence for the era-independent "lab inflates effects" mechanism (see below), which does appear robust across both pre-agentic and the two agentic entries.

## Cross-reference: this meta-analysis independently includes the METR RCT

**P008 (Becker, Rush, Barnes, Rein, "Measuring the impact of early-2025 AI on experienced open-source developer productivity," arXiv:2507.09089v2) is the METR study already anchored in this project's PROTOCOL §5/§6 (the "≈19% slower" RCT).** In this meta-analysis's forest plot (Fig. 3) it is the sole effect size rendered in red/negative territory, with the lowest (most negative) point estimate of all 16 productivity effect sizes, sitting in the "open-source" and "Cursor/Sonnet" subgroup — the same subgroup (open-source, g = 0.01 pooled, ns) that drags the setting-moderator result toward zero. **This is independent corroboration, via a third party's re-extraction and re-standardisation of the same primary data, that the METR finding is a real negative/null outlier, not an artefact of that paper's own analysis choices.** This should be logged as a confirming (not contradicting) cross-reference in `synthesis/contradictions.md` if a METR source record already exists — it strengthens rather than weakens the METR result.

## Extracted findings (one record per finding, PROTOCOL §4)

### Finding 1 — Pooled productivity effect (headline, mixed-era)
Hedges' g = 0.33, 95% CI [0.09, 0.58], SE = 0.13, p = 0.008, k = 16 effect sizes / n = 14 studies, random-effects REML. Heterogeneity I² = 99%, τ² = 0.22, Q(15) = 206.06, p < 0.001.
**Can support:** a description of the pre-2026 literature's central tendency for objectively-measured productivity effects, era-mixed and dominated by E1/E2.
**Cannot support:** any specific claim about agentic-tool productivity effects, or about "typical" gains in any one context, given I²=99% and 87.5% E1/E2 composition.

### Finding 2 — Pooled learning effect (headline, non-agentic evidence base)
Hedges' g = 0.14, 95% CI [−0.18, 0.47], SE = 0.17, p = 0.389 (non-significant — CI spans zero). k = 11 / n = 10. I² = 86%, τ² = 0.25, Q(10) = 54.96, p < 0.001.
**Can support:** a null/no-reliable-effect finding for GenAI on learning outcomes, E1/E2-era only.
**Cannot support:** any claim about agentic-tool effects on skill formation (zero E3 studies in this pool); cannot be used as evidence either for or against "cognitive debt" in the agentic era.

### Finding 3 — Study-setting moderator dominates productivity heterogeneity, but is confounded with era
QM(2) = 10.51, p = 0.005, explains ~36% of between-study heterogeneity. Laboratory g = 0.73 (p<0.001, k=7, **all 7 lab studies are E1/E2** — no agentic study was conducted in a lab setting in this pool); Enterprise g = 0.19 (p=0.448, ns, k=4); Open-source g = 0.01 (p=0.975, ns, k=5, **contains both E3 studies**).
**Can support:** the greenfield/lab-vs-real-world split (PROTOCOL §5 tension 2) — lab settings inflate measured effects relative to real-world/open-source settings, and this holds even including the agentic-era entries.
**Cannot support:** a clean "era effect" separate from "setting effect" — the two are confounded in this dataset (no lab-based agentic study exists to disentangle them). Flag as a genuine methodological gap, not resolved by this paper.

### Finding 4 — No tool-era moderator was tested; only a coarse "Copilot vs Other" split was, and it was null
QM(1) = 0.21, p = 0.644 for "GenAI interface: GitHub Copilot vs Other." This is the paper's only technology-modality moderator, and it collapses autocomplete, chat, and agentic tools into "Other."
**Can support:** the meta-methodological finding that the existing literature has not yet been analysed with an autocomplete/chat/agentic split — this is a genuine, citable gap.
**Cannot support:** any inference that tool generation doesn't matter — the test as constructed could not detect an era effect (E3 n=2, folded into "Other" alongside E2 studies).

### Finding 5 — Exam-environment moderator for learning: tool-dependent performance vs durable learning
QM(1) = 7.23, p = 0.007, explains 45.49% of learning heterogeneity. When GenAI was **disallowed** during the assessment: g = −0.06, 95% CI [−0.36, 0.24], p = 0.674 (null, slightly negative point estimate). When GenAI was **allowed** during the assessment: g = 0.76, 95% CI [0.24, 1.28], p = 0.004 (large, significant).
**Can support:** a clean, well-powered demonstration that "AI improves test scores" and "AI improves durable skill acquisition" are different claims — apparent learning gains evaporate once the tool is removed. Directly feeds the skill-formation/cognitive-debt cross-cutting theme (PROTOCOL §2) and RQ4/RQ6.
**Cannot support:** any claim about which specific cognitive mechanism (offloading, reduced practice, etc.) causes the gap — the paper is agnostic on mechanism, citing it as consistent with cognitive-offloading literature.

### Finding 6 — Risk of bias is not a significant moderator, but higher-risk studies descriptively report larger effects
Productivity: QM=2.90, p=0.089; lower-risk g=0.08 [−0.29, 0.45] (k=6) vs higher-risk g=0.50 [0.19, 0.80] (k=10). Learning: QM=1.15, p=0.284; lower-risk g=−0.043 (k=5) vs higher-risk g=0.319 (k=6). 59.3% of all effect sizes across both outcomes were rated higher-risk (high/critical under RoB2/ROBINS-I); 40.7% lower-risk.
**Can support:** a directional (non-significant but consistent across both outcomes) signal that methodologically weaker studies in this literature skew toward larger reported effects — a caution for weighting practitioner/Tier C claims that lack rigorous design.
**Cannot support:** a firm statistical claim of bias-driven inflation (p>0.05 in both cases; underpowered with k=16/11).

### Finding 7 — Publication bias assessment: mixed picture, resolved in favour of "true heterogeneity" not suppression
Productivity: Egger's test z=4.52, p<0.001 (significant funnel asymmetry) but trim-and-fill imputed **zero** missing studies. Learning: Egger's z=0.55, p=0.585 (no asymmetry); trim-and-fill also zero missing studies.
**Can support:** the authors' interpretation that funnel asymmetry in the productivity set reflects genuine study-to-study heterogeneity (consistent with Finding 3/4) rather than selective non-publication of null results — i.e., no strong evidence the literature is hiding negative agentic-tool findings.
**Cannot support:** full confidence — trim-and-fill is known to under-detect bias under high heterogeneity (I²=99%), so this null finding should be read cautiously, not as a clean bill of health.

### Finding 8 — Cumulative (temporal) meta-analysis: no capability-driven trend in reported productivity gains
Cumulative pooled g stabilises at 0.331 as studies are added chronologically 2022→2025, despite substantial underlying model-capability improvements over that window (Fig. 5). Authors: "raw model capability or AI literacy may not be the primary drivers of productivity gains."
**Can support:** a genuinely interesting null/negative-in-spirit finding — the trendline does NOT show accelerating productivity gains matching public model-capability improvements through 2025.
**Cannot support:** any claim about the agentic-era trajectory specifically, because the chronological series is dominated by E1/E2 entries throughout its length and only picks up its 2 E3 entries at the very end (2025), where the cumulative estimate is already heavily anchored by 14 prior E1/E2 points — the series has essentially no power to detect an agentic-era discontinuity even if one existed in the underlying (unpooled) data.

### Finding 9 — Three-level model confirms pooled estimates are robust to effect-size non-independence
Accounting for effect sizes nested within studies (some studies contribute >1 effect size): productivity g=0.38, SE=0.15, 95% CI [0.09, 0.67], p=0.010 (σ²_between=0.266, σ²_within=0.000); learning g=0.19, SE=0.18, 95% CI [−0.154, 0.54], p=0.275 (σ²_between=0.261, σ²_within=0.000).
**Can support:** confirmation that the simpler random-effects model's conclusions (significant productivity effect, non-significant learning effect) are not an artefact of pseudo-replication from studies contributing multiple effect sizes.
**Cannot support:** anything beyond that — same era-composition caveats as Findings 1–2 apply, since this is the same underlying data.

### Finding 10 — Methodological note: this is an entirely "measured" (not self-reported) evidence base by design
Productivity operationalised only as task completion time, commits, or LOC (never survey/perception items); studies "relying on subjective productivity measures" were excluded by protocol.
**Can support:** a clean, uncontaminated-by-self-report set of productivity numbers for triangulation with survey-based practitioner sources.
**Cannot support:** any statement about the *size of the perception-reality gap* (METR tension, PROTOCOL §5.1) — this paper structurally cannot speak to that gap since it excludes the self-report side of the comparison entirely.

## Red flags / limitations (author-acknowledged and independently noted)

1. **I²=99%/86%** heterogeneity on both outcomes — headline numbers are not "typical effects," they are averages of incommensurable study designs (author-acknowledged, and PROTOCOL-relevant).
2. **Actual GenAI use/adherence not controlled for** in most included studies — designs capture treatment *assignment*, not confirmed usage intensity (author-acknowledged limitation).
3. **First author did initial screening alone** ("Screening and eligibility assessment were conducted by the first author") for the primary database search, though risk-of-bias rating used two independent raters — a single-screener design is a minor internal-validity concern for a PRISMA review, though citation-search eligibility appears to have been checked more broadly.
4. **Task-type moderator was dropped entirely**: "coding task type was excluded as no meaningful categorisation across studies was feasible" (Table 6 footnote) — meaning this meta-analysis, unlike this project's PROTOCOL taxonomy, provides **no T1–T11 task-type breakdown at all**. Every row in the proposed evidence table below is necessarily tagged with a broad/unspecific task_types field for this reason — a real gap relative to what RQ1 needs.
5. Small subgroup cell sizes throughout (moderator subgroups k=3–11) — the authors flag several non-significant moderator results as likely underpowered rather than true nulls.
6. The paper's own "Recommendations for future research" section explicitly names the agentic-era gap: "future research should investigate... systematic comparisons across different GenAI technologies, including reasoning-capable GenAI, agentic systems... to better understand how GenAI capabilities and usage patterns influence productivity" — the authors know their pool is pre-agentic-dominated and say so, though not with the specific 12.5%/0% quantification this extraction provides.

## Surprises

- The paper is a genuinely rare specimen for this evidence base: a rigorous, pre-registered, independently-funded, PRISMA-compliant meta-analysis directly on-topic — closer to the "Tier A anchor" the protocol hoped existed than most sources found so far.
- It independently re-derives and re-confirms the METR RCT (P008) as a real negative outlier via third-party standardisation — useful triangulation rather than a new claim.
- Its central "lab inflates effects" finding (g=0.73 lab vs g≈0 real-world) directly and quantitatively substantiates PROTOCOL §5 tension 2, using a mostly-independent set of primary studies from the ones likely already in this project's evidence table.
- Despite covering literature through Dec 2025 and being submitted in May 2026, its agentic-era coverage is almost nil (2/16 productivity, 0/11 learning) — strong evidence that **the scarcity clause in PROTOCOL §8 is not a research-effort artefact of this project but a real feature of the published literature itself**, corroborated by an independent team's systematic search across four databases.

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
genai-productivity-meta-2026	2026	A	MIXED (E1=10/16, E2=2/16, E3=2/16, unclear=2/16; see era-composition table)	meta-analysis (random-effects REML) of 14 primary studies (RCT n=10, natural experiment n=2, quasi-experiment n=2)	m=3,535 participants + r=6,355 repositories across 14 studies, mixed experience levels (experienced k=9, students k=4, mixed k=3 effect sizes)	unspecified/not codeable by authors (task-type moderator explicitly dropped as "no meaningful categorisation... feasible") — likely spans T3/T4/T5/T9	Hedges' g pooled across task completion time / commit counts / LOC	g=0.33, 95% CI [0.09,0.58], SE=0.13, p=0.008, I²=99%, τ²=0.22	positive, moderate, significant	measured (self-report explicitly excluded by design)	none reported	not analysed as moderator (excluded — insufficient variability)	lab (k=7) / enterprise (k=4) / open-source (k=5)	independent academic (LMU Munich/MCML), SNSF-funded, no vendor COI declared	I²=99% renders pooled point estimate not usable as a single dial; 87.5% of underlying effect sizes are E1/E2-era; setting moderator (QM(2)=10.51,p=0.005) explains only ~36% of heterogeneity, rest unexplained	4
genai-productivity-meta-2026	2026	A	E1/E2 only (0/11 E3)	meta-analysis (random-effects REML) of 10 primary studies (experimental n=4, quasi-experimental n=6)	m=1,069 students, university (k=6 studies) + high school/middle school/K-12 (k=4)	education/learning outcomes, not mapped to T1-T11 (out of SDLC scope but feeds skill-formation cross-cutting theme)	Hedges' g pooled across final-exam performance	g=0.14, 95% CI [-0.18,0.47], SE=0.17, p=0.389 (non-significant), I²=86%, τ²=0.25	null (CI spans zero)	measured (exam scores; self-report excluded by design)	none reported	not analysed as moderator	university (k=6) vs pre-university (k=4); course-integrated (n=8) vs lab (n=2)	independent academic, SNSF-funded, no COI	Zero E3 evidence in this subset — cannot inform agentic-era skill-formation claims at all, only pre-agentic baseline	3
genai-productivity-meta-2026	2026	A	E1/E2 only (all 7 lab-setting studies predate/exclude agentic tools)	moderator subgroup of above meta-analysis (mixed-effects meta-regression, REML)	subset of the k=16 productivity pool, laboratory-setting studies only	unspecified, controlled/standardised lab tasks	Hedges' g, laboratory subgroup	g=0.73, p<0.001, k=7 (setting moderator overall QM(2)=10.51, p=0.005, R²≈36%)	positive, large, significant	measured	none reported	not analysed	laboratory (controlled, short, standardised tasks)	independent academic	Confounded with era: no agentic-era study in this pool used a lab design, so "lab effect" and "pre-agentic effect" cannot be separated here	4
genai-productivity-meta-2026	2026	A	E1 (2/5) + E3 (2/5) + E1 (1/5, ambiguous) mixed within this single subgroup	moderator subgroup of above meta-analysis	subset of k=16 productivity pool, open-source-setting studies only, includes the METR RCT (P008) and He et al. Cursor diff-in-diff (P012)	real open-source repositories/commits	Hedges' g, open-source subgroup	g=0.01, p=0.975, k=5 (non-significant, effectively null)	null	measured (commits/time; includes METR's objective task-completion-time RCT)	none reported	not analysed	real open-source codebases, both autocomplete-era (Copilot) and agentic-era (Cursor) tools represented	independent academic; this subgroup includes the METR RCT, itself independently funded (non-profit AI safety org)	Cross-references and corroborates METR's own ~-19% finding via independent re-standardisation; this is the ONLY subgroup mixing E1 and E3 tools and it is the one closest to zero — suggestive that real-world/open-source settings erase the productivity gain regardless of tool generation, though k=5 is small	5
genai-productivity-meta-2026	2026	A	E3 (single study, embedded in meta-analysis)	RCT (individually randomized parallel-group; embedded primary study within the meta-analysis, Becker/Rush/Barnes/Rein 2025 = the project's existing METR anchor)	experienced open-source developers	unspecified brownfield open-source maintenance tasks	% change in task completion time	single effect size, visually the most negative/lowest point estimate in the entire 16-study forest plot (Fig. 3); exact g not stated numerically in main text beyond forest-plot position	negative (slower with AI)	measured	none reported	experienced only	real open-source repositories, agentic tool (Cursor + Claude Sonnet)	independent (METR is a non-profit AI safety evaluations org; re-extracted here by an unrelated third-party academic team)	This is the METR "-19%" RCT already anchored in PROTOCOL §5/§6, now independently corroborated via a separate team's re-standardisation into Hedges' g — strengthens rather than duplicates the existing METR source record	5
genai-productivity-meta-2026	2026	A	E2 (learning subgroup, exam-environment moderator)	moderator subgroup of learning meta-analysis	subset of k=11 learning pool, GenAI-permitted-during-exam studies	exam/assessment performance	Hedges' g, "GenAI allowed" subgroup	g=0.76, 95% CI [0.24,1.28], p=0.004, k=3	positive, large, significant	measured (exam score, but tool present during measurement)	none reported	not analysed	university/pre-university, course-integrated	independent academic	Confounds "AI helps you pass a test while using AI" with "AI helps you learn" — authors explicitly interpret as tool-dependent augmentation, not durable learning; directly feeds skill-formation/cognitive-debt cross-cutting theme	5
genai-productivity-meta-2026	2026	A	E2 (learning subgroup, exam-environment moderator)	moderator subgroup of learning meta-analysis	subset of k=11 learning pool, GenAI-disallowed-during-exam studies	exam/assessment performance	Hedges' g, "No GenAI" subgroup	g=-0.06, 95% CI [-0.36,0.24], p=0.674, k=8	null, slightly negative	measured	none reported	not analysed	university/pre-university, course-integrated	independent academic	When the tool is removed at test time, the apparent learning benefit disappears entirely (point estimate even slightly negative) — strongest single piece of evidence in this source for a genuine (not just self-reported) skill-formation gap	5
genai-productivity-meta-2026	2026	N/A (methodological finding, not an effect size)	MIXED — this is the paper's core limitation	meta-analytic moderator design critique	n/a	n/a	n/a — methodological finding about moderator design	QM(1)=0.21, p=0.644 for "GenAI interface: Copilot vs Other" — the only tool-modality moderator tested	null (not significant), but test was underpowered to detect an era effect	n/a	n/a	n/a	n/a	independent academic	No autocomplete/chat/agentic moderator was ever constructed; E3 studies (n=2) were folded into a generic "Other" bucket alongside E2 studies — this is the precise era-conflation risk this task was dispatched to check for, and it is realised	5
