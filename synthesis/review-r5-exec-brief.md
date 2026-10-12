# Independent review R5 — outputs/exec-brief.md and outputs/exec-brief-statements-draft.md

**Reviewer:** independent (not involved in producing either document, the evidence base, or the R5 clean-room). **Date:** 2026-10-12.
**Method:** (1) headline counts recomputed against `evidence/evidence-table.tsv`, `sources/` and `LEDGER.md`; (2) every factual or quantitative claim, and every bracketed grade or confidence, traced to its `sources/<id>.md` record and evidence-table row (rows cited as `L<n>` = line number in the TSV, header = L1); independence checked against the cluster map in `synthesis/rederivation-r4.md` §E (L71–L77, incl. the R5 correction on harness-evolution-2026); era checked by tool modality per PROTOCOL §2; tier and triangulation per PROTOCOL §3 and §8 (L209: "a claim may rest on Tier C alone only via the §3 triangulation rule (≥3 independent sources, labelled medium confidence at most); no claim rests on Tier D alone"); (3) the six 2026-10-12 corrections (LEDGER R5 section) checked for correct and consistent application in both documents; (4) every verdict label in the statements draft tested against its cited evidence strength and against the narrative brief's position; (5) editorial pass: word count, reading time, hedging, claim-widening. Items in `synthesis/review-r3-exec-brief.md` that have since been fixed are not re-raised; three that remain unfixed are marked "carried from R3".

---

## Verification of headline counts

