---
name: news-radar-investing
description: Investigate News Radar or Event Radar scheduled-task alerts and other public-equity developments, connect them to Mike's live TaskTracker projects and Mind Model theses and his live Investing Firestore portfolios, score each security's investability from 1 to 10, specify the expected trade duration and exit plan, and make a direct risk-aware recommendation. Always use when Mike asks to dig deeper on a radar alert, assess news against his holdings or theses, identify beneficiaries or new positions, decide whether an event makes a stock investable, or score an event-driven investment idea.
---

# News Radar Investing

Turn a news alert into a source-backed investment decision. Verify the event, trace the financial mechanism, connect it to Mike's current research and exposure, identify the best securities, and recommend action when expected upside justifies the risk.

## Required posture

- Treat News Radar and legacy Event Radar scheduler alerts as lead generators, not proof or trade signals.
- Be willing to recommend risk. Investable means the expected return and payoff justify the uncertainty; it does not mean risk-free.
- Do not reject an idea merely because it has competition, volatility, incomplete certainty, or a credible downside. Every investment has downside.
- Do not lower every score to avoid being wrong. Use the scoring anchors consistently and state the real recommendation.
- Do not force an investment. Reject stale, false, immaterial, fully priced, or negatively skewed ideas.
- Separate the world thesis, company value capture, security valuation, and portfolio action.
- Separate an immediate event-reaction trade from a multi-week catalyst trade and a long-term thesis investment. A good company can be investable on one horizon and unattractive on another.
- Lead with what Mike should do, why, and what would change the answer.
- Separate `Fact`, `Derived calculation`, `Assumption`, and `Judgment` whenever the distinction matters.
- Timestamp event status, prices, estimates, filings, FX, and portfolio data.
- Keep TaskTracker's Investor Center research-only. Never place trades, change holdings, or approve a Mind Model proposal.

## 1. Read the alert precisely

Capture:

- issuer, ticker, security, exchange, geography, and event type;
- what is genuinely new, publication time, event time, and radar scan window;
- the original source behind the alert, not only repeating coverage;
- confirmed facts, reported-but-unverified claims, missing details, and conflicts;
- whether the relevant market was open when the information became public;
- timestamped price and volume reaction when one could actually have occurred.

Reject or downgrade stale, duplicated, circularly sourced, immaterial, or rhetorical alerts. Never invent a market reaction while the market is closed. Do not manufacture an investment angle or fill an alert quota.

## 2. Load Mike's current context

Use live data rather than remembered holdings or hardcoded thesis wording. Never print credentials.

### Personal context

Read the narrowest relevant `personal_context` resource first when available. Use `portfolio://all` only when broad personal context is genuinely needed. If the server is unavailable, say so briefly and continue with the authoritative project sources.

### TaskTracker projects and Mind Model

Repository: `C:\Users\Mike McConnell\Documents\mike_apps\TaskTracker`

1. Read `AGENTS.md` and apply the current `mind-model` skill.
2. Load the API key from `.env.local` without printing it.
3. Read current production state:
   - `GET https://tasktracker-one-azure.vercel.app/api/mind-model/overview`
   - `GET https://tasktracker-one-azure.vercel.app/api/projects?page=1&pageSize=100`
   - read idea or research detail only when relevant.
4. Match the event to:
   - exact-company research projects;
   - sector, basket, supplier, customer, or thematic projects;
   - thesis mechanisms, competing outcomes, forecasts, falsifiers, watchlist candidates, and pending proposals.
5. If the production API returns `UNAUTHORIZED`, treat production persistence as unavailable. A read-only Firestore fallback may be used when authorized local Firebase credentials exist, but label the access path and do not claim the API succeeded.
6. Local seed data explains schema only; it is not confirmed live state.

### Investing portfolios

Repository: `C:\Users\Mike McConnell\Documents\mike_apps\Investing`

