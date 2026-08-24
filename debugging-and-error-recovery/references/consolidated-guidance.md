# Consolidated error-handling guidance

Read this when the fix changes error boundaries or user-visible failure behavior.

- Catch errors only where the system can add context, recover, or translate them safely.
- Preserve the original cause for diagnostics without exposing secrets to users.
- Give users a clear next action and degrade gracefully when possible.
- Use structured logs with operation and correlation context.
- Never replace a narrow known-error guard with broad exception swallowing.
- Add a regression test for the original failure path.
