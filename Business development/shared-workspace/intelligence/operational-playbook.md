# Vitan Operational Playbook — System Health Management

**Purpose**: Document lessons learned from Q2 2026 system capacity assessment. Guide future monitoring and team coordination.

**Created By**: HR Agent  
**Date**: 2026-04-10  
**Status**: Reference document (ongoing updates as new patterns emerge)

---

## 1. Capacity Management Patterns

### PA Bottleneck Pattern
**Symptom**: CEO-level decision-maker also doing IC (individual contributor) work
**Impact**: 
- Queue of decisions waits for PA availability
- Strategic planning delayed when PA is executing tasks
- System throughput constrained

**Solution Approach**:
- Delegate IC work to managers or team leads (create manager-level agent if needed)
- Elevate decisions to board level for faster turnaround (board can decide in parallel)
- Protect PA's calendar for strategy + high-touch decisions only

**Monitoring**:
- Track PA todo queue length; escalate if > 6 items
- Distinguish PA decisions vs PA execution; automate execution
- Weekly review of decision SLAs

---

## 2. Assignment Routing

### Problem: Unassigned Backlog
**Symptom**: New issues created without explicit assignee; sit in backlog waiting for manual routing
**Root Cause**: No auto-routing heuristic; assignment friction between issue creation and agent pickup

**Impact**: 
- Tasks pile up, losing context
- Agents unaware of available work
- Uncertainty about ownership

**Solution Approach**:
Create auto-routing rules:
- **Content/Narratives** → Brand Storyteller
- **Awards/Visibility** → Outreach Coordinator  
- **Client/Growth** → Business Builder
- **Technical/Infrastructure** → Founding Engineer
- **Social/Digital** → Digital Presence Manager
- **People/Capability** → HR

Implement in issue templates: auto-suggest assignee based on work type

**Monitoring**:
- Track unassigned issue count; escalate if > 5
- Monthly review of routing accuracy (wrong agent assignment rate)

---

## 3. Blocker Tracking & Escalation

### Pattern: Cascading Blockers
**Symptom**: One blocked issue blocks downstream work (VITA-211 ArchDaily blocked by VITA-226 metadata)
**Impact**: Multiplier effect; 1 blocker cascades to 3-4 dependent tasks

**Solution Approach**:
- Maintain live blocker tracker ([VITA-400](/VITA/issues/VITA-400)) updated daily
- Identify critical path dependencies
- Escalate blockers if duration > 48 hours
- Daily standup focus on top 3 blockers + escalation actions

**Escalation Ladder**:
1. First 24h: Blocker owner attempts unblock
2. 24-48h: Escalate to owner's manager (PA for FE, etc.)
3. 48h+: Escalate to PA + create blocker issue for board visibility
4. 3+ days: Auto-escalate to board with impact assessment

**Monitoring**:
- Track blocker age; alert on any > 72h
- Document root cause + resolution time for retrospectives

---

## 4. Idle Capacity Activation

