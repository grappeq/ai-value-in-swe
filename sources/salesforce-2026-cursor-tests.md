# Source: Salesforce Engineering Blog — "How Cursor AI Cut Legacy Code Coverage Time by 85%"

## Identity

- **URL:** https://engineering.salesforce.com/how-cursor-ai-cut-legacy-code-coverage-time-by-85/
- **Publisher:** Salesforce Engineering Blog (engineering.salesforce.com) — Salesforce's own first-party engineering blog, not a third-party aggregator.
- **Authors:** Rachna Singh (Senior Director of Software Engineering, Einstein Activity Capture), Percy Mehta, Spencer Ho — all identified as Salesforce engineering staff, not Cursor/vendor employees.
- **Publication date:** 18 August 2025.
- **Format:** Q&A-style interview article with section headers (see below), not a data-driven technical report. No charts, no raw telemetry tables, no methodology appendix.
- **Article structure (headers):**
  1. How Cursor AI Cut Legacy Code Coverage Time by 85%
  2. What is your team's mission?
  3. What legacy code coverage challenges did Cursor AI solve for distributed repositories?
  4. What productivity barriers were slowing AI-assisted code coverage efforts before Cursor?
  5. What technical obstacle emerged when generating meaningful unit tests with Cursor AI?
  6. How do you balance rapid AI code generation with enterprise code quality standards?
  7. Learn more / Related Articles

**Recency check:** published 18 August 2025, ~11 months before today (2026-07-17) — just inside the 12-month recency-check threshold, so not strictly required, but I searched anyway. No retraction, correction, or superseding Salesforce post found. A related, later Salesforce post exists ("How AI Test Automation Cut Productivity Bottlenecks by 30%") but it is a distinct piece, not a correction of this one — flagging as a related source worth a separate extraction if in scope, not cross-checked in depth here.

## Context / what the project was

- Team: Einstein Activity Capture (EAC) engineering team, plus an adjacent "EAP" set of repositories.
- Codebase origin: inherited from the **RelateIQ acquisition** — "a legacy codebase from the RelateIQ acquisition with extremely low test coverage — some repositories were below 10%." Languages: "mostly written in Java, Scala and Kotlin." Spread across many distributed GitHub repositories, with the article noting "limited knowledge" among current engineers of this inherited code (implicit-knowledge-loss framing).
- Trigger: "When Salesforce introduced the 80% code coverage mandate, the team recognized an opportunity to leverage AI-powered development tools like Cursor to optimize their testing workflows."
- Scope: 62 EAC repositories + 14 EAP repositories (76 total), reaching 80% code coverage.
- A separate throughput figure is given for part of the effort: "produced 180,000 lines of code in just 12 days by replicating patterns" (this appears to describe the template-replication phase, not the whole 26→4 day figure — the article does not clearly link the two numbers, which is itself a clarity gap worth flagging).

## Finding 1 — headline effort-reduction figure (26 → 4 engineer-days)

- **Exact quote (title/intro):** "reduced unit test development time from 26 engineer days per module to just 4 days"
- **Exact quote (body):** "Cursor delivered dramatic acceleration, reducing the effort from 26 engineer days per repository to just 4 engineer days — an 85% improvement in productivity."
- **Note on internal inconsistency:** the article itself is not internally consistent about the unit — the title/intro says "per module," the body says "per repository." Neither is defined (a "module" and a "repository" are not stated to be equivalent in this codebase, and no repository/module count-to-effort mapping is given). This ambiguity should be preserved, not silently resolved, when this figure is cited downstream.
- **Measurement basis: NOT STATED / narrative estimate, not measured telemetry.** The article provides **no methodology, no timesheet data, no ticketing/telemetry source, and no explicit statement that this is an average, a single project's before/after, or a rough recollection.** There is no "we tracked X hours in Jira" or "based on N repositories measured before and after" language anywhere in the piece. This is a bare, unsourced narrative claim delivered as a soundbite in a marketing-adjacent Q&A post.
- **Absence flagged as a finding (per evidence rule 3):** no denominator is given for how many repositories/modules this 26-day baseline was computed over, no variance/range, no confidence interval, and no independent verification method (e.g., git history mining, time-tracking system) is cited. This is a **self-reported, single-org, unaudited estimate** presented with press-release precision (an exact "85% improvement").
- **Can support:** a directional, Tier C practitioner data point that legacy/brownfield test-authoring effort can drop substantially with an agentic coding tool, under specific enabling conditions (see below).
- **Cannot support:** any quantitative claim about typical or expected effort reduction, any claim generalisable beyond this one team/codebase, or any claim that this was measured rather than recalled/estimated.

