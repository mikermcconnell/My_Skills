# Primary-Source Feed Map

Use this map to design or audit Radar coverage. It is a source architecture, not a claim that every feed is connected or complete. State which feeds were actually searched during each run.

## Core principle

Prefer the source closest to the underlying event, then use independent sources to interpret, challenge, or confirm it.

A derivative article can surface an event faster than a primary source search, but the Event Ledger should link back to the original filing, decision, dataset, trial record, statement, or observable evidence whenever available.

## General public-equity sources

### Securities and exchange disclosure

Monitor where relevant:

- SEC EDGAR submissions, inline XBRL facts, ownership filings, registration statements, tender or merger materials;
- SEDAR+ issuer filings and disclosure alerts;
- exchange notices, trading halts, listing changes, corporate actions, and material issuer announcements;
- issuer investor-relations feeds, earnings releases, presentations, transcripts, and designated disclosure channels;
- debt, rating-agency, covenant, financing, and credit disclosures when capital structure is material.

High-priority filing deltas include:

- guidance, segment, KPI, risk-factor, accounting-policy, auditor, internal-control, covenant, liquidity, share-count, compensation, related-party, customer-concentration, and capital-allocation changes.

### Regulators, courts, policy, and official data

Use the relevant original body for:

- regulator decisions, enforcement, permits, sanctions, tariffs, reimbursement, safety actions, recalls, licenses, and rulemaking;
- court dockets, opinions, settlements, injunctions, and transaction decisions;
- government procurement, budgets, grants, subsidies, statistics, trade data, energy data, and transportation or shipping notices;
- standards bodies and official certification records where technical adoption depends on approval.

### Company ecosystem evidence

Check named customers, suppliers, partners, distributors, competitors, and industry bodies. A customer order, supplier capacity statement, partner economics, or competitor launch can be more decision-relevant than the focal company's promotional claim.

## Clinical, biotech, and medical sources

Use when relevant:

- ClinicalTrials.gov and other jurisdictional trial registries;
- FDA, Health Canada, EMA, MHRA, PMDA, NMPA, reimbursement and health-technology-assessment bodies;
- peer-reviewed publications, conference abstracts, protocols, statistical-analysis plans, labels, briefing documents, advisory-committee materials, and safety databases;
- sponsor filings and partner disclosures for rights, milestones, royalties, manufacturing, launch, runway, and financing.

Registry changes are evidence of a record change, not automatic proof of clinical success or failure. Compare the archived baseline and identify sponsor versus regulator-originated information.

## Sector-specific examples

### Technology and industrials

- product qualification, standards, benchmark, patent, developer, procurement, cloud-capacity, supply-chain, channel, lead-time, backlog, and manufacturing evidence;
- named-customer or ecosystem confirmation rather than generic total-addressable-market claims.

### Resources and energy

- technical reports, reserve/resource statements, permits, studies, operating data, commodity balances, pipeline/storage, export/import, sanctions, environmental, and project-financing records.

### Shipping and transportation

- company fixtures and fleet disclosures, port/traffic data, AIS-based datasets with known limitations, freight indices, insurance, sanctions, charter coverage, orderbooks, scrapping, and route changes.

### Financials and fintech

- regulator, banking, brokerage, payment, deposit, credit, capital, liquidity, customer-asset, transaction-volume, take-rate, and disclosure records.

## Expert, journalism, social, and alternative-data lanes

These are valid discovery and interpretation sources, but preserve provenance:

- named experts and specialist research;
- high-quality journalism;
- channel checks and practitioners;
- social, retail, forum, app, search, traffic, pricing, product-availability, or transaction observations.

For each observation state whether it is:

- an original observation;
- a summary of another source;
- an inference;
- independently reproducible;
- representative or anecdotal.

Do not count several accounts repeating the same screenshot, filing, article, or expert statement as independent evidence.

## Coverage declaration for each run

Record:

```text
run timestamp and scan window
markets and event categories covered
primary feeds searched successfully
feeds unavailable, delayed, or not connected
expert/social lanes searched
known scheduled catalysts checked
holdings/theses covered
material limitations and likely blind spots
```

A Radar result with incomplete source coverage must not imply that no material events occurred. Say that no qualifying event was found in the searched universe.

## Feed-performance feedback

Radar Calibration Audit should evaluate each feed by unique-origin capture, latency, novelty precision, RWC survival, underwriting yield, missed-event contribution, and research cost. Do not remove a high-recall feed merely because it produces noise without checking whether another source catches the same valuable events in time.
