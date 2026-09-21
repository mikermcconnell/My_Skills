# Source and Routing Rules — V3

Reconciled September 21, 2026. The run contract owns protected discovery and cadence; the feed map owns source coverage; `investment-firm-output/SKILL.md` owns the combined news/case-change/stock-table presentation. These rules do not require completed investment underwriting before surfacing a credible lead.

## Source origin versus claim status

Use the most specific source origin: regulator/court/government; securities filing/exchange; company IR/designated channel; trial registry/standards/official dataset; independent structured data provider; high-quality journalism; named expert/practitioner; anonymous industry source; or social/retail/forum observation.

Classify the actual claim using supported values: REPORTED_FACT; REGULATOR_OR_COURT_FINDING; COMPANY_CLAIM; INDEPENDENT_CONFIRMATION; CHANNEL_CHECK_OR_OBSERVATION; DERIVED_CALCULATION; RESEARCHER_INFERENCE; UNSUPPORTED_ASSERTION.

A primary source can be promotional. Reliability changes confidence, not whether evidence supports or challenges the thesis. A new company statement establishes what was said, not that its forecasts/economics are independently proven. Use directly attributable current sources and preserve access limitations.

## Independence and seen-history

Assign one independence_group per material claim: an issuer release repeated by outlets; one syndicated wire; one analyst note summarized elsewhere; one registry update repeated by its sponsor; or genuinely separate counterparty/regulator/dataset/practitioner observations. Several articles with the same origin count once.

Before declaring first detection, consult the canonical Event Ledger AND verified dated fallback/Reporting Journal. Reuse existing event/parent/evidence IDs where supported. A finding saved only in fallback is already seen for reporting even if its app write failed. Preserve first-detected time and the app-write gap; do not rediscover it every run. Fallback seen-history is not an accepted investment baseline, active monitor, completed research or proof of delivery.

If history is unavailable, state novelty/history unverified. Do not infer zero prior events from missing access or empty app arrays when fallback research is readable. Prior public guidance can establish a comparison for a new company with no internal underwriting; missing internal coverage is not automatic rejection.

## Five gates

### Novelty

Pass only for a real change in the fact/evidence state versus the relevant prior baseline. Independent confirmation may qualify for an old underlying claim, labelled as new evidence. A price move, article date, new ticker or mention count does not by itself pass.

Missing expected documents, removed KPIs, delayed milestones or unfulfilled proof can be newly relevant evidence-state changes. Repeated unchanged absence is not new every run, and absence is not automatically negative. If the source observation is supported but prior-state comparison is unavailable, keep Novelty UNKNOWN and identify the resolving check rather than inventing a PASS or discarding a worthwhile lead.

### Materiality

Require a plausible bridge to revenue/units/pricing/share/backlog; margins; free cash flow/capex/working capital/debt/dilution; assets/resources/royalties/milestones; clinical/regulatory/legal/transaction/policy probability; time to realization; or permanent-loss risk. Radar needs a plausible mechanism, not a completed sensitivity model. For an Emerging Signal, an observable upstream change with a credible path to a later financial KPI can satisfy the research-stage materiality hypothesis even before revenue/profit is reported. Social importance alone is not security materiality.

### Capture

Require sufficiently direct potential exposure through a public security, holding or active thesis. Check actual issuer/subsidiary, product/geography, ownership/royalty/counterparty, share class and dilution far enough to avoid the wrong security. A newly identified public company need not already be held, watched or underwritten. For multi-party events consider unfamiliar counterparties or beneficiaries rather than defaulting to the familiar mega-cap.

RWC owns the complete independently verified value-capture map; Full Underwriting owns fully diluted equity economics. Unknown mapping/capture is a named research question, not a proven investment benefit. A demonstrably absent economic link fails this gate.

### Expectation

Identify a plausible unresolved question about prior public knowledge/guidance, pre-event price changes, consensus revisions, positioning/options/short interest/narrative saturation, duration/ownership/timing/second-order effects or disputed attribution. Radar does not prove mispricing or assign a percentage priced in; it identifies whether research is warranted.

### Researchability

Name a document, datum, counterparty, disclosure, benchmark, source-of-truth metric or dated catalyst that can resolve uncertainty. A permanently unobservable story should not consume highest research priority. Missing access is a limitation, not invented confirmation.

## Leading-indicator / Emerging Signal treatment

Apply `emerging-signal-lens.md` when observable behavior or operations may lead reported results.

For these cases:
- **Materiality** may be a plausible upstream transmission path; reported revenue/profit is not required at Radar stage.
- **Expectation** may remain an explicit research question; Radar need not prove mispricing before P2/P1.
- **Researchability** should name the next leading indicator plus the later financial KPI or disclosure that would confirm/kill the bridge.
- A sequence that gains meaningful velocity, persistence, breadth or independent confirmation can escalate from P3/P2 to P1 even before financial conversion is reported.
- Do not mistake one viral datapoint, one management claim or one price move for a sequence.

When several observations belong to one parent trajectory, preserve one Signal Sequence and atomic evidence lineage. New evidence changes the trajectory; it is not a new thesis by default.

## Route and priority

