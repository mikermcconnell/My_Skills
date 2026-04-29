---
name: opportunity-brainstorm
description: Structured opportunity brainstorming for personal strategy. Explores the intersection of skills, interests, constraints, and market trends to identify high-leverage plays. Uses interactive questions to build a profile, then proposes 2-3 approaches with trade-offs. Triggers include "opportunity", "brainstorm opportunities", "what should I build", "side hustle", "career move", "investment thesis", "where to focus", "strategic direction", or any request to explore personal/professional opportunities.
---

# Opportunity Brainstorming Framework

Structured exploration of opportunities at the intersection of someone's skills, interests, constraints, and market conditions. Produces a clear strategy with prioritized approaches.

## Process

Use `AskUserQuestion` for ALL questions (interactive form format, not inline text). One topic per question round. Multiple choice preferred, multiSelect where appropriate.

### Phase 1: Profile & Context (2-3 rounds)

**Round 1 — Opportunity type** (multiSelect):
- Career acceleration
- Side business / consulting
- Investment thesis
- Tool building
- Other

**Round 2 — Timeline & risk appetite** (2 questions):
- Time horizon: Already started / 3-6 months / 1-2 years / Exploring only
- Risk tolerance: Stay put / Internal pivot / Jump when ready / Aggressive move

**Round 3 — Current state & constraints** (2 questions):
- What's already in motion? (multiSelect): Active projects, skill-building, investments, applied at work
- Biggest constraint: Time / Capital / Network / Direction

### Phase 2: Thesis & Vision (1-2 rounds)

**Round 4 — Where's the disruption?**
- Tailor options to the person's domain and interests
- Ask where they see the biggest opportunity for AI/tech/market disruption

**Round 5 — Success definition**
- What does success look like in 2-3 years?
- Options should span: reputation, revenue, returns, role advancement

**Round 6 (if needed) — Edge thesis**
- What's your specific advantage?
- Why you and not someone else?

### Phase 3: Approach Design (present, don't ask)

Based on answers, propose **2-3 approaches** with:
- Clear description of what it looks like in practice
- Why it wins (advantages, leverage points)
- Risk/downside
- Your recommendation with reasoning

Ask which direction resonates (single select).

### Phase 4: Design & Deliverables

Flesh out the chosen approach into:
- **Vision statement** (1-2 sentences)
- **Core modules/components** (3-5 areas of focus)
- **Integration with existing work** (how it builds on what's already happening)
- **Success metrics** (how you'll know it's working)

Then offer to save as:
1. **Design doc** — `docs/plans/YYYY-MM-DD-<topic>-design.md`
2. **Personal strategy skill** — `~/.Codex/skills/my-strategy/skill.md` (updateable reference)

## Key Principles

- **One question per topic** — Don't overwhelm
- **Use AskUserQuestion tool** — Always interactive form format
- **Lead with recommendation** — Don't be neutral; have a point of view
- **High-leverage only** — If the person is time-constrained, filter ruthlessly for compound-return activities
- **No fluff** — Concrete actions, not motivational platitudes
- **Revisitable** — The strategy skill should be a living document the person can update

## Anti-Patterns

- Don't ask more than 6 rounds of questions before proposing approaches
- Don't present more than 3 approaches (decision fatigue)
- Don't be afraid to tell someone an idea is weak — honest assessment > encouragement
- Don't conflate "interesting" with "high ROI" — filter for leverage
