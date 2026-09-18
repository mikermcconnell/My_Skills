# AI Efficiency Watch — News Radar V3

Contract version: 1.0. Activated: 2026-09-18. Lane ID: `AI_EFFICIENCY_WATCH`.

## Purpose and authority

Detect whether companies USING AI are doing more useful work with the same or fewer resources, before the full financial impact is obvious. Seek early operating evidence, not only reported earnings and not only AI vendors. Treat the efficiency-wave thesis as a hypothesis to test, not a conclusion to promote.

This is the eleventh mandatory specialized lane. Run inside the existing 08:00, 11:30 and 15:00 America/Toronto Radar slots. Preserve portfolio defense, all ten existing specialized lanes, the broad scan, source provenance, five gates and stage boundaries. No separate alert task, portfolio trade, automatic thesis approval or valuation change is authorized.

The existing research rubric is `mikermcconnell/Investor/docs/ai_efficiency/research_rubric.md` (v1.0 when checked on 2026-09-18). Read its current version and applicable company/tranche work before a substantial RWC handoff. Its scores, categories and promotion rules remain unchanged. The evidence stages below are NOT replacements for that scoring system. A repository research snapshot is not current live portfolio or Mind Model state.

## Preflight and coverage

Use MikeInvestor `get_investor_context`, preserving `stateVersion`; use `get_security_context` for serious issuer-specific work. Load the live TaskTracker Mind Model through a discovered authenticated read when available. Link only actual returned thesis/pillar/forecast IDs. If it is unavailable, use `THESIS_LINK_PENDING`; do not invent IDs or infer live approvals from seeds. This lane tests enterprise productivity and value capture, not recursive self-improvement or automatic infrastructure-demand growth.

Load prior lane coverage, cohort, claims, open questions and review dates before discovery. If unavailable, mark the gap and do not claim a clean delta-only scan. Refresh relevant holdings and active research candidates dynamically. Group wrappers, share classes and options by verified economic issuer for breadth counts; unresolved identity remains an explicit limitation.

Initial fixed comparison cohort, selected for workflow/sector coverage rather than favourable AI results:

| Sector | Issuers |
|---|---|
| Banking | JPM, BAC |
| Insurance | PGR, CB |
| Retail and logistics | WMT, UPS |
| Healthcare administration | UNH, CVS |
| Customer operations and services | T, ACN |
| Software and professional workflows | CRM, INTU |

These are research coverage seeds, not endorsed investments or verified efficiency winners. Freeze as `aiew-cohort-2026-09-18-v1`. Add relevant live holdings and rubric candidates as an overlay, not silent replacements in the comparison denominator. Version additions/removals prospectively with reasons and retain a common-cohort comparison. Cover at least one negative/no-result comparator in each sector; do not drop companies because they stop discussing AI.

Every run: check due claims, material held-company risks and fresh disclosures; perform a cheap cross-industry discovery sweep. Rotate deeper cohort checks, persisting last checked time and a resume cursor so every fixed-cohort issuer is covered at least weekly. Do not imply every company was fully researched every run. Urgent portfolio risks outrank backfill.

## Sources and searches

Primary-source first: annual/quarterly filings; earnings releases and calls; investor days; official operating/engineering reports; attributable customer deployments. Secondary news, vendor case studies and employee observations discover leads, not independent confirmation. Preserve source origin separately from `COMPANY_CLAIM`, `INDEPENDENT_CONFIRMATION`, `DERIVED_CALCULATION`, or `RESEARCHER_INFERENCE` using the normal V3 provenance rules.

Combine company/workflow names with AI, agents, automation, productivity, cost per task/transaction, revenue/output per employee, processing time, human review, error rate, operating leverage, implementation costs and margin. Search challenges too: rework, quality deterioration, reversals, rehiring, AI costs, missed savings and withdrawn metrics. Distinguish `DIGITAL_AI`, `PHYSICAL_AUTOMATION`, `MIXED` and `UNSPECIFIED`; classify vendors' internal deployment separately from sales to customers.

Read the original disclosure. Record publication date, underlying measurement period, first detection and target/review date separately. Old results found during bootstrap are `BASELINE_BACKFILL` or canonical `LATE_DETECTION` when material and previously missed, never new breakthroughs merely because found today. Current independent confirmation of an old claim is a new evidence observation, not a second original claim.

## Evidence stages: one company/workflow/claim at a time