## Finding 2 — outcome/quality data accompanying the effort claim

- **Exact quote:** "The team also successfully achieved 80% code coverage spanning 62 Einstein Activity Capture repositories and 14 EAP repositories."
- Before-state: "some repositories were below 10%" coverage.
- **This is coverage-percentage outcome data, and it is reported** — so the effort figure is *not* entirely unaccompanied by an outcome metric. However:
  - No defect/bug-rate data is reported as an outcome metric (see Finding 4 for a related but distinct bug-discovery anecdote, which is not a systematic defect-rate comparison).
  - No data on test flakiness, test runtime, maintenance burden, or whether the 80% figure held up over subsequent releases (durability of the coverage gain is not reported).
  - Coverage percentage is a quantity metric (lines/branches touched), not a quality metric — the article itself acknowledges this tension in Finding 3 below, but does not resolve it with data (e.g., no mutation-testing score, no count of assertions per test, no post-hoc defect-escape comparison).
- **Absence flagged as a finding:** no quality/defect outcome data is given that would let a reader distinguish "80% coverage of meaningful tests" from "80% coverage of superficial tests," despite the article explicitly naming that risk (see Finding 3).

## Finding 3 — the article's own admission of a coverage-vs-meaningfulness tension, and the mitigation described

- **Exact quote:** "The main challenge was mastering effective prompting techniques and context management to guide Cursor in generating meaningful tests, rather than just hitting surface-level coverage metrics."
- **Exact quote (verification step):** "Engineers manually reviewed all generated code, checking test intentions through AI-generated JavaDoc comments and ensuring that the tests covered meaningful functionality, not just superficial coverage."
- This is an **enabling-condition / verification-harness finding**: the reported effort reduction was achieved *with* a mandatory human-review step per generated test, not via unsupervised generation. The review method described is inspection of AI-generated JavaDoc comments plus manual judgement of functional meaningfulness — not automated mutation testing or independent QA sign-off.
- **Can support:** a mechanism-level point (RQ3/RQ6-relevant) that human review remained a required step even where large effort reductions were reported — i.e., the reported time saving is net of at least some review overhead, though the review time itself is not separately quantified (a cost-profile gap, relevant to RQ4).
- **Cannot support:** any claim that the 26→4 day figure represents "hands-off" AI generation, or that review overhead is captured/excluded transparently in that figure — the article does not say whether review time is included in the "4 days," which is a material ambiguity for RQ4 cost-profile purposes.

## Finding 4 — incidental defect discovery (not a systematic defect-rate finding)

- **Exact quote:** the AI-assisted test-writing process "uncovered existing bugs in production code," with one named example: "a health check logic error where an AND condition should have been an OR."
- This is a **single anecdote**, not a counted/systematic defect discovery rate. No total count of bugs found this way, no severity classification, no comparison to a baseline (e.g., bugs found per KLOC by manual test-writing historically).
- **Can support:** a plausible mechanism note that generating tests for previously-untested legacy code can surface latent defects as a side effect — consistent with, but not independent confirmation of, similar anecdotes elsewhere in the literature.
- **Cannot support:** any effect-size claim about defect-discovery rate.

## Finding 5 — enabling conditions / what made this work (process detail)

