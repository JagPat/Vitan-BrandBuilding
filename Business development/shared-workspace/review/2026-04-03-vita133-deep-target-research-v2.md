# VITA-133 Deep Target Research v2 (Decision-Maker Layer)

Date: 2026-04-03
Issue: [VITA-133](/VITA/issues/VITA-133)
Parent: [VITA-7](/VITA/issues/VITA-7)
Owner: Business Builder

## Objective
Replace generic mailbox outreach with named decision-maker targeting wherever verifiable.

## Research Method (Depth Upgrade)
1. Identify company-specific leadership routes (official site + corporate profiles).
2. Identify named senior leaders from company LinkedIn/public pages.
3. Score each candidate by verification confidence.
4. Build enrichment queue for direct-work email validation (Apollo/Clearbit/Hunter-like tooling).
5. Route only high-confidence, role-matched contacts into send window.

## Confidence Scale
- `high`: name + role + company source alignment confirmed.
- `medium`: name linked to company, role inferred from recent context.
- `low`: role known but person not verified.

## First-5 Account Intelligence

### 1) HN Safal
- Current status: no high-confidence named leader captured from public sources in this pass.
- Route currently available: `sales@hnsafal.com` (fallback only).
- Decision-maker roles to target:
  - Managing Director
  - Founder Office
  - Business Development Head
- Confidence: `low` (role-only).
- Required enrichment action: identify 2-3 named leaders and direct emails before send.

### 2) Arvind SmartSpaces
- Named decision-maker candidates:
  - Priyansh Kapoor — CEO & Whole-Time Director (public LinkedIn profile evidence).
  - Kamal Singal — MD & CEO reference appears in public profile context; role recency needs verification.
- Current route: `investor@arvindinfra.com` (routing fallback, not final executive inbox target).
- Confidence:
  - Priyansh Kapoor: `high`
  - Kamal Singal role recency: `medium`
- Required enrichment action: validate active executive office email path and executive assistant route.

### 3) Shivalik Group (Ahmedabad)
- Named decision-maker candidate:
  - Chitrak Shah — public profile indicates Shivalik Group affiliation.
- Current route: `info@shivalikgroup.com` (fallback only).
- Confidence: `medium` (affiliation clear, final role title needs confirmation).
- Required enrichment action: confirm exact title and direct business email.

### 4) Goyal & Co. (Ahmedabad)
- Current status: Ahmedabad project organization visible; named Ahmedabad leadership contacts not confidently verified in this pass.
- Current routes:
  - `vinay@goyalco.com`
  - `sales@goyalco.com`
- Decision-maker roles to target:
  - Director (Ahmedabad operations)
  - Corporate leasing/business head
- Confidence: `low` (role + route only).
- Required enrichment action: identify named Ahmedabad leadership and direct work emails.

### 5) Iscon Group
- Current status: no high-confidence named real-estate leadership contact captured in this pass.
- Current route: `jp@iscongroup.com` (existing route, ownership not yet verified).
- Decision-maker roles to target:
  - Founder Office
  - Development Head
  - Business Head
- Confidence: `low`.
- Required enrichment action: verify ownership of `jp@` route and map at least 2 named leaders.

## Output for Operations
- New enrichment queue file:
  - `Business development/shared-workspace/review/2026-04-03-vita133-apollo-enrichment-queue.csv`
- This queue is ready for Apollo-style bulk enrichment and confidence updates.

## Immediate Recommendation
Do not send to role-generic inboxes alone for top-management outreach unless:
1. named recipient is unavailable after enrichment, and
2. a parallel referral route exists (EA/office line/common contact).

## Source Pointers
- Arvind SmartSpaces company + leadership activity (LinkedIn public context)
- Priyansh Kapoor profile (Arvind SmartSpaces CEO/WTD context)
- Shivalik Group profile context and associated leadership profiles
- Existing official contact routes already in VITA-133 pack (fallback routes only)
