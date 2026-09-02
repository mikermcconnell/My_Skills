# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
cadence: 08:00, 11:30, 15:00 America/Toronto
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
visible_output: complete_chat_response
markdown_artifact_required: false
```

Every scheduled News Radar task instance must load the active skill and monitor contract before scanning. The active version applies beginning with the first scheduled occurrence after this activation commit.

The visible chat response is the complete user-facing Radar report. A separate Markdown attachment is not required. Research-only persistence may still use the canonical store or a dated Library fallback when supported; that persisted state is an audit/persistence layer, not a second user-facing report.

Changing this pointer does not authorize changes to thesis probabilities, underwriting posture, fair value, monitor thresholds, review dates, or portfolio holdings.
