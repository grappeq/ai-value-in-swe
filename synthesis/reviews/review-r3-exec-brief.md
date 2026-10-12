# Independent review R3 — outputs/exec-brief.md

**Reviewer:** independent (not involved in producing the brief or the evidence base). **Date:** 2026-07-17.
**Method:** every factual/quantitative claim in the brief traced to its primary record in `sources/`, the evidence table, and the synthesis memos; internal counts recomputed; independence and era discipline checked against LEDGER.md's one-voice flags and PROTOCOL §2/§3/§8; then an editorial pass for the five-minute non-engineer reader.

## Verification of headline counts

- **"74 sources and 362 extracted findings"** — VERIFIED. `evidence/evidence-table.tsv` has 363 lines = 362 data rows; 74 distinct `source_id` values. The `sources/` directory holds 76 files; the two absent from the table (`end-of-code-review-2026`, a non-evidentiary position paper, and `ghaleb-2026-fingerprinting`, an instrument-validation record) carry no findings, so 74 is the defensible count.
- Claims that traced cleanly to primaries (sample): METR −19% with believed +20% and its [A, high] tag (`sources/metr-2025-rct.md`); the 2026 METR re-run's non-significant −18%/−4% estimates, design abandonment, and [B] grade (`sources/metr-2026-design-change.md`); the 10,186-record PRISMA screen (`sources/genai-productivity-meta-2026.md`); Gartner's 25% at $200–500/dev/month and 6% >$2,000, DX's seat-era $101–500/dev/year, the salary-crossing-by-2028 forecast (`sources/ai-spend-landscape-2026.md`); the Uber COO's "that link is not there yet" (`sources/uber-2026-claude-cost.md`); corruption count of seventeen incl. the phantom Bain report, Atlassian's 45%-vs-30.8% self-inflation (~1.5×, i.e. "by half"), Opsera's untraceable "5×", and the Uber-figure-laundered-onto-Microsoft case (`synthesis/cycles/rederivation-r3.md` §A Q13, `synthesis/rq/rq2-measurement-methods.md` §4, `synthesis/contradictions.md`); dx-reock's ~400 companies / +7.76% delivery vs +65% usage with the direction-only Tier D caveat correctly attached; Cloudflare's $0.98/review [C]; the 23.2pp CRA-only merge deficit [B]; the 83% human maintenance share [B]; the two genuinely independent Tier A quality legs (CMU complexity trio counted as one voice + `agent-maintainability-2026`); the Borg pre-agentic null [A]; the architecture null-to-artefact [B]; the T1/T2/T9 documented dry holes; the tension-5 "never statistically significant / two agent-era datapoints disagree" bullet (`synthesis/tension-verdicts/tension-5-seniority.md`); Nubank's 6M+ LOC monolith; and the bottleneck echo set ("two vendors and two other companies" = Faros, DX, Agoda, Zendesk per `synthesis/rq/rq5-translation.md` — genuinely outside the CMU cluster). The brief's independence discipline is, with the exceptions below, better than typical for this genre.

---

## Findings

### BLOCKER

**1. "In the entire world, only three rigorous (randomised) trials of AI coding *productivity* exist"** — over-scoped to the point of being factually wrong, and contradicted two sentences later by the brief's own source.
- The support is `synthesis/rq/rq2-measurement-methods.md` §2: "three on productivity outcomes **in the entire base**" (`metr-2025-rct`, `peng-2023-copilot-rct`, `google-rct-2024`) — a claim about this project's evidence base, not the world.
- The brief's own Tier A meta-analysis (`sources/genai-productivity-meta-2026.md`) pooled "14 primary studies (**RCT n=10**...)" on productivity — at least ten randomised productivity trials existed in the literature to Dec 2025 (mostly small lab/student RCTs, but randomised trials nonetheless). The same paragraph of the brief then cites that meta-analysis, so the internal contradiction is visible to a careful reader.
- **Fix:** re-scope, e.g. "Only three rigorous randomised trials have tested AI coding productivity on professional developers doing realistic work — and none tested a mature present-day agent" (Peng is a toy task, so safer still: "Our evidence base contains only three true randomised trials of AI coding productivity...").

