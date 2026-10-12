# Tension 6 — Bottleneck displacement: verdict

## 1. The tension as pre-registered

PROTOCOL §5.6: "**Bottleneck displacement.** If code generation accelerates but review, verification, and deployment don't, local speedup should show up as review queue growth, not feature velocity. Look for direct evidence of shifted bottlenecks."

## 2. Direct evidence found

This is one of the strongest yields of the whole research programme.

**he-2026-2x-mandate** (Tier A, E3, single self-selected firm, staggered DiD with developer fixed effects and a 113-developer control group) gives the sharpest measured picture available: human review coverage fell **89%→68%**; automated review adoption rose **~19%→~84%**, overtaking human review; substantive human review roughly halved (~39%→~21%, or 47%→21% per the paper's own figure-vs-text discrepancy); per-reviewer load **doubled** because PR volume grew **3.1×** against a reviewer pool that grew only **1.5×**; and total cycle time *rose* **~22%** (review lead +20%) despite the throughput doubling — "more reviewer engagement, not more fixing." The authors' own caveat: late-window auto-approval routing likely biases this premium *toward zero*.

**faros-2026-whiplash** (Tier D, COI, 22,000 devs/4,000+ teams, within-team quarter-pair contrast) is directionally consistent: median time in PR review **+441.5%**, PRs merged without any review **+31.3%**, lead time +480.4% — alongside genuine throughput gains (task throughput +33.7%, epics/dev +66.2%). Caveats: an unaddressed organisational-growth confound, no absolute baselines published, and agentic *authorship* under 1% of the dataset (human-in-the-loop, not autonomous).

**dx-reock-2026** (Tier D, COI, ~400 companies) shows a usage/output wedge — AI usage **+65%** vs PR throughput **+7.76%** — that Noda's companion piece attributes to review absorbing coding's time savings (asserted, not measured). Against Faros's closest matched metric (PR merge rate/dev +16.2%), the earlier "4–8×" gap narrows to roughly 2×; DX's disclosure is markedly thinner than Faros's.

The throughput-outpaces-delivery arithmetic recurs across all three telemetry sources despite three designs, three populations, and two opposite-direction vendor COIs.

## 3. The mechanism voices

Two named non-vendor practitioners at unrelated organisations reached the identical qualitative conclusion narratively: **agoda-2026-bottleneck** (Stern, Tier C weak-end — "who reviews it? Line-by-line review doesn't scale," specification/verification named as the migrated constraint) and **zendesk-2026-absorption** (Tóth, Tier C weak-end — "absorption capacity" as the scarce resource). Neither supplies a single organisation-specific number.

Counted honestly: **one measured voice** (he-2026, unreplicated) **+ two narrative voices** (Agoda, Zendesk — mechanism-existence only) **+ two Tier D telemetry voices** (Faros, DX — opposing COIs). Mechanism corroboration spans five organisations; only one measured anything.

## 4. Complications

**unreviewed-ai-prs-2026** (Tier B, EASE 2026, matched subsample of 9,616 AI-authored vs 5,574 human-authored PRs in the same OSS repos) complicates the coverage-collapse framing: observable human participation is **statistically indistinguishable** by authorship (30.1% vs 30.8%); AI PRs are reviewed slightly *more* often (71.08% vs 65.48%). What shifts is composition — a quarter of human engagement with AI-authored code is agent-steering, not evaluation. This supports reading the enterprise bottleneck as **volume/capacity-driven**, not **AI-discrimination-driven** — a distinction OSS data can speak to and the enterprise panel cannot.

The automated-review-absorption question splits in two. **cloudflare-2026-ai-review** (Tier C strong-end on cost) shows automated review is cheap and fast (median $0.98/run, 3m39s latency, 131k runs/month) but reports **zero** effectiveness data — no catch-rate, no acceptance rate, no human-review-time comparison — despite naming the review bottleneck as its own motivation. **review-agents-reality-2026** (Tier B, MSR 2026, 2,456 AIDev PRs) supplies the missing outcome layer, and it is unflattering: CRA-only-reviewed PRs merge at **45.20%** vs **68.37%** for human-only (χ²=83.03, p<0.001), and 92.31% of CRA tools average signal ratios below 60%. Automation absorbs the **queue** (cost/latency are genuinely low) but the evidence on absorbing the **function** is negative where measured at all — he-2026's substantive-human-review halving alongside a still-rising cycle time is the worrying leg.

## 5. Era + independence audit

Measured magnitude rests on he-2026 (Tier A, one unreplicated firm, self-described "upper envelope") plus Faros and DX (Tier D, opposing COIs, neither carries a claim alone). Mechanism corroboration is genuinely multi-voice: Agoda and Zendesk share no authorship or sponsorship with each other or with the telemetry cluster. The complicating OSS sources (unreviewed-ai-prs-2026, review-agents-reality-2026) sit outside the enterprise-telemetry cluster entirely — an independence strength for the composition argument, though a caution against treating OSS and enterprise findings as measuring the same thing. No E1/E2 source is load-bearing; the tension is tested almost entirely on E3-modality evidence.

## 6. VERDICT

**CONFIRMED in direction; magnitude unresolved.** Confidence **medium-high** on mechanism existence — five independent organisations converge, none contradicts. Confidence **low-medium** on magnitude — the sole causal estimate is one self-selected best-case firm; the two multi-company telemetry estimates disagree 2–8× depending on matched metrics; and automated review's cost data and outcome data come from different organisations never jointly measured. This is arguably the research's central RQ5 finding: generation accelerated; absorption did not accelerate commensurately, and where automation substituted for absorption, it is cheap but not yet shown effective.

## 7. What would change the verdict

An independent Tier A replication of he-2026's design at a second, non-self-selected enterprise would resolve magnitude. A study jointly measuring automated-review cost *and* catch-rate on the same system would resolve whether automation absorbs the function or only the queue. No source reports the opposite pattern.

## 8. Feeds exec brief as

Code generation is accelerating faster than review, verification, and delivery capacity everywhere it has been measured — the bottleneck has moved, not disappeared, and cheap automated review has not yet been shown to close the gap it was built to close.

## R3 addendum (2026-07-17) — mechanism deepened, verdict unchanged
CONFIRMED in direction stands; no dissenting source appeared in 20 new extractions. New mechanism detail, all convergent: (a) humans still perform 83.21% of maintenance commits on agent-authored files (agent-code-maintenance-2026) — absorption stays human even where authorship is not; (b) agentic-PR rejection composition is coordination-dominated — reviewer abandonment 38% + duplicates 23% (failed-agentic-prs-2026), only ~36% of rejections demonstrably reflect agent failure (a further third has no recorded reason, so the true share is unknown) and 79.1% of merged agentic PRs show no visible human feedback loop (agentic-pr-merge-reject-2026); (c) reviewer sentiment does not track measured redundancy — objectively more-redundant agent code draws no more negative review reaction (more-code-less-reuse-2026) — a review-FUNCTION degradation signal, complementing he-2026's coverage collapse; (d) the burden-shift mechanism now has a measured pre-agentic antecedent (xu-2025, E1: core contributors +review/−own-output). Caveats: (a)–(c) are all AIDev-derived — one voice for triangulation; magnitude remains unresolved as before. The R1 formulation survives from scratch: automation absorbs the review queue, not yet the function.

## R4 addendum (2026-10-11) — direction confidence raised to HIGH; magnitude now bounded at open-source scale (one cluster)
From scratch, the convergence is now: seven named organisations (Agoda, Zendesk, the 2× firm, Cloudflare, Salesforce, Itaú — lead time per story unchanged at 15–20 days despite throughput gains — and Duolingo, whose auto-approval bot routes around rather than restores review), three vendor telemetry sets (Faros, DX, LinearB — agentic PRs wait 5.25× longer for first review and are reviewed 1.5× *slower* once picked up; acceptance 32.7% vs 84.4%), two CI-vendor reports with no AI variable (CircleCI: feature-branch activity up, main-branch flat-to-down), platform volumes with no agent split (GitHub: commits 5× YoY), and **the first large-N measured attenuation chain**: across 500,000+ public-GitHub developers in a time-shifted matched event study, sync agents raised commits +153% → PRs +86% → repositories +47% → releases +20%, autocomplete +30% → +9% n.s. (demirer-2026-writing-vs-shipping, B). An independent own-mined study of 1.02M reviewed PRs adds that AI-reviewer involvement speeds decisions while a process-quality proxy stays flat-to-worse (zhong-2026). hoffmann-2024 supplies the E1 ancestor of the mechanism: Copilot access shifted effort away from coordination/review events (−24.9%) toward code pushes. No source in 25 shows the opposite; falsifier (c) did not fire.
Magnitude caveats that must travel with Demirer: Microsoft confidential telemetry with two Microsoft-consultant authors (one cluster with Peng/Cui/Heilman/Quispe); "release" is a GitHub Releases object, not delivery to users; no quality, review-time or incident outcome; magnitudes moved 40–80% between the May and September revisions. he-2026 remains the only enterprise causal estimate. **Verdict: CONFIRMED in direction, confidence high; magnitude bounded at OSS scale, confidence low-medium.** Open question Q14: does the attenuation hold inside enterprise delivery pipelines?

## R5 note (2026-10-12) — confidence split
Two referees, reviewing the R4 upgrade independently, both split the confidence: HIGH that the bottleneck moved downstream (the attenuation is measured at scale and every source points one way), MEDIUM that the bottleneck is *review specifically* — demirer-2026 measures no review time, and the review-side evidence is one firm plus vendor telemetry and one-voice PR mining. Verdict wording amended accordingly in the index and the brief.