1. Read `AGENTS.md`, then `CLAUDE.md`.
2. Load Firebase configuration from the repo environment without exposing it.
3. Initialize Firebase through `src.firebase_config.init_firebase()`.
4. Resolve Mike's user ID from authenticated app context. For a local read-only run, use the sole distinct portfolio owner only when exactly one exists; otherwise ask rather than reading across users.
5. Read through user-scoped helpers:
   - `src.data.firestore_service.get_portfolios(user_id)`
   - `src.data.firestore_service.get_all_positions(user_id, portfolio_type="active")`
6. Preserve portfolio, account, lot, strategy, and currency separation.
7. Normalize economic exposure carefully:
   - CDRs and Canadian wrappers such as `.TO` or `.NE`;
   - options to their underlying while retaining strike, expiry, and nonlinear risk;
   - direct holdings versus peer, supplier, customer, ETF, sector, or factor exposure;
   - duplicate underlyings across accounts and strategies.
8. Fetch timestamped prices and FX before calculating value, weight, P/L, concentration, or sizing implications. When the market is closed, use the last valid close and make any entry recommendation conditional on the next tradable price.

## 3. Build the evidence pack

Use the smallest high-quality source set that can answer the investment question.

### Source order

1. **Primary:** issuer filings and investor relations, exchange notices, contracts, court dockets, regulators, governments, and official statistics.
2. **Structured market evidence:** timestamped prices, volume, estimates, ownership, short interest, options, benchmarks, and FX from a reliable provider.
3. **High-quality secondary reporting:** synthesis, channel checks, and facts not yet in primary material. Trace anonymously sourced claims when possible.
4. **Industry and technical evidence:** customers, suppliers, practitioners, standards bodies, technical repositories, and peer-reviewed work when they test adoption or value capture.
5. **Social or retail commentary:** discovery and sentiment only, never sole confirmation of a material fact.

For important claims record the URL, publisher, publication date, access date, proximity to the fact, reliability limits, incentives, and shared origin. Source reliability affects evidence strength, not whether a claim supports or challenges a thesis.

Use the installed `public-equity-investing` router and the narrowest relevant workflow when available. Typical routes are event analysis, earnings analysis, idea generation, thesis tracking, valuation, economic impact, or portfolio risk. Do not duplicate a full specialist workflow when a focused skill already owns it.

## 4. Analyze the investment

Answer these in order.

### Event mechanics

- What exactly happened?
- Is it confirmed, binding, dated, material, and incremental?
- What conditions, deadlines, or next decision points remain?
- Is the edge informational, analytical, timing-based, or a second-order read-through?

### Business and financial bridge

Translate the event into the affected model variables:

- volume, price, mix, market share, backlog, and revenue;
- gross margin, operating costs, productivity, depreciation, and capital intensity;
- working capital, free cash flow, debt, liquidity, dilution, buybacks, and share count;
- probability-adjusted outcomes for regulatory, legal, clinical, policy, or transaction events.

Do not call a deployment financially material without evidence linking it to orders, production, revenue, margins, or estimates. Explain which company in the value chain captures the economics and why.

### Expectations and valuation

- What did investors appear to expect before the event?
- What is already reflected in price, estimates, positioning, or the valuation multiple?
- What would have to be true for the security to be cheap, fair, or expensive?
- What is the plausible upside, base case, downside, and time horizon?
- Is the reward sufficiently asymmetric after dilution, execution risk, taxes, FX, and opportunity cost?

Use current valuation inputs when available. If the market is closed or an input is missing, give a conditional entry threshold rather than refusing to decide. Do not confuse a strong company with an attractive security.

### Candidate map

Evaluate separately:

- the obvious issuer;
- direct suppliers and customers;
- peers with stronger exposure or cheaper valuation;
- picks-and-shovels beneficiaries;
- negatively affected incumbents or short candidates;
- securities already held by Mike.

Do not advance a candidate because it merely mentions the theme. Require a defensible path to orders, revenue, margins, cash flow, assets, or a dated market catalyst.

### Social-arbitrage lane

