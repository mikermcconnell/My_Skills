# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
cadence: 08:00, 11:30, 15:00 America/Toronto
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
specialized_lanes_contract: news-radar-investing/references/specialized-lanes.md
price_monitor_contract: news-radar-investing/references/price-monitor-live-source.md
price_monitor_mode: dynamic_live_source
mandatory_visible_specialized_lanes: 9
visible_output: complete_chat_response
markdown_artifact_required: false
```

Every scheduled News Radar task instance must load the active skill, monitor contract, run contract, specialized-lanes contract, and price-monitor live-source contract before scanning. The active version applies beginning with the first scheduled occurrence after this activation commit.

The visible chat response is the complete user-facing Radar report. A separate Markdown attachment is not required. Every scheduled visible run must include the mandatory specialized-lanes coverage, including the Price Monitor Check table and the TTWO, AMZN, and HOOD bespoke lanes.

The Price Monitor Check is **dynamic**: every Radar run must query the canonical live price-monitor/underwriting-monitor state at run time, enumerate whatever active price-bearing monitors exist then, and retrieve current prices for that dynamically resolved set. Radar must not maintain a hard-coded ticker/threshold/action list or use the prior Radar table as source of truth. Additions, removals, activations, deactivations, threshold edits, and action edits in the canonical monitor must flow into the next Radar run automatically. If live monitor state is unavailable, report `UNAVAILABLE` rather than silently presenting a stale list.

Research-only persistence may still use the canonical store or a dated Library fallback when supported; that persisted state is an audit/persistence layer, not a second user-facing report or the next run's monitor source of truth.

Changing this pointer does not authorize changes to thesis probabilities, underwriting posture, fair value, monitor thresholds, review dates, or portfolio holdings.
