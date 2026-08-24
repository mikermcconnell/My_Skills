---
name: performance-optimization
description: Measure and improve application performance without speculative complexity. Use for user-reported slowness, regressions, Core Web Vitals, browser rendering, server latency, database cost, memory use, network work, or any measurable performance target.
---

# Performance optimization

## Workflow

1. Define the user-visible problem and measurable target.
2. Capture a repeatable baseline with representative data and environment.
3. Identify whether the constraint is network, CPU, rendering, memory, storage, database, or third-party work.
4. Change the smallest high-impact cause.
5. Re-measure with the same method and check correctness regressions.
6. Keep the change only when the improvement is meaningful and maintainable.

## Rules

- Measure before optimizing.
- Remove unnecessary work before adding caches, concurrency, or new infrastructure.
- Include cold starts, large data, slow devices, and failure paths when relevant.
- Define cache invalidation, memory limits, and operational cost for every new optimization mechanism.
- Do not trade accessibility, correctness, or security for a cosmetic benchmark win.

## Frontend guidance

Read [references/consolidated-guidance.md](references/consolidated-guidance.md) for browser-specific measurement and optimization decisions.

## Deeper reference

Read [references/legacy-skill-2026-07.md](references/legacy-skill-2026-07.md) only when detailed measurement examples are needed.
