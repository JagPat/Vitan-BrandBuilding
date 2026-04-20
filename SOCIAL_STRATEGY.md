# SOCIAL_STRATEGY

Last updated: 2026-04-20 (UTC, Skyscraper Wave & 'Efficiency of Grandeur' update)
Owner: Business Builder
Canonical status: repo-tracked source of truth for DPM, BS, and OC. Agent-local notes must defer to this file.

## 1. Objectives

- Grow qualified awareness for Vitan Architects across LinkedIn, Facebook, Instagram, and X.
- Convert social attention into tracked inquiry actions through `connect@vitan.in`.
- Build repeatable proof-first storytelling around Vitan projects, design philosophy, and delivery rigor.
- Position Vitan as the "Execution Specialist" for the 2026 Ahmedabad Skyscraper Wave.
- Keep the strategy -> weekly plan -> review cascade explicit in git so downstream agents are never dependent on implicit or agent-local state.

## 2. Core Brand Direction

- Human impact first: spaces as lived experience, not visual spectacle alone.
- Calm authority: practical, confident, specific.
- Execution credibility: design quality plus delivery discipline.
- **Value Positioning:** Lead with: "We are a profit centre, not a cost." Vitan's experience saves 10-15% on execution costs.
- Use only `Vitan Architects` in new outward-facing copy.
- Canonical website: `https://www.vitan.in`
- Canonical inquiry contact for new outbound content: `connect@vitan.in`
- Do not reintroduce legacy outward identifiers such as `Jagrut & Partners`, `#jagrutandpartners`, or non-canonical domain/email references.

## 3. Content Pillars (Current Weights)

- Project proof and case snapshots (Focus on High-Rise): 40% (+5%)
- Process and execution insights (Profit Centre model): 25% (+5%)
- Founder perspective / philosophy: 20% (-5%)
- Capability and firm proof points: 10% (-5%)
- Market commentary and trend POV (Skyscraper Wave): 5%

## 4. Platform Guidelines

### LinkedIn

- Primary business narrative and authority channel.
- Format: 1-2 short paragraphs, strong opening line, one clear CTA.
- Best use: project proof, founder POV, developer-facing insights, and `Proof vs Pattern` contrasts. Focus on vertical urbanism ROI.

### Facebook

- Community reinforcement and reach extension channel.
- Format: concise caption plus visual proof with stronger local relevance.
- Best use: project highlights, milestones, branded stats, and trust-signal reinforcement.

### Instagram

- Visual-first storytelling channel.
- Format: image-led post plus concise caption and focused hashtags.
- Non-negotiable: publish flow requires publicly accessible `image_url` for API-based posting.
- **Image Direction:** High-contrast, monolithic shots for the "Rising Skyline" theme.

### X

- Secondary channel; keep lower priority unless account credits and execution stability are confirmed.
- Publish readiness gate: verify X API account credits/plan before execution to avoid `402 CreditsDepleted` failures.

## 5. Conversion Hooks And Measurement

Conversion rule:
- Every post carries exactly one intent CTA.
- Approved CTA set:
  - `Book a 20-minute project-fit discussion`
  - `Request a site-responsive concept review`
  - `Share your project brief for a first-pass feasibility response`
  - `Inquire about our 10-15% execution saving model for high-rise projects` (New)

Weekly measurement pack:
- Post level: reach, saves, comments, inbound DMs, CTA clicks/replies.
- Funnel level: touched, replied, meeting booked, proposal started, proposal won.
- Brand hygiene: count of legacy-name/domain traces discovered and corrected.

## 6. Process-Led Thought Leadership Rules

Use process/capability posts only when internal rigor is translated into external client value.

Translation rule:
- Start with the client-facing outcome, not the internal fix.
- Convert internal mechanics into one of these external value frames:
  - **Lower execution cost (10-15% saving)**
  - faster decision clarity
  - lower coordination risk
  - stronger design intent retention
  - smoother consultant/site handoff
  - higher confidence before capital is committed
- Anchor the point in a project reality, design principle, or market pattern the audience recognizes.

Allowed public framing:
- What disciplined process helps a client avoid.
- How better documentation improves execution quality.
- Why structured reviews protect design intent and delivery confidence.
- How capability depth reduces ambiguity across approvals, consultants, and site execution.

Keep out of public posts:
- approval churn
- packet mechanics
- internal normalization work
- publication workstream status
- internal backlog cleanup
- tool/process administration that has no direct client consequence

Drafting test:
- If the post reads like an internal team update, rewrite it.
- If the benefit lands on Vitan first and the client second, rewrite it.
- If the reader cannot tell why the process matters to project outcomes, rewrite it.

Before/after examples:
- Pattern from [VITA-270](/VITA/issues/VITA-270)
  - Before: "We tightened our approval workflow so review packets move with less internal churn."
  - After: "Clear review gates help clients compare options sooner, reduce late-stage ambiguity, and move toward confident project decisions."
