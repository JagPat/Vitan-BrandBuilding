# Vitan Growth OS — Paperclip System Architecture

## Four Linked Workstreams

### WS1: Client Scanning & Relationship Management (BB primary, PA review)
- Research active developers/builders/institutional clients in Gujarat
- Track new project launches (RERA, press, site activity)
- For each contact: their projects, challenges, growth plans, current architects
- Enrich via Hunter.io, score by sector match + growth trajectory
- Outputs: enriched contacts-master.csv, prospect briefs, weekly scanning summary

### WS2: Competition & Positioning Intelligence (BB research, PA analysis)
- Map top 10-15 competing architecture firms by sector
- Track: recent projects, awards, strengths/weaknesses, key clients
- PA synthesizes positioning: where Vitan wins, where differentiation needed
- BB uses positioning to tailor outreach vs specific competitors
- Outputs: competitor profiles, positioning matrix

### WS3: Domain & Market Expansion (PA primary, HR capability input)
- Track Gujarat real estate trends, government programs, emerging project types
- Evaluate new domains: market size, capability overlap, competitive intensity, entry strategy
- HR assesses team readiness, skill gaps, hiring needs
- Geographic expansion: Gandhinagar, Surat, Vadodara, Rajkot
- Outputs: market opportunity briefs, expansion recommendations, capability gap reports

### WS4: Communication & Brand Execution (BB executes, PA approves)
- Follow 7-stage engagement journey (see engagement-system.md)
- Every outreach reflects intelligence from WS1-WS3
- Brand consistency: colors, typography, logo, voice, project photography
- Content types: emails, PDFs, portfolios, meeting briefs, proposals
- Outputs: all content in shared-workspace/review/vita{NNN}/

## Agent Roles

### PA → Growth Strategist
- Synthesize intelligence from all workstreams
- Set monthly/quarterly growth priorities
- Approve outreach plans, evaluate expansion opportunities
- Coordinate cross-agent work

### BB → Growth Engine  
- Client scanning, competitive research, communication execution
- Build client intelligence profiles
- Execute multi-stage engagement journeys
- Report market signals to PA

### HR → People & Capability Intelligence
- Assess team readiness for expansion opportunities
- Track skills gaps and hiring needs
- Monitor agent operational health

### FE → Platform & Intelligence Tooling
- Maintain content generation scripts (create_email.py, create_pdf.py)
- Fix infrastructure (git push, deployments)
- Build monitoring/reporting tools

## Cross-Agent Coordination

Weekly Intelligence Cycle:
1. BB scans prospects, updates intelligence, researches competitors
2. BB commits findings to shared-workspace
3. PA reviews, synthesizes positioning guidance
4. PA sets outreach priorities
5. BB executes outreach
6. Board reviews/sends, logs responses
7. BB monitors follow-up triggers → loop

Escalation: BB→PA (high-value prospects, competitive threats), PA→HR (capability assessment), PA→BB (priority changes), Any→FE (infrastructure)

## Shared Data
- shared-workspace/contacts-master.csv — contact database
- shared-workspace/review/vita{NNN}/ — working artifacts
- shared-workspace/approved/vita{NNN}/ — board-approved
- shared-workspace/intelligence/ — competitive/market data
- shared-workspace/references/ — system docs (this file, engagement-system.md)

## Success Metrics
1. Intelligence breadth: prospects with full profiles
2. Competitive awareness: positioning matrix completeness
3. Pipeline depth: contacts at each stage
4. Conversion: outreach→meetings→proposals→wins
5. Expansion readiness: domains evaluated by PA
6. Agent utilization: all 4 contributing to growth