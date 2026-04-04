#!/usr/bin/env python3
"""Apollo lead enrichment utility for Vitan Business Builder workflows.

Features:
- Single-person enrichment via /api/v1/people/match
- ICP prospect search via /api/v1/mixed_people/search
- Organization enrichment via /api/v1/organizations/enrich
- Queue CSV processing with normalized output artifacts
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_BASE_URL = "https://api.apollo.io"
DEFAULT_OUTPUT_DIR = Path("Business development/lead-enrichment/output")


@dataclass
class ApiResult:
    ok: bool
    status: str
    http_status: int | None
    endpoint: str
    payload: dict[str, Any]
    error: str | None = None


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def parse_json(raw: bytes) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        return {"raw": raw.decode("utf-8", errors="replace")}
    return data if isinstance(data, dict) else {"data": data}


def classify_error(http_status: int | None, payload: dict[str, Any], fallback_message: str) -> str:
    code = str(payload.get("error_code", "")).upper()

    if code in {"API_INACCESSIBLE", "FORBIDDEN_FEATURE"}:
        return "plan_limited"
    if http_status in (401, 403):
        return "auth_error"
    if http_status == 402:
        return "credits_depleted"
    if http_status == 404:
        return "not_found"
    if http_status == 429:
        return "rate_limited"
    message = f"{payload.get('error', '')} {fallback_message}".lower()
    if "rate" in message and "limit" in message:
        return "rate_limited"
    if "not found" in message:
        return "not_found"
    return "api_error"


def call_apollo(
    api_key: str,
    method: str,
    path: str,
    *,
    query: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    base_url: str = DEFAULT_BASE_URL,
    max_retries: int = 3,
) -> ApiResult:
    endpoint = base_url.rstrip("/") + path
    if query:
        encoded = urllib.parse.urlencode(query, doseq=True)
        endpoint = f"{endpoint}?{encoded}"

    payload_bytes: bytes | None = None
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
        # Apollo/Cloudflare blocks urllib default signatures in some runtimes.
        "User-Agent": "curl/8.5.0",
    }
    if body is not None:
        payload_bytes = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    for attempt in range(1, max_retries + 1):
        request = urllib.request.Request(endpoint, data=payload_bytes, method=method.upper(), headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                payload = parse_json(raw)
                return ApiResult(
                    ok=True,
                    status="ok",
                    http_status=response.getcode(),
                    endpoint=endpoint,
                    payload=payload,
                )
        except urllib.error.HTTPError as exc:
            raw = exc.read() if hasattr(exc, "read") else b""
            payload = parse_json(raw)
            status = classify_error(exc.code, payload, str(exc))

            if status == "rate_limited" and attempt < max_retries:
                retry_after = exc.headers.get("Retry-After")
                wait_seconds = int(retry_after) if retry_after and retry_after.isdigit() else min(2**attempt, 10)
                time.sleep(wait_seconds)
                continue

            return ApiResult(
                ok=False,
                status=status,
                http_status=exc.code,
                endpoint=endpoint,
                payload=payload,
                error=str(payload.get("error") or exc),
            )
        except urllib.error.URLError as exc:
            status = "network_error"
            if attempt < max_retries:
                time.sleep(min(2**attempt, 10))
                continue
            return ApiResult(
                ok=False,
                status=status,
                http_status=None,
                endpoint=endpoint,
                payload={},
                error=str(exc),
            )

    return ApiResult(
        ok=False,
        status="api_error",
        http_status=None,
        endpoint=endpoint,
        payload={},
        error="Unexpected retry loop exit",
    )


def people_match(api_key: str, args: argparse.Namespace) -> ApiResult:
    body: dict[str, Any] = {}
    if args.email:
        body["email"] = args.email
    if args.linkedin_url:
        body["linkedin_url"] = args.linkedin_url
    if args.first_name:
        body["first_name"] = args.first_name
    if args.last_name:
        body["last_name"] = args.last_name
    if args.organization_name:
        body["organization_name"] = args.organization_name

    if not body:
        raise ValueError("people-match requires at least one identifier")

    return call_apollo(api_key, "POST", "/api/v1/people/match", body=body)


def people_search(api_key: str, args: argparse.Namespace) -> ApiResult:
    titles = [part.strip() for part in args.titles.split(",") if part.strip()]
    body: dict[str, Any] = {
        "person_titles": titles,
        "person_seniorities": [part.strip() for part in args.seniorities.split(",") if part.strip()],
        "organization_locations": [part.strip() for part in args.locations.split(",") if part.strip()],
        "organization_num_employees_ranges": [part.strip() for part in args.company_size_ranges.split(",") if part.strip()],
        "contact_email_status": [part.strip() for part in args.email_status.split(",") if part.strip()],
        "page": args.page,
        "per_page": args.per_page,
    }

    domains = [part.strip() for part in args.organization_domains.split(",") if part.strip()]
    if domains:
        body["q_organization_domains_list"] = domains

    return call_apollo(api_key, "POST", "/api/v1/mixed_people/search", body=body)


def organization_enrich(api_key: str, args: argparse.Namespace) -> ApiResult:
    if not args.domain:
        raise ValueError("org-enrich requires --domain")
    return call_apollo(api_key, "GET", "/api/v1/organizations/enrich", query={"domain": args.domain})


def best_person_payload(search_payload: dict[str, Any]) -> dict[str, Any] | None:
    people = search_payload.get("people")
    if isinstance(people, list) and people:
        return people[0]
    contacts = search_payload.get("contacts")
    if isinstance(contacts, list) and contacts:
        return contacts[0]
    return None


def normalize_row(input_row: dict[str, str], person: dict[str, Any] | None, org: dict[str, Any] | None, status: str, note: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "account": input_row.get("account", ""),
        "priority": input_row.get("priority", ""),
        "target_role": input_row.get("target_role", ""),
        "target_person_name": input_row.get("target_person_name", ""),
        "company_domain": input_row.get("company_domain", ""),
        "location": input_row.get("location", ""),
        "recommended_next_action": "",
        "enrichment_status": status,
        "enrichment_note": note,
    }

    if person:
        out.update(
            {
                "full_name": person.get("name") or " ".join(filter(None, [person.get("first_name"), person.get("last_name")])),
                "title": person.get("title") or person.get("job_title"),
                "seniority": person.get("seniority"),
                "email": person.get("email"),
                "phone": person.get("phone_numbers", [{}])[0].get("sanitized_number") if isinstance(person.get("phone_numbers"), list) and person.get("phone_numbers") else person.get("sanitized_phone"),
                "linkedin_url": person.get("linkedin_url"),
                "company_name": (person.get("organization") or {}).get("name") if isinstance(person.get("organization"), dict) else person.get("organization_name"),
                "company_domain_out": (person.get("organization") or {}).get("primary_domain") if isinstance(person.get("organization"), dict) else input_row.get("company_domain", ""),
                "company_size": ((person.get("organization") or {}).get("estimated_num_employees")) if isinstance(person.get("organization"), dict) else None,
                "industry": ((person.get("organization") or {}).get("industry")) if isinstance(person.get("organization"), dict) else None,
            }
        )
        out["recommended_next_action"] = "Draft personalized outreach to named contact and route for approval"
        return out

    if org:
        out.update(
            {
                "company_name": org.get("name"),
                "company_domain_out": org.get("primary_domain"),
                "company_size": org.get("estimated_num_employees"),
                "industry": org.get("industry"),
                "linkedin_url": org.get("linkedin_url"),
                "phone": org.get("sanitized_phone") or org.get("phone"),
            }
        )
        out["recommended_next_action"] = "Use org intelligence to identify a named decision-maker manually"
    else:
        out["recommended_next_action"] = "Retry with alternate identifiers or manual research fallback"

    return out


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    headers: list[str] = []
    for row in rows:
        for key in row.keys():
            if key not in headers:
                headers.append(key)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def enrich_queue(api_key: str, args: argparse.Namespace) -> dict[str, Any]:
    input_path = Path(args.input_csv)
    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    normalized_rows: list[dict[str, Any]] = []
    raw_results: list[dict[str, Any]] = []

    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        role = (row.get("target_role") or "").strip()
        domain = (row.get("company_domain") or "").strip()
        search_args = argparse.Namespace(
            titles=role or "Manager,VP",
            seniorities=args.seniorities,
            locations=args.locations,
            company_size_ranges=args.company_size_ranges,
            email_status=args.email_status,
            page=1,
            per_page=args.per_row_limit,
            organization_domains=domain,
        )
        person_result = people_search(api_key, search_args)
        person = best_person_payload(person_result.payload) if person_result.ok else None

        org_result = None
        org_payload: dict[str, Any] | None = None
        if not person and args.include_org_fallback and domain:
            org_result = call_apollo(api_key, "GET", "/api/v1/organizations/enrich", query={"domain": domain})
            if org_result.ok:
                org_payload = org_result.payload.get("organization") if isinstance(org_result.payload.get("organization"), dict) else org_result.payload

        if person_result.ok and person:
            status = "ok"
            note = "person matched"
        elif person_result.ok and not person:
            status = "partial"
            note = "search returned no person rows"
        else:
            status = person_result.status
            note = person_result.error or "people search failed"

        normalized_rows.append(normalize_row(row, person, org_payload, status, note))
        raw_results.append(
            {
                "input": row,
                "people_search": {
                    "ok": person_result.ok,
                    "status": person_result.status,
                    "http_status": person_result.http_status,
                    "endpoint": person_result.endpoint,
                    "payload": person_result.payload,
                },
                "organization_enrich": {
                    "ok": org_result.ok,
                    "status": org_result.status,
                    "http_status": org_result.http_status,
                    "endpoint": org_result.endpoint,
                    "payload": org_result.payload,
                }
                if org_result is not None
                else None,
            }
        )

    stamp = utc_stamp()
    json_path = output_dir / f"apollo-enrichment-results-{stamp}.json"
    csv_path = output_dir / f"apollo-enrichment-results-{stamp}.csv"

    write_json(
        json_path,
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "input_csv": str(input_path),
            "row_count": len(rows),
            "results": raw_results,
        },
    )
    write_csv(csv_path, normalized_rows)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_csv": str(input_path),
        "output_json": str(json_path),
        "output_csv": str(csv_path),
        "row_count": len(rows),
        "status_counts": count_by_status(normalized_rows),
    }
    return summary


def count_by_status(rows: list[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        status = str(row.get("enrichment_status", "unknown"))
        out[status] = out.get(status, 0) + 1
    return out


def ensure_api_key(explicit_key: str | None) -> str:
    key = explicit_key or os.getenv("APOLLO_API_KEY")
    if not key:
        raise RuntimeError("APOLLO_API_KEY is missing. Set env var or pass --api-key.")
    return key


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apollo enrichment utility")
    parser.add_argument("--api-key", help="Apollo API key (optional if APOLLO_API_KEY env var is set)")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Output directory for artifacts")

    sub = parser.add_subparsers(dest="command", required=True)

    pm = sub.add_parser("people-match", help="Enrich a person from identifiers")
    pm.add_argument("--email")
    pm.add_argument("--linkedin-url")
    pm.add_argument("--first-name")
    pm.add_argument("--last-name")
    pm.add_argument("--organization-name")

    ps = sub.add_parser("people-search", help="Search people by ICP filters")
    ps.add_argument("--organization-domains", default="", help="Comma-separated organization domains")
    ps.add_argument("--titles", default="Manager,VP")
    ps.add_argument("--seniorities", default="director,c_suite")
    ps.add_argument("--locations", default="United States")
    ps.add_argument("--company-size-ranges", default="101,10000")
    ps.add_argument("--email-status", default="verified")
    ps.add_argument("--page", type=int, default=1)
    ps.add_argument("--per-page", type=int, default=25)

    oe = sub.add_parser("org-enrich", help="Enrich organization by domain")
    oe.add_argument("--domain", required=True)

    eq = sub.add_parser("enrich-queue", help="Run enrichment against queue CSV")
    eq.add_argument("--input-csv", required=True)
    eq.add_argument("--per-row-limit", type=int, default=10)
    eq.add_argument("--seniorities", default="director,c_suite")
    eq.add_argument("--locations", default="United States")
    eq.add_argument("--company-size-ranges", default="101,10000")
    eq.add_argument("--email-status", default="verified")
    eq.add_argument("--include-org-fallback", action="store_true", default=False)

    return parser


def run_single(result: ApiResult, output_dir: Path, command: str) -> dict[str, Any]:
    stamp = utc_stamp()
    out_path = output_dir / f"apollo-{command}-{stamp}.json"
    record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "ok": result.ok,
        "status": result.status,
        "http_status": result.http_status,
        "endpoint": result.endpoint,
        "payload": result.payload,
        "error": result.error,
    }
    write_json(out_path, record)
    return {"output_json": str(out_path), **record}


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        api_key = ensure_api_key(args.api_key)
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if args.command == "people-match":
            result = people_match(api_key, args)
            summary = run_single(result, output_dir, "people-match")
        elif args.command == "people-search":
            result = people_search(api_key, args)
            summary = run_single(result, output_dir, "people-search")
        elif args.command == "org-enrich":
            result = organization_enrich(api_key, args)
            summary = run_single(result, output_dir, "org-enrich")
        elif args.command == "enrich-queue":
            summary = enrich_queue(api_key, args)
        else:
            raise RuntimeError(f"Unsupported command: {args.command}")

        print(json.dumps(summary, indent=2, ensure_ascii=True))

        status = summary.get("status") if isinstance(summary, dict) else None
        if status in {"auth_error", "credits_depleted", "rate_limited", "plan_limited", "api_error", "network_error"}:
            return 2
        return 0

    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
