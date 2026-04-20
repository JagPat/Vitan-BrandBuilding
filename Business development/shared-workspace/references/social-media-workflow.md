# Weekly Social Media Workflow — Vitan Growth OS

## Purpose

This document defines the automated weekly workflow that generates, reviews, publishes, and monitors Vitan's social media content across all platforms. The workflow runs every Thursday evening, preparing the complete content plan for the following week and emailing it to the board for approval before anything gets published.

## Workflow Owner

**Primary**: Digital Presence Manager (DP) agent — `agent/dp` branch
**Supporting**: HR agent (social copy), BB agent (email alignment), FE agent (visual assets), PA agent (strategy oversight)

## Platforms Covered

| Platform | Content Type | Weekly Volume | Primary Day |
|----------|-------------|---------------|-------------|
| LinkedIn | Professional credibility, thought leadership | 3 posts | Mon/Wed/Fri |
| Instagram | Visual aspiration, project showcase | 3 posts + 5 stories | Thu/Fri |
| Facebook | Community engagement, project albums | 3 posts | Thu/Fri |
| X/Twitter | Sharp takes, industry commentary | 5 tweets | Daily |
| Pinterest | Project photo pins | 3-5 pins | Fri |
| YouTube | Project videos (monthly) | 1/month | Monthly |

## Weekly Rhythm

```
THURSDAY 7 PM (automated):
  → Paperclip generates next week's full content plan
  → Self-assessment of content quality
  → Email sent to board: jagrutpatel@gmail.com, CC: chitrang@vitan.in, kaivana@vitan.in
  → Plan committed to agent/dp branch, PR created to main

FRIDAY–SUNDAY (board):
  → Board reviews plan
  → Replies: APPROVED / APPROVED WITH CHANGES / HOLD
  → Provides requested content (photos, quotes, approvals)

MONDAY:
  → Campaign Brief finalized based on board feedback
  → Email + LinkedIn + Facebook drafts finalized

TUESDAY:
  → Instagram + X + Pinterest drafts finalized
  → Visual assets prepared

WEDNESDAY:
  → Final edits and visual polish

THURSDAY:
  → Outreach emails sent (if applicable)
  → LinkedIn + Facebook posts published

FRIDAY:
  → Instagram + X + Pinterest posts published
  → Week performance tracking begins
```

## Content Plan Structure

Every weekly plan includes:

### Per-Post Specification
- Campaign ID (CAMP-YYYY-WW-NNN)
- Theme and purpose
- Full copy draft (platform-appropriate)
- Visual composition brief (template type, project reference, layout, AI generation notes)
- Story/Reel concepts (Instagram/Facebook)
- Publishing schedule with exact times
- Cross-platform hooks
- Brand consistency checklist

### Board Requests
- Content needed (photos, testimonials, quotes)
- Decisions needed (theme approval, sensitivity flags)
- Asset requests (new photography, video)

### Performance Review
- Previous week's metrics by platform
- Week-over-week trends
- Best/worst performing content
- Next week's KPI targets

### Self-Assessment
- Capability scorecard (8 dimensions, rated 1-10)
- Gaps identified with concrete improvement plans
- Honesty check questions
- Overall verdict: TRUSTWORTHY / NEEDS IMPROVEMENT / NOT READY

## File Locations

| What | Where |
|------|-------|
| Weekly content plans | `shared-workspace/review/social-plans/week-YYYY-WW-content-plan.md` |
| Performance reports | `shared-workspace/review/social-plans/week-YYYY-WW-performance.md` |
| Approved content | `shared-workspace/approved/social-plans/` |
| Visual templates | `Brand Guide/social-card-template.html` |
| Publishing protocol | `shared-workspace/references/publishing-protocol.md` |
| Brand ecosystem | `shared-workspace/references/brand-ecosystem.md` |

## Email Configuration

- **Zoho Mail Account**: 3228151000000002002
- **From**: growthos@vitan.in
- **To**: jp@vitan.in
- **CC**: chitrang@vitan.in, kaivana@vitan.in
- **Subject format**: "Vitan Social Media Plan — Week of [Date Range] — Ready for Review"

## Board Approval Protocol

The board can reply to the weekly plan email with:

1. **APPROVED** — Content published as planned per the weekly rhythm
2. **APPROVED WITH CHANGES** — Board lists specific edits; DP agent incorporates and proceeds
3. **HOLD** — No publishing; board schedules discussion

If no response by Monday 12 PM, a reminder is sent. If no response by Tuesday 12 PM, the plan is held (no publishing without explicit approval).

## Performance Monitoring

### Metrics Tracked
- **Reach/Impressions**: How many people saw the content
- **Engagement rate**: Likes, comments, shares, saves as % of reach
- **Profile visits**: Traffic driven to Vitan's profiles
- **Website clicks**: Traffic driven to vitan.in
- **Follower growth**: Net new followers per platform
- **Lead attribution**: Inquiries/contacts that came through social

### Monitoring Cadence
- **Mid-week (Wednesday)**: Quick check on published content performance
- **End of week (Friday)**: Full performance data collection
- **Thursday plan**: Previous week's full performance review included in next plan

### Learned Patterns
When content significantly over- or under-performs, the pattern is documented in `publishing-protocol.md` under the Learned Patterns section, feeding continuous improvement.

## Paperclip Capability Assessment

The self-assessment serves three purposes:

1. **Transparency**: The board knows exactly where AI-generated content is strong and where it's weak
2. **Improvement tracking**: Week-over-week scores show whether the system is getting better
3. **Trust calibration**: Helps the board decide how much human review each piece needs

### Assessment Dimensions
1. Content Strategy — Are themes strategic and timely?
2. Copywriting Quality — Is the copy genuinely compelling?
3. Visual Composition — Are visual briefs specific and professional?
4. Brand Consistency — Does every piece feel like Vitan?
5. Platform Fluency — Does content feel native to each platform?
6. Audience Insight — Do we understand what the audience responds to?
7. Competitive Edge — Would this stand out against competitor firms?
8. Overall Trustworthiness — Can the board trust this to represent the firm?

### Improvement Triggers
- Score drops below 5 on any dimension → flag for board discussion
- Overall score below 6 → recommend human content strategist review
- Same gap persists 3+ weeks → escalate to PA agent for strategy intervention
- Score consistently above 8 → consider reducing board review scope

---

## Scheduled Task Reference

- **Task ID**: `weekly-social-media-plan`
- **Schedule**: Every Thursday at 7:00 PM IST
- **Notifications**: Enabled (board session notified on completion)
- **Managed in**: Claude Cowork → Scheduled Tasks
