#!/usr/bin/env python3
"""Build a clean-room export for the R5 re-derivation (synthesis/cleanroom-r5-protocol.md).

Usage: python3 -I tools/cleanroom_export.py <target-dir> [--level 3|2]
Refuses to run if <target-dir> exists. Writes synthesis/cleanroom-r5-redaction-log.txt in the repo.
"""
import sys, re, pathlib, json, shutil

repo = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
if not args:
    sys.exit(__doc__)
target = pathlib.Path(args[0]).expanduser().resolve()
level = 3
if "--level" in args:
    level = int(args[args.index("--level") + 1])
if target.exists():
    sys.exit(f"refusing: {target} already exists")
if str(target).startswith(str(repo)):
    sys.exit("refusing: target must be outside the repository")

LINE_PATTERNS = [
    ("tension-ref", re.compile(r"\btension[s]?\s*(#|§5\.)?\s*[1-7]\b|§5\s*tension|§5\.[1-7]\b|\btensions?\b.*§5|§5\b", re.I)),
    ("synthesis-files", re.compile(r"synthesis/|contradictions\.md|rederivation|tension-verdicts|\brq[1-6]-[a-z-]+\.md", re.I)),
    ("outputs/ledger", re.compile(r"outputs/|exec[- ]brief|measurement proposal|\bLEDGER\b|\bledger\b|batch log|\bQueued\b|triage (note|guess)|Original ledger", re.I)),
    ("verdict-words", re.compile(r"\b(CONFIRMED|CONTESTED|RESOLVED|INSUFFICIENT EVIDENCE|SATURATED)\b")),
    ("open-questions", re.compile(r"(open|follow-up) question", re.I)),
]
CROSSREF_HEADING = re.compile(r"^#{2,4}\s.*cross-?ref", re.I)
HEADING = re.compile(r"^#{2,4}\s")

log = []

def redact_record(path: pathlib.Path) -> str:
    out = []
    lines = path.read_text(errors="replace").split("\n")
    skipping = False
    for n, line in enumerate(lines, 1):
        if HEADING.match(line):
            if CROSSREF_HEADING.match(line):
                skipping = True
                log.append(f"{path.name}:{n}\tSECTION-REMOVED\t{line.strip()[:80]}")
                out.append(f"[redacted section — line {n}]")
                continue
            skipping = False
        if skipping:
            continue
        hit = next((k for k, p in LINE_PATTERNS if p.search(line)), None)
        if hit:
            log.append(f"{path.name}:{n}\t{hit}\t{line.strip()[:80]}")
            out.append(f"[redacted — line {n}]")
        else:
            out.append(line)
    return "\n".join(out)

def redact_table(path: pathlib.Path) -> str:
    rows = path.read_text(errors="replace").rstrip("\n").split("\n")
    hdr = rows[0]
    assert hdr.count("\t") == 16
    out = [hdr]
    cell_pats = [p for k, p in LINE_PATTERNS if k in ("tension-ref", "synthesis-files", "outputs/ledger", "open-questions", "verdict-words")]
    n_cells = 0
    for i, r in enumerate(rows[1:], 2):
        cells = r.split("\t")
        assert len(cells) == 17, (i, len(cells))
        for j, c in enumerate(cells):
            for p in cell_pats:
                if p.search(c):
                    log.append(f"evidence-table.tsv:{i}:col{j+1}\tCELL\t{c[:80]}")
                    c = p.sub("[redacted]", c)
                    n_cells += 1
            cells[j] = c
        out.append("\t".join(cells))
    log.append(f"evidence-table.tsv\tSUMMARY\t{n_cells} cell substitutions across {len(rows)-1} rows")
    return "\n".join(out) + "\n"

def trim_protocol(path: pathlib.Path, level: int) -> str:
    t = path.read_text()
    start = t.index("## 1. Research Questions")
    stop_marker = "## 6. Anchor Sources" if level == 2 else "## 5. Tensions"
    end = t.index(stop_marker)
    body = t[start:end]
    head = ("# Research Protocol (clean-room extract)\n\n"
            "Sections 1–4 of the programme's pre-registered protocol, reproduced verbatim. "
            "Later sections are withheld by design for this exercise.\n\n")
    return head + body

