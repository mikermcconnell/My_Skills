# Source and Routing Rules

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

Pass only when the claim changes the prior baseline. Independent confirmation can pass even when the underlying claim is old, but label it correctly.

### Materiality

Pass when a plausible bridge exists to at least one of:

- revenue, units, price, market share, backlog;
- gross or operating margin;
- free cash flow, capex, working capital, debt, dilution;
- asset value, reserves/resources, royalties, milestones;
- clinical/regulatory/legal probability;
- time to realization;
- permanent-loss risk.

Large social importance is not automatically security materiality.

### Capture

Pass only when a public security has a sufficiently direct economic interest. Check the actual subsidiary, geography, product mix, royalty, customer relationship, ownership, share class, and dilution.

### Expectation

Look for:

- prior guidance or public knowledge;
- pre-event price run-up or selloff;
- consensus estimates and revisions;
- valuation-implied assumptions;
- positioning, options, short interest, or obvious narrative saturation;
- a plausible attribution error or second-order effect.

Radar need only establish a plausible expectations gap, not complete the valuation.

### Researchability

Pass when named documents, data, counterparties, disclosures, benchmarks, or dated catalysts can resolve the key uncertainty. A compelling but permanently unobservable story should not consume the highest research priority.

## Priority rules

Rank within each route using:

1. risk to an existing holding or active thesis;
2. potential permanent-loss magnitude;
3. novelty and source proximity;
4. financial materiality;
5. exposure purity;
6. likely expectation gap;
7. time sensitivity;
8. availability of decisive evidence.

Do not rank by headline drama or raw mention count.

## Scheduled cadence

- **08:00 America/Toronto:** overnight international developments, pre-market filings, regulatory actions, portfolio risks, and known catalyst results.
- **12:00:** intraday primary-source confirmation, new North American developments, and reprioritization of open events.
- **15:00:** pre-close changes, time-sensitive holdings risk, and selection of the research queue.
- **After close:** capture earnings, filings, trial results, and regulatory announcements. Deep research only for P0 items or when explicitly requested.

Each run should search from the last successful scan timestamp, then update open events rather than rediscovering them.

## No-quota rule

A valid run may return no P0 or P1 leads. Never lower the gates to produce activity. Report what was scanned, material duplicates, and why nothing advanced.
