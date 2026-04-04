# Unified Publishing & Storytelling Protocol — Vitan Growth OS

## Purpose

Every piece of content Vitan publishes — an email, a LinkedIn post, an Instagram image, a tweet — is a chapter in the same story. A prospect who sees a LinkedIn post, then receives an email, then checks Instagram should experience a coherent narrative that builds on itself. This protocol ensures that happens systematically.

## The Story Architecture

### One Story, Four Expressions

Every campaign starts from a single **Campaign Brief**, then adapts to each platform:

```
Campaign Brief (the STORY)
  ├── Email → The personal, direct version (1-to-1 relationship)
  ├── LinkedIn → The professional credibility version (industry peers)
  ├── Instagram → The visual/emotional version (aspirational audience)
  └── X (Twitter) → The sharp, quotable version (broad reach)
```

These are NOT four separate pieces of content. They are four windows into the same idea.

### Campaign Brief Template

Every campaign starts here. No content gets produced without this being filled:

```
Campaign ID: [auto-generated, e.g., CAMP-2026-04-001]
Theme: [One line, e.g., "The Profit Centre Architect"]
Core Message: [The single idea, e.g., "Good architecture saves more than it costs"]
Target Audience: [Who this speaks to]
Emotional Register: [How it should feel: authoritative / warm / aspirational / urgent]
Value Proposition Tie: [How this connects to Vitan's 10-15% savings message]
Sensitivity Check: [Any contacts/companies to be careful about? Check sensitivity-protocol.md]
Call to Action: [What do we want people to DO after seeing this?]
Campaign Duration: [Start date → end date]
Cross-Platform Hooks: [How does each platform point to the others?]
```

## Platform Playbooks

### Email (BB Agent — connects to engagement-system.md)

**Role in story**: The personal invitation. The email is where the story becomes about THEM.

**Rules**:
- Subject line must echo the campaign theme but feel personal, not broadcast
- Opening paragraph: about THEM (their project, their challenge, their market)
- Middle: the campaign's core message, framed as relevant to their situation
- Close: specific CTA (meeting, call, studio visit)
- Sensitivity guardrails from contacts-master MUST be applied
- Email goes through engagement-system.md stage workflow (draft → review → board sends)

**Connection to other platforms**: Email can reference "as we shared recently on LinkedIn" or include a project image that's also on Instagram. This makes the story feel alive, not siloed.

### LinkedIn (HR Agent)

**Role in story**: The professional proof. LinkedIn is where Vitan establishes authority.

**Format rules**:
- Hook in first 2 lines (this is what shows before "see more")
- 150-300 words maximum
- One insight, one proof point, one question
- End with engagement prompt (question or invitation to comment)
- Use 3-5 relevant hashtags (not more)
- Include project photo or design visual when possible

**Content types that work**:
1. **Project Insight**: "On [project], we saved X% by doing Y" — proof of value proposition
2. **Industry Observation**: "Gujarat's residential market is shifting toward Z" — thought leadership
3. **Behind the Design**: Process photo + what the design decision achieved — shows craft
4. **Client Win** (with permission): Testimonial or project milestone — social proof

**Connection to other platforms**: LinkedIn post drops within 24 hours of email outreach to the same sector. Prospects who receive the email then see the LinkedIn post — reinforcement without repetition.

### Instagram (HR Agent)

**Role in story**: The visual aspiration. Instagram is where Vitan makes people FEEL what good architecture looks like.