Classify an alert as `Social Arbitrage` when the potential edge comes from observable consumer, employee, supplier, community, search, app, product, pricing, inventory, or cultural behaviour that may reach company results or analyst estimates with a lag. A popular stock post, influencer opinion, management claim, or ordinary breaking news item is not social arbitrage by itself.

Reuse the Investing repo's existing social-arbitrage evidence rather than starting a parallel scanner:

- `/ai-efficiency/api/social-arb/evidence` for saved manual observations;
- `/ai-efficiency/api/social-arb/signals` for combined ticker scores;
- `src/services/social_signal_extractor.py` for signal-quality and purity checks;
- `src/services/firecrawl_social_sources.py` and the Social Signals page for Chris Camillo and Dumb Money research leads.

For each social-arbitrage candidate test:

1. **Novelty:** when the behaviour began, whether it is accelerating, and whether investors already discuss it widely.
2. **Velocity and breadth:** change in volume or intensity, independent sources, geography, demographic reach, and persistence across more than one observation.
3. **Authenticity:** organic behaviour versus paid promotion, bots, affiliate incentives, investor echo chambers, or one viral outlier.
4. **Ticker mapping:** the actual public company, segment, geography, product economics, ownership structure, and whether another supplier or platform captures more value.
5. **Materiality bridge:** units, price, market share, revenue exposure, margins, estimate sensitivity, and the reporting period in which evidence should appear.
6. **Expectations gap:** what analysts and the current valuation imply, whether the signal is saturated, and why the market has not incorporated it.
7. **Confirmation and falsification:** the next measurable app rank, traffic, pricing, inventory, channel, search, transaction, guidance, or earnings evidence and the date it should appear.

Treat social activity as a lead until the business and valuation bridge is supported. Do not mistake attention for purchasing, purchasing for revenue, revenue for profit, or a good signal for an attractive stock. Prefer several independent observations over a high raw mention count that shares one origin.

Social-arbitrage trades will usually need weeks or months for the information edge to reach estimates or reported results. Use a one-day reaction only when the signal is genuinely new, financially material, not yet reflected in price, and has a credible immediate repricing path.

### Event-specific checks

- **Earnings/guidance:** expectation bar, beat or miss quality, guidance bridge, KPI revisions, and cash conversion.
- **Financing/capital allocation:** dilution, discount, use of proceeds, funding need, returns on incremental capital, and balance-sheet runway.
- **M&A/legal/regulatory:** controlling documents, approvals, remedies, timing, terminal outcomes, probabilities, and payoffs.
- **Clinical/biotech:** trial design, endpoint, population, clinical significance, safety, regulatory path, and cash runway.
- **Product/contract/capex:** customer commitment, unit economics, capacity, ramp timing, cancellation rights, and revenue recognition.
- **Macro/commodity/policy:** transmission path, sensitivity, lag, hedge, geography, and second-order effects.
- **Management/ownership/flow:** authority, incentives, size relative to holdings or float, liquidity, borrow, crowding, and exit path.

### Trade horizon and exit plan

Assign every recommended security one primary holding period. Do not say only "short term" or "long term."

- **One-day reaction:** enter for the next tradable session and exit by that close or a stated intraday trigger. Use only when the event is new, the market has not reacted, liquidity is adequate, and there is a clear reason the repricing should occur immediately.
- **Two-to-five-day reaction:** capture delayed analyst revisions, cross-market transmission, positioning, or confirmation from a near-term event.
- **Two-to-six-week catalyst trade:** hold through a dated earnings release, regulatory decision, placement completion, product event, estimate revision cycle, or other near catalyst.
- **One-to-six-month position:** allow the event to appear in orders, pricing, guidance, earnings, or industry data.
- **Six-to-twenty-four-month thesis position:** underwrite several reporting periods, an operating ramp, capacity cycle, or strategic change.
- **Two-plus-year investment:** use only when durable economics, balance-sheet capacity, valuation, and portfolio fit support owning through ordinary volatility and more than one catalyst cycle.

For each action state:

