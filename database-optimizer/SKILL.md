---
name: database-optimizer
description: Diagnose and improve database performance through query analysis, indexing strategy, schema design, migration safety, and connection-pattern review. Use when the user asks about slow queries, bad query plans, schema changes, indexes, N+1 issues, PostgreSQL/MySQL tuning, Supabase or PlanetScale database behavior, or zero-downtime migration planning.
---

# Database Optimizer

Use this skill when the bottleneck is probably data access, not application syntax.

## Workflow

1. Find the hot path.
   Identify the exact query, ORM pattern, endpoint, job, or report that is slow.
   Ask for or inspect:
   - SQL text
   - ORM-generated query shape
   - schema
   - indexes
   - row counts or growth expectations
   - `EXPLAIN` / `EXPLAIN ANALYZE` if available

2. Classify the problem.
   Common buckets:
   - missing or wrong index
   - N+1 query pattern
   - bad join order or predicate shape
   - over-fetching
   - schema mismatch with access pattern
   - expensive migration or lock risk
   - connection pooling or transaction misuse

3. Fix the cheapest high-impact issue first.
   Usually:
   - query rewrite
   - index addition
   - batch loading
   - pagination
   - schema tweak

4. State the trade-offs.
   Every index costs writes and storage.
   Every denormalization adds consistency burden.
   Every materialized path adds refresh complexity.

5. Verify with evidence.
   Prefer before/after plan differences, row estimates, or reduced query count.

## Rules

- Do not recommend indexes without matching them to real predicates and sort order.
- Index foreign keys used in joins.
- Prefer measuring query count and plan shape before proposing cache layers.
- Flag ORM loops and hidden N+1 patterns early.
- Call out migration lock risk on large tables.
- Prefer reversible migrations and phased rollouts for production schema changes.

## Output Shapes

- Slow query diagnosis:
  - likely cause
  - proposed query/index fix
  - why it helps
  - risks or side effects

- Schema review:
  - current access patterns
  - schema/index mismatches
  - recommended changes
  - migration order

- Migration plan:
  - safe sequence
  - backfill strategy
  - lock/rollback considerations

## Checklist

- Which exact query or query family is slow?
- What indexes already exist?
- Are estimates and actual rows badly mismatched?
- Is the application doing extra round trips?
- Will the fix hurt writes, storage, or maintainability?