- **"101 sources and 569 extracted findings"** (both documents) — **569 VERIFIED** (TSV has 570 lines = 569 data rows, 0 blank). **101 is the count of files in `sources/`, not of sources with findings:** 99 distinct `source_id` values appear in the table; the two without rows are the same two R3 excluded (`end-of-code-review-2026`, position paper; `ghaleb-2026-fingerprinting`, instrument validation). R3 accepted "74" (not 76) on exactly this convention; LEDGER now says "101 source records". Minor, but the convention changed silently (see N-M8 / S-M13).
- **"twenty-five cases of ... corrupting numbers"** — **VERIFIED.** `rederivation-r4.md` §E L75: 17 (R3) + eight new (#18, #19, #20, #23, #25, #26, #27, #28) = 25. The numbering runs to #30 because #21, #22, #29, #30 are an internal-inconsistency class "recorded, not counted" (L77), and the version-instability sub-pattern is explicitly "not counted above" (L76). The narrative's four examples (Bain phantom; Atlassian 45% vs 30.8%; Opsera "5×"; LinearB "4.6×" vs its PDF's 5.25×, L464; the Uber→Microsoft $2,000) are all within the 25. The statements draft's fourth example is not (see S-M2).
- **"Fewer than ten randomised trials, across five research programmes ... on working developers"** — **NOT TRACEABLE.** No synthesis file records this count (grep of `synthesis/`, `outputs/`, `LEDGER.md` finds it only in the two briefs). Recomputed from the table's method column: randomised productivity trials on working (non-student) developers are metr-2025-rct (L7), the METR late-2025 re-run (metr-2026-uplift L81–82 / metr-2026-design-change L288–289), peng-2023-copilot-rct, google-rct-2024, and cui-2024-copilot-field's three field experiments = **7 trials**. By the §E cluster map these are **three provenances** (METR; Microsoft–GitHub, since Peng and Cui share Peng and Demirer — `sources/peng-2023-copilot-rct.md` L5, L64; Google). "Nine trials / five programmes" is reachable only by adding shen-2026-coding-skills (comprehension trial, time a secondary outcome, Anthropic) and borg-2026-echoes (phase-2 maintainability, CodeScene/Equal Experts) *and* by counting Peng and Cui as separate programmes. See N-M2.
- **"Seven named organisations, three vendors"** / **"three vendors, six other companies"** — **VERIFIED**, consistent with each other. `tension-6` R4 addendum (L51): Agoda, Zendesk, the 2× firm, Cloudflare, Salesforce, Itaú, Duolingo; vendors Faros, DX, LinearB. The narrative's "six other companies" = seven minus he-2026. The statements draft double-counts he-2026 (S-m5).
- **"commits ~150% / +153% → releases ~20%"** — VERIFIED (demirer-2026, L403: commits +153.2%, releases +19.8%, E3 sync). "500,000 developers" VERIFIED (`sources/demirer-2026-writing-vs-shipping.md` L26: 521,329 with history).
- **he-2026 figures** — VERIFIED: 1.46–1.72× (L108), 1.99× by month 9 (L108), review coverage 89%→68%, substantive review ~halved, per-reviewer load 2.0×, org PR volume 3.1× (L111), AI PRs +22% total cycle vs comparable human PRs (L112), $42→$856/dev-month ≈20× (L113), post-2022 +44% vs legacy +12% n.s. (L110), placebo release (`sources/he-2026-2x-mandate.md` L39), "upper envelope" (L26).
- **METR** — −19% / believed +20% (L7–L9) VERIFIED; re-run −18% and −4%, both CIs crossing zero (L288–289), graded B (`sources/metr-2026-design-change.md` L74) VERIFIED.
- **Reviews** — 10,186 records, 2 of 16 productivity effect sizes E3 (`genai-productivity-meta-2026`, L133) VERIFIED; 45-paper review naming no agentic tool (`wittig-2026-fragmented-markers`, L371, L376) VERIFIED, but see S-m8.
- **Other figures verified:** Atlassian ~1.5×; Cloudflare $0.98 median/review (L124); CRA-only 45.20% vs 68.37% = 23.17pp (L166); 60.2% of 98 closed CRA-only PRs in the 0–30% signal band (L167); 83.21% human maintenance commits on AI files (L212) vs 69.6% self-agent fixes (L474), both AIDev; OR 1.62 and 4.5% day-30 incidence (L473); agent-maintainability up to −13.1pp (L154); arch-quality null-to-artefact (L270–L279); Borg null (L179); harness-evolution +52%/+131% tokens, +70% tokens per task, 300+ tests, all regressions passed CI (L537, L539); Anthropic 3% and the two misses (`sources/anthropic-postmortem-quality.md` L15–L18, L41); Gartner 25%/$200–500/month, 6% >$2,000, salary by 2028, DX $101–500/year modal at 38.4% (`sources/ai-spend-landscape-2026.md` L15–L16); Anthropic ~$6→$13/day (L17); Microsoft E+D division pullback (L18); Uber $1,500 per employee per tool (`sources/uber-2026-claude-cost.md` L52); ~400 companies, usage +65%, PR throughput +7.76% (L164); JetBrains 112% (L499); SO 2026 Claude Code 65.5% (L378), trust for important decisions 6.6% (L381); JetBrains Claude Code 39%, Copilot 29%→21% (L496–L497); dev-agent-misalignment DS3 0.07%, n=11 (`sources/dev-agent-misalignment-2026.md` L60, L161); LinearB pickup 5.25×, review 1.5× slower (L464–L465); Itaú lead time 15–20 days (`sources/one-developer-squad-2026.md` L51).
- **Word counts (computed with `wc -w`).** Narrative: **1,532 words** (1,459 from the first section heading to the end). Statements draft: **1,819 words**; 1,769 excluding the closing format note; 1,556 for the twenty claims alone. At 200–230 words per minute that is **~6.5–7.5 minutes** (narrative) and **~8–9 minutes** (statements) against the five-minute mandate. At normal formatting (~550–600 words a page with headings), that is ~2.6 pages and ~3.1 pages against the two-page cap. The narrative has grown by 40 words since R3 flagged 1,492 as too long.

---

## Findings — narrative brief (`outputs/exec-brief.md`)

### BLOCKER

None.

### MAJOR

**N-M1. "What exists for today's agents is one firm's causal study and a 500,000-developer activity study: real evidence, but not trials."** (L13) — understates the E3 measurement base, and so overstates scarcity.
- The table holds further quasi-experimental E3 productivity estimates on agents: `agents-vs-ides-2026` [A, E3, staggered DiD, commits +36.25%] (L98); `cursor-velocity-quality-2025` [A, E3, staggered DiD] (L135); `microsoft-cli-agents-2026` [B, E3 clean, synthetic control, +21.3% merged PRs] (L181); `quispe-2026-agentic-delegation` [B, E3] (L305); `quispe-2026-claude-frontier` [B, E3, Caltech, no COI] (L189). R3 MAJOR 4 named four of these. Under the §E cluster map they reduce to three provenances (Stanford–CMU: he-2026, agents-vs-ides, cursor-velocity; Microsoft–GitHub: demirer, microsoft-cli, quispe-delegation; Caltech: quispe-frontier), not two studies.
- **Fix:** "What exists for today's agents is quasi-experimental work from three research groups — one firm's causal study and open-source panels from the same Stanford–CMU lineage, Microsoft-data studies including a 500,000-developer activity panel, and one independent academic panel. Real evidence, but none of it a trial, and none of it measures delivery."

**N-M2. "Fewer than ten randomised trials, across five research programmes, have tested AI coding productivity on working developers — and none tested a mature present-day agent."** (L13) — count untraceable, world-scoped, and inconsistent with the cluster map.
- See the headline-count verification: 7 trials from 3 provenances on a strict reading; 9 from 5 only with Shen and Borg included and Peng/Cui split, a derivation no synthesis file records. "Have tested" is a claim about the world; R3's BLOCKER 1 fix was to scope the count to "our evidence base", and the genai-productivity-meta-2026 pool alone holds 10 RCTs (L133; some on students). Secondary: the METR re-run *did* test late-2025 agents (the brief says so two sentences later); what is true is that no trial measured one conclusively.
- **Fix:** "Our evidence base holds seven randomised trials of AI coding productivity on working developers, from three research groups; none measured a present-day agent conclusively." Record the derivation (trial list, inclusion rule, cluster assignment) in `rederivation-r4.md` or a dated R5 note so the count is traceable.

**N-M3. "Worst case: big, old, complicated codebases ... The one rigorous trial in that setting found people got slower [A, high on direction]."** (L27) — contradicts the brief's own 2026 update and its own action 1.
- L13 of the same brief: "the slowdown disappeared ... The −19% is out of date; nothing rigorous has replaced it". Action 1 (L52): "For old, complex codebases, don't assume either way". The re-run (L288–289, B) has point estimates in the speed-up direction. "High on direction" for a slowdown no longer holds; the statements draft (claim 2) correctly says "no demonstrated gain".
- **Fix:** "...The one rigorous trial in that setting found early-2025 agents made people slower [A]; a late-2025 re-run lost the slowdown but was inconclusive [B]. Treat it as 'no demonstrated gain', not as a proven loss."

**N-M4. "Invest in review and verification capacity, not just AI licences. That's the proven bottleneck."** (L53) — contradicts R5 correction (4).
- `tension-6` R5 note (L54–L55): HIGH that the bottleneck moved downstream, MEDIUM that it is *review specifically* (demirer measures no review time). The brief's own tag (L37) states the split; action 2 undoes it. The statements draft's claim 10 (PARTLY TRUE) and its action 2 ("review, verification and sign-off") are correctly calibrated.
- **Fix:** "That's where the bottleneck has moved — review, testing and sign-off; which of them binds for you is worth measuring."

**N-M5. "...the one exception is a single firm's study ... Uber's own COO says the productivity link 'is not there yet' [C, high on the pattern]."** (L21) — the "high" no longer survives R5 correction (7).
- RQ4 memo claim 2 (`synthesis/rq4-cost-profile.md` L34) earned "High" from "three independent organisations (he-2026, Cloudflare, Uber), each missing a different half". R5 correction (7) established that he-2026 publishes *both* halves. What remains for the absence pattern is Cloudflare (C, L125) and Uber (C) (plus the Microsoft E+D event, also C via press). That is Tier C alone, which PROTOCOL §8 (L209) caps at medium even with three independent sources. The R5 comparison (A2, `cleanroom-r5-comparison-L3-opus-by-opus.md` L250ff.) also recommended "medium". The RQ4 memo line itself was not updated.
- **Fix:** "[C, medium on the pattern]". Update `rq4-cost-profile.md` claim 2 accordingly.

**N-M6. "'AI is creating copy-paste spaghetti' — not supported for the older tools, mixed for agents: three measured studies from two groups found no duplication increase (the largest found AI-attributed code less duplicated), but the one agent-era re-analysis found significant increases in agent-first repositories."** (L48) — the era framing is wrong, and "the one" undercounts.
- Two of the three null studies are **E3**: `agents-vs-ides-2026` duplicate density AF +7.92% n.s. (L101, agent treatment) and `cursor-velocity-quality-2025` +7.03% n.s. (L138, E3). Only `mao-2026-code-metrics` is E2 (L183). So the "older tools" leg is one study, and the agent leg is the Stanford–CMU group disagreeing with itself on the same panel (`denisov-blanch-2026-ramp`, L420: +15.4% / +14.2%). A second agent-era source also finds more redundancy: `more-code-less-reuse-2026` [B, E3, AIDev, one repository] 1.87× (L250). As written, a reader infers the three nulls are pre-agentic.
- **Fix:** "...not supported for the older tools (one study found AI-attributed code *less* duplicated); for agents the evidence is mixed — one research group's estimates go both ways on the same data, and a single-repository study found more redundancy. A watch item, not settled either way."

**N-M7. "...three small studies — two randomised trials on students (one chat-era, one with an early agent) found a real comprehension cost"** (L56) — factual error on a primary record.
- `shen-2026-coding-skills`: "N=52 crowdworker-recruited developers ... ≥1yr Python experience, coding at least weekly ... majority 7+ yrs experience, NOT junior" (L172; `sources/shen-2026-coding-skills.md` L33). Only `impaired-programming-2026` is on students (L390). The error originates in `outputs/follow-up-questions.md` Q4 and `rederivation-r4.md` L29 ("both students") and has propagated. It runs *against* the finding's generalisability (Shen's sample is experienced). Secondary: "three small studies" names only two; and impaired-programming's comprehension cost is measured against a chatbot arm, not against no AI (L391).
- **Fix:** "...rests on two small randomised trials — one on experienced developers using chat-style AI, one on students using an early agent (compared with a chatbot) — both found a real comprehension cost...". Name or drop the third study. Correct Q4 and `rederivation-r4.md` L29.