- **Exact quote (initial failure mode):** the tool initially "went rogue, modifying hundreds of files at once and making drastic changes that required complete rollbacks."
- **Exact quote (fix — narrowing scope):** "The team refined their approach by focusing on one class at a time instead of giving broad, generic instructions. They used Cursor's interface to select specific files and provide targeted guidance."
- **Exact quote (template replication for homogeneous files):** "For files with similar structures, like data transfer objects, they created initial templates and instructed Cursor to replicate these patterns across hundreds of similar files. This method achieved 90-99% accuracy, allowing for the rapid generation of meaningful tests."
- **Exact quote (agentic failure mode requiring manual intervention):** the article separately describes "cyclic loops where Cursor would repeatedly attempt compilation fixes," which needed manual intervention to break.
- **Interpretation (not a quote):** this describes an agentic (plan/generate/compile/fix-loop) mode of use, consistent with Cursor's agent mode rather than pure autocomplete or copy-paste chat — supports an **E3** era tag. However, the article never explicitly names "agent mode" versus "chat" versus "autocomplete" — the E3 assignment rests on inferred behavioural description (multi-file edits, autonomous compilation-fix loops, template-driven bulk generation across hundreds of files), not an explicit tool-mode label. This inference should be treated as **medium, not high, confidence** on the era tag mechanism, though the described behaviour (autonomous multi-step loops needing a human to interrupt them) is difficult to reconcile with E1/E2 tooling.
- **Task-structure enabling condition:** effort reduction was concentrated in **structurally homogeneous, repetitive file types** (data transfer objects / similar-structure classes) where a template could be replicated hundreds of times at 90-99% accuracy — i.e., the best gains map to low-complexity, pattern-repeating code, not arbitrary complex legacy logic. This is directly relevant to PROTOCOL §5 tension 2 (greenfield/low-complexity vs. brownfield/complex split): even within a "legacy brownfield" codebase, the reported gains cluster in the more template-like, lower-complexity subset of files, which is consistent with the tension rather than a counterexample to it.

## Vendor relationship / COI assessment

- The primary post itself (engineering.salesforce.com) is **authored by named Salesforce engineering staff**, not Cursor employees, and contains no visible sponsorship disclosure, co-branding banner, or "in partnership with Cursor" language in the body text as fetched.
- However, cross-referencing found a **separate, later Cursor-published customer case study**: https://cursor.com/blog/salesforce ("Salesforce accelerates velocity by over 30% and ships higher-quality code with Cursor"), byline "Cursor Team," published **21 January 2026** — i.e., roughly five months *after* the Salesforce engineering post. That Cursor-authored piece:
  - Explicitly cites the same "85% reduction in legacy test coverage time" figure, sourcing it back to the Salesforce engineering blog post being extracted here.
  - Adds further figures not present in the Salesforce post: "75% engineering adoption at Salesforce," "30%+ PR velocity increase," and unspecified "double-digit increases" in cycle time, quality, and throughput.
  - Contains direct quotes from **Shan Appajodu, SVP of Engineering at Salesforce** (a different, more senior individual than the three named authors of the original post), e.g. "It's 0 to 1 in terms of how Cursor has transformed the way our developers use tools."
