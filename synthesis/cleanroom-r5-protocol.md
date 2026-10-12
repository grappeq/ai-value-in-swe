# Clean-room re-derivation — pre-registered protocol (R5)

**Written 2026-10-12, before any clean-room run.** Purpose: test whether the programme's conclusions follow from the extracted evidence, or from the framing that accumulated over five cycles. A fresh analyst re-derives conclusions from the extraction records and the evidence table with no access to our synthesis, outputs, ledger, git history, or the web.

## Runs

| Run | Analyst model | Inputs | Tests |
|---|---|---|---|
| **L3-opus** (this run) | Claude Opus 5.5, fresh session, separate directory | Evidence table + redacted source records + PROTOCOL §1–§4 (research questions, taxonomy and eras, tiers, extraction schema). **No §5 tensions.** | Are the seven fault lines real features of the evidence, or artefacts of how we framed the search? The analyst must find the contradictions itself. |
| L3-fable (later) | Claude Fable 5.1, fresh session | identical export | Inter-analyst agreement — how much is evidence vs analyst judgement |
| L2 (optional) | either | as above + PROTOCOL §5 | Do the conclusions follow under our own pre-registered tensions? |

## Isolation (three leak vectors)

1. **Files.** Export via `tools/cleanroom_export.py` into a directory outside this repository, containing only: `evidence/evidence-table.tsv` (redacted), `sources/*.md` (redacted), `PROTOCOL.md` (§1–§4 only), a clean-room `CLAUDE.md`, and `.claude/settings.json`. Nothing from `synthesis/`, `outputs/`, `LEDGER.md`, `README.md`. **No `.git`** — commit messages carry conclusions verbatim.
2. **Network.** The repository is public under CC BY; one search finds our exec brief. The clean-room settings deny `WebSearch`, `WebFetch`, and `curl`/`wget` via Bash. The analyst is told the inputs are complete and that web access is off by design.
3. **Session.** A new Claude Code conversation started in the export directory (no memory of this session; the project memory directory is keyed to this repository's path and does not load there). The analyst must not be told the name of the source project or shown any of its outputs in the kickoff prompt.

## Redaction rules (applied mechanically by the export script; every removal logged to `synthesis/cleanroom-r5-redaction-log.txt`)

Removed from source records:
- Any section whose heading contains "Cross-ref" / "Cross-reference" (extractor assessments written against §5 tensions or other sources' conclusions).
- Any line matching: references to "§5 tension N" / "tension N"; references to `synthesis/`, `contradictions.md`, `rederivation`, `tension-verdicts`, `rq*-*.md`; references to the exec brief, measurement proposal, LEDGER/ledger, batch log, Queued, triage guesses ("Original ledger guess", "triage note"); verdict vocabulary in capitals (CONFIRMED / CONTESTED / RESOLVED / INSUFFICIENT EVIDENCE / SATURATED); references to "open question" / "follow-up question" numbers.
- Each removed line is replaced by `[redacted — line N]` so the analyst can see that something was removed, not what.

Kept deliberately (provenance, not conclusion): references to other source_ids ("same lab as he-2026", "AIDev-derived", "one voice with…"), tier/era/COI grading, "can / cannot support" verdicts written by the blind extractors, red-flag sections, proposed evidence rows.

Applied to the evidence table: the same tension/synthesis patterns are replaced in-cell by `[redacted]`; rows are never dropped; column count is re-verified.

Removed from PROTOCOL.md: everything from §5 onward (tensions, anchor list, query plans, workflow, DoD, scope decisions, changelog) and the v0.3/v0.4 framing in the preamble about expected results; §1–§4 kept verbatim (the RQ text and RQ4's pre-registered expectation are pre-registration, not findings).

Known residual leakage, accepted: the RQ wording itself (RQ5 names the greenfield/brownfield question; RQ6 asks which metrics mislead); the taxonomy's note that T3 is "the known sweet spot" and T4 "the contested zone"; extractor-written "can/cannot support" verdicts, which embody judgement at the source level. These are upstream of synthesis and part of what the analyst is meant to work from.

## Output template (fixed; the analyst writes exactly these files)

`cleanroom-output/01-rq-verdicts.md` — RQ1–RQ6: one verdict each, confidence high/medium/low with one sentence of justification, source_ids cited.
`cleanroom-output/02-contradictions.md` — the five strongest contradictions in the evidence, each with both sides, the source_ids, an independence assessment, and a status (resolved / contested / insufficient evidence).
`cleanroom-output/03-brief.md` — one page, ≤8 claims, each with tier and era tag and a confidence level; a short "what the evidence cannot say" section.
`cleanroom-output/04-gaps-and-metrics.md` — the three task types with the least evidence; three metrics it would refuse and why; three metrics it would adopt.
`cleanroom-output/05-independence-map.md` — groups of source_ids it judges non-independent (shared authors, data, funding, organisation), with the reason for each group.
`cleanroom-output/06-method-notes.md` — how it worked (fan-out, what it read, what it could not resolve), so the run is auditable.

## Comparison rubric (pre-registered)

Targets (scored one by one against the clean-room output): the seven §5 tension verdicts (mapped onto whichever of the analyst's contradictions correspond; a tension with no counterpart scores "absent"); the RQ1–RQ6 verdicts; the scarcity headline; the three "things we're sure about" in the exec brief; the dry task types; the provenance clusters (Stanford–CMU, Microsoft–GitHub, AIDev, Anthropic).

Scores: **same direction & confidence** · **same direction, different confidence** · **different direction** · **absent**. Plus two open lists: conclusions the clean room reached that we did not; ours it did not reach.

Triage of every discrepancy, logged in `synthesis/cleanroom-r5-comparison.md`, never silently merged: (i) clean room right, we were wrong → correction to outputs; (ii) we were right, clean room missed evidence → record which cue it needed (a legibility finding about the records); (iii) genuine judgement call → both positions recorded.

**Who compares:** not the author of the synthesis. A third agent receives both documents and this rubric and is instructed to argue each discrepancy both ways; the human adjudicates.

## Files

- `tools/cleanroom_export.py` — builds the export; refuses to run if the target directory exists; writes the redaction log.
- `synthesis/cleanroom-r5-redaction-log.txt` — every redacted line, file:line, with its first 80 characters, so the redaction itself can be audited.
- `synthesis/cleanroom-r5-output-L3-opus/` — the analyst's six files, committed unedited after the run.
- `synthesis/cleanroom-r5-comparison.md` — scored comparison and triage.
