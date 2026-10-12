# Independent Review (R5) — proposal, open questions, independence addendum, README and the R4/R5 internal records

**Reviewer role:** independent, not involved in production. **Date:** 2026-10-12. **Scope:** `outputs/internal-measurement-proposal.md`, `outputs/follow-up-questions.md`, `outputs/independence-crisis.md` (October 2026 addendum and count changes), `README.md`, and the records they lean on: `synthesis/rederivation-r4.md` (incl. §E R5 correction), the R4/R5 addenda in `synthesis/contradictions.md` and `synthesis/tension-verdicts/*.md`, the new addenda in `synthesis/rq3-failure-map.md` and `synthesis/rq5-translation.md`, and `LEDGER.md` (R4 gate summary, R5 section, DoD, batch log). Checked against `sources/*.md`, `evidence/evidence-table.tsv`, `PROTOCOL.md` §2–§3 and §8, `CLAUDE.md`. Cross-checked against `outputs/exec-brief.md` as corrected on 2026-10-12 where the task required it. No edits made to any reviewed file; no git commands run; no web access used.

**Method.** (1) Every count in the four outputs was recomputed from the table, the `sources/` directory and the ledger. (2) Every quantitative exhibit in the proposal's adopt/reject lists was traced to its source record, with particular attention to the three R4 additions. (3) Every status and sentence in the questions file was checked against `rederivation-r4.md` and the R5 corrections. (4) Each claim in the independence addendum was traced to a record; for the eight new corruption instances the test was the article's own stated standard ("Every example above has a source record and grading in this repository"). (5) Internal consistency across ledger, rederivation and outputs. (6) Editorial pass. Items fixed since the R3 review (`review-r3-other-outputs.md`) were verified as fixed and are not re-raised: the reject-metric #8 inversion, the "one of them pre-agent" wording, the "three months" window, the eight-vs-nine count, the 3%-attached-to-both-postmortems compression, the "16k agent-failure" label and the T8 "first evidence" phrasing all check out as corrected.

A large majority of claims verified exactly and are not listed below: all header counts; the he-2026 review figures (89%→68%, ~39→21%, 3.1× vs 1.5×, +22%); METR's <44% and +47%; the Stanford 14%/−9%/2.5× case; the r≈0.2 "death valley"; d=0.738; the 1.62× [1.10, 2.39] fix odds and 69.6%/27.4% split; 22.7% static-issue survival; the 0.07% / n=11 / judge 0.64 caveat; the +52%/+131%/−6.9pp/300+ CI harness figures; the 5.25× (1,055 vs 201 min) and 1.5×-slower LinearB figures; the 112% sum (47/38/27); the Demirer chain +153/+86/+47/+20 and the rev0→Sept drift (100k→500k, 40/140/180→30/180/240, projects 50→80, no change log); zhong's 1.02M PRs / 207 projects / −2.5 and −4.5 days per KLOC; the 291 conversations / 65 practitioners / median 11 rounds; Google Auto-Diagnose 90.1% vs 63.0%; CircleCI 70.8%→76.7%; Itaú 3 vs 6 sprints; the RAMP merger (v1 26 Aug 2026; Agarwal/He/Vasilescu + Denisov-Blanch/Koyejo; "estimator unchanged" per the record); the Uber 6× cost line; the dont-vibe suitability counts.

---

## Verification of counts

