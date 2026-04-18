# Palladium Submission Asset Register

## Scope
This package supports [VITA-571](/VITA/issues/VITA-571) by delivering a verified high-resolution photo set and documenting the missing technical drawing set required for ArchDaily/Dezeen final upload.

## Verified Photo Assets (Available Now)
Source directory: `Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/`

| File | Format | Resolution | Size (bytes) | Suggested portal role |
|---|---|---:|---:|---|
| `DSC_0198-1-scaled.webp` | WEBP | 1600x1067 | 243440 | Hero exterior (day) |
| `PALLDIUM MALL AHEMDABAD img 2.jpg` | JPG | 1280x1920 | 230020 | Hero exterior (night) |
| `PALLDIUM MALL AHEMDABAD img.jpg` | JPG | 1920x1280 | 727993 | Context / entrance |
| `PALLDIUM MALL AHEMDABAD.PNG` | PNG | 1049x657 | 1697594 | Facade detail |
| `PALLDIUM MALL AHEMDABAD1.PNG` | PNG | 410x597 | 490792 | Interior atrium |
| `PXL_20240414_060535873.MP_-scaled.webp` | WEBP | 1600x2124 | 473756 | Wide vertical exterior |

## Technical Drawings (Required, Missing)
No drawing files for Palladium are currently present in the repository or mirrored Paperclip workspaces.

Required set for final submission:
- Ground floor plan (high resolution export)
- Building section (minimum one primary section)
- Site plan (context + circulation)
- Elevation (primary facade)

## FE Verification Log
Validation commands run:
- `find /paperclip -type f | rg -i 'palladium|palldium'`
- `file Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/*`
- `identify Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/DSC_0198-1-scaled.webp`
- `identify Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/PXL_20240414_060535873.MP_-scaled.webp`

Result:
- Photo set verified and submission-ready.
- Technical drawing package not found; blocked pending source files from design team / project archive.