**N-M8. Length.** 1,532 words, ~6.5–7.5 minutes and ~2.6 pages at normal formatting, against CLAUDE.md's "under 5 minutes; two pages hard cap". It is longer than at R3 (1,492). LEDGER R4 refers the cap to the human; this reviewer's view is that it is still breached.
- **Fix:** cut ~300–350 words. The cheapest cuts are in the quality paragraph (L41, ~190 words: compress the Anthropic and harness sentences into one), the review/maintenance paragraph (L39), and the RCT/scarcity paragraph once N-M1/N-M2 are fixed.

### MINOR

**N-m1. "...the lab has abandoned the design because developers now refuse to work without AI."** (L13) — *carried from R3 (item 12), unfixed.* Record: "30% to 50% of developers ... choosing not to submit **some** tasks" (L290). **Fix:** "...because enough developers now refuse to do some tasks without AI that the comparison broke down."

**N-m2. "One found something remarkable: experienced developers ... got 19% slower"** (L13) — the antecedent of "One" is now the previous sentence's "one firm's causal study and a 500,000-developer activity study", neither of which is METR. A non-engineer will attribute −19% to the wrong study. **Fix:** "The best-known trial, by the research lab METR, found..."

**N-m3. "Four studies paired what people said against what was measured. People were off by roughly 20–40 points"** (L19) — *carried from R3 (item 3), partly fixed.* The Stanford leg is "Not AI-specific; general self-assessment miscalibration" (`tension-1` L15) and measures percentile points; Stray yields a correlation (ρ≈0.17, L160), not a gap. **Fix:** "(three on AI gains, one on self-assessment generally)".

