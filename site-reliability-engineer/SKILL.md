---
name: site-reliability-engineer
description: Improve production reliability through SLOs, observability, alerting, rollout safety, toil reduction, and operational risk analysis. Use when the user asks about service reliability, SLOs/SLIs, monitoring, incident prevention, on-call burden, alert noise, production hardening, canary rollout strategy, or reliability trade-offs for a system.
---

# Site Reliability Engineer

Use this skill when the question is not just "does it work?" but "will it keep working in production?"

## Workflow

1. Define the user-facing reliability problem.
   Identify the critical path, expected volume, blast radius, and what failure looks like from the user's perspective.

2. Translate goals into measurable signals.
   Prefer:
   - availability
   - latency
   - error rate
   - saturation
   - queue depth
   - retry pressure

3. Check the control loop.
   Review:
   - alerts
   - dashboards
   - logs/metrics/traces
   - rollout strategy
   - runbooks
   - recovery path

4. Propose the smallest reliability improvements with the best leverage.
   Usually:
   - better alert thresholds
   - missing instrumentation
   - safer deploy strategy
   - retry/backoff correction
   - circuit breaking or load shedding
   - toil automation

5. Distinguish feature risk from operational risk.
   Be explicit about what should block launch versus what can be monitored after launch.

## Rules

- Define SLOs around user experience, not internal component vanity metrics.
- Do not add alerts that lack a clear action.
- Prefer burn-rate style alerting over noisy symptom spam when appropriate.
- Call out missing rollback and canary paths.
- Prefer automation over repeated manual ops work.
- Treat reliability as a trade-off budget, not an abstract ideal.

## Output Shapes

- Reliability review:
  - main risks
  - missing controls
  - recommended mitigations
  - launch readiness judgment

- SLO proposal:
  - service
  - user-facing objective
  - SLI definition
  - target
  - alerting implications

- Toil reduction plan:
  - repetitive work
  - automation candidate
  - expected operational payoff

## Checklist

- What user promise is being protected?
- Is there enough telemetry to detect and explain failure?
- Does the alert tell someone exactly what to do?
- Can the team roll back safely?
- What operational task should be automated next?
