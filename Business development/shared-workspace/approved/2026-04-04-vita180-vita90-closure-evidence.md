# VITA-180 Closure Evidence for VITA-90

## Summary

This note restores objective closure evidence for [VITA-90](/VITA/issues/VITA-90), whose latest issue comment was blocker-oriented even though the pilot verification work had already been completed and later advanced.

## Verified Outcome

- Original four-platform pilot execution was completed and documented on 2026-04-03.
- The first live four-platform attempt produced `0/4` successful publishes and captured root causes for every platform.
- Follow-up execution later succeeded on LinkedIn, Facebook, and Instagram after credential and media fixes.
- X remained an external billing constraint rather than an unresolved adapter bug.

## Evidence Captured

### First full pilot result

- Request flow executed for X, LinkedIn, Facebook, and Instagram.
- Final run summary:
  - X: `HTTP 402` `CreditsDepleted`
  - LinkedIn: `HTTP 422` invalid author URN format
  - Facebook: `HTTP 403` insufficient page permission/admin context
  - Instagram: `HTTP 400` media URI rejected

### Later successful retry on supported platforms

- LinkedIn: `HTTP 201`
- Facebook: `HTTP 200`
- Facebook post id: `290161881095312_1534916488636597`
- Instagram create media: `HTTP 200`
- Instagram publish media: `HTTP 200`
- Instagram publish id: `18427804027187943`

## Closure Interpretation

- [VITA-90](/VITA/issues/VITA-90) required a controlled pilot plus verification capture.
- That verification now exists in a repo-tracked form: first as the full failure baseline, then as the narrowed successful retry once prerequisites were corrected.
- The stale blocker comment reflected an intermediate rerun gate, not the final deliverable state.
