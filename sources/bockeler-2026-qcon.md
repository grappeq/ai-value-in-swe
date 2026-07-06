# bockeler-2026-qcon — Böckeler, "AI Coding: State of the Game" / "State of Play: AI Coding Assistants" (QCon London 2026 keynote)

**source_id:** bockeler-2026-qcon
**Date verified:** 2026-07-06 (Phase 1 FETCH+EXTRACT)
**RQs fed:** RQ4 (cost trajectory claim — resolves the Uber cross-ref magnitude question, see below); RQ3 (security/failure-mode claim, thin); RQ6 (anti-metric aside on "lines of code")

## Citation chain (primary → secondary)

**Primary:** Birgitta Böckeler (Distinguished Engineer / AI-Coding lead, Thoughtworks), keynote **"State of Play: AI Coding Assistants,"** QCon London, delivered ~16–18 March 2026. Talk video (42:01) hosted on InfoQ: https://www.infoq.com/presentations/ai-coding-assistants/ — **not paywalled; fetchable with a transcript-level text extraction**, so this record is built from the primary talk content itself, not merely the news summary. QCon programme page: https://qconlondon.com/keynote/mar2026/state-play-ai-coding-assistants. She gave what appears to be the same-content talk again as **"State of Play: AI Coding Assistants,"** AI Native DevCon London, 1–2 June 2026 (YouTube: https://www.youtube.com/watch?v=tFffUnSq7VA) — confirmed via search snippet that the $380/day → $91,200/year figures recur unchanged in the June talk, i.e. no update or correction between March and June 2026.

**Secondary (triage source):** Olimpiu Pop, **"QCon London: AI Coding State of the Game: More Capable, More Expensive, More Dangerous Coding Agents,"** InfoQ, 22 March 2026. https://www.infoq.com/news/2026/03/ai-coding-state/ — a news write-up of the keynote, broadly accurate on the figures checked against the primary transcript (see below), but its framing omits the crucial provenance detail (that the $380/day figure is a Reddit-adjacent anecdote, not Böckeler's own data or an industry average) — a reader of the InfoQ piece alone would not know this.

**Independent secondary corroborating talk content (no cost figures):** Richard Speed / The Register, **"QCon London: AI for developers is in a 'dangerous state',"** 18 March 2026. https://www.theregister.com/2026/03/18/ai_for_software_developers_qcon/ — confirms the security/prompt-injection framing, the Yegge/Willison citations, and the "request limiting"/token-exhaustion theme, but **reports no dollar figures at all** — the cost-escalation numbers do not appear in this outlet's coverage, only in InfoQ's.

**No written Böckeler-authored article** (Thoughtworks blog, martinfowler.com "Exploring GenAI" memo series, or personal site birgitta.info) covering this specific content was found. Checked martinfowler.com/articles/exploring-gen-ai.html directly — the memo index exists but contains no section matching the cost or security claims; the QCon/DevCon talks are, as far as could be established, spoken-only content at the time of this extraction.

**Verdict: VERIFIED against the primary (talk transcript text), not merely the secondary news piece.** This is a rare case in this evidence base where the primary source itself was fetched and read, not substituted for.

## Tier, era, independence

- **Tier: C** — independent practitioner authority (Böckeler is a named, individually-credentialed Distinguished Engineer with a long public track record on this topic, not an anonymous vendor voice), speaking from direct observation of the field. **COI flag: mild.** Thoughtworks is a consultancy that sells AI-delivery advisory/implementation services; Böckeler's public profile-raising on this topic has commercial value to her employer, though the talk itself contains no product pitch, no Thoughtworks case study, and includes material that undercuts hype (she explicitly debunks the "12 cents/100 lines" metric as meaningless, flags rising costs and weekly security incidents as problems, not wins). This is a *lower*-COI profile than Uber's or a vendor whitepaper, but the flag stands per CLAUDE.md rule 7.
- **Era: E3** — the talk is explicitly about agentic coding tools (coding agents, "unsupervised for up to 20 minutes," agent swarms, Claude Code agent-teams preview, harness engineering). Confirmed E3 throughout.
- **Independence:** Böckeler is not paid by, or reporting for, any single tool vendor; she synthesises across the field (Cursor, Claude Code, Anthropic, OpenAI mentioned as subjects, not sponsors). No indication of vendor sponsorship of the talk itself.

