# quispe-2026-claude-frontier

## Citation & version

Quispe, Alexander (2026). "Coding Beyond Your Training: Claude Code and the Technological Frontier of Software Developers." arXiv:2605.25438 [econ.GN], v1, submitted 25 May 2026. Marked "Preliminary draft, May 2026. Comments welcome."

- Single author, verified: Alexander Quispe, Department of Computing and Mathematical Sciences, California Institute of Technology (aquisper@caltech.edu).
- Version extracted: arXiv v1 (HTML full text, `arxiv.org/html/2605.25438v1`). No published/peer-reviewed version exists; no preprint-substitution issue. Fetched and read in full 2026-07-06.
- The draft explicitly reserves several analyses "for the full paper" — a later version is likely; recheck before synthesis if much time passes.

## Verification status

VERIFIED. Title, author, date, sample size (5,838 developers) and 28-month panel all match the triage description. Reportedly single-author: confirmed.

## Design

- **Method:** Staggered-adoption difference-in-differences using the **Callaway & Sant'Anna (2021) doubly robust estimator** (`csdid`: `control_group=notyettreated`, `anticipation=1`, `base_period=varying`, `est_method=dr`; SEs from 1,000 multiplier-bootstrap iterations clustered at developer level). Event-study aggregation over event time e ∈ [−6, 10]; "simple" aggregation averages ATT(g,t) over all post-treatment cells.
- **Treatment definition:** a developer's first Claude-co-authored commit on GitHub. Detection exploits the `Co-Authored-By: Claude` trailer that Claude Code attaches to commits, which "is machine-readable and propagates to GitHub's public event API". Adoption events span May 2025 – January 2026. Data are public GitHub event data, not vendor-provided telemetry.
- **Panel:** 7,786,771 Claude-co-authored commits from 185,517 developers harvested over the 13-month Claude Code availability window; analysis sample filtered to 5,838 developers (3,060 treated, 2,778 control), 28 monthly windows January 2024 – April 2026, 163,464 developer-month rows. Treated developers required ≥5 Claude-co-authored commits (excludes one-time experimenters); bot accounts removed by naming pattern.
- **Comparison group:** **not-yet-treated** developers — those who adopt Claude Code in 2025 Q4 or 2026 Q1 serve as controls for earlier adopters, "the standard recommendation in the Callaway and Sant'Anna (2021) framework". There is **no never-treated group**: every developer in the panel eventually adopts. The design therefore compares earlier adopters with later adopters, not adopters with non-adopters.
- **Covariates:** none in the main specification; conditional parallel trends with rich covariates is named "a natural next step".
- **Pre-trends:** "For five of six outcomes the pre-period event-study coefficients are small, statistically insignificant, and do not trend." Exception: cumulative languages, where the pre-trend is acknowledged as mechanical ("by construction, the cumulative count is weakly increasing in calendar time").

### The author's own causal hedges (verbatim)

The paper is unusually forthright that this is not a clean causal estimate:

- "Identification limits prevent a strict causal claim and we outline an agenda for cleaner tests." (abstract)
- "The central threat is that Claude adoption is voluntary and self-selected. A developer does not adopt Claude at random; she adopts because something about her work situation has changed."
- "Claude adoption is voluntary, and the timing of adoption is plausibly correlated with the timing of a developer's decision to start a new project in an unfamiliar language."
- "A developer who decides to ship a Rust application may install Claude *because* the language is unfamiliar, and her first Claude commit will be mechanically contemporaneous with her first Rust commit."
- "The staggered DiD design addresses cohort heterogeneity and TWFE negative-weighting concerns but does not resolve this reverse-causal selection problem."
- "If that something also affects the outcomes…then the parallel-trends assumption fails and the estimated ATT confounds the treatment effect with the selection mechanism."
- On the reversed Ashenfelter dip: "the treatment timing is endogenous: the developer's overall activity ramps up in the month preceding her first Claude commit, consistent with the start-of-a-new-project narrative." (The `anticipation=1` setting is the mitigation.)
- "We treat the estimates as documenting a *sharp, persistent shift in developer behavior coincident with Claude adoption, quantitatively consistent with the model's mechanism*, rather than as a settled causal claim."
- "The most defensible reading of the results is therefore associational rather than strictly causal."

