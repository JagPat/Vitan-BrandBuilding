# Board Digest Template

Owner: Principle Architect  
Use for: morning and evening board digests  
Status: active reference

## Filename Pattern

- Morning: `board-morning-digest-YYYY-MM-DD.md`
- Evening: `board-evening-digest-YYYY-MM-DD.md`

## Required Header

```md
# Board Morning Digest

Date: YYYY-MM-DD
Prepared by: Principle Architect
```

or

```md
# Board Evening Digest

Date: YYYY-MM-DD
Prepared by: Principle Architect
```

## Required Sections

### Headline

- one status line only: `GREEN`, `AMBER`, or `RED`
- one sentence on why that status is true

### Planning Cascade Health

- current `planningCascade.strategy` signal state when available
- current state of `SOCIAL_STRATEGY.md`
- current state of latest `strategy-brief-*.md`
- current state of latest `weekly-plan-*.md`
- note whether daily content review is operating normally

If any expected artifact is missing or stale, call it out explicitly.
If the platform-health signal is unavailable, say that manual repo inspection was used as fallback.

### Active Execution

- list the highest-value live execution items only
- prefer board-relevant work over routine low-signal queue noise

### Main Blockers

- name the blocking chain clearly
- separate upstream dependency blockers from execution-quality blockers
- avoid vague wording such as "pending" without naming the event needed

### Strategic Risks

- list only material risks
- include planning, market, capability, or platform risks when they affect delivery

### Next Actions

- one line each for BB, DPM, BS, OC, FE, HR, PA when relevant
- omit agents with no relevant action

### Sources Consulted

- every digest must end with a `Sources Consulted` section
- include governance docs, issue identifiers, and artifact paths actually used

## Status Rules

- `GREEN`: planning cascade healthy, no major blockers threatening current execution
- `AMBER`: execution continues, but at least one significant blocker or missing artifact needs action
- `RED`: planning cascade broken or major delivery path halted without a credible near-term recovery path

## Writing Rules

- keep it concise and executive-readable
- use direct operational language, not motivational language
- do not expose secrets, credentials, or sensitive client details
- do not imply certainty where an upstream dependency is unresolved

## Minimum Inputs Before Writing

- current `planningCascade.strategy` health signal when available
- current open issue snapshot
- latest architecture/governance changes
- active blocker chain status
- latest strategy and weekly-plan artifact availability

## Sources Consulted

- `SYSTEM_ARCHITECTURE.md`
- `Business development/shared-workspace/drafts/README.md`
- `Business development/shared-workspace/review/vita288/board-evening-digest-2026-04-05.md`
- [VITA-289](/VITA/issues/VITA-289)