| Claim (where) | Recomputed | Result |
|---|---|---|
| 101 sources, 569 findings (README, brief, rederivation §F) | 101 files in `sources/`; 569 data rows in the TSV; 99 distinct source_ids with rows (end-of-code-review-2026 and ghaleb-2026-fingerprinting have none) | **Matches** ("99 with rows / 101 records" in rederivation-r4 is exact) |
| 25 sources + 2 drift checks, 207 rows in R4 (questions header, ledger) | 25 R4 source_ids in the Done table; those 25 account for **205** rows | **Consistent only if the two drift checks (dev-agent-misalignment-2026 v2, agent-maintainability-2026 v2) each added one row**; the table has no cycle column, so the 207 cannot be confirmed independently. Not a defect; worth a one-line note in the batch log |
| Tier A/B E3 share "33/54 = 61%; 30/54 = 56%" (ledger DoD, rederivation §F) | 54 sources carry at least one A/B row; 30 carry an A/B row tagged exactly `E3`; 35 carry one tagged with an E3-prefixed era | **Matches** at the 54 and 30 anchors; the 33 depends on three named boundary cases and is within the reviewer's 30–35 band |
| 6 adopt / 9 reject (README, brief, proposal, DoD) | Proposal table has 6 rows; reject list 1–9 | **Matches** |
| Corruption instances 17 → 25, "eight new" (addendum, brief, README, Q13, rederivation §E) | §E lists #18, #19, #20, #23, #25, #26, #27, #28 as counted (8); #21, #22, #29, #30 as internal-inconsistency (not counted); #24 and #31 as judgement cases (not counted). 17 + 8 = 25 | **Arithmetic matches; standard does not** — see findings I1–I3: one counted case has no source record, one contains an undocumented quotation, one is classified inconsistently with the addendum's own new sub-pattern. Defensible count as recorded today: 23–24 |
| "Five ... studies are now one provenance" (addendum) | he-2026, agents-vs-ides, cursor-velocity, stanford-denisov-blanch, denisov-blanch-2026-ramp | **Matches** (but see I7 on "agent-era" and "two biggest") |
| "seven named organisations, three vendor telemetry sets" (T6 R4 addendum; brief "six other companies") | Agoda, Zendesk, 2× firm, Cloudflare, Salesforce, Itaú, Duolingo = 7; Faros, DX, LinearB = 3 | **Matches** |
| "Fewer than ten randomised trials, across five research programmes" (brief, R5 correction 2) | Out of scope for this review; not recomputed | — |
| Brief length "~1,400 words" (ledger R4 gate) | `wc -w` = 1,532 after the R5 additions | **Stale** (see L4) |

---

## Findings

### A. `outputs/internal-measurement-proposal.md`

#### [MAJOR] P1 — "Not one published company" pairs cost with results: contradicts the R5-corrected brief

**Text at issue** (lesson 2, opening): "**Nobody pairs cost data with results data.** Not one published company."

**What the record says:** `LEDGER.md` R5 section, correction (7): "'publishes nothing about what the money bought' corrected — he-2026 pairs spend with throughput." `sources/he-2026-2x-mandate.md` finding 6: per-capita Claude Code spend "$42 to $856 per developer-month (Jul 2025–Apr 2026)" sits in the same paper as the 1.46–1.72× within-developer throughput estimate. The brief now reads: "the one exception is a single firm's study, where spend rose 20× for a 1.5–1.7× throughput gain."

The proposal was not revised after R5 and now contradicts its companion on the very claim R5 singled out. (rederivation-r4 §A(d) is not affected: it is scoped to *new* R4 sources.)

**Fix:** "Almost nobody pairs cost data with results data — one published firm does (spend up 20× for a 1.5–1.7× throughput gain), and everyone else publishes one or the other."

#### [MAJOR] P2 — Skill-formation text is stale after R4: "the one trial ... going no faster" and "two studies, both pre-agent era"

