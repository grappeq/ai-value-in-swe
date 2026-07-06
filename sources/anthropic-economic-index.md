# Source: Anthropic Economic Index (report series, 2025–2026)

source_id: `anthropic-economic-index`
Phase 0 anchor verification. Extraction depth: verification + headline findings (full per-finding extraction deferred to Phase 2 if triaged in).

## Citation(s)

The Economic Index is a continuing series, not a single report. Editions as of July 2026:

1. **"Introducing the Anthropic Economic Index"** — Anthropic, 10 February 2025. https://www.anthropic.com/news/the-anthropic-economic-index
   Accompanying paper: Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., Ganguli, D. (2025). *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations.* arXiv:2503.04761 (v1, 11 Feb 2025). https://arxiv.org/abs/2503.04761
   Open dataset: https://huggingface.co/datasets/Anthropic/EconomicIndex (release 2025-02-10 and subsequent).
2. **"Anthropic Economic Index: Insights from Claude 3.7 Sonnet"** — Anthropic, 27 March 2025. https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7 *(citation verified via dataset README and search; page not fully fetched — see Verification status)*
3. **"Anthropic Economic Index: AI's impact on software development"** — Anthropic, 28 April 2025. https://www.anthropic.com/research/impact-software-development
   **This is the core software-engineering edition** (first Claude Code analysis). No named authors on page.
4. **"Anthropic Economic Index report: Uneven geographic and enterprise AI adoption"** — Appel, R., McCrory, P., Tamkin, A. (lead); McCain, M., Neylon, T., Stern, M. Anthropic, 15 September 2025. https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
5. **"Anthropic Economic Index report: Economic primitives"** — Appel, R., Massenkoff, M., McCrory, P. (lead); McCain, M., Heller, R., Neylon, T., Tamkin, A. Anthropic, 15 January 2026. https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
   Companion research page: "New building blocks for understanding AI use" — https://www.anthropic.com/research/economic-index-primitives ; authors PDF: https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf
6. **"Anthropic Economic Index report: Learning curves"** — Massenkoff, M., Lyubich, E., McCrory, P. (lead); Appel, R., Heller, R. Anthropic, 24 March 2026. https://www.anthropic.com/research/economic-index-march-2026-report
7. **"Anthropic Economic Index report: Cadences"** — Massenkoff, M., Lyubich, E., Sacher, S., Hitzig, Z., Zhang, S., Heller, R., McCrory, P. Anthropic, 26 June 2026. https://www.anthropic.com/research/economic-index-june-2026-report — **most recent edition as of July 2026.**

Series hub: https://www.anthropic.com/economic-index (last updated 26 June 2026).
Dataset releases per Hugging Face README: 2025-02-10, 2025-03-27, 2025-09-15, 2026-01-15, 2026-03-24, 2026-06-26 (the April 2025 SWE report is a special report without its own dataset release entry).

## Verification status

**VERIFIED** (series existence, all edition dates, canonical URLs, accompanying paper, and headline figures for editions 1, 3, 4, 5, 6, 7 confirmed from the primary pages on 2026-07-06). Edition 2 (March 2025) is PARTIALLY VERIFIED: date and title confirmed via the dataset README and search results, but the page itself was not fully fetched; its findings are not extracted here and must not be cited beyond citation-level detail.

## Tier, era, independence

- **Tier: D (vendor).** **COI FLAG — prominent:** Anthropic analysing usage of Anthropic's own products, published by Anthropic's own economic research team. Every figure serves, at minimum, a narrative interest in demonstrating economic significance of Claude. Population is exclusively Claude users (early-adopter skew acknowledged by the authors). Use for directional signal and hype-baseline characterisation only; never carries a claim alone (PROTOCOL §3, §8).
- **Era: split by product surface, per the era-assignment rule (modality, not year):**
  - Claude.ai chat conversations → **E2** (chat-assisted).
  - Claude Code sessions → **E3** (agentic). The April 2025 and June 2026 editions distinguish these explicitly.
  - First-party API traffic (Sept 2025 onward) → mixed/unclassifiable per-conversation; treat as E2/E3-mixed and do not assign E3 findings from API aggregates unless the report itself isolates agentic traffic. The March 2026 report notes Claude Code's agentic architecture splits work into many small API calls, which contaminates naive API task-share comparisons.
- **Independence flags:** vendor-published; self-selected user population; single-vendor lens (Claude only — says nothing about Copilot/Cursor/ChatGPT usage mix); consumer plans only in early editions (Team/Enterprise/API excluded until Sept 2025); privacy-window truncation; June 2026 survey respondents skew heavily to computer/mathematical occupations (30% vs ~4% of US employment) and are stated by the authors to be non-representative.