- **This establishes an active vendor customer-reference relationship between Salesforce and Cursor** (Salesforce leadership giving on-record quotes for Cursor's own marketing blog), even though the specific 26→4 day figure originates on Salesforce's own domain under Salesforce authorship. **COI flag: MEDIUM** — not a Tier D vendor post itself, but the source organisation has a subsequent, visible commercial reference-customer relationship with the tool vendor, which is a relevant incentive to consider when weighing how polished/rounded ("85%," precise percentages, no caveasted variance) the reported figures are. This should be recorded and carried forward wherever this figure is cited.

## Tier and era grading

- **Tier: C** (named organisation, real numbers, credible engineering blog, first-party — matches PROTOCOL §3 Tier C definition precisely: "Engineering-org case studies with real numbers, credible engineering blogs"). Not Tier D — authorship is Salesforce's own engineering staff, not the vendor — but the COI flag above should travel with any citation of this figure, and per §3 a single Tier C source supports **directional claims only**, not an exec-brief-carrying claim, absent ≥3 independent corroborating Tier C sources.
- **Era: E3 (agentic)**, medium confidence on the mechanism-inference (see Finding 5) — behavioural description (multi-file edits, autonomous compile-fix loops, bulk template replication, "went rogue" file-modification incident) is consistent with an agentic tool mode, but the article never uses the words "agent mode" explicitly.
- **Independence:** single-organisation, single-team (Einstein Activity Capture) self-report. Not independently audited. No triangulating second source found in this session covering the *same* 26→4 figure from a non-Salesforce, non-Cursor-affiliated source.

## Overall one-line verdict

**Can support:** a Tier C, medium-confidence-mechanism, single-org directional data point that agentic AI tooling can sharply cut test-authoring effort on template-like, low-complexity subsets of a brownfield legacy codebase, when paired with narrowed per-class prompting and mandatory human review — useful as one input toward a ≥3-source triangulated claim on T6 (test authoring) effort reduction, and as an RQ3/RQ5 data point on where in brownfield code gains concentrate (homogeneous/template files, not arbitrary complex legacy logic).

**Cannot support:** any precise, generalisable effect-size claim for exec-brief purposes on its own (no measurement methodology disclosed, unit of "26 days" is internally inconsistent between "module" and "repository," no defect-rate or test-durability data, review-time cost not separately quantified, and a subsequent vendor customer-reference relationship exists that should temper confidence in the round, press-release-quality numbers).

---

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture), 76 repositories (62 EAC + 14 EAP), Java/Scala/Kotlin	T6	unit test authoring effort per repository/module (unit inconsistently reported)	26 engineer-days -> 4 engineer-days (85% reduction)	positive (effort reduction)	self-reported, no methodology disclosed (not measured telemetry, not timesheet-sourced per the text)	no separate cost data; review time not separately quantified from the "4 days"	not reported	legacy brownfield codebase inherited via RelateIQ acquisition, pre-existing coverage <10% in some repos, Java/Scala/Kotlin, distributed across dozens of GitHub repos	single-org self-report; subsequent Cursor vendor customer-reference blog (cursor.com/blog/salesforce, Jan 2026) cites same figure and features Salesforce SVP quotes -> medium COI flag	unit ambiguity (module vs repository) unresolved in source; no variance/N given for the 26-day baseline	3
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture), 76 repositories	T6	code coverage percentage	<10% (some repos) -> 80% across 62 EAC + 14 EAP repos	positive	self-reported / narrative, no audit trail described	not reported	not reported	same as above	same as above	coverage % is a quantity metric only; no mutation-testing/defect-escape/quality-of-test data given alongside it despite the article naming that exact risk	3
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture)	T6	human review requirement for AI-generated tests	engineers "manually reviewed all generated code" incl. AI-generated JavaDoc comments for test intent	n/a (process/enabling-condition finding, not an effect size)	narrative, not quantified	review time cost not separately quantified from the 26->4 day figure -- cost-profile gap	not reported	same as above	single-org self-report	directly relevant to RQ4 cost-profile gap: verification/review overhead exists but is not decomposed from the headline effort number	4
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture)	T6, T5	task-structure enabling condition: gains concentrated in structurally homogeneous/template-like files (DTOs) vs arbitrary complex legacy logic	"90-99% accuracy" replicating templates across hundreds of similar files	positive, but conditional on task homogeneity	self-reported, no accuracy-measurement method disclosed	not reported	not reported	same brownfield codebase	single-org self-report	supports PROTOCOL S5 tension 2 (greenfield/low-complexity vs brownfield/complex): even within "legacy brownfield," gains cluster in template-like low-complexity subset, not complex logic	4
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture)	T6	incidental defect discovery via AI-generated tests (anecdotal, not a rate)	1 named example (health-check AND/OR logic bug); no total count given	positive (anecdotal), null on systematic rate	self-reported anecdote, not a measured defect-rate	not reported	not reported	same brownfield codebase	single-org self-report	absence flagged: no systematic defect-discovery rate or baseline comparison provided despite the anecdote being used to imply a broader quality benefit	2
salesforce-2026-cursor-tests	2025	C	E3	practitioner case study / Q&A interview, single org	1 team (Einstein Activity Capture)	T6	failure modes requiring human intervention: uncontrolled multi-file edits requiring full rollback; cyclic compilation-fix loops requiring manual break	n/a (qualitative failure-mode finding)	negative (friction/failure evidence, recorded per evidence rule 3)	narrative	not reported	not reported	same brownfield codebase	single-org self-report	directly relevant to RQ3 failure map: early rollout attempts with broad/generic instructions caused uncontrolled changes; narrowing scope to one class at a time was required to make the tool usable	4
