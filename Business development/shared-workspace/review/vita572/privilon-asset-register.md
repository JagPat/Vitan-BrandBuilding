# Privilon Submission Asset Register

## Scope
This package supports [VITA-572](/VITA/issues/VITA-572) by verifying available Privilon visual assets and documenting the missing technical drawing set required for portal submission readiness.

## Verified Photo Assets (Available Now)
Source directory: `Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/`

| File | Format | Resolution | Size (bytes) | Suggested portal role |
|---|---|---:|---:|---|
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/FOR BOOK/Privilon (13).jpg | JPG | 5568x3132 | 10826020 | Exterior hero candidate |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/FOR BOOK/Privilon (16).jpg | JPG | 4191x2383 | 6084487 | Project experience / user perspective |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/FOR BOOK/Privilon (2).jpg | JPG | 5368x3132 | 12449577 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/FOR BOOK/Privilon (23).jpg | JPG | 5271x2965 | 9260867 | Massing and composition |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/FOR BOOK/Privilon (54).jpg | JPG | 5526x3611 | 14902997 | Alternate hero / dusk-lighting |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (10).jpg | JPG | 3902x2195 | 6821259 | Facade / streetscape context |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (12).jpg | JPG | 3598x2066 | 5431624 | Architectural detail |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (13).jpg | JPG | 5568x3132 | 10826020 | Exterior hero candidate |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (14).jpg | JPG | 4650x2617 | 7852378 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (15).jpg | JPG | 5568x3712 | 12582852 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (16).jpg | JPG | 4191x2383 | 6084487 | Project experience / user perspective |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (17).jpg | JPG | 3561x4873 | 13518167 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (2).jpg | JPG | 5368x3132 | 12449577 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (23).jpg | JPG | 5271x2965 | 9260867 | Massing and composition |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (26).jpg | JPG | 5155x3459 | 12805763 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (29).jpg | JPG | 5568x3611 | 12772577 | Supporting project photography |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (54).jpg | JPG | 5526x3611 | 14902997 | Alternate hero / dusk-lighting |
| Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/Privilon (6).jpg | JPG | 3150x1772 | 5267911 | Supporting project photography |

## Technical Drawings (Required, Missing)
No drawing files for Privilon are currently present in this repository for the required editorial exports.

Required set from issue scope:
- Site plan (PDF/CAD export)
- Typical office plan (PDF/CAD export)
- Retail plan (PDF/CAD export)
- Project sections (minimum one primary section)

## FE Verification Log
Validation commands run:
- `find "Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON" -maxdepth 3 -type f`
- `identify -format "%wx%h" <file>` for each discovered asset
- `find "Business development" -type f | rg -i "privilon|site plan|typical office|retail|section|dwg|dxf|cad"`

Result:
- Photo set is verified with dimensions/size metadata.
- Required technical drawing package is not in git and remains blocked pending source exports from design/project archive.
