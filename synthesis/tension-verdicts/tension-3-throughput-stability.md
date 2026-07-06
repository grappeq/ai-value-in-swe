# Tension 3 — Throughput vs Stability

## 1. The tension as pre-registered

PROTOCOL §5.3, verbatim: *"Throughput vs. stability. DORA 2024 associated rising AI adoption with reduced delivery throughput and stability; DORA 2025 reframed AI as an amplifier of existing organisational capability. Track how this evolved in 2026 data."*

## 2. The trendline assembled

**dora-2024** (Tier B, E1/E2, self-report, n≈3,000): per 25% increase in AI adoption, throughput **−1.5%**, stability **−7.2%** (report's own construct is "stability" falling; later paraphrases invert the label to "instability" rising — same direction). Both self-reported, no telemetry. The anchor figures sit on a **freshly redefined** construct: 2024 was the first wave to split throughput/stability and add a new "rework rate" item into stability.

**dora-2025** (Tier B, E1/E2-weighted with minority E3, self-report, n=4,867, 61% never use agent mode): throughput **flipped positive**; stability **did not** — instability persisted, and DORA tested whether adoption maturity moderates it and found no evidence. Three live, unresolved explanations for the flip: (a) real change with adoption maturity; (b) construct redefinition — the split/rework-rate item arrived the year before the flip; (c) modality-mix shift (2024 had no agent-mode concept; 2025 added a minority one) — both waves bundle all modalities into one factor.

**dora-2026-roi** (Tier D, no new data): recasts persistent instability as a temporary J-curve "tuition cost," with an illustrative (not measured) −$344k "instability tax" worked example, borrowed by analogy from unrelated transformation literature. No panel data shows an AI-specific dip-then-rise, and it contradicts DORA 2025's own rejected moderation test. This is a **reframe, not a resolution**.

**No DORA 2026 annual report exists yet** (fielded September; re-check queued). The ROI report is the only 2026 DORA data point, and it isn't data.

## 3. Non-DORA evidence on stability

- **faros-2026-whiplash** (Tier D, COI, E2/E3-blend, human-in-loop authorship): +242.7% incidents/PR, +54% bugs/developer, +31.3% PRs merged unreviewed — direction only; confounded with organisational growth, no absolute baselines.
- **he-2026-2x-mandate** (Tier A, E3, single firm): cycle time +22%, review lead +20% — a real causal cost — but revert rate is **flat-to-better** (−0.059***, AI PRs revert *less*) and merge rate flat. The strongest measured stability datapoint here, and it is reassuring, though a coarse, short-horizon proxy with no defect/incident data.
- **cui-2024-copilot-field** (Tier A, E1): build success −5.53% pooled (n.s.), **−17.4%** at Accenture (significant) — a measured, mild cost on autocomplete-era tooling.
- **uplevel-2024** (Tier D, COI, E1, contested): +41% bugs, undefined bug construct, access-not-usage confound — cannot carry a claim alone.
- **Amazon Mar 2026 outages** — unextracted lead only, not evidence.

## 4. The measurement problem

DORA's throughput and stability are self-reported both years — the flip is self-report vs self-report, not a resolution of the self-report-vs-measured gap (RQ2). The only *measured* stability datapoints — he-2026's revert rate, Faros's incidents/bugs, Cui's build success — point in **different directions on non-comparable constructs**, and no source measures more than one of them together. There is no single telemetry study of both throughput and stability in one population. Plainly: DORA gives a self-reported trade-off story that changed direction once; the measured proxies disagree with each other and can't be pooled.

## 5. Era and independence audit

Era: dora-2024 E1/E2 (no agent-mode concept); dora-2025 E1/E2-weighted with minority E3; dora-2026-roi inherits that same pre-agentic data under agentic rhetoric; he-2026 genuine E3; Faros E2/E3-blend but scoped to human-in-the-loop authorship (<1% agent-authored PRs); Cui/Uplevel E1 baselines. Independence: DORA 2024/2025 are vendor-adjacent (Google Cloud, GitHub/GitLab sponsors); dora-2026-roi is Tier D, co-authored with Google's own paid consulting arm — the weakest-independence source, making the most reassuring claim. Faros has inverted COI (sells governance tooling, benefits from alarm, not reassurance). he-2026 is a single, self-selected, explicitly "upper envelope" firm.

## 6. VERDICT: CONTESTED — medium confidence

The throughput flip happened inside one self-report instrument whose construct was redefined the year before, and cannot be adjudicated as real change versus artefact from the primary texts alone. The stability cost is directionally persistent across every instrument that has looked, but unmeasured in magnitude and non-comparable in the one dataset that does use telemetry (he-2026, which shows the opposite on revert rate). The "it's temporary" narrative has zero longitudinal support and comes from the least independent source in the set. Medium rather than low confidence because direction is unusually well triangulated; not high because no source can put a trustworthy number on it, and the one rigorous causal study measures a more reassuring construct than the alarming ones.

## 7. What would change the verdict

A DORA 2026 annual report repeating the same self-report items would turn a two-point flip into a real trajectory. Any organisation publishing DORA-style throughput *and* stability metrics from telemetry, pre/post agentic adoption, with he-2026-level identification rigour, would let both halves finally be tested against each other in one population.

## 8. Feeds exec brief as

The throughput story has already flipped once inside a single yearly survey and can't be trusted as a trend; the stability cost shows up almost everywhere it's looked for but has never been measured with a number we can act on, so budget for a review/incident-handling cost without believing anyone's current estimate of its size.
