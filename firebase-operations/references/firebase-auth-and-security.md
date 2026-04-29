# Firebase Auth and Security

## Auth patterns

Typical needs:
- sign-in
- sign-out
- auth state listener
- current user access

Keep the auth boundary clear between UI, service layer, and security rules.

## Security rules guidance

Rules should normally enforce:
- authentication required
- user ownership on read/write
- document shape validation for creates
- owner immutability where relevant

## Rules gotchas

- queries fail if rules and query shape do not align
- rules are not filters; they are gatekeepers
- ownership should be enforced in rules, not only in UI code
- create/update validation should reflect the actual document schema
