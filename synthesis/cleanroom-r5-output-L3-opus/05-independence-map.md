# 05 — Independence map

Rule applied (CLAUDE.md, PROTOCOL.md §3): sources that share authors, datasets, funding or organisation count as **one voice**. For Tier C, independence additionally requires different organisations, no retellings of the same rollout, and no shared vendor sponsorship. The groups below come from the `independence_flags` column and the source records. Wherever a group could inflate convergence, the deliverables count it once.

Two records (`ghaleb-2026-fingerprinting`, `end-of-code-review-2026`) exist in `sources/` but have no rows in the evidence table. They are therefore not cited anywhere in this output.

## Groups judged non-independent

| # | Group | source_ids | Reason | Consequence for counting |
|---|---|---|---|---|
| G1 | **AIDev dataset cluster** | aidev-dataset-2026, agentic-pr-merge-reject-2026, unmerged-fix-prs-2026, failed-agentic-prs-2026, more-code-less-reuse-2026, ai-build-code-2026, task-stratified-agents-2026, unreviewed-ai-prs-2026, review-agents-reality-2026, readability-agents-2026, agent-code-maintenance-2026, who-finishes-the-job-2026, agents-vs-ides-2026; indirectly denisov-blanch-2026-ramp (re-uses the agents-vs-ides panel) | **Shared dataset.** All draw on one corpus of agent-authored GitHub PRs. Its attribution heuristic is recorded as having no precision/recall validation. The aidev-dataset record says such papers "should be counted as one voice". | Any claim about agent PR merge, acceptance, review or rework rates has **one** large-N observational leg, however many papers repeat it. |
| G2 | Queen's University SAIL group | aidev-dataset-2026, harness-evolution-2026, zhong-2026-agentic-review | **Shared authors and organisation** (Hassan, Li, Adams). zhong re-uses the AIDev PR-type taxonomy but not its data. | Treat as one research voice. zhong's *data* are independent of G1, so it may count separately on review-latency questions. |
| G3 | **CMU (Vasilescu/He/Agarwal) + Stanford (Denisov-Blanch) lineage** | cursor-velocity-quality-2025, agents-vs-ides-2026, he-2026-2x-mandate, denisov-blanch-2026-ramp, stanford-denisov-blanch | **Shared authors.** The cursor-velocity record says to "treat all three as one evidentiary voice". he-2026-2x-mandate shares an author with stanford-denisov-blanch, and ramp re-uses the CMU panel. | The "velocity spike fades / static-analysis debt persists" finding and the "gains shrink with codebase age and size" finding are each **one voice**, despite different datasets. |
| G4 | **METR** | metr-2025-rct, metr-2026-uplift, metr-2026-design-change, metr-2026-survey, metr-2026-transcript-bound | **Same organisation, overlapping authors.** uplift and design-change describe the same February 2026 redesign, and the table grades them differently (C and B). | The METR follow-ups are not replications of the 2025 RCT. The −19% result has no independent E3 replication. |
| G5 | **Microsoft/GitHub economists' Copilot programme** | peng-2023-copilot-rct, cui-2024-copilot-field, hoffmann-2024-nature-of-work, demirer-2026-writing-vs-shipping, quispe-2026-agentic-delegation, quispe-2026-claude-frontier | **Shared authors** (Peng, Demirer, Musolff, Xu), Microsoft telemetry or GitHub funding, and paid Microsoft consultancy. quispe-2026-claude-frontier's table flag ("no COI") is superseded by its record (Microsoft–GitHub-adjacent in v2). | One vendor-adjacent voice. cui-2024-copilot-field's trials at three firms do not make it independent of peng-2023-copilot-rct. |
| G6 | Microsoft internal engineering research | heilman-2026-microsoft, microsoft-cli-agents-2026 | Shared author (Murphy-Hill), Microsoft-on-Microsoft. | One voice. Combine with G5 and G7 when counting "Microsoft" sources. |
| G7 | SPACE / DX measurement lineage | space-dx-core4, space-of-ai-2025, dx-reock-2026 | Shared framework authors (Forsgren, Zimmermann, Houck, Storey). DX is a measurement vendor. | One voice for metric-framework recommendations. Linked to Microsoft through the SPACE authors. |
| G8 | Google | google-rct-2024, google-migrations-2025, google-autodiagnose-2026 | Same organisation. Ziftci is on migrations and autodiagnose. The migrations papers are "same rollout". | One Google voice. The migrations results are a single rollout. |
| G9 | DORA / Google Cloud | dora-2024, dora-2025, dora-2026-roi | Same programme. dora-2026-roi has "no new data collection" and re-models dora-2025. The 2025 edition was sponsored by GitHub/GitLab. | dora-2026-roi adds nothing empirical. dora-2024/2025 are one voice (and soft-linked to G8). |
| G10 | Stack Overflow surveys | stackoverflow-survey-2025, stackoverflow-survey-2026 | Same publisher and instrument, self-selected respondents. | One voice; usable for trendlines only. |
| G11 | CircleCI | circleci-2026-delivery, circleci-2026-pulse-q2 | Same authors and telemetry; the Pulse is a follow-up. Thoughtworks sponsored the 2026 edition, which links it to bockeler-2026-qcon. | One voice. |
| G12 | Anthropic-authored | anthropic-economic-index, anthropic-postmortem-quality, shen-2026-coding-skills | Anthropic employees or Fellows writing about Anthropic products. | One vendor voice. shen-2026-coding-skills is an RCT but carries a COI in both directions. |
| G13 | Uber spend/adoption figures | uber-2026-claude-cost, uber-autocover-2026 (part B), ai-spend-landscape-2026 (the Uber-derived figure) | Same organisation and the same interview retold through several outlets. ai-spend-landscape records that one apparent corroboration is the Uber number "laundered". | One Uber voice for spend. The AutoCover ICSE paper (part A) is a distinct sub-study. |
| G14 | Pragmatic Engineer outlet | prageng-2026-survey, uber-autocover-2026 (part B), ai-spend-landscape-2026 (anecdote pool) | Same author/outlet. | Counts as one channel for Tier C convergence. |
| G15 | NAIST MSR authors | readability-agents-2026, agent-code-maintenance-2026 (also G1); agentic-pr-merge-reject-2026 ↔ churn-151-repos-2025 (shared author Fan) | Shared authors. | The first pair is already inside G1. The churn-151 link is weak (no shared data). |
| G16 | JetBrains | sergeyuk-2026-evolving, jetbrains-2026-ecosystem | Same vendor. | One vendor voice. |
| G17 | Meta-analyses re-pooling primaries | genai-productivity-meta-2026 (includes metr-2025-rct, cursor-velocity-quality-2025); wittig-2026-fragmented-markers (includes METR, Cui, Peng, Faros, Xu) | Data overlap. | Never counted as corroboration of the primaries they pool. |
| G18 | Microsoft-owned data in outside studies | xu-2025-maintenance-burden (100% Microsoft-owned repos); defect-rate-side-b (GitHub half) | Data provenance and vendor. | Soft link to G5/G6; noted, not merged. |

