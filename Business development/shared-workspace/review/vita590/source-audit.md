# VITA-590 Source Audit

Date (UTC): 2026-04-20

## Scope
Validate whether high-resolution photos for Shaligram Luxuria and Augusta are currently available in the repo to unblock [VITA-590](/VITA/issues/VITA-590) and upstream [VITA-474](/VITA/issues/VITA-474).

## Search Results
- Global filename scan (`rg --files | rg -i 'shaligram|augusta|luxuria'`) returned no matches.
- Existing project photo roots under `Business development/PHOTOS FOR SAMPLE PROJECT/` include Palladium, Privilon, Seventy, and other projects, but no Shaligram/Augusta directories.

## Evidence
- Missing names scan:
  - `cd repo && rg --files | rg -i '(shaligram|augusta|luxuria)'` -> no output
- Photo root listing:
  - `find 'Business development/PHOTOS FOR SAMPLE PROJECT' -maxdepth 2 -type d`
  - No directory path contains `shaligram`, `augusta`, or `luxuria`.

## Conclusion
VITA-590 remains blocked by missing source assets. FE cannot package the requested high-resolution files until the board uploads Shaligram Luxuria and Augusta media to the repository/workspace.

## Requested Upload Target
- Recommended path: `Business development/PHOTOS FOR SAMPLE PROJECT/SHALIGRAM LUXURIA/`
- Recommended path: `Business development/PHOTOS FOR SAMPLE PROJECT/AUGUSTA/`
- Expected formats: original JPG/PNG/TIFF or lossless exports with dimensions >= 2400px on the long edge.
