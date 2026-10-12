# 06 — Method notes

## Tools used and access boundary
- **Tools:** Claude Code with the following:
  - **Bash:** `ls`, `wc`, `cut`, `sort`, `uniq`, `grep`. Used to list the directory, count rows per source and tier, and check that source_ids exist.
  - **Read:** for `PROTOCOL.md`.
  - **Write and Edit:** only for the six files in `cleanroom-output/`.
  - **Agent:** read-only analyst subagents, each restricted to this directory.
- An attempt to run Python for table statistics was refused by the permission system. All counting was then done with standard shell tools by me and by the subagents.
- One helper script (never executed) was written to the session's scratch directory outside the project tree. Nothing outside `cleanroom-output/` in this directory was created or modified.
- **Access boundary confirmed:**
  - Only `PROTOCOL.md`, `CLAUDE.md`, `evidence/evidence-table.tsv` and `sources/*.md` in `/home/grappeq/work/cleanroom-L3-opus` were read.
  - No network access was attempted.
  - No web search or URL fetch was made.
  - No attempt was made to identify or locate the original programme or its conclusions.
  - Lines marked `[redacted]` were left as they are and not reconstructed.

## How I worked
1. **Read the protocol and checked the table's shape.**
   - I read `PROTOCOL.md` in full.
   - I profiled the table: 569 finding rows, 99 distinct source_ids, and the tier distribution per source.
   - I checked that table source_ids match `sources/` records. Two records have no table rows: `ghaleb-2026-fingerprinting` and `end-of-code-review-2026`. They are not cited.
2. **Ran seven parallel read-only analysts:**
   - one per research question (RQ1–RQ6), with the RQ6 analyst also counting task-type coverage;
   - one building the independence map.
   - Each read the relevant table rows (filtered with grep/cut) and the source records, especially the tier, independence, red-flag and "can / cannot support" sections. Each reported back with source_ids, tier, era and measurement basis.
3. **Ran five contradiction adjudicators**, one per candidate contradiction drawn from the RQ reports:
   - T4 speed in E3;
   - durability of gains;
   - the review bottleneck;
   - quality debt;
   - the direction of the perception gap, with seniority asymmetry assessed alongside.
   - Each re-verified the numbers against the rows and records and judged independence and status.
4. **Synthesised the findings myself.**
   - I applied the CLAUDE.md rules: no averaging; measured kept separate from self-reported; Tier C only with three or more independent sources; never Tier D alone; one voice per independence group; and the era transfer rule (E1/E2 effect sizes labelled pre-agentic).
   - I did not read all ~100 records personally. The subagents read them, and I relied on their verified extracts.

## Judgement calls
- **metr-2026-uplift and metr-2026-design-change** describe the same 2026 wave but are graded differently in the table (C and B). I treated them as one voice and as uninformative, following their own authors' disclaimer.
- **heilman-2026-microsoft** is Tier A by design, but its record says it is E1/E2 and "NOT an E3 comparator". It was excluded from E3 effect-size claims.
- **quispe-2026-claude-frontier:** the table's independence flag ("no COI, academic") conflicts with its record, where v2 is Microsoft–GitHub-adjacent. I followed the record.
- **bain-2026-benchmark** was excluded; its record judges the citation fabricated.
- **"4.6×" review-wait figure** (Opsera and LinearB marketing) was not used as corroboration.
- **Task-type counts** exclude range tags such as "T1–T11". 158 rows carry no T-code.
- **he-2026-2x-mandate** carries a lot of weight in RQ1, RQ4, RQ5 and RQ6. It is a single self-selected firm and shares authors with the CMU/Stanford lineage. I flagged this wherever it carries a claim.
- **Spend versus output:** the comparison of a ~20× spend increase with ~1.5–2× PRs is my own juxtaposition, not a ratio computed by the source.

## What I could not resolve
- **Whether E3 agents speed up experienced developers on mature code** (contradiction C1). The one clean task-time RCT is early-E3, and its replication failed on design grounds.
- **Whether E3 throughput gains last** (C2). The moderators (setting, prior AI exposure, model vintage) have not been tested directly, and much of the tension sits within one research lineage.
- **Whether thinner human review and rising static-analysis debt turn into production defects** (C3, C4). The one Tier A E3 stability proxy (reverts) points the other way.
- **Direction of developers' perception error** (C5). Unreliability is settled; direction is not.
- **Seniority asymmetry.** No source reports a statistically significant interaction.
- **Any cost-to-value ratio** (RQ4). The data is absent.
- **The quality of record-level grading.** Some rows carry non-standard tier strings, such as "A-candidate", "B/C (COI)" and "A-for-method". I used the record's prose to interpret them but did not re-grade any source.
- **Redacted material.** Parts of several records' "can / cannot support" sections are redacted, for example peng-2023-copilot-rct, google-rct-2024 and part of he-2026-2x-mandate. Where that happened, verdicts rest on the table rows and the unredacted record text only.
