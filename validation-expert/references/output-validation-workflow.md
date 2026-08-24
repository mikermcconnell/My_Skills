# Output Validation Workflow

## Main idea
Validation checks whether a result should be trusted in the real-world context.

## Testing vs validation
- Testing: does the feature work correctly?
- Validation: should the output be trusted for the real use case?

## Apply this order
1. define what the output is for
2. inspect source data quality
3. surface assumptions
4. review formula or method
5. run sanity checks against known reality
6. decide confidence level and review needs

## Good validation questions
- What is this output meant to support?
- What data is it based on?
- Is the data complete and current enough?
- What assumptions matter most?
- Could this be technically correct but misleading?
- Does it pass a common-sense check?
- What would a domain expert challenge?
- Is this exploratory, internal-only, or decision-ready?

## Common validation checks
- compare result to known recent values
- compare summary to detail totals
- check whether averages hide important variation
- check whether missing data changes interpretation
- check whether labels or wording overstate certainty
- check whether the rule or metric definition matches the real business use

## Confidence levels
- Low confidence: incomplete data, weak assumptions, exploratory only
- Medium confidence: mostly sound, but still needs caution or review
- High confidence: sound data, reasonable assumptions, sanity-checked, and appropriate for action

## Warning signs
- output looks too neat
- assumptions are hidden
- incomplete data is not mentioned
- summary sounds more certain than the evidence supports
- result conflicts with known reality
- no stakeholder or domain review on a high-stakes output

## Minimum validation summary
Before finishing, report:
- output purpose
- key assumptions
- sanity checks performed
- confidence level
- remaining uncertainty
- whether domain review is still needed
