# german-se-survey-2026 — GenAI adoption in the German software engineering industry (interviews + survey)

**source_id:** german-se-survey-2026
**Date verified:** 2026-07-06
**RQs fed:** RQ1 (secondary — perceived value only, all self-reported), RQ2 (secondary — a wholly self-report instrument whose authors themselves concede the construct-validity problem), RQ3 (primary among this source's contributions — barrier ranking, the "context wall", seniority moderation), RQ6 (obliquely — adoption/governance context for what a European org can expect to see internally).
**Cross-cutting theme:** touches **skill formation & cognitive effects** (PROTOCOL v0.4) via practitioner-voiced atrophy concerns only — interview quotes, no measurement. See Finding 9.

## Citation

Felder, L., Eisenreich, T., Fischer, M., Wagner, S., & Chen, C. (2026). *Adoption of Generative Artificial Intelligence in the German Software Engineering Industry: An Empirical Study.* Accepted at FSE '26 — 34th ACM International Conference on the Foundations of Software Engineering (ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering), 5–9 July 2026, Montréal, QC, Canada.

- arXiv: [2601.16700](https://arxiv.org/abs/2601.16700) — **v1: 23 January 2026; v2: 9 June 2026**. Version read for this record is **v2** (presumed camera-ready given the June revision date ahead of the July conference; the arXiv page does not itemise changes between versions — recorded per the PROTOCOL §3 substitution rule, since the ACM proceedings version was not fetched).
- Licence: CC BY 4.0.
- Affiliations as printed: Felder, Eisenreich, Wagner, Chen — Technical University of Munich; Fischer — Heilbronn University of Applied Sciences.

## Verification status

**VERIFIED — full text read** (arXiv HTML v2), not abstract-only, across two targeted fetch passes. Title, authors, venue acceptance, interview count (18), survey n (109), and the fielding window (**15 April – 20 August 2025**, exactly as the task brief stated) all confirmed. The policy-practice-gap passage and the Becker et al. citation were re-fetched and quoted verbatim in a second pass. **Numeric caveats:** (a) the main body reports **88%** of respondents working primarily in Germany while the limitations section reportedly says 89% — trivial, but do not quote both; (b) the experience bands as extracted (20% junior 0–3 years, 54% mid 5–15, 26% senior 15+) do not visibly cover 3–5 years, so the band edges may be an extraction artefact — treat the mean (12.1 years) and median (10 years) as the reliable figures; (c) most percentage figures were surfaced in a single fetch pass and are not double-confirmed digit-by-digit.

## Tier, era, independence

- **Tier: B, at the weak end.** Peer-reviewed academic mixed-methods study (FSE '26 research paper) — structured observational work, not practitioner signal, so Tier C's definition does not fit. But it sits well below the DORA-class exemplars of Tier B: n = 109 convenience sample, single country, one-off, and **every quantitative result is self-reported**. Practical grading rule for downstream use: its *adoption-pattern and perception* claims carry Tier B weight with caveats; anything resembling an effect on productivity or quality carries no more weight than a good self-report survey ever can, i.e. it feeds RQ2's perception side, never a measured-effect cell.
- **Era: E1/E2-blended, chat-dominant; not E3-attributable.** Fielded April–August 2025 — chronologically the agentic era — but the era rule tags by modality studied. The instrument asked about *tools*, not modalities, and the paper states outright that "the survey did not distinguish between chat interfaces, IDE integrations, or other deployment forms". The tool mix is dominated by chat (ChatGPT 90%) and classic IDE assistance (Copilot 55%); the only clearly agentic-capable tool is Cursor at 16%, with no data on whether its agent mode was used. Under the era-transfer rule, this source supports adoption baselines, barrier/perception patterns, and methodology points — **no E3 effect-size claim can rest on it**.
- **Independence: clean, no COI flag.** Wholly academic authorship (TUM, Heilbronn UAS); no vendor funding or sponsorship statement was found in the fetched text, and no author is affiliated with a tool vendor. No funding statement was positively identified either — recorded as "none found", not "none exists".

## Method & population

- **Design:** Mixed methods. (1) Qualitative pre-study: **18 semi-structured exploratory interviews** with practitioners — junior and senior developers, project managers, and CTOs — from "both major German corporations and various small and medium enterprises (SMEs)"; all sessions recorded and transcribed; open coding by two independent researchers with consensus resolution. (2) Quantitative survey: **n = 109 complete responses** (210 started, 101 excluded as incomplete — a 48% completion rate), fielded **15 April – 20 August 2025**, recruited by **convenience sampling** via industry contacts and LinkedIn; anonymous, voluntary, no incentives.
- **Instrument:** six blocks — demographics; tooling and usage frequency (5-point scales); prompting strategies (10 techniques); challenges (14 items); impact assessment (5 dimensions); future perspectives.
- **Population:** 62% software developers/engineers, 13% team leads/managers, 8% architects/requirements engineers. Experience mean 12.1 years, median 10 (not a junior-skewed sample). Organisation sizes: 29% medium (100–999 employees), 27% large (1,000–9,999), 24% very large (>10,000), 14% small (10–99), remainder micro/unstated. 88% work primarily in Germany. Education: 51% Master's, 22% Bachelor's, 14% doctorate, 12% no academic background.
- **German context as the authors frame it:** GDPR and the EU AI Act create "immediate tensions when using cloud-based AI services"; the Mittelstand (SME-heavy) structure and a quality-focused engineering culture are claimed to distinguish this market from the US-centric adoption literature.

## Key findings

Every quantitative finding below is **self-reported** (survey Likert/frequency items) or **interview-derived**; the study measures nothing. One record per finding, per §4.

### 1. Tool mix (self-reported adoption, multi-select)
ChatGPT **90%**, GitHub Copilot **55%**, Google Gemini **37%**, Anthropic Claude **28%**, internal company tools **28%**, Ollama (self-hosted) **20%**, Cursor **16%**, Mistral **10%**. Modality undifferentiated by design (see era note above). The 90/55 split — general chat far ahead of the integrated IDE assistant — is itself the clearest single datum: as of mid-2025, German SWE GenAI use was still predominantly a copy-paste chat workflow (E2).

### 2. Task-type usage (self-reported frequency)
- Code completion / snippet generation: most common — **70%** use it at least a few times per week (**T3/T4 blend, unresolved** — the instrument does not split greenfield from brownfield).
- Learning / training: high adoption (T10-adjacent; also the cross-cutting skill theme).
- Bug fixing: **36%** multiple times a week (T8).
- Testing: **25%** adoption (T6).
- Validation-type tasks generally lower — the authors call out a "clear divide between creation and validation": generative tasks dominate, quality-assurance use is thin. Feeds the PROTOCOL §5 tension-6 picture: generation adopted faster than verification.

### 3. Perceived impact (self-reported, 5-point)
**76%** report individual workflow speed improved; **73%** report faster learning of new topics; bug-fixing efficiency **40%** improved vs **39%** no change (the weakest of the impact dimensions). Overall sentiment "overwhelmingly positive". These are perception rows for RQ2, not value rows for RQ1.

### 4. Barrier ranking (self-reported severity, 5-point; 14 items)
1. AI hallucinations / invented facts — mean **3.4**; **51%** rated very/extremely challenging.
2. **Limited context awareness of the codebase — mean 3.3; >50% severe.** The paper's abstract names this the most significant barrier to effective use.
3. Outdated information / knowledge cutoff — mean **3.2**; 50% critical.
4. Data privacy and security concerns — mean **3.1**; **47%** high severity.
Rated *least* relevant: "AI does not comply with instructions", "AI output not useful", and "prompting is time consuming" — i.e. respondents' complaint is not that output is worthless but that the tool cannot see enough of the project. The authors describe a two-sided "context wall": spatial (the AI "just see[s] part of the code and miss[es] dependencies") and temporal (knowledge cutoff). Directly feeds RQ3's task-characteristic hypothesis: context requirement predicts failure.

### 5. Distrust–speed correlation (self-reported, correlational)
Negative correlation between reported workflow-speed improvement and distrust in AI output: **ρ = −0.33, p < 0.001**. Direction of causality unknowable from this design (distrust may suppress benefit, or poor results may generate distrust); the authors concede correlational limits.

### 6. Seniority moderation — the "experience paradox" (self-reported)
Junior engineers (<5 years) rated "being very specific with instructions" effective at **78%** vs **39%** among seniors (>15 years); **χ²(2, N=109) = 10.84, p_adj = 0.022**. The authors read this as greater expertise reducing perceived utility. Consistent in direction with the §5 tension-5 seniority asymmetry (gains concentrate in juniors), but note the outcome here is *perceived prompting effectiveness*, not measured productivity. (Band edge "<5 years" vs the demographic junior band "0–3" as extracted — see verification caveats.)

### 7. Organisation-size effects (self-reported)
- Code-generation frequency falls with organisation size: small enterprises **93%** weekly-plus use vs **31–50%** in large enterprises and corporations.
- Self-hosted models (Ollama) show a bimodal pattern: **34%** in medium enterprises and **35%** in >10,000-employee corporations, but **0%** in 1,000–9,999-employee large enterprises. The authors propose "two distinct drivers": resource-rich corporations building sovereign stacks, and cost-conscious mid-size firms self-hosting cheaply, with the in-between tier doing neither.

### 8. Governance and the policy–practice gap — extract exactly as evidenced
This is the finding the reported angle rests on, so the sourcing matters:
- **The paper's own primary evidence** (interview pre-study, Theme 3): "Participants from larger companies reported strict data sovereignty policies that prohibit the use of public LLMs, necessitating the use of company internal tools." Smaller enterprises are "concerned about intellectual property leakage but lack the infrastructure to support self-hosting." One interviewee: "AI in most applications these days is a service, not a product, it phones home."
- **The policy-practice-gap claim itself is a citation, not this paper's finding.** Verbatim: "Recent qualitative research confirms these dynamics: Neumann et al. (2026) found that regulatory pressures in German organizations are often translated into restrictive policies without accounting for actual usage patterns, creating systematic gaps between policy and practice."
- **What this paper does *not* show:** any direct measurement of a gap between stated policy and actual usage (no shadow-usage question, no policy-vs-behaviour cross-tabulation). A suggestive tension exists in its own data — 90% ChatGPT adoption across a sample where large-organisation respondents report public-LLM prohibitions — but the paper does not itself make that inference, and neither should we without the cross-tab. **If the policy-practice gap matters downstream, Neumann et al. (2026) is the primary source and needs its own extraction; this record cannot carry that claim.**

### 9. Nulls, negatives, and practitioner-voiced concerns
- **Prompting-technique null:** advanced strategies underperform basics — context-giving (mean 4.0) and specificity (3.9) top the list; role prompting (**2.9**) and pre-made templates (**2.8**) rank lowest. Elaborate prompt engineering shows no perceived advantage over simply providing context.
- **Bug-fixing reversal (interview, negative):** "Bug fixing takes longer than before, because you are not fixing your own code" — review/comprehension overhead eroding gains on unfamiliar AI-authored code (T8; RQ4-adjacent, qualitative only).
- **Quality-debt concern (interview):** a senior engineer: "I expect a large amount of low-quality code in the near future." Perception, not measurement; consistent in direction with §5 tension 4.
- **Skill-atrophy concern (interview; cross-cutting theme tag):** "With continuous and extensive use of AI, the basic understanding of how the code works is lost." Practitioner-voiced mechanism concern only — no comprehension outcome measured; feeds the v0.4 theme as anecdotal corroboration that the concern is live among practitioners, nothing more.
- The paper itself cites Becker et al. (2025), arXiv:2507.09089 — i.e. the METR RCT, elsewhere in this repository — as a counterpoint: "experienced open-source developers using AI tools actually increased completion time by 19%, suggesting that expertise moderates AI effectiveness in complex ways." Recorded here only to note the paper positions its perception data against that measured result; this record adds no evidence to the METR row.

### Heterogeneity
Splits reported: seniority (finding 6) and organisation size (finding 7). No splits by language ecosystem, codebase age, or industry vertical. Task-type resolution is coarse (completion / bug fixing / testing / learning) and cannot separate T3 from T4.

## Authors' stated limitations (near-verbatim)

- **Internal validity:** "All values were measured via self-report, introducing measurement error"; fixed, thematically grouped question order "may have introduced context or carryover effects".
- **External validity:** convenience sample "may not fully represent the broader user population"; findings "were sampled in mid-2025 and may not generalize to future states"; German concentration limits global transfer.
- **Construct validity:** usage frequency, prompting effectiveness, and workflow-speed impact all "rely on respondents' subjective interpretations".
- **Causality:** correlational analysis only.
- **Response bias, openly conceded:** "Participants enthusiastic about GenAI may both use tools more frequently and overestimate their productivity impact." The authors' own limitations section is, usefully, a compact argument for RQ2's central point.

## What this can and cannot support

**Can support (Tier B weak-end, E1/E2-blended, no COI):** a mid-2025 adoption baseline for a GDPR/AI-Act-regulated European market — chat-first tool mix (ChatGPT 90% vs Copilot 55%, Cursor 16%), creation-over-validation task skew, context-awareness as the top-ranked barrier, perceived-utility gains concentrating in juniors, and organisation-size-patterned governance (public-LLM prohibitions in large firms, bimodal self-hosting). Strongest downstream use: RQ3's context-wall hypothesis (practitioner-ranked, n=109, converging with mechanism arguments elsewhere) and RQ6/exec context on what a European enterprise's adoption profile actually looks like versus US-centric narratives.

**Cannot support:** any measured productivity or quality effect (nothing is measured); any E3/agentic claim (modality undifferentiated, chat-dominant); the policy-practice gap as a finding of *this* paper (it is cited from Neumann et al. 2026 — see Finding 8); representative population claims (convenience sample via LinkedIn, plausibly enthusiast-skewed, per the authors' own bias concession); causal direction on the distrust–speed correlation.

## Cross-reference assessment (report only)

- **§5 tension 1 (perception–reality):** contributes perception-side rows only (76% perceived speed-up, wholly self-reported) — exactly the class of evidence METR's result warns against treating as impact evidence. The paper's own citation of Becker/METR as a counterpoint shows the authors agree.
- **§5 tension 2 (greenfield/brownfield):** the context-wall barrier (limited codebase awareness, top-ranked) is indirect practitioner corroboration that high-implicit-context work resists current tools — mechanism-level support, no effect size.
- **§5 tension 5 (seniority asymmetry):** the 78%/39% junior/senior perceived-effectiveness split is directionally consistent with Cui et al.-class findings, on a perception outcome.
- **§5 tension 6 (bottleneck displacement):** the creation-vs-validation adoption divide is weak, indirect support (generation adopted, verification not).
- No contradiction with existing evidence rows surfaced during extraction; nothing appended to contradictions.md is warranted from this source alone (and this subagent does not write there in any case — flagging for the orchestrator: none needed).

## Follow-up leads (not extracted)

1. **Neumann et al. (2026)** — the actual primary source for "regulatory pressure → restrictive policies without accounting for actual usage patterns, creating systematic gaps between policy and practice". Qualitative, German organisations. If the governance/shadow-usage angle matters for the exec brief, this needs its own extraction; it is the load-bearing citation.
2. The ACM FSE '26 proceedings version, to confirm v2 = camera-ready.
3. Replication package / questionnaire instrument, if published — would settle the experience-band edges and allow the policy-vs-usage cross-tab this paper never ran.

## Recency check notes

Paper is ~1–6 months old at verification (v1 January 2026, v2 June 2026; conference is running the week of this extraction) — inside the 12-month threshold, so no mandatory supersession search. No retraction or follow-up encountered during fetches. Survey data are mid-2025 vintage; the authors themselves flag that adoption states move quickly, so treat the tool-mix percentages as a dated snapshot, not a current reading.
