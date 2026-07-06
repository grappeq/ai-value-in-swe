# Source Record: Google enterprise RCT on AI development speed (2024)

## Citation

Elise Paradis, Kate Grey, Quinn Madison, Daye Nam, Andrew Macvean, Vahid Meimand, Nan Zhang, Ben Ferrari-Church, Satish Chandra. **"How much does AI impact development speed? An enterprise-based randomized controlled trial."** arXiv:2410.12944 [cs.SE].

- v1: 16 Oct 2024; v2: 24 Oct 2024; v3 (current): 11 Nov 2024
- Published venue: **2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP 2025)** — confirmed via multiple independent secondary sources (search aggregators citing the ICSE-SEIP proceedings entry); the arXiv abstract page itself carries no journal-ref field, so this should be treated as corroborated-but-not-primary-verified. No author-hosted copy of the camera-ready SEIP version was located; arXiv v3 is being treated as materially equivalent per the preprint-substitution rule (PROTOCOL §3) — no evidence of a substantive text delta between preprint and proceedings version was found, but this has not been diffed line-by-line.
- All co-authors are Google-affiliated (Google Research / Google internal developer-tooling teams).

## Verification status

**Verified.** The candidate matches the seed description in PROTOCOL §6. Confirmed via arXiv abstract page, arXiv HTML full text (v1 and v2), dblp record, ResearchGate mirror, and multiple secondary citations. dblp lists only the arXiv CoRR entry as "informal publication" (dblp has not been updated with the SEIP proceedings record at time of check), but three independent web sources converge on the ICSE-SEIP 2025 venue attribution.

## Tier, era, independence

- **Tier: A (candidate)** — genuine RCT with random assignment, objective (telemetry-based) outcome measure, and a control condition. However, see "Corrections" below: the paper's own headline 21% figure is **not statistically significant** once developer-level covariates are controlled for, which materially weakens how much weight this source can carry on its own for an exec-brief effect-size claim. Treat as Tier A for *methodology* (the RCT design itself), but flag the headline number as **contested-within-the-paper**, not a clean anchor.
- **Era: E1/E2 — autocomplete and context-aware suggestion tooling, not chat and not agentic.** All three studied features (AI Code Completion, Smart Paste, Natural Language to Code) are inline, suggestion-based, human-triggered-and-reviewed features. None involve multi-file autonomous planning, execution loops, or agent-initiated action. This is closer to E1 (autocomplete) than E2 (chat-in-a-panel) in mechanism, though "Natural Language to Code" has a prompting-window interaction that gives it a thin E2 flavour. **Recommended tag: E1/E2 boundary, autocomplete-dominant.** Per the era transfer rule (PROTOCOL §2), this cannot support any E3/agentic-era effect-size claim in the exec brief; usable only as historical baseline, methodology reference, or era-independent-effect evidence.
- **Independence: COI flag — Google studying Google's own internal developer tooling on Google's own engineers.** The paper explicitly acknowledges this ("risk associated with us evaluating our own team's developer tools... it was impossible to run the study with developers outside of Google"). Not vendor-marketing in tone or venue (peer-reviewed SEIP track, transparent about null results and limitations), but the structural conflict of interest is real and should travel with any citation of this source.

## Method & population

- **Design:** RCT, individual-level randomisation, parallel two-arm (AI-enabled vs AI-disabled), identical task in both arms. Randomisation occurred *after* pre-task questionnaire and AI-feature training/review, before task start.
- **n = 96** full-time Google software engineers (48 per arm); 93 completed the task (96.9% completion).
- **Selection criteria:** ≥1 year Google tenure, C++ proficient, regular users of Google's internal Piper code repository and Cider V IDE, task-domain experience. Mean seniority level 4.38 (scale 3–7, where 3 = early career and 7 = just below first executive/Staff-adjacent level) — a mid-to-senior-skewed, homogeneous, single-company, single-language-ecosystem sample.
- **Task:** edit a pre-existing 10-file, 474-line changelist to implement a new logging service writing to Google's proprietary internal file storage infrastructure; update build files, data structures, test files; task complete when all tests passed. Pre-tested with 8 engineers and expected to take 30 minutes–2.5 hours; actual observed range 4.4–271.1 minutes (mean 104.4 min, SE 60.3). Authors' own definition of "enterprise-grade": reflects real Google developer work, exercises the full internal tool stack, and stays feasible within a lab session (3-hour cap).
- **Tooling studied (E1/E2 boundary, confirmed from full text):**
  - *AI Code Completion* — transformer-based single/multi-line inline suggestions as the developer types (Copilot-classic style).
  - *Smart Paste* — AI-adjusted, context-aware transformation of pasted code, accept via Tab.
  - *Natural Language to Code* — cursor/selection-triggered prompting window producing a suggested code change, which the developer reviews and applies or rejects (no autonomous multi-step execution).
