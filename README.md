# What AI Coding Tools Actually Deliver — an Evidence Review

A personal research project, completed July 2026 and refreshed in October 2026. I wanted a straight answer to one question: **where do AI coding tools measurably help software engineering, where do they hurt, and how would you even know?** The marketing numbers didn't survive contact with their own primary sources, so this repo is the systematic version: 101 graded sources, 569 extracted findings, every claim traceable to a source record.

## Start here

- **[The exec brief](outputs/exec-brief.md)** — the whole answer in two pages.
- **[Count Voices, Not Papers](outputs/independence-crisis.md)** — a methods piece: how the AI-productivity literature shrinks by more than half once you check which "independent" sources are actually the same voice, with twenty-five documented cases of numbers corrupted in transit.
- **[How to tell whether AI is working for you](outputs/internal-measurement-proposal.md)** — six things to measure, nine popular metrics to refuse, each with a documented case of it burning someone.
- **[Open questions](outputs/follow-up-questions.md)** — what's still unknown and what would settle it.

## How this was made

An AI research agent (Claude Code) executed a pre-registered protocol ([PROTOCOL.md](PROTOCOL.md)) under human review gates: fixed research questions, a source-quality grading scheme, rules against averaging away contradictions, and saturation criteria — with a human (me) reviewing each phase before the next opened. [CLAUDE.md](CLAUDE.md) contains the agent's working instructions, and [LEDGER.md](LEDGER.md) is the running log of what was searched, extracted, rejected, and why.

That provenance matters for how you read it. The final documents in `outputs/` speak with two voices: "we" is the research programme reporting what it found; "you" is the reader — anyone deciding where to invest in AI. The working documents (`synthesis/`, `sources/`, `LEDGER.md`) keep their internal research voice, including mentions of "the human" (me, at review gates) — they are the audit trail, published unedited.

## How to read the grades

Every claim carries a source tier and an era tag:

- **Tiers:** **A** rigorous experiment · **B** large-scale data without an experiment · **C** credible company account · **D** vendor material (they have something to sell)
- **Eras:** **E1** autocomplete (Copilot-classic) · **E2** chat assistants · **E3** autonomous agents — tagged by the tool actually studied, never the publication year. Most famous numbers are E1/E2; most current decisions are about E3.
- **Confidence:** high / medium / low, always with a stated reason.

## Repo map

| Path | What it is |
|---|---|
| `outputs/` | The four final documents (start here) |
| `synthesis/` | Per-question synthesis memos, contradiction log, tension verdicts, review records — working documents, published as-is |
| `sources/` | One extraction record per source: what it measured, what it can and cannot support |
| `evidence/evidence-table.tsv` | Every extracted finding as one graded, era-tagged row |
| `PROTOCOL.md` | The pre-registered research protocol |
| `LEDGER.md` | The audit trail: batches, rejections, blocked sources, RQ status |
| `CLAUDE.md` | The research agent's operating instructions |

## Licence

[CC BY 4.0](LICENSE) — share and adapt freely, with attribution.
