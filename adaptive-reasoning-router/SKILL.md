---
name: adaptive-reasoning-router
description: Automatically choose the least expensive safe Sol or Terra model and reasoning level at the start of every task. Also use when the user asks to save tokens, adjust reasoning, requests `/quick`, `/standard`, `/deep`, `/relay`, or `/auto`, or explicitly requests multi-agent work.
---

# Adaptive Reasoning Router

Choose one model and effort before ordinary work. Optimize cost per successful task, not raw token count. Do not duplicate a task across models automatically.

## Routing contract

| Route | Work | Model | Effort |
| --- | --- | --- | --- |
| Quick | Typo, formatting, obvious local edit, or one known command | Terra | Low |
| Standard Read | Analysis, planning, research, rewriting, documentation, or routine checks | Terra | Medium |
| Standard Build | Normal features, known-cause fixes, refactoring, or test additions | Terra | High |
| Deep | Security, architecture, production, destructive, uncertain, or costly-to-reverse work | Sol | High |
| Relay | Explicit `/relay` or explicit parallel-agent request only | Sol | High |

Auto must never choose Relay, XHigh, Max, or Ultra. Sol High is the automatic ceiling. A manual XHigh request remains allowed when the host supports it.

## Core rules

1. Honor explicit manual model and effort choices unless they would omit required safety or validation.
2. Honor `/quick`, `/standard`, `/deep`, and `/relay`; remove the directive before executing the task.
3. Classify by consequence, uncertainty, reversibility, and requested action rather than apparent size.
4. Use Standard Read for non-mutating work and Standard Build for ordinary code or test changes.
5. Escalate to Deep for authentication, authorization, passwords, credentials, secrets, PII, customer data, payments, destructive production actions, migrations, public interfaces, architecture boundaries, concurrency, intermittent failures, conflicting evidence, unknown causes, or a failed prior attempt.
6. Use Quick only when an explicit trivial-work signal is present and no Deep signal exists.
7. Never choose Relay automatically. Use it only when the user explicitly requests relay, parallel specialists, or multi-agent work.
8. Never claim a model or effort changed unless the host confirms it.

## Execution

### Quick and Standard

- Work directly in the current thread.
- Use the narrowest practical verification for Quick and focused boundary checks for Standard.
- Do not create child threads.

### Deep

- Define the decision, evidence, risks, and finish line before changing anything.
- Work in the current Sol High thread.
- Do not add children unless the user separately requests multi-agent work.
- De-escalate only for deterministic closeout work when the host can confirm the change.

### Relay

- Use Sol High for the coordinator and never enable Ultra automatically.
- Create a short phase table with one owner, artifact, and gate per phase.
- Use at most three active threads and only for independent deliverables or review gates.
- Default to one writing thread at a time and pass actual artifacts forward.
- Stop children when their gate passes.

## Host handling

- If the host supports model and effort controls, request the route and record only confirmed settings.
- If an exact change fails, continue only when the current model and effort are both at least as capable as requested.
- Treat Terra as below Sol and Low below Medium below High below XHigh.
- Block rather than silently downgrade. Do not create a child solely to simulate a cheaper effort.
- If controls are unavailable, continue operationally with the current thread only when it is a safe upscale.

## Escalation

Escalate to Deep when new risk appears, evidence conflicts, a focused attempt fails, or the original route is invalidated. Do not repeat the same failed approach more than once.

Relay remains explicit even after escalation. A hard task alone does not authorize multi-agent work.

## Reporting

For Quick and Standard, report the normal outcome and verification. For Deep or Relay, add one concise line naming the route actually used and any confirmed fallback. Do not claim token savings without route-level telemetry and outcome evidence.
