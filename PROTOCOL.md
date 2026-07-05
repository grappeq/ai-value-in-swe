# AI Value in Software Engineering — Research Protocol v0.2

**Purpose:** Internal evidence base to shape AI strategy direction. Not for external publication — optimise for decision-relevance, honesty about uncertainty, and reusability, not citation polish.

**Decisions this must inform:**
1. Which task types to push AI adoption on (and which to explicitly deprioritise)
2. How to measure AI impact internally (what to instrument, what to stop trusting)
3. Exec narrative and expectation-setting (what we can credibly claim, what the hype gets wrong)

**Evidence bar:** Rigorous core (RCTs, telemetry studies) + graded practitioner signal. Everything gets a quality grade; nothing gets discarded for being anecdotal, but grades travel with claims all the way to the exec brief.

**Scope:** Full SDLC — requirements/specs, design, implementation, review, testing, debugging, deployment, operations/incidents. Excludes adjacent knowledge work (support, general docs) unless a source covers it incidentally.

---

## 1. Research Questions

- **RQ1 — Value map.** Where across the SDLC does AI deliver measurable value, broken down by task type? What are the effect sizes, and on which metrics (speed, throughput, quality, satisfaction)?
- **RQ2 — Measurement methods.** How was each result measured (RCT, telemetry, field experiment, self-report survey, case study)? How trustworthy is each method, and how large are the gaps between self-reported and measured outcomes?
- **RQ3 — Failure map.** In which task types is AI useless or net-negative? What *task characteristics* predict failure (codebase maturity, context requirements, implicit knowledge, verification cost)?
- **RQ4 — Cost profile.** What does cost look like per task type — licence/token spend, but also review overhead, rework, verification time, and quality debt? Where is the cost-to-value ratio favourable vs. inverted?
  *Pre-registered expectation:* literature-level cost data is thin — token spend and review-overhead numbers are rarely published. If RQ4 saturates at "insufficient evidence", that scarcity **is** the finding; report it as such rather than stretching Tier C/D sources to fill the gap.
- **RQ5 — The translation question.** AI demonstrably helps with prototypes, tech debt, and internal tooling. Does that translate into (a) velocity on new features in mature production codebases and (b) production quality/stability? Or does local task speedup fail to move system-level delivery metrics?
- **RQ6 — Internal measurement.** Given RQ1–RQ5, what should we instrument internally to know whether AI is working *for us*? Which popular metrics are misleading and should be avoided?

RQ5 is the strategic core — it directly tests whether the visible wins justify the exec-level velocity claims.

## 2. Task-Type Taxonomy

Every piece of evidence gets tagged against this taxonomy. Refine it during Phase 1 if sources use a better carving.

| Code | Task type | Notes |
|---|---|---|
| T1 | Requirements, specs, user stories | Includes acceptance criteria generation |
| T2 | System design, architecture | Design docs, ADRs, trade-off analysis |
| T3 | Greenfield / prototyping | New code, few constraints — the known sweet spot |
| T4 | Feature dev in mature codebases | Brownfield, high implicit context — the contested zone |
| T5 | Refactoring / tech debt | Migrations, dependency upgrades, dead code removal |
| T6 | Test authoring & maintenance | Unit, integration, e2e; test repair |
| T7 | Code review | AI-assisted review, PR summarisation |
| T8 | Debugging & incident response | Root-cause analysis, log interpretation |
| T9 | Internal tooling & automation | Scripts, dashboards, glue code |
| T10 | Documentation & knowledge | Code docs, runbooks, onboarding material |
| T11 | Ops / infra / CI | IaC, pipeline config, deployment |

Cross-cutting tags: developer seniority (junior/senior effects often diverge), codebase size/age, language ecosystem, and — critically — **tool era**:

- **E1 — Autocomplete era:** inline single-point suggestions (Copilot-classic); typical of ~2021–2023
- **E2 — Chat-assisted era:** ChatGPT/Claude in a side panel, copy-paste workflows; typical of 2023–2024
- **E3 — Agentic era:** multi-file, plan–execute–verify loops (Claude Code, Cursor agents, autonomous PR agents); typical of 2025+

**Era assignment rule:** tag by the **tool modality actually studied**, never by publication year — the year ranges above are heuristics only. A 2025 paper analysing 2023 autocomplete telemetry is E1; a late-2024 study of an early agent mode is E3. Where a study mixes modalities, tag each finding by the modality that produced it, splitting into separate findings if necessary.

