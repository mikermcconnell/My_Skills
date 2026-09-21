# Portfolio Capital Allocation Skill Changelog

## Version 1 — September 21, 2026

Dedicated portfolio-allocation gate added to the Investment Firm workflow.

### Scope
- Converts completed Full Underwriting / Challenger outputs into portfolio sizing decisions.
- Owns portfolio loss-budget sizing, starter/target/max weights, cluster/correlation constraints, funding-source logic, staged entries, and add/hold/trim/exit evidence.
- Requires live portfolio context for account-specific sizing when available.
- Treats cash as an active alternative and does not force deployment.
- Does not execute trades, provide tax/account-location advice, or replace Full Underwriting.

### Workflow position
`News Radar -> Research With Confidence -> Full Underwriting -> Underwriting Challenger -> Portfolio Capital Allocation -> Mind Model / monitoring`

### Key implementation rules
- Use cash-inclusive NAV when available; holdings-only outputs remain conditional.
- Use the underwritten Bear case for downside-budget sizing.
- Do not infer personal risk tolerance; show sensitivity when no explicit loss budget exists.
- Aggregate correlated economic clusters rather than relying on ticker count.
- Preserve separate company, security, portfolio, and instrument decisions.


## Evidence-earned sizing update — September 21, 2026

Added a mandatory evidence ladder for staged allocations.

Each staged position must now show:

`Current weight -> Next weight -> Evidence required -> Valuation condition -> Deadline -> Gate status -> Cancellation/falsifier`

Scaling requires evidence, valuation/hurdle, and portfolio-risk gates to pass together. Time passage, price appreciation, repeated guidance, or narrative momentum do not unlock additional capital by themselves. Failed or overdue proof blocks scaling and can route the position back to Full Underwriting.