Assess PASS/FAIL/UNKNOWN separately. A clear failure of Novelty/Materiality/Capture normally rejects or deduplicates; a credible observation with a resolvable unknown is not equivalent to failure. P1 needs a plausible positive novelty/materiality/economic-exposure case. A remaining targeted uncertainty can be P2/P3 without false certainty. Do not lower gates to meet a story quota.

Assign exactly one primary route: P0 holdings/thesis risk; P1 Research With Confidence now; P2 targeted evidence; P3 monitor; REJECT/DUPLICATE. Name one concrete next step and evidence/date, retaining up to three decisive questions in the stored P0/P1 handoff. A route is not a running worker, trade-ready recommendation or executed trade.

Rank within targeted routes by imminent holding/underwriting risk, threatened kill criteria, permanent-loss magnitude, consequential due evidence, novelty/source proximity, financial materiality, exposure purity, time sensitivity, plausible expectations gap and decisive evidence availability. Do not rank by drama, mentions or upside alone. This ranking does NOT move broad discovery behind all routine known-case work: follow the protected pass immediately after bounded urgent triage.

## P0 fast path

For a credible possible thesis break, financing/liquidity/fraud/safety/regulatory/clinical/internal-control/permanent-loss event, locate original support, resolve affected exposure where possible, state new risk versus prior baseline and the immediate evidence needed, and route promptly. If private ownership cannot be confirmed, qualify the portfolio implication rather than fabricate it or suppress an independently credible warning.

Do not delay urgent risk for beneficiary mapping, full valuation, table assembly or broad context. If this preempts discovery, record the skipped sources/window as partial and recover them. Unchanged old risk labels or failed saves alone do not create a fresh P0.

## Conditional security mapping

For each serious event identify direct security/exposure, preliminary mechanism and main capture uncertainty. Require a suitable second-order candidate and comparator/non-beneficiary when relevant to P1 opportunity, industry/policy/bottleneck/class events, already-recognized obvious issuers or cross-company transmission. Mark unknown when evidence is absent; do not force a beneficiary or delay P0. RWC independently verifies mapping before underwriting advancement.

## Freshness and late detection

Keep underlying event time, first public availability, first Radar detection, ingestion, research completion and report delivery distinct. Visible labels NEW DEVELOPMENT, NEW EVIDENCE — EXISTING STORY, LATE DETECTION and NOVELTY UNVERIFIED map to existing supported schema fields; do not add unsupported enums to strict writes.

For earlier public information first detected now with no earlier canonical OR verified fallback detection: label LATE_DETECTION, preserve original dates, measure/estimate latency with uncertainty, identify likely missed-feed/process cause and route normally. Do not discard valuable late evidence or call it fresh because it was found today.

A prior event newly disclosed publicly in the window is not automatically late; congressional filing date and trade date are the clear example. Dependent repeated coverage is FOLLOW_UP/DUPLICATE, not a newly detected event. A failed canonical write cannot reset first detection. If seen-history cannot be checked, qualify the novelty and latency conclusion.

Outside-known-universe status is separate from freshness: compare with readable holdings/watchlist/underwriting records at discovery, or mark membership unknown. Familiar companies can have genuinely new news; unfamiliar companies can have old recycled stories.

## Price-dislocation routing

An unexplained move can create PRICE_DISLOCATION_UNEXPLAINED. Search poorly indexed filings/official decisions/trial records/issuer channels; counterparty/competitor/peer evidence; macro/commodities/rates/factors/index/options/short-interest/forced flows; and stale/false social attribution. Do not advance to P1 without a real underlying delta or defensible attribution question. A price-monitor crossing activates only its stored review workflow, never establishes fundamental novelty or automatic BUY/SELL.

## Schedule and reporting

Existing runs are **08:00, 11:00 and 15:00 America/Toronto, daily**. Morning uses overnight/premarket context; midday intraday updates; afternoon pre-close evidence and decisions. Every slot retains protected broad discovery, targeted checks and the simple stock table. Explicit after-close capture preserves the next scheduled pass. Recover actual missed/partial source windows; do not use a scheduled timestamp as proof of a completed scan.

Publish one combined report under the output contract: new news/opportunities first (urgent risks may lead), meaningful changes to existing cases second, and the stock table third. Material credible new findings are surfaced in the same run with uncertainty, not hidden until full underwriting or exclusively deferred to the Daily Brief. The brief synthesizes rather than republishes everything.

P0/P1 detail retains exact delta/baseline, source status, preliminary mechanism/exposure, strongest failure reason, underwriting requirement, precise question and next evidence/date. P2/P3 stay compact. Unchanged old cases belong in retained state/table, not as fresh news. All eleven lanes are checked; their unchanged status dump is not required in chat.

Stop when the remaining work is principally independent causality/counterfactuals, detailed materiality/capture/expectations, valuation/dilution/scenarios/returns/timing, clinical-commercial economics, event payoff/execution or portfolio construction. Preserve existing stage permissions and no automatic trading.

## No quota and audit

A completed scan may find no qualifying new lead. Say no qualifying developments were found in the actual sources checked, not that nothing material happened anywhere. If discovery was incomplete, say so rather than report an unqualified zero. Persist actual source coverage, outside-universe search evidence, new/updated/late/duplicate IDs and material discoveries included in output in the existing manifest. They are diagnostics, not lead targets or proof of delivery. Failed saving and notification settings remain operational limitations, not novelty or investment conclusions.