**Era transfer rule:** the E2→E3 shift changed the task economics enough that findings do not transfer across it by default. E1/E2 evidence is admissible only as (a) historical baseline for trendlines, (b) evidence about *measurement methodology* (still valid — an RCT design doesn't age), or (c) evidence for plausibly era-independent effects (perception–reality gaps, bottleneck displacement, seniority asymmetry). Every effect-size claim that reaches the exec brief must rest on E3-era evidence or carry an explicit "pre-agentic" label. Tag every evidence-table row with era.

## 3. Evidence Tiers & Grading

**Tier A — Rigorous:** RCTs, controlled field experiments, large-N telemetry with counterfactuals. Carries claims on its own.
**Tier B — Structured observational:** Large-scale telemetry without randomisation, longitudinal industry reports (DORA-class), multi-company code-quality analyses. Carries claims with caveats.
**Tier C — Practitioner signal:** Engineering-org case studies with real numbers, credible engineering blogs, postmortems of AI rollouts. Used for mechanism hypotheses and colour, never as sole support for an exec-brief claim.
**Tier D — Vendor & consultancy:** GitHub/Microsoft/Anthropic/McKinsey-class publications. Always flag conflict of interest; use for directional signal and to understand the hype baseline the exec narrative must correct against.

Each source record gets: tier, independence (vendor-funded? population selection?), population (n, seniority, context), and a one-line "what this can and cannot support."

**Preprint substitution rule:** if a Tier A/B source is paywalled, an arXiv/SSRN/author-hosted preprint may substitute for the published version, provided the version difference (and any known changes between versions) is recorded in the source record. Escalate as BLOCKED only when no preprint or author copy exists.

## 4. Evidence Extraction Schema

One record per finding (a source can yield several). Store as rows in `evidence/evidence-table.tsv` — **tab-separated**, because effect sizes and confidence intervals contain commas:

```
source_id | year | tier | era | method | population | task_types (T1–T11) |
metric | effect_size | direction | measurement_basis (measured / self-reported / both) |
cost_data | seniority_split | codebase_context | independence_flags |
quality_notes | relevance_to_us (1–5)
```

Rules: record effect sizes exactly as reported, including confidence intervals where given; record *null and negative* results with the same diligence as positive ones; when a source reports both perceived and measured effects, capture both as separate rows (`measurement_basis` distinguishes them) — the delta is itself a finding for RQ2 and RQ6.

## 5. Tensions to Actively Stress-Test

These are the known fault lines in the literature (as of early 2026). The research should try to *break* the convenient narrative, not confirm it.

1. **Perception–reality gap.** The METR 2025 RCT found experienced open-source devs were ~19% *slower* with AI while believing they were ~20% faster. If replicated, this invalidates self-report surveys as impact evidence and is the single most important input to RQ6.
2. **Greenfield vs. brownfield split.** Early Copilot RCTs (Peng et al. 2023, ~55% faster) used standardized greenfield tasks; telemetry work (e.g., Stanford / Denisov-Blanch) suggests gains concentrate in low-complexity/greenfield code and shrink toward zero or negative in complex legacy systems. This is the crux of RQ5.
3. **Throughput vs. stability.** DORA 2024 associated rising AI adoption with *reduced* delivery throughput and stability; DORA 2025 reframed AI as an amplifier of existing organisational capability. Track how this evolved in 2026 data.
4. **Quality debt signals.** GitClear's multi-year analyses report rising code churn and duplication and declining refactoring in the AI era. Cross-check against defect-rate studies (e.g., Uplevel's contested +41% bug-rate finding).
5. **Seniority asymmetry.** Field experiments (Cui et al., Microsoft/Accenture) found gains concentrated in junior developers. Strategic implication differs radically depending on whether AI lifts the floor or the ceiling.
6. **Bottleneck displacement.** If code generation accelerates but review, verification, and deployment don't, local speedup should show up as review queue growth, not feature velocity. Look for direct evidence of shifted bottlenecks.
7. **Bad-metric traps.** Suggestion acceptance rate, lines of code, and "AI-generated %" are all gameable or meaning-free. Collect explicit critiques for the RQ6 anti-metrics list.

## 6. Anchor Sources (Phase 0 verification list)

Seeded from memory (early 2026); **verify every detail and expect 2026 publications to have superseded several of these.** Era tags in brackets; the E3 column is where Phase 0 search effort should concentrate.

**E3 / agentic-era (primary evidence base):**
- METR (2025) — RCT on experienced OSS developers using agentic tooling (the −19% study); search for replications, critiques, and METR follow-ups
- DORA 2025 report (+ 2026 if released) — AI-as-amplifier framing, throughput/stability trends
- GitClear 2025–2026 code quality reports — churn/duplication in the agentic era
- Stanford productivity group (Denisov-Blanch) — cross-company telemetry, latest waves
- Anthropic Economic Index 2025–2026 — task-level usage, automation vs. augmentation (Tier D)
- Stack Overflow Developer Survey 2025/2026 — adoption vs. trust trendlines