- **Measurement basis: MEASURED, not self-reported.** Time-on-task was logged via IDE/system telemetry: "time spent in Cider V working in the study-specific workspace... and on adjoining development surfaces," from workspace creation to last observed IDE interaction. No self-report of speed is used as the outcome variable (a pre/post questionnaire on AI-feature familiarity etc. was collected but is a covariate, not the dependent variable).

## Key findings (exact figures, with measured/self-reported labels)

All findings below are **measured** (telemetry-based), not self-reported, unless noted.

1. **Unadjusted comparison:** AI-arm mean 96 minutes vs control-arm mean 114 minutes on task. Welch's t(83.6) = 2.11, **p = .038** (significant at α=.05). Raw difference ≈ 15.8% of the control mean.
2. **Headline "~21%" figure — Model 2 (developer-level covariates controlled):** β₁ = ‑0.24 (log-time model) → ≈21% speedup. **95% CI = [‑0.51, 0.03]; p = .086 — NOT statistically significant at the conventional p<.05 threshold.** The authors themselves state the effect "lost its significance" once covariates were added and that "our confidence interval is large." **This is the figure the PROTOCOL seed description cites as "~21% faster"; it must not be reported as a significant result without this caveat.**
3. **Model 3 (task-level factors only, different covariate set):** β₁ = ‑0.30 → ≈26% speedup, **p < .05 — significant** under this alternative specification. The paper itself thus contains two competing "best estimate" numbers (21% NS vs 26% significant) depending on which covariates are included — this is a within-paper model-specification sensitivity, not a single clean number.
4. **Heterogeneity — daily coding hours:** developers self-reporting ≥5 hours/day of coding were 32% faster overall regardless of arm (β=‑0.38, p<.05, a control-variable main effect, not an AI-interaction effect). The interaction of high coding-hours × AI condition was negative (β=‑0.29, suggesting extra AI benefit for heavy coders) but **not statistically significant**; authors describe this only as a tentative suggestion.
5. **Heterogeneity — seniority:** each seniority-level increase associated with ~15% faster completion overall (β=‑0.16, p<.05, main effect, not AI-specific). The seniority × AI interaction was negative but non-significant (p=.706). Authors read this as mildly consistent with *more* senior engineers benefiting somewhat more from AI — the opposite direction from the seniority-asymmetry literature flagged in PROTOCOL §5.5, though the finding is not significant and should not be used to contest that tension.
6. **Heterogeneity — prior AI tool usage frequency (0–13 scale):** **no significant effect** (p=.235). Explicit null result: "no statistically significant evidence that more frequent use of AI coding tools... increased their speed." Recorded here per the CLAUDE.md rule to preserve nulls with the same diligence as positives.
7. **Task-level moderators (C++ proficiency, task-domain expertise):** neither significantly predicted completion time; authors note they find this puzzling ("unclear why expertise... [was] not significant").

## Authors' stated limitations (paraphrased/quoted)

- Single-company, single-tool-ecosystem, single-language sample: "findings may therefore not be directly comparable to those obtained from studies with other developer populations."
- Self-evaluation conflict of interest acknowledged directly: evaluating "our own team's developer tools," and it "was impossible to run the study with developers outside of Google."
- Lab-task realism trade-off: an artificial task, however well-designed, "cannot perfectly match the complexity of developers' real-world work, which often has no obvious nor definitive solution."
- 3-hour session cap constrains generalisability "to the broader company or ecosystem levels."
- Tooling is a moving target: "We are still very early in the evolution of genAI-based tools for code... a 'true estimate' of the contribution of AI tools to developer speed will be a moving target" — the authors themselves flag that this snapshot (internal Google tooling, summer 2024) will likely be superseded, which is exactly why the era tag matters here.
- Underpowered for interaction effects: adequately powered for the main effect only; "further analyses are needed with larger sample sizes to ascertain interaction effects" — this directly qualifies findings 4–7 above.

## What this can and cannot support

**Can support:** a methodology reference for RCT-based, telemetry-measured (not self-reported) time-on-task designs in enterprise settings; historical baseline for E1/E2-era autocomplete/suggestion-tooling effect sizes; a documented instance of the "one paper, two significance conclusions depending on covariate specification" pattern relevant to RQ2 (measurement trustworthiness) and RQ6 (metric fragility). **Cannot support** any claim about agentic-era (E3) tooling, and per the era transfer rule cannot appear in the exec brief as an unqualified "~21% faster" figure — if cited at all, it must carry both the non-significance caveat and the E1/E2 pre-agentic label.

## Corrections vs. the seed description (PROTOCOL §6)

1. Seed describes the finding as "~21% faster task completion" without qualification. **Correction: the ~21% figure is the paper's own preferred model estimate but is NOT statistically significant (p=.086, CI crosses zero).** A different, also-reported model specification gives 26% and *is* significant. The unadjusted raw comparison (96 vs 114 min, p=.038) is the only cleanly significant number in the paper, and it is not the 21% figure.
2. Seed frames this as an "E2 baseline." **Correction: the tooling described (inline autocomplete, paste-transform, prompt-triggered single suggestion) is more accurately E1/E2 boundary, autocomplete-dominant, not clearly chat-era E2.** Recommend tagging E1/E2 rather than E2 outright in the evidence table if/when this source is extracted into rows.
3. Seed does not mention the venue. **Addition: published at ICSE-SEIP 2025** (per corroborating secondary sources; not independently confirmed against a camera-ready PDF).
4. Seed does not mention the null finding on prior-AI-usage frequency or the counter-directional (non-significant) seniority interaction. Both are recorded above per the nulls-diligence rule.

## Follow-up leads (not extracted — leads only)

- **METR (2025), "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"** — arXiv:2507.09089 — https://arxiv.org/abs/2507.09089 — the −19% agentic-era RCT already seeded as its own anchor in PROTOCOL §6; came up repeatedly as the natural contrast case to this source. Already tracked separately (sources/metr-2025-rct.md) — do not re-extract here.
- **"Creating benchmarkable components to measure the quality of AI-enhanced developer tools"** — Paradis, Murillo, Pandey, D'Angelo, Hughes, Macvean, Ferrari-Church — CHI 2025 EA — arXiv:2504.12211 — https://arxiv.org/abs/2504.12211 — same core Google author group, one year later; about building product-quality benchmarks for AI dev tools rather than a new RCT, but worth a look for whether it references an agentic-tooling follow-up study internally.
- **"The Fast and Spurious: Developer Productivity with GenAI"** — arXiv:2510.24265 (v1 and v2) — https://arxiv.org/abs/2510.24265 — title suggests a critical/methodological angle on GenAI productivity measurement; unclear if it cites or replicates the Google RCT; worth triage in Phase 1.
- **"AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development"** — arXiv:2601.13597 — https://arxiv.org/abs/2601.13597 — potential E3 RCT/field-experiment candidate distinguishing IDE-assistant from agent modality; high-priority Phase 1 triage target given the protocol's explicit hunt for agentic-tooling RCTs.
- **"Usage, Effects and Requirements for AI Coding Assistants in the Enterprise: An Empirical Study"** — arXiv:2601.20112 — https://arxiv.org/html/2601.20112v1 — enterprise-context empirical study, post-dates the Google RCT by over a year; worth checking whether it's a Google follow-up or an independent replication attempt elsewhere.
- **No agentic-era (E3) Google internal RCT was found.** Searches for a 2025–2026 Google-internal controlled experiment on agentic tooling (Gemini-based coding agents, Antigravity, etc.) returned only product-launch/marketing material (Google I/O 2026 announcements, DORA 2025 blog coverage) and CEO-level anecdotal figures (e.g. "+10% engineering velocity," "25% of code AI-assisted," "75% of new code AI-generated" — all unsourced, self-reported/PR-style claims, not RCT or telemetry studies). This absence is itself notable and consistent with PROTOCOL's pre-registered expectation that agentic-era RCTs are scarce — flagging as a live E3 gap rather than something to force-fit.

## Recency check notes (source >12 months old)

Source is from October–November 2024, now >18 months old relative to the 2026-07-06 research date, so the CLAUDE.md recency-check rule applies. One search round was spent specifically checking for supersession/retraction/replication: no retraction or correction notice was found on arXiv (still listed, v3 current, CC-BY 4.0, no withdrawal notice); the paper appears to have progressed to peer-reviewed publication (ICSE-SEIP 2025) rather than being superseded, and continues to be actively cited by 2025–2026 productivity-measurement papers (e.g. the METR 2025 write-ups reference it as a comparison point). No direct replication of this specific study (same task, same tooling) was found. **Conclusion: not superseded or retracted; treat as stable but dated (E1/E2-era) evidence.**