**Text at issue** (track #6): "The skill check follows the **one trial** showing AI-assisted learners understood significantly less (effect size d=0.738) **while going no faster**." And "Honest limits": "The skill-erosion check (#6) rests on deliberately thin evidence — **two studies, found incidentally, both from the pre-agent era**".

**What the record says:** `sources/impaired-programming-2026.md` (R4.1, Tier A-candidate, E3 agent arm): 54 students randomised; "Agent users were more accurate and quicker than chatbot users"; comprehension "p<0.002, Cohen's d>0.80". `rederivation-r4.md` §B Q4: "The theme now has two randomised legs from independent groups and its first agent-modality one." The brief's footnote was updated in R4 ("three small studies — two randomised trials ... one chat-era, one with an early agent ... the agent trial found speed gains alongside it"); rederivation §G lists only reject-metric exhibits as applied to the proposal, so the adopt-side text was left as of July.

As written, the proposal says there is one trial, that it found no speed gain, and that all evidence is pre-agentic — each now false, and each contradicted by the companion brief. The "while going no faster" clause is the practical hook (it is why the check is cheap to justify), and the agent-era trial found the opposite on speed.

**Fix:** track #6: "The skill check follows two randomised trials: one (chat-era) found AI-assisted learners understood significantly less (d=0.738) while going no faster; a second (early agent) found them faster and more accurate but again understanding less (d>0.8) — and preferring the agent anyway." Honest limits: "three small studies — two randomised trials on single sessions (one chat-era, one early-agent), neither on working professionals over time."

#### [MAJOR] P3 — The 112% exhibit rests on figures the source record says must be re-verified before exec-brief use

**Text at issue** (reject #4): "A 15,000-developer survey's self-reported shares (agent-written, AI-assisted, manual) add up to 112%." (Also in the brief.)

**What the record says:** `sources/jetbrains-2026-ecosystem.md` lines 8 and 66: "pages were read through the WebFetch summariser (small-model paraphrase), not as raw HTML ... **Re-verify exact numbers against the live pages before they reach the exec brief**"; "Every 2026 number is blog-only and unverified against the survey pages. Fetches were via a summariser; verify exact figures." The 47/38/27 means and the 112% sum are consistent across the record's two fetches and the post itself attributes the >100% sum to bucket midpoints, so the exhibit is probably right — but the extractor's explicit precondition for promotion to an output is not recorded as met anywhere (ledger, rederivation or record).

**Fix:** re-verify the three means against the live JetBrains post, note the verification in the source record, and keep the exhibit; failing that, drop it from the proposal and the brief (the "% AI-generated" point stands on `uber-2026-claude-cost` and `aidev-dataset-2026` without it).

#### [MINOR] P4 — Header date is July; content is October

**Text at issue:** "**July 2026** · companion to the exec brief". The document now carries three R4 exhibits (11 Oct 2026) and the brief it accompanies is dated "October 2026 (refreshed 11 Oct)".

**Fix:** "October 2026 (first issued July 2026; exhibits added 11 Oct) · companion to the exec brief".

#### [MINOR] P5 — "still growing at nine months" lacks the R5 durability caveat

**Text at issue** (pilot): "The 'dip then rise' story is plausible (gains in the best study were still growing at nine months) but no one has actually shown the rise follows a dip."

**What the record says:** `contradictions.md`, R5 entry "Durability of agentic gains": CONTESTED — "the same he-2026 record states the model-generation channel 'is not credibly identified' — a placebo release moved the outcome as much as real model releases; demirer ... attributes growth over time to model vintage, 'not learning'." The brief now carries this; the proposal's parenthetical still reads as if the nine-month growth were evidence of learning.

**Fix:** "(gains in the best study were still growing at nine months — though that study cannot tell practice from newer models)".

#### [MINOR] P6 — "directly caused" overstates a journalistic inference

**Text at issue** (reject #5): "one company's token leaderboard **directly caused** its budget blow-out."

**What the record says:** `sources/uber-2026-claude-cost.md`: "Root-cause mechanism (**self-report/journalistic inference, not measured**)".

**Fix:** "one company's own executives blamed its token leaderboard for its budget blow-out."

#### [MINOR] P7 — "turned out to be a data artefact" overstates a contested adjudication

**Text at issue** (track #4): "the era's biggest churn scare **turned out to be** a data artefact."

**What the record says:** `contradictions.md`, churn entry: "CONTESTED, leaning Side B"; "Dataset-composition drift is now a **live, unaddressed alternative** to an AI-driven churn increase." The brief no longer makes this claim.

**Fix:** "the era's biggest churn scare is contested and may be a data artefact."

#### [MINOR] P8 — Review-duration exhibit omits the condition under which it holds

**Text at issue** (reject #7): "in the largest agent-PR dataset, time under review did not predict whether a merge later needed a fix."

**What the record says:** `sources/who-finishes-the-job-2026.md` RQ4: pooled Cliff's delta for time under review is −0.221 (small, p<0.001 — *less* review time slightly associated with later fixes); the null (p=0.18) is the within-repository model with a PR-size control, in which commit count *did* predict (OR 6.1). "Largest agent-PR dataset" is also loose: the study uses a ≥500-star slice of AIDev-pop (6,774 merged agent PRs).

**Fix:** "in a large agent-PR dataset, once repository and PR size are controlled, time under review did not predict whether a merge later needed a fix — the number of commits did."

#### [MINOR] P9 — "taking weeks to surface" misplaces the delay

**Text at issue** (pilot): "user complaints were the alarm both times, **taking weeks to surface**."

**What the record says:** `sources/anthropic-postmortem-quality.md` line 27: "users reported Claude 'felt less intelligent' **essentially as soon as the change shipped** ... Anthropic's internal attribution and reversal took roughly five weeks"; total ~seven weeks to resolution.

**Fix:** "user complaints were the alarm both times — and it still took weeks for them to be attributed and acted on."

#### [MINOR] P10 — "proven in every study that ever checked" is a universal the base cannot carry

**Text at issue** (lesson 3): "What people say tells you nothing about what happened — **proven in every study that ever checked**."

**What the record says:** tension 1 verdict: four paired designs plus two new datapoint *kinds* in R4; confidence high on the operative claim. "Every study that ever checked" is a claim about the literature, not the base.

**Fix:** "shown in every study we found that paired the two (six so far)."

#### [MINOR] P11 — The 500,000-developer exhibit travels without its caveats

**Text at issue** (reject #2): "The largest study yet (500,000 open-source developers) saw agents raise commits ~150% while releases rose ~20%."

**What the record says:** `sources/demirer-2026-writing-vs-shipping.md`: the figures are the **sync (interactive) agent** arm (async: commits +61%, releases not estimated); Tier B; Microsoft telemetry with two paid Microsoft consultants as authors; "release" = GitHub Releases object; magnitudes moved 40–80% between revisions. The brief carries "[B; Microsoft data, figures unstable between revisions]"; the proposal carries nothing.

**Fix:** append "(interactive agents; vendor-supplied data; figures shifted between versions)".

---

### B. `outputs/follow-up-questions.md`

#### [MAJOR] F1 — Q4: "both students" is wrong for Shen & Tamkin

**Text at issue** (Q4): "Two randomised legs now, **both students**, both single-session, both finding the comprehension cost."

**What the record says:** `sources/shen-2026-coding-skills.md` line 33: "**Population:** N = 52 **crowdworker-recruited developers**. Inclusion criteria: ≥1 year Python experience, coding at least weekly"; tension 5 memo §4: "the sample was **majority-experienced by tenure (55.8% at 7+ years)**, not junior." Only impaired-programming-2026 is a student sample (54 CS students at two US colleges). The same error appears in `rederivation-r4.md` §B Q4 ("both students, both single-session") and in the exec brief's closing footnote ("two randomised trials on students") — an upstream R4 synthesis slip carried into two outputs.

This matters because Q4's *watch* ("any professional, longer-horizon study") is framed as if no professional sample exists; one does, single-session.

**Fix:** "Two randomised legs now — one on crowdworker developers (chat), one on students (agent) — both single-session, both finding the comprehension cost. *Watch: any longer-horizon study on working professionals.*" Propagate to rederivation-r4 §B Q4 and the brief footnote.

#### [MINOR] F2 — Q3(c) "two independent provenances" should say *data* provenances after R5

**Text at issue** (Q3(c)): "*Detectability — now two independent provenances*".

**What the record says:** `LEDGER.md` R5 (3) and tension 4 R5 correction: harness-evolution-2026 "shares two authors (Li, Hassan) with the AIDev papers. The detectability leg therefore rests on two independent *data* provenances ... not two independent voices." Q10's wording ("a lab provenance as well as a vendor one") is fine.

**Fix:** "now two independent *data* sources (one vendor postmortem, one lab benchmark whose authors overlap the AIDev group)".

#### [MINOR] F3 — No R5 line, although the new durability contradiction explicitly feeds Q9 and Q14

**Text at issue:** header "updated after refresh cycle R4 (2026-10-11 ...)"; Q9 and Q14 unchanged.

**What the record says:** `contradictions.md`, R5 entry: "Status: CONTESTED. Practice, model vintage and selection are confounded in every longitudinal source ... **feeds Q9 (J-curve) and Q14**."

**Fix:** add "R5 (12 Oct): durability of gains re-labelled CONTESTED — the nine-month rise in he-2026 cannot be separated from model vintage; this sharpens Q9's 'rise' half as well as its 'dip' half" to Q9, and a header note.

#### [MINOR] F4 — Q5 "a second source" undercounts T8

**Text at issue** (Q5): "Debugging (T8) gains a **second source** (Google's single-pass test-failure diagnoser ...)".

**What the record says:** T8 already carried zalando-2025-postmortems (C, E2), task-stratified-agents-2026 (fix-task split) and rca-failures-2026 (R3, lab). `rq3-failure-map.md`'s R4/R5 addendum says "a second **non-agentic** source", which is accurate (zalando + Google). The R3 review flagged the same kind of miscount on this item.

**Fix:** "gains a further non-agentic source".

#### [MINOR] F5 — Q8 presents the two favourable adoption patterns as the whole result

**Text at issue** (Q8): "AI-reviewer involvement cut time-to-decision by 2.5–4.5 days per KLOC while a process-quality proxy stayed flat or worsened."

**What the record says:** `sources/zhong-2026-agentic-review.md` line 30: Gradual −2.5 and Rapid Agent −4.5 (significant); **Rapid LLM −0.1 (not significant)** with more smells; line 36: "the three practices diverge sharply (Rapid LLM shows no speed gain and more smells)."

**Fix:** "cut time-to-decision by 2.5–4.5 days per KLOC in two of three adoption patterns (none in the third) while ..."

#### [MINOR] F6 — Q12 "price, usage and solve rate all held flat" over-specifies the design

**Text at issue** (Q12): "with the model, price, usage and solve rate all held flat".

**What the record says:** `sources/harness-evolution-2026.md`: a self-hosted open-weight model (no price variable) on a fixed 50-task benchmark (no usage variable); resolve rate shows **no trend** (ρ=0.208, p=0.231) but swings 23–39% between releases.

**Fix:** "with the model and task set fixed and no trend in solve rate".

#### [MINOR] F7 — Q2 "only on unfamiliar tasks" adds a word the record does not support

**Text at issue** (Q2): "drop code review **only** on unfamiliar tasks".

**What the record says:** `sources/dont-vibe-control-2026.md` line 23: "9 of 13 reviewed every change (all in own domain); 3 on unfamiliar tasks monitored outputs and rejected dependencies instead of reviewing code" — the three are the unfamiliar-task cases; nothing establishes exclusivity, and the record's own red flag (line 60) notes the title is stronger than the evidence.

**Fix:** drop "only".

---

### C. `outputs/independence-crisis.md` — October 2026 addendum

#### [BLOCKER] I1 — Instance #18 is counted as "at the same standard" but has no source record

**Text at issue:** "**The count is now twenty-five.** Eight new cases at the same standard: a newsletter headline ('Uber thinks Claude Code makes you 5% better') whose own body contains no 5%; ..."

**What the record says:** the article's standard, in its own closing line: "*Every example above has a source record and grading in this repository.*" Instance #18 exists only as a Rejected-table line in `LEDGER.md` (line 286): "headline figure appears nowhere in the post's own body — **candidate** corruption instance #18". There is no record in `sources/`; `sources/uber-2026-claude-cost.md` does not mention the newsletter; nothing records who read the post, when, or how the absence was established. By contrast #19 (the "ninefold" claim) has a verification record (`sources/github-2026-agent-scale.md`, "Do not use") and #20 is documented in `sources/stackoverflow-survey-2026.md`'s red flags — though both are also still labelled "candidate" in the ledger (lines 287, 310) with no adjudication step recorded.

A methods piece whose thesis is "trace the number" cannot carry a headline count that includes an untraced case. The 25 is repeated in the README and the brief.

**Fix:** either write a short verification record for the newsletter (as was done for #19) and promote #18, or drop it and restate the count as 24 everywhere (addendum, README, brief, Q13, rederivation §E, ledger R4 gate). Strike "candidate" from #19 and #20 in the ledger with a dated adjudication line.

#### [MAJOR] I2 — Instance #23 quotes a phrase ("halves wait times") that the source record does not contain

**Text at issue:** "a conference publisher's summary turning a speaker's 'for the most part, no' into 'without increasing defect rates' **and an 18-to-12-hour change into 'halves wait times'**".

**What the record says:** `sources/duolingo-2026-risk-bot.md` documents only the defect-rate framing gap (line 47: InfoQ summary "speeds up delivery without increasing defect rates" vs transcript "for the most part, no"; evidence row 92) and the 18h→12h series (line 32). No "halves", "half" or "wait" appears anywhere in the record. The phrase appears only in `rederivation-r4.md` §E and the ledger batch-3 line. 18→12 h is a 33% fall, so the claim would be a genuine corruption *if* the summary said it — but the base does not show that it did.

**Fix:** locate the phrase in the InfoQ summary and add it (with the quotation) to the source record's red-flags list and an evidence row; otherwise delete the clause and let #23 rest on the defect-rate inflation alone.

#### [MAJOR] I3 — Instance #28 is counted under a criterion the addendum's own new sub-pattern excludes

**Text at issue:** "... and a preprint whose abstract hardened from 'limited productivity change' to 'spurious' between versions with no new data." (counted, #28) — and two bullets later: "**New pattern: point estimates that move between preprint versions.** ... a second study's headline tripled between v1 and v2 (noted in July). Cite preprints by revision" (explicitly **not** counted, per rederivation §E: "Version-instability sub-pattern (not counted above)").

**What the record says:** `sources/fast-and-spurious-2025.md` line 8: "v1 -> v2 changes: new title; abstract reframed from 'limited overall productivity change' to ... 'perceived productivity gains may be spurious'" — the authors revising their own abstract. That is the same phenomenon as Quispe's v1→v2 headline tripling and Demirer's 40–80% drift (authors revising their own numbers), and the same as xu-2025's title escalation ("hedged→causal"), which was never counted in the original seventeen. The seventeen were all *third-party* distortions (press, aggregators, vendor marketing layers, DORA's paraphrase of its own prior construct being the closest edge case). #28 is the only author-own revision counted as "corruption in transit".

**Fix:** move #28 into the version-instability sub-pattern (count becomes 24, or 23 with I1), or state the criterion that makes an abstract reframing "transit" while a headline tripling is not. Whichever is chosen, apply it to xu-2025 as well.

#### [MINOR] I4 — "three widely circulated figures ... belong to two other vendors": four figures, and the trace is open in the record

**Text at issue:** "three widely circulated figures attributed to that vendor that belong to two other vendors".

**What the record says:** rederivation §E (#26) lists four: "+98%/+91%/+154%" and "1.7× issues per PR". `sources/linearb-2026-benchmarks.md` line 65: "not in this source and, **as I recall**, originate elsewhere (Faros AI; CodeRabbit). **Treat as misattributed until traced.**" The trace can be closed inside the base: `sources/faros-2026-whiplash.md` lines 112–114 cross-confirm +98% (PRs merged) and +154% (PR size) as Faros 2025 figures quoted in Faros's own 2026 PDF, and +91% (review time) as Faros blog/landing only; `sources/defect-rate-side-b.md` line 88 gives CodeRabbit's "~1.7x more issues". So "two other vendors" is right, "three" is not, and the linearb record still says "until traced".

**Fix:** "four widely circulated figures ... that belong to two other vendors (three to Faros, one to CodeRabbit)"; close the trace in the linearb record with the two cross-references.

#### [MINOR] I5 — #27 drops the record's hedge

**Text at issue:** "a survey vendor comparing its summer wave to 'a year ago' **when the comparator is** its own January wave".

**What the record says:** `sources/jetbrains-2026-ecosystem.md` line 29: "the 'a year ago' 29% is **plausibly** the January 2026 wave"; line 67: "**probably** a six-month comparison, or the post is using a different earlier wave without saying so."

**Fix:** "when the comparator appears to be its own January wave (the figures coincide; the post does not say)".

#### [MINOR] I6 — "three different percentages for one survey item" is two items

**Text at issue:** "three different percentages for one survey item" (#29).

**What the record says:** `sources/enterprise-ai-assistants-2026.md` lines 32–33: 44/57 = 77% vs "97.8% of the users who answered" are the *same* item (gain ≥25%) on two denominators; "88% perceived gains" is a *different* item (any gain) that conflicts with "13 of 57 (22%) little or no gain".

**Fix:** "percentages for its productivity items that cannot all be true of the same 57 respondents".

#### [MINOR] I7 — "the two biggest clusters merged" and "five ... agent-era studies"

**Text at issue:** "**One lab, many papers: the two biggest clusters merged.** The Stanford telemetry group and the CMU agent-quality group ... Five of the base's most-quoted agent-era studies are now one provenance."

**What the record says:** rederivation §E: the merged Stanford–CMU cluster has 5 members; the Microsoft–GitHub cluster has 7 (peng, cui, heilman, microsoft-cli-agents, quispe, demirer, hoffmann); the AIDev monoculture has at least ten members by the article's own body ("Ten of the sources ... stand on it"; 18 source records reference the dataset). Stanford–CMU is the third-largest. Of the five, `stanford-denisov-blanch` is a talk-grade record whose era is "E1/E2-dominant, unstratified" (tension 1 memo), not agent-era.

**Fix:** "two of the most-cited clusters merged" and "five of the base's most-quoted telemetry studies (four of them agent-era)".

#### [MINOR] I8 — Stale July counts in the body, now under an October addendum

**Text at issue:** header "July 2026"; "(74 sources, 362 extracted findings)"; §2 "Ten of the sources in our own evidence base stand on it"; Honest limits "the **seventeen** documented corruption cases are a lower bound".

**What the record says:** 101 / 569; AIDev-based records now include who-finishes-the-job-2026 (the body's "ten" is at least eleven); the count is 25 (or 23–24 after I1–I3). The short-version paragraph was updated to point at the addendum; the other three sentences were not.

**Fix:** one bracketed note at the head of the body ("Counts in the body are as of July 2026; the October addendum updates them") or update the three sentences.

#### [MINOR] I9 — Instance numbering catalogue in rederivation §E is incomplete

**Text at issue** (`rederivation-r4.md` §E): the counted list, the internal-inconsistency list (#21, #22, #29, #30) and "two judgement cases noted, not counted: Bowley's '1 in 20' (a p95 cut) and CircleCI's pooled 9× vs within-band ~4×" — unnumbered.

**What the ledger says:** batch 3 numbers "#24: CircleCI's '59%' is a heavy-tailed mean (median +4%) and Bowley's '1 in 20' is a p95 cut"; batch 5 numbers "#31 (CircleCI pooled-vs-banded ratio)". So numbers run #18–#31 (14): 8 counted + 4 internal + 2 judgement — arithmetically consistent, but §E omits #24's "59%" case and never gives #31 its number, so a reader cannot reconcile the ledger's numbering with the article's "eight".

**Fix:** in §E, label the judgement cases "#24 (CircleCI '59%' mean vs median +4%; Bowley p95) and #31 (CircleCI pooled 9× vs ~4× within band)".

---

### D. `README.md`

All counts verified (101 sources, 569 findings, twenty-five cases, six/nine, July–October dates, tier and era definitions matching PROTOCOL §2–§3). One item:

#### [MINOR] R1 — "The four final documents" vs five files in `outputs/`

**Text at issue:** "`outputs/` | The four final documents (start here)". `outputs/` contains a fifth file, `exec-brief-statements-draft.md`, written for human review in R5.

**Fix:** either move the draft under `synthesis/` or add "(plus one working draft of the brief in statement format, for review)". Note also that the README's "twenty-five documented cases" inherits I1–I3.

---

### E. Internal records — `LEDGER.md`, `rederivation-r4.md`, `contradictions.md`, tension verdicts, `rq3`/`rq5` addenda

The R5 corrections are in place where the R5 section says they are: rederivation §E carries the harness-evolution correction; tension 3 (dual label), tension 4 (R5 correction), tension 6 (confidence split) and the contradictions index all match the corrected brief; the durability entry is logged with both sides; rq3 and rq5 now carry dated R4/R5 addenda that are consistent with the corrected brief (rq3's "second data provenance" and rq5's "'review specifically' only at medium confidence" are both correct). Remaining items:

#### [MAJOR] L1 — Ledger header does not say where the research stands

**Text at issue:** "Phase: REFRESH CYCLE R4 COMPLETE (2026-10-11) — awaiting human review of the R4 gate summary below | Last session: 2026-10-11 (R4 complete)".

**What the ledger itself says two lines later:** an R5 section dated 2026-10-12 recording nine corrections "applied on the human's instruction", a 2026-10-12 batch-log entry, and a pending L3-fable run. The header's "awaiting human review" and "last session 2026-10-11" are both false. `CLAUDE.md`: "a human reading only LEDGER.md ... should be able to tell exactly where the research stands."

**Fix:** "Phase: R5 CORRECTIONS APPLIED (2026-10-12) — R4 gate reviewed; independent review of revised outputs in progress; L3-fable clean-room suspended | Last session: 2026-10-12".

#### [MAJOR] L2 — R4 gate summary and rederivation §B/§C still carry the two statements R5 corrected, without annotation

**Text at issue:** ledger R4 gate summary: "'standard testing does not see agent-quality drift' now rests on **two voices**" and "direction confidence raised to HIGH"; `rederivation-r4.md` §B Q3(c): "now two independent provenances ... this is no longer a vendor anecdote"; §C T4: "the detectability leg gains an independent lab provenance"; §C T6: "confidence on direction raised to HIGH"; §D item 3.

**What the record says:** R5 (3) "harness-evolution-2026 is not a new voice"; R5 (4) "tension 6 confidence split: high that the bottleneck moved, medium that it is review specifically". Only §E, tension 4, tension 6 and the index were amended. The gate summary is the document the human is asked to review, and it still states the pre-correction versions.

**Fix:** bracketed "[superseded by R5 (3)]" / "[split by R5 (4)]" notes at each location; no rewriting of history needed.

#### [MINOR] L3 — DoD line is stale

**Text at issue:** "R4 outputs NOT yet independently reviewed — decision requested." An R5 clean-room with two referees has since run and this review was commissioned.

**Fix:** "R4 outputs: clean-room re-derivation + two referees (R5); independent review of the other outputs 2026-10-12 (this file)".

#### [MINOR] L4 — "brief now ~1,400 words" is out of date

`wc -w` gives 1,532 after the R5 additions (destructive-incident cluster, durability caveat, spend exception). The two-page cap was already flagged for the human; the number they are deciding on should be current.

#### [MINOR] L5 — rederivation-r4 §B Q4 "both students" (see F1)

Same error at the synthesis layer; fix there so the questions file and the brief do not re-inherit it.

#### [MINOR] L6 — The 207-row claim is not separable in the table

205 rows belong to the 25 R4 source_ids; the two drift checks' rows cannot be distinguished from the pre-R4 rows of the same sources. Add "(205 new-source rows + 2 drift-check rows)" to the R4 gate summary so the arithmetic is auditable without git.

---

## Cross-document consistency

| Claim | Brief (corrected 12 Oct) | Proposal | Questions | Addendum / README | Records | Status |
|---|---|---|---|---|---|---|
| Cost paired with outcome | "one exception — a single firm's study" | "Not one published company" | — | — | R5 (7); he-2026 | **Conflict** (P1) |
| Skill-formation evidence | three studies; two RCTs (chat, early agent); agent trial faster | "the one trial ... going no faster"; "two studies, both pre-agent" | two randomised legs | — | impaired-programming-2026 | **Conflict** (P2) |
| Population of the two RCTs | "on students" | — | "both students" | — | shen = crowdworker developers | **All three wrong** (F1, L5; brief footnote) |
| Durability of gains | CONTESTED; cannot separate practice from models | "still growing at nine months" (no caveat) | Q9/Q14 unchanged | — | contradictions R5 entry | Gap, not conflict (P5, F3) |
| Detectability provenance | "A lab study on different data" | — | "two independent provenances" | — | R5 (3) | Wording gap (F2); gate summary says "two voices" (L2) |
| Tension 6 confidence | high moved / medium review | — | — | — | index + T6 memo split; rederivation §C and gate summary say HIGH | Annotation gap (L2) |
| Corruption count | twenty-five | — | twenty-five | twenty-five | 8 counted, one unrecorded, one undocumented phrase, one misclassified | **Count not at standard** (I1–I3) |
| Six / nine metrics | six / nine | six / nine | — | nine (README) | DoD 6/9 | Consistent |
| Dates | October 2026 | **July 2026** | October 2026 | July + October addendum | — | P4, I8 |
| Source/row counts | 101 / 569 | — | 25 + 2 / 207 | 101 / 569 | 101 / 569 / 205 (+2) | Consistent (L6) |
| Where the research stands | — | — | — | — | ledger header says awaiting R4 review | **Stale** (L1) |

---

## Editorial observations (no severity)

- The proposal still reads cleanly for a non-engineer and the R4 exhibits were slotted in without breaking its point-first style. The one dense spot the R3 review noted (spend row #5) is unchanged.
- The questions file remains internal-register, consistent with its "planning material, not findings" header; Q14 is a good addition and is correctly cautious about "release" as a construct.
- The independence addendum's register is right and its two new patterns are genuinely new; the problems above are all about the count and the standard, not the argument. The closing line ("if a number has a version history, name the version") is a worthwhile checklist addition — and is exactly the rule that makes I3 awkward, since the addendum then counts a version change as transit corruption.
- No hedging theatre found; the opposite tendency (small hardenings: "directly caused", "turned out to be", "proven in every study", "when the comparator is", "only on unfamiliar tasks") is the recurring pattern this cycle, and it is the mechanism the independence piece itself names ("shortening a claim quietly widens it").

---

## Verdicts

**`outputs/internal-measurement-proposal.md` — GO-WITH-FIXES.** Structure and the R3 corrections hold; the three R4 reject exhibits trace to their records (with the P8/P11 precision notes). Three MAJOR items block distribution as-is: the proposal now contradicts the corrected brief on cost-with-outcome (P1), is stale on skill-formation after R4 and again contradicts the brief (P2), and carries the 112% exhibit past a re-verification gate the extractor set in writing (P3). Eight MINOR items are wording.

**`outputs/follow-up-questions.md` — GO-WITH-FIXES.** Statuses match `rederivation-r4.md` throughout; all counts and nearly all figures verify. One MAJOR factual error (F1: Shen's sample described as students — an upstream R4 slip that also sits in the brief and the rederivation). Six MINOR precision items and the absence of any R5 line.

**`outputs/independence-crisis.md` (October addendum) — GO-WITH-FIXES, with the count held until the blocker is cleared.** The cluster-merger, AIDev self-contradiction and version-instability paragraphs verify against the records. The headline "twenty-five" does not meet the article's own standard: one counted instance has no source record (I1, BLOCKER), one quotes a phrase the record does not contain (I2), and one is classified by a criterion the addendum's own new sub-pattern contradicts (I3). The defensible count today is 23–24; whichever it becomes must be propagated to the README, the brief, Q13, rederivation §E and the ledger.

**`README.md` — GO.** Every count verifies; one MINOR (R1), plus the inherited corruption-count dependency.

**Internal records (`rederivation-r4.md`, `contradictions.md`, tension verdicts, `rq3`/`rq5` addenda, `LEDGER.md`) — GO-WITH-FIXES.** The R5 corrections landed where the R5 section says they did and the memos are consistent with the corrected brief. Two MAJOR ledger items: the header misreports where the research stands (L1), and the R4 gate summary and rederivation §B/§C still carry the two statements R5 corrected, unannotated (L2). Four MINOR.

**Counts:** 1 BLOCKER (I1) · 8 MAJOR (P1, P2, P3, F1, I2, I3, L1, L2) · 25 MINOR (P4–P11, F2–F7, I4–I9, R1, L3–L6).
