# Evaluation Baselines

Owner: Board-controlled artifact  
Status: Bootstrap baseline set  
Last published: 2026-04-06

## Core Rule

This file is the scoring function for the operating system.

- After publication, Principle Architect and other agents may enforce this file but may not change it unilaterally.
- Baseline changes require explicit board approval.
- If a metric cannot be measured from external or system-recorded evidence, verdict is `UNMEASURED`, not `PASS`.

## Current Baseline Set

| Metric | Scope | Baseline / Threshold | Verdict Trigger |
| --- | --- | --- | --- |
| Strategy-to-publish time | system | `< 7 days` | `PASS` when met, `REVERT/KAIZEN` when repeatedly missed |
| Full cycle time | system | `< 14 days` | `PASS` when met, `REVERT/KAIZEN` when repeatedly missed |
| Cascade completion rate | system | `100%` | `PASS` only when all required milestones complete |
| Relay drop rate | system | `0` | any drop is failure evidence |
| PA approval latency | PA | `< 4 hours` | `PASS` when met |

## Bootstrap Note

These baseline values are seeded from the current operating directives so the repo has an enforceable starting point. Future edits require board approval, not PA discretion.

## Auto-Revert Use

- Experiments that worsen the measured metric against this file must be reverted immediately.
- Flat results do not qualify for adoption.
- Improvements may be proposed for ratchet review, but not written here without board approval.

## Evidence Rules

- Agent self-reports are not sufficient evidence.
- Acceptable evidence sources include tracked artifacts, issue timelines, platform-health data, scorecards, and externally verifiable output.

## Sources Consulted

- Principle Architect operating instructions loaded for 2026-04-06
- `SYSTEM_ARCHITECTURE.md`
