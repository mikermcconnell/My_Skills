# Release Workflow

## Main idea
Deployment discipline makes changes safe to release, easier to understand, and easier to recover from.

## Built vs ready
- Built: the feature exists
- Tested: logic was checked
- Validated: the output makes sense in real use
- Ready: the release risk is understood and the change is safe enough to rely on

## Apply this order
1. define what changed
2. define the release risk
3. confirm testing and validation happened
4. run a short release checklist
5. check rollback or recovery path
6. leave a short release record

## Good release questions
- What changed?
- What did not change?
- What old behavior could this have broken?
- Is this low, medium, or high risk?
- What was tested?
- What was validated?
- If this fails, how do we go back?
- Is this ready for local use, stakeholder review, or operational reliance?

## Minimum release checklist
- main flow works
- one realistic case works
- one regression check was done
- final output still looks plausible
- stakeholder-facing limitations are clear if needed

## Rollback thinking
Rollback can mean:
- last good commit
- last stable deployed version
- previous config or settings
- last known-good data snapshot

If rollback is weak or unclear, say so.

## Risk guide
- Low risk: cosmetic or low-impact changes
- Medium risk: workflow changes, filters, imports, or non-trivial UI logic
- High risk: calculations, scheduling logic, blocking logic, dashboard metrics, operational outputs, public-facing outputs

## Minimum release summary
Before finishing, report:
- what changed
- risk level
- what was tested
- what was validated
- rollback path
- remaining concern or unknown
