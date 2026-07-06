# Research Ledger
Phase: 0 | Gate status: OPEN
Last session: 2026-07-06 | Last commit: phase-0 batch 1 checkpoint (see git log)

## Done
| source_id | RQ | tier | era | batch |
|---|---|---|---|---|
| anthropic-economic-index | RQ1 | D (COI: vendor self-analysis) | E2/E3 split by surface | 1 |
| metr-2025-rct | RQ1, RQ2 | A | E3 (early IDE-agent; boundary caveat) | 1 |
| stanford-denisov-blanch | RQ1, RQ3, RQ5 | B (talk-grade figures) | E1/E2-mixed; 2026 wave E3 | 1 |
| gitclear-2025 | RQ3, RQ4 | B (COI: vendor telemetry) | E1/E2 trendline; 2026 edn E2/E3 (gated) | 1 |
| dora-2025 | RQ5, RQ2 | B (vendor-adjacency flag) | E1/E2/E3 mixed, weighted pre-agentic | 1 |
| google-rct-2024 | RQ1 | A (COI: Google-on-Google; headline 21% non-significant in main model) | E1/E2 boundary, autocomplete-dominant | 2 |
| stackoverflow-survey-2025 | RQ2 | B (topline-percentages survey; self-selection; reverse-COI noted) | E1/E2/E3 mixed; agent sub-items E3 | 2 |

## Queued
| source_id / search target | RQ | priority |
|---|---|---|
| METR Feb 2026 uplift update (57 devs, 800+ tasks; METR judge wave unreliable but expect improved speedup) — reinterprets metr-2025-rct | RQ1, RQ2 | high |
| METR "forthcoming" autonomous-agent evidence (per arXiv:2507.09089 §4.1) — search target | RQ1 | medium |
| METR critiques roundup (Zvi Mowshowitz; The Experimentalist) | RQ2 | medium |
| DORA "ROI of AI-assisted Software Development" 2026 interim (v2026.01, Apr 2026) — J-curve model, "instability tax" | RQ4, RQ5 | high |
| DORA 2025 critiques/analyses (RedMonk, InfoQ, getDX) | RQ2, RQ5 | medium |
| DORA 2026 annual report — re-check September 2026 (does not exist as of Jul 2026) | RQ5 | note |
| arXiv 2507.10422 — peer-reviewed 151-repo churn study (contradicts gitclear-2025 churn leg) | RQ3 | high |
| arXiv 2606.21804 "Is Agent Code Less Maintainable Than Human Code?" — direct E3 quality test | RQ3 | high |
| arXiv 2603.28592 "Debt Behind the AI Boom" | RQ3, RQ4 | medium |
| GitClear Jan 2026 "Top Performers" piece | RQ1 | low |
| arXiv:2607.01904 "AI Writes Faster Than Humans Can Review" (Denisov-Blanch co-auth., Jul 2026; 802 devs, 196k PRs, diff-in-diff, E3) | RQ5, RQ1 | high |
| Denisov-Blanch Dec 2025 "inflection point" artefact + ASE 2026 repo-AI-config paper — search targets | RQ3, RQ5 | medium |
| "Ghost engineers" critiques (Jellyfish, HN) — anti-metrics material on the Stanford model | RQ2, RQ6 | low |
| OpenAI/NBER "How People Use ChatGPT" (WP 34255) — comparable vendor usage index, Tier D baseline | RQ1 | low |
| Economic Index methodology critiques (Strauss; Empiricrafting) | RQ2 | low |
| Stack Overflow 2026 survey results — re-check ~Q4 2026 (collection opened 23 Jun 2026, no results yet) | RQ2 | note |
| SO "Closing the developer AI trust gap" post (Feb 2026) | RQ2, RQ6 | low |
| Peng et al. 2023 Copilot RCT (baseline) | RQ1 | medium |
| Cui et al. 2024 field experiments (seniority) | RQ1, RQ3 | medium |
| arXiv:2601.13597 "AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents" — potential E3 RCT (fills the biggest §6 gap) | RQ1 | high |
| arXiv:2510.24265 "The Fast and Spurious: Developer Productivity with GenAI" | RQ2 | medium |
| arXiv:2601.20112 "Usage, Effects and Requirements for AI Coding Assistants in the Enterprise" | RQ1, RQ4 | medium |
| Uplevel 2024 (methodology critique) | RQ2, RQ6 | medium |
| DORA 2024 (trendline anchor) | RQ5 | medium |
| SPACE framework & DX Core 4 | RQ6 | medium |

## Blocked
| source_id | reason | needs |
|---|---|---|
| stanford-denisov-blanch (verification upgrade only — extraction done at talk-grade) | headline effect sizes exist only in talks; slides PDF image-only, videos not viewable in-session; figures taken from secondary write-ups which disagree on the headline number | human to watch/skim the Jun 2025 + Nov 2025 talk videos, or accept talk-grade ranges as-is |
| gitclear-2026 full report ("The Maintainability Gap") | email-gated (business email + name + job title); no free PDF exists; landing-page headline figures extracted, but methodology/caveats/baselines unreadable | human to register once and hand over the PDF, or accept landing-page figures only |

## Rejected (triage)
| source | one-line reason |
|---|---|

## RQ status
RQ1: OPEN | RQ2: OPEN | RQ3: OPEN | RQ4: OPEN | RQ5: OPEN | RQ6: OPEN

## Batch log
- 2026-07-06 phase-0 batch 1: five E3-anchor verifications done (metr-2025-rct, dora-2025, gitclear-2025, stanford-denisov-blanch, anthropic-economic-index). Headline outcome: the seed list survives but its era framing was optimistic — only METR is genuinely (early-)E3; Stanford's quadrant figures are talk-published E1/E2-mixed, GitClear 2025 is E1/E2 trendline, DORA 2025 respondents are 61% agent-mode-never. Two contradictions logged (GitClear churn vs arXiv 2507.10422; DORA 2024→2025 throughput flip with instability persisting). Two Blocked items need human input (Stanford talk videos; GitClear 2026 email gate). Strong new E3 leads queued: METR Feb 2026 update, arXiv 2607.01904 (2x-mandate diff-in-diff), DORA 2026 ROI interim, arXiv 2606.21804. Search-strategy note: arXiv preprints and vendors' own S3-hosted PDFs beat landing pages; secondary write-ups repeatedly misquote effect sizes (METR CI misquote; Stanford headline number varies by write-up) — always pull primary numbers.
- 2026-07-06 setup (2): protocol v0.3 — reweighted toward practitioner evidence: Tier C is the expected volume centre, ≥3 independent Tier C sources can carry an exec-brief claim (medium confidence cap), Tier C hunting grounds and practitioner query variants added. Few formal papers expected; that is by design, not a gap.
- 2026-07-06 setup: protocol v0.2 adopted (renamed to PROTOCOL.md; per-source commits; era-by-modality; preprint rule; TSV schema + era/measurement_basis columns; §6.5 query plans; saturation rule disambiguated; DoD scarcity clause; RQ4 expectation pre-registered). Repository initialised, scaffolding created. No research batches yet — Phase 0 not started.
