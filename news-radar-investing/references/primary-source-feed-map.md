# Primary-Source Feed Map — V3

Use this map to design or audit Radar coverage. It is a source architecture, not a claim that every feed is connected or complete. State which feeds, holdings, underwritings, theses, catalysts, and evidence-due items were actually checked during each run.

## Core principle

Prefer the source closest to the underlying event, then use independent sources to interpret, challenge, or confirm it.

A derivative article can surface an event faster than a primary-source search, but the Event Ledger should link back to the original filing, decision, dataset, trial record, statement, or observable evidence whenever available.

## V3 coverage order

Search in this order unless a time-sensitive event requires otherwise:

1. active holdings, active underwritings, monitors, kill criteria, and evidence due;
2. known catalysts and open P0/P1/P2 items;
3. active Mind Model theses and watchlist candidates;
4. named customers, suppliers, partners, competitors, regulators, and ecosystem sources linked to those exposures;
5. broad opportunity discovery.

This ordering protects current capital without turning every run into a full portfolio review.

## General public-equity sources

### Securities and exchange disclosure

Monitor where relevant:

- SEC EDGAR submissions, inline XBRL facts, ownership filings, registration statements, tender or merger materials;
- SEDAR+ issuer filings and disclosure alerts;
- exchange notices, trading halts, listing changes, corporate actions, and material issuer announcements;
- issuer investor-relations feeds, earnings releases, presentations, transcripts, and designated disclosure channels;
- debt, rating-agency, covenant, financing, and credit disclosures when capital structure is material.

High-priority filing deltas include:

- guidance, segment, KPI, risk-factor, accounting-policy, auditor, internal-control, covenant, liquidity, share-count, compensation, related-party, customer-concentration, and capital-allocation changes;
- removed tables, changed definitions, missing previously material disclosures, or evidence that was due but did not arrive.

### Regulators, courts, policy, and official data

Use the relevant original body for:

- regulator decisions, enforcement, permits, sanctions, tariffs, reimbursement, safety actions, recalls, licenses, and rulemaking;
- court dockets, opinions, settlements, injunctions, and transaction decisions;
- government procurement, budgets, grants, subsidies, statistics, trade data, energy data, and transportation or shipping notices;
- standards bodies and official certification records where technical adoption depends on approval.

Track decision windows and expected dates. A missing or delayed official action can become an evidence-state observation even before its economic meaning is known.

### Company ecosystem evidence

Check named customers, suppliers, partners, distributors, competitors, and industry bodies. A customer order, supplier capacity statement, partner economics, competitor launch, or counterparty omission can be more decision-relevant than the focal company's promotional claim.

## Clinical, biotech, and medical sources

Use when relevant:

- ClinicalTrials.gov and other jurisdictional trial registries, including version history;
- FDA, Health Canada, EMA, MHRA, PMDA, NMPA, reimbursement and health-technology-assessment bodies;
- peer-reviewed publications, conference abstracts, protocols, statistical-analysis plans, labels, briefing documents, advisory-committee materials, and safety databases;
- sponsor filings and partner disclosures for rights, milestones, royalties, manufacturing, launch, runway, and financing.

Registry changes are evidence of a record change, not automatic proof of clinical success or failure. Compare the archived baseline and identify sponsor versus regulator-originated information. Track enrollment, sites, endpoints, completion dates, decision windows, and evidence that becomes overdue.

## Sector-specific examples

### Technology and industrials

- product qualification, standards, benchmark, patent, developer, procurement, cloud-capacity, supply-chain, channel, lead-time, backlog, manufacturing, power, cooling, networking, packaging, and financing evidence;
- named-customer or ecosystem confirmation rather than generic total-addressable-market claims;
- migration of a bottleneck from one layer to another.

### Resources and energy

- technical reports, reserve or resource statements, permits, studies, operating data, commodity balances, pipeline or storage, export or import, sanctions, environmental, and project-financing records;
- missed construction, permit, financing, or production milestones.

### Shipping and transportation

- company fixtures and fleet disclosures, port or traffic data, AIS-based datasets with known limitations, freight indices, insurance, sanctions, charter coverage, orderbooks, scrapping, and route changes;
- evidence of normalization or disruption that must move together rather than relying on one daily datapoint.

### Financials and fintech

- regulator, banking, brokerage, payment, deposit, credit, capital, liquidity, customer-asset, transaction-volume, take-rate, and disclosure records;
- legal or policy changes affecting prediction markets, crypto, payments, custody, capital, or customer access.

## Expert, journalism, social, and alternative-data lanes

These are valid discovery and interpretation sources, but preserve provenance:

- named experts and specialist research;
- high-quality journalism;
- channel checks and practitioners;
- social, retail, forum, app, search, traffic, pricing, product-availability, inventory, employee, or transaction observations.

For each observation state whether it is:

- an original observation;
- a summary of another source;
- an inference;
- independently reproducible;
- representative or anecdotal;
- potentially promotional, bot-driven, affiliate-incentivized, or part of an investor echo chamber.

Do not count several accounts repeating the same screenshot, filing, article, or expert statement as independent evidence.

## Price-dislocation investigation sources

When a holding or candidate moves materially without an indexed company announcement, check where available:

- recent filings, regulator and court records, trial registries, exchange notices, and company channels;
- customers, suppliers, competitors, peers, commodities, rates, currencies, sectors, and index changes;
- options, short-interest, borrow, rebalance, forced-flow, or liquidity explanations;
- social claims for an identifiable original source.

The move is a search trigger, not proof of novelty or materiality.

## V3 coverage manifest

Record for each scheduled run:

```text
run_id and radar_version
run timestamp and scan window
scheduled slot and run status
last successful run timestamp
markets and event categories covered
holdings checked
active underwritings, monitors, kill criteria, and review dates checked
theses and watchlist checked
known catalysts checked
evidence-due items checked
primary feeds searched successfully
feeds unavailable, delayed, or not connected
expert, social, and alternative lanes searched
state sources unavailable
material limitations and likely blind spots
persistence status
next scheduled slot
```

A result with incomplete source or state coverage must not imply that no material events occurred. Say that no qualifying event was found in the searched universe.

## Feed-performance feedback

Radar Calibration Audit should evaluate each feed by:

- unique-origin capture;
- on-time versus late detection;
- latency;
- novelty precision;
- RWC survival;
- underwriting yield;
- missed-event contribution;
- evidence-due resolution yield;
- outage frequency and disclosure quality;
- research cost.

Do not remove a high-recall feed merely because it produces noise without checking whether another source catches the same valuable events in time.