**Proposed cleaner tests (the author's agenda):** (1) exogenous shocks — regional free-tier rollouts, pricing changes, institutional-subscription eligibility cutoffs, enabling IV or RD designs; (2) conditional parallel trends on pre-period commit history, language portfolio, account age, organisational affiliation; (3) placebo treatments — fake adoption dates 6–12 months earlier should return nulls under a valid design. None of these is implemented in v1.

**Design verdict:** methodologically careful staggered DiD on public telemetry, but with self-selected treatment, no never-treated controls, no covariates, and documented endogenous timing. Per the author's own words, associational, not causal.

## Outcome variables — what they can and cannot represent

All six outcomes are **activity/breadth measures computed from public GitHub commit metadata**: monthly commits, distinct repositories contributed to, distinct languages used (GitHub Linguist primary classification), Shannon entropy of the language distribution, newly-used languages, cumulative lifetime languages. All are **measured** (telemetry), none self-reported.

They can support claims about the *volume and diversity of public GitHub activity*. They cannot support claims about productivity, value delivered, code quality, or delivery outcomes:

- The paper does not measure commit size, lines changed, code quality, review outcomes, defects, or whether the new activity survives (e.g. whether newly-adopted languages are sustained or abandoned).
- **Instrument-changes-the-metric confound:** agentic workflows characteristically produce more, smaller commits (frequent checkpointing is part of the Claude Code workflow itself). Part of the +41 commits/month at adoption may be mechanical re-denomination of the same work into more commits, not more output. The paper does not address this. This is squarely the PROTOCOL §5.7 bad-metric trap (commit counts as gameable/meaning-free activity metrics); treat the commit finding as an adoption-signature, not a productivity effect.
- The language-diversity outcomes (entropy, newly-used, cumulative languages) are less vulnerable to commit-granularity inflation and are the paper's genuinely novel contribution — but they measure *exploration*, not competence: a co-authored commit in a new language does not show the developer can now work in that language (the paper's title claim, "coding beyond your training", rests on this untested equation of activity with capability).
- Treated developers are also detectable only via the co-author trailer, which users can strip; stripping behaviour, if correlated with developer type, adds selection on top of adoption selection. Not discussed in the paper.

## Findings (one record per finding; all measured; all E3)

Baselines: treated pre-adoption means (Table 1) — monthly commits 16.05 (SD 129.79), repositories 1.02, languages 0.60, entropy 0.09, newly-used languages 0.16, cumulative languages 1.64.

### F1 — Monthly commits
- ATT at adoption (e=0): **+40.708 (SE 2.674)**, significant; decays to +24.004 at e=1 and +13.277 at e=2; remains elevated but partially reverting. Simple aggregated post-treatment ATT: **+20.822 (SE 2.738)**.
- Against a pre-adoption mean of ~16–21 commits/month this is a very large jump at adoption, roughly halving within two months. Interpretation limited by the commit-granularity confound above.
- Robustness: +43.616 (SE 5.668) in the ≥50%-pre-active sample (n=1,620); +38.974 (SE 3.863) in the ≥6-pre-months sample (n=2,672).

### F2 — Repositories contributed to
- ATT at adoption: **+1.497 (SE 0.059)**, significant; e=1 +0.804, e=2 +0.422 (partial reversion). Simple ATT **+0.717 (SE 0.059)**. Pre-adoption mean 1.02.
- Robustness: +1.634 and +1.538 in the stricter samples.

### F3 — Distinct programming languages per month
- ATT at adoption: **+0.830 (SE 0.020)**, significant; e=1 +0.392, e=2 +0.210 (partial reversion). Simple ATT **+0.360 (SE 0.021)**. Pre-adoption mean 0.60.
- Robustness: attenuates to +0.623 (≥50% pre-active) and +0.710 (≥6 pre-months) but stays significant.

