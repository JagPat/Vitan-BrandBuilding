# Image and Drawing Manifest: Parijaat Eclat
**Issue**: VITA-189
**Status**: DRAFT — curation held for Principle Architect review
**Date**: 2026-08-24
**Publication state**: Not ready. Not approved. Not published. No portal upload.

Photography permission is flagged `true` in `intelligence/projects/parijaat-eclat.yaml` (photographer: Abhishek Shah). That flag is **not** live publish clearance.

---

## Verification method

Filenames were read from disk on this `agent/bs` working tree. Hashes were compared with the same paths on `origin/main` where those paths exist. No file was credited as Parijaat on filename alone when the name said Privilon.

---

## Folder A — present on this tree

Path: `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT ECLAT/`

All five files are named `Privilon (…).jpg`. They are **not** credited as Parijaat photography in the case-study narrative.

| Filename on this tree | Bytes | Pixels (approx.) | Camera (file metadata) | Credit on this draft | Evidence |
|---|---|---|---|---|---|
| `Privilon (10).jpg` | 6.6M | 3902 × 2195 | FC220 (drone) | **HOLD — mixed campus** | Byte-identical to `PRIVILON/Privilon (10).jpg` **and** to `origin/main` `PARIJAAT/PAARIJAT ECLAT (1).jpg`. Aerial of a courtyard with a glass commercial volume in frame. Do not use as a Parijaat-only hero. |
| `Privilon (27).jpg` | 16M | 5798 × 4361 | Nikon D7500 | **HOLD — filename Privilon** | Byte-identical to `origin/main` `PARIJAAT/PAARIJAT ECLAT (2).jpg`. Not present under `PRIVILON/`. Dusk approach / courtyard. PA to rule before any credit. |
| `Privilon (32).jpg` | 11M | 5568 × 3132 | Nikon D7500 | **HOLD — filename Privilon** | Byte-identical to `origin/main` `PARIJAAT/PAARIJAT ECLAT (3).jpg`. Not present under `PRIVILON/`. Twilight courtyard lounge. PA to rule before any credit. |
| `Privilon (35).jpg` | 8.8M | 5534 × 3113 | Nikon D7500 | **HOLD — filename Privilon** | Byte-identical to `origin/main` `PARIJAAT/PAARIJAT ECLAT (4).jpg`. Not present under `PRIVILON/`. View outward from a lobby through glass. PA to rule before any credit. |
| `Privilon (39).jpg` | 11M | 4894 × 2753 | Nikon D7500 | **HOLD — filename Privilon** | Byte-identical to `origin/main` `PARIJAAT/PAARIJAT ECLAT (5).jpg`. Not present under `PRIVILON/`. Dusk amenity pavilion beside water. PA to rule before any credit. |

Hash pairs (MD5) used for the identity check:

| This tree (`PARIJAAT ECLAT/`) | `origin/main` (`PARIJAAT/`) | Also in `PRIVILON/` |
|---|---|---|
| `Privilon (10).jpg` `3fc5029da8389277e6ba1d11f8236944` | `PAARIJAT ECLAT (1).jpg` same hash | **Yes** — `Privilon (10).jpg` same hash |
| `Privilon (27).jpg` `cf53924d9021acef21d25aee7300407c` | `PAARIJAT ECLAT (2).jpg` same hash | No |
| `Privilon (32).jpg` `140eaa0de8b48ebbaea63e4191ee528a` | `PAARIJAT ECLAT (3).jpg` same hash | No |
| `Privilon (35).jpg` `dc0a0d073411475992bdd013ca70c17d` | `PAARIJAT ECLAT (4).jpg` same hash | No |
| `Privilon (39).jpg` `656b5f054171071d6e6bdc3d9023c0a7` | `PAARIJAT ECLAT (5).jpg` same hash | No |

Visual notes below are observations of the files, not project facts and not a curated submission set.

---

## Folder B — expected, absent on this tree

Path: `Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT/`

This folder is **not on the `agent/bs` working tree**. Sync maps in `scripts/sync_to_workdrive.py` and `scripts/sync_from_workdrive.py` still point at it. The files below were verified by reading `origin/main` (not copied into this draft package).

