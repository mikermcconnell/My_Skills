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
price_monitor_visible_format: action_sorted_queue
price_monitor_rows: one_per_security
price_monitor_proximity_band: 5_percent
mandatory_visible_specialized_lanes: 9
visible_output: complete_chat_response
markdown_artifact_required: false
```

Every scheduled News Radar task instance must load the active skill, monitor contract, run contract, specialized-lanes contract, and price-monitor live-source contract before scanning. The active version applies beginning with the first scheduled occurrence after this activation commit.

The visible chat response is the complete user-facing Radar report. A separate Markdown attachment is not required. Every scheduled visible run must include the mandatory specialized-lanes coverage, including the Price Monitor Check table and the TTWO, AMZN, and HOOD bespoke lanes.

The Price Monitor Check is **dynamic**: every Radar run must query the canonical live price-monitor/underwriting-monitor state at run time, enumerate whatever active price-bearing monitors exist then, and retrieve current prices for that dynamically resolved set. Radar must not maintain a hard-coded ticker/threshold/action list or use the prior Radar table as source of truth. Additions, removals, activations, deactivations, threshold edits, action edits, consumed triggers, and re-arm state in the canonical monitor must flow into the next Radar run automatically.

The visible Price Monitor is an **action-sorted queue**, not a raw threshold list. It shows one row per security using `Action | Stock | Current price | Next trigger | What to do`, with the highest-priority currently valid action or closest next valid trigger. Controlled visible actions are `RE-UNDERWRITE NOW`, `EXIT REVIEW NOW`, `TRIM REVIEW NOW`, `COMPELLING BUY/ADD REVIEW`, `BUY/ADD REVIEW NOW`, `GETTING CLOSE`, `NO ACTION`, and `UNAVAILABLE`. Ownership determines `BUY` versus `ADD` when readable. A buy/add price trigger activates underwriting refresh and then capital-allocation review if the thesis remains intact; it is never an automatic trade instruction.

`news-radar-investing/references/price-monitor-live-source.md` is authoritative for the Price Monitor lane and supersedes older/conflicting Price Monitor presentation wording in other V3 files.

Research-only persistence may still use the canonical store or a dated Library fallback when supported; that persisted state is an audit/persistence layer, not a second user-facing report or the next run's monitor source of truth.

Changing this pointer does not authorize changes to thesis probabilities, underwriting posture, fair value, monitor thresholds, review dates, or portfolio holdings.
