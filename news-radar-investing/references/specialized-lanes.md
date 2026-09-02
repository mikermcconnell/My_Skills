# Specialized Radar Lanes — V3

This contract defines the specialized lanes that must be checked on every scheduled News Radar V3 run and must always appear in the complete visible chat response.

These lanes supplement portfolio defense, Active Thesis Research, broad event/news/filing/regulator discovery, evidence-due checks, and the market tape. They do not replace those core workflows.

## Mandatory visible section

Every scheduled 08:00, 11:30, and 15:00 run must include a `Specialized lanes` section covering every lane below, even when there is no qualifying update.

For narrative lanes use one of these visible statuses:

- `UPDATE — <one-sentence material delta or routed item>`
- `NO UPDATE — no decision-relevant delta found in the searched sources since the prior successful run`
- `UNAVAILABLE — <feed/state limitation>`

Do not invent an update to avoid saying `NO UPDATE`. If an item is already in the lead Radar table, the specialized-lane line should identify or cross-reference it briefly rather than repeat the full analysis.

Mandatory visible lane order:

1. **Price Monitor Check**
2. **Slow-Burn Fundamentals**
3. **Catalysts / Evidence Due**
4. **Social Arbitrage / Alternative Data**
5. **Clinical / Medical**
6. **Expert / Industry Sources**
7. **TTWO — GTA VI / GTA Online / GTA+**
8. **AMZN — AWS / Retail / Ads / Optionality**
9. **HOOD — Customer / Product / Social Arbitrage**

The Price Monitor Check is always a table. The other eight lanes normally use one compact status line each. A material P0/P1 remains explained in the normal lead table/detail block rather than expanded again here.

Persist lane coverage/status in the run manifest when the write path supports it.

## 1. Price Monitor Check

This is a permanent visible lane and must run on every scheduled Radar pass.

Before rendering it, load or attempt to load **every active price-bearing monitor** from the canonical underwriting/monitor state. Do not limit this table to current holdings if an active monitor exists for a watchlist or underwriting security.

Use the actual stored monitor threshold, target, entry range, review level, or other price trigger. Do **not** invent a fresh fair value, target price, entry range, or action inside Radar.

For each active price trigger show:

| Stock | Current price | Target / trigger | Action |
|---|---:|---:|---|

Rules:

- Include **all active price monitors**. If one security has multiple distinct actionable thresholds, use one row per threshold unless the stored monitor explicitly treats them as one range.
- `Current price` must be the freshest reliable price available at the run cutoff and should preserve currency when ambiguity exists.
- At **08:00**, use a reliable pre-market price when available; otherwise use the latest regular-session close and label it `prev. close`. Do not present an overnight indicative quote as a regular-session trade.
- At **11:30** and **15:00**, use an actual same-day market price when available and state the table's price as-of time immediately above or below the table.
- `Target / trigger` is the monitor's stored threshold or range, not analyst consensus and not a newly calculated Radar value.
- `Action` is the monitor's stored action/instruction, such as `review`, `re-underwrite`, `entry review`, `trim review`, `exit review`, `monitor`, or another canonical instruction. **Do not execute the action.**
- If the target exists but the action is not stored, write `REVIEW — action unspecified` rather than guessing.
- If monitor state cannot be loaded, render the table heading and write `UNAVAILABLE — active price-monitor state could not be read`; do not silently show a partial list as complete.
- If only some monitor records or quotes are unavailable, include the readable rows and mark the affected price/target/action cell `UNAVAILABLE`; disclose that the table is partial.
- If there are genuinely no active price monitors, show a one-row table stating `NO ACTIVE PRICE MONITORS`.
- A crossed price trigger does not by itself change a thesis, fair value, posture, holding, or position size. It activates only the stored review/re-underwrite/action workflow.

Persist the price-monitor coverage, quote timestamp/source when supported, trigger status, and any unavailable monitor/quote state in the run manifest or canonical monitor state.

## 2. Slow-Burn Fundamentals

Apply `slow-burn-and-catalyst-lanes.md`. Look for cumulative decision-relevant changes that may not create a standalone headline: guidance language, estimates and underlying drivers, backlog/book-to-bill, pricing, utilization, capacity, margins, capex, cash conversion, share count, financing, disclosure quality, management wording, operating KPIs, repeated channel evidence, and missing expected evidence.

## 3. Catalysts / Evidence Due

Apply `slow-burn-and-catalyst-lanes.md`. Check known catalyst dates, frozen expectations packets, thesis forecast dates, next-evidence dates, regulator windows, trial readouts, earnings, launches, financing, court decisions, permits, and other dated evidence. Missing or delayed evidence is itself an observation but not automatically negative.

## 4. Social Arbitrage / Alternative Data

Apply `social-arbitrage-lane.md`. Search for genuinely new consumer, employee, supplier, developer, community, search, app, product, pricing, inventory, transaction, hiring, traffic, engagement, signup, usage, or cultural behavior that could reach financial results before conventional estimates. Preserve authenticity and denominator uncertainty. Social evidence can surface a lead; it does not confirm economics.

## 5. Clinical / Medical

Apply `clinical-radar-overlay.md`. Check relevant holdings, active underwritings, watchlist programs and competitor read-throughs for registry/protocol changes, enrollment, endpoints, safety, readouts, regulator actions, reimbursement, manufacturing/CMC, partnerships, and overdue evidence.