CLEANROOM_CLAUDE_MD = """# Clean-room re-derivation — analyst instructions

You are a fresh analyst. In this directory you have the complete extracted evidence base of a research programme on where AI coding tools deliver measurable value in software engineering: `PROTOCOL.md` (research questions, task taxonomy, tool-era definitions, evidence tiers, extraction schema), `evidence/evidence-table.tsv` (one graded finding per row, tab-separated, 17 columns), and `sources/*.md` (one extraction record per source, with grading, red flags and the extractor's "can / cannot support" verdict). Some lines and sections are marked `[redacted]`: they were removed on purpose and you must not try to reconstruct them.

**Rules**
- Work only from these files. There is no network access, by design; do not attempt to search the web, fetch URLs, or look for the project this evidence came from. Do not try to identify or locate the original programme's conclusions.
- Derive conclusions from the evidence as graded here. Where sources conflict, present both sides; never average. Separate measured from self-reported. Tag every claim with tier (A/B/C/D) and era (E1/E2/E3) as defined in PROTOCOL.md. A claim may rest on Tier C only if three or more independent Tier C sources converge; never on Tier D alone. Treat sources sharing authors, datasets, funding or organisation as one voice.
- Record nulls, absences and contested findings with the same diligence as positive ones. Confidence levels are high / medium / low, each with one sentence of justification.
- British spelling, sober register.

**How to work**
The records are large (~100 files). Read `PROTOCOL.md` first, then the evidence table. Fan out with subagents (one per research question, then one per candidate contradiction) that read the relevant rows and records and report back with source_ids; keep the orchestrating context for synthesis. Every claim you write must cite source_ids that exist in the table.

**Deliverables** — write exactly these files under `cleanroom-output/`:
1. `01-rq-verdicts.md` — RQ1–RQ6: one verdict each, confidence + one-sentence justification, source_ids.
2. `02-contradictions.md` — the five strongest contradictions in this evidence base: both sides, source_ids, independence assessment, status (resolved / contested / insufficient evidence).
3. `03-brief.md` — one page, at most 8 claims, each with tier, era and confidence; end with "What the evidence cannot say".
4. `04-gaps-and-metrics.md` — the three task types (T1–T11) with the least evidence; three metrics you would refuse and why; three you would adopt.
5. `05-independence-map.md` — groups of source_ids you judge non-independent, with the reason for each group.
6. `06-method-notes.md` — how you worked, what you read, what you could not resolve.

Stop when the six files are written. Do not edit anything outside `cleanroom-output/`.
"""

SETTINGS = {
    "permissions": {
        "deny": ["WebSearch", "WebFetch", "Bash(curl:*)", "Bash(wget:*)", "Bash(git:*)"],
    }
}

# build
(target / "evidence").mkdir(parents=True)
(target / "sources").mkdir()
(target / "cleanroom-output").mkdir()
(target / ".claude").mkdir()
for f in sorted((repo / "sources").glob("*.md")):
    (target / "sources" / f.name).write_text(redact_record(f))
(target / "evidence" / "evidence-table.tsv").write_text(redact_table(repo / "evidence" / "evidence-table.tsv"))
(target / "PROTOCOL.md").write_text(trim_protocol(repo / "PROTOCOL.md", level))
(target / "CLAUDE.md").write_text(CLEANROOM_CLAUDE_MD)
(target / ".claude" / "settings.json").write_text(json.dumps(SETTINGS, indent=2) + "\n")
(repo / "synthesis" / "cleanroom-r5-redaction-log.txt").write_text(
    f"# Clean-room export redaction log — level {level} — target {target}\n" + "\n".join(log) + "\n")
n_lines = sum(1 for l in log if "\tSECTION-REMOVED\t" not in l and "\tCELL\t" not in l and "\tSUMMARY\t" not in l)
n_sec = sum(1 for l in log if "\tSECTION-REMOVED\t" in l)
print(f"export written to {target}")
print(f"records: {len(list((target/'sources').glob('*.md')))}; redacted lines: {n_lines}; removed sections: {n_sec}; "
      f"table cell substitutions: see log; protocol level {level}")