**E3 search directives (things that should exist by mid-2026 — go find them):**
- RCTs or controlled field experiments specifically on agentic tools (Claude Code, Cursor, Devin-class) rather than autocomplete — this is the biggest gap in the seed list
- Enterprise rollout case studies with real delivery metrics (Tier C) from 2025–2026: engineering blogs of large orgs reporting post-agentic DORA-style numbers
- Studies on AI-assisted code *review* and *incident response* — thin in the pre-2025 literature
- Security/defect analyses of agent-authored code merged to production
- Any published work on review-bottleneck displacement under agentic throughput

**E1/E2 — baseline & methodology value only:**
- Peng, Kalliamvakou, Cihon, Demirer (2023) — original Copilot RCT [E1; baseline only]
- Cui et al. (2024) — Copilot field experiments, Microsoft/Accenture [E1/E2; seniority-asymmetry evidence]
- Google internal RCT (~2024) on enterprise task time [E2; baseline]
- Uplevel (2024) — null velocity + bug-rate claim [E1; methodology-critique value]
- DORA 2024 — throughput/stability decline finding [E2; trendline anchor]
- SPACE framework & DX Core 4 — era-independent measurement inputs for RQ6

**Tier D standing set:** GitHub/Microsoft research, vendor whitepapers, consultancy reports — collect to characterise the hype baseline the exec narrative corrects against; COI-flag everything.

## 6.5 Per-RQ Query Plans

Seed queries per RQ. These are starting points, not a ceiling: refinements, dead ends, and productive variants get logged in the ledger's batch log so search strategy survives context resets. Default era filter: 2025+ unless explicitly hunting baselines.

- **RQ1 (value map):** `agentic coding tool RCT 2025 2026` · `AI coding assistant productivity controlled study telemetry` · `Claude Code Cursor Devin evaluation developer velocity` · `AI pair programming effect size task type`
- **RQ2 (measurement):** `perceived vs actual productivity AI developers` · `self-report versus telemetry software engineering measurement` · `METR developer study replication critique` · `developer productivity measurement validity AI`
- **RQ3 (failure map):** `AI coding assistant legacy codebase failure` · `brownfield code generation limitations study` · `task complexity moderator AI programming productivity` · `where AI coding tools fail empirical`
- **RQ4 (cost):** `AI code review overhead cost` · `rework rate AI-generated code` · `AI coding tool ROI total cost ownership study` · `verification cost AI-authored pull requests`
- **RQ5 (translation):** `AI adoption DORA delivery performance 2025 2026` · `feature velocity production codebase AI telemetry` · `system-level productivity AI local task speedup` · `AI code production incidents stability`
- **RQ6 (internal measurement):** `developer productivity metrics critique AI era` · `SPACE framework DX Core 4 AI measurement` · `suggestion acceptance rate metric criticism` · `engineering metrics anti-patterns AI adoption`

## 7. Execution Workflow (Claude Code)

**Workspace layout:**

```
ai-value-research/
├── PROTOCOL.md              # this file
├── CLAUDE.md                # agent instructions (grading rules, schema, tone)
├── LEDGER.md                # state: done / queued / blocked / rejected, per RQ
├── sources/                 # one .md per source: full notes + extraction records
├── evidence/
│   └── evidence-table.tsv
├── synthesis/
│   ├── rq1-value-map.md … rq6-measurement.md
│   └── contradictions.md    # where sources disagree and why
└── outputs/
    ├── exec-brief.md
    └── internal-measurement-proposal.md
```

**Phases:**

- **Phase 0 — Anchor verification (½ day).** Verify every anchor source, correct effect sizes, find 2026 successors. Output: corrected source list.
- **Phase 1 — Landscape sweep (1–2 days).** Per RQ, broad search from the §6.5 query plans; target ~25–40 sources total across tiers. Log everything into `sources/` with tier + task-type tags. Refine taxonomy if needed.
- **Phase 2 — Extraction (1–2 days).** Populate the evidence table. One finding per row. Capture perceived-vs-measured deltas explicitly.
- **Phase 3 — Contradiction hunting (1 day).** For each tension in §5, assemble the strongest evidence on *both* sides. Write `contradictions.md`. This is what makes the exec brief credible.
- **Phase 4 — Synthesis (1–2 days).** Per-RQ memos, each ending with "what this means for us" and a confidence level (high/medium/low) per claim.
- **Phase 5 — Outputs.** Exec brief (2 pages max: value map, failure map, the RQ5 verdict, expectation-setting corrections) and the internal measurement proposal (recommended instruments, anti-metrics list, suggested pilot design).

**Agent operating loop (per source):**

```
SEARCH → TRIAGE → FETCH → EXTRACT → GRADE → CROSS-REF → LEDGER → COMMIT
```