If the current portfolio/thesis state contains no relevant clinical or medical exposure, a cheap source/evidence-due sweep is sufficient and the visible line may say `NO UPDATE`.

## 6. Expert / Industry Sources

Apply `EXPERT_SOURCES.md`. Check named high-signal experts and industry publications mapped to active holdings/theses. SemiAnalysis / Dylan Patel remain priority sources for AI infrastructure and semiconductors. Separate new factual observations, channel checks and estimates from expert interpretation; reject recycled commentary.

## 7. TTWO — GTA VI / GTA Online / GTA+

This is a permanent bespoke holdings/thesis-risk lane and must run on every scheduled Radar pass.

Load the current TTWO holding/thesis/underwriting baseline first when available. Search primary Rockstar and Take-Two sources before secondary/social evidence.

Prioritize genuinely new evidence on:

- GTA VI launch timing versus the current November 19 baseline and any delay/acceleration evidence;
- GTA VI Online / GTA Online launch sequencing and architecture;
- GTA+ timing, pricing, subscription integration and attach potential;
- multiplayer/persistent-world scope, cross-progression, account/economy continuity and platform strategy;
- recurring-spend mechanics, engagement, retention and post-launch content cadence;
- preorder conversion/cancellations, premium/edition mix and pricing;
- product quality, previews/reviews and launch readiness;
- Rockstar social signals plus search/video/social/player engagement as leads, not proof of economics;
- FY27 Net Bookings and FY28/FY29 EBITDA evidence;
- NBA 2K/mobile offsets, dilution, share count, net debt and management commentary.

Treat a blockbuster GTA VI launch as substantially expected. The key variant remains evidence supporting or challenging roughly >40M FY27 launch-window units / ~50M+ first-year units plus durable Online/GTA+ economics. Do not treat social excitement alone as confirmation.

## 8. AMZN — AWS / Retail / Ads / Optionality

This is a permanent bespoke holdings/thesis-risk lane and must run on every scheduled Radar pass.

Load the current AMZN holding/thesis/underwriting baseline first when available. Search Amazon filings, IR, AWS announcements and regulator/partner/customer primary sources before relying on secondary commentary.

Prioritize genuinely new evidence on:

- AWS revenue growth, backlog/remaining performance obligations, customer demand, utilization, capacity constraints and incremental power/datacenter availability;
- AI infrastructure demand and deployment across Trainium, Inferentia, Graviton, Bedrock, Anthropic and major customer workloads;
- AWS margins, capex intensity, depreciation, return on invested capital and the capacity -> utilization -> revenue -> operating income -> cash flow chain;
- custom-silicon share/adoption versus Nvidia/other accelerators and evidence of workload migration or bottlenecks;
- retail/3P marketplace growth, fulfillment productivity, delivery speed, regionalization, Prime economics, seller behavior and margin structure;
- advertising growth, pricing/load, measurement, advertiser behavior and material regulatory/legal developments, including Sponsored Ads/FTC issues when active;
- meaningful labor, antitrust, marketplace, cloud or consumer-protection regulatory risk;
- material optionality from Zoox, Prime Air/drones, robotics, healthcare or other emerging businesses only when new evidence could affect the thesis or valuation path;
- social/alternative-data signals such as AWS instance availability, hiring, developer/customer activity, seller behavior, advertiser behavior, traffic, app/search trends or delivery observations when they can be independently bridged to the business.

Do not convert a product announcement, capacity headline or social observation directly into AWS/AMZN economics. Route unresolved causality, value capture and expectations questions to RWC.

## 9. HOOD — Customer / Product / Social Arbitrage

This is a permanent bespoke holdings/thesis-risk lane and must run on every scheduled Radar pass.

Load the current HOOD holding/thesis/underwriting baseline first when available. The social-arbitrage check is mandatory because customer/product behavior may lead reported KPIs.

Prioritize genuinely new evidence on:

- net deposits, funded customers, assets under custody, transfer-in behavior and customer quality/retention;
- equities, options and crypto trading volumes/activity plus mix and monetization;
- Robinhood Gold subscriptions, attachment, ARPU and retention;
- cash sweep/net-interest economics and sensitivity to the rate environment;
- credit card, retirement/IRA, banking/cash products, event contracts/prediction markets, advisory and other product adoption;
- international expansion and product/geographic rollout;
- app downloads/rankings, web/search interest, social discussion, referral behavior, customer anecdotes, product waitlists, transaction/activity proxies and other Chris-Camillo-style behavioral leads;
- customer satisfaction, outages, complaints, trust/safety issues and service quality that could affect retention or acquisition;
- regulatory changes affecting crypto, options, payment for order flow, event contracts, custody, tokenization or other material revenue pools;
- revenue diversification, operating leverage, share-based compensation/dilution and material management commentary.

Treat app/social excitement as a lead, not as proof of funded accounts, assets, revenue or profit. Seek independent KPI confirmation and route the business bridge to RWC before security underwriting changes.

## Routing and output boundary

Any specialized-lane observation still uses the normal V3 five gates, one primary route, detection status, Event Ledger reconciliation and exactly one `Underwriting Required?` classification when it is a surfaced event or material thesis delta.

The always-visible lane status is a coverage guarantee, not an alert quota. `NO UPDATE` is the correct output when a narrative lane was checked and no decision-relevant delta was found. `UNAVAILABLE` is required when the lane could not actually be checked because a material feed or state source was unavailable. The Price Monitor Check is coverage/reporting state and does not create a Radar event merely because a security is near or through a threshold.