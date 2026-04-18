#!/usr/bin/env python3
"""Helper to link entities in intelligence briefs to contacts-master.csv."""

import csv
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTACTS_CSV = REPO_ROOT / "Business development" / "shared-workspace" / "contacts-master.csv"

def load_contacts():
    contacts = []
    if not CONTACTS_CSV.exists():
        return contacts
    with open(CONTACTS_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append({
                "id": row.get("Contact ID"),
                "company": row.get("Company"),
                "name": row.get("Contact Name")
            })
    return contacts

def normalize(name):
    if not name: return ""
    return re.sub(r"[^a-z0-9]+", "", name.lower())

def find_matches(text, contacts):
    found = {}
    for contact in contacts:
        company = contact["company"]
        if not company: continue
        # Simple fuzzy match: if company name is in text
        if company.lower() in text.lower():
            found[company] = contact["id"]
    return found

def process_brief(brief_path, contacts):
    with open(brief_path, "r") as f:
        content = f.read()
    
    matches = find_matches(content, contacts)
    if not matches:
        print(f"No matches found for {brief_path.name}")
        return

    print(f"\n### [CONTACTS_MAP] for {brief_path.name}")
    print("| Entity | Contact ID |")
    print("| --- | --- |")
    for entity, cid in sorted(matches.items()):
        print(f"| {entity} | {cid} |")

def main():
    if len(sys.argv) < 2:
        print("Usage: link_intelligence_contacts.py <path_to_brief>")
        sys.exit(1)
    
    contacts = load_contacts()
    for arg in sys.argv[1:]:
        process_brief(Path(arg), contacts)

if __name__ == "__main__":
    main()