## Method & population/dataset

- **What it is:** privacy-preserving classification of Claude conversation transcripts using **Clio** (Claude-as-classifier pipeline producing anonymised aggregate insights), mapped to the US Department of Labor **O*NET** task taxonomy (~20,000 tasks), plus bottom-up clustering. From Jan 2026, five "economic primitives" classifiers added: task complexity, human/AI skills, use case, AI autonomy, task success. From June 2026: output-artifact classifiers, hourly sampling, monthly aggregates, and a linked user survey (~9,700 respondents with 5+ sessions, May–June 2026).
- **Populations by edition:** Feb 2025: ~1M (paper: >4M) Claude.ai Free/Pro conversations. Apr 2025: 500k coding interactions, ~evenly split Claude.ai vs Claude Code, collected 6–13 April 2025. Sept 2025: 1M Claude.ai conversations (4–11 Aug 2025) + 1M first-party API transcripts (Aug 2025). Jan 2026: 1M Claude.ai + 1M API transcripts (13–20 Nov 2025). Classifier model upgraded across waves (Sonnet 3.7 → Sonnet 4 → Sonnet 4.5 → Opus 4.5/4.6), a comparability caveat across editions.
- **Critical methodological boundary (bounds everything below):** this is **measured telemetry of usage** — what people ask Claude to do and how they interact. It measures **neither productivity impact nor output quality nor whether the work was accepted/used**. The April 2025 report itself states results "don't reflect actual code quality or productivity improvements". "Automation" here is an interaction-style classification (task delegated in one shot) inferred from transcripts, not evidence the task was completed autonomously or well; apparent automation may involve substantial unobserved human post-editing.

## Key findings (exact figures as reported; all **measured usage telemetry** unless marked survey/self-reported)

**Coding's share of Claude usage** (era: E2 for Claude.ai shares; API mixed):
- Feb 2025: computer & mathematical occupations = **37.2%** of Claude.ai conversations vs **3.4%** of the US workforce; software development + writing together ≈ half of all usage (paper abstract).
- Sept 2025: coding ≈ **36%** of Claude.ai usage; computer/mathematical = **44% of API traffic**.
- Jan 2026: computer/mathematical ≈ **one-third of Claude.ai**, **nearly half of API**; single most prevalent task = "modifying software to correct errors" at **6% of Claude.ai / 10% of API** [T8, arguably T4/T5].
- Mar 2026: coding ≈ **35%** of Claude.ai, "migrating to the API"; top-10 O*NET task concentration on API rose 28% → 33%.
- Jun 2026: code and technical work ≈ **one-sixth of conversations by output type** (new artifact-based classifier — not directly comparable to earlier occupational shares).

**Automation vs augmentation split and trend** (interaction-style classification, not impact):
- Feb 2025: **57% augmentation / 43% automation** (Claude.ai overall).
- Mar 2025: reported no change in the balance (citation-level only — edition not fully fetched).
- Apr 2025 (SWE special): **Claude Code 79% automation / 21% augmentation** vs **Claude.ai 49% / 51%** [E3 vs E2 — first agentic-modality datapoint]. Directive interactions: Claude Code 43.8% vs Claude.ai 27.5%; feedback loops: 35.8% vs 21.3%. Coding work is more automative than non-coding work.
- Sept 2025: first edition where **automation exceeds augmentation on Claude.ai**; directive share jumped **27% → 39%**; API traffic **77% automation** vs ~50% Claude.ai.
- Jan 2026: reversal — augmentation back to **52%** (from 45% in Aug 2025), directive down to **32%**; authors attribute partly to product changes (file creation, memory). **Note: the trend is sensitive to Anthropic's own product releases and classifier changes — do not read as a labour-market trend.**
- Jun 2026: Claude Code sessions score **0.37 points higher AI autonomy** (1–5 scale) than chat/Cowork; blog-post-type tasks: median **13 turns on chat vs 1 prompt on Claude Code**; ~**two-thirds of the autonomy difference attributed to delegation style, not task mix** [E3 vs E2 comparison].

**Task-level breakdown within coding** (Apr 2025 edition; era E2/E3 pooled across the two surfaces):
- Languages: JavaScript/TypeScript ~31%, HTML/CSS ~28%, Python 14%, SQL 6%.
- Top coding uses: UI/UX component development **12%**, web & mobile app development **8%** [T3-leaning greenfield/application work; the dominant observed use is *not* mature-codebase feature work — relevant to RQ5 framing, though usage share cannot establish where value lies].
- Claude Code usage skews to startups: **32.9% startup vs 23.8% enterprise** work on Claude Code.

