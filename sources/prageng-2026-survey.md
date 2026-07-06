# prageng-2026-survey — The Pragmatic Engineer, "AI Tooling for Software Engineers in 2026" (+ companion trend pieces)

## Citation(s)

**Main survey report (primary record):**
Orosz, Gergely & Nilsson, Elin. **"AI Tooling for Software Engineers in 2026."** *The Pragmatic Engineer* (Substack newsletter), published 3 March 2026.
- https://newsletter.pragmaticengineer.com/p/ai-tooling-2026

**Companion trend pieces (same underlying survey, narrative follow-ups, read for this record):**
- Orosz, G. **"The impact of AI on software engineers in 2026: key trends. Part 1."** Published 14 April 2026. https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026
- Orosz, G. **"The impact of AI on software engineers in 2026: key trends. Part 2."** Published 19 May 2026. https://newsletter.pragmaticengineer.com/p/ai-impact-on-software-engineers-part-2

**Referenced but not itself extracted (different, broader survey — flagged so it is not conflated):**
- Orosz, G. **"The Pragmatic Engineer 2025 Survey: What's in your tech stack?"** Fielded April–May 2025, n = 2,997 (post-dedup), covers whole tech stack, of which AI tools are one section (85% mention using at least one AI tool; 4% explicitly none). This is a **different, broader** annual "tech stack" survey, not the dedicated AI-tooling survey the main record above is drawn from. The 2026 AI-tooling article's own "nine months ago, last May" comparison point most plausibly refers to this or a similarly-timed AI-specific check-in — Orosz's piece does not give the May 2025 comparator a formal name, and this ambiguity is recorded rather than resolved (see Method notes below).

## Verification status

**PARTIALLY VERIFIED.** All three pieces are Substack posts with a hard paywall partway through; each was fetched and read to the paywall boundary.

- **Main post (3 March 2026):** the data-bearing sections are **free and were read**: "Interesting findings," "Most-used AI tools," "Popular models," "AI trends: Mainstream adoption achieved," "AI agent usage rising," "Company size and tool usage," "Tools engineers love," "Demographics." The paywall begins at the section headed **"Takeaways and the full report"** (last visible line: the demographics/region chart) — everything past that point, including the promised **65-page detailed report** for paying subscribers, was **not read** and is not extracted here.
- **Part 1 (14 April 2026):** free through roughly the first three sections (costs, usage limits, "Builder" impact); paywalled from "Section 4 (Shipper benefits)" onward, marked "This post is for paid subscribers."
- **Part 2 (19 May 2026):** free through the seniority/code-quality/organisational-barriers material extracted below; "Section 5 (AI tooling 'addiction')" is partially paywalled and Sections 6–7 are fully behind the paywall.
- No free companion post was found that covers the full 65-page report; the two "key trends" pieces are narrative add-ons with their own (different) data points, not a full-text mirror of the paywalled report. Per CLAUDE.md's extraction rule, only the material actually read below is presented as extracted; nothing past a paywall marker is treated as read.
- Numbers below were pulled via automated page fetches (WebFetch), not a manual re-read of the raw HTML; exact percentages are quoted as returned, but treat single-decimal precision (e.g. "63.5%") as sourced from the article's own charts/text rather than independently re-verified against a screenshot.

## Tier, era, independence