- Pattern from [VITA-595](/VITA/issues/VITA-595)
  - Before: "We use high-rise transport optimization."
  - After: "Vitan's technical execution typically saves 10-15% on high-rise execution costs through optimized engineering integration."

## 7. Hashtag Strategy

### Core recurring

`#VitanArchitects #AddingLifeEverySqFt #Architecture #EfficiencyOfGrandeur #AhmedabadSkyscrapers`

Canonical branded hashtag rule:
- Use `#AddingLifeEverySqFt` as the only recurring branded hashtag form in captions, first comments, approval tickets, and review packets.
- Do not mix or substitute variants such as `#AddingLifeEverySquareFoot`.

### Rotating discovery sets

- Project proof: `#SkyscraperExecution #HighRiseArchitecture #AhmedabadSkyline`
- Premium segment: `#LuxuryVerticalLiving #DesignCredibility #VerticalUrbanism`
- Process insight: `#ProfitCentreDesign #ExecutionOptimization #BuiltResilience`

Rule:
- LinkedIn/Facebook: 4-6 total hashtags.
- Instagram caption: 2-3 hashtags max.
- Instagram first comment bundle: 6-10 hashtags total.
- If Instagram is published without a first-comment bundle, keep the caption within the 2-3 hashtag cap rather than moving to a 6-10 caption block.

## 8. Image Pipeline

1. Source from `JagPat/Vitan-BrandBuilding` repository assets first.
2. Match post pillar to project folder image set.
3. For Instagram API flow, convert selected asset into a public raw URL.
4. If no suitable asset, generate a branded social card and host it at a public URL.

## 9. Approval Workflow (Current)

- Draft content package per post: platform, caption, hashtags, CTA, image URL, publish window.
- Approval tickets are incomplete until they include all three required contract blocks below.
- Add mandatory `Feedback alignment` block in each approval request:
  - `Recent feedback reviewed`: list last up to 10 feedback ids or `none yet`.
  - `Applied in this draft`: concrete choices in tone, pillar, CTA, or hashtag use.
  - `Open conflicts`: any contradictory feedback pending Principle Architect decision.
- Add mandatory `Hashtag counts` block in each approval request:
  - `LinkedIn`: `<count>/6 max`
  - `Facebook`: `<count>/6 max`
  - `Instagram caption`: `<count>/3 max`
  - `Instagram first comment`: `<count>/10 max`
- Add mandatory one-line `Strategy compliance` statement in each approval request:
  - `Strategy compliance: hashtag limits verified + canonical #AddingLifeEverySqFt applied.`
- For process/capability posts, add a second one-line `Translation check` statement:
  - `Translation check: internal process language converted to client-facing outcome language.`
- Submit via Paperclip issue for Principle Architect approval before any external publishing.
- Publish only after explicit approval status is recorded.
- Review packets and approval HTML exports must preserve these blocks verbatim; if any block is missing, treat the item as draft-incomplete rather than review-ready.

## 10. Active Execution Signals (April 2026 Wave)

### DPM

- **Campaign:** "Ahmedabad's Rising Skyline"
- **Task:** Sequence posts to coincide with Stage 1 outreach send.
- **Messaging:** Highlight the "Profit Centre" model (10-15% execution savings).
- **Assets:** Use high-contrast monolithic shots of Parijaat Eclat and Privilon.

### BS

- **Theme:** "Execution Mastery in the 100m+ Segment."
- **Task:** Draft LinkedIn long-form article on "Vertical Logistics: Why Execution Matters for Skyscrapers."
- **Heritage:** Refresh case studies for Parijaat Eclat and Mondeal as Vitan's high-rise foundation.

### OC

- **Campaign:** "Landmark Recognition."
- **Award Priority:** CTBUH 2026, WAF 2026, India's Best Design Awards 2026.
- **Projects:** Shaligram Luxuria, Augusta, Safal Vihaan.
- **Blocker:** High-res photography is the critical path.

## 11. Publication Route Discipline

- Keep `ArchDaily` as the primary global publication lane when a project is ready for flagship external proof.
- Use `ArchitectureLive!` and `ArchiSHOTS` as the default India follow-on route once the flagship submission lane and supporting package are clear.
- Treat `Surfaces Reporter` as conditional rather than default; use it when the strongest story is material-led, detailing-led, or product-surface driven.
- Keep outlet priority separate from first-project selection. Do not assume that the oldest blocked publication thread should define the next pack.
- If the first-project choice is still unresolved, hold the execution choice until the comparison is explicit rather than letting the queue drift into a false default.

## 12. Reputation Review Sequencing

- The reputation workflow now follows this order:
  1. approved review-request copy variants
  2. trigger definitions for when the request is sent
  3. tracking fields for request status and response status
  4. testimonial intake format for reusable proof capture
  5. monthly `GBP` and `Houzz` monitoring