## Figures with exact provenance — this is the load-bearing section for the RQ4 cross-ref

| Figure | Value | Exact basis (whose data, what population) | Original source per Böckeler | Measurement basis |
|---|---|---|---|---|
| 2024 baseline cost | "~12 cents per 100 lines of generated code" | **Not Böckeler's data.** Her own words: *"In the beginning of '24, I heard a keynote where the keynote speaker said, generating 100 lines of code only costs about 12 cents, compare that to a developer's salary."* Unnamed keynote speaker, unnamed event, no citation given. Böckeler immediately flags the metric as poor: *"Leaving aside that lines of code is of course not a good measure of value."* | Unidentified third party, relayed second-hand by Böckeler | Anecdote-of-an-anecdote; not a measurement she endorses |
| 2025/26 escalated cost | "~$380 USD per day" | **n = 1, self-reported, anonymous social-media post.** Exact words: *"This is from summer 2025, this is some websites where people post their token usage. There was this one person who was using, on average, $380 a day..."* No subreddit/platform named, no tool named (not confirmed to be Claude Code specifically — the source record's own triage notes assumed Claude Code, but Böckeler never names a tool for this figure), no verification that the poster's self-reported number is accurate. | An anonymous individual's own social-media disclosure of their personal average daily token spend | Self-reported by an unidentified individual; **not** an org average, not a client engagement, not Böckeler's own usage |
| Annualised figure | "$91,200 USD" | **Böckeler's own arithmetic extrapolation**, not a real annual cost anyone incurred: *"...which if you extrapolate that to 20 workdays a month, 12 months, would be a developer's salary of $91,200, which is not a bad developer's salary in Germany."* This is a rhetorical device (compare token spend to a salary) built on the single n=1 anecdote above, multiplied out. | Böckeler's own calculation, applied to the anonymous Reddit-type figure | Hypothetical extrapolation of a self-reported anecdote — two removes from any measurement |
| Security incidents | "Almost every week now there's some report of something happening," "usually all related to prompt injection" | Her own pattern-observation from following the field; no incident database, tracker, or report cited; no rate/count given beyond "weekly" | Böckeler's own synthesis of public reports she has seen | Impression/anecdotal pattern-noticing, not a measured incident rate |
| Illustrative security incident | An attacker used a crafted GitHub Issue (prompt injection) to extract secrets and push malicious packages to an npm registry, ~11 days before the talk | One specific, named-in-kind (tool unnamed: "this particular tool") incident, offered as an example of the weekly-incidents pattern above | Unnamed public report Böckeler is aware of; not sourced to a named outlet or CVE/advisory in the talk itself | Single incident, not independently traced to a primary advisory in this extraction |
| Productivity/delivery metrics | None | No velocity, DORA-style, throughput, or quality metric appears anywhere in the talk (confirmed via both InfoQ and Register coverage plus direct transcript fetch) | — | Absent — record as a null per CLAUDE.md rule 3 |

## Resolving the RQ4 magnitude discrepancy flagged by uber-2026-claude-cost

The Uber record's cross-ref (§3 of that file) asked whether Böckeler's ~$91k/year/dev figure describes a different population (frontier power users/agent fleets) than Uber's org-average, or genuinely conflicts. **Neither, precisely — the figure is not a population statistic at all.**

- Uber's $150–2,000/month range and he-2026's $42→$856/month are, whatever their other flaws (undisclosed methodology, single-interview provenance), at least framed as **populations**: an org-wide average, a power-user tier, a DiD-identified telemetry trend across "several hundred engineers."
- Böckeler's $91,200/year figure is **one anonymous individual's self-reported daily average from a token-usage-sharing website, in summer 2025, extrapolated by the speaker herself into an annualised "salary-equivalent" for rhetorical effect.** It has n=1, no verification, no named tool, no named platform, and the annualisation step never happened in reality — nobody spent $91,200 in a year; someone claimed to spend $380 on an average day, once, on a website.
- This makes the figure **strictly weaker evidence than Uber's**, not a different but comparable population. It should **not** be pooled, averaged, or placed on the same axis as Uber's or he-2026's figures in any evidence-table row or synthesis chart. The correct treatment is: Böckeler's figure is anecdotal colour illustrating that *extreme individual outliers exist and are visible enough to be talked about at conferences* — a qualitative point about the shape of the cost distribution's tail (consistent with, and probably the same underlying phenomenon as, the "heavy-usage tail" pattern the Uber cross-ref already identified from Uber's own power-user figure and He et al.'s ramp) — but it cannot itself be extracted as a comparable dollar figure.
- **Recommended evidence-table treatment:** if this figure is entered at all, it should carry `measurement_basis = self-reported`, population = "n=1, anonymous, unverified," and a note flag distinguishing it from the org-level figures. Better: exclude it from any quantitative RQ4 cost comparison and cite it only in prose as illustrative of "practitioner discourse has started noticing extreme outlier token spend, converging directionally with Uber/he-2026's heavy-tail finding, but this specific number is not independently measurable."
- The 12-cents/100-lines 2024 figure is even more removed (a second-hand recollection of an unnamed 2024 keynote) and should not enter the evidence table as a data point at all — it is useful only as color for "here is what the hype/discourse claimed at the start of this trend, which the speaker herself calls a bad metric."

**This resolves the escalation cleanly: it is not a conflict requiring a contradictions.md entry.** The apparent 4–15× gap dissolves once the figure's actual (anecdote → extrapolation) provenance is exposed — it was never commensurable with Uber's or he-2026's figures in the first place, and no stretching is needed to reconcile it. Recommend **not** adding a contradictions.md entry for this; instead a methodological note in the RQ4 synthesis memo about anecdote-extrapolation as a recurring source of inflated-looking cost figures in the discourse (useful given the 12-cents and $91,200 figures are both instances of the same pattern: single anecdote → arithmetic extrapolation → soundbite).

## What's original vs re-quoted (Böckeler's own observations vs citations of others)

**Original to Böckeler (her own framing/synthesis):**
- The risk-assessment framework for agent autonomy (probability × impact × detectability)
- Her critique of "lines of code" as a value metric (a useful, ready-made RQ6 anti-metric citation, though she offers no new data — just the standard critique)
- Commentary on review burden scaling with unsupervised agent run-length ("the longer it goes without supervision, the more I have to review afterwards")
- Her selection and synthesis of the cost/security anecdotes into a "more capable, more expensive, more dangerous" narrative arc

**Explicitly cited from named others (re-quoted, not her data):**
- Simon Willison — "lethal trifecta" concept (untrusted content exposure + private data access + external communication)
- Steve Yegge — "eight stages of dev evolution to AI," "Gas Town" framing
- OpenAI — "harness engineering" term; a five-month autonomous-greenfield-project observation about entropy (mentioned but not quantified in what was fetched)
- Cursor / Anthropic — agent-swarm experimentation; Claude Code's agent-teams preview feature

**Cited from unnamed others (re-quoted but not attributable further):**
- The 2024 "12 cents/100 lines" keynote speaker (unidentified)
- The summer-2025 token-usage-sharing website poster (unidentified individual and platform)
- The npm-registry prompt-injection attack (unidentified tool and outlet)

**Not present at all:** no mention of METR, DORA, GitClear, Faros, Stanford/Denisov-Blanch, Anthropic Economic Index, or Stack Overflow survey data anywhere in either the InfoQ news piece, The Register's coverage, or the fetched talk transcript excerpts. This source does **not** re-quote any source already in this evidence base (Uber, he-2026, Cloudflare) — it is an independent lineage of anecdotes and citations, which is itself worth noting: it neither corroborates nor contradicts those sources on specifics, only on the general "costs are rising and concentrated in a heavy tail" shape.

## Productivity/outcome claims — verdict: absent (null, recorded per rule 3)

No velocity, throughput, DORA-style, or quality-outcome metric appears anywhere in this talk, confirmed by three independent fetch passes (InfoQ news article, The Register, and the InfoQ presentation/transcript page). This is a pure cost-and-risk-focused keynote section; it makes no productivity claim to weigh against the costs and incidents it describes.

## What this can and cannot support

**Can support:** that a credible, independent, field-tracking practitioner (Böckeler) publicly synthesised, as of March–June 2026, a perception that per-developer AI-coding costs have risen sharply since 2024 and that security incidents tied to prompt injection in coding agents are being reported on a roughly weekly cadence; that "lines of code" is a poor value metric (a citable, if unoriginal, RQ6 anti-metric point); that this qualitative narrative ("more capable, more expensive, more dangerous") was consistent across two independent conference appearances three months apart without correction or update.

**Cannot support:** any specific dollar figure as a measured population statistic — the headline $380/day → $91,200/year figure is a single anonymous, unverified, self-reported social-media anecdote arithmetically extrapolated by the speaker, not an organisational cost, not an average, and not independently verifiable; the 12-cents/100-lines figure is a third-hand, unsourced recollection that the speaker herself discredits as a metric; the weekly-security-incident claim as a measured rate (no tracker or count, just an impression); any productivity or ROI claim (none made, in either direction).

## Cross-ref assessment (for orchestrator review — synthesis/contradictions.md NOT edited)

1. **vs. uber-2026-claude-cost:** see the dedicated resolution section above. No contradiction — the figures are incommensurable in kind (population statistic vs. extrapolated anecdote), not merely in scale. Recommend closing this cross-ref thread without a contradictions.md entry, but flagging the anecdote-extrapolation pattern in the RQ4 synthesis memo as a methodological caution, since it is likely to recur in other Tier C/D "cost" soundbites this research encounters.
2. **vs. he-2026-2x-mandate:** no direct figure-level comparison possible for the same reason; directionally consistent only in the general "heavy-usage tail exists and is large relative to baseline" shape, which he-2026's audited telemetry actually measures and Böckeler's anecdote merely illustrates. He-2026 remains the load-bearing RQ4 cost source; Böckeler is colour, not corroboration, for any specific number.
3. **RQ3/security:** this is the first source in the evidence base (as far as this extraction is aware) raising agent prompt-injection security incidents as a recurring operational failure mode. It is thin (no named report, no count, one example) but flags a genuine gap this protocol's E3 search directives (§6: "Security/defect analyses of agent-authored code merged to production") ask us to fill — recommend prioritising a dedicated search for the npm-registry/GitHub-Issue prompt-injection incident Böckeler references, and for Simon Willison's own "lethal trifecta" write-up, which is likely to be a more citable, better-sourced primary than this secondhand mention.
4. **RQ6:** the "lines of code is not a good value metric" aside is a low-cost, easy addition to the anti-metrics list, though it adds no new argument beyond what is already standard in this literature — do not let it stand in as a distinct triangulation point; it is restating a consensus view, not new evidence.

## Follow-up leads (not extracted)

- **Simon Willison's "lethal trifecta" blog post** — likely a well-documented, citable, independent practitioner primary source on agentic security risk; worth extracting in its own right for RQ3.
- **The specific npm-registry/GitHub-Issue prompt-injection incident** (~11 days before the March 2026 talk, i.e. approx. early-to-mid March 2026) — worth a targeted search to identify the actual advisory/report and the "particular tool" involved; currently unidentified in this extraction.
- **Steve Yegge's "eight stages of dev evolution" / "Gas Town" essay** — a practitioner primary source on agentic-era developer role change; potentially relevant to the skill-formation/cognitive-effects cross-cutting theme (CLAUDE.md/PROTOCOL §2) as well as RQ3.
- **OpenAI's unnamed "five-month autonomous greenfield project" observation about entropy** — mentioned only in passing in the transcript excerpt fetched; worth chasing to a named OpenAI publication if it exists, as it could be Tier D (vendor) evidence for RQ3/RQ5 (agent autonomy limits over long horizons).
- **The AI Native DevCon June 2026 talk** (https://www.youtube.com/watch?v=tFffUnSq7VA) — confirmed via search snippet to repeat the same $380/$91,200 figures unchanged; worth a full fetch only if a later, updated, or corrected version of these claims is specifically needed — no indication of substantive difference found in this pass.
- **The unnamed 2024 keynote speaker and the unnamed token-usage-sharing website/post** — both untraceable further without additional targeted search; flagging rather than chasing, given their evidentiary weight is already established as minimal (anecdote, not data).

## Recency check notes

Checked 2026-07-06. The InfoQ news article (22 March 2026) is ~3.5 months old; the primary talk (mid-March 2026) is of similar age — both well inside the CLAUDE.md rule 8 twelve-month threshold. A supersession check was run anyway: Böckeler repeated the same cost figures, apparently unchanged and uncorrected, in a second public talk in June 2026 (AI Native DevCon London), which is mild positive evidence that she has not walked back or updated the numbers, but also means no more-rigorous version of the underlying data has surfaced between March and June 2026. No retraction, correction, or rebuttal of either the cost figures or the security claim was found.