### Pattern: Available Agents, Unavailable Work
**Symptom**: BB, DPM, HR have zero tasks while 8+ items sit unassigned in backlog
**Root Cause**: Assignment friction (see #2) + unclear priority

**Solution Approach**:
- Pair idle agents with backlog triage
- Weekly "backlog sprint" where idle agents pick up relevant todo items
- Create explicit "ready for assignment" status for high-priority backlog

**Team Reactivation**:
- **BB**: Growth scanning, competitive research (WS1 + WS2 inputs)
- **DPM**: Social presence monitoring, content amplification (tied to WS4)
- **HR**: Capability planning, team health intelligence (tied to WS3)

**Monitoring**:
- Alert if any agent idle > 1 week
- Monthly utilization report by agent + workstream

---

## 5. System Health Dashboard

### Key Metrics to Track (Daily)
| Metric | Target | Alert Level | Action |
|--------|--------|-------------|--------|
| PA todo queue | < 4 | > 6 | Delegate/elevate |
| Unassigned backlog | < 3 | > 5 | Triage + route |
| Blocked issues | < 2 | > 3 | Escalate + unblock |
| Agent utilization | > 60% avg | < 40% for agent | Activate/retask |
| Average blocker age | < 24h | > 48h | Daily escalation |

### Dashboard Owner
HR agent maintains [VITA-400](/VITA/issues/VITA-400) (System Blocker Tracker)
- Daily update (end of business)
- Weekly summary (Monday morning)
- Monthly trend analysis (last Friday)

---

## 6. Team Development & Capability Planning

### Proactive Capability Assessment (WS3 Input)
When PA evaluates expansion:
1. **Identify Required Skills**: What does this domain need?
2. **Assess Current State**: Do we have these skills in-house?
3. **Gap Analysis**: High/Medium/Low severity gaps
4. **Build vs. Buy vs. Partner**: Cost/timeline trade-offs
5. **Recommendation**: Go/No-go + hiring plan + timeline

**Tool**: [Capability Assessment Framework](/shared-workspace/intelligence/capability-assessment-framework.md)
**Turnaround**: 1-2 weeks per assessment

### Skill Upgrades
Track when agents are stretched beyond capability:
- FE handling Paperclip integration issues (not full-time architecture)
- OC doing awards strategy without dedicated training

Plan quarterly skill development:
- Technical certifications (FE: Paperclip internals)
- Domain certifications (Brand Storyteller: Architecture publications)
- Leadership development (manager-level agent preparation)

---

## 7. Communication Patterns

### Board Interaction Best Practices
(From 2026-04-02 learning: board responses most effective with 3 explicit decisions)

**Effective Request Format**:
1. **Destination**: Where should decision happen? (PA, board, agent)
2. **Owner**: Who owns implementation?
3. **SLA**: By when does this need resolution?

**Example (Good)**:
"Board approval needed for Q2 Brand Strategy deck. Owner: PA. SLA: April 10 EOD. Decision: Approve/Reject/Request changes."

**Example (Weak)**:
"Please review the strategy deck when you get a chance."

---

## 8. Retrospectives & Continuous Improvement

### KAIZEN: Mandatory After Issue Completion
When marking any issue done, add retrospective comment:
- What worked well?
- What didn't work?
- What would make it 10x better?
- System improvement suggestion?

**Example**:
```
✅ Marked VITA-331 done

Retrospective:
- Worked: PA's focused execution once SLA was clear
- Didn't work: Unclear board approval timeline delayed this 3 days
- Better: Proactive board SLA clarification before assigning PA work
- System improvement: Add "approval SLA" field to issue template for visibility-type tasks
```

### Monthly Retrospective Review
HR collects retrospectives from all completed issues:
- Pattern recognition (repeated gaps, workarounds)
- Create follow-up KAIZEN issues for system improvements
- Share learnings in shared-workspace/intelligence/learnings/

---

## 9. Red Flags & Escalation Triggers

### Watch For These Patterns
- ⚠️ PA todo queue > 6: CEO overloaded, delegation needed
- ⚠️ Unassigned backlog > 5: Routing friction, needs process fix
- ⚠️ Any blocker > 72h: Critical path at risk, escalate
- ⚠️ Agent idle > 1 week: Utilization problem, retask or pause hiring
- ⚠️ Same mistake repeated 2x: System issue, create KAIZEN task
- ⚠️ Board SLA missed 2x: Process broken, escalate to board

### Escalation Owners
- PA capacity → Escalate to PA + board
- Blocker duration → Escalate to blocker owner's manager
- System issues → Create KAIZEN task for HR + PA
- Board SLA → Escalate to board directly

---

## 10. Integration with Growth OS

This playbook supports all 4 workstreams:

**WS1 (Client Scanning)**: BB needs active assignment; use idle time for prospect research
**WS2 (Competition)**: BB uses unassigned time for competitive intelligence
**WS3 (Expansion)**: HR uses capability framework to assess new domains
**WS4 (Execution)**: DPM uses idle time for social amplification of WS4 content

---

## Document History

| Date | Version | Changes |
|------|---------|---------|
| 2026-04-10 | 1.0 | Initial version based on system health assessment |
| [TBD] | 1.1 | Updated with first month of operational experience |

---

**Owner**: HR Agent  
**Review Frequency**: Monthly  
**Audience**: PA, all agents, board  
**Storage**: shared-workspace/intelligence/operational-playbook.md
