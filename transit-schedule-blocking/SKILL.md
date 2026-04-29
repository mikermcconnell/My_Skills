---
name: transit-schedule-blocking
description: Fixed-route transit schedule and blocking workflow for Scheduler 4. Use when tasks involve trip insertion, headways, recovery, cycle time, block assignment, Step 2/3/4 New Schedule wizard work, Schedule Editor behavior, master comparison, trip lineage, or planner-facing schedule safeguards.
---

# Transit Schedule Blocking

Use this skill for Barrie Transit fixed-route schedule work in Scheduler 4. Treat schedule edits as operational logic, not generic table editing.

## Load only the needed repo context

- Start with `docs/rules/LOCKED_LOGIC.md`.
- Read `docs/ARCHITECTURE.md` when you need file ownership or data-flow context.
- Read `ORCHESTRATOR.md` when you need the current fragile areas, recent behavior changes, or verification expectations.
- Read `.Codex/AGENTS.md` and `.Codex/context.md` only when you touch danger-zone schedule files or need historical compatibility notes.

## Classify the task before editing

Put the request into one of these buckets first:

1. Draft Schedule Editor behavior
2. New Schedule wizard Step 2 / Step 3 / Step 4 behavior
3. Blocking or block assignment logic
4. Compare-to-master, trip lineage, or review-needed matching
5. Planner-facing UX for adding, editing, or validating service

Name the bucket in your own notes before making changes. Most bugs come from treating these as generic table edits instead of domain behavior.

## Preserve these guardrails

- Keep the planner in control. Suggest, warn, and summarize, but do not silently override operational decisions.
- Preserve the draft → publish model. Do not turn master schedules into editable working copies.
- Respect locked logic:
  - round each segment before summing
  - treat each row as a paired north/south trip
  - compute cycle time as `lastTripEnd - firstTripStart`
  - assign merged-route blocks by actual gap, not expected start
  - treat Excel times `>= 1.0` as next-day/post-midnight service
- Preserve operational-day ordering for overnight service.
- Treat the current approved Step 2 runtime contract as the source of truth for Step 3 and Step 4.
- Preserve lineage-aware compare behavior. If the compare result is ambiguous, surface review instead of forcing a confident match.
- Reuse shared logic between Schedule Editor and New Schedule Step 4 when behavior should stay aligned.

## Use this file map

- `components/ScheduleEditor.tsx` — core editor shell
- `components/schedule/RoundTripTableView.tsx` — paired trip grid and row-level interactions
- `components/NewSchedule/NewScheduleWizard.tsx` — wizard shell and gating
- `components/NewSchedule/steps/Step2Analysis.tsx` — runtime review and approval flow
- `components/NewSchedule/steps/Step3Build.tsx` — cycle/headway/recovery build logic
- `components/NewSchedule/steps/Step4Schedule.tsx` — generated schedule editing context
- `components/NewSchedule/utils/wizardProjectState.ts` — persisted wizard state and approval contract wiring
- `utils/schedule/scheduleGenerator.ts` — schedule generation
- `utils/schedule/addTripPlanner.ts` — add-service planning logic
- `utils/schedule/masterComparison.ts` — compare-to-master and review-needed state
- `utils/blocks/blockAssignmentCore.ts` — block chaining logic
- `utils/parsers/masterScheduleParser.ts` and `utils/parsers/masterScheduleParserV2.ts` — imported schedule truth
- `utils/newSchedule/stopOrderResolver.ts` — runtime-derived stop order decisions

## Work the problem in this order

1. Identify whether the change affects timing, pairing, direction, block chaining, lineage, or approval state.
2. Trace the current data flow before editing, especially across wizard state or shared editor utilities.
3. Prefer the smallest change that preserves current operational behavior.
4. Add planner-visible explanation or warning text when automation becomes more powerful.
5. Update the nearest targeted tests instead of relying on broad manual confidence.

## Verify with targeted tests

Choose the narrowest useful checks first, then run a build if the change touches shared logic or app wiring.

### Add-trip and planner UX

- `npx vitest run tests/AddTripModal.test.tsx`
- `npx vitest run tests/addTripPlanner.test.ts`
- `npx vitest run tests/ScheduleEditor.interactions.test.tsx`

### Blocking and schedule generation

- `npx vitest run tests/blockAssignmentCore.test.ts`
- `npx vitest run tests/scheduleGenerator.goldenPath.test.ts`
- `npx vitest run tests/scheduleGenerator.canonicalTravelTimes.test.ts`
- `npx vitest run tests/runtimeAnalysis.totalTripTimes.test.ts`

### Wizard Step 2 / 3 / 4

- `npx vitest run tests/Step2Analysis.test.tsx`
- `npx vitest run tests/step2Approval.test.ts tests/step2ApprovedRuntimeModelAdapter.test.ts`
- `npx vitest run tests/Step3Build.test.tsx`
- `npx vitest run tests/Step4Schedule.test.tsx`
- `npx vitest run tests/wizardProjectState.test.ts`

### Compare-to-master and trip lineage

- `npx vitest run tests/tripLineage.test.ts`
- `npx vitest run tests/masterCompareState.test.ts`
- `npx vitest run tests/NewScheduleWizard.masterCompare.test.tsx`
- `npx vitest run tests/RoundTripTableView.masterCompare.test.tsx`

### Grid and editor behavior

- `npx vitest run tests/RoundTripTableView.accessibility.test.tsx`
- `npx vitest run tests/RoundTripTableView.actions.test.tsx`
- `npx vitest run tests/RoundTripTableView.paste.test.tsx`
- `npx vitest run tests/ScheduleEditor.publishOnly.test.tsx`

When the change crosses shared schedule logic, finish with:

- `npm run build`

## Watch these failure patterns

- Do not let north/south previews or warnings only inspect one direction when the workflow can alternate both.
- Do not rebuild Step 2 truth ad hoc in Step 3 or Step 4 if an approved runtime contract already exists.
- Do not convert review-needed compare cases into false `removed` or false exact matches.
- Do not assume adding service in the wizard is a different domain feature than adding service in the editor; the surrounding workflow differs, but the planner-facing add-service behavior should stay aligned unless explicitly changed.