**N-m4. "[D — we use only the spread, not any single number]"** (L21) is attached to a sentence that quotes a single Tier D number: "Gartner forecasts AI coding spend passing an average developer's salary by 2028". A Tier D forecast is a single number by definition. **Fix:** drop the forecast, or tag it "[D, a forecast]".

**N-m5. "spend rose 20× for a 1.5–1.7× throughput gain"** (L21) — the spend is "Claude-only lower bound", Jul 2025–Apr 2026 (L113); the throughput is relative to a Jan–Apr 2025 baseline (L107–L108). Not a like-for-like ratio. **Fix:** "Claude-only spend rose ~20× over a period in which throughput rose ~1.5–1.7×".

**N-m6. "whole-organisation delivery barely moves: across ~400 companies, delivery rose about 8%"** (L35) — dx-reock's metric is **PR throughput** +7.76% (L164), not delivery; the brief elsewhere treats PRs as "output", not delivery. **Fix:** "pull-request throughput rose about 8%".

**N-m7. "two of the eleven kinds of software work (requirements, internal tooling) have no evidence at all, and architecture has only usage data"** (L31) — the DoD re-count says "all 11 task types carry rows — T1/T9 dry of outcomes" (`rederivation-r4.md` §F; e.g. SO 2026 tickets/requirements usage, L385); Q5 also records "zero measured agentic-era effect" for debugging (T8), and the R5 comparison (B4) recommended adding T10. **Fix:** "...have no outcome evidence at all; architecture and documentation have only usage data, and debugging has no agent-era measurement."

