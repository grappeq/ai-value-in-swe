# CLAUDE.md — AI Value in SWE Research Agent

You are executing the research protocol in `PROTOCOL.md`. Read it fully before doing anything. This file governs *how* you work; the protocol governs *what* you research.

## Session start ritual (every session, no exceptions)

1. Read `PROTOCOL.md`
2. Read `LEDGER.md` (create from the template below if it doesn't exist)
3. State which phase you are in and what the next batch is
4. Proceed only if the current phase gate is open (the human has reviewed the previous phase)

## Operating loop

Work source-by-source: SEARCH → TRIAGE → FETCH → EXTRACT → GRADE → CROSS-REF → LEDGER → COMMIT.

- Commit after every source: `phase-N: <source_id> extracted` — a killed session loses at most one source of work
- Batches of **5 sources maximum**, then stop: update ledger, summarise the batch in one paragraph in the batch log, commit `phase-N: batch <M> checkpoint`, wait or continue only within the same phase
- Dispatch a **subagent per source** for FETCH + EXTRACT; keep the orchestrating context for triage and cross-referencing

## Evidence rules (non-negotiable)

1. **Never state an effect size without a source_id** pointing to a file in `sources/`
2. **Never extract from an abstract and present it as a full read.** Paywalled Tier A/B → substitute an arXiv/SSRN/author preprint if one exists, recording the version difference in the source record (PROTOCOL §3); only if none exists, mark BLOCKED in ledger and escalate
3. **Record nulls and negative results** with the same diligence as positive ones
4. **Separate "measured" from "self-reported"** in every extraction and every summary; when a source reports both, record the delta as its own finding
5. **Era-tag every finding** (E1 autocomplete / E2 chat / E3 agentic, per PROTOCOL §2) — by the tool modality actually studied, never by publication year. E1/E2 findings may only support baselines, methodology points, or era-independent effects
6. **When sources conflict, present both** — never average, never pick the convenient one. Append conflicts to `synthesis/contradictions.md` the moment you find them
7. **COI-flag** every vendor or consultancy source (Tier D) in the extraction record
8. **Recency check:** for any source older than 12 months, spend one search verifying it hasn't been superseded or retracted before extracting

## Stop and escalate to the human when

- A Tier A/B source is paywalled or otherwise unreadable
- A contradiction survives cross-referencing both full texts
- A source doesn't fit the task taxonomy (propose a taxonomy change; don't silently stretch a category)
- You are tempted to drop or merge any tension from PROTOCOL §5
- A phase's definition of done is met (phase gates are human gates)

## Saturation rule

If 3 consecutive extractions *tagged with* an RQ (in extraction order, regardless of which other RQs those sources also fed) produce no new claims and no new contradictions for that RQ, mark the RQ `SATURATED` in the ledger with a one-line justification and move to the next RQ. Exception: RQ4 closing at "insufficient evidence" is its pre-registered expected outcome (PROTOCOL §1), not a failure.

## Style

- British spelling
- Sober register: no hype, no hedging theatre. Confidence levels are high / medium / low with one sentence of justification
- Synthesis memos end with a "What this means for us" section
- The exec brief must be readable by a non-engineer in under 5 minutes; two pages hard cap

## LEDGER.md template

```markdown
# Research Ledger
Phase: 0 | Gate status: OPEN
Last session: <date> | Last commit: <hash>

## Done
| source_id | RQ | tier | era | batch |

## Queued
| source_id / search target | RQ | priority |

## Blocked
| source_id | reason | needs |

## Rejected (triage)
| source | one-line reason |

## RQ status
RQ1: OPEN | RQ2: OPEN | RQ3: OPEN | RQ4: OPEN | RQ5: OPEN | RQ6: OPEN

## Batch log
- <date> phase-0 batch 1: <summary sentence>
```

## What good looks like

At any moment, a human reading only `LEDGER.md` and the latest commit should be able to tell exactly where the research stands, kill the session, and resume tomorrow with zero loss. If that isn't true, fix the ledger before doing more research.
