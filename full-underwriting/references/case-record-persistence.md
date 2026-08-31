# Full Underwriting — Cross-Chat Case Record Persistence

Use this reference for every new Full Underwriting and every material re-underwrite, event touchpoint, mandatory renewal, or decision-changing update.

The goal is to make the latest security-level decision recoverable in a fresh chat without reconstructing it from conversational memory.

## Source-of-truth hierarchy

Use this precedence when prior records conflict:

1. **Canonical current baseline in the persistent Library** — authoritative for the latest underwriting decision.
2. **Newest dated append-only decision log** — authoritative for what changed and why.
3. **Live underwriting monitors** — operational alert copies of the baseline, not the master record.
4. **Prior chat outputs / cross-chat retrieval / memory** — discovery aids only; never override a newer canonical case record without verification.
5. **Older previews, RWC handoffs, or Radar notes** — evidence inputs, not current underwriting conclusions.

Do not treat memory as the database. Memory may help locate the case; the canonical case record defines the case.

## Canonical Library paths

For ticker `<TICKER>` use:

- `/Investing/Underwriting/<TICKER>/<TICKER>-current-baseline.md`
- `/Investing/Underwriting/<TICKER>/<TICKER>-decision-log-YYYY-MM-DD.md`

If more than one material decision occurs on the same date, append a time or sequence suffix rather than overwriting the earlier log.

Examples:

- `/Investing/Underwriting/HOOD/HOOD-current-baseline.md`
- `/Investing/Underwriting/HOOD/HOOD-decision-log-2026-08-30.md`
- `/Investing/Underwriting/TTWO/TTWO-decision-log-2026-11-12-02.md`

## Retrieval gate — run before new analysis

Before a re-underwrite, event touchpoint, mandatory renewal, monitoring refresh, covered-call/option-expression review, or valuation update:

1. Search for `/Investing/Underwriting/<TICKER>/<TICKER>-current-baseline.md`.
2. If found, read and freeze it before interpreting new evidence.
3. Read the newest relevant decision log when the requested question depends on why the baseline changed.
4. Reverify market-sensitive and load-bearing facts such as current price, capital structure, guidance, estimates, regulatory state, financing, and new evidence.
5. State the previous decision, new evidence, and decision delta.
6. Do not fall back to an older preview, Radar/RWC output, or conversational memory unless the canonical record is missing.
7. If the canonical record conflicts with a live monitor, treat the canonical record as authoritative and repair the monitor before finishing when tools permit.

## Current-baseline file — required contents

The current-baseline file should be concise enough to retrieve quickly but complete enough to support a fresh-chat re-underwrite. Include when applicable:

### Identity and state

- ticker, company/security, exchange/listing, currency;
- underwriting date and research cut-off;
- reference/current price used in the underwriting;
- underwriting mode;
- company-thesis status;
- security-thesis readiness;
- action posture;
- source readiness, evidence confidence, and model status.

### Valuation and return

- Bear / Base / Bull assumptions, probabilities, and value per share;
- probability-weighted or selected fair value;
- expected return / annualized return where applicable;
- required-return hurdle;
- hurdle-clearing price;
- preferred / entry-review / add / compelling / trim / valuation-gap / exit thresholds;
- key valuation method and decisive sensitivities.

### Thesis and evidence map

- one-sentence thesis;
- measurable variant perception;
- what the current price appears to discount;
- the one to four decisive economic drivers;
- key upgrade evidence;
- key deterioration / kill criteria;
- unresolved questions;
- Social-Arbitrage Overlay conclusions when applicable.

### Time and implementation context

- expected holding period;
- target realization date/window;
- mandatory re-underwrite date;
- event-driven accelerators;
- ownership / trade-expression context that changes monitoring, without turning the underwriting record into account-specific sizing advice;
- active monitor names or monitoring state if known.

### Provenance

- prior baseline date/path when this record supersedes an earlier one;
- dated decision log written for this change;
- any material user-specified premise or correction that must remain distinct from verified fact.

## Append-only decision log — required contents

Every new underwriting or material decision-changing update gets a new dated file. Never overwrite or rewrite prior decision logs.

Record:

- decision date/time and price;
- previous baseline date and posture;
- new evidence;
- assumptions changed and why;
- probabilities changed and why;
- valuation / threshold / timing changes;
- company-thesis status, security readiness, and action posture;
- kill / upgrade criteria added, removed, or changed;
- target realization and re-underwrite dates;
- monitor changes;
- unresolved questions;
- source/provenance of each materially changed rule: inherited baseline, verified evidence, analyst judgment, or user-approved assumption.

A later reader must be able to reconstruct what was believed at each decision date without hindsight edits.

## Persistence sequence — mandatory completion order

For every material underwriting conclusion:

1. Finish the security-level underwriting and challenge/red-team work.
2. Write a new dated append-only decision log.
3. Create or replace `<TICKER>-current-baseline.md` with the newly authoritative baseline.
4. Synchronize live monitors from that current baseline.
5. Verify that the persisted baseline and monitors agree on fair value, thresholds, kill criteria, and review date.
6. Only then finalize the user-facing response.

The Library case record is the source of truth; monitors are synchronized operational copies.

## Materiality rule

A new decision log and current-baseline update are required when any of these change materially:

- company-thesis status;
- security readiness or action posture;
- Bear/Base/Bull economics or probabilities;
- probability-weighted / selected fair value;
- required-return hurdle or hurdle-clearing price;
- entry/add/compelling/trim/valuation-gap/exit thresholds;
- kill or upgrade criteria;
- capital structure / financing assumptions;
- target realization date;
- mandatory re-underwrite date;
- ownership/trade-expression context that changes monitoring;
- a user correction that changes the authoritative case.

Purely informational evidence that does not change the decision can remain in the monitor/event record without rewriting the canonical baseline.

## Failure and fallback behavior

If persistent Library writes are unavailable:

- do not claim that the case was persisted;
- mark `CASE_PERSISTENCE_BLOCKED` explicitly;
- create an exact current-baseline and decision-log artifact in the conversation when possible;
- still synchronize live monitors when monitor editing is available, but note that monitors are temporarily acting as an operational fallback rather than the master record;
- automatically backfill the Library case record in the next session where persistent file writes are available before performing a material update.

If monitor editing is unavailable but Library persistence succeeds:

- persist the case record normally;
- mark monitor synchronization blocked;
- save the exact monitor-update payload in the current baseline or a companion artifact;
- apply it automatically in the next session where monitor editing is available.

## Quality-control questions

Before finishing, answer internally:

1. Did I retrieve the canonical prior case before interpreting new evidence?
2. Is the current baseline now saved at the canonical ticker path?
3. Did I preserve the old decision in an append-only log rather than overwrite history?
4. Do the live monitors match the persisted baseline?
5. Could a fresh chat recover the security's current thesis, valuation, thresholds, kill criteria, and re-underwrite date without relying on memory?

If the answer to #2, #3, or #5 is no and persistence tooling is available, the underwriting is not complete.
