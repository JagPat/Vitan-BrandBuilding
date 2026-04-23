#!/usr/bin/env python3
import csv
from pathlib import Path

csv_path = Path("Business development/shared-workspace/contacts-master.csv")
target_ids = {
    "VIT-C-009", "VIT-C-010", "VIT-C-011", "VIT-C-012", "VIT-C-013",
    "VIT-C-014", "VIT-C-015", "VIT-C-016", "VIT-C-017", "VIT-C-018"
}

rows = []
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row["Contact ID"] in target_ids:
            row["Draft Message Status"] = "drafted"
            row["VITA Issue"] = "VITA-595"
            row["Last Updated"] = "2026-04-18"
            row["Updated By"] = "BB"
        rows.append(row)

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(target_ids)} contacts in {csv_path}")