1. **Trade type:** event reaction, catalyst swing, cyclical position, or long-term thesis investment.
2. **Expected holding period:** one concrete range, such as `2-5 trading days`, `1-3 months`, or `12-24 months`.
3. **Why this long:** the financial transmission or catalyst that needs that amount of time.
4. **Expected selling date:** one explicit `YYYY-MM-DD` date based on the planned entry and primary holding period. This is the maximum time-stop unless a nearer invalidation or profit rule exits the trade first.
5. **Review date or event:** the next earnings release, filing, data point, or calendar deadline.
6. **Profit-taking rule:** a target, valuation threshold, event completion, or evidence-based condition.
7. **Loss/invalidating rule:** price stop when suitable, thesis break, failed catalyst, adverse filing, or maximum time stop.

News Radar positions use a default performance target of **2% every 30 calendar days**, compounded for the actual time invested:

```text
target return % = ((1 + 0.02) ^ (days invested / 30) - 1) * 100
```

State the target return implied by the expected selling date. Keep this time-scaled strategy target separate from a security-specific target price. If the actual fill date changes materially from the assumed entry date, recalculate the expected selling date and target before recording the purchase.

For a **one-day reaction**, count the session as one invested day and track two targets rather than treating the roughly `0.066%` one-day strategy pace as sufficient:

1. **Strategy pace target:** the time-scaled 2%-per-30-day benchmark.
2. **Trade target:** the larger of the event-specific expected move or **1.0%**.

An investable one-day recommendation must include a numeric planned entry and stop, preserve at least **1.5-to-1 potential reward versus planned loss**, and exit by the regular market close on the expected selling date unless the profit or invalidation rule triggers earlier. Recalculate the target price and reward-to-risk ratio from the actual fill before recording the purchase. If the actual fill cannot preserve 1.5-to-1, do not activate the trade at that price.

Keep the investment thesis horizon separate from the recommended trade duration. For an existing holding, say whether the alert changes the holding period or merely confirms the original plan. If several horizons are viable, choose one primary expression and briefly name the alternative rather than blending them into an indefinite hold.

Do not recommend a one-day trade merely because the alert is recent. If the market is closed, make the one-day case conditional on the opening price and define the exit before recommending it. If the event needs financial confirmation, use a multi-week or multi-month horizon instead.

## 5. Score investability

Score every serious existing holding and new candidate from `1.0` to `10.0`. Use five sub-scores from `0.0` to `2.0`; half-points are allowed. Show the sub-scores and arithmetic.

1. **Evidence quality and durability**
   - `0`: false, stale, circular, or unsupported core premise.
   - `1`: credible but secondary, incomplete, or partly expected.
   - `2`: primary or independently confirmed, durable, and genuinely incremental.
2. **Financial materiality and value capture**
   - `0`: no credible earnings or asset-value bridge.
   - `1`: plausible but modest, delayed, or uncertain capture.
   - `2`: clear and potentially material revenue, margin, cash-flow, or asset impact.
3. **Expectations and valuation**
   - `0`: clearly priced in or unattractive even if the thesis is right.
   - `1`: mixed, roughly fair, or dependent on a reasonable entry threshold.
   - `2`: meaningfully underappreciated with an attractive valuation or implied expectation.
4. **Catalyst path and timing**
   - `0`: no path for recognition or an impractical horizon.
   - `1`: plausible but timing is uncertain.
   - `2`: identifiable catalysts, milestones, or estimate revisions within the thesis horizon.
5. **Risk-reward and portfolio fit**
   - `0`: downside overwhelms upside, liquidity is unacceptable, or exposure duplicates a major risk without compensation.
   - `1`: balanced payoff or manageable but meaningful portfolio conflict.
   - `2`: asymmetric upside with manageable downside and useful portfolio fit.

### Score-to-action anchors

