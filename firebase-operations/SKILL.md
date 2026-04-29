---
name: firebase-operations
description: Firebase and Firestore implementation patterns for CRUD, authentication, listeners, security rules, transactions, and offline support. Use when implementing or reviewing Firebase or Firestore behavior in an app.
---

# Firebase Operations

Use this skill for Firebase and Firestore implementation work that needs correct data patterns, auth boundaries, security, and client behavior.

## Use these references

Read only what you need:
- `references/firestore-service-patterns.md` for CRUD, listeners, batch operations, transactions, offline support, and timestamp handling
- `references/firebase-auth-and-security.md` for auth patterns and security rules guidance

## Workflow

1. Identify whether the task is about data access, auth, real-time sync, rules, or offline behavior.
2. Choose the matching reference pattern before writing code.
3. Keep document shape, ownership fields, and timestamps consistent.
4. Verify that security rules match the data model and access pattern.
5. Watch for edge cases: listener cleanup, transaction conflicts, offline state, and timestamp conversion.

## Core rules

- Prefer a consistent service layer instead of ad hoc Firestore calls everywhere.
- Include user ownership fields when the security model depends on them.
- Treat security rules as part of the implementation, not an afterthought.
- Be explicit about optimistic UI, offline behavior, and listener lifecycle.
- Normalize timestamp handling at system boundaries.

## Gotchas

- Don't write queries that the security rules or indexes won't support.
- Don't forget unsubscribe cleanup for real-time listeners.
- Don't trust client-side filtering when rules should enforce ownership.
- Don't mix server timestamps and client timestamps casually.
- Don't assume transactions and batched writes solve the same problem.
