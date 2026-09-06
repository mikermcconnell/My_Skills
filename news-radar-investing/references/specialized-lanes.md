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
10. **Nancy Pelosi — Congressional Disclosures / Stock & Options**

The Price Monitor Check is always an action-sorted table governed by `price-monitor-live-source.md`. The other nine lanes normally use one compact status line each. A material P0/P1 remains explained in the normal lead table/detail block rather than expanded again here.

Persist lane coverage/status in the run manifest when the write path supports it.

## 1. Price Monitor Check

This is a permanent visible lane and must run on every scheduled Radar pass. `references/price-monitor-live-source.md` is authoritative for its dynamic membership, trigger resolution, sorting, visible action labels, consumed/re-arm logic, and failure behavior.

Before rendering it, load or attempt to load **every active price-bearing monitor** from the canonical live underwriting/monitor state. Do not limit the lane to current holdings if an active monitor exists for a watchlist or underwriting security, and do not maintain a static Radar ticker list.

The visible table is:

| Action | Stock | Current price | Next trigger | What to do |
|---|---|---:|---:|---|

Rules:

- Show **one row per security**, not one row per threshold. Preserve all thresholds in canonical/audit state but show the highest-priority currently valid action or closest next valid trigger.
- Sort by action/urgency: `RE-UNDERWRITE NOW`, `EXIT REVIEW NOW`, `TRIM REVIEW NOW`, `COMPELLING BUY/ADD REVIEW`, `BUY/ADD REVIEW NOW`, `GETTING CLOSE`, `NO ACTION`, `UNAVAILABLE`.
- Use ownership-sensitive wording: `ADD` for owned securities, `BUY` for confirmed unowned securities, and `BUY/ADD` if ownership cannot be resolved.
- `BUY/ADD REVIEW NOW` means a stored entry/add price trigger has been crossed. It does **not** mean automatically buy. Refresh underwriting first; if the thesis and threshold remain valid, advance to capital-allocation review.
- `COMPELLING BUY/ADD REVIEW` means the deeper/more attractive stored buy/add threshold has been crossed and is currently valid. It still requires underwriting refresh and capital-allocation review before a portfolio decision.
- A previously consumed trigger must not remain actionable merely because price is still beyond it. Respect canonical consumed and re-arm state and move to the next valid trigger when applicable.
- `GETTING CLOSE` means price is within 5% of the next valid price trigger by default. This is a visible attention rule only; it does not alter the monitor or activate downstream work.
- `Current price` must be the freshest reliable price available at the run cutoff and should preserve currency when ambiguity exists.
- At **08:00**, use a reliable pre-market price when available; otherwise use the latest regular-session close and label it `prev. close`.
- At **11:30** and **15:00**, use an actual same-day market price when available and state the table's price as-of time immediately above or below the table.
- `Next trigger` must come from the canonical stored threshold/range. Do not substitute analyst consensus or calculate a new Radar target.
- `What to do` is a concise translation of the stored downstream workflow, not a new trade instruction.
- If live monitor state cannot be loaded, render the table heading and write `UNAVAILABLE — live active price-monitor state could not be read`; never silently show a stale static list as current.
- If only some monitor records or quotes are unavailable, include readable securities, mark the affected row `UNAVAILABLE`, and disclose partial coverage.
- If there are genuinely no active price monitors, show a one-row table stating `NO ACTIVE PRICE MONITORS`.
- A crossed price trigger does not by itself change a thesis, fair value, posture, holding, or position size.

Persist the price-monitor coverage, quote timestamp/source, all underlying trigger state, selected visible action, consumed/re-arm state, and unavailable/partial state when supported.

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

Apply `EXPERT_SOURCES.md`. Check named high-signal experts, industry publications, and senior operators mapped to active holdings/theses. SemiAnalysis / Dylan Patel remain priority sources for AI infrastructure and semiconductors.

For AI-related holdings, underwritings, theses, and market structure, this lane must also explicitly check attributable commentary from the **current CEOs, founders, senior executives, chief scientists/research leaders, infrastructure leaders, and major product/model leaders at frontier AI labs**. At minimum, cover relevant current leadership at:

- **OpenAI**;
- **Anthropic**;
- **Google / Google DeepMind**;
- **Meta / Meta AI**.

Resolve the relevant current people and roles dynamically at run time rather than relying on a stale static name list, and extend to other frontier labs when they become material. Search official posts, interviews, podcasts, conferences, developer events, testimony, research/product launch commentary, technical blogs/papers, model/system cards, and other directly attributable public statements.

Prioritize statements that can affect training/inference compute demand, AI infrastructure bottlenecks, model capability and deployment cadence, product adoption, enterprise/developer demand, pricing/monetization, capex and unit economics, cloud/vendor relationships, custom silicon, power/datacenter needs, open-weight strategy, regulation/safety constraints, or competitive read-throughs to public companies.

Treat frontier-lab executive statements as **primary evidence of what the organization is saying, planning, observing, or claiming**, not as independent proof that the economics are correct. Separate factual observations, channel/operating knowledge, forecasts, aspirations, marketing claims, policy arguments, and expert interpretation; reject recycled commentary; and independently corroborate material claims before allowing them to change a thesis or security posture.

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

## 10. Nancy Pelosi — Congressional Disclosures / Stock & Options

This is a permanent congressional-disclosure / alternative-data lane and must run on every scheduled Radar pass. Apply `references/nancy-pelosi-tracker-lane.md` as authoritative for its source hierarchy, transaction normalization, disclosure-lag handling, options treatment, routing, visible status, and persistence.

Search the official **U.S. House Clerk Financial Disclosure / Periodic Transaction Report (PTR)** source first. Secondary congressional-trade databases and news reports may be used for discovery or reconciliation but must not supersede the official filing when it is available.

Prioritize genuinely new official disclosures involving:

- purchases of public-company common stock, ETFs, or other marketable securities;
- purchases of call or put options, preserving strike, expiration and contract count only when disclosed;
- sales, exchanges, option exercises, or amendments when they materially change the interpretation of a previously tracked position;
- large disclosed amount ranges or transactions in securities that overlap the user's holdings, active underwritings, watchlist or active theses;
- transactions occurring near a material public catalyst only as a research lead, never as proof of nonpublic information or a reason to copy the trade.

Preserve **transaction date and filing/disclosure date separately**. Congressional PTRs are delayed disclosures, so a trade may be weeks old when first observable. Do not call the trade itself `LATE_DETECTION` merely because the transaction predates the current scan window if the filing only became public in the current window.

Preserve the official owner code. If a filing identifies `SP` or another non-self owner, describe it as a **Pelosi household / spouse disclosure** rather than stating that Nancy Pelosi personally executed the transaction.

Treat disclosed dollar values as ranges, never exact amounts. Do not infer current position size, continued ownership, inside information, illegality, superior expected returns, or an automatic BUY/SELL signal from the disclosure.

The normal next question is: **what public, independently testable company/catalyst/valuation evidence could explain the disclosed transaction, and does that evidence matter to our thesis?** Route that question through normal V3 gates and RWC when material.

## Routing and output boundary

Any specialized-lane observation still uses the normal V3 five gates, one primary route, detection status, Event Ledger reconciliation and exactly one `Underwriting Required?` classification when it is a surfaced event or material thesis delta.

The always-visible lane status is a coverage guarantee, not an alert quota. `NO UPDATE` is the correct output when a narrative lane was checked and no decision-relevant delta was found. `UNAVAILABLE` is required when the lane could not actually be checked because a material feed or state source was unavailable. The Price Monitor Check is coverage/reporting state and does not create a Radar event merely because a security is near or through a threshold.