### F4 — Shannon language entropy
- ATT at adoption: **+0.138 (SE 0.006)**, significant. Simple ATT **+0.067 (SE 0.006)**. Pre-adoption mean 0.09. Robustness: +0.121 / +0.140.

### F5 — Newly-used languages (near-null on average — record with equal diligence)
- ATT at adoption: **+0.308 (SE 0.014)**, significant. But simple aggregated ATT is only **+0.035 (SE 0.014)** — a one-off burst of language experimentation at adoption that does not persist as an elevated monthly rate. The headline abstract number (+0.31) is the adoption-month spike, not the average effect.
- Robustness: +0.173 / +0.220 at e=0 in the stricter samples (roughly halved).

### F6 — Cumulative lifetime languages (the paper's core theoretical result)
- ATT at adoption: **+0.507 (SE 0.016)**; e=1 +0.565, e=2 +0.610; event-study profile "monotonically increasing" through e=10. Simple ATT **+0.586 (SE 0.016)** — the only outcome where the average effect exceeds the adoption-month effect, "exactly what the model anticipates" (Bayesian-learning prediction, Proposition 5). Cross-sectional post-treatment gap vs control: 2.17 cumulative languages.
- Caveat: this is the one outcome with significant (acknowledged mechanical) pre-period coefficients.
- Robustness: shrinks substantially to **+0.203** (≥50% pre-active) and **+0.234** (≥6 pre-months) — a ~55–60% attenuation among consistently active developers, the largest attenuation of any outcome. The frontier-expansion effect is concentrated in low-baseline-activity developers; the paper does not foreground this.

### F7 — Endogenous adoption timing (methodological finding, feeds RQ2/RQ6)
- Reversed Ashenfelter dip: developer activity ramps up in the month *before* first Claude commit. Direct telemetry evidence that adoption timing correlates with new-project starts — a caution for every observational adoption study in this literature, era-independent as a methodology point.

### Mechanism (background, not an evidence claim)
Bayesian-learning model: developers hold noisy priors over their productivity in unfamiliar languages; AI supplies "free signals about unfamiliar technologies and lowers the switching barrier", so unused languages accumulate precision passively and cross the adoption threshold over time. Predictions 1, 3, 5 (language diversification, repo expansion, growing dynamic effect) are matched; predictions 2 (sector diversification) and 4 (specialist advantage — larger effects for narrow specialists than generalists) are explicitly **not yet tested**, reserved for the full paper.

## Nulls / negatives

- Newly-used languages: simple ATT +0.035 (SE 0.014) — economically near-zero average effect despite a significant adoption-month spike (F5).
- Strong decay in commits, repos, and monthly languages after the adoption month (roughly −50% by e=1, −65–75% by e=2 relative to e=0): the adoption-month numbers in the abstract are peaks, not steady states.
- Cumulative-languages effect drops by more than half under either stricter activity filter (F6) — the persistence result is weakest exactly where measurement is cleanest.
- No quality, defect, or delivery outcome is measured at all, so no claim in this paper bears on production value (relevant null for RQ5: local activity surge with zero evidence on system-level delivery).

## Heterogeneity

Largely absent from this draft. No splits by seniority, geography, language ecosystem, organisation, or team. The specialist-vs-generalist split (Proposition 4) is reserved for the full paper. Only heterogeneity available is the implicit one across activity-filter samples noted in F6.

## Era & task-type tagging

- **Era: E3 (agentic).** Modality studied is Claude Code, a multi-file agentic tool; adoption window May 2025 – January 2026. Tag by modality per PROTOCOL §2 — unambiguous.
- **Task types: poor fit — flagged for orchestrator.** Outcomes are developer-level activity and technology-exploration measures, not SDLC task types. Closest mapping: **T3** (greenfield/exploration — new languages, new repositories) for F2–F6; F1 (commits) is cross-cutting/untaggable. F7 is a methodology finding (RQ2/RQ6), no task type. Recommend tagging evidence-table rows T3 with a "developer-level, not task-level" quality note rather than stretching the taxonomy.

## Tier & grade

