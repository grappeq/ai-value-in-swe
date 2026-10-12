# Independent review R5 — `synthesis/exec-brief-claims-companion-draft.md` (ten-claim companion)

**Reviewer:** independent (not involved in producing the companion, the brief, the evidence base or the earlier statements draft). **Date:** 2026-10-12.
**Method:** (1) each of the ten verdicts and its confidence word tested against the cited evidence strength, and against the corrected narrative brief `outputs/exec-brief.md` (revised 12 Oct) on the same point; (2) every number, bracketed grade, era label and independence count traced to `sources/<id>.md` and to its `evidence/evidence-table.tsv` row (cited `L<n>`, header = L1); independence checked against the cluster map in `synthesis/rederivation-r4.md` §E (incl. the R5 correction on harness-evolution-2026); era by tool modality (PROTOCOL §2); tiers and the Tier C triangulation / no-Tier-D-alone rules (PROTOCOL §3, §8); (3) headline counts recomputed (§H trial derivation; §E corruption ledger; `tension-1` and `tension-6` verdicts; `sources/` and the TSV); (4) every BLOCKER and MAJOR in `synthesis/review-r5-exec-brief.md` (statements-draft section) checked for resolution, plus the minors that could recur; (5) editorial pass: word count with `wc -w`, reading time, confidence legibility, claim-widening, the closing note. No file other than this one was edited; git was not run.

---

## Verification of counts