**2. "The companion proposal lists six things to track and eight popular metrics to refuse"** — stale count.
- `outputs/internal-measurement-proposal.md` now says "**Nine** metrics to refuse" (R3 added reject metric #9, raw agent-PR merge rate — `synthesis/cycles/rederivation-r3.md` §D). "Six things to track" is correct.
- **Fix:** "eight" → "nine".

### MAJOR

**3. "Four separate studies compared what people *said AI did for them* against what was *measured*"** — a caveat the RQ2 memo says must travel does not travel.
- `synthesis/rq/rq2-measurement-methods.md` §3: "strictly three AI-specific pairings plus one general-calibration corroborant (the Stanford 43-developer exercise measures self-assessment accuracy generally, **not AI benefit specifically**; tension-1 carries this caveat and it travels here too)."
- Secondary: "off by 20–40 percentage points" clips METR's own ~39–43pp over-estimate, and the fourth design (Stray) yields a correlation (ρ≈0.17, ns), not a percentage-point gap.
- **Fix:** "Four separate studies paired self-report against measurement (three on AI gains specifically, one on developers' self-assessment generally). People were off by roughly 20–40 points..."

**4. "An independent screen of 10,000+ studies confirms the hole: only two productivity measurements exist for today's agent-class tools"** — the count is real but the scope is inflated.
- `sources/genai-productivity-meta-2026.md`: 2 of the meta-analysis's 16 productivity effect sizes are E3 — **within its pool, screened to Dec 2025**, and the era split is this project's own hand-classification ("era hand-classified by extractor", LEDGER.md), not the paper's claim. The project's own table holds further E3 productivity measurements the screen post-dates or excludes (`agents-vs-ides-2026` [A], `quispe-2026-agentic-delegation` [B], `microsoft-cli-agents-2026` [B], the METR re-run [B]).
- The careful formulation is `synthesis/cycles/rederivation-r3.md` §C.1: "a pre-registered Tier A meta-analysis screening 10,186 records **to Dec 2025** found only 2/16 productivity effect sizes... from agentic-era tools."
- **Fix:** "...confirms the hole: of everything it found worth counting, only two measurements covered today's agent-class tools."

**5. "code output tripled ... — and things actually took 22% *longer* to ship"** — the 22% belongs to a narrower comparison.
- `sources/he-2026-2x-mandate.md` §Key findings 4: the +22% is the **per-PR premium for AI-authored PRs vs comparable human PRs** (Table IV, post-mandate, controlling for author/month/size), likely understated per the authors' own auto-approval caveat. The organisation's *aggregate* cycle-time metric actually peaked and then receded — via routing work around substantive review, not faster shipping. (Note: `synthesis/rq/rq5-translation.md` carries the same compression; the primary record is authoritative.)
- As written, an executive will read "everything shipped 22% slower". The truth ("AI-written changes took 22% longer to ship than comparable human ones") is just as useful and shorter.
- **Fix:** "...and the AI-written changes took 22% longer to ship than comparable human-written ones."

**6. "when Claude Code's own maker shipped changes that measurably degraded its output by 3%, its internal testing missed it — twice, months apart"** — the 3% attaches to only one of the two misses.
- `sources/anthropic-postmortem-quality.md`: the 3% figure is "the only quantified effect size in the postmortem" and belongs to one of three product-layer bugs in the **April 2026** incident. The second miss (September 2025) was a different class of infrastructure bug (context-window misrouting peaking at 16% of Sonnet 4 requests, etc.), not a measured 3% drop. What genuinely happened twice: internal evals missed user-perceptible degradation, and user complaints were the detection channel both times.
- **Fix:** "...shipped changes that degraded its output — one drop later measured at 3% — its internal testing missed the degradation twice, months apart; user complaints were the alarm both times."

**7. "Anthropic's own per-day cost estimate doubled in three months with no price change"** — "in three months" is unsupported anywhere in the repo.
- `sources/ai-spend-landscape-2026.md` item 3: "The estimate **silently doubled** (~$6→$13/day) in April 2026, attributed by Anthropic to Opus 4.7 usage patterns with 'no pricing change'." No date is recorded for the prior $6 estimate; the evidence-table row (line 206) likewise carries no window.
- **Fix:** drop the timeframe ("doubled between successive published estimates with no price change") or source the prior estimate's date before asserting one.

**8. "Almost every famous number you've heard — '55% faster', '26% more output' — comes from old autocomplete tools timed on artificial lab tasks"** — wrong for the second named example.
- The 26.08% is `cui-2024-copilot-field` (Tier A, E1): randomised **field experiments** at Microsoft/Accenture measuring real weekly output, not a lab task. "Old autocomplete tools" is right; "artificial lab tasks" is not.
- **Fix:** "...comes from old autocomplete tools — the '55% faster' was a timed toy web server built from scratch — not today's agents doing real work."

**9. Skill-formation footnote lacks the pre-agentic label the protocol requires.** "one found a real comprehension cost from AI-assisted learning, with no speed benefit to offset it."
- The finding is `shen-2026-coding-skills` (RCT, d=0.738): **E2 chat, explicitly not agentic** — "era-transfer caveat applies" (LEDGER.md); `synthesis/rq/rq3-failure-map.md` §4: "do not carry it forward as agentic-era fact." PROTOCOL §2 requires every effect claim reaching the brief to be E3-backed or carry an explicit "pre-agentic" label. The footnote's "treat all claims as open questions" hedge mitigates but does not substitute for the label.
- **Fix:** "...(one found a real comprehension cost from chat-style AI assistance — pre-agentic tools — with no speed benefit to offset it)."

**10. Length breaches the brief's own bar.** The file is 1,492 words — roughly 6–7 minutes for a non-engineer at ~200–230 wpm, against CLAUDE.md's "readable... in under 5 minutes; two pages hard cap". At standard formatting 1,492 words plus headings is nearer 2.5 pages.
- **Fix:** cut ~250–350 words. Candidates: the second half of the opening paragraph (the "does not mean autocomplete beat agents" clarification can be one sentence), the parenthetical pile-up in "Three things" item 2, and the migration nuance paragraph (its point survives at half the length).

### MINOR

**11. "four studies found no duplication increase"** — two of the four (`agents-vs-ides-2026`, `cursor-velocity-quality-2025`) are the same CMU lab, one voice per `synthesis/tension-verdicts/tension-4-quality-debt.md` §4. Three independent groups is still ≥3, so the claim stands; say "four studies from three independent groups".

**12. "developers now refuse to work without AI"** — record: "30% to 50% of developers told us that they were choosing not to submit **some** tasks" without AI, and "an increased share" would not want to do 50% of their work without it (`sources/metr-2026-design-change.md`). Suggest "enough developers now refuse to do tasks without AI that the comparison group collapsed".

**13. "Uber capped spend at $1,500/month per developer"** — the cap is $1,500/employee/month **per agentic coding tool** (Claude Code and Cursor each; `sources/uber-2026-claude-cost.md`, Bloomberg-attested). Add "per tool" or the ceiling reads lower than it is.

**14. "Microsoft pulled its Claude Code licences over cost"** — one division (Experiences + Devices), not company-wide (`sources/ai-spend-landscape-2026.md` item 4). "Microsoft pulled a division's Claude Code licences" costs three words and stays accurate.

**15. "most of the review comments were noise"** — the measured construct is PR-level: 60.2% of closed CRA-only PRs fell in the lowest review-signal band (`synthesis/rq/rq3-failure-map.md` §3). "most of the AI reviews carried no usable signal" is closer.

**16. "clean, well-tested codebases"** — "clean" is evidenced (Stanford cleanliness R²≈0.40); "well-tested" has no supporting record I could locate (the nearest is Salesforce's verification-harness colour, C, COI-flagged, migrations-specific). Suggest "clean, newer codebases".

**17. "a genuine 1.5–1.7× throughput gain"** — the record is 1.46–1.72× (`sources/he-2026-2x-mandate.md`); rounding the conservative end up flatters slightly. "≈1.5–1.7×" or the exact 1.46–1.72 both fine.

**18. "[D, distribution-grade]"** — the only tag in the brief not covered by the how-to-read line, and a non-engineer cannot parse it. Say "[D — but we only use the spread, not any single number]" or gloss it.

**19. "Rare programming languages, messy codebases... do consistently badly [B, medium]"** — the rare-language and cleanliness evidence is Stanford talk-grade, era-mixed E1/E2-weighted (`LEDGER.md`); only the performance-work leg has clean E3 support (`task-stratified-agents-2026`). A "(partly pre-agentic evidence)" hedge would keep the era discipline consistent with the rest of the brief.

---

## Verdict: **GO-WITH-FIXES**

The brief is structurally honest to an unusual degree — grades travel with claims, nulls and absences are stated, Tier D figures are direction-only, the scarcity headline matches the ledger's invoked §8 clause, and the corroboration counts I checked (bottleneck echo set, the two independent quality legs, the seniority stalemate, the corruption count of seventeen) are genuinely supported. But two statements are factually wrong as written (the "in the entire world, only three randomised trials" escalation, contradicted by the brief's own meta-analysis source; the stale "eight metrics to refuse"), and a cluster of MAJOR items shows one consistent failure mode: compression that silently widens a claim's scope (the 22% cycle-time premium becomes "things took longer to ship"; the meta-analysis's pool-internal count becomes a world total; one incident's 3% becomes both incidents'; an undated doubling acquires a three-month window). Every fix is a sentence-level edit; none disturbs the brief's conclusions or structure.

**Readability assessment.** For its audience this is very good writing: point-first sections, plain words ("the bottleneck moved", "spending without checking what they get back"), consistent British spelling, a sober register that earns trust precisely because it keeps saying what is *not* known, and a tag system explained in one line and used consistently. Two genuine weaknesses: length (1,492 words is a 6–7-minute read against a 5-minute mandate, and past the two-page cap at normal formatting) and two overloaded sentences — the seventeen-corruptions sentence (~70 words, four dash-clauses) and the spend sentence in item 3 — each of which forces a second read and should be split. Trim those and the brief is the rare executive document that is both accurate and pleasant to read.

**Counts: 2 BLOCKER · 8 MAJOR · 9 MINOR.**
