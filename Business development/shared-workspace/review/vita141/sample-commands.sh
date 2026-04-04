#!/usr/bin/env bash
set -euo pipefail

SCRIPT="Business development/lead-enrichment/scripts/apollo_enrich.py"
QUEUE="Business development/shared-workspace/review/2026-04-03-vita133-apollo-enrichment-queue.csv"

python3 "$SCRIPT" org-enrich --domain "arvindsmartspaces.com"

# Requires Apollo plan access for people endpoints.
python3 "$SCRIPT" people-match --email "investor@arvindinfra.com" || true
python3 "$SCRIPT" people-search --organization-domains "arvindsmartspaces.com" --titles "CEO" --per-page 5 || true

python3 "$SCRIPT" enrich-queue --input-csv "$QUEUE" --include-org-fallback || true
