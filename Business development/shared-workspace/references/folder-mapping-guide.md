# Vitan Growth OS — Folder Mapping Guide
_Last updated: 2026-04-20 | Author: PA (VITA-780)_

This guide tells the board exactly where to upload files — in Zoho WorkDrive — and
shows how those folders correspond to paths in the GitHub repository.

---

## How the sync works

```
Zoho WorkDrive  ←→  GitHub (Vitan-BrandBuilding)
```

Files placed in mapped Zoho WorkDrive folders automatically sync to GitHub within
~15 minutes (via GitHub Actions). Files written to GitHub by the agents also sync
back to WorkDrive. **You only need to interact with Zoho WorkDrive** — the GitHub
side is managed by the system.

---

## Folder Map: Zoho WorkDrive → GitHub

| Zoho WorkDrive folder | GitHub path | What belongs here |
|---|---|---|
| **Competitor Research** | `Business development/shared-workspace/review/vita191/` | Competitor profiles, positioning matrix |
| **Market Analysis** | `Business development/shared-workspace/review/vita192/` | Market opportunity briefs, expansion research |
| **Outreach Drafts** | `Business development/shared-workspace/review/vita193/` | Email drafts, outreach letters in progress |
| **Content Calendar** | `Business development/shared-workspace/change-notes/` | Social posts, scheduled content |
| **Growth OS Playbook** | `Business development/shared-workspace/references/` | System docs (this file, engagement system, etc.) |
| **Contacts** | `Business development/shared-workspace/contacts-master.csv` | Master contact/prospect list |
| **Brand Guidelines** | `Business development/Brand Guide/` | Logo files, colour palettes, typography rules |
| **Board Review** | `Growth OS/Board Review/` | Board digests, PA strategy notes |
| **ARA** | `Business development/PHOTOS FOR SAMPLE PROJECT/ARA/` | ARA project photos |
| **MERLIN** | `Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN/` | Merlin project photos |
| **PALLADIUM** | `Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/` | Palladium project photos |
| **PARIJAAT** | `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT/` | Parijaat project photos |
| **PRIVILON** | `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/` | Privilon project photos |
| **RETHAL** | `Business development/PHOTOS FOR SAMPLE PROJECT/RETHAL/` | Rethal project photos |
| **SAFAL PARISAR** | `Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PARISAR/` | Safal Parisar photos |
| **SAFAL PEGASUS** | `Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PEGASUS/` | Safal Pegasus photos |
| **SEVENTY** | `Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY/` | Seventy project photos |

---

## Where to upload images

**Always upload images to Zoho WorkDrive, not directly to GitHub.**

1. Go to **Zoho WorkDrive → Vitan Growth OS team → [project folder]**
2. Drop the image files into the correct project folder (see table above)
3. The sync runs automatically — files appear in GitHub within ~15 minutes

**For new projects not yet listed above:** Create a Paperclip issue to request a new
folder mapping. FE will add the folder to the sync configuration.

---

## Known naming issues (action required — FE)

The GitHub repo currently has duplicate photo folders that are **not** synced to
WorkDrive. Files placed in these folders will not transfer:

| GitHub folder (NOT synced) | Use this folder instead |
|---|---|
| `PHOTOS FOR SAMPLE PROJECT/ARA (AHMEDABAD RACQUET ACADEMY)/` | `PHOTOS FOR SAMPLE PROJECT/ARA/` |
| `PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/` | `PHOTOS FOR SAMPLE PROJECT/MERLIN/` |
| `PHOTOS FOR SAMPLE PROJECT/PARIJAAT ECLAT/` | `PHOTOS FOR SAMPLE PROJECT/PARIJAAT/` |
| `PHOTOS FOR SAMPLE PROJECT/RETHAL GREENS/` | `PHOTOS FOR SAMPLE PROJECT/RETHAL/` |

The folder `SHORTLISTED TREES & LANDSCAPE/` (at the root of the repo) is also not
synced. Images there are visible in GitHub but will not appear in WorkDrive.

These duplicate folders should be consolidated by FE. Until then, use the
**short-name folders** listed in the Folder Map above.

---

## GitHub paths not visible in Zoho WorkDrive

These GitHub paths are agent-only working areas and are not exposed in WorkDrive:

- `Business development/shared-workspace/review/vita{NNN}/` (beyond vita193) — agent working drafts
- `Business development/shared-workspace/approved/` — board-approved artefacts archive
- `Business development/shared-workspace/deliverables/` — final published outputs
- `Business development/shared-workspace/drafts/` — agent draft staging area
- `Business development/shared-workspace/email-templates/` — reusable email templates
- `Business development/shared-workspace/intelligence/` — competitor and market data
- `Business development/shared-workspace/scorecards/` — performance tracking

The board can view these via GitHub but should not need to upload to them.