- `ADOPTION`: access, usage, rollout or task involvement only. 90% of tasks involving AI is not 90% of work automated.
- `TARGET`: specific future efficiency promise, with original baseline, scope and due date preserved when disclosed. A target is never an achieved result.
- `OPERATING_RESULT`: a defined useful-output, cost or human-effort improvement is reported for an identified workflow and measurement period. Require a comparable baseline or clearly defined relative change. Missing quality, scope or cost evidence stays visible.
- `FINANCIAL_RESULT`: a separately identified realized revenue/cost/margin/cash effect is reported, with its company/segment scope and AI attribution stated. Do not promote generic margin expansion or multiply gross hours by salary and call it realized savings.
- `REPEATED_RESULT`: comparable beneficial results across at least two distinct measurement periods or independently supported deployments. Record whether the repeated evidence is operating or financial; repeated operating improvement is not financial proof.

Stage describes what was reported, not certainty. Keep verification status and observation direction separate. A company can have several workflows at different stages. Preserve failures, costs and contradictions even for companies with prior strong results. Non-quantified setbacks are valid observations and need no fabricated metric. Source gaps are unknown, not zero and not failure.

## Claim-versus-result record

Use a structured `aiEfficiencyWatch` payload inside the supported research evidence envelope, or an explicitly labelled fallback record. Minimum fields (null plus reason when unknown):

- `schemaVersion`, `laneId`, `claimId`, `eventId`, `parentEventId`, `issuerKey`, `ticker`, `company`, `sector`, `workflow`, `technologyTag`, `adopterOrEnabler`;
- `claimText`, `speaker`, `sourceOrigin`, `claimStatus`, `sourceUrl`, `sourcePublishedAt`, `measurementPeriod`, `firstDetectedAt`, `sourceLocator`, `independenceGroup`;
- `stage`, `verificationStatus`, `direction`, `deploymentScope`, `deploymentScale`, `baseline`, `target`, `actual`, `metricUnit`, `metricDefinition`, `comparablePeriods`;
- `humanReviewIncluded`, `qualityMetric`, `qualityResult`, `aiAttribution`, `confounders`, `grossOrNet`, `implementationAndRunningCosts`, `financialBridge`, `benefitRecipient`, `durabilityRisk`;
- `claimLifecycle`, `targetDate`, `nextCheckDate`, `nextCheckBasis`, `lastCheckedAt`, `outcome`, `missingEvidence`, `thesisLinks`, `rubricVersion`, `nextQuestion`, `persistenceStatus`.

Lifecycle: `OPEN`, `DUE`, `OVERDUE`, `MET`, `MISSED`, `WITHDRAWN`, `UNRESOLVED`. At due date without a result use `OVERDUE` or `UNRESOLVED`, not `MISSED`. Treat a discontinued KPI as `REPORTING_GAP` until clarified. Preserve original targets and append amendments, rather than moving the goalposts. Use the next announced earnings/report date when verified; otherwise nextCheckDate = detection + 30 calendar days and label it an analyst review date, not a company promise. Close as MET/MISSED only against comparable evidence; preserve partial outcomes.

Stable claim identity is economic issuer + normalized workflow + original claim/metric identity + original disclosure date. A revision or realization remains linked to that original claim. Reuse an existing canonical eventId when another lane already owns the same underlying event. A later distinct result may have a new eventId with parentEventId pointing to the original, while claimId remains stable. Never use a new article URL, ticker wrapper, detected date or AI stage as a reason to duplicate the event. Syndications and vendor/customer repetitions of the same measurement share an independence group.

## The economic checks

Ask: Is this useful finished output rather than tokens, code lines or AI seats? Does human time include prompting, supervision, retries, checking and correction? Was quality maintained? Was deployment a pilot, a department, or material company scale? Are layoffs, outsourcing, acquisitions, pricing, mix, demand or ordinary restructuring confounders?

Separate gross capacity freed, time redeployed, costs avoided, realized cash savings, output/revenue growth and net financial impact. Include subscriptions, inference, integration, security, training, human review and ongoing maintenance. Estimate company materiality only with explicit scope and assumptions; do not multiply a pilot result by the whole workforce. Avoid double-counting cost savings and the output created by the same freed hours. Check whether shareholders retain benefits, customers receive lower prices, employees capture them, or vendors/competitors absorb them. Margin gains alone do not prove AI causality; a valuable improvement can still be competed away.

## Escalation and existing handoffs

Surface a first credible scaled operating result early; do not require the next earnings margin to start RWC. Also surface comparable replication, a material financial bridge, target failures, quality deterioration, net costs above benefits, or competitive/revenue pressure on a holding. Generic adoption or a new target normally gets a tracked claim/review date, not a high-priority investment alert. No blanket percentage threshold applies across unrelated workflows.

All surfaced events still pass V3 novelty, materiality, capture, expectations and researchability gates, select ONE supported primary route and the existing controlled `Underwriting Required?` classification. Keep `AI_EFFICIENCY_WATCH` as lane metadata, not a new invented route. Potential permanent-loss/thesis-breaking risk uses the existing P0 path; ordinary promising results must not crowd out portfolio defense.