**Claude Code / agentic-specific (E3-relevant):**
- Apr 2025: 79/21 automation split (above); Claude Code users use it more for automation-style delegation than chat users.
- Mar 2026: agentic architecture decomposes coding work into many small API calls (measurement artefact warning for API shares).
- Jun 2026: **54% of Claude Code sessions use Opus-class models vs 10% of chat/Cowork**; Claude Code sessions classified "automated" exceed chat/Cowork rates.

**Other era-independent items of protocol relevance:**
- Jan 2026: Claude task success ≈ **67%** on Claude.ai overall, declining with task complexity (~70% simple vs ~66% college-level) — *classifier-judged success, not ground truth*.
- Mar 2026: high-tenure users (6+ months) show **~10% higher conversation success rate**, ~3–4 pp after controlling for task type — learning-curve/cohort caveats acknowledged.
- Jun 2026 (survey, **self-reported**, non-representative sample): >1/3 expect AI to handle "most or nearly all" work tasks within 12 months; 57% say AI increased their skills' market value; 10% rate own job loss likely. Authors flag reported exposure systematically exceeds observed exposure — a perception–reality gap datapoint for RQ2/RQ6, though within a vendor survey.

## What this can and cannot support

Can support: directional claims about *what Claude users ask Claude to do* (usage composition, interaction styles, the E2-vs-E3 delegation contrast) and the vendor hype baseline. Cannot support: any claim about productivity, quality, value delivered, or labour-market impact — **usage share ≠ value delivered**, "automation" ≠ successful autonomous completion, and every trendline is confounded by Anthropic's own product and classifier changes. Tier D: never carries an exec-brief claim alone.

## Corrections vs the seed description (PROTOCOL §6)

1. Seed said "Anthropic Economic Index 2025–2026" as if a report or two; it is **seven distinct editions** (Feb, Mar, Apr, Sept 2025; Jan, Mar, Jun 2026) plus a founding arXiv paper and an open dataset. The seed missed the dedicated **April 2025 software-development special report**, which is the single most protocol-relevant edition (first Claude Code / E3 analysis).
2. Seed framing "software engineering heavily represented" verified: 35–37% of Claude.ai conversations, up to ~44–50% of API traffic.
3. Seed framing "automation vs augmentation patterns" needs correction: the split is **not stable** — 57/43 augmentation-leaning (Feb 2025) → automation-majority (Sept 2025) → back to 52% augmentation (Jan 2026), with the authors themselves attributing swings partly to product changes. Any single snapshot is misleading.
4. Not in the seed: the Jan 2026 "economic primitives" framework (incl. task success rates) and the Mar 2026 learning-curve finding — both potentially useful methodology inputs for RQ6.

## Follow-up leads (NOT extracted)

- OpenAI, "How People Use ChatGPT" — Chatterji et al., NBER WP 34255 (Sept 2025). https://www.nber.org/system/files/working_papers/w34255/w34255.pdf — the directly comparable vendor usage index (Tier D hype-baseline set); consumer non-work share rose to 73% by June 2025.
- OpenAI, "GPTs are GPTs" (exposure estimates). https://openai.com/index/gpts-are-gpts/ — exposure-index genre anchor, Tier D.
- OpenAI, "ChatGPT usage and adoption patterns at work". https://openai.com/business/guides-and-resources/chatgpt-usage-and-adoption-patterns-at-work/ — vendor workplace-usage companion, Tier D.
- Strauss, I., "anthropic-econ-critique" (GitHub). https://github.com/IlanStrauss/anthropic-econ-critique/blob/main/BLOG_POST.md — third-party methodological critique of the AI Usage Index's cross-country comparisons.
- "Claude Just Refereed the Anthropic Economic Index" (Empiricrafting Substack). https://empiricrafting.substack.com/p/claude-just-refereed-the-anthropic — informal critique; triage before use.
- Evaluating Claude adoption in healthcare occupations (PMC12143583). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12143583/ — independent academic reuse of the Clio/Economic Index approach; methodology-validation lead.
- Anthropic open dataset. https://huggingface.co/datasets/Anthropic/EconomicIndex — enables independent re-analysis; check for third-party papers built on it.

## Recency check notes

Checked 2026-07-06. The series is actively maintained; the June 2026 "Cadences" edition (26 June 2026, ten days old) is current. Earlier editions are superseded for *levels* (classifier and product-mix changes break comparability) but remain citable for the within-edition contrasts noted above, especially the April 2025 Claude Code vs Claude.ai comparison, which no later edition repeats in the same form (the June 2026 autonomy-score analysis is its closest successor). No retractions found; third-party critiques located are methodological, not correction-forcing.
