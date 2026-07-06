# ai-build-code-2026 — AI builds, We Analyze: AI-Generated Build Code Quality (MSR 2026)

## Citation & version

Anwar Ghammam (University of Michigan–Dearborn), Mohamed Almukhtar (University of Michigan–Flint). "AI builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality." MSR '26 (23rd International Conference on Mining Software Repositories, Mining Challenge track), Rio de Janeiro, 13–14 April 2026.

- Extracted from: arXiv:2601.16839 **v1** (submitted 23 January 2026), full HTML read — not abstract-only.
- Version note: arXiv v1 is the author preprint of the accepted challenge paper; no camera-ready diff known. Extraction date 2026-07-06.

## Verification

- Title, authors, and affiliations verified against the arXiv page and the MSR 2026 programme.
- Venue verified: listed among accepted papers in the MSR 2026 Mining Challenge track (2026.msrconf.org).
- Recency check: published January 2026, under 12 months old — no supersession search required.

## Design

- **Type:** repository-mining study on a shared challenge dataset; descriptive, no control group, no statistical inference.
- **Dataset provenance:** derives from **AIDev** (Li et al., 2025 — the official MSR 2026 Mining Challenge dataset; see `aidev-dataset-2026`), "a large-scale dataset of around 933k agentic PRs" from five coding agents on real GitHub repositories. AI authorship attribution is therefore inherited from AIDev's agent-account/metadata identification and is described by the authors as vetted by the challenge organisers; this paper performs **no independent validation of attribution**.
- **Build-code identification:** filtered AIDev for PRs modifying files of four build systems — Maven (`pom.xml`), Gradle (`.gradle`, `.gradle.kts`), CMake (`CMakeLists.txt`, `.cmake`), Make (`Makefile`, `.mk`). Two filtering rounds (automated pattern match, then manual inspection by one author) reduced 632 candidate PRs to **387 PRs with authentic build-system changes**, containing **945 build files**. CI pipeline config (GitHub Actions, GitLab CI), Dockerfiles, and other build systems (e.g. Ant, npm scripts) are **out of scope** — a material gap for T11 coverage.
- **Agents represented (PRs):** OpenAI Codex 173, GitHub Copilot 104, Devin 69, Cursor 38, Claude Code 2.
- **Smell detection:** *Sniffer*, a static analyser for build-specific smells across the four systems. Authors acknowledge false positives are possible, citing "significantly high" precision from prior literature; no re-validation on this corpus.
- **Qualitative component:** two authors manually labelled changes where smells were eliminated; Fleiss' kappa 0.76 (substantial agreement).
- **Period:** not stated in the paper; bounded by AIDev's collection window (agentic PRs up to mid-2025).

## Findings

All findings are **measured** (static analysis of merged repository artefacts), not self-reported. Era **E3** throughout (autonomous PR agents). Task type **T11** (ops/infra/CI — build configuration).

### F1 — Prevalence of quality issues in AI-authored build changes

"Across the 66 files, in which AI-generated changes introduced code quality issues, we found a total of **364 code smells**." Denominator context the abstract omits: "the majority of the build files (**824 out of 945**) did not introduce any smells either before or after" the AI change — i.e. ~87% of touched build files were smell-free throughout, ~7% (66/945) acquired new smells.

Maintainability-related smells (counts, severity as reported):
| Smell | n | Severity |
|---|---|---|
| Wildcard usage | 97 | medium |
| Lack of error handling | 63 | medium |
| Deprecated dependencies | 56 (+4) | medium–high (low) |
| Outdated dependencies | 27 | medium–high |
| Complexity | 27 | low |
| Suspicious comments | 23 | low |
| Missing version in raw | 19 | medium |
| Duplicate code/dependency | 15 | low |
| Inconsistent dependency management | 1 | low–medium |

Security-related smells: hardcoded paths/URLs 25 total (13 low, 9 medium, 1 low–medium, 2 high), hardcoded credentials 5 (high), insecure URLs 2 (high) — **32 security smells, 12 of them high severity**, in merged agent-authored build code.

### F2 — Smell elimination (the positive direction, recorded with equal diligence)