- **Seven randomised trials, three research groups** (claim 1) — **VERIFIED** against `rederivation-r4.md` §H: metr-2025-rct; the METR late-2025 re-run; peng-2023-copilot-rct; google-rct-2024; cui-2024-copilot-field ×3 = 7; METR / Microsoft–GitHub / Google = 3. Matches the brief (L13) word for word in substance. The inclusion rule is now on record, so the previous untraceability finding is closed.
- **Twenty-four corruption cases** (claim 3) — **VERIFIED** against §E (17 from R3 + #18, #19, #20, #23, #25, #26, #27; #28 reclassified to version instability). All four examples sit inside the 24: the Bain phantom report (`sources/bain-2026-benchmark.md`), Opsera's "5×" (`sources/opsera-2026-benchmark.md`), LinearB's "4.6×" (#25, `sources/linearb-2026-benchmarks.md`), Uber's cost figure re-attributed to Microsoft (`sources/uber-2026-claude-cost.md`; ai-spend-landscape-2026 L207). The version-instability "40–200%" sits in a separate sentence and is not presented as corruption (Demirer 40–80%, Quispe ×3, §E). "Each with a source record" holds (`outputs/independence-crisis.md` closing note and addendum).
- **Four paired designs, four independent voices** (claim 2) — **VERIFIED** against `tension-1` §2 and §5: metr-2025-rct (A), peng-2023 (A), stanford-denisov-blanch (B), stray-2026-nav (B). After the §E merger Stanford sits in the Stanford–CMU cluster, but none of the other three does, so the four voices survive. Caveat dropped (see m2).
- **Three vendors / six other companies** (claim 6) — **VERIFIED** against `tension-6` R4 addendum (seven organisations incl. he-2026; Faros, DX, LinearB). he-2026 is not double-counted this time.
- **Ninety-nine sources** — not stated in the companion. For the record: 99 distinct `source_id` values carry rows (VERIFIED). `sources/` now holds **102** records, not the 101 the brief's header gives: `astrolabium-2026-uber-5pct` (the #18 verification record added in R5) has no TSV row, like `end-of-code-review-2026` and `ghaleb-2026-fingerprinting`. Out of scope for the companion; the brief's "(101 records)" is stale by one.
- **Numbers traced and verified:** METR −19% / re-run inconclusive (L7, L288–289); he-2026 1.46–1.72× (L108), +44% vs +12% n.s. (L110), coverage 89%→68% and org volume 3.1× (L111), +22% total cycle (L112), $42→$856 ≈20× Claude-only (L113), "upper envelope" (`sources/he-2026-2x-mandate.md` L26); Demirer commits +153.2%, releases +19.8% (L399, L403), model vintage (L411); Uber COO "that link is not there yet" (L146, C weak end); Gartner 25% at $200–500/month and DX $101–500/year (L204–L205, D); suitability 25:0, 19:2, 3:17 (L542, C, self-reported); agent-maintainability up to −13.1pp (L154); cursor-velocity warnings/complexity persist (L136); who-finishes OR 1.62, 4.5% day-30 (L473); arch-quality null beyond growth (L270–L272); harness +52%/+131% tokens, resolve-rate drop, all passed CI (L537, L539); Anthropic two missed regressions (L332–L333, D against interest); JetBrains 112% (L499). No figure is wrong.
- **Tier D alone:** no verdict rests on Tier D alone. Claim 4's spend figures are context, tagged "[D, spread only]"; claim 10 pairs D with an A lab study.
- **Word count** (`wc -w`): **1,066 words** in total, comprising a header and how-to-read block of ~136, the ten claims ~870, and the closing note 57. At 200–230 words per minute that is **~4.6–5.3 minutes**, and ~1.8–1.9 pages at normal formatting (550–600 words a page).

---

## Findings

### BLOCKER

None.

### MAJOR

**C-M1. Claim 6: "'Writing code faster means shipping faster.' FALSE (high that the bottleneck moved; medium that it is review specifically)."** (L29–L30): the verdict label contradicts the evidence the entry cites, and the confidence attaches to a different proposition.
- The [B] leg it cites shows shipping *did* get faster: releases **+19.8% (SE 2.9)** for sync-agent adopters, stable across revisions (+20.2 → +19.8), and **+39.4% (SE 6.8)** for Claude Code adopters (`demirer-2026-writing-vs-shipping` L403; `sources/demirer-2026-writing-vs-shipping.md` L41, L43, L105). What the evidence shows is that shipping rises by a small fraction of the coding gain, not that it does not rise. "(high ...)" is the confidence that the *bottleneck moved* (tension-6 R5 split), not confidence that the claim is false. The brief's tag also carries "**low on size**" (L37), which the companion drops. A non-engineer will read "FALSE (high)" as "faster coding does not speed up shipping", which the cited 500,000-developer study refutes.
- The brief's heading ("writing code faster ≠ shipping faster") is equally terse, but its body says "releases only ~20%" and keeps "low on size". The companion inherits the heading but not the body.
- **Fix:** "**PARTLY TRUE — only a fraction carries through.** (High that the bottleneck moved downstream; medium that it is review specifically; low on size.) Strength: [B] commits +153% but releases +20% in a 500,000-developer panel; ..." Optionally align the brief's heading ("writing code faster ≠ shipping proportionally faster").

**C-M2. Claim 1 context: "what exists for agents is quasi-experimental work from three research groups (one firm's causal study; open-source panels; a 500,000-developer activity panel on Microsoft data)"** (L11). The count "three" is right but the list under it is wrong, and under the §E cluster map it collapses to two.
- §E (L71): he-2026 ("one firm's causal study") and the open-source panels agents-vs-ides-2026 and cursor-velocity-quality-2025 are **one provenance, Stanford–CMU**. The third group, the independent Caltech panel `quispe-2026-claude-frontier` (B, E3, L189), is missing. A reader will count three independent groups, when the list actually names two. The brief has the enumeration right (L13: "one firm's causal study and open-source panels from the same Stanford–CMU lineage, Microsoft-data studies including a 500,000-developer panel, and one independent panel").
- **Fix:** "...from three research groups: one firm's causal study plus open-source panels (one Stanford–CMU lineage); Microsoft-data studies including a 500,000-developer panel; and one independent academic panel."

**C-M3. Claim 9 context: "agents with production access have caused real damage in three organisations [C ×3] — existence proofs, not rates."** (L43). This drops the brief's "contested" on the Amazon case and asserts as fact a causal attribution that the named company disputes.
- `amazon-2026-outages`: the outage rows are C (L235, L237–L239), but Amazon's own attribution is "user error — misconfigured access controls" and "only one incident involved AI in any way... cause was unrelated to AI" (L236, L240, D). The brief keeps both sides ("Amazon's contested outages", L41). CLAUDE.md evidence rule 6 requires that both be presented. The other two (Replit/SaaStr, L244; Grigorev, L324) are uncontested.
- **Fix:** "...agents with production access have caused real damage in two documented cases, and are implicated in a third that the company disputes (Amazon) [C ×3] — existence proofs, not rates."

**C-M4. Length and the "One-page" label.** The header (L3) says "One-page companion". At 1,066 words the page reads in ~4.6–5.3 minutes and fills ~1.8–1.9 pages. That misses the four-minute target set for this review, and a non-engineer who reads the brief first (~1,470 words) faces about 12 minutes in total. The previous review's "≈1,000–1,100 words" target put a ten-claim card at two pages, not one, so this misses on the label rather than the arithmetic.
- **Fix:** either relabel it "Two-page companion" or cut ~250 words to reach ~800 (one page, under four minutes). The cheapest cuts: the how-to-read block (~100 words, which repeats the brief's tag legend; compress to two lines), claim 10's context (~45 words, which belong to the proposal), claim 8's last sentence, claim 4's spend-shape context (which is not about the claim), and claim 1's "Two independent reviews" sentence.

### MINOR

**C-m1. Claim 7: "UNKNOWN (contested)."** (L34) has no confidence word. "Contested" is a state, not one of CLAUDE.md's high/medium/low, so this is the one verdict that still falls short of previous item S-M9. **Fix:** "UNKNOWN — contested (medium that the evidence genuinely conflicts: three designs point different ways)".

**C-m2. Claim 2: "four paired designs, four independent voices [A/B], era-independent"** (L14) drops the brief's caveat "(three on AI gains, one on self-assessment generally)" (brief L19; tension-1 L15: Stanford's is "Not AI-specific; general self-assessment miscalibration"). This is previous item S-m3, unresolved. Also "era-independent" is the PROTOCOL §2 *candidate* category: three legs are pre-agentic and one is E3 (tension-1 §4). **Fix:** "four paired designs (three on AI gains, one on self-assessment generally), four independent voices [A/B]; three pre-agentic, one agent-era — the pattern holds across both."

**C-m3. Claim 1: "none of it measures delivery"** (L11) contradicts claim 6, which cites releases +20% (Demirer, L403) and AI changes taking 22% longer to ship (he-2026, L112). The brief has the same tension ("no delivery outcome", L13, against L37). **Fix (both documents):** "none of it measures delivery inside an enterprise pipeline end to end" or "only one measures releases, and only in open source".

**C-m4. Header: "every verdict traces to a graded row in `evidence/evidence-table.tsv`"** (L3). Claim 1's count and claim 3's 24 trace to synthesis derivations (`rederivation-r4.md` §H, §E), not to TSV rows. This is previous item S-m12 in a narrower form. **Fix:** "...traces to graded rows in `evidence/evidence-table.tsv` or to the recorded derivations in `synthesis/rederivation-r4.md` (§E, §H)".

**C-m5. Claim 4 context: "seat licences ... gave way to token bills ... for a quarter of leaders [D, spread only]"** (L23). "Gave way to" says seats were replaced. The D spread (L204–L205) shows a quarter of leaders on token bills, and the brief says "colliding with" (L21). The strength line also gives "pairs a ~20× Claude-only spend rise with a ~1.5–1.7× throughput gain", which drops the brief's "over a period in which" (the windows differ: L107–L108 vs L113; previous N-m5/S-m10). **Fix:** use the brief's wording in both places.

**C-m6. Claim 4 verdict: "'Companies know what their AI coding spend buys.' FALSE"** (L21–L22). The evidence is about *publication*: organisations that publish spend do not publish outcomes (`rq4-cost-profile.md` claim 2, L34). Only Uber's COO speaks to knowledge (L146). "FALSE" on "know" infers private ignorance from public silence. The strength line also reads "[C, two organisations plus press]", which leaves a reader unsure whether the ≥3-independent-Tier-C bar (PROTOCOL §3) is met. **Fix:** restate the claim as "Companies can show what their AI coding spend buys" (FALSE, medium), and write the strength as "[C, three organisations, one via press]" if the Microsoft E+D event (L207) is the third leg, or else name the third leg.

**C-m7. Claim 5 lists no counter-evidence** (L26). CLAUDE.md rule 3 requires nulls. `cursor-velocity-quality-2025` (A, E3, L135): month +1 commits +55%, back to ~0 by months +3–6, pooled ATT +2.63% n.s.; and the agents-vs-ides IF-cohort reversal (`tension-2` L19). TRUE (medium) still holds, but the entry reads as unopposed. **Fix:** add "Against: in one open-source panel the gain faded to zero within six months (see 7)."

**C-m8. Claims 5 and 6: "500,000 open-source developers (commits +153% ...)"** (L26, L30). The +153% and +20% are estimated on ~140,000 matched sync-adopter pairs (L399, L403) within a ~500,000-developer panel (`sources/demirer-2026-writing-vs-shipping.md` L14). The brief has the same compression. **Fix:** "in a 500,000-developer panel".

**C-m9. Claim 7: "several panels show gains fading within months [A/B]"** (L34). The two A panels that show fading (cursor-velocity L135; the agents-vs-ides IF cohort) are one Stanford–CMU provenance (§E L71). Demirer's Claude Code cohort "declines then stabilises", then rises (L411). That is two lineages at most, and the voice count is not given. The brief has the same wording (L25). **Fix:** "panels from two research lineages show gains fading or stalling within months".

**C-m10. Claim 10: "Strength: two documented misses on different data — the maker of Claude Code twice failed ... ; in a lab, routine tool updates ..."** (L46). The entry describes three misses from two sources. Context: "the companion proposal lists six things to track in cost/outcome pairs" is wrong on two counts. The proposal builds its six as "three cost/result pairs plus two safety checks" (`outputs/internal-measurement-proposal.md` L13), so not all six are pairs. And "companion" is ambiguous on a page that calls itself a companion. The 112% exhibit is Tier D (jetbrains-2026, L499) and untagged. **Fix:** "two sources (three documented misses)"; "the measurement proposal lists six things to track, built around cost/result pairs"; tag the 112% "[D]".

**C-m11. Closing note: "two small single-session trials found a comprehension cost"** (L51). This drops the comparator and era. Shen is chat-style, pre-agentic, against no AI (`sources/shen-2026-coding-skills.md`). impaired-programming-2026's cost is agent *versus a chatbot* (L390–L391). The brief keeps both (L56). The population and effect-size errors from previous S-M7 are gone, because the note now gives neither. **Fix:** "...two small single-session trials (one pre-agentic against no AI; one comparing an agent with a chatbot) found a comprehension cost".

**C-m12. Claim 8 verdict parenthesis: "PARTLY TRUE (medium — unanimous direction, size contested, one research lineage behind the sharpest numbers)"** (L38). "Unanimous direction" sits awkwardly beside PARTLY TRUE. The "partly" comes from the "worst on old, familiar code" half ("no demonstrated gain, not a proven loss"), and the parenthesis does not say so. **Fix:** "PARTLY TRUE (medium) — 'best on new code' holds in direction, one lineage behind the sharpest numbers; 'worst on familiar old code' is unproven."

*Out of scope, noted for the orchestrator (not counted):* (i) the brief's header "(101 records)" is now 102 (see counts); (ii) `outputs/independence-crisis.md` addendum still says "not counted in the twenty-five" (L111 region) after the revision to 24; (iii) `outputs/internal-measurement-proposal.md` L9 says the self-report gap was "shown in every study ... that paired the two (six so far)", while the brief and companion say four. Reconcile one way. tension-1's R4 additions are not self-report-vs-measured *productivity* pairs, and in impaired-programming self-rated understanding was accurate.

---

## Claim-by-claim consistency with the brief

| # | Claim | Brief position (outputs/exec-brief.md) | Companion position | Consistent? |
|---|---|---|---|---|
| 1 | Agents tested in rigorous trials | "barely been measured — and never conclusively in a trial"; 7 trials / 3 groups; quasi-experimental work from three groups, correctly enumerated (L13) | FALSE (high); 7 / 3; three groups mis-enumerated | **Verdict yes; context no** (C-M2) |
| 2 | Developers can tell you their AI gain | Four studies "(three on AI gains, one on self-assessment generally)" [A/B, high] (L19) | FALSE (high); four independent voices; caveat dropped | Yes, minus caveat (C-m2) |
| 3 | Press numbers reliable | 24 cases; trace to primary and version [high] (L20) | FALSE (high); 24; examples within the count | **Yes** |
| 4 | Companies know what spend buys | "spending without checking"; [C, medium on the pattern]; seat budgets "colliding with" token bills (L21) | FALSE (medium on the pattern); "gave way to"; window caveat dropped | Verdict yes; wording widened (C-m5, C-m6) |
| 5 | Agents raise individual output | "Individual coding gains are real"; best case [A/B, medium — one research lineage] (L25, L35) | TRUE (medium); two E3 voices | **Yes** (counter-evidence absent, C-m7) |
| 6 | Writing faster means shipping faster | "≠" heading; releases "only ~20%"; high moved / medium review / **low on size** (L33–L37) | FALSE (high moved; medium review); "low on size" dropped | Mirrors the heading but not the body; **the label is not defensible** (C-M1) |
| 7 | Gains compound — be patient | Durability "contested" [A/B, contested]; "measure whether yours persist" (L25, L52) | UNKNOWN (contested) | **Yes** (no confidence word, C-m1) |
| 8 | Best on new, worst on old familiar code | Best case [A/B, medium, one lineage]; worst case "no demonstrated gain, not a proven loss"; mechanical-change exception [C/D, low-medium] (L25–L31) | PARTLY TRUE (medium), with the same legs and the same exception | **Yes** |
| 9 | Agent code costs more to maintain | "real maintenance cost" [A, medium]; architecture null [B]; no bug-rate number; incidents incl. "Amazon's **contested** outages" [C ×3] (L41) | TRUE on direction (medium); size/defects UNKNOWN; "caused real damage in three organisations" | Verdict yes; **incident line widened** (C-M3) |
| 10 | Dashboards would catch a drop | "Don't assume your dashboards would catch small drops"; [D, against interest; A, lab, medium] (L41) | UNPROVEN — do not assume it (medium) | **Yes** |
| — | Juniors (omitted) | "never statistically significant ... contradict each other [not enough evidence]" (L46) | Same | **Yes** |
| — | Skill erosion (omitted) | two small trials with comparators and era given; open (L56) | Same position; comparators and era dropped | Yes, minus detail (C-m11) |

No companion verdict reverses a brief position. Two entries (6 and 9) drop a qualifier that the brief keeps.

---

## Previous-review items (statements draft, `review-r5-exec-brief.md`)

| Item | Issue | Status |
|---|---|---|
| S-B1 | Lead verdict reversed R5 correction (2) | **Resolved.** Claim restated as trials, FALSE (high), now defensible. A new error in its context line (C-M2). |
| S-M1 | Untraceable RCT count | **Resolved.** 7 / 3 per §H, scoped to "our base". |
| S-M2 | Corruption example outside the counted set | **Resolved.** All examples inside the 24; version instability separated. |
| S-M3 | Tier C survey graded [B]; pre-agentic leg unlabelled; one lineage | **Resolved.** [C, self-reported], [B, pre-agentic], "one research lineage". |
| S-M4 | "High on the pattern" for spend | **Resolved.** Medium. |
| S-M5 | Duplication era mislabel | **Resolved.** Reduced to "mixed for agents and a watch item"; no era claim on the nulls. |
| S-M6 | Dashboards verdict over-reach | **Resolved.** UNPROVEN (medium), "Neither tests dashboards". |
| S-M7 | Skill-trial population and effect size wrong | **Resolved by removal** of both figures. Comparator and era now missing (C-m11). |
| S-M8 | Claude Code "default" TRUE below the triangulation bar | **Resolved.** Claim dropped. |
| S-M9 | Missing confidence words | **Largely resolved.** Nine of ten carry one; claim 7 does not (C-m1). TRUE (medium) and FALSE (high) are now visibly distinct, and no TRUE carries "high". |
| S-M10 | Length | **Partly resolved.** 1,819 → 1,066 words, but still ~5 minutes and ~2 pages against a "one-page" label (C-M4). |
| S-m3 | Stanford caveat on the paired designs | Not resolved (C-m2). |
| S-m4 | "Microsoft-funded" | Resolved ("on Microsoft data"). |
| S-m5 | he-2026 double-counted | Resolved ("six other companies"). |
| S-m7 | AI-review signal unit | Resolved ("where measured, carried little usable signal"). |
| S-m10 | 20× vs 1.5–1.7× windows | Partly ("Claude-only" added; window caveat lost, C-m5). |
| S-m12 | Traceability claim widened | Partly (narrower, still overstated, C-m4). |

---

## Verdict

**GO-WITH-FIXES. 0 BLOCKER · 4 MAJOR · 12 MINOR. Publish in `outputs/` next to the brief: not in its current form. Yes once the four MAJORs are applied.**

The rebuild did what it set out to do. Every blocker and major from the previous review is resolved or, in one case (length), much reduced. The headline counts (7 trials / 3 groups, 24 cases, 4 paired designs, 3 vendors / 6 companies) all trace to recorded derivations. Every number I traced is correct. Tier D never carries a verdict alone. No TRUE verdict sits above medium. No verdict reverses the corrected brief. What remains is the pattern the previous round found in the brief: a qualifier that the source keeps goes missing in compression. Claim 6's FALSE label is the substantive one, because the study it cites shows releases rising a significant 20% (40% for Claude Code). The correct verdict is "partly true — only a fraction carries through". The other two MAJORs are sentence-level: claim 1's list of the three research groups collapses to two under §E, and claim 9 drops "contested" from a disputed attribution to a named company. The last is honest labelling: either cut ~250 words or stop calling it one page. None of the fixes needs new evidence. After they land, a spot-check of claims 1, 6 and 9 is enough, with no full re-review.
