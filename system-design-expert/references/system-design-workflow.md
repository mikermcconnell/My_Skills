# System design workflow

Use this workflow when the goal is to keep a feature or app clean as it grows.

## Main question
System design is mostly about one thing:
- where should each responsibility live?

## Step 1: Define the feature
Start by stating:
- what the feature does
- who uses it
- what inputs and outputs matter
- what business rules are involved

Do not jump straight to file changes before the feature is clear.

## Step 2: Map the layers
For practical app work, think in layers:
- UI and interaction
- route or request handling
- business logic
- data access and persistence
- auth, config, or infrastructure

The goal is not perfect purity. The goal is to avoid collapsing all responsibilities into one place.

## Step 3: Decide the source of truth
Ask:
- where should the real rule live?
- where should validation happen?
- where should trusted calculations happen?
- where should data ownership sit?

Important rules should have one main home.

## Step 4: Check data flow
Ask:
- where does data enter?
- where is it validated?
- where is it transformed?
- where is it stored?
- where is it displayed?
- where could the meaning drift?

If data flow is unclear, the feature design is probably still weak.

## Step 5: Check coupling
Watch for:
- one route doing everything
- business logic split across frontend and backend
- the same rule repeated in multiple places
- imports tightly mixed with presentation
- helpers that know too much about unrelated modules

A good design keeps dependencies understandable.

## Step 6: Prefer the simplest clean shape
Good defaults:
- extend an existing module if the responsibility clearly belongs there
- create a small new module when a responsibility is distinct and growing
- keep a modular monolith before considering service splits
- delay abstraction until the repetition is real

## Launch timing
Use system design review:
- after prompt clarification
- before implementation
- especially for multi-file or multi-layer changes

Usually skip it for:
- small cosmetic tweaks
- simple copy edits
- obvious one-file fixes

## Minimum output
A useful system design pass should include:
- what the feature is
- where the main responsibilities should live
- the main data flow
- the top structure risks
- the recommended shape
- the next implementation step

## Good review questions
- What is the real responsibility here?
- Where should that responsibility live?
- What changes together?
- What should be the single source of truth?
- Am I introducing duplication or hidden coupling?
- Is this putting too much logic in the wrong layer?