- **Tier: C.** Practitioner-run survey journalism (not an academic or telemetry study; not a vendor product write-up). Fits PROTOCOL §3's Tier C definition and the named §6 "Pragmatic Engineer" hunting ground directly.
- **Independence / COI check:** No sponsor, "brought to you by," partner-company mention, or advertisement was found in the main 3 March 2026 post itself (checked directly). The Pragmatic Engineer's business model is subscription revenue from the newsletter itself, not tool sales — Orosz has no identified stake in any of the ranked tools (Claude Code, Cursor, Copilot, Codex, etc.). **Caveat:** this check covers only the piece in hand; The Pragmatic Engineer newsletter has run sponsored content/ads in other editions historically, and that broader pattern was not audited here. No COI flag is being attached to the actual survey data, but note this is a for-profit publication whose growth depends on engaging content about a fast-moving topic — a much weaker incentive concern than a tool vendor, but not zero.
- **Population COI (the more important flag): self-selection via newsletter readership.** Recruitment was "The Pragmatic Engineer subscribers" — an audience that opted in to a newsletter specifically covering advanced/insider engineering practice. Demographics confirm the skew: median respondent experience is **11–15 years**; **34%** of respondents are engineering leadership (vs 55% "engineers"); Europe/US-majority geography. This is a *more* senior- and engaged-skewed population than Stack Overflow's own self-selected sample (which recruited from a broader Q&A-site readership) — record this explicitly, as instructed, before using any adoption figure from this source in synthesis.
- **Era: E3-focused by design, but individual figures need per-item tagging, not a single blanket tag.** The survey deliberately foregrounds agentic tools — eight of the top-10 ranked tools are agentic products (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Antigravity, JetBrains Junie, Zed) rather than autocomplete or chat. Tag accordingly:
  - **E3-taggable directly:** "regular AI agent use" (55%), agent adoption by seniority, Claude Code/Cursor/Codex market-share and "most loved" figures, agent-user-vs-non-user sentiment split.
  - **E2-taggable:** the chatbot figures (ChatGPT, Gemini, Claude-as-chat) and "popular models" (Opus/Sonnet — used across both chat and agent surfaces, not cleanly separable in this source).
  - **E1/E2-mixed:** GitHub Copilot's ranking and company-size breakdown (Copilot spans autocomplete and agent-mode configurations; the survey does not separate them, the same limitation recorded for GitHub Copilot in the Stack Overflow 2025 record).
  - The blanket "95% weekly+ AI usage" and "75% use AI for 50%+ of work" toplines are **era-mixed** (any tool counts) — treat as adoption-intensity trendline, not an E3-specific claim.

## Method & population

- **n = 906 respondents.** Recruitment: Pragmatic Engineer newsletter subscribers (self-selected, not random or representative of the developer population at large).
- **Fielding window: 27 January – 17 February 2026** (three weeks).
- **Measurement basis: self-reported throughout.** This is a pure attitudinal/behavioural survey — no telemetry, no control group, no counterfactual, no measured productivity outcome anywhere in the source. Every figure below is self-report and is marked as such.
- **Respondent composition:** Engineers 55%, engineering leadership (EM/Director/VP roles) 34% (remainder unspecified); median experience 11–15 years; company-size distribution described as "fairly even"; geography majority Europe or US.
- Respondents could select multiple tools (usage figures are not mutually exclusive).
- **Trendline comparators referenced in-article, not independently verified beyond the article's own text:** "our previous survey nine months ago, last May [2025]" and "our survey three years ago, in the spring of 2023" — Orosz does not give either comparator a formal title/citation in the free portion, so exact methodology parity with the 2026 fielding cannot be confirmed from this record alone. Treat trend comparisons (e.g. "Copilot usage barely risen," "Cursor grew ~35% in nine months") as the *article's own* claimed trend, not an independently checked one.

## Key findings (all self-reported; era tag per item)

**Adoption intensity [era-mixed]:**
- 95% use AI tools weekly or more often; 2.1% report no AI usage at all.
- 75% use AI for 50%+ of their work; 56% use AI for 70%+ of their work.
- Tool multiplicity: 70% use 2–4 tools simultaneously; 15% use 5+ tools; 15% use a single tool.

**Agent-specific adoption [E3]:**
- **"55% of respondents now regularly use AI agents."** No formal definition of "AI agent" is given in the free text; usage examples cited include code review, bug fixing, and code investigation. This is the headline figure named in the task brief.

**Tool rankings [mixed E1–E3, per item]:**
- Top-10 by mentions: (1) Claude Code — described as market leader, "51% of agent users" figure attached to it; (2) chatbots (ChatGPT/Claude/Gemini combined); (3) GitHub Copilot; (4) Cursor; (5) Codex; (6) Gemini CLI; (7) OpenCode; (8) Antigravity; (9) JetBrains Junie; (10) Zed.
- Chatbot leaders near parity: ChatGPT 107 mentions, Gemini 107 mentions, Claude "comparable volume" (exact Claude mention-count not given in the free portion).
- "Most loved" tools: Claude Code 46%, Cursor 19%, GitHub Copilot 9%.
- Models: "Anthropic's Opus and Sonnet dominate the ranking of models used for coding," with more combined mentions than all other models; ~1 in 8 respondents use their company's default model rather than choosing one.

**Seniority splits [E3; directly relevant to §5 tension 5]:**
- **Agent adoption by role:** Staff+ engineers 63.5%; Directors/VPs 51.9%; regular engineers 49.7%; engineering managers/leads 46.1%.
- Claude Code is more loved at Director level than at junior levels (magnitude not quantified in the free text); Cursor preference declines with seniority; GitHub Copilot adoption is comparatively stable across management levels.
- Part 2 (narrative, self-reported anecdote, not a survey topline stat): senior/director-level respondents describe AI as an "amplifier" of existing expertise and a substitute for work "previously delegated to interns," with one quote characterising the benefit as "10x more productivity" for seniors — **this is a self-reported anecdotal quote from the write-up, not a measured effect size or a survey percentage; do not treat as an effect-size claim.**
- Junior-specific complaints (Part 2, self-reported): AI tools are "stressful to use" for less-experienced developers; juniors report higher token consumption and higher personal/team AI bills than seniors; juniors report spending significant time "triple checking and redoing stuff"; juniors report lacking "the experience or knowledge to tell AI exactly what to do."
- Senior-specific complaint (Part 2, self-reported): seniors report having fewer tasks left to delegate to juniors because AI now absorbs that work — a mentoring-pipeline concern, not a productivity complaint.

**Company-size effects [mixed]:**
- Claude Code usage: ~75% at the smallest companies, lower (exact figure not given in the free portion) at 10,000+-employee companies.
- GitHub Copilot usage: 56% at companies of 10,000+ employees vs 35% at the smallest companies — framed in-article as enterprise procurement driving Copilot's large-company share rather than individual engineer preference.
- Engineers at large enterprises report fewer opportunities to experiment with new tools than engineers at smaller companies.

**Satisfaction / sentiment [self-reported, E3-framed]:**
- Agent users report feeling "excited" about AI at 61% vs 36% for non-users; agent users report "skeptical" sentiment at 11% vs 22% for non-users — i.e., agent users are roughly twice as likely to be excited and half as likely to be skeptical as non-users. **This is a correlation between agent use and pre-existing/concurrent AI enthusiasm, not a measured causal productivity effect** — the direction of causality (excited people adopt agents vs agents make people excited) cannot be determined from this source.

