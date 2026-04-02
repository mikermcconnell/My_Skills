---
name: risk-register
description: Build and maintain project risk registers with standardized assessment and mitigation strategies. Use when identifying risks, assessing impact/probability, developing mitigation plans, or reporting on risk status. Triggers include "risk register", "risk assessment", "identify risks", "what could go wrong", "mitigation", "risk matrix", "probability and impact", "risk management", "contingency plan", "risk reporting", or any request to analyze, document, or track project or operational risks.
---

# Risk Register Management

Create and maintain comprehensive risk registers for transit planning and strategic initiatives.

## Risk Register Structure

```markdown
# [Project Name] Risk Register

Last Updated: [Date]
Risk Owner: [Name/Role]
Review Frequency: [Monthly/Quarterly]

## Risk Summary Dashboard

| Category | High | Medium | Low | Total |
|----------|:----:|:------:|:---:|:-----:|
| Strategic | | | | |
| Operational | | | | |
| Financial | | | | |
| External | | | | |
| **Total** | | | | |
```

## Risk Categories for Transit

| Category | Description | Examples |
|----------|-------------|----------|
| **Strategic** | Risks to achieving strategic goals | Ridership decline, competition from rideshare |
| **Operational** | Risks to service delivery | Driver shortage, vehicle breakdowns |
| **Financial** | Budget and funding risks | Cost overruns, revenue shortfall, grant loss |
| **Regulatory** | Compliance and legal risks | AODA requirements, environmental regulations |
| **Technology** | IT and systems risks | System failures, cybersecurity, vendor lock-in |
| **External** | Factors outside control | Economic downturn, pandemic, political change |
| **Reputational** | Public perception risks | Safety incidents, service failures |
| **Project** | Implementation risks | Schedule delays, scope creep |

## Risk Assessment Matrix

### Probability Scale

| Score | Level | Description |
|:-----:|-------|-------------|
| 5 | Almost Certain | >90% likely in plan period |
| 4 | Likely | 60-90% likely |
| 3 | Possible | 30-60% likely |
| 2 | Unlikely | 10-30% likely |
| 1 | Rare | <10% likely |

### Impact Scale

| Score | Level | Financial | Service | Reputation |
|:-----:|-------|-----------|---------|------------|
| 5 | Severe | >$5M | >20% service loss | Provincial/national media |
| 4 | Major | $1-5M | 10-20% service loss | Sustained local media |
| 3 | Moderate | $250K-1M | 5-10% service loss | Some media coverage |
| 2 | Minor | $50K-250K | 2-5% service loss | Customer complaints |
| 1 | Negligible | <$50K | <2% service loss | Minimal notice |

### Risk Score Matrix

```
              IMPACT
           1  2  3  4  5
         ┌──┬──┬──┬──┬──┐
       5 │ 5│10│15│20│25│  PROBABILITY
         ├──┼──┼──┼──┼──┤
       4 │ 4│ 8│12│16│20│
         ├──┼──┼──┼──┼──┤
       3 │ 3│ 6│ 9│12│15│
         ├──┼──┼──┼──┼──┤
       2 │ 2│ 4│ 6│ 8│10│
         ├──┼──┼──┼──┼──┤
       1 │ 1│ 2│ 3│ 4│ 5│
         └──┴──┴──┴──┴──┘

HIGH (15-25): Red     - Immediate action required
MEDIUM (8-14): Yellow - Active monitoring/mitigation
LOW (1-7): Green      - Monitor periodically
```

## Individual Risk Entry Template

```markdown
## RISK-[XXX]: [Risk Title]

| Attribute | Value |
|-----------|-------|
| **Category** | [Strategic/Operational/Financial/etc.] |
| **Risk Owner** | [Name/Role] |
| **Date Identified** | [Date] |
| **Status** | [Open/Mitigating/Closed/Accepted] |

### Description
[Clear statement of what could go wrong and the consequence]

### Assessment

| Dimension | Inherent | Residual |
|-----------|:--------:|:--------:|
| Probability | [1-5] | [1-5] |
| Impact | [1-5] | [1-5] |
| **Risk Score** | [P×I] | [P×I] |

### Root Causes
- [Cause 1]
- [Cause 2]

### Consequences if Realized
- [Consequence 1]
- [Consequence 2]

### Mitigation Strategies

| Strategy | Type | Owner | Due Date | Status |
|----------|------|-------|----------|--------|
| [Action] | [Prevent/Reduce/Transfer/Accept] | [Name] | [Date] | [Status] |

### Monitoring Indicators
- [Early warning sign 1]
- [Early warning sign 2]

### Contingency Plan
[What to do if risk materializes despite mitigation]

### History
| Date | Update |
|------|--------|
| [Date] | Risk identified |
| [Date] | [Status change/update] |
```