The RWC handoff carries: stable eventId/claimId, original source and date, exact before/after metric, deployment scope, claim-versus-verification distinction, missing quality/cost evidence, confounders, plausible company-wide economic bridge, benefit recipient, expectations uncertainty, actual thesis link or pending status, and exactly one next question. RWC verifies causality and capture before Full Underwriting updates scenarios, valuation or posture. Radar does not approve a Mind Model change, change probability, create a trade, set position size or silently re-score the rubric.

## Persistence adapter and failure handling

Use the current discovered tools and schemas, not invented cache endpoints. With MikeInvestor, persist only material company discoveries through `create_radar_event` using a stable eventId, actual issuer ticker, fresh observedInvestorContextVersion and existing route classification. Store the lane/claim payload in a structured evidenceRefs object when supported. Read back using `get_security_context` to verify round-trip retention. If extra fields are dropped, preserve a compact source-linked claim summary in coreQuestion/evidenceRefs and report `PARTIAL_PERSISTENCE`; do not claim a durable structured ledger.

Append result observations through `save_research_result` only under a permitted stage, clearly distinguishing a RADAR follow-up from completed RWC. Reuse lineage and never overwrite a prior conclusion. Handle stale-version rejection by refreshing context and reconciling before retrying. Do not put invented theme tickers or infrastructure tickers into issuer-specific APIs just to save a sector summary.

The available six-tool MikeInvestor surface does not by itself establish a generic cohort/run-cache write API. Persist cohort coverage, non-material claims, bootstrap cursor and weekly digest through an actually discovered supported research/run store; otherwise use the authorized dated Library fallback in the integration contract. If neither is available, report `PERSISTENCE_UNAVAILABLE`, retain the visible evidence, and do not claim cross-run dedup, automatic due-date tracking or weekly delivery exactly-once. A configuration file or test fixture is not live evidence. Do not publish private holdings or detailed portfolio weights to a public GitHub repository.

## Baseline and weekly breadth report

Bootstrap each fixed-cohort issuer plus priority holdings from the latest TWO completed earnings cycles as of the run cutoff. Verify which cycles are completed; do not assume fiscal quarters align. Record both cycles, checked source URLs, comparable metrics or NO_DISCLOSURE, and any unavailable sources. Use `PENDING`, `PARTIAL`, `COMPLETE`, `UNAVAILABLE` per issuer; never claim the baseline is complete while any planned issuer remains unfinished. Budget up to two issuer backfills per run and retain a resume cursor; this is a configured work limit, not a claim that backfill has happened. Existing claims found in historical research still require source/date reconciliation.

At the Friday 15:00 America/Toronto run, add one compact weekly breadth summary. If that occurrence fails, the next successful run catches up. Resolve the latest due Friday in Toronto time and deduplicate on `AI_EFFICIENCY_WATCH:WEEKLY:<due-Friday-date>` in a supported durable store; mark delivered only after the visible summary and acknowledged persistence. Do not create another automation.

Report period/as-of, cohort version, total N, actually checked n, unknown/unavailable count, unique issuers with new operating results, net financial benefits, repeated benefits, setbacks, unresolved promises and quality/cost gaps. Count issuers once per category; categories may overlap and do not sum to N. Include both numerator/N and checked coverage n/N. Compare only common-cohort, comparable-period snapshots and disclose additions, removals and stale observations. Historical adoption stages are not this week's new results. Do not average incompatible percentage gains or treat article counts as business breadth.

A provisional 'spreading pattern' research flag requires new qualifying operating-or-better results at three unrelated issuers across at least two sectors in a rolling 90-day measurement window, with distinct underlying evidence groups and known deployment/quality limitations. This is an operational triage rule, not statistical proof or a buy signal. Show independent verification separately; drop no setbacks or silence from the denominator. Change this monitoring threshold only by versioning this contract, never by silently altering the Investor scoring rubric.

## Visible output and acceptance checks

Every scheduled report includes `AI Efficiency Watch — UPDATE / NO UPDATE / UNAVAILABLE`. Add an explicit partial-coverage qualifier when only some sources were checked. NO UPDATE is permitted only after checks; inaccessible sources do not count as silence. Cross-reference material lead-table events rather than duplicate their full writeups. Weekly summary stays compact and does not replace other lanes.

Before activation verify: adoption is not savings; target is not realized; measured gain with unknown costs stays operating; quality deterioration is visible; three articles from one announcement count once; wrappers count once; a missed source is unknown; elapsed target without result is overdue not failed; old baseline is not new; repeated operating evidence is not financial proof; normal RWC/underwriting and portfolio-defense boundaries remain; all existing lanes and schedule slots are retained. Synthetic cases belong only in tests, never the live event ledger.
