# SOCIAL_STRATEGY

Last updated: 2026-04-05 (UTC, VITA-273 process-led thought-leadership translation rules)
Owner: Business Builder

## 1. Objectives

- Grow qualified awareness for Vitan Architects across LinkedIn, Facebook, Instagram, and X.
- Convert social attention into tracked inquiry actions through `connect@vitan.in`.
- Build repeatable proof-first storytelling around Vitan projects and design philosophy.

## 2. Core Brand Voice

- Human impact first: spaces as lived experience, not visual spectacle alone.
- Calm authority: practical, confident, specific.
- Execution credibility: design quality + delivery discipline.

## 3. Content Pillars (Current Weights)

- Project proof and case snapshots: 35%
- Founder perspective / philosophy: 25%
- Process and execution insights: 20%
- Capability and firm proof points: 15%
- Market commentary and trend POV: 5%

## 4. Platform Guidelines

### LinkedIn

- Primary business narrative channel.
- Format: 1-2 short paragraphs, strong opening line, one clear CTA.
- Best use: project proof, founder POV, developer-facing insights.

### Facebook

- Community reinforcement and reach extension.
- Format: concise caption + visual proof; stronger local relevance.
- Best use: project highlights, milestones, branded stats.

### Instagram

- Visual-first storytelling channel.
- Format: image-led post + concise caption + focused hashtags.
- Non-negotiable: publish flow requires publicly accessible `image_url` for API-based posting.

### X

- Secondary channel; currently lower priority until token/credits are stable.
- Publish readiness gate: verify X API account credits/plan before execution to avoid `402 CreditsDepleted` runtime failures.

## 5. Process-Led Thought Leadership Rules

Use process/capability posts only when internal rigor is translated into external client value.

Translation rule:
- Start with the client-facing outcome, not the internal fix.
- Convert internal mechanics into one of these external value frames:
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
- Pattern from [VITA-271](/VITA/issues/VITA-271)
  - Before: "We are improving documentation discipline across our publication workflow."
  - After: "Documentation discipline protects design intent from concept to construction by reducing ambiguity across consultants, approvals, and on-site execution."

## 6. Hashtag Strategy

### Core recurring
`#VitanArchitects #AddingLifeEverySqFt #Architecture #DesignThinking`

Canonical branded hashtag rule:
- Use `#AddingLifeEverySqFt` as the only recurring branded hashtag form in captions, first comments, approval tickets, and review packets.
- Do not mix or substitute variants such as `#AddingLifeEverySquareFoot`.

### Rotating discovery sets
- Project proof: `#ProjectHighlight #BuiltEnvironment #ArchitectureIndia`
- Premium segment: `#LuxuryDesign #UrbanDevelopment #DesignQuality`
- Process insight: `#DesignProcess #ProjectDelivery #BuiltForm`

Rule:
- LinkedIn/Facebook: 4-6 total hashtags.
- Instagram caption: 2-3 hashtags max.
- Instagram first comment bundle: 6-10 hashtags total.
- If Instagram is published without a first-comment bundle, keep the caption within the 2-3 hashtag cap rather than moving to a 6-10 caption block.

## 7. Image Pipeline

1. Source from `JagPat/Vitan-BrandBuilding` repository assets first.
2. Match post pillar to project folder image set.
3. For Instagram API flow, convert selected asset into a public raw URL.
4. If no suitable asset, generate a branded social card and host at public URL.

## 8. Approval Workflow (Current)

- Draft content package per post: platform, caption, hashtags, CTA, image URL, publish window.
- Approval tickets are incomplete until they include all three required contract blocks below:
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
- Review packets and approval HTML exports must preserve these blocks verbatim; if any block is missing, the item should be treated as draft-incomplete rather than review-ready.

## 9. Operational Learnings (From Live Runs)

- LinkedIn publish endpoint can return HTTP 201 with minimal response body.
- Facebook publish can fail with permission errors unless token role includes required page permissions.
- Instagram API flow fails without `image_url`; text-only assumption is invalid for current endpoint path.
- Instagram publish can succeed using a public `raw.githubusercontent.com` image URL sourced from the brand repository.
- After Instagram publish, fetch `/{media_id}?fields=permalink` to capture proof URL in issue comments and reports.
- Social publisher now includes media URL preflight (`HTTP 2xx` + `image/*`) and an approved fallback list of 3 Instagram-safe project image URLs to reduce interruption risk.
- Pillar-based caption templates are now standardized in `Business development/social-publisher/templates/caption-templates.md` to reduce drafting latency.
- Keep technical blockers isolated in dedicated engineering issues for rapid unblock.
- X API can fail with `HTTP 402` / `CreditsDepleted` even when OAuth credentials are valid; treat as account billing/plan blocker and escalate to Founding Engineer.
- After credits restoration, X publish retry succeeded with `externalPostId=2040064800764604691` (2026-04-03 UTC); keep the same retry path and attach URL proof in the issue thread.
- Board-confirmed unblock retry also succeeded with `externalPostId=2040070439972790297` (2026-04-03 UTC), confirming end-to-end X publish path is stable when credits are available.

## 10. Weekly Kaizen Cadence

Every week:
1. Review post-level outcomes (reach, replies, inquiry actions).
2. Identify top-performing pillar and weak-performing pillar.
3. Adjust pillar weights by small increments (5-10%).
4. Rotate hashtag sets and compare discovery lift.
5. Record one process improvement in PARA memory and, if systemic, open a `[KAIZEN]` issue.

## 11. Board Feedback Loop (Capability Baseline)

Feedback issue protocol:
- Board/CEO opens issue with prefix `[FEEDBACK]` and uses template at `Business development/social-publisher/templates/board-feedback-issue-template.md`.
- Required fields: content reference, 1-5 rating, what worked, what to improve, strategic direction, priority.

Business Builder processing SLA:
1. Acknowledge feedback issue in same heartbeat.
2. Log entry into PARA feedback memory:
   - `$AGENT_HOME/memory/feedback/index.yaml`
   - `$AGENT_HOME/memory/feedback/YYYY-MM-DD.yaml`
   - `$AGENT_HOME/memory/feedback/strategy-impact/changelog.yaml` when strategy changes are made.
3. Apply concrete strategy adjustments to this file within 24 hours when applicable.
4. Create follow-on action issues when requested or implied by feedback.
5. Close feedback issue with summary of applied updates and any pending conflicts.

Feedback-aware creation rule:
- Before drafting any new content, read last 10 entries in `$AGENT_HOME/memory/feedback/index.yaml` and incorporate them.
- If feedback is conflicting, flag to Principle Architect before publishing.
