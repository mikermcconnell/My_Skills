# Feature Testing Workflow

## Main idea
Testing is a repeatable check that reduces the chance of shipping polished wrong behavior.

## Apply this order
1. calculations and business logic
2. validation and data transformations
3. filters, aggregations, and summaries
4. imports and exports
5. workflow and UI checks
6. visual polish only when it matters

## Risk questions
For each feature, ask:
- What could break?
- What would matter most if it broke?
- What edge cases are easy to miss?
- What related behavior might regress?
- What should be automated vs checked manually?

## Automated tests are best for
- calculations
- business rules
- validation
- date and time logic
- data transformations
- filters and aggregation
- scheduling logic
- deterministic output rules

## Manual checks are best for
- end-to-end user flow
- sanity checking outputs
- map or chart plausibility
- UI behavior and clarity
- stakeholder-facing confidence checks

## Minimum manual checklist
- main flow works
- one realistic case works
- one edge case works
- one related regression check is done
- output looks plausible in real use

## Minimum verification summary
Before finishing, report:
- automated tests added or run
- manual checks completed
- edge cases considered
- remaining gaps or risks

## Example edge cases
- empty input
- missing values
- invalid format
- duplicate data
- zero values
- extreme values
- date or time rollover
- impossible scenarios
- partial data

## Warning signs
- tests only prove code runs, not that it is correct
- no edge cases were considered
- no regression check was done
- the output still needs a human sanity check
