# Sensitivity Discovery & Intelligence Protocol — Vitan Growth OS

## Purpose

This protocol transforms the Growth OS from a task executor into a learning system. When the system encounters sensitive relationship dynamics, political risks, payment concerns, or competitive conflicts, it doesn't just solve that case — it builds the pattern into its operating rules so similar situations are handled automatically in the future.

## The Three Loops

### Loop 1: DISCOVER (Proactive Intelligence Gathering)

Every time BB researches a new prospect or enriches an existing contact, it must run this discovery checklist BEFORE drafting any communication:

**Relationship Discovery:**
- Has Vitan worked with this company before? (Check contacts-master history, ask board if unsure)
- Has Vitan worked with any company connected to this one? (parent companies, subsidiaries, splinter companies, joint ventures, former partners)
- Does anyone at this company have personal or professional ties to Vitan's existing clients?
- Is there a competitive dynamic between this prospect and any existing Vitan client?

**Financial Discovery:**
- If past client: What was the payment experience? (Mark: excellent / standard / difficult / non-payer)
- What is this company's general market reputation for vendor payments?
- What project scale do they typically operate at? Does it justify Vitan's fee structure?

**Political Discovery:**
- Has this company gone through a merger, demerger, split, or ownership change recently?
- Are there family dynamics or partner disputes that could affect engagement?
- Is there any public controversy, legal dispute, or reputation risk?
- Would engaging this client create perceived conflicts with existing clients?

**Market Discovery:**
- What are their active and upcoming projects?
- Who are they currently working with (architects, consultants)?
- What are their stated priorities (cost, speed, quality, prestige)?
- What pain points might they have that Vitan's value proposition addresses?

**Discovery Sources:**
- Web search (company news, press releases, court filings)
- LinkedIn (company page, key personnel connections)
- Industry databases and directories
- contacts-master.csv Notes field (board intelligence)
- Shared-workspace intelligence briefs from previous issues

### Loop 2: CLASSIFY (Tag Every Contact With Sensitivity Metadata)

After discovery, every contact must be tagged in contacts-master.csv using these fields:

| Field | Values | Meaning |
|-------|--------|---------|
| Sensitivity Type | none / political / financial / competitive / reputational | Primary risk category |
| Sensitivity Level | green / amber / red | How much caution needed |
| Sensitivity Detail | Free text | Specific risk description |
| Communication Guardrails | Comma-separated codes | Which guardrails auto-apply |
| Discovery Status | undiscovered / partial / complete | Has full discovery been run? |
| Last Discovery Date | ISO date | When was discovery last performed? |

**Sensitivity Levels:**
- **GREEN**: No known risks. Standard engagement protocol applies.
- **AMBER**: Known dynamics that require careful messaging. Agent can proceed but must apply guardrails and flag to board before sending.
- **RED**: High-risk dynamics. Agent must prepare materials but ALL outreach requires explicit board approval. No autonomous sending.

**Communication Guardrail Codes:**
- `NO_COMPETITOR_MENTION` — Never mention specific competitors or other clients by name
- `NO_PRICE_FIRST` — Never lead with pricing; lead with value/savings framework
- `INDEPENDENCE_FRAME` — Include professional independence language in first outreach
- `MILESTONE_PAY_ONLY` — Only propose milestone-linked payment terms
- `PROFITABILITY_CHECK` — Run profitability analysis before proposing engagement
- `BOARD_APPROVE_FIRST` — All outreach must be approved by board before sending
- `CONFIDENTIALITY_OFFER` — Proactively offer NDA or confidentiality clause
- `NO_PAST_DETAIL` — Never reference details of past projects with this client
- `VALUE_LEAD` — Lead with qualitative value-first framing (for example premium perception, decision confidence, execution clarity, or reduced downstream drift). Numeric savings or value-loss language is allowed only when tied to a canonical, approved external-proof source named in the draft or approval packet.
- `WARM_REINTRO` — Use re-introduction framing, not cold outreach

### Loop 3: LEARN (Turn Every Board Correction Into a System Rule)

This is the most critical loop. When the board provides feedback that changes how a contact should be handled:

**Step 1: Capture the correction.**
When the board says something like "HN Safal split from B Safal, don't mention B Safal" or "Arvind doesn't pay well" — this isn't just a note on one contact. It's a new PATTERN.

**Step 2: Generalise the pattern.**
Ask: "What category does this correction fall into?"
- "Don't mention X to Y" → Pattern: COMPETITOR/CONFLICT SENSITIVITY
- "They don't pay well" → Pattern: FINANCIAL RISK
- "They split from Z" → Pattern: CORPORATE RESTRUCTURE SENSITIVITY
- "I know them personally" → Pattern: PERSONAL RELATIONSHIP (handle differently from cold)

**Step 3: Update the system, not just the contact.**
- Update the contact's sensitivity fields in contacts-master.csv
- Add the generalised pattern to this protocol document (append to Learned Patterns section below)
- Check: does this pattern apply to any OTHER contacts? If so, update them too.
- Create an intelligence brief in shared-workspace/intelligence/ documenting the pattern

**Step 4: Verify no outreach violates the new rule.**
- Scan all pending draft messages
- Check all contacts with similar profiles
- If any existing drafts would violate the new pattern → flag to board

## Communication System Integration

### Before drafting ANY outreach message:

