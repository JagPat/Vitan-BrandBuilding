# Git Coordination Protocol — Vitan Growth OS

## Branch Isolation (7 Agents)

| Agent | Branch | Primary Dimensions |
|-------|--------|-------------------|
| Business Builder (BB) | `agent/bb` | Dim 1: Client Acquisition, Dim 11: Strategic Partnerships |
| Founding Engineer (FE) | `agent/fe` | Dim 4: Website & SEO (technical), Infrastructure |
| Principle Architect (PA) | `agent/pa` | Strategic Oversight, Quality Gate, Vision |
| HR | `agent/hr` | Dim 7: Academic Engagement, Talent Pipeline |
| Brand Storyteller (BS) | `agent/bs` | Dim 2: Industry Portals, Dim 8: Publications, Dim 9: Media/PR |
| Outreach Coordinator (OC) | `agent/oc` | Dim 5: Awards, Dim 6: Speaking, Dim 10: Associations |
| Digital Presence Manager (DP) | `agent/dp` | Dim 3: Social Media, Dim 4: Website (content), Dim 12: Reputation |

## Protected Main Branch

- Direct push to `main` is **blocked** for all agents
- All changes go through PRs: `agent/{name}` → `main`
- PA agent or board merges approved PRs
- After merge, agents sync their branches from latest main

## File Ownership (Advisory)

| Path | Primary Owner | Secondary |
|------|--------------|-----------|
| shared-workspace/references/ | PA | All agents |
| shared-workspace/contacts-master.csv | BB | PA |
| shared-workspace/review/{issue-id}/ | Assigned agent | PA |
| shared-workspace/deliverables/content/ | BS | PA |
| shared-workspace/deliverables/outreach/ | OC | PA |
| shared-workspace/deliverables/social/ | DP | HR |
| shared-workspace/deliverables/analytics/ | DP | PA |
| shared-workspace/references/awards-calendar.md | OC | PA |
| shared-workspace/references/publishing-protocol.md | DP | BS, BB |
| shared-workspace/references/sensitivity-protocol.md | BB | PA |
| shared-workspace/references/brand-ecosystem.md | PA | All |

## Cross-Agent Coordination Rules

1. Never modify files another agent is actively working on
2. Use shared-workspace/references/ for inter-agent communication
3. If you need content from another agent's domain, create an issue requesting it
4. PA agent is the merge authority — tag PA in your PR description
5. All deliverables must go through shared-workspace/review/ before final
