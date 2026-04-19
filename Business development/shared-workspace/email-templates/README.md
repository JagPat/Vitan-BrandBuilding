# Email Templates — Vitan Growth OS

Two distinct email types exist in the system. Use the correct template for each.

---

## Type 1 — Outreach Emails (external, to prospects)

**Generator:** `scripts/generate_branded_email.py`

Full-width branded HTML with dark header, hero image, project snapshot, and CTA button. Generated per-contact from `contacts-master.csv`. Always requires board approval before sending.

**When to use:** Any external communication to prospects, developers, or partners.

---

## Type 2 — System Emails (operational, to board)

Sender: `growthos@vitan.in`  
Recipients: `board@vitan.in`, `jp@vitan.in`, `kaivana@vitan.in`, `chitrang@vitan.in`

### Templates

| File | Use case | Severity colors |
|---|---|---|
| `action-required.html` | Stale blocker alerts, escalations | High: `#D42B2B` / Critical: `#8B0000` |
| `board-digest.html` | Weekly/daily pipeline summaries, Monday standups | — (uses red accent `#D42B2B`) |

### Variables (replace `{{TOKEN}}` before sending)

**action-required.html**
- `{{DATE}}` — e.g. "19 Apr 2026"
- `{{SUBJECT}}` — one-line summary
- `{{SEVERITY_COLOR}}` — `#D42B2B` (High) or `#8B0000` (Critical)
- `{{SEVERITY_LABEL}}` — `HIGH` or `CRITICAL`
- `{{BODY_INTRO}}` — opening paragraph explaining the situation
- `{{ISSUE_ID}}` — e.g. `VITA-476`
- `{{LAST_ACTIVITY}}` — ISO timestamp or human-readable
- `{{SILENCE_DURATION}}` — e.g. "28 hours"
- `{{OWNING_AGENT}}` — e.g. "DPM"
- `{{BODY_ACTION}}` — what the board needs to do

**board-digest.html**
- `{{DATE}}` — e.g. "19 Apr 2026"
- `{{DIGEST_TITLE}}` — e.g. "Weekly Digest · w/c 14–20 Apr"
- `{{PERIOD}}` — date range covered
- `{{HIGHLIGHTS}}` — bullet list HTML or plain text
- `{{PIPELINE_ITEMS}}` — active issues / campaigns
- `{{ATTENTION_ITEMS}}` — blockers needing board action
- `{{NEXT_ACTIONS}}` — what PA / agents will do next

---

## Brand Reference

| Token | Value |
|---|---|
| Primary red | `#D42B2B` |
| Dark | `#1A1A1A` |
| Gray | `#4A4A4A` |
| Light bg | `#F5F5F3` |
| Warm off-white | `#F8F6F1` |
| Font | Arial, sans-serif |
| Tagline | "Adding life, every square foot" |
| Sender address | `growthos@vitan.in` (system) / `connect@vitan.in` (outreach) |