```
1. Check contact's Discovery Status
   → If "undiscovered" or "partial": RUN FULL DISCOVERY FIRST
   → If "complete" and Last Discovery Date > 30 days ago: RUN REFRESH

2. Check contact's Sensitivity Level
   → GREEN: Proceed with standard engagement-system.md protocol
   → AMBER: Apply all listed Communication Guardrails automatically
   → RED: Prepare draft but DO NOT queue for sending. Post to issue for board review.

3. Check contact's Communication Guardrails
   → Apply each guardrail code to the message draft
   → Run self-check: "Does this draft violate any guardrail?"
   → If violation found: rewrite before submitting for review

4. Include guardrail compliance note in issue comment:
   "Draft prepared. Guardrails applied: [codes]. Sensitivity: [level]. Discovery: [status]."
```

### When the board provides new intelligence:

```
1. Parse the intelligence for sensitivity implications
2. Update contact record (sensitivity fields)
3. Generalise: does this create a new pattern?
4. If yes: update this protocol's Learned Patterns section
5. Scan all contacts for similar patterns
6. Flag any pending outreach that might be affected
7. Comment on relevant VITA issues with the update
```

## Learned Patterns (Living Section — Agents Add Here)

### Pattern: CORPORATE SPLIT SENSITIVITY
- **Trigger**: Company A and Company B were formerly one entity and split
- **Risk**: Working with one may alienate the other
- **Auto-guardrails**: `NO_COMPETITOR_MENTION`, `INDEPENDENCE_FRAME`, `CONFIDENTIALITY_OFFER`
- **Example**: B Safal / HN Safal split. Vitan works with B Safal → HN Safal engagement requires independence framing.
- **Discovery question to add**: "Has this company recently split from or merged with another entity?"

### Pattern: POOR PAYMASTER HISTORY
- **Trigger**: Past client with difficult payment collection experience
- **Risk**: Investing effort in unprofitable engagement
- **Auto-guardrails**: `MILESTONE_PAY_ONLY`, `PROFITABILITY_CHECK`, `VALUE_LEAD`, `NO_PRICE_FIRST`
- **Example**: Arvind SmartSpaces — 2 past projects, poor payment discipline
- **Discovery question to add**: "If past client, what was the payment experience?"

### Pattern: PERSONAL RELATIONSHIP
- **Trigger**: Board member knows the prospect personally
- **Risk**: Messaging tone must match personal relationship, not cold outreach
- **Auto-guardrails**: `WARM_REINTRO`, `BOARD_APPROVE_FIRST`
- **Discovery question to add**: "Does any board member have a personal connection to this contact?"

### Pattern: TOWNSHIP COMPETITION CONFLICT
- **Trigger**: Prospect’s flagship township is in direct geographic/market competition with a Vitan-designed township.
- **Risk**: Perceived conflict of interest; "township rivalry" dynamic.
- **Auto-guardrails**: `NO_COMPETITOR_MENTION`, `VALUE_LEAD`, `WARM_REINTRO`
- **Example**: Adani Realty (Shantigram) vs Vitan (Applewoods).
- **Discovery question to add**: "Is this prospect’s major project in direct competition with a landmark Vitan project?"

### Pattern: VENDOR LITIGATION HISTORY
- **Trigger**: Public record of litigation between the prospect and previous vendors/contractors regarding payments.
- **Risk**: Financial loss; difficult payment collection.
- **Auto-guardrails**: `MILESTONE_PAY_ONLY`, `PROFITABILITY_CHECK`, `VALUE_LEAD`
- **Example**: K K Group (RK Buildcon) — Saini Shuttering Store vs RK Buildcon litigation.
- **Discovery question to add**: "Are there any public records of payment disputes or litigation with vendors?"

### Pattern: DEEP PROFESSIONAL HISTORY
- **Trigger**: Vitan has a multi-decade history of being the primary/house architect for the prospect.
- **Risk**: Relationship dormancy; messaging must acknowledge legacy without sounding stale.
- **Auto-guardrails**: `WARM_REINTRO`, `BOARD_APPROVE_FIRST`, `VALUE_LEAD`
- **Example**: Bakeri Group — Vitan designed Sakar series, Bakeri City, and personal residence.
- **Discovery question to add**: "What is the full depth of Vitan’s historical involvement with this client’s portfolio?"

### Pattern: COMPETITOR LOCK-IN
- **Trigger**: Prospect has a near-exclusive or high-volume relationship with a specific top-tier architect.
- **Risk**: Low conversion probability; messaging must offer a distinct "wedge" (e.g. execution precision, operational cost savings) or specialized role.
- **Auto-guardrails**: `NO_COMPETITOR_MENTION`, `VALUE_LEAD`, `INDEPENDENCE_FRAME`
- **Example**: Shivalik Group — deep partnership with INI Design Studio.
- **Discovery question to add**: "Does the prospect have a primary architectural partner for their flagship projects?"

---

## System Evolution Rules

1. **Every board correction = a system upgrade.** Never just update one contact. Always ask: "What rule does this create?"
2. **Discovery is continuous, not one-time.** Re-run discovery every 30 days for active prospects, every 90 days for dormant contacts.
3. **The Learned Patterns section grows forever.** Each new pattern makes the system smarter. Never delete patterns.
4. **When in doubt, classify AMBER.** It's better to flag something that turns out fine than to miss something that damages a relationship.
5. **The board is the ultimate authority.** The system proposes, the board disposes. RED sensitivity items never go out without board approval.