- `9.0-10.0` — **HIGH CONVICTION**: unusually attractive. A 10 is exceptional, not riskless.
- `7.0-8.5` — **INVESTABLE / INITIATE**: recommend opening a standard starter position, or adding when already held.
- `6.0-6.5` — **SPECULATIVE POSITION**: recommend a small, risk-budgeted starter when the upside is meaningfully asymmetric.
- `4.0-5.5` — **WATCH**: not attractive enough now; give the price, evidence, or catalyst threshold that would make it investable.
- `1.0-3.5` — **AVOID**: weak, immaterial, fully priced, structurally impaired, or negatively skewed.

Do not use undocumented score caps. Ordinary uncertainty, volatility, competition, or downside does not prevent a 6 or 7. A reported-but-unconfirmed event lowers evidence quality but may still support a speculative or conditional idea when independent fundamentals and the payoff justify it.

For an existing position use `ADD`, `HOLD`, `TRIM`, or `EXIT` when the evidence supports it. For a new position use `INITIATE`, `SPECULATIVE POSITION`, `WATCH`, or `AVOID`. If price is unavailable, use a conditional action such as `INITIATE AT OR BELOW [threshold]`.

Give only a sizing class:

- small speculative starter;
- standard starter;
- high-conviction candidate.

Use `portfolio-risk-management` for exact sizing, hedging, or implementation. Never execute the recommendation.

## 6. Connect to the Mind Model

Restate the relevant thesis as a falsifiable claim and identify the real competing outcomes.

Split sources into atomic, decision-relevant claims. Classify each by its actual effect on the specific thesis or forecast:

- `SUPPORT`: makes it more likely.
- `CHALLENGE`: makes it less likely or strengthens a genuine competing outcome.
- `CONTEXT`: explains mechanism, timing, scope, limits, or uncertainty without materially moving it.

Do not balance evidence counts, double-count one origin, treat a source limitation as opposing evidence, or update probability by vote counting. State the probability effect as `raise`, `lower`, or `no change`, with a range only when justified.

Keep separate:

1. probability of the world outcome;
2. which company captures value;
3. whether the earnings impact is material;
4. whether the security is attractively priced.

If no thesis fits, recommend a bounded Investor Center research item or new-thesis proposal. Do not create a duplicate thesis automatically.

## 7. Evaluate portfolio impact

Classify each connection:

- `DIRECT`: the security or economic equivalent is held.
- `DERIVATIVE`: options or another instrument create material exposure.
- `READ_THROUGH`: supplier, customer, peer, ETF, sector, or factor exposure.
- `NONE IDENTIFIED`: no meaningful current link found.

Assess affected portfolios, accounts, strategies, instruments, direction, likely magnitude, concentration, correlation, duplicate-underlying exposure, and catalyst timing versus option expiry or intended horizon.

Recommend action when current prices and evidence support it. Do not hide behind `PORTFOLIO REVIEW` when the analysis supports `ADD`, `HOLD`, `TRIM`, or `EXIT`; state the recommendation and then identify any exact sizing work still required.

## 8. Rank the research response

Assign one research-priority status separately from the investment action:

- `IGNORE`: false, stale, immaterial, or no defensible investment link.
- `MONITOR`: real but not yet decision-relevant.
- `RESEARCH NOW`: material, time-sensitive, or plausibly mispriced.
- `THESIS UPDATE PROPOSAL`: evidence justifies a pending Mind Model change for Mike to review.
- `PORTFOLIO REVIEW`: current exposure needs exact sizing, hedge, tax, or account work.

Rank multiple alerts by direct exposure, thesis relevance, financial materiality, surprise, source confidence, time sensitivity, and plausible mispricing.

## 9. Output format

Start with the decision:

```text
Recommendation: INITIATE / SPECULATIVE POSITION / ADD / HOLD / TRIM / EXIT / WATCH / AVOID
Investability: 7.5 / 10 - INVESTABLE
Idea type: Event-driven / Social Arbitrage
Why: One sentence connecting the event, financial impact, valuation, and risk-reward.
Sizing class: Standard starter
Entry condition: Current price or conditional threshold
Trade type: Event reaction / Catalyst swing / Cyclical position / Long-term thesis investment
Expected holding period: Concrete range
Expected selling date: YYYY-MM-DD
Return target: 2% every 30 calendar days
Target return by expected sale: Compounded percentage for the planned days invested
One-day trade target: Event-specific target, never below 1.0% when applicable
One-day reward versus risk: At least 1.5 to 1 when applicable
Information edge: Specific behavioural observation when Social Arbitrage
Expected financial lag: Time until the signal should reach estimates or results
Next confirmation: Measurable evidence and expected date
Next review: Dated catalyst or evidence checkpoint
Exit plan: Profit-taking, invalidation, and maximum time-stop rules
Confidence: High / Medium / Low
```

