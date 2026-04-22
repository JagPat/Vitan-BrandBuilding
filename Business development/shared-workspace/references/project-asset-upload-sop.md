# Project Asset Upload SOP

Owner: Principle Architect (PA)
Version: 1.0 | Effective: 2026-04-22
KAIZEN origin: [VITA-764](/VITA/issues/VITA-764)

---

## Purpose

This SOP eliminates recurring blockers where award submissions, editorial briefs, and portal entries stall because agents cannot find project photos or technical drawings. It defines where assets live, what quality standards apply, and how gaps are surfaced proactively rather than discovered at deadline.

---

## 1. Standard Asset Paths

All project assets in WorkDrive and the git repo follow these conventions:

### Photos
```
Business development/PHOTOS FOR SAMPLE PROJECT/{project-slug}/
```

Naming convention: `{project-slug}_{view-type}_{sequence}.jpg`  
Examples:
- `palladium_exterior_01.jpg`
- `privilon_lobby_02.jpg`
- `seventy_aerial_01.jpg`

### Technical Drawings
```
Business development/shared-workspace/assets/drawings/{project-slug}/
```

Naming convention: `{project-slug}_{drawing-type}_{scale}.pdf`  
Examples:
- `palladium_floor-plan_1-100.pdf`
- `privilon_elevation_1-200.pdf`

### Asset Index File (per project)
Each project folder must contain an `ASSET_CHECKLIST.md` (see Section 5 — Template).

---

## 2. Minimum Quality Standards by Submission Type

| Submission Type | Photos | Drawings | Notes |
|---|---|---|---|
| Awards (WAF, IBDA, IIA, CTBUH) | Min 5 MP, 300 DPI, JPG or TIF | PDF vector or raster ≥150 DPI | Check portal spec — some require TIFF |
| Editorial / ArchDaily | Min 8 MP, 300 DPI, JPG | Not required (optional) | Watermark-free |
| Speaking ops (CEPT, conferences) | Min 3 MP, 72 DPI for slides | CAD export or PDF | Presentation-ready |
| Portal (own website/Google) | Min 2 MP, 72–150 DPI | Not required | WebP acceptable |

---

## 3. Asset Gap Signal Protocol

Agents must **not block immediately** when assets are missing. Follow this escalation ladder:

### Level 1 — Asset Check (T-30 days before deadline)
- BS/OC checks the project folder and ASSET_CHECKLIST.md
- If assets are complete: proceed to submission prep
- If assets are incomplete: post an **asset gap comment** on the submission issue tagging PA

### Level 2 — PA Asset Probe (T-21 days)
- PA creates a `[ASSET REQUEST]` task assigned to the board (user, not agent)
- Task description lists: project name, submission, specific missing files, deadline
- Include direct WorkDrive upload link if available

### Level 3 — Action Required Email (T-14 days)
- If no board response to Level 2 task within 7 days, PA sends an Action Required email
- Template: `email-templates/action-required.html` with severity=Medium
- Subject: `[ASSET REQUEST] {project} — {submission} deadline {date}`

### Level 4 — File with available assets (T-3 days)
- If still no assets, OC/BS proceeds with what is available
- Adds a note in the submission: "Additional documentation to follow"
- PA logs in BOARD_FEEDBACK.md: date, submission, missing assets, board response status

**Rule:** Never let an agent stay `blocked` more than 7 days on a missing-asset task without escalating to Level 3.

---

## 4. Proactive Deadline Monitoring

PA includes an **asset readiness check** in the Monday BB standup digest for any submission with a deadline within 60 days:

```
## Asset Readiness — Upcoming Submissions
| Submission | Deadline | Projects | Asset Status |
|---|---|---|---|
| IIA Ascension | 2026-04-30 | TBD | ⚠️ Missing floor plan |
| ArchDaily BOTY | 2026-12-01 | TBD | ✅ Ready |
```

FE is requested to implement a **pre-deadline routine** (separate [FE_REQUEST] to be filed) that:
- Runs monthly (1st of each month)
- Reads `contacts-master.csv` or a `submission-calendar.md` for known deadlines
- For each deadline within 60 days: checks that the project folder exists and has ≥3 photos
- Posts a summary to the current BB standup issue

---

## 5. ASSET_CHECKLIST.md Template

Create this file at `Business development/PHOTOS FOR SAMPLE PROJECT/{project-slug}/ASSET_CHECKLIST.md`:

```markdown
# Asset Checklist — {Project Name}

Project slug: {project-slug}
Last updated: YYYY-MM-DD
Updated by: {agent or board}

## Photos
- [ ] Exterior hero (min 5 MP, 300 DPI)
- [ ] Exterior approach / street level
- [ ] Main interior (lobby or primary space)
- [ ] Secondary interior (2–3 additional)
- [ ] Aerial / contextual (if available)
- [ ] Night view (if applicable)
- [ ] Construction sequence (if applicable)

## Drawings
- [ ] Site plan (PDF, ≥150 DPI)
- [ ] Ground floor plan (PDF, ≥150 DPI)
- [ ] Typical floor plan (PDF, ≥150 DPI)
- [ ] Key elevation (PDF, ≥150 DPI)
- [ ] Section (PDF, ≥150 DPI)

## Awards-specific
- [ ] Board narrative (50–100 words, jargon-free)
- [ ] Project metadata complete (area sqm, year, client, team)
- [ ] Signed authorisation (if required by award body)

## Status
- Ready for: [ ] Awards [ ] Editorial [ ] Speaking [ ] Portal
- Blockers: {describe any}
- Requested from board: {date of last request}
```

---

## 6. Known Asset Gaps (Active)

As of 2026-04-22:

| Project | Issue | Missing | Deadline |
|---|---|---|---|
| Palladium | [VITA-571](/VITA/issues/VITA-571) | Technical drawings + hi-res photos | TBD |
| Privilon | [VITA-572](/VITA/issues/VITA-572) | Technical drawings | TBD |
| Seventy | [VITA-573](/VITA/issues/VITA-573) | Technical drawings | TBD |
| Ahmedabad Racquet Academy | [VITA-233](/VITA/issues/VITA-233) | Metadata + drawing export | Critical |
| IIA Ascension | [VITA-739](/VITA/issues/VITA-739) | IIA Membership Number (board input) | 2026-04-30 |

---

## 7. Ownership

| Role | Responsibility |
|---|---|
| Board | Upload actual photos and drawings to WorkDrive |
| FE | Implement pre-deadline routine; maintain path conventions in git |
| BS/OC | Signal gaps early (Level 1); never block silently |
| PA | Level 2+ escalation; include readiness check in Monday standup |
| HR | Document this SOP in team protocols; onboard new agents to it |
