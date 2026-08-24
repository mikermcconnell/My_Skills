# My Health API

Base URL: `https://tasktracker-one-azure.vercel.app`

Use `Authorization: Bearer <TASKTRACKER_HEALTH_API_KEY>`. Never print the value. The key must be the dedicated health key, not `TASKTRACKER_API_KEYS`.

## Read context

`GET /api/health/context` returns the profile, approved genetics, recent structured check-ins, trends, and pending actions. Treat the response as private.

## Save a check-in

`POST /api/health/check-ins` accepts a strict structured object. Daily records require `kind="DAILY"`, a Toronto `date`, an `energy` integer from 1-5, a short `summary`, arrays for `nutritionSignals`, `symptoms`, `redFlags`, `wins`, `concerns`, `sources`, and at most three `actions`. Add a unique `operationId` so retries do not duplicate a write.

Do not add a raw-text field. Each action needs `title`, `rationale`, a neutral `neutralTaskTitle`, and optional `plannedDate`.

## Act on suggestions

- `POST /api/health/actions/:id/approve` creates or reuses a neutral PERSONAL task and marks the action approved.
- `POST /api/health/actions/:id/archive` dismisses the action.

Call approval only after Mike explicitly accepts that specific suggestion in the current conversation.
