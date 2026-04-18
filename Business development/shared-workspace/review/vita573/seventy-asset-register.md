# Seventy Submission Asset Register

## Scope
This package supports [VITA-573](/VITA/issues/VITA-573) by verifying available Seventy visual assets and documenting the missing technical drawing exports required for submission readiness.

## Source Reference Check
Issue scope references `Business development/shared-workspace/review/vita461/seventy-image-manifest.md`, but that file is not present in the current repository checkout.

## Verified Photo Assets (Available Now)
Source directory: `Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY/`

| File | Format | Resolution | Size (bytes) | Suggested portal role |
|---|---|---:|---:|---|
| `1.PNG` | PNG | 604x473 | 610953 | Context thumbnail / supporting visual |
| `DSC_7982.jpg` | JPG | 5504x8256 | 10152927 | Vertical hero / arrival sequence |
| `DSC_8455-HDR.jpg` | JPG | 8229x5486 | 8821192 | Exterior hero (wide) |
| `DSC_8768-HDR.jpg` | JPG | 8229x5486 | 7536630 | Exterior alternate / lighting variant |
| `DSC_8996-HDR.jpg` | JPG | 8230x5487 | 8183357 | Project context / facade composition |
| `DSC_9372.jpg` | JPG | 8184x5456 | 8050244 | User-experience perspective |

## Technical Drawings (Required, Missing)
No technical drawing files for Seventy are currently present in this repository for the requested editorial exports.

Required set from issue scope:
- Sky Villa floor plan (PDF/CAD export)
- "Cloud" bridge section (PDF/CAD export)

## FE Verification Log
Validation commands run:
- `find "Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY" -maxdepth 1 -type f`
- `identify -format "%wx%h" <file>` for each discovered asset
- `rg --files | rg -i "seventy|sky villa|cloud|\\.dwg$|\\.dxf$|\\.cad$|\\.pdf$"`

Result:
- Seventy photo set verified with dimensions and file-size metadata.
- Required technical drawing package is not in git and remains blocked pending source exports from design/project archive.