**Tier B — structured observational.** Justification: large-N public telemetry (n=5,838; 163k developer-months) with a formal staggered-DiD counterfactual, which nominally reads as Tier A ("large-N telemetry with counterfactuals"); downgraded because (a) treatment is self-selected with documented endogenous timing and the author himself calls the defensible reading "associational rather than strictly causal", so the counterfactual does not carry causal weight; (b) preliminary single-author preprint, v1, no peer review; (c) no never-treated control group. Carries claims with caveats — specifically, claims about behavioural shifts coincident with adoption, never causal productivity claims.

## Independence / COI

- No vendor funding, no Anthropic affiliation, no acknowledgements section in v1. Author is academic (Caltech CMS). Data are public GitHub event data (the Co-Authored-By trailer is in public commit messages) — not Anthropic-provided telemetry, as far as the draft discloses. Cites Anthropic (2025) skill-formation work descriptively only.
- **Independence flag: none apparent — not Tier D.** Residual note: the paper studies a single vendor's product and its headline framing is favourable to it, but there is no disclosed relationship; treat as independent academic work pending the full version's acknowledgements.
- Population selection flag: GitHub-public-activity developers who leave the co-author trailer intact; treated must have ≥5 co-authored commits. Not representative of enterprise/private-repo development.

## One-line verdict

**Can support:** E3-era, measured evidence that Claude Code adoption coincides with a large, partially-reverting surge in public GitHub activity and a persistent broadening of language portfolios, concentrated among lower-baseline-activity developers; plus a methodology lesson (endogenous adoption timing) for RQ2/RQ6. **Cannot support:** any causal productivity, quality, velocity, or delivery claim — by the author's own statement and because every outcome is an activity metric (§5.7 trap).

## RQ relevance

- RQ1: weak/directional — activity and exploration breadth only, no value metric (relevance 2/5).
- RQ2: strong — endogenous-timing evidence and a worked example of what public-telemetry counterfactuals can and cannot identify (relevance 4/5).
- RQ5: negative-space relevance — a canonical example of local activity surging with no evidence on system-level delivery (relevance 3/5).
- RQ6: feeds the anti-metrics list — commit counts inflated at adoption, partially mechanically (relevance 3/5).

## Escalations / notes for orchestrator

1. **Taxonomy fit:** source does not map onto T1–T11; proposed handling above (T3 + quality note). Per CLAUDE.md this is an escalation trigger — do not silently stretch.
2. **Recheck for v2:** preliminary draft explicitly defers Propositions 2 and 4 and the covariate/placebo checks to "the full paper"; a revised version may exist by synthesis time.
3. **Cross-ref candidates:** the attenuation of headline effects under stricter activity filters, and the abstract-quotes-the-peak pattern (e=0 vs simple ATT), should be checked against any secondary reporting of this paper — press coverage citing "+41 commits" without the decay profile would overstate it roughly twofold.

## AMENDMENT (2026-07-17, R3 cycle — supersession + independence correction)

The v2 revision of this paper (arXiv 2605.25438v2, 7 Jul 2026, retitled "Agentic Delegation and the Language Frontier of Software Developers") is extracted as its own record: **sources/quispe-2026-agentic-delegation.md**. Material changes v1→v2:
1. **Independence grading of THIS record is corrected retroactively.** v2 adds a GitHub-employed co-author (Kevin Xu, khxu@github.com) and discloses: "This research was made possible by Alexander Quispe's time as a research associate at Microsoft–GitHub during summer 2026." The R1 grading "Caltech, independent of all our clusters" is therefore WRONG as an ongoing description: the work is Microsoft–GitHub-adjacent. It remains outside the CMU and AIDev clusters, but convergence with Microsoft-cluster sources (heilman-2026-microsoft, microsoft-cli-agents-2026) should no longer be counted as fully independent triangulation.
2. v2 rebuilt measurement at commit level; the headline language-count effect roughly tripled (+0.83 → +2.5) — a measurement-sensitivity caution against citing either version's point estimate as stable.
3. v2's cumulative-stock "keeps growing" outcome is self-flagged for differential pre-trends; the spike-then-decay pattern on flow outcomes persists.
Use the v2 record for any forward citation; this record stands for the v1 snapshot R1 actually analysed.
