---
name: my-strategy
description: Personal strategy reference for Mike McConnell. Captures current strategic direction, opportunity thesis, and priorities across career, investments, and side projects. Use when making decisions about where to spend time, what to build next, or how to evaluate opportunities. Triggers include "my strategy", "what am I working toward", "should I pursue this", "priority check", "time allocation", "is this worth it", or any decision that benefits from strategic context.
---

# My Personal Strategy

Last updated: 2026-02-25

## Identity & Position

| Dimension | Current State |
|-----------|---------------|
| **Day job** | Transit Projects Lead, Barrie Transit (stable, staying put) |
| **Side focus** | AI-powered investing tools + agentic coding |
| **Investing style** | Active, AI-informed, building custom tooling for personal edge |
| **AI skill level** | Actively building with Codex, MCP, skills, agents |
| **Constraint** | Time — full-time job + life limits available hours |

## Strategic Direction: AI Quant Stack + Compounding Flywheel

**Vision:** Build a private, AI-powered investment research and execution platform that synthesizes information at scale, executes systematically, and learns from every decision over time.

**Why this wins:**
- Compounds across everything I'm already doing (investing app, agentic coding, AI investments)
- Every hour invested makes my tools better AND makes me a better investor
- The tooling moat is real — most retail investors can't build this
- Agents do the work while I'm at my day job (time-leverage)

**2-3 year success metric:** Consistently outperform the market with AI-informed strategy.

## Alpha Thesis

My edge comes from three sources:
1. **Information synthesis** — AI processes earnings calls, filings, news, sentiment at scale
2. **Systematic execution** — Remove emotion, automate strategies, backtest rigorously
3. **Tooling moat** — My ability to BUILD custom AI investing tools is itself the edge

**Keep it private** — sharing tools dilutes the alpha.

## Core Modules (Priority Order)

### 1. AI Research Agents
- Earnings call transcript analysis (key metrics, sentiment, guidance changes)
- SEC filing monitor (10-K, 10-Q, 8-K material change detection)
- News/sentiment aggregation for watchlist
- Macro indicator synthesis (Fed, employment, CPI)

### 2. Systematic Screening & Signals
- Custom factor screens (value + momentum, quality) on schedule
- Technical signal alerts (extends existing alert system)
- Sector rotation signals based on macro regime
- Position sizing based on conviction + risk

### 3. Decision Flywheel (Learning System)
- Trade journal: every entry/exit with rationale + AI analysis snapshot
- Thesis tracker: expected vs. actual outcomes
- Pattern engine: after 50+ decisions, surface correlations with best/worst trades
- Strategy scorecard: performance by strategy type

### 4. Command Center (Existing App, Enhanced)
- Dashboard: portfolio, active signals, pending research
- Agent status: what ran, what it found, what needs attention
- Weekly digest: AI-generated portfolio summary + recommended actions

## Integration With Existing Work

| Existing | Extends Into |
|----------|-------------|
| Flask investing app | Command center, dashboards, all UI |
| `src/analysis/` | Systematic screening, signals |
| `src/monitor/alerts.py` | Signal alerts, filing monitors |
| `src/portfolio/` | Decision flywheel, trade journal |
| Agentic coding skills | Building the agents themselves |
| AI stock positions | Informed by my own research tools |

## Decision Filter

When evaluating whether to spend time on something, ask:

1. **Does it compound?** — Will this make my tools/skills/portfolio better over time?
2. **Is it high-leverage?** — Does AI do the heavy lifting, or am I doing manual work?
3. **Does it fit the stack?** — Can it integrate with what I've already built?
4. **Is the time cost justified?** — Given my constraint, is this the best use of limited hours?

If it doesn't pass at least 3 of 4, skip it.

## What I'm NOT Doing

- Not productizing or sharing tools (dilutes alpha)
- Not leaving Barrie Transit (stable base)
- Not consulting or freelancing on AI (time constraint)
- Not chasing every AI trend — focused on investing tooling specifically