- Treat this sequence as canonical for reputation execution and reporting.
- DPM should align review-request planning to this order rather than treating reputation as an unstructured follow-up task.

## 13. Review-Only Strategy Inputs

- The Instagram guideline in [VITA-320](/VITA/issues/VITA-320) is still approval-stage only.
- Until the board explicitly approves that guideline, do not treat its weekly post mix or platform refinements as canonical strategy.
- Current canonical Instagram direction remains the simpler visual-first system already defined in this file.

## 14. Operational Learnings (From Live Runs)

- LinkedIn publish endpoint can return HTTP 201 with minimal response body.
- Facebook publish can fail with permission errors unless token role includes required page permissions.
- Instagram API flow fails without `image_url`; text-only assumption is invalid for the current endpoint path.
- Instagram publish can succeed using a public `raw.githubusercontent.com` image URL sourced from the brand repository.
- After Instagram publish, fetch `/{media_id}?fields=permalink` to capture proof URL in issue comments and reports.
- Social publisher now includes media URL preflight (`HTTP 2xx` plus `image/*`) and an approved fallback list of 3 Instagram-safe project image URLs to reduce interruption risk.
- Pillar-based caption templates are standardized in `Business development/social-publisher/templates/caption-templates.md` to reduce drafting latency.
- Keep technical blockers isolated in dedicated engineering issues for rapid unblock.
- X API can fail with `HTTP 402` / `CreditsDepleted` even when OAuth credentials are valid; treat as an account billing/plan blocker and escalate to Founding Engineer.
- After credits restoration, X publish retry succeeded with `externalPostId=2040064800764604691` (2026-04-03 UTC); keep the same retry path and attach URL proof in the issue thread.
- Board-confirmed unblock retry also succeeded with `externalPostId=2040070439972790297` (2026-04-03 UTC), confirming the end-to-end X publish path is stable when credits are available.

## 15. Weekly Kaizen Cadence

Every week:
1. Review post-level outcomes (reach, replies, inquiry actions).
2. Identify the top-performing pillar and the weak-performing pillar.
3. Adjust pillar weights by small increments (5-10%).
4. Rotate hashtag sets and compare discovery lift.
5. Record one process improvement in PARA memory and, if systemic, open a `[KAIZEN]` issue.

## 16. Board Feedback Loop (Capability Baseline)

Feedback issue protocol:
- Board/CEO opens an issue with prefix `[FEEDBACK]` and uses the template at `Business development/social-publisher/templates/board-feedback-issue-template.md`.
- Required fields: content reference, 1-5 rating, what worked, what to improve, strategic direction, priority.

Business Builder processing SLA:
1. Acknowledge the feedback issue in the same heartbeat.
2. Log the entry into PARA feedback memory:
   - `$AGENT_HOME/memory/feedback/index.yaml`
   - `$AGENT_HOME/memory/feedback/YYYY-MM-DD.yaml`
   - `$AGENT_HOME/memory/feedback/strategy-impact/changelog.yaml` when strategy changes are made
3. Apply concrete strategy adjustments to this file within 24 hours when applicable.
4. Create follow-on action issues when requested or implied by feedback.
5. Close the feedback issue with a summary of applied updates and any pending conflicts.

Feedback-aware creation rule:
- Before drafting any new content, read the last 10 entries in `$AGENT_HOME/memory/feedback/index.yaml` and incorporate them.
- If feedback is conflicting, flag it to Principle Architect before publishing.

## Sources Consulted

- [VITA-595](/VITA/issues/VITA-595) — Established the 'Efficiency of Grandeur' campaign theme and the 2026 Skyscraper Wave focus.
- [VITA-531](/VITA/issues/VITA-531) — Identified high-prestige skyscraper prospects in Ahmedabad.
- [VITA-727](/VITA/issues/VITA-727) — Monday standup confirming sub-team health and blocker status.
- [VITA-287](/VITA/issues/VITA-287) — required a repo-tracked canonical strategy file plus a dated strategy brief for the execution layer.
- [VITA-211](/VITA/issues/VITA-211) — confirmed the ArchDaily package remains blocked, so publication-led amplification cannot assume resolved source data.
- [VITA-226](/VITA/issues/VITA-226) — confirmed the Ahmedabad Racquet Academy metadata and permissions gap that must remain visible in strategy dependencies.
- [VITA-302](/VITA/issues/VITA-302) — established the explicit reputation-review sequencing that now belongs in canonical strategy.
- [VITA-320](/VITA/issues/VITA-320) — confirmed the Instagram guideline remains review-stage only and should not be merged into canonical strategy before approval.
- [VITA-325](/VITA/issues/VITA-325) — established the current publication-route order and the need to separate outlet priority from first-project selection.
- `Business development/shared-workspace/references/growth-os.md` — informed the cross-workstream role of strategy across scanning, positioning, and communication execution.