**31 build files improved** after the AI change; **54 smells removed** in total. "About **65% of the eliminated smells** resulted from intentional, quality-oriented changes" (refactorings such as Pull Up Module, Externalize Properties, remove unused/redundant code) rather than incidental deletion. Net picture: smells introduced (364) outnumber smells removed (54) roughly 7:1, but improving files (31) are half as common as degrading files (66), and most files (824) are untouched either way.

### F3 — Merge/intervention finding (the headline ">61%")

Verified: "Overall, **61.4% (238/387)** of the analyzed PRs were merged by developers, and in most cases, the merge occurred immediately after automated checks passed, with no additional modifications" from human reviewers. No quantitative definition of "minimal human intervention" (no review-time or comment-count thresholds) is given — the characterisation rests on the authors' manual reading of PR discussions.

**The paper's own framing is deliberately dual.** On one hand it reads the rate as adoption/trust: "developers currently perceive AI-generated build changes as sufficiently efficient and trustworthy to integrate rapidly." On the other, set against F1 (including high-severity security smells in merged code), the authors flag it as a governance concern: it "highlights the need for developer oversight when integrating AI-generated build updates" and motivates work on preventing agents "unintentionally introducing technical debt through redundant or inconsistent build configurations." Neither reading is endorsed as the verdict; the abstract calls it a "dual impact".

### F4 — Heterogeneity by agent (treat as descriptive only)

Smell-introduction rates differ sharply by agent: Copilot 226 smells across 266 build files (~0.85/file, the outlier), Cursor 60/155 (~0.39), Codex 53/326 (~0.16, despite touching the most files), Devin 23/195 (~0.12), Claude Code 0 — but Claude Code appears in only **2 PRs / 3 build files**, far too few to support any claim about it. No normalisation for repository, task difficulty, or build system; agent–repo selection effects are unaddressed. No per-build-system breakdown of results is reported.

### Nulls / absences

- **No human-authored baseline.** The study cannot say whether the smell prevalence is better or worse than human build PRs — a comparison the AIDev dataset would permit and other challenge papers attempt.
- No statistical testing, confidence intervals, or longitudinal trend analysis.

## Authors' limitations (as stated)

1. Dependence on AIDev's attribution and curation (external validity).
2. Only four build systems; no Ant, no CI/CD pipeline files.
3. Sniffer false positives possible (mitigation: prior-literature precision claims only).
4. Manual PR-discussion evaluation relies on authors' professional judgement and peer review between the two of them.

## Grading

- **Tier: B** (structured observational — repository mining on a curated shared dataset, peer-reviewed venue), with the caveat that it is a short Mining Challenge paper: small filtered n (387 PRs), single tool, no baseline, no inference. Grades closer to the weak end of B.
- **Era: E3** — agent-authored pull requests (Codex, Copilot, Devin, Cursor, Claude Code), tagged by modality studied.
- **Task type: T11** (build/CI/infra code). This is direct T11 evidence — one of the few sources examining agent output quality in build systems specifically rather than application code.
- **Independence:** academic authors, no vendor funding or COI apparent; dataset originates from an academic team (Li et al.). Not Tier D; no COI flag.
- **Measurement basis:** measured (static analysis + manual labelling); no self-report component.
- **Relevance to us: 4/5** — direct E3 evidence on agent-authored infra code quality and on review laxity for build changes; docked one point for the narrow build-system scope and missing human baseline.

## One-line verdict (can / cannot support)

**Can support:** directional claims that agent-authored build changes carry a non-trivial rate of maintainability and security smells (including high-severity ones) and are frequently merged with little human scrutiny; a mechanism hypothesis for T11 quality debt and review-bottleneck bypass. **Cannot support:** any claim that AI build code is worse (or better) than human build code, any per-agent ranking (especially Claude Code, n=2 PRs), or any effect size on delivery outcomes.

## Cross-reference notes (for the orchestrator)

- Same dataset family as `aidev-dataset-2026` and other MSR 2026 challenge extractions — findings are **not independent** of other AIDev-derived sources for triangulation purposes (same underlying PR population).
- F3 speaks to PROTOCOL §5 tension 6 (bottleneck displacement / review bypass) and tension 4 (quality-debt signals): merged-with-minimal-review agent PRs containing high-severity security smells is a concrete instance of quality debt entering via weak review, in T11 where review attention is typically thin.
- The abstract's foregrounding of 364 smells against the body's 824/945 smell-free files is a framing asymmetry worth remembering when this source is quoted elsewhere.
