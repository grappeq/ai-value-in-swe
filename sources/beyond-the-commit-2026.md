# beyond-the-commit-2026 — "Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants" (ICSE 2026 SEIP)

**source_id:** beyond-the-commit-2026
**Date verified:** 2026-07-06 (verification-subagent check, four-check batch)
**RQs fed:** RQ2 (measurement — self-report internal inconsistency: satisfaction vs perceived time-saved); RQ6 (anti-metrics — satisfaction as a poor productivity proxy; candidate long-term measurement dimensions)

## Citation and fetchability

Chen, V. (Carnegie Mellon University); He, J., Williams, B., Valentino, J. (BNY Mellon); Talwalkar, A. (Carnegie Mellon University). *"Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants."* ICSE 2026 — Software Engineering in Practice (SEIP), Rio de Janeiro, 12–18 April 2026. **Full text fetchable**: arXiv:2602.03593 (https://arxiv.org/abs/2602.03593, HTML at https://arxiv.org/html/2602.03593v1) — no BLOCKED escalation needed.

## Method, population, scope

- **Method:** mixed-method — org-internal survey (n = 2,989 developer responses) + 11 semi-structured follow-up interviews, all at a single company (BNY Mellon, a large financial-services firm). Independent academic co-authorship (CMU) alongside company-employed co-authors (BNY Mellon) — collaborative, not purely company-authored/sponsored, but not an external/arms-length audit either.
- **Tooling studied:** primarily **GitHub Copilot**, with Cursor, ChatGPT and TabNine mentioned for context; the paper explicitly places emerging **agentic tools out of scope**. Data-collection timeframe not stated in the fetched text.
- **Era tag: predominantly E1/E2** (autocomplete/chat-assisted), by tool modality actually studied per PROTOCOL §2 — not E3, despite the 2026 publication date. Any productivity claim from this source does not count toward the DoD's E3 evidence bar.
- **Measurement basis:** entirely self-reported (survey + interview). No telemetry, code-output analysis, or objective performance measure anywhere in the paper — confirmed by the text itself, which notes the researchers "were unable to reliably obtain [objective] metrics ... across all engineers."

## Key findings (as reported, self-reported throughout)

- 86% of respondents reported being "satisfied or very satisfied" with AI coding-assistant tools, yet roughly 60% separately reported **less than one hour per week** of perceived time savings — a within-survey disconnect between stated satisfaction and stated quantitative benefit. Both figures are self-report; this is not a self-report-vs-measured gap (contrast METR), but a self-report-vs-self-report inconsistency, still useful for RQ6's case against satisfaction/acceptance-style metrics as productivity proxies.
- 11 interviews elicited six factors developers use to judge productivity: (1) self-sufficiency (less context-switching to external help), (2) frustration/cognitive load from imperfect outputs and prompt iteration, (3) task completion rate/quality on well-defined work, (4) ease of peer review of AI-generated code, (5) technical expertise/long-term skill development, (6) ownership of work (authorship, accountability, depth of understanding).
- Stated contribution: prior frameworks (SPACE, DORA-class) under-weight the last two, longer-horizon factors (technical expertise, ownership); the authors position this as the paper's main addition.

## Tier, independence, relevance

- **Tier: C** (single-company practitioner study with real survey N, mixed academic/practitioner authorship; not a controlled experiment, no counterfactual).
- **Independence:** partial — CMU co-authors are external academics, but three of five authors are BNY Mellon employees studying their own workforce; no vendor-sponsorship flag, but not an arms-length third party either.
- **Relevance to us: 2/5.** Per the verification brief for this check: the paper adds two things beyond a generic developer-perception survey — a documented satisfaction/perceived-benefit disconnect (RQ6-relevant) and a proposed set of longer-horizon productivity factors missing from SPACE/DORA — but it is otherwise a qualitative/self-report perception study of the kind this evidence base already holds many of, studying largely pre-agentic tooling (Copilot-class) despite its 2026 publication date. It should not be used to support any E3/agentic-era effect-size claim.

## What this can and cannot support

**Can support:** that self-reported satisfaction with AI coding assistants can diverge sharply from self-reported quantitative time-savings within the same population (86% satisfied vs ~60% reporting <1hr/week saved) — a caution against treating satisfaction or acceptance-style metrics as productivity evidence (RQ6); that practitioners themselves nominate long-term, hard-to-instrument factors (skill development, ownership/authorship) as part of how they judge AI-assistant value, which is directly relevant to RQ6's measurement-design question and to the skill-formation cross-cutting theme (§2).

**Cannot support:** any effect-size or productivity claim for agentic-era (E3) tooling — the tools studied are predominantly Copilot-class autocomplete/chat assistants, explicitly excluding agentic tools; any claim that AI coding assistants measurably improve or harm output, since no objective/measured data was collected; any generalisation beyond one financial-services firm's developer population.