| Filename on `origin/main` | Role suggested by filename | Present here? | Notes for PA |
|---|---|---|---|
| `PAARIJAT ECLAT (1).jpg` | Photo (spelling “PAARIJAT”) | No | Same bytes as ECLAT `Privilon (10).jpg` and PRIVILON `Privilon (10).jpg`. Mixed-campus hold. |
| `PAARIJAT ECLAT (2).jpg` | Photo | No | Same bytes as ECLAT `Privilon (27).jpg`. |
| `PAARIJAT ECLAT (3).jpg` | Photo | No | Same bytes as ECLAT `Privilon (32).jpg`. |
| `PAARIJAT ECLAT (4).jpg` | Photo | No | Same bytes as ECLAT `Privilon (35).jpg`. |
| `PAARIJAT ECLAT (5).jpg` | Photo | No | Same bytes as ECLAT `Privilon (39).jpg`. |
| `Paarijat eclat Masterplan.jpg` | Site / masterplan drawing | No | Named in WorkDrive sync commit `73cc8bd`. See drawing hold below. |
| `Paarijat eclat typical floor plan.jpg` | Typical floor plan | No | Named in WorkDrive sync commit `73cc8bd`. See drawing hold below. |
| `ASSET_CHECKLIST.md` | OC checklist (VITA-814, commit `9328e09`) | No | Historical. Claimed a masterplan and typical floor as available on 2026-04-23. Not proof that they sit on this tree now. |

---

## Drawings

Portal guidelines in-repo still ask for site plan, floor plans, and sections before any later filing. This draft does **not** attach drawings.

| Drawing | Status on this tree | If restored from `origin/main` | PA flags |
|---|---|---|---|
| Site / masterplan | **MISSING** | `Paarijat eclat Masterplan.jpg` (approx. 4615 × 3504, 1.1M) | Labels on that file include two towers (Tower-A / Tower-B) and amenity rooms. Those labels are **not** promoted into the case-study fact file. Confirm before any use. |
| Typical floor plan | **MISSING** | `Paarijat eclat typical floor plan.jpg` (approx. 4615 × 3504, 982K) | Sheet titles read “TOWER-A 1st to 9th Floor” and “TOWER-B 1st to 9th Floor”, with 4-bedroom room lists. That 1st–9th label may sit next to the yaml’s 23 floors / 48 units. Do not invent a floor breakdown. Confirm before any use. A Vitan mark is visible on the sheet; that does not add credits. |
| Ground floor plan | **MISSING** | Not found on this tree or in the `origin/main` PARIJAAT listing | Still required for a later portal binder. |
| Elevations | **MISSING** | Not found | Still required for a later portal binder. |
| Sections | **MISSING** | Not found | Still required for a later portal binder. |

Amenity words visible on the main-branch masterplan (pool, gym, play areas, and similar labels) are **not** copied into the narrative or metadata. They remain PENDING unless PA promotes them into the canonical yaml.

---

## Curated selection for submission

**None.** This draft does not nominate a hero image or a submission set.

Reason: every file on this tree is named Privilon; one file is also stored in the Privilon photo folder; the clearly named Parijaat photo and drawing set is not on this working tree.

---

## Photography credit (held)

- **Named in yaml**: Abhishek Shah
- **Permission flag in yaml**: true
- **EXIF artist/copyright on the five ECLAT JPEGs**: not established in this pass (no Artist field recovered from available file metadata)
- **Clearance for portal upload**: **PENDING Principle Architect** — yaml permission is not treated as live clearance

---

## Hypothesis (discarded)

The working idea that Parijaat Eclat is the cleanest unblocked first case study — because it is not ARA and already has photos plus plans — is **discarded for this tree**.

What the tree actually shows:

1. It is not ARA / VITA-211 / VITA-226. That part holds.
2. Photos exist, but every file in `PARIJAAT ECLAT/` is named Privilon.
3. One of those photos is a byte-identical duplicate of a Privilon-folder file.
4. The `PARIJAAT/` folder with Parijaat-named photos and two drawings is on `origin/main`, not on `agent/bs`.
5. Ground-floor plan, elevations, and sections are still missing even on `origin/main`.
6. GBA and several credit fields are blank in the canonical yaml.

---

## Next action

- **Principle Architect**: Rule on each HOLD file. Decide whether to restore `PARIJAAT/` from `origin/main` / WorkDrive.
- **Do not** retitle Privilon-named files as Parijaat without that ruling.
- **Do not** upload any image from this packet.
