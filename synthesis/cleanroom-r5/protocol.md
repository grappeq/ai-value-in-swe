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

## Redaction rules (applied mechanically by the export script; every removal logged to `synthesis/cleanroom-r5/redaction-log.txt`)

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

Triage of every discrepancy, logged in `synthesis/cleanroom-r5/comparison.md`, never silently merged: (i) clean room right, we were wrong → correction to outputs; (ii) we were right, clean room missed evidence → record which cue it needed (a legibility finding about the records); (iii) genuine judgement call → both positions recorded.

**Who compares:** not the author of the synthesis. A third agent receives both documents and this rubric and is instructed to argue each discrepancy both ways; the human adjudicates.

## Files

- `tools/cleanroom_export.py` — builds the export; refuses to run if the target directory exists; writes the redaction log.
- `synthesis/cleanroom-r5/redaction-log.txt` — every redacted line, file:line, with its first 80 characters, so the redaction itself can be audited.
- `synthesis/cleanroom-r5/output-L3-opus/` — the analyst's six files, committed unedited after the run.
- `synthesis/cleanroom-r5/comparison.md` — scored comparison and triage.

## Execution note (2026-10-12, L3-opus)

At the human's request the L3-opus run was executed as a fresh Opus subagent launched from the orchestrating session, pointed at `~/work/cleanroom-L3-opus`, rather than as a separate interactive session. Consequences for isolation, recorded honestly: the subagent has no access to this conversation's context (it is not a fork), but it runs under the orchestrating session's tool permissions, so the no-network and directory-restriction rules are enforced by instruction, not by the clean-room `settings.json`. The agent was required to state in its method notes which tools it used and whether it accessed anything outside the directory; that statement is the audit record for this run. The later Fable run should use a separate interactive session so the config-level denial is in force.

## Execution note 2 (2026-10-12, L3-opus, superseding note 1)
The subagent run was stopped by the human before producing output (no files written). The L3-opus run is instead executed as a separate background Claude Code session started from the clean-room directory with `claude --bg --remote-control --model opus --permission-mode acceptEdits`, so the clean-room `settings.json` (allow: read-only tools, writes under `cleanroom-output/`, subagents; deny: WebSearch, WebFetch, curl, wget, git, python) is in force at config level, and the human can observe the session through Remote Control. Isolation is therefore config-enforced as originally specified.

## Execution note 3 (2026-10-12, L3-opus run complete)
Run executed as background session `c47622ba` (Remote Control session https://claude.ai/code/session_01AMzXe6NuvUKeuJGWpxbS5D), model Opus 5.5, permission mode acceptEdits with the clean-room allow/deny list in force. Six deliverables written (≈8,000 words) and copied unedited to `synthesis/cleanroom-r5/output-L3-opus/`. The analyst's method notes (its audit record) state: only PROTOCOL.md, CLAUDE.md, the table and `sources/*.md` in the directory were read; no network, search or fetch attempted; a Python call was refused by the deny rule and counting was done with shell tools; seven read-only analyst subagents (one per RQ, one for the independence map) and five contradiction adjudicators were used; one helper script was written to the session's own scratch directory outside the project tree and never executed. Subagents inherited the Opus 5.5 model (no default subagent model is configured). Observation for the next export: the line-level redaction removed parts of the "can / cannot support" sections in some records (the analyst names peng-2023-copilot-rct, google-rct-2024, he-2026-2x-mandate) because those lines referenced tensions by number — broader than intended; for the Fable repeat, keep the export byte-identical (comparability first) and note the limitation. Comparison: delegated to a Sonnet 5.5 agent (neither the synthesis author's model nor the clean-room model), writing `synthesis/cleanroom-r5/comparison.md` against the pre-registered rubric.

## Execution note 4 (2026-10-12, L3-fable started)
Second clean-room run started in parallel with the Opus comparison, as a separate background Remote Control session `a53d4b53`, model Fable 5.1, in `~/work/cleanroom-L3-fable` — a copy of the Opus export verified byte-identical on all 105 input files (md5 over evidence/, sources/, PROTOCOL.md, CLAUDE.md, .claude/settings.json), with an empty `cleanroom-output/`. Same kickoff prompt, same permission mode and allow/deny list. Output will be committed unedited to `synthesis/cleanroom-r5/output-L3-fable/`; a second referee pass will score it against the same rubric and, additionally, score Fable-vs-Opus agreement (inter-analyst agreement, the measure of evidence vs analyst judgement).

## Execution note 5 (2026-10-12, referee design changed)
The human judged Sonnet too weak to referee; the Sonnet pass was stopped before writing a complete file (partial discarded). Because neither frontier model is neutral — Opus produced Side B, Fable produced Side A — the comparison of the L3-opus run is made twice by fresh agents, each warned about its own affinity: `synthesis/cleanroom-r5/comparison-L3-opus-by-opus.md` and `synthesis/cleanroom-r5/comparison-L3-opus-by-fable.md`, against the same rubric. Rows where the two referees disagree are treated as judgement calls and go to the human. The L3-fable run will be refereed the same way (by Opus and by Fable), plus a Fable-vs-Opus inter-analyst agreement pass.

## Execution note 6 (2026-10-12, rate-limit interruption and restart)
At ~05:00 UTC the account's session limit was reached: both referee agents terminated mid-read (no complete file written; partials discarded) and the L3-fable clean-room session lost at least one of its own subagents to the same limit ("RQ3 failure map synthesis" failed). A clean-room run with failed subagents is not comparable to the Opus run, so session `a53d4b53` was stopped before it wrote any deliverable (output directory verified empty) and the Fable run was restarted from scratch at ~08:55 UTC on the unchanged export, with the same kickoff prompt. Both referees were relaunched at the same time. Inputs for the Fable run therefore remain byte-identical to the Opus run; only the start time differs.

## Execution note 7 (2026-10-12, L3-fable run suspended)
The restarted Fable clean-room session (`b1a2265c`) hit the account's session limit again mid-run (limit text observed in its log from ~09:50 UTC); with subagents failing on the limit the run is not comparable to the Opus run, so it was stopped and any partial output set aside (none committed). The L3-fable run is SUSPENDED by the human's decision; the export at `~/work/cleanroom-L3-fable` remains byte-identical to the Opus inputs and can be re-run from an empty `cleanroom-output/` when usage allows. The inter-analyst agreement measure is therefore not yet available; the L3-opus run with two referees stands as the completed part of R5.