**Format rules**:
- Lead with the strongest visual (project photo, render, detail shot)
- Caption: short story (2-3 sentences) + the campaign message woven in naturally
- Use brand colors in any graphics (#D42B2B, #1A1A1A)
- Include tagline "Adding life, every square foot" in graphic overlays
- Stories for behind-the-scenes; Posts for polished output
- Reels for walkthroughs or time-lapses (when available)

**Content types that work**:
1. **Before/After**: Transformation shots showing Vitan's impact
2. **Detail Shots**: Close-ups that show quality and craft
3. **Site Progress**: Construction-to-completion journey
4. **Design Process**: Sketches → renders → reality
5. **The Space in Use**: People enjoying the completed project — "adding life"

**Connection to other platforms**: Instagram visual becomes the hero image in the email. Same photo appears in LinkedIn post with a different (professional) framing. Cross-pollination, not duplication.

### X / Twitter (HR Agent)

**Role in story**: The sharp take. X is where Vitan's point of view reaches beyond the immediate network.

**Format rules**:
- Under 200 characters for maximum impact
- One idea per tweet
- Thread for deeper insights (max 4 tweets)
- Quote or retweet industry news with Vitan's perspective added
- Use campaign hashtag if created

**Content types that work**:
1. **Stat + Insight**: "10-15% execution savings. That's what design-stage optimization delivers. Architecture isn't a cost — it's an investment that pays for itself."
2. **Contrarian Take**: Challenge common assumptions about architecture/construction
3. **Quick Wins**: Bite-sized tips from Vitan's experience
4. **Industry Commentary**: Vitan's view on market trends

**Connection to other platforms**: Tweet distills the LinkedIn post to its sharpest point. Links back to LinkedIn for the full version or to Instagram for the visual.

## The Publishing Calendar

### Weekly Rhythm

```
Monday:    Campaign Brief approved → content production starts
Tuesday:   Email drafts ready for board review (in shared-workspace/review/)
Wednesday: LinkedIn + Instagram + X drafts ready for board review
Thursday:  Board approves/edits → emails sent (board via Zoho)
Friday:    Social posts published (board or scheduled)
```

### Coordination Rules

1. **Email goes first** (Thursday). Social follows (Friday). This way, the prospect sees the personal message before the public one.
2. **Same visual thread**: The project photo in the email appears (differently cropped/framed) on Instagram and LinkedIn within 48 hours.
3. **Message escalation**: Email is specific and personal → LinkedIn is professional and credible → Instagram is visual and aspirational → X is sharp and memorable. Same story, escalating emotional registers.
4. **No platform contradicts another**. If the email says "we save 10-15%", the LinkedIn post can't say "we save 20%". Consistency is trust.

## Content Production Workflow

### Step 1: Campaign Brief (PA Agent proposes, Board approves)
- PA identifies campaign theme from Growth OS workstream progress
- Brief created in shared-workspace/review/camp-{id}/campaign-brief.md
- Board reviews and approves

### Step 2: Content Drafting (BB for emails, HR for social)
- BB drafts emails per engagement-system.md, applying sensitivity guardrails
- HR drafts LinkedIn, Instagram, X posts using brand guide
- All drafts placed in shared-workspace/review/camp-{id}/
- Each draft includes: platform, post text, visual reference, hashtags, CTA, scheduled time

### Step 3: Board Review
- Board reviews all drafts in one batch (not piecemeal)
- Board edits/approves via issue comments
- Approved drafts moved to shared-workspace/approved/camp-{id}/

### Step 4: Publishing
- Emails: Board sends via Zoho Mail
- Social: Board publishes or schedules (agents prepare final copy + images)
- BB updates contacts-master.csv (Last Contacted, Response Status)
- HR logs social post metrics when available

### Step 5: Feedback Loop
- Track: email opens/replies, social engagement, profile visits
- Feed results back into next campaign brief
- Update sensitivity-protocol.md if any response reveals new dynamics
- Winning content patterns get documented in this protocol's Learned Patterns section

## Brand Consistency Checklist

Before ANY content goes to board review:

- [ ] Uses Vitan voice (authoritative but warm, never salesy)
- [ ] Includes value proposition (10-15% savings / profit centre framing)
- [ ] Uses brand colors in any graphics (#D42B2B primary, #1A1A1A text)
- [ ] Includes tagline where appropriate ("Adding life, every square foot")
- [ ] Sensitivity guardrails checked for any named/implied contacts
- [ ] Cross-platform consistency verified (no contradictions between posts)
- [ ] CTA is clear and platform-appropriate
- [ ] Visual is high quality and from approved project photos

## Learned Patterns (Living Section — Agents Add Here)

### Pattern: VALUE-FIRST MESSAGING
- **Observation**: "We save you money" lands better than "hire us"
- **Rule**: Every piece of content must lead with client benefit, not Vitan capability
- **Applies to**: All platforms

---

## Agent Responsibilities

| Platform | Primary Agent | Backup Agent | Board Role |
|----------|--------------|--------------|------------|
| Email drafts | BB | PA | Sends via Zoho, provides relationship context |
| LinkedIn | HR | BB | Approves, publishes |
| Instagram | HR | FE (visuals) | Approves, publishes |
| X / Twitter | HR | BB | Approves, publishes |
| Campaign Brief | PA | BB | Approves theme and direction |
| Visual assets | FE | HR | Provides project photos |
| Analytics | PA | HR | Reviews, feeds into next cycle |