## Transit Strategic Plan Common Risks

### Strategic Risks

| ID | Risk | P | I | Score |
|----|------|:-:|:-:|:-----:|
| S-01 | Ridership fails to recover post-pandemic | 3 | 4 | 12 |
| S-02 | Autonomous vehicles reduce transit demand | 2 | 4 | 8 |
| S-03 | Rideshare/micromobility competition | 3 | 3 | 9 |
| S-04 | Regional integration fails to materialize | 2 | 3 | 6 |

### Operational Risks

| ID | Risk | P | I | Score |
|----|------|:-:|:-:|:-----:|
| O-01 | Driver recruitment/retention challenges | 4 | 4 | 16 |
| O-02 | BEB reliability issues during transition | 3 | 3 | 9 |
| O-03 | Fleet capacity insufficient for growth | 3 | 4 | 12 |
| O-04 | TOD demand exceeds capacity | 3 | 2 | 6 |

### Financial Risks

| ID | Risk | P | I | Score |
|----|------|:-:|:-:|:-----:|
| F-01 | Provincial/federal funding reduction | 3 | 5 | 15 |
| F-02 | Electrification costs exceed budget | 3 | 4 | 12 |
| F-03 | Fare revenue below projections | 3 | 3 | 9 |
| F-04 | Unexpected infrastructure costs | 2 | 3 | 6 |

### External Risks

| ID | Risk | P | I | Score |
|----|------|:-:|:-:|:-----:|
| E-01 | Economic recession reduces ridership | 2 | 4 | 8 |
| E-02 | Boundary expansion accelerates timeline | 3 | 3 | 9 |
| E-03 | Climate events disrupt service | 3 | 3 | 9 |
| E-04 | Supply chain delays for buses/parts | 3 | 3 | 9 |

## Mitigation Strategy Types

| Type | Description | When to Use |
|------|-------------|-------------|
| **Avoid** | Eliminate the risk entirely | Risk is unacceptable; alternatives exist |
| **Reduce** | Lower probability or impact | Most common; active management |
| **Transfer** | Shift risk to third party | Insurance, contracts, partnerships |
| **Accept** | Acknowledge and monitor | Low risks; mitigation cost > benefit |
| **Exploit** | Turn threat into opportunity | Risk has potential upside |

## Reporting Template

```markdown
## Risk Report: [Period]

### Risk Status Summary

| Status | Count | Change |
|--------|:-----:|:------:|
| High risks | X | [+/-] |
| Medium risks | X | [+/-] |
| Low risks | X | [+/-] |
| Risks closed | X | [+/-] |

### Top 5 Risks

| Rank | Risk | Score | Trend | Owner |
|:----:|------|:-----:|:-----:|-------|
| 1 | [Risk] | XX | [↑↓→] | [Name] |
| 2 | [Risk] | XX | [↑↓→] | [Name] |
| 3 | [Risk] | XX | [↑↓→] | [Name] |
| 4 | [Risk] | XX | [↑↓→] | [Name] |
| 5 | [Risk] | XX | [↑↓→] | [Name] |

### Risks Requiring Attention
[Narrative on risks that need escalation or decision]

### Emerging Risks
[New risks identified this period]

### Risks Closed
[Risks removed and why]
```

## Best Practices

1. **Review regularly** - Monthly for active projects, quarterly for strategic
2. **Assign owners** - Every risk needs an accountable person
3. **Track residual risk** - Show mitigation effectiveness
4. **Use early warnings** - Define triggers that indicate risk is increasing
5. **Document decisions** - Record risk acceptance rationale
6. **Connect to actions** - Mitigation must be in work plans with due dates
7. **Communicate upward** - High risks require leadership visibility
