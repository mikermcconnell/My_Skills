# Source and Routing Rules — V3

## Separate source origin from claim status

### Source origin

Use the most specific applicable category:

- regulator, court, or government;
- securities filing or exchange notice;
- company investor relations or designated corporate channel;
- trial registry, standards body, or official dataset;
- independent structured data provider;
- high-quality journalism;
- named industry expert or practitioner;
- anonymous industry source;
- social, retail, or forum observation.

### Claim status

Classify what the source actually provides:

- `REPORTED_FACT`
- `REGULATOR_OR_COURT_FINDING`
- `COMPANY_CLAIM`
- `INDEPENDENT_CONFIRMATION`
- `CHANNEL_CHECK_OR_OBSERVATION`
- `DERIVED_CALCULATION`
- `RESEARCHER_INFERENCE`
- `UNSUPPORTED_ASSERTION`

A source can be primary and promotional. Reliability changes confidence, not whether a claim supports or challenges a thesis.

## Independence groups

Assign one `independence_group` to every material claim. Examples:

- the same issuer release quoted by many outlets;
- one newswire syndicated across publications;
- one analyst note summarized by several websites;
- one trial registry update repeated by the sponsor;
- genuinely separate customer, supplier, regulator, dataset, or practitioner evidence.

Several articles from one origin count as one evidentiary observation.

## Gate guidance

### Novelty

Pass only when the claim or evidence state changes the prior baseline. Independent confirmation can pass even when the underlying claim is old, but label it correctly.

A large price move, a new headline, a fresh publication date, or a high mention count does not by itself pass Novelty.

A missed expected document, removed KPI, delayed milestone, or unfulfilled promised proof may pass Novelty when the changed evidence state is itself new. Do not automatically infer that the implication is negative.

### Materiality

Pass when a plausible bridge exists to at least one of:

- revenue, units, price, market share, backlog;
- gross or operating margin;
- free cash flow, capex, working capital, debt, dilution;
- asset value, reserves or resources, royalties, milestones;
- clinical, regulatory, legal, transaction, or policy probability;
- time to realization;
- permanent-loss risk.

Radar needs a plausible bridge, not a completed sensitivity model. Large social importance is not automatically security materiality.

### Capture

Pass only when a public security, existing holding, or active thesis has sufficiently direct economic exposure. Check the actual subsidiary, geography, product mix, royalty, customer relationship, ownership, share class, and dilution only far enough to avoid routing the wrong security.

Research With Confidence owns the complete value-capture map. Full Underwriting owns fully diluted equity economics.

### Expectation

Look for a plausible unresolved question involving:

- prior guidance or public knowledge;
- pre-event price run-up or selloff;
- consensus estimates and revisions;
- positioning, options, short interest, or narrative saturation;
- missed duration, ownership, timing, second-order consequence, or attribution;
- a security move that appears inconsistent with the underlying evidence.

Radar does not need to prove mispricing. It only determines whether an expectations question deserves research.

### Researchability

Pass when named documents, data, counterparties, disclosures, benchmarks, or dated catalysts can resolve the key uncertainty. A compelling but permanently unobservable story should not consume the highest research priority.

## Priority rules

Rank within each route using:

1. risk to an existing holding or active underwriting;
2. breached or threatened kill criteria;
3. potential permanent-loss magnitude;
4. evidence due today or overdue;
5. novelty and source proximity;
6. financial materiality;
7. exposure purity;
8. time sensitivity;
9. likely expectation gap;
10. availability of decisive evidence.

Do not rank by headline drama, raw mention count, or potential upside alone.

## P0 fast path

For a possible thesis break, financing or liquidity issue, fraud, safety event, regulator action, clinical hold or rejection, internal-control problem, or another permanent-loss concern:

- identify the original source;
- confirm the affected holding or underwriting;
- state the exact new risk and prior baseline;
- name the immediate evidence needed;
- route promptly.

Do not delay a P0 alert to complete second-order beneficiary mapping, false-friend analysis, broad thematic context, or a full economic model.

## Conditional security mapping

Require direct exposure and the main capture uncertainty for every serious event.

Require a second-order candidate and non-beneficiary or comparator only when the lead is:

- a P1 opportunity;
- an industry, policy, bottleneck, or class-level event;
- likely to be fully recognized in the obvious issuer;
- valuable mainly because of cross-company transmission.

Research With Confidence must independently verify the complete security map before an underwriting advance.

## Late-detection routing

When an event predates the current scan window but has no canonical Event Ledger record:

- label it `LATE_DETECTION`;
- backfill the original publication and event timestamps;
- calculate or estimate detection latency;
- identify the likely missed-feed or process reason;
- route using the same five gates as an on-time event.

Do not call it new merely because Radar found it today, and do not reject it merely because it should have been found earlier.

## Price-dislocation routing

An unexplained move may create a temporary `PRICE_DISLOCATION_UNEXPLAINED` investigation item.

First search for:

- a poorly indexed filing, court action, regulator update, trial record, or company announcement;
- customer, supplier, competitor, or peer read-through;
- macro, commodity, rates, factor, index, options, short-interest, or forced-flow explanations;
- stale or false attribution circulating in media or social channels.

Do not advance to P1 until a genuine underlying delta or defensible attribution question exists.

## Scheduled cadence

The authoritative News Radar V3 schedule is:

- **08:00 America/Toronto:** overnight international developments, pre-market filings, regulator actions, portfolio risks, known catalyst outcomes, and evidence due before the open.
- **11:30 America/Toronto:** intraday primary-source confirmation, new North American developments, updates to open events, and evidence-due checks.
- **15:00 America/Toronto:** pre-close changes, time-sensitive holdings risk, final research-queue selection, unresolved-event status, and coverage exceptions.
- **After close when explicitly invoked:** capture earnings, filings, trial results, and regulator announcements. Deep research only for P0 items or when explicitly requested.

Each run searches from the last successful timestamp and updates open events rather than rediscovering them. Advanced, delayed, partial, failed, or skipped runs must preserve the resulting gap and reason.

## Scheduled output discipline

A scheduled run should prioritize breadth and routing accuracy over mini deep dives.

For P0 and P1, provide the exact delta, baseline, source status, preliminary mechanism, direct exposure, strongest failure reason, three or fewer Research With Confidence questions, and next evidence/date.

For P2 and P3, state the missing evidence and date without expanding into a full report.

Stop when the remaining work is principally causal verification, detailed materiality, full value capture, expectations analysis, valuation, dilution, scenarios, return, clinical-commercial analysis, event payoff, or portfolio construction.

## No-quota rule

A valid run may return no P0, P1, or P2 leads. Never lower the gates to produce activity. Report what was scanned, open-event updates, material duplicates, overdue-evidence checks, source and state limitations, and persistence status.
