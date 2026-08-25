# Mike's Integration and Persistence Rules

Read this only when the Radar run needs live TaskTracker, Mind Model, or portfolio context, or when Mike explicitly asks to persist the result.

## Read current context

Use live data rather than remembered holdings or hardcoded thesis wording. Never print credentials.

### TaskTracker and Mind Model

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\TaskTracker`

1. Read `AGENTS.md` and apply the current `mind-model` skill.
2. Load the API key from `.env.local` without displaying it.
3. Read current production state through the supported overview, project, and research endpoints.
4. Match events to exact-company research, sector or thematic projects, thesis mechanisms, forecasts, falsifiers, watchlists, and pending proposals.
5. Treat `UNAUTHORIZED` as no production persistence. A permitted read-only fallback may be used only when authorized and clearly labelled.
6. Local seed data explains schema; it is not confirmed live state.

### Investing portfolios

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\Investing`

1. Read `AGENTS.md`, then `CLAUDE.md`.
2. Initialize Firebase only through the supported repo configuration without exposing secrets.
3. Use user-scoped portfolio and position helpers.
4. Preserve portfolio, account, lot, strategy, instrument, share class, and currency separation.
5. Normalize CDRs, Canadian wrappers, options, duplicate underlyings, and direct versus read-through exposure.
6. Use timestamped price and FX data for value, weight, P/L, or concentration claims.

For ordinary scheduled Radar, load only the narrow context needed to prioritize P0 risks and link known theses. Do not turn every scan into a full portfolio review.

## Exposure labels

- `DIRECT`
- `DERIVATIVE`
- `READ_THROUGH`
- `NONE_IDENTIFIED`

## Persistence

Default to report-only. Persist only when Mike explicitly asks.

When persistence is requested:

1. reread the latest production state immediately before writing;
2. save the Event Ledger record and original source before downstream evidence;
3. preserve first-seen time, original route, confidence, and price context;
4. add only atomic evidence justified by the source;
5. submit thesis wording, probability, status, or investment-view changes as pending proposals against the current revision;
6. never approve a proposal;
7. reread after the write and verify identifiers, status, revision, and persistence;
8. never store credentials, access tokens, raw portfolio secrets, or unlicensed full-text material.

A Radar write records research. It never places an order, changes a holding, or activates a strategy position without Mike's explicit statement that the broker transaction occurred and the actual fill details.
