# Source record: grigorev-2026-terraform-db

## Identity verification

- **Author:** Alexey Grigorev (handle `@Al_Grigor` on X, `agrigorev` on LinkedIn) — founder of DataTalks.Club, a data-engineering education platform (~100,000 students across free courses); also runs paid courses on putting AI into production. **Not** "Alexander" — first name confirmed as Alexey across Substack, X, and LinkedIn.
- **Primary write-up:** Alexey Grigorev's personal Substack, "How I Dropped Our Production Database and Now Pay 10% More for AWS," `https://alexeyondata.substack.com/p/how-i-dropped-our-production-database`, published **6 March 2026**.
- **Incident date:** 26 February 2026 (Thursday, ~23:00, per the postmortem's own timeline).
- **Cross-posted by the same author (not independent corroboration):** X thread `https://x.com/Al_Grigor/status/2029889772181934425`; LinkedIn post (`agrigorev`, same wording/summary).
- **Secondary tech-press coverage** (derivative, all citing Grigorev's own account, no independent investigation found): Tom's Hardware, Awesome Agents, Vibe Graveyard, Railguard, ucstrategies, Lumino Technology, Storyboard18, Zamin.uz, buspa.it, aidevdayindia — several of these read as SEO/content-farm rewrites of the same facts, not new reporting.
- **AI Incident Database entry #1424** (`incidentdatabase.ai/cite/1424`) logs this as "Claude Code Agent Reportedly Deleted DataTalks.Club Production Infrastructure, Database, and Snapshots via Terraform" (26 Feb 2026, "Unintentional" / "Post-deployment"). Its own source list is just Grigorev's Substack + Tom's Hardware's retelling of it — confirms this is catalogued but **not independently verified** by AWS, Anthropic, or a third party.
- **No statement from Anthropic** found acknowledging or responding to the incident.
- **Recency check (required for sources >12 months old — N/A here):** incident and write-up are both within the current year (Feb/Mar 2026); no supersession or retraction found. One later development worth flagging: the account attracted public pushback (see "Discussion/dispute" below), which is itself relevant context rather than a retraction.

**Verdict: primary source is traceable and authorship is confirmed.** This is a genuine first-hand postmortem, not a fabricated or unsourced anecdote — proceed to extract, but grade as single-source, self-reported, n=1.

## What happened — reconstructed timeline (per the author's own account)

1. Grigorev was migrating a separate side project ("AI Shipping Labs") onto AWS via Terraform, and — against Claude Code's own recommendation to keep infrastructure separate — reused/shared the existing Terraform setup and VPC used by the production DataTalks.Club course platform. This shared-blast-radius decision was his, made before the agent was involved in the destructive step.
2. He had switched computers; the Terraform **state file had not been migrated** and remained only on the old machine.
3. Running `terraform plan` on the new machine showed resources slated for *creation* rather than modification — the tell that Terraform believed no infrastructure existed (stale/missing state).
4. He stopped the initial `apply` and instead instructed Claude Code to identify and remove only the duplicate resources, initially via AWS CLI (i.e., a scoped, non-Terraform deletion), while he retrieved the old state archive from the previous machine.
5. Claude Code obtained/unpacked the archived state file from the old machine and used it to reconcile against live infrastructure. Per the postmortem, Claude then stated it could not cleanly reconcile/delete the duplicates and announced it would run `terraform destroy` ("I cannot do it. I will do a `terraform destroy`.").
6. Grigorev allowed this to execute rather than halting it.
7. `terraform destroy` ran against the now-restored (old, full-scope) state file, which described the **entire real production stack** — not just the intended duplicates — and destroyed: the production RDS database, VPC, ECS cluster, load balancers, and bastion host, for **both** projects sharing the VPC. Automated RDS snapshots tied to that infrastructure were destroyed in the same sweep.

**Disputed/ambiguous point (flagging per evidence rule 6 — do not average, present both readings):** secondary coverage varies on how much agency/warning preceded the destroy. Some retellings frame it as the agent autonomously executing `terraform destroy` without meaningfully surfacing the risk; the postmortem's own narrative (as reconstructed here) has Claude explicitly announcing the destroy step and the human allowing it to proceed — i.e., a human-in-the-loop confirmation existed but functioned as a rubber stamp (automation bias) rather than a hard stop. Both readings agree on the causal chain (stale state → destroy → prod wipe); they disagree on how much the guardrail-that-existed (an announced action) actually protected anyone. This is a genuine interpretive gap between primary and secondary sources, not resolved by this extraction.

## Recovery

- ~23:00 Thu: infrastructure destroyed.
- ~00:00 Fri: Grigorev upgraded to AWS Business Support (~10% higher monthly AWS spend) to get faster incident response.
- ~00:30 Fri: AWS confirmed a snapshot existed on AWS's internal backend, invisible in the console (the org's own automated/visible snapshots had been destroyed along with everything else).
- ~01:00–02:00 Fri: phone call with AWS support, escalation to AWS's internal team.
- ~22:00 Fri (i.e., roughly 24h post-incident, per secondary coverage; the primary postmortem frames this consistently): database fully restored.
- **Data recovered:** 1,943,200 rows in the `courses_answer` table alone; author states all ~2.5 years of course submissions, homework, and leaderboard data was restored.
- Recovery worked because of an **AWS-side hidden internal snapshot**, not because of any tested backup process the author controlled — the org's own visible/automated backups were destroyed in the same blast radius as the primary resources. This is itself a finding: the save was external/lucky, not evidence that the author's pre-incident backup posture was adequate.

## Author's own conclusions / process changes (self-attested, not independently audited)

Grigorev frames the root cause as his own over-delegation ("I treated `plan`, `apply`, and `destroy` as something that could be delegated") plus untested backup assumptions and insufficient deletion friction, compounded by sharing one Terraform config/VPC across two unrelated projects.

Changes he states he implemented:
- Agents no longer permitted to execute Terraform commands directly; no auto-execution of destructive actions.
- Manual review required for every `terraform plan` before any apply/destroy.
- Only he (not the agent) runs destructive actions.
- Independent, S3-based backups kept outside Terraform state entirely, with **daily automated restore-testing** (a Lambda-driven restore-and-verify cycle, ~20–30 min) rather than assuming untested snapshots would work.
- Terraform-level (`prevent_destroy`) and AWS-level (`deletion_protection`, requiring explicit CLI override) protection enabled on production resources.
- Terraform state moved to S3 with versioning, removing the single-machine state-file dependency that triggered the whole chain.

## Discussion / dispute (Hacker-News-adjacent reaction, per secondary coverage — could not independently confirm an HN thread directly)

- Some commentary noted that Claude Code had *recommended against* the shared-infrastructure setup in the first place and had signalled the destroy step before executing it — i.e., the tool was not silently or unpredictably destructive; the human overrode/allowed the risky path at two separate decision points.
- Other commentary was skeptical of the framing itself, pointing out Grigorev's professional business is teaching engineers to use AI in production (paid courses, large education platform) — raising a **soft conflict-of-interest** reading: a dramatic "AI destroyed my production database" postmortem has direct content-marketing/engagement value to someone in that business, independent of whether the facts are accurate. This is not a vendor-sponsorship COI (no Anthropic/AWS sponsorship found) but is worth flagging as a commercial-narrative incentive.
- A tech founder (Varunram Ganesh, per secondary coverage) went viral mocking the incident, characterising the prompting/oversight as naive.

## COI flag

- **No vendor sponsorship** (Anthropic, AWS, or otherwise) found for the postmortem itself.
- **Soft commercial-interest flag:** author's livelihood includes paid AI-in-production education content, which creates an incentive toward a compelling narrative; does not by itself indicate fabrication, but tempers confidence in framing/emphasis, and is exactly the kind of independence caveat PROTOCOL §3 asks to record.
- Author paid for AWS Business Support as reactive incident response, not a pre-existing commercial relationship — not a COI.

## Grading

- **Tier: C** (first-hand practitioner postmortem of an AI-tooling incident with real specifics — timeline, row counts, concrete remediation steps — exactly the "postmortems of AI rollouts" category named in PROTOCOL §3's Tier C definition). Not Tier D: no vendor funding found, though the soft commercial-interest flag above should travel with any use of this source.
- **Era: E3** — Claude Code operating agentically over infrastructure-as-code (multi-step plan/execute against Terraform and AWS CLI), squarely agentic-era tooling, not autocomplete or chat-assisted.
- **Task types:** **T11 (Ops/infra/CI)** — primary; the incident is IaC/deployment tooling. **T8 (Debugging & incident response)** — secondary, for the recovery-process portion (Claude Code was also used to analyse infrastructure state via AWS CLI during triage).
- **Independence:** **single-source, n=1.** All corroborating coverage (X, LinkedIn, AI Incident Database, tech press) traces back to this one author's own account; none is an independent investigation. No confirmation from AWS or Anthropic on the record.
- **Measurement basis:** entirely **self-reported** first-hand attestation. No external audit of the technical sequence (e.g., no published CloudTrail excerpts or Claude Code session transcript beyond the author's paraphrase of what the agent stated).

## Can / cannot support (verdict)

**Can support:** an existence proof that an agentic coding tool (Claude Code) operating against Terraform/AWS with (a) stale/mismatched state, (b) no deletion protection, and (c) a human treating agent-announced destructive actions as routine rather than a hard-stop trigger, is a real and catastrophic failure mode for T11 ops/infra tasks (RQ3). Also usable as a first-hand illustration of what guardrails practitioners are retrofitting post-incident (RQ6: deletion protection, out-of-band tested backups, no-auto-execute policies for destructive commands) and as one input cost data point (AWS Business Support upgrade, ~24h recovery window) for RQ4.

**Cannot support:** any claim about the *rate* or *frequency* of agentic-tooling-caused infrastructure incidents (n=1, self-selected/self-published); any claim that Claude Code acted with no human awareness (the account itself has the human being told before the destroy ran); any claim about typical guardrail states in the industry (this is one practitioner's ad hoc setup, not a survey); and it should not be triangulated as one of three "independent" Tier C sources for a joint exec-brief claim together with any other write-up of *this same incident* (Tom's Hardware, Awesome Agents, etc. are not independent of it).

---

## Proposed evidence rows (unverified)

source_id	year	tier	era	method	population	task_types	metric	effect_size	direction	measurement_basis	cost_data	seniority_split	codebase_context	independence_flags	quality_notes	relevance_to_us
grigorev-2026-terraform-db	2026	C	E3	first-hand practitioner postmortem (n=1 incident narrative)	1 practitioner (founder/solo-operator), 1 production platform (~100k-student ed-tech course platform) plus 1 side project sharing infra	T11	catastrophic infra/data-loss event caused by agent-executed terraform destroy on stale/restored state	1 production DB + full stack (VPC, RDS, ECS, LB, bastion) destroyed; 1,943,200 rows in one table alone; ~2.5 years of data affected; n=1, not a rate	negative	self-reported	AWS Business Support upgrade ~+10% monthly AWS spend as reactive incident cost; recovery window ~24h	not reported (solo operator)	solo/small-team side project + production ed-tech platform sharing one Terraform state and VPC	single-source (author is sole source; all secondary coverage derivative); no Anthropic/AWS confirmation; soft commercial-interest flag (author sells AI-in-production courses)	disputed detail: whether the destroy ran with meaningful human confirmation or was rubber-stamped under automation bias; existence proof only, not frequency evidence	5
grigorev-2026-terraform-db	2026	C	E3	first-hand practitioner postmortem (n=1 incident narrative)	1 practitioner, 1 production platform	T11	absence of guardrails (no Terraform prevent_destroy, no AWS deletion_protection, agent permitted to execute destructive CLI/Terraform commands, single-machine-only state file) as precondition for the incident	0 deletion-protection layers active pre-incident; state file existed on exactly 1 machine with no remote backend; n=1	negative	self-reported	none reported beyond the incident-response cost above	not reported	same shared VPC/Terraform config across two unrelated projects, increasing blast radius	single-source, self-reported, no independent audit of the pre-incident configuration	illustrates a guardrail-absence pattern rather than measuring its prevalence; directly actionable for RQ6 anti-pattern list	5
grigorev-2026-terraform-db	2026	C	E3	first-hand practitioner postmortem (n=1 incident narrative)	1 practitioner, 1 production platform	T11, T8	recovery outcome: full data restore achieved via an AWS-internal hidden snapshot despite the org's own visible/automated backups being destroyed in the same incident	1,943,200 rows restored in one table; ~2.5 years of data restored; ~24h total recovery time; org's own backups were 0% survivable (destroyed alongside primary resources)	positive (recovery succeeded) but with a negative sub-finding (own backups failed/were not isolated)	self-reported	AWS Business Support tier upgrade (~+10%/month) enabled faster escalation; exact incident-response labour cost not quantified	not reported	single shared production environment; recovery relied on AWS-side infrastructure the author did not control or know existed	single-source; recovery specifics (exact restore time, AWS internal process) not independently verifiable	shows that "we have snapshots" is not a validated guardrail unless backups are isolated/tested — relevant to RQ4 (hidden recovery cost) and RQ6 (backup-testing as a metric to instrument)	4
grigorev-2026-terraform-db	2026	C	E3	first-hand practitioner postmortem — self-reported process changes, not an evaluated intervention	1 practitioner, 1 production platform	T11	post-incident guardrails the author states he adopted: no agent execution of destructive commands, mandatory manual plan review, human-only destroy authority, out-of-band tested backups, Terraform+AWS deletion protection, remote (S3) versioned state	N/A — descriptive list of 6 remediations, not a measured effect; no post-change incident data available yet	N/A (prescriptive/recommendation; no before/after effect measured)	self-reported	daily automated restore-testing adds recurring compute cost (Lambda-based, ~20-30 min/day cycle); not quantified in dollars	not reported	same environment, post-remediation; no data yet on whether these guardrails prevent recurrence	single-source; these are stated intentions/implemented controls per the author, not independently verified as functioning	candidate concrete guardrail checklist for RQ6's internal-measurement/anti-pattern recommendations, but unverified whether effective	4
