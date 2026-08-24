# Image and Drawing Manifest: Parijaat Eclat
**Issue**: VITA-189
**Status**: PARKED / in_progress — all images HOLD; no hero set
**Date**: 2026-08-24
**Publication state**: Not ready. Not approved. Not published. No portal upload.
**Wait-state owner**: Not Principle Architect. Tree restore and filename collision wait on Founding Engineer, only after PA says the packet may take files.

Yaml `photography_permission: true` (photographer: Abhishek Shah) is **not** upload clearance.

---

## Verification method

Filenames were read from disk on this `agent/bs` working tree. Hashes were compared with the same paths on `origin/main` where those paths exist. No file is credited as Parijaat while the filename on this tree says Privilon. Files were not copied from main into this packet.

---

## Folder A — present on this tree — HOLD (no hero set)

Path: `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT ECLAT/`

All five files are named `Privilon (…).jpg`. **No hero set. Hold all five.** None are credited as Parijaat photography.

| Filename on this tree | Bytes | Pixels (approx.) | Camera (file metadata) | Credit on this draft | Hold reason |
|---|---|---|---|---|---|
| `Privilon (10).jpg` | 6.6M | 3902 × 2195 | FC220 (drone) | **HOLD — mixed-campus** | Byte-identical to `PRIVILON/Privilon (10).jpg` **and** to `origin/main` `PARIJAAT/PAARIJAT ECLAT (1).jpg`. Mixed-campus. **Cannot be a Parijaat-only hero.** |
| `Privilon (27).jpg` | 16M | 5798 × 4361 | Nikon D7500 | **HOLD — uncredited** | Filename says Privilon. Stays uncredited while it says Privilon, even though `origin/main` also stores the same bytes as `PARIJAAT/PAARIJAT ECLAT (2).jpg`. |
| `Privilon (32).jpg` | 11M | 5568 × 3132 | Nikon D7500 | **HOLD — uncredited** | Filename says Privilon. Stays uncredited while it says Privilon, even though `origin/main` also stores the same bytes as `PARIJAAT/PAARIJAT ECLAT (3).jpg`. |
| `Privilon (35).jpg` | 8.8M | 5534 × 3113 | Nikon D7500 | **HOLD — uncredited** | Filename says Privilon. Stays uncredited while it says Privilon, even though `origin/main` also stores the same bytes as `PARIJAAT/PAARIJAT ECLAT (4).jpg`. |
| `Privilon (39).jpg` | 11M | 4894 × 2753 | Nikon D7500 | **HOLD — uncredited** | Filename says Privilon. Stays uncredited while it says Privilon, even though `origin/main` also stores the same bytes as `PARIJAAT/PAARIJAT ECLAT (5).jpg`. |

Hash pairs (MD5):

| This tree (`PARIJAAT ECLAT/`) | `origin/main` (`PARIJAAT/`) | Also in `PRIVILON/` |
|---|---|---|
| `Privilon (10).jpg` `3fc5029da8389277e6ba1d11f8236944` | `PAARIJAT ECLAT (1).jpg` same hash | **Yes** — `Privilon (10).jpg` same hash |
| `Privilon (27).jpg` `cf53924d9021acef21d25aee7300407c` | `PAARIJAT ECLAT (2).jpg` same hash | No |
| `Privilon (32).jpg` `140eaa0de8b48ebbaea63e4191ee528a` | `PAARIJAT ECLAT (3).jpg` same hash | No |
| `Privilon (35).jpg` `dc0a0d073411475992bdd013ca70c17d` | `PAARIJAT ECLAT (4).jpg` same hash | No |
| `Privilon (39).jpg` `656b5f054171071d6e6bdc3d9023c0a7` | `PAARIJAT ECLAT (5).jpg` same hash | No |

Main-branch storage under `PARIJAAT/` is not a credit and is not a reason to attach or retitle files.

---

## Folder B — absent on this tree — do not copy from main

Path: `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT/`

This folder is **not on the `agent/bs` working tree**. It was not copied into this packet. Sync maps still point at it. Presence on `origin/main` is recorded only so the filename collision is visible.

| Filename on `origin/main` | Present here? | Hold |
|---|---|---|
| `PAARIJAT ECLAT (1).jpg` | No | Same bytes as ECLAT `Privilon (10).jpg` and PRIVILON `Privilon (10).jpg`. Mixed-campus. Cannot be a Parijaat-only hero. |
| `PAARIJAT ECLAT (2).jpg` | No | Same bytes as ECLAT `Privilon (27).jpg`. Uncredited while the tree filename says Privilon. |
| `PAARIJAT ECLAT (3).jpg` | No | Same bytes as ECLAT `Privilon (32).jpg`. Uncredited while the tree filename says Privilon. |
| `PAARIJAT ECLAT (4).jpg` | No | Same bytes as ECLAT `Privilon (35).jpg`. Uncredited while the tree filename says Privilon. |
| `PAARIJAT ECLAT (5).jpg` | No | Same bytes as ECLAT `Privilon (39).jpg`. Uncredited while the tree filename says Privilon. |
| `Paarijat eclat Masterplan.jpg` | No | Drawing. Not attached. Not copied. See drawing hold. |
| `Paarijat eclat typical floor plan.jpg` | No | Drawing. Not attached. Not copied. See drawing hold. |
| `ASSET_CHECKLIST.md` | No | Historical OC note (VITA-814). Not current presence on this tree. |

**Named unblocker for tree restore and filename collision**: Founding Engineer, only after PA says the packet may take files.

---

## Drawings — not attached; yaml must be reconciled first

This packet does **not** attach drawings and does **not** copy them from `origin/main`.

- Masterplan amenity labels are **not** promoted into the narrative or metadata.
- “1st to 9th Floor” tower titles are **not** promoted. They conflict with the yaml’s 23 floors / 48 units.
- The yaml must be reconciled before drawings are considered.

| Drawing | On this tree | Action |
|---|---|---|
| Site / masterplan | MISSING | Do not attach. Do not copy from main. Do not promote amenity labels. |
| Typical floor plan | MISSING | Do not attach. Do not copy from main. Do not promote “1st to 9th Floor” titles. |
| Ground floor plan | MISSING | Not found. Still absent. |
| Elevations | MISSING | Not found. Still absent. |
| Sections | MISSING | Not found. Still absent. |

---

## Curated selection for submission

**None.** No hero set. Hold all five images.

---

## Photography credit (held)

- **Named in yaml**: Abhishek Shah
- **Yaml `photography_permission`**: true
- **Upload clearance**: **no** — yaml permission is not upload clearance
- **EXIF artist/copyright on the five ECLAT JPEGs**: not established in this pass

This is not a campaign project until the photo set is clean.

---

## Hypothesis (discarded)

The idea that the existing draft already matched this parked gate is discarded. The first draft still named Principle Architect as the wait-state owner and still invited scope confirmation. This rewrite parks the packet and names the unblockers.

The earlier idea that this is the cleanest unblocked first case study is still discarded: photos exist, but all five are HOLD; one is mixed-campus; drawings are not attached; yaml and drawing titles are unreconciled.

---

## Parked action

- Do not retitle Privilon-named files as Parijaat.
- Do not upload any image from this packet.
- Do not copy `PARIJAAT/` from main into this packet.
- Facts stay PENDING until Board / studio records supply them.
- File restore waits on Founding Engineer, only after PA says the packet may take files.
