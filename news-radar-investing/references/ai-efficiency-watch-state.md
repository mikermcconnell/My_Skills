# AI Efficiency Watch — State adapter

Version 1.0 — 2026-09-18. Read with `ai-efficiency-watch.md` on each Radar run. This file specifies the concrete fallback adapter and weekly activation boundary; it does not change the evidence stages, rubric or decision authority.

## Verified initial state

The authorized research-only Library fallback is `/News Radar/AI Efficiency Watch`.

Initialization snapshot: `ai-efficiency-watch-state-2026-09-18-1640-ET.json`; snapshot ID `aiew-init-20260918T204000Z`. The file was uploaded and its complete contents successfully read back on 2026-09-18. This verifies Library persistence only, not MikeInvestor event writes or a scheduled end-to-end run.

The initialization is explicitly `CONFIGURATION_INITIALIZATION_NOT_A_RADAR_SCAN`: twelve fixed-cohort issuers, zero checked, zero completed baselines, no claims, observations or delivered weekly keys. It does not advance the global Radar watermark. Never report these empty lists as a finding that no companies have achieved efficiency gains.

## Read and resume

1. Load canonical material company events from MikeInvestor first. Library records supplement missing non-material claims, cohort coverage and run state; they never supersede live holdings or underwriting.
2. Use `files.list` on the exact Library folder, sorted by modified time descending. Follow returned pagination as needed to find the newest valid snapshot and its parent. Use `files.read` on the returned file reference, not a guessed file ID. The filename prefix is `ai-efficiency-watch-state-`.
3. Check `schemaVersion`, `laneId`, `snapshotId`, `parentSnapshotId`, `createdAt`, `cohortVersion`, baseline statuses and source timestamps. An initialization snapshot is valid resumable configuration, not evidence of a completed scan.
4. Resume `baseline.nextCohortIndex` and due `nextChecks`. Resolve the dynamic holdings/research overlay from live context; do not interpret an empty initialization overlay as an empty portfolio.
5. Reconcile claims and observations with canonical event IDs and source independence groups before adding evidence. Read all unmerged descendants if snapshots have forked; never discard a sibling merely because another file was uploaded later.

## Write and verify

Append an immutable dated JSON snapshot containing the updated full lane state. Include a new snapshot ID, parent snapshot ID(s), actual creation time, actual scan cutoff, coverage/limitations, cohort and cursor, claim/observation history, next checks and weekly delivery state. Preserve original claim dates and targets. Files uploaded only for testing must never use the live snapshot prefix.

Immediately before writing, reread the most recent state and merge independent observations by stable identity. Do not overwrite a newer snapshot. `files.manage_library` upload to this folder is authorized by the existing Radar research-persistence rules. Use `overwrite=false`; if a name collides, accept the returned duplicate-safe path rather than guessing it.

After uploading, rediscover the saved file with `files.list`, then `files.read` it. Verify snapshot ID, parent, cutoff, cohort/cursor, event lineage and persisted fields. A successful upload receipt alone is not round-trip verification. Record confirmation in the run's audit ending; an immutable snapshot may still say its readback was pending at the moment it was written.

If this store cannot be read, label continuity unavailable and do not assume an empty prior state. If writes fail, report `PERSISTENCE_FAILED`, retain visible findings and do not claim the cursor or weekly delivery marker advanced. A Library-backed agent workflow does not provide an atomic lock or guarantee exactly-once delivery across concurrent runs; reconcile duplicate records and avoid promising otherwise.

## Weekly activation and coverage boundaries

Both existing task prompts were updated by `2026-09-18T20:37:52.611651+00:00`, after that Friday's 15:00 Toronto slot. The first eligible weekly summary is therefore **2026-09-25 at 15:00 America/Toronto**. Do not treat the earlier September 18 slot or any pre-activation Friday as missed.

Use the persisted `weekly.firstEligibleDueAt` as the lower bound when resolving the latest due Friday. After that boundary, use the existing catch-up and due-Friday deduplication rules. Do not mark a weekly key delivered unless the corresponding summary was visibly produced and the persistence result was acknowledged. A configuration-only run is never a weekly summary.

The fixed cohort is a measurement denominator, not a requirement to find a negative outcome. Search for setbacks and no-result evidence in every sector, but never manufacture a negative comparator or assume that silence proves failure. Keep unknowns in coverage and do not replace inconvenient companies.

## Verification boundary

Activation checks performed: saved lane and active-pointer Git blob hashes matched; fifteen static configuration/initial-state checks passed; the specialized-lane diff preserved all ten existing lane definitions; both task updates returned enabled exact schedules with unchanged Toronto slots; the initialization snapshot passed full Library readback.

Not performed during configuration: company-source scanning, the two-earnings-cycle baseline, live Mind Model linkage, a canonical event-write round trip, a completed RWC handoff, or an end-to-end scheduled run. These must be checked in actual runs; configuration checks do not establish investment signal quality.