1. **SEARCH** against the current RQ's query plan (§6.5; era-filtered: 2025+ unless hunting baselines)
2. **TRIAGE** from title/abstract: relevance ≥3/5 and era tag assignable? If not, log one line in the ledger's rejected list and move on — no full read
3. **FETCH** full text. If paywalled and the source is Tier A/B: apply the §3 preprint substitution rule first; mark `BLOCKED` and escalate only if no preprint or author copy exists. Never extract from an abstract and present it as a full read
4. **EXTRACT** into `sources/<source_id>.md` using the §4 schema; one finding per record
5. **GRADE** tier, era (by modality, per §2), independence; write the one-line "can/cannot support" verdict
6. **CROSS-REF** against the evidence table: does this confirm, contradict, or extend an existing row? Contradictions get appended to `synthesis/contradictions.md` immediately, not at synthesis time
7. **LEDGER** update, then **COMMIT** with message `phase-N: <source_id> extracted` — one commit per source, so a killed session loses at most one source of work

**Loop control (what keeps it on track):**
- **Batches of 5 sources**, then stop: update ledger, write a one-paragraph batch summary in the batch log, and commit the checkpoint as `phase-N: batch <M> checkpoint`. Never more than 5 sources without a checkpoint
- **State lives in `LEDGER.md`**, not in the agent's context: done / queued / blocked / rejected, per RQ. Every session starts by reading PROTOCOL.md, CLAUDE.md, and LEDGER.md — this makes the work survive context resets and lets you kill and resume a session at any point
- **Saturation stop rule:** if 3 consecutive extractions *tagged with* an RQ (in extraction order, regardless of which other RQs those sources also fed) add no new claims and no new contradictions for that RQ, mark it `SATURATED` in the ledger with a one-line justification and move on
- **Phase gates are human gates:** the agent never advances a phase on its own; each phase ends with a summary in the ledger and a stop
- **Subagent extraction:** the orchestrating session dispatches one subagent per source for FETCH+EXTRACT, keeping the main context clean for cross-referencing — this matters most in Phase 2

**Escalation triggers (stop and ask):** paywalled Tier A/B source with no preprint; a contradiction that survives cross-referencing both full texts; a source that doesn't fit the taxonomy; any temptation to prune a §5 tension.

**Kickoff prompt for Claude Code:**

> Read PROTOCOL.md, CLAUDE.md, and LEDGER.md (create the ledger from the template in CLAUDE.md if absent). Execute Phase 0: for each anchor source in §6, verify it exists, correct citation and effect sizes, assign tier and era, and search for 2026 follow-ups or replications — prioritising the E3 search directives. Work in batches of 5, following the operating loop. Flag anything you could not verify as BLOCKED rather than guessing. Stop at the Phase 0 gate for my review.

Full agent instructions live in `CLAUDE.md` (drafted alongside this protocol).

## 8. Definition of Done

- Evidence table with ≥25 graded sources spanning Tiers A–D and ≥8 task types
- ≥60% of Tier A/B sources are E3-era; every exec-brief effect-size claim is E3-backed or labelled pre-agentic
- **Scarcity clause:** if a genuine search cannot meet the 60% E3 bar, do not grade-inflate tiers or era-inflate boundary studies to hit it. Record the shortfall in the ledger and report "the agentic era has not yet been rigorously measured" as a headline finding in the exec brief — scarcity is a result, not a protocol failure, and it directly informs decisions 2 and 3
- Every §5 tension has a written verdict: resolved, contested, or insufficient evidence
- RQ5 answered with an explicit confidence level and the strongest counter-evidence stated
- Exec brief contains zero claims resting solely on Tier C/D evidence
- Measurement proposal names ≤6 metrics to adopt and ≥3 popular metrics to explicitly reject
- RQ4 may close at "insufficient evidence" per its pre-registered expectation (§1) without blocking overall completion

## Scope Decisions (resolved)

1. **No proprietary/internal data.** External literature only; internal calibration is out of scope and, if ever wanted, a separate exercise.
2. **One-time research.** No refresh cadence; the ledger and evidence table make a future re-run cheap if the need arises, but none is planned.
3. **Cost evidence stays literature-level.** RQ4 reports cost findings as reported by sources (licence/token spend, review-overhead, rework) — no bespoke cost model scaled to org size.

## Changelog

- **v0.2 (2026-07-06):** renamed file to PROTOCOL.md; commits standardised to one per source + batch checkpoint; era assignment by tool modality, not year; preprint substitution rule for paywalled Tier A/B; evidence table switched CSV→TSV, `era` and `measurement_basis` columns added to schema; per-RQ query plans added (§6.5); saturation rule disambiguated for multi-RQ sources; DoD scarcity clause added; RQ4 thin-evidence expectation pre-registered.
- **v0.1:** initial draft.