Then give:

1. **Ranked action queue** — security, score, action, expected holding period, and research priority.
2. **What changed** — verified event, timestamp, market status, and source quality.
3. **Why it matters financially** — model-variable bridge and materiality.
4. **Mike's existing connection** — projects, Mind Model, and portfolio exposure.
5. **Investability scorecard** — all five sub-scores, total, and concise rationale.
6. **Investment case** — variant view, valuation, catalyst, upside, downside, strongest opposing case, trade duration, and exit plan.
7. **Thesis impact** — natural `SUPPORT`, `CHALLENGE`, and `CONTEXT` claims plus probability effect.
8. **What would change the answer** — price, evidence, milestone, or falsifier.
9. **Sources** — primary first, with dates and working links.

For several alerts, keep the queue concise and give detailed cards only for the most decision-relevant securities. Do not bury the recommendation below the research.

## Persistence rules

Default to report-only. Persist only when Mike explicitly asks.

When Mike asks to record the recommendation in Investing, save the research decision to the **News Radar** Strategy Desk card rather than Event Reaction Drift. Record the idea type, ticker, security name, score, action, source event, rationale, expected holding-period label, maximum hold days, explicit expected selling date, the default 2%-per-30-day return target, next review date, entry threshold, target price, stop when used, profit-taking rule, invalidation rule, and primary-source URL. For Social Arbitrage also record the information edge, expected financial lag, and next confirming evidence. For a one-day trade also record the trade-return target, reward-to-risk ratio, and market-close deadline. Recording research is not trade execution. Use the News Radar activation flow only when Mike says the broker purchase was completed and supplies the fill; that action records the fill but does not place an order.

Attribute an activated `Event-driven` position to the **News Radar** strategy. Attribute an activated `Social Arbitrage` position to the **ChrisCamillo** strategy so the two approaches retain separate performance histories.

- Re-read TaskTracker immediately before any write.
- Capture the original source before evidence.
- Add only justified atomic evidence records.
- Use Investor Center research items for bounded questions with a concrete next action.
- Submit thesis wording, probability, status, or investment-view changes as a pending proposal against the current revision.
- Never approve a proposal.
- Re-read after writes and verify IDs, status, revision, and persistence.
- Treat `UNAUTHORIZED` as no production persistence.
- Never store credentials, access tokens, raw portfolio secrets, or unlicensed full-text material.

## Final quality check

Before finishing, confirm:

- the event is new and accurately sourced;
- issuer, security, share class, currency, wrapper, and underlying are correct;
- market-sensitive facts have timestamps and closed-market claims are not invented;
- current TaskTracker and portfolio data were read or clearly labelled unavailable;
- direct holdings and new candidates were both considered;
- every serious candidate has visible sub-scores and correct score arithmetic;
- the score maps to the stated action;
- every recommended action has one concrete holding period, an explicit expected selling date, the target return implied by that date, a review event, and an exit or time-stop rule;
- every Social Arbitrage action names the information edge, ticker mapping, financial lag, next confirmation, and falsifier, and routes activated performance to ChrisCamillo;
- one-day trades have a credible immediate repricing mechanism and are conditional on the next tradable price when the market is closed;
- normal investment risk was analyzed rather than used as an automatic veto;
- the recommendation is direct, conditional only where genuinely necessary, and not an executed trade;
- downside, strongest opposing case, and what would change the answer are visible;
- no TaskTracker record, holding, or thesis approval changed without explicit permission.