**"What didn't work" / limitations material (Part 1 and Part 2 companion posts, self-reported):**
- Cost: ~15% of respondents raise AI tool cost as a concern; typical company-paid plans ~$200/month vs personal subscriptions ~$20/month or free tiers; ~5% maintain separate work and personal subscriptions; UK/EU-based respondents express more budget concern than US-based respondents, with European firms reportedly demanding clearer ROI before committing $30–50/month per engineer.
- Usage limits: ~30% report hitting usage/rate limits; ~20% report staying comfortably under limits. Complaints include "daily limits disrupt workflow mid-task" and token-budget mistakes causing rapid quota depletion; friction from switching between multiple tools.
- Engineer "archetypes" introduced in Part 1 (self-reported/authors' framing, not a validated taxonomy): **Builders** (quality/architecture-focused), **Shippers** (speed-to-production focused), **Coasters** (adequate performers, described as lacking strong technical taste). Builders specifically report "more AI slop" from colleagues' code, increased debugging responsibility, and a sense of identity loss from reduced hands-on coding.
- Code-quality complaints (Part 2): "low code quality," "duplicate, verbose code, poor abstractions," "tiny bugs," "repetitive code"; developers reportedly "losing understanding of the codebase"; management described as focusing on "output over quality."
- Organisational friction (Part 2): "tooling chaos" when teams independently pick different AI tools; difficulty reviewing AI-generated pull requests; quality-monitoring concerns described as outweighing velocity gains in some teams' framing.

**Trendline vs prior editions (article's own framing, not independently re-verified):**
- Claude Code: did not exist at the "last May [2025]" comparison point (it launched May 2025); is now ranked #1 roughly nine months later.
- Cursor: usage grew "~35%" over the same nine months.
- GitHub Copilot: usage "barely risen" over the same window.
- Codex: "explosive early growth" despite not existing at the May 2025 comparison point; now cited at roughly 60% of Cursor's usage level.
- OpenCode, Gemini CLI, and Antigravity are all noted as having launched after the May 2025 comparison point.

## What this can and cannot support

**Can support:** a directional, self-reported picture of a heavily senior-/leadership-skewed, engaged newsletter-readership population in which AI-agent tools (led by Claude Code) have become the dominant coding-tool category by early 2026, adoption intensity is high, and agent adoption/enthusiasm correlates positively with seniority (Staff+ highest) within this specific sample — plus descriptive base rates for cost concerns, usage-limit friction, and code-quality/organisational complaints as reported by this population. Useful as a second, differently-selected practitioner-survey data point alongside Stack Overflow 2025 and DORA 2025 for RQ1/RQ2, and as one input (not the sole input) to the seniority-asymmetry tension (§5.5).

**Cannot support:** any measured/telemetry productivity effect size (nothing in this source is measured — it is 100% self-report); representativeness of developers generally (the population is explicitly skewed toward senior, newsletter-engaged, Europe/US-based respondents, smaller and more selected than Stack Overflow's already-flagged self-selected sample); a validated causal seniority-productivity claim (adoption/sentiment correlations only, and the one "10x" figure attributed to seniors is an anecdotal quote, not a survey statistic); any claim about the paywalled 65-page full report, which was not read.

## Cross-referencing assessment (for the human's review — not written to contradictions.md)

**1. Adoption-rate divergence across surveys (906-respondent PragEng "55% regularly use agents" vs Stack Overflow 2025's 31% "currently use AI agents" vs DORA 2025's 61% "agent mode never used"):**
These three figures, all self-reported and all fielded within roughly a 9-month window (SO: May–June 2025; DORA: fielded earlier in 2025 per its own record; PragEng: Jan–Feb 2026), disagree by tens of percentage points and are not straightforwardly reconcilable from the source records alone. Contributing factors, none of which can be cleanly separated with the data at hand:
- **Population selection is the largest suspect.** PragEng's readership is explicitly more senior (median 11–15 years, 34% leadership) and more engaged with cutting-edge tooling than Stack Overflow's already self-selected "highly engaged" respondents, which in turn is presumably more engaged than DORA's broader survey population. A more senior/engaged population plausibly agent-adopts earlier and more heavily — consistent with the ordering PragEng > Stack Overflow > DORA (never-use) implies.
- **Question wording differs materially.** "Regularly use" (PragEng) vs "currently use" (Stack Overflow) vs "never use agent mode" (DORA) are not the same construct, and none of the three source records give a shared operational definition of "agent."
- **Fielding-date gap in a fast-moving market.** PragEng's fielding (Jan–Feb 2026) postdates Stack Overflow's (May–June 2025) by roughly eight months, and the PragEng article's own trendline data shows Claude Code alone going from non-existent to market leader in that period — some genuine adoption growth almost certainly occurred, not purely a population artefact.
- **Recommendation:** treat all three adoption percentages as population- and wording-specific snapshots, not as competing measurements of one true "developer agent-adoption rate." This reinforces (rather than resolves) the RQ2/RQ6 point that self-reported adoption survey figures should not be pooled or averaged across sources with different recruitment.

**2. DORA 2025 (61% "agent mode never used"):** Same divergence and same likely explanation as above (population and wording). Worth flagging that DORA's broader/likely-more-representative sample reporting a *majority never using agents* at roughly the same time PragEng's newsletter sample reports a *majority regularly using* them is one of the starkest population-dependency findings collected so far in this research — a useful, concrete illustration for RQ6 of why adoption self-report figures need their recruitment population stated every time they are cited.

**3. Seniority-reversal hypothesis (§5 tension 5 — does E3 show seniors gaining more, reversing Cui et al.'s junior-gains-more E1 finding?):** PragEng's data is **directionally consistent with a seniors-adopt/benefit-more pattern in the agentic era**, but with three important caveats before treating it as a resolution of the tension:
- Supporting signal: agent adoption is highest at Staff+ (63.5%) and lowest among regular engineers (49.7%) and EM/leads (46.1%); Claude Code is more loved at Director level; senior/director respondents in Part 2 describe AI as an amplifier of existing expertise, while junior respondents describe it as stressful, expensive (higher token/AI bills), and requiring more rework ("triple checking and redoing").
- Caveat (construct mismatch): this is an **adoption and sentiment** pattern, not a **measured output/productivity** pattern — Cui et al.'s finding was about measured telemetry output gains (junior developers gaining 21–40% vs senior 7–16%, not statistically significant heterogeneity). PragEng offers no comparable measured-output breakdown by seniority; it cannot directly confirm or refute Cui et al.'s specific numeric claim, only the adjacent question of who adopts/likes the tools more.
- Caveat (non-monotonic by role): EM/leads show the *lowest* adoption (46.1%), below even "regular engineers" — complicating a clean "more senior = more adoption" story. This is more parsimoniously read as "engineering managers write less code, full stop" than as a seniority effect, and should not be smoothed away when this is cited.
- Caveat (self-report only, small anecdotal "10x" claim): the most eye-catching seniority claim ("10x more productivity benefit" for seniors) is a quoted anecdote from Part 2, not a survey statistic, and should never be cited as an effect size.
- **Net assessment:** medium-to-low confidence directional signal that, within this specific newsletter-reader population, seniority (at least on the IC/Staff+ track) correlates with higher agentic-tool adoption and more positive sentiment in the E3 era — a plausible complement to, not a proof of, a seniority-asymmetry reversal. It should be paired with a measured (non-self-report) E3 source with a seniority breakdown before being used to argue the reversal in the exec brief.

## Follow-up leads (not extracted — leads only)

1. **The paywalled 65-page full report** (linked from the main March 2026 post, "Takeaways and the full report" section) — likely contains the detailed cross-tabs (e.g. exact company-size × tool, or seniority × satisfaction breakdowns) only partially summarised in the free portion. Would need a paid subscription or an alternative access route to extract; escalate if Phase 2 wants to pursue.
2. **The Pragmatic Engineer 2025 Survey ("What's in your tech stack?", April–May 2025, n=2,997)** — https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey — the broader annual tech-stack survey referenced obliquely as a trend comparator; worth extracting separately if a clean 2025→2026 AI-adoption trendline from the *same* survey lineage is wanted, though note it is a broader survey (AI is one section, not the focus).
3. **Part 1 and Part 2 paywalled sections** ("Shipper benefits" onward in Part 1; "AI tooling 'addiction'" and Sections 6–7 in Part 2) — likely contain more seniority/satisfaction/limitation material relevant to §5 tension 5 and RQ3/RQ6; candidate for a paid-access follow-up extraction.
4. **Steve Yegge interview, "From IDEs to AI Agents"** (The Pragmatic Engineer podcast/newsletter) — turned up in the search for prior editions; a practitioner-interview companion piece that might corroborate or complicate the tool-ranking narrative; not checked for paywall status.
5. Independent secondary coverage seen during verification (not read in full, could serve as cross-checks): aiproductivity.ai's summary of this survey; Vinod Sharma's blog post "Claude Code Is the Most-Loved Developer Tool in 2026"; both merely restate the PragEng figures and would not add independent evidence, but could be checked for any additional free detail if the paywalled report remains inaccessible.

## Recency check notes

Main post is 3 March 2026 (4 months old at time of this extraction, 2026-07-06) — well within the 12-month window, so the mandatory supersession search was not strictly triggered, but a check was still run: no 2026-edition successor or retraction was found beyond the two companion "key trends" posts (April/May 2026) already incorporated above, and no critique or debunking piece targeting this specific survey was found during search. Given the pace of tool-market change this survey itself documents (Claude Code going from nonexistent to #1 in under a year), treat any of its tool-ranking figures as liable to be stale within months, independent of any formal supersession.