## Single-event or single-rollout retellings (each counts once)

These are recorded as a single source_id, but the press around each is derivative. None can be counted twice towards the three-source Tier C rule.
- nubank-devin-2025: one rollout.
- grigorev-2026-terraform-db: one incident; the press is derivative.
- amazon-2026-outages: one FT scoop plus Amazon's rebuttal.
- replit-db-deletion-2025: one user's posts plus the vendor's account.
- salesforce-2026-cursor-tests: the vendor blog cites the same figure.
- faros-2026-whiplash: the 2026 edition re-quotes 2025 figures.
- bain-2026-benchmark: the record judges the attribution fabricated ("aggregator cites aggregator"), so it is **excluded** from all claims.

## Tier D vendor singletons

Each is its own vendor voice, with a conflict of interest, and never carries a claim alone: linearb-2026-benchmarks, plandek-2026-benchmarks, opsera-2026-benchmark, uplevel-2024, qodo-2026-code-quality, code-cleanliness-tokens-2026 (SonarSource), faros-2026-whiplash, github-2026-agent-scale. gitclear-2025 is graded B but is vendor-authored.

Possible shared figure: the "4.6×" review-wait figure appears in opsera-2026-benchmark's report. It also appears in linearb-2026-benchmarks' marketing copy, but not in LinearB's own PDF, where the in-report figure is 5.25×. Because borrowing cannot be excluded, "4.6×" is not cited as an independent corroboration anywhere in this output.

## Sources judged independent of all groups above

- **Clean:** stray-2026-nav, arch-quality-agentic-2026, agent-maintainability-2026, cotroneo-2025-defects, german-se-survey-2026, vella-blincoe-2026, mao-2026-code-metrics, llm-software-design-2026, rca-failures-2026, impaired-programming-2026, dont-vibe-control-2026, fast-and-spurious-2025.
- **dev-agent-misalignment-2026:** independent; one Google co-author, a mild COI.
- **borg-2026-echoes:** independent of the groups above, but a CodeScene collaboration with a vendor COI.
- **debt-behind-ai-boom-2026:** possible but untested overlap with AIDev repositories.
- **Tier C practitioner sources from distinct organisations:**
  - cloudflare-2026-ai-review, agoda-2026-bottleneck, zendesk-2026-absorption, duolingo-2026-risk-bot, zalando-2025-postmortems, one-developer-squad-2026.
  - bockeler-2026-qcon, except for the Thoughtworks link to G11.
  - agoda-2026-bottleneck and zendesk-2026-absorption share an InfoQ author's framing and contain no numbers. They are treated as one narrative channel.

## Practical effect on the analysis

- **Agent-PR analyses (G1):** the apparent breadth of E3 large-N evidence on agent PRs is one dataset.
- **E3 quality debt (G3):** the apparent breadth of Tier A E3 quality-debt evidence is one research lineage. agent-maintainability-2026 is the only independent Tier A E3 corroboration.
- **E3 mature-codebase slowdown (G4):** the single strongest negative result (metr-2025-rct) has no independent replication.
- **Tier C counting:** the three-source threshold is met only where sources come from different organisations. In practice that means the T11 destructive-incident cluster (grigorev, replit, amazon) and the review-bottleneck narrative (agoda/zendesk counted as one, plus one-developer-squad-2026 and bockeler-2026-qcon).
