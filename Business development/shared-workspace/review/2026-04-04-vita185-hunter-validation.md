# VITA-185 Hunter.io Validation

## Scope

Validate that Hunter.io is ready to replace Apollo for Business Builder email enrichment and verification.

## Runtime Validation

- `HUNTER_API_KEY` was present in the active Founding Engineer heartbeat environment.
- `GET /v2/account` returned `200 OK`.
- Account response confirmed the Hunter plan is `Free` with active search, verification, and credit counters plus reset date `2026-05-04`.

## Domain Search Smoke Test

- Request: `GET /v2/domain-search?domain=hunter.io`
- Result: `200 OK`
- Returned organization: `Hunter`
- Returned pattern: `{first}`
- Returned total results: `32`
- Returned page size: `10`
- Domain flags: `disposable=false`, `webmail=false`, `accept_all=false`

## Operational Outcome

- Hunter.io is operational in the current runtime and suitable as the default enrichment provider for Business Builder.
- Apollo should remain deprecated for email enrichment, people search, and verification.
- Business Builder should use Hunter Domain Search, Email Finder, and Email Verifier for future lead-enrichment work.

## Repo Gap Noted

- The task description referenced `Business development/shared-workspace/targeting-audience-master.csv`, but that file was not present in the checked-out `Vitan-BrandBuilding` repository during this validation pass.
- Before Business Builder writes enriched contacts back to Git, the targeting sheet needs to be restored or created at the intended shared-workspace path.
