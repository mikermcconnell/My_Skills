# Firestore Service Patterns

## Document structure reminders

Common patterns:
- stable document ID
- user ownership field when needed
- createdAt and updatedAt timestamps
- serialized app-friendly shape

## Service layer pattern

Use a small service abstraction for:
- create
- read single
- read collection by query
- update with updatedAt
- delete
- document-to-app-model conversion

## Real-time listeners

Remember to:
- keep query shape predictable
- surface errors cleanly
- return unsubscribe functions
- clean up listeners on teardown

## Batch operations

Use batched writes when multiple independent writes should succeed together.
Use transactions when the write depends on reading current state.

## Offline support

Consider:
- pending writes
- stale cache reads
- conflict expectations on reconnect
- explicit user feedback when sync is delayed

## Timestamp handling

Normalize timestamps at the service boundary.
Convert Firestore timestamps into the app's preferred format consistently.