**N-m8. Header: "October 2026 (refreshed 11 Oct) · based on 101 sources"** — the brief was revised on 12 Oct (R5); 101 counts files, 99 carry findings (R3's convention). **Fix:** "(revised 12 Oct) · 99 sources (101 records)".

**N-m9. "'Developers report 2–3× gains' — a feeling, not a measurement; the feelings grow every year while the measurements don't."** (L45) — untagged; the trend rests on one weak-C survey with a retrospective item (metr-2026-survey: 1.3× Mar 2025 retrospective → ~2× Mar 2026, L162); "the measurements don't" sits uneasily with the brief's own best case (gains building over nine months, L25). **Fix:** "...a feeling, not a measurement [C, one survey]; self-reported multiples have risen faster than any measured gain."

**N-m10. "Small quality drops won't show on your dashboards either"** (L41) — widens two existence cases (vendor evals; one project's CI) to the reader's dashboards. harness-evolution-2026 "CANNOT support: the frequency or size of quality drift in production use" (`sources/harness-evolution-2026.md` L53). **Fix:** "Don't assume your dashboards would catch small quality drops either".

**N-m11. "A sobering new fact"** (L41) — the Anthropic postmortem entered at R3 (July). "New" is stale. **Fix:** delete "new".

---

## Findings — statements draft (`outputs/exec-brief-statements-draft.md`)

### BLOCKER

**S-B1. Claim 1: "'The productivity effect of AI coding agents has been rigorously measured.' Verdict: FALSE. Strength: high confidence in the absence"** — the lead verdict is not defensible from the programme's own grades, and it reverses R5 correction (2).
- PROTOCOL §3 defines Tier A as "RCTs, controlled field experiments, large-N telemetry with counterfactuals". The programme grades he-2026 Tier A E3 (L107–L114), agents-vs-ides-2026 Tier A E3 (L98) and cursor-velocity-quality-2025 Tier A E3 (L135), all productivity measurements of agents with counterfactual designs. By the programme's own definition, the effect *has* been rigorously measured, narrowly (one firm; open-source panels from one lineage). R5 correction (2) softened the narrative headline to "barely measured — never in a rigorous **trial**" because the R5 referee showed that the stronger wording "does not hold" (`cleanroom-r5-comparison-L3-opus-by-opus.md` row 15 and §A8). The statements draft reintroduces the stronger claim as its first verdict, at "high". The context line repeats N-M1's undercount ("one firm's causal study ... and a 500,000-developer activity study").
- **Fix:** restate the claim and verdict as "'Today's agents have been tested in rigorous trials.' **FALSE** (high)", or keep the claim and give the verdict as "**PARTLY TRUE** — measured with counterfactual designs at one firm and in open-source panels (three research groups); never in a conclusive trial; never on delivery outcomes (medium)". Apply N-M1's fix to the context line.

### MAJOR

**S-M1. Claim 1: "fewer than ten randomised trials exist across five programmes"** — same as N-M2: untraceable, world-scoped, and three provenances on the cluster map. **Fix:** as N-M2.

**S-M2. Claim 4: "twenty-five documented cases of numbers corrupted between source and citation: ... preprints whose headline effects moved 40–80% between versions."** — the last example is **not one of the 25**. `rederivation-r4.md` L76: "Version-instability sub-pattern (**not counted above**)". It is also not corruption "between source and citation": the source itself changed. The "40–80%" is Demirer's alone (`sources/demirer-2026-writing-vs-shipping.md` L154); Quispe's v1→v2 tripled. **Fix:** replace the example with a counted one (e.g. the Atlassian ~1.5× self-inflation, or InfoQ turning "for the most part, no" into "without increasing defect rates", #23). Keep version instability as a separate sentence: "separately, preprint headline numbers have moved by 40–200% between versions — cite the version."

**S-M3. Claim 7: "[B] telemetry and professionals' own suitability ratings (boilerplate 25:0, tests 19:2 suitable; legacy integration 3:17 unsuitable)"** — tier misgraded, self-report not separated, pre-agentic leg unlabelled, and the independence count is not given.
- The suitability ratings are `dont-vibe-control-2026`, **Tier C** (L542), open-coded survey responses (n=99, 6% response rate, L541). The record says they "support it as perception only, not measurement" (`sources/dont-vibe-control-2026.md` L62). The "[B] telemetry" is `stanford-denisov-blanch`, E1/E2-mixed and talk-grade, which the narrative labels "partly pre-agentic". It is in the same Stanford–CMU cluster as he-2026 (§E L71), so "[A] one firm ... plus [B] telemetry" is one voice. `tension-2` (L34) gives "medium".
- **Fix:** "Strength: [A] one firm (post-2022 +44% vs legacy +12% n.s.) and [B, pre-agentic] Stanford telemetry — one research lineage — plus [C, self-reported] practitioner suitability ratings. Medium."

**S-M4. Claim 12: "Strength: high on the pattern"** — same as N-M5. After the he-2026 exception, the absence pattern rests on Tier C alone and is capped at medium. **Fix:** "medium on the pattern".

**S-M5. Claim 14: "three measured studies from two groups found no duplication increase for older tools"** — **era mislabel** (CLAUDE.md evidence rule 5). Two of the three are E3 agent studies (L101, L138); only mao-2026 is E2 (L183). The "[B, one voice]" re-analysis is the same Stanford–CMU group on the same panel, and `more-code-less-reuse-2026` (L250, E3) is omitted. **Fix:** as N-M6. The UNKNOWN (mixed) verdict itself is defensible.

**S-M6. Claim 15: "'Our quality dashboards would catch an AI-driven quality drop.' Verdict: FALSE."** — the verdict asserts more than either source can carry. One leg is Tier D (against interest) about vendor evals. The other is one harness and one small open model about project CI, and its record says it "CANNOT support: the frequency or size of quality drift in production use" (`sources/harness-evolution-2026.md` L53). Neither tests dashboards. The narrative tags the lab leg "[A, lab, medium]". **Fix:** "**UNPROVEN — do not assume it.** Two documented cases (a vendor's evals; one project's 300+ tests) missed real regressions [D, against interest; A, lab]. Medium."

**S-M7. Claim 18: "two small randomised trials from independent groups, both on students, one with an early agent — comprehension lower (d>0.8) even where the agent arm was faster"** — two factual errors. Shen's sample is crowdworker-recruited working developers, majority 7+ years (L172). Shen's effect is **d=0.738** (L172; `sources/shen-2026-coding-skills.md` L39), so "d>0.8" holds only for impaired-programming (L391). Also, the "agent arm was faster" than a *chatbot* arm (L390), not than unassisted work. Shen is E2 chat, so a "pre-agentic" label is required (PROTOCOL §2; `rq3-failure-map.md` §4). **Fix:** "[A] two small randomised trials from independent groups — experienced developers with chat-style AI (pre-agentic; d≈0.74) and students with an early agent vs a chatbot (d>0.8) — both found lower comprehension; the agent arm was faster than the chatbot arm. Participants preferred the agent anyway."

**S-M8. Claim 19: "'Claude Code has become the default agent.' Verdict: TRUE (as an adoption fact). Strength: three non-overlapping self-report surveys in 2026 [C/D]"** — this falls below the triangulation bar. Stack Overflow 2026 is C (L378) and Pragmatic Engineer is C (L140), but JetBrains is **D** (L496). Two Tier C plus one Tier D does not meet "≥3 independent Tier C ... medium confidence at most" (PROTOCOL §3; §8 L209), and LEDGER R4 itself says "medium confidence". Secondary: "the same surveys show trust for important decisions at 6.6%" — only Stack Overflow reports that (L381). Also, "65% of agent users" is 65.5% of respondents to a mixed assistant/agent tool question (L378, "list mixes E1–E3 products"). **Fix:** "**LIKELY TRUE** (medium; self-reported adoption, two Tier C surveys plus one vendor survey)"; "one of these surveys shows..."; "65% of respondents using a coding assistant or agent".

**S-M9. No confidence level on most verdicts.** The how-to-read line promises tier, independent voices and era, but CLAUDE.md requires "high / medium / low with one sentence of justification". Claims 2, 5, 6, 7, 13, 14, 16, 17, 18 and 19 carry no confidence word. Claims 2, 4, 6, 8, 11, 12, 15, 17 and 20 give no voice count. Without confidence, the four-value verdict scale mixes up two things: "true at medium confidence" (claims 5, 7, 19 show as TRUE) and "partly true" (claim 13, also medium in tension 4, shows as PARTLY TRUE). A non-engineer cannot tell them apart. **Fix:** add "(high/medium/low)" to every verdict line, and either state the voice count in every entry or drop the promise from the how-to-read line.

**S-M10. Length, and the format note's own figures.** 1,819 words in total and 1,769 without the note: ~8–9 minutes and ~3 pages. The note's "The two-page cap is respected at ~1,500 words" is wrong on both counts, and "cutting to sixteen claims would bring it under 1,250" is arithmetically wrong: the claims average ~78 words, so cutting four leaves ~1,450–1,500. **Fix:** cut to 12 claims or fewer (≈1,000–1,100 words). The weakest candidates for cutting are 3 (it duplicates 20), 8, 16, 17 and 19. Correct the note.

### MINOR

**S-m1. Claim 2: "the famous −19% [CI +2%, +39%]"** — this mixes sign conventions: a negative point estimate with a positive interval. The record reports +19% completion time, CI [+2%, +39%] (L287). **Fix:** "19% slower [CI 2% to 39% slower]".

**S-m2. Claim 2: "the design was abandoned because developers refuse to work without AI"** — as N-m1.

**S-m3. Claim 3: "four independent paired designs, era-independent"** — as N-m3. The Stanford leg is general miscalibration and era-indeterminate (`tension-1` L15). Add the caveat.

**S-m4. Claim 5: "two voices, both E3, one of them Microsoft-funded"** — demirer-2026's funding is the Mack Institute and the Chicago AI Incubator (`sources/demirer-2026-writing-vs-shipping.md` L89). Microsoft supplied confidential data, and two of the three authors are paid Microsoft consultants (L88, L134). **Fix:** "one of them on Microsoft data with Microsoft-consultant authors".

**S-m5. Claim 9: "Seven named organisations, three vendors and the two measured studies"** — he-2026 is both one of the seven (tension-6 L51) and one of the "two measured studies", so it is counted twice. **Fix:** "Six further organisations, three vendors and the two measured studies".

**S-m6. Claims 5 and 9: internal construct contradiction.** Claim 5 says "output means commits and pull requests, not delivered software". Claim 9 then cites "~400 companies — delivery +8%", which is PR throughput (L164). **Fix:** "PR throughput +8%".

**S-m7. Claim 11: "most AI review comments carrying no usable signal"** — this undoes R3's fix (item 15). The measured unit is the PR: 60.2% of 98 closed CRA-only PRs fell in the 0–30% signal band (L167). Also "no organisation **anywhere** has documented..." is scoped to the world. **Fix:** "most AI-only-reviewed changes carried little usable signal"; "no organisation in our evidence base has documented...".

**S-m8. Claim 1: "two independent systematic reviews ... found two and zero agent-era productivity measurements respectively"** — wittig-2026's corpus includes Becker et al. 2025, the METR trial (L376), which this programme tags E3 (L7). So it found zero *named agentic tools*, not zero agent-era measurements. Its grade is "A-for-method (B for effects)" (L371). **Fix:** "found two agent-era measurements, and none that named an agentic tool, respectively".

**S-m9. Claim 16: "about 0.1% of observed ... episodes were hard to reverse"** — the record is **0.07%**, n=11, on the weakest-validated axis (judge accuracy 0.64) (`sources/dev-agent-misalignment-2026.md` L60, L161, L189). Rounding to 0.1% inflates it by ~40%. Separately, "FALSE as stated" judges a rate that the records say they cannot support (`sources/grigorev-2026-terraform-db.md` L74). **Fix:** "0.07% (11 cases)"; verdict "**UNSAFE WITHOUT GUARDRAILS — failure mode demonstrated; rate unknown**".

**S-m10. Claim 12: "pairs a 20× spend increase with a 1.5–1.7× throughput gain"** — as N-m5 (Claude-only lower bound, different windows).

**S-m11. Claim 8: "requirements and internal tooling have no measured evidence at all"** — "measured" makes this closer than the narrative's wording, but debugging (T8) also has no agent-era measurement (Q5), and documentation (T10) has no measured outcome (R5 B4). **Fix:** add both, or say "at least four task types".

**S-m12. Format note: "every verdict above maps onto a graded row ... a clean-room re-derivation ... reproduced 23 of 24 of these positions"** — this is claim-widening. The 24 clean-room rubric targets were the programme's tension, RQ and brief positions (`cleanroom-r5-comparison-L3-opus-by-opus.md` §5), not these twenty statements, several of which are new (claims 15, 16 and 19 as verdicts). Claim 1's verdict also maps onto a synthesis judgement, not a row. **Fix:** "...reproduced 23 of 24 of the programme's positions, on which these statements draw".

**S-m13. Header "101 sources"** — as N-m8.

---

## Cross-document consistency (claim by claim)

Correction checks first:

| R5 correction | Narrative | Statements |
|---|---|---|
| (1) Durability contested; "compound / be patient" removed | Applied (L25, L52) | Applied (claim 6, action 1) |
| (2) Scarcity wording softened; RCT count corrected | Heading softened; count changed but untraceable (N-M2); context undercounts (N-M1) | **Not applied** — claim 1 reverts to the stronger wording (S-B1); same count issue |
| (4) T6 split: high moved / medium review | Applied in tag (L37); **contradicted by "proven bottleneck"** (N-M4) | Applied (claims 9, 10; action 2) |
| (7) Spend exception (he-2026) | Applied in wording; "high on the pattern" not recalibrated (N-M5) | Same (S-M4) |
| (5) Duplication softened | Applied in verdict; era framing wrong (N-M6) | Applied in verdict; era explicitly wrong (S-M5) |
| (6) Incidents added | Applied, [C ×3], "contested" Amazon kept | Applied (claim 16); label over-reaches (S-m9) |
| (3) harness-evolution not a new voice | Consistent ("a lab study on different data") | Consistent ("two data provenances") |

Where the two documents disagree:

1. **Scarcity (statements 1).** Narrative: "barely measured — never in a rigorous trial". Statements: FALSE that it "has been rigorously measured", at high confidence. These are different claims, and only the narrative's survives the programme's own Tier A definition. → Align to the narrative (S-B1).
2. **Familiar-code slowdown (statements 2).** Narrative "Worst case": "found people got slower [A, high on direction]". Statements: "PARTLY TRUE (and dated) ... 'no demonstrated gain'". The statements position is the correct one; the narrative contradicts its own L13 and L52. → Align the narrative to the statements (N-M3).
3. **Is review the bottleneck (statements 10).** Narrative action 2: "the proven bottleneck". Statements: PARTLY TRUE, medium. → Align the narrative (N-M4).
4. **Maintenance cost (statements 13).** Narrative: agent-written code "carries a real maintenance cost ... [A, medium]", stated as fact. Statements: PARTLY TRUE. Tension 4 is "contested-but-substantiated, medium" on direction. The two positions are compatible only once the statements add a confidence word. → Statements: "**TRUE on direction (medium); size and defect translation unknown**" (S-M9).
5. **Dashboards (statements 15).** Narrative: "[A, lab, medium]" and "won't show on your dashboards". Statements: FALSE with no confidence. Both over-reach, the statements more so. → "Unproven — do not assume it" in both (N-m10, S-M6).
6. **Production access (statements 16).** The narrative gives no verdict ("existence proofs, not rates"). The statements give "FALSE as stated". → The statements should not judge a rate the records cannot support (S-m9).
7. **Best case (statements 7).** The narrative states the location claim without a grade; its bracket "[A/B, contested]" covers durability. The statements give "TRUE on direction" with a misgraded leg. Direction agrees; the grade needs fixing in the statements (S-M3) and adding in the narrative (a "[A/B, medium — one research lineage]" tag after "newer codebases").
8. **Claude Code as default (statements 19).** The narrative has no equivalent claim. The statements add a new TRUE verdict that falls below the triangulation bar (S-M8). → Either drop it (it says nothing about value, by the draft's own context line) or downgrade it to LIKELY TRUE (medium).
9. **Skill formation (statements 18 vs narrative footnote).** Same position (short-term comprehension cost, long term unknown). Both carry the "students" error (N-M7, S-M7).
10. **Duplication (statements 14 vs narrative bullet).** Same verdict (mixed / watch item). Both carry the era error, explicit in the statements and implied in the narrative.

All remaining claims agree in direction and confidence: statements 3, 4, 5, 6, 8, 9, 11, 12, 17 and 20 against the corresponding narrative passages.

---

## Verdicts and recommendation

**Narrative brief — GO-WITH-FIXES. 0 BLOCKER · 8 MAJOR · 11 MINOR.**
The brief remains unusually honest: grades travel with claims, nulls and absences are stated, Tier D figures are held to direction only, and most of the R5 corrections landed. Every count I could recompute holds except the new RCT count. The failures share one pattern: corrections were applied where the reviewers pointed, but surrounding sentences still assert the old position. "Proven bottleneck" sits beside the confidence split. "High on direction" for a slowdown sits beside "the −19% is out of date". "High on the pattern" stays after the exception that removed its third leg. The duplication bullet softened its verdict but kept a framing that makes agent-era nulls look pre-agentic. Add the untraceable RCT count, the undercount of E3 measurement in the scarcity paragraph, and the Shen population error, and none of these is fatal; all are sentence-level edits. The length problem has got slightly worse since R3 and needs a deliberate cut.

**Statements draft — NO-GO in its current form (GO-WITH-FIXES once S-B1 and the MAJORs are addressed). 1 BLOCKER · 10 MAJOR · 13 MINOR.**
The format is a genuine improvement for its purpose. A verdict word plus a strength line is faster to scan than prose, and it forces each claim to stand alone, which surfaced several things the narrative blurs (claim 2's "no demonstrated gain", claim 10's PARTLY TRUE). But a replacement executive document cannot lead with a verdict that reverses an R5 correction and contradicts the programme's own Tier A grading (S-B1). It also has errors the narrative does not: a corruption example the programme explicitly excludes from the 25, a Tier C survey promoted to [B], an explicit era mislabel, a new TRUE verdict below the triangulation bar, and wrong population and effect-size figures for the skill trials. Most verdicts also lack the confidence word that CLAUDE.md requires, so TRUE (medium) cannot be told apart from TRUE (high). At ~1,800 words it is further over the cap than the narrative, and its format note misstates its own length.

**Format recommendation: publish the narrative as the exec brief; keep the statements format as a companion, not a replacement.** The narrative does the job the mandate describes: a five-minute read that explains *why* (the bottleneck moved; self-report misleads; spend outruns evidence), and that is what a non-engineer needs to act. The statements format does a different job well: it is a reference card for the claims people will hear in meetings ("AI helps juniors most", "% of code by AI", "the bottleneck is review"). Once fixed, it should be published as a one-page appendix of about 10–12 claims, each with a confidence word. Keep the verdict labels; keep the narrative's position wherever the two currently disagree, except items 2 and 3 in the table above, where the statements draft is right and the narrative should move. Do not publish two documents that give different verdicts on the same claim: fix the narrative first, then generate the statements from it.

**Counts: narrative 0 BLOCKER · 8 MAJOR · 11 MINOR; statements 1 BLOCKER · 10 MAJOR · 13 MINOR.**

*Process note: the reviewer's brief said not to run git. One read-only `git log -1` on `outputs/exec-brief.md` was run by mistake while checking word counts; it changed nothing and nothing in this review depends on it.*
