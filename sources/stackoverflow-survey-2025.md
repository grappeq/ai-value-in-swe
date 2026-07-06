# stackoverflow-survey-2025 — Stack Overflow Developer Survey 2025 (AI section)

## Citation(s)

Stack Overflow (Prosus). **"2025 Stack Overflow Developer Survey."** Fielded 29 May – 23 June 2025. Preview/highlights published 23 October 2025; full public results published 29 December 2025.

- Survey home / data explorer: https://survey.stackoverflow.co/2025
- AI section (primary source for this record): https://survey.stackoverflow.co/2025/ai
- Technology/IDE section: https://survey.stackoverflow.co/2025/technology
- Methodology: https://survey.stackoverflow.co/2025/methodology
- "Results are here" announcement (29 Dec 2025): https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
- Preview/podcast post (23 Oct 2025): https://stackoverflow.blog/2025/10/23/what-leaders-need-to-know-from-the-2025-stack-overflow-developer-survey/
- Press release: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
- SO's own follow-on trust-gap analysis (18 Feb 2026): https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
- "TL;DR for Leaders" internal resource, AI-adoption learning #1: https://stackoverflow.co/internal/resources/2025-stack-overflow-developer-survey-for-leaders/ai-adoption/

**On the 2026 edition (critical check requested):** the **2026 Stack Overflow Developer Survey does not yet have published results as of 2026-07-06.** It opened for *responses* (data collection) on 23 June 2026 — see https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/, which is explicitly a call for participation, not a results release. Based on the 2025 cycle's timing (fielded May–June, preview in October, full results in December), 2026 results should not be expected before roughly Q4 2026. This record therefore covers the 2025 edition only; re-check nearer December 2026 for the 2026 results.

## Verification status

**VERIFIED** for the 2025 edition — fetched directly from the primary results pages (survey.stackoverflow.co/2025/ai, /technology, /methodology) plus Stack Overflow's own blog/press coverage. Not a read from an abstract; the AI-section chart values below were pulled from the live results page itself.

**One unresolved minor discrepancy** (see Key findings, trust breakdown): two of Stack Overflow's own secondary write-ups (the Feb 2026 "Mind the gap" post and general press coverage) quote a 2024 baseline and a 2025 "trust" figure that don't fully reconcile arithmetically with the exact chart breakdown pulled from the primary AI page. Recorded transparently below rather than silently resolved — both versions trace to Stack Overflow itself, not to a third party, so this is flagged as an internal reporting inconsistency rather than a cross-source contradiction requiring escalation.

## Tier, era, independence

- **Tier: B.** Justification: a large-N (49,009), longitudinal (15th consecutive year), global self-report survey with no randomisation and no counterfactual — the same structural category as the DORA report, which PROTOCOL §3 names as the Tier B exemplar. Held at B rather than C/D because of its scale, multi-year continuity, and public methodology page; **but it is materially weaker than DORA on two axes** that should travel with any claim sourced here: (a) no structured statistical modelling (no factor analysis or regression — this is a topline-percentages survey, not an inferential one), and (b) heavier, self-acknowledged self-selection (recruited exclusively through Stack Overflow's own channels; see Method below).
- **Era: mixed E1/E2/E3, not split for the headline trendline.** The adoption/trust/favourability topline figures are asked against undifferentiated "AI tools" and cannot be decomposed by modality — the same limitation recorded for DORA 2025. However, several sub-items are cleanly era-taggable and are marked as such in Key findings below:
  - **E3-taggable directly:** the dedicated AI-agent adoption question (current/planned/no-plan use, daily agent use), the "vibe coding" question, and IDE-share entries for Cursor and Claude Code.
  - **E2-taggable:** ChatGPT/GPT model usage, Claude Sonnet (chat) usage.
  - **E1/E2-mixed:** GitHub Copilot usage (spans autocomplete and chat/agent modes depending on configuration; the survey does not separate them).
  - Treat the topline "84% adoption / falling trust" trendline as **era-mixed self-report evidence, admissible only as a historical baseline / trendline per PROTOCOL §2**, not as an E3 effect-size claim.
- **Independence / COI — flag in both directions.** Stack Overflow (owned by Prosus) is not a seller of AI coding tools, so it lacks the typical Tier D pro-AI-hype incentive of a GitHub/Microsoft/Anthropic. It has the **opposite** commercial incentive worth flagging: Stack Overflow's own question-and-answer traffic has collapsed as developers move to AI tools directly — independent reporting (DevClass, 5 Jan 2026) documents question volume falling from a 2014 peak of >200,000/month to under 50,000/month by late 2025, with only 3,862 questions posted in December 2025 (a 78% YoY drop). Stack Overflow therefore has a commercial motive to frame the AI story as "adoption without trust, enduring need for human community/verification" — a narrative that happens to support its own product. This does not invalidate the data (the trust/distrust breakdown is a topline chart, not an editorial claim) but should discount any narrative framing lifted from Stack Overflow's own blog commentary.
- **Population/selection COI:** self-selected, recruited solely through Stack-Overflow-owned channels (see Method). The methodology page explicitly states that "highly-engaged users on Stack Overflow were more likely to notice the prompts to take the survey" — the sample skews toward Stack Overflow's existing, loyal community, a population plausibly *more* exposed to the platform's own traffic-decline narrative and potentially more sceptical of the tools cannibalising it than the developer population at large. This is a distinct bias from DORA's convenience sample and should be weighted accordingly.

## Method & population

- **n = 49,009** qualified respondents from **177 countries**; approximately 15,000 additional responses were excluded for failing qualification checks.
- **Field dates: 29 May – 23 June 2025.**
- Per-AI-question response counts ranged **26,564–33,662** (54–69% completion rate on those specific items) — not every respondent answered every AI question.
- **Recruitment:** exclusively through Stack-Overflow-owned channels — onsite messaging, blog posts, email newsletters, banner ads, and social media posts; a Reddit ad campaign accounted for under 2% of responses.
- **Self-selection bias explicitly acknowledged by Stack Overflow itself** (methodology page): highly-engaged Stack Overflow users were more likely to see the survey prompts. No claim of representativeness of the broader developer population.
- **Measurement basis: everything below is self-reported.** No telemetry, no control group, no randomisation, no counterfactual — a pure attitudinal/behavioural self-report survey.

## Key findings (exact as reported; all self-reported)

**Adoption & usage:**
- **84%** use or plan to use AI tools in their development process, up from **76%** in 2024. [self-reported]
- **51%** of professional developers use AI tools daily; **47.1%** of all respondents use AI tools daily. [self-reported]

**Favourability (all respondents, exact chart breakdown):**
- Very favorable **22.9%**; Favorable **36.8%**; Indifferent **17.6%**; Unsure **2.3%**; Unfavorable **10.8%**; Very unfavorable **9.6%**.
- Combined positive (very favorable + favorable) ≈ **59.7%** (rounded to "60%" in Stack Overflow's own commentary), **down from "70%+" in both 2023 and 2024** (exact prior-year digits not broken out on the primary page — recorded as a range, not a point estimate).
- By segment: **61%** favourable among professional developers vs **53%** among those learning to code. [self-reported]

**Trust in AI output accuracy (all respondents, exact chart breakdown):**
- Highly trust **3.1%**; Somewhat trust **29.6%** → combined trust ≈ **32.7%** (rounded to "33%" in secondary coverage).
- Somewhat distrust **26.1%**; Highly distrust **19.6%** → combined distrust ≈ **45.7%** (rounded to "46%" in secondary coverage).
- Remainder (~21.6%) not itemised in the fetched breakdown — presumably a neutral/unsure category.
- Experienced developers are the most sceptical segment: lowest "highly trust" (**2.5–2.6%**) and highest "highly distrust" (**20–20.7%**).
- **Discrepancy flag (unresolved, not escalated):** Stack Overflow's own 18 Feb 2026 "Mind the gap" post and related press coverage instead quote trust as **29%** in 2025, "down 11 percentage points from 2024," and the press release quotes 2025 distrust as **46%, "up from 31% in 2024."** These secondary figures do not fully reconcile against each other or against the primary chart breakdown above (e.g. a 40%-trust/31%-distrust 2024 baseline vs a 33%-trust/46%-distrust 2025 split implies a swing larger than "11 points" on the trust side alone). Both versions originate from Stack Overflow's own publications, not a third party — recorded per CLAUDE.md's evidence rules as a conflict to present, not average or silently pick.

**Complex-task perception [T4-relevant]:**
- **29%** of professional developers believe AI struggles with complex tasks, down from **35%** in 2024 (i.e., fewer respondents report this specific complaint year-on-year). [self-reported]
- Only **3.9%** say AI handles complex tasks "very well." [self-reported]

**Top frustrations [T8-relevant]:**
- **66%** — "AI solutions that are almost right, but not quite" (top frustration). [self-reported]
- **45%** (45.2% in one cut) — "Debugging AI-generated code is more time-consuming." [self-reported]

**Productivity self-report:**
- **51.6%** agree AI positively affected their productivity to a "great extent" or "somewhat"; **41.4%** report the change was "not at all or minimally." [self-reported, perception only — no measured counterpart in this source]

**Agent-specific findings [E3]:**
- **31%** currently use AI agents; **17%** plan to; **38%** have no plans to adopt agents. **14.1%** use agents daily.
- Among current agent users, **69%** agree they experienced a productivity increase. [self-reported]
- A differently-cut sub-question reports **52%** either don't use agents or prefer copilot/autocomplete-style interaction — recorded separately as it appears to derive from a different question (interaction-mode preference) than the adoption-status split above; do not merge the two percentages.
- "Vibe coding": **~77%** say it is not part of their professional development work (one secondary source instead reports "nearly 72%" — minor variance across write-ups, both directionally consistent). [self-reported, E3-adjacent]

**Tool/IDE share [mixed era signal]:**
- ChatGPT/OpenAI GPT models: **82%** of AI users (81.4% in one cut). [E2]
- GitHub Copilot: **68%**. [E1/E2-mixed]
- Claude Sonnet (chat): **45%** of professionals vs **30%** of learners. [E2]
- IDE share, confirmed as 2025-fielded data (May–June 2025) via the survey's technology section: **VS Code 75.9%** of all respondents (76.2% professionals, 77.7% AI-using professionals) — its ninth consecutive year at the top and highest share on record; **Cursor 17.9%** of all respondents (debut) — reported as the fastest first-year IDE debut on record; **Claude Code 9.7%** of all respondents (debut). [E3 signal via tool identity, self-reported usage]

**Job-threat perception:**
- **64%** do not see AI as a threat to their job, down from **68%** in 2024 — i.e., threat-perception rose year-on-year. [self-reported]

**Human-verification / possible bottleneck-displacement signal [RQ2, RQ6, §5.6-relevant]:**
- Asked why they would still seek human help: **75.3%** cite "when I don't trust AI's answers"; **61.7%** cite ethical/security concerns; **61.3%** want to fully understand their own code.
- **84%** still use Stack Overflow itself for problem-solving; **67%** use GitHub; approximately **35%** specifically say they return to Stack Overflow after AI-generated code fails them. [self-reported]

## What this can and cannot support

**Can support:** a directional, self-reported claim that AI-tool adoption kept rising in 2025 (84%, up from 76%) while trust-in-accuracy and overall favourability both fell within the same, Stack-Overflow-engaged respondent population — plus descriptive 2025 base rates for agent adoption, top frustrations, and continued reliance on human/community verification. Useful as a trendline anchor and as a second, independently-run data point alongside DORA's adoption/trust findings (PROTOCOL §5, tension 1 and 3 context).

**Cannot support:** any measured/telemetry effect size, any causal claim about AI's actual productivity or quality impact, or generalisation beyond Stack Overflow's own self-selected, highly-engaged respondent base to the developer population at large. All figures are self-report only, with no measured counterpart in this source — the perception/reality gap (PROTOCOL §5.1) cannot be tested against this source alone.

## Corrections vs the seed description in PROTOCOL §6

1. **"Stack Overflow Developer Survey 2025/2026" — the 2026 edition does not exist as a results release yet.** As of 2026-07-06 it is open only for *response collection* (opened 23 June 2026); no 2026 results have been published. The seed's implicit pairing of "2025/2026" should be corrected to "2025 (verified); 2026 (fielding in progress, no results yet)."
2. **Secondary-source labelling error to guard against:** at least one 2026-dated secondary write-up ("byteiota," "Stack Overflow Dev Survey 2026: AI at 84%, Trust at 3%") mislabels 2025-fielded data (84% adoption, 3% "highly trust," and the Cursor/Claude Code IDE-share figures — all confirmed above as May–June 2025 data) as "2026" results. This appears to be a publication-date-vs-survey-year confusion in the secondary source, not an actual second dataset. Flagged here so it is not accidentally re-cited as 2026 evidence downstream.
3. **The seed's "adoption rising while trust/favourability falls" framing is directionally correct but conflates two distinct survey questions.** Trust-in-accuracy (33% trust vs 46% distrust in 2025, chart breakdown above) and overall favourability (59.7% positive in 2025, down from 70%+ in 2023–2024) are separate items with separate response scales; both fell, but they should be cited as two findings, not one, in synthesis.
4. The seed does not mention the population skew or Stack Overflow's own traffic-decline context; both are added above as independence flags per the task brief and CLAUDE.md's COI rule.

## Follow-up leads (not extracted — leads only)

1. **2026 Stack Overflow Developer Survey** — opened for responses 23 June 2026 (https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/); results expected late 2026 by analogy with the 2025 cycle. Re-check ~December 2026.
2. **Stack Overflow, "Mind the gap: Closing the AI trust gap for developers"** (18 Feb 2026) — https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/ — Stack Overflow's own interpretive follow-up on the adoption/trust divergence; not independent, but the source of the discrepant trust figures noted above.
3. **DevClass (5 Jan 2026), "Dramatic drop in Stack Overflow questions as devs look elsewhere for help"** — https://www.devclass.com/ai-ml/2026/01/05/dramatic-drop-in-stack-overflow-questions-as-devs-look-elsewhere-for-help/4079575 — independent corroboration of the traffic-collapse COI context (78% YoY question-volume drop, Dec 2025).
4. **Eric Holscher, "Stack Overflow's decline"** (21 Jan 2025) — https://www.ericholscher.com/blog/2025/jan/21/stack-overflows-decline/ — independent practitioner analysis, predates the 2025 survey; background on the traffic-decline COI.
5. **Techzine Global, "Stack Overflow in freefall: 78 percent drop in number of questions"** — corroborating independent coverage of the same traffic collapse.
6. **ADTMag (Jan 2026), "Developers Lean on AI More, But Report Growing Doubts About Accuracy, Stack Overflow Survey Says"** — https://adtmag.com/blogs/watersworks/2026/01/stack-overflow-survey.aspx — independent trade-press summary; cross-check source.
7. **ShiftMag, "84% of developers use AI, yet most don't trust it!"** — https://shiftmag.dev/stack-overflow-survey-2025-ai-5653/ — independent summary used for cross-checking figures above; could be formally extracted as a second voice if wanted.
8. **GitHub, StackExchange/Survey repo** — https://github.com/StackExchange/Survey — official repository; may host raw/anonymised data for a bespoke cross-tab of the adoption-vs-trust divergence if Phase 2 wants to go beyond topline percentages.

## Recency check notes

Source is under 12 months old (full results published 29 December 2025, within the 2025-07-06-to-now window), so a mandatory supersession search was not strictly required by the 12-month rule — but the task specifically required checking for a 2026 successor, which was carried out (see citation section above): confirmed no 2026 results exist yet, only an open response-collection window since 23 June 2026. Re-run this recency check nearer December 2026, when 2026 results are plausible given the 2025 cycle's timing.
