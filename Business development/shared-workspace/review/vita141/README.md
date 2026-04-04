# Apollo Lead Enrichment (VITA-141)

Reusable Apollo enrichment tooling for Business Builder workflows.

## Files
- `scripts/apollo_enrich.py`: CLI for people match, people search, org enrich, and queue enrichment
- `examples/sample-commands.sh`: Command examples
- `output/`: Generated enrichment artifacts (`.json` + `.csv`)

## Requirements
- Python 3.10+
- `APOLLO_API_KEY` environment variable, or pass `--api-key`

## Commands

### 1) Person enrichment by known identifier
```bash
python3 "Business development/lead-enrichment/scripts/apollo_enrich.py" \
  people-match --email "someone@company.com"
```

### 2) ICP people search
```bash
python3 "Business development/lead-enrichment/scripts/apollo_enrich.py" \
  people-search \
  --organization-domains "arvindsmartspaces.com" \
  --titles "Manager,VP" \
  --seniorities "director,c_suite" \
  --locations "United States" \
  --company-size-ranges "101,10000" \
  --email-status "verified" \
  --per-page 25
```

### 3) Organization enrichment by domain
```bash
python3 "Business development/lead-enrichment/scripts/apollo_enrich.py" \
  org-enrich --domain "arvindsmartspaces.com"
```

### 4) Queue enrichment from CSV
```bash
python3 "Business development/lead-enrichment/scripts/apollo_enrich.py" \
  enrich-queue \
  --input-csv "Business development/shared-workspace/review/2026-04-03-vita133-apollo-enrichment-queue.csv" \
  --include-org-fallback
```

## Output Schema (normalized CSV)
For each queue row, output includes:
- `full_name`, `title`, `seniority`
- `email`, `phone`, `linkedin_url`
- `company_name`, `company_domain_out`, `company_size`, `industry`
- `enrichment_status`, `enrichment_note`, `recommended_next_action`

## Status Mapping
- `ok`: successful call with matched contact data
- `partial`: successful call but no matching person row
- `not_found`: explicit 404 response
- `auth_error`: 401/403 credential problems
- `credits_depleted`: 402 billing/credit limit
- `rate_limited`: 429 throttling (auto-retry with backoff)
- `plan_limited`: endpoint blocked by Apollo plan (`API_INACCESSIBLE`)
- `api_error` / `network_error`: non-specific failure

## Operational Notes
- Script never writes API keys to files or console.
- For `auth_error` (401/403), raise a `[TECH]` issue to Founding Engineer.
- For `credits_depleted` or `plan_limited`, raise an `[ESCALATION]` issue to board/CEO for plan upgrade.
