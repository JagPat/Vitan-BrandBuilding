#!/usr/bin/env python3
import csv
from pathlib import Path

csv_path = Path("Business development/shared-workspace/contacts-master.csv")
target_ids = {
    "VIT-C-028", "VIT-C-029", "VIT-C-030", "VIT-C-031", "VIT-C-032",
    "VIT-C-033", "VIT-C-034", "VIT-C-035", "VIT-C-036", "VIT-C-037", "VIT-C-038"
}

rows = []
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        cid = row["Contact ID"]
        if cid in target_ids:
            row["Response Status"] = "waiting"
            row["Draft Message Status"] = "sent"
            row["Last Contacted"] = "2026-04-23"
            row["Last Updated"] = "2026-04-23"
            row["Updated By"] = "BB"
            
            # Update Notes with outreach record
            prefix = "Stage 1 Skyscraper Sent 2026-04-23: "
            if cid == "VIT-C-028": row["Notes"] = prefix + "Shivanta Group milestones."
            elif cid == "VIT-C-029": row["Notes"] = prefix + "Sivanta Infra Projects LLP milestones."
            elif cid == "VIT-C-030": row["Notes"] = prefix + "150m Tremont Tower execution."
            elif cid == "VIT-C-031": row["Notes"] = prefix + "The Westin Shilaj technical rigor."
            elif cid == "VIT-C-032": row["Notes"] = prefix + "Times Marvel ROI for Thaltej."
            elif cid == "VIT-C-033": row["Notes"] = prefix + "Gala Corporat mixed-use efficiency."
            elif cid == "VIT-C-034": row["Notes"] = prefix + "Brillia precision at 32 floors."
            elif cid == "VIT-C-035": row["Notes"] = prefix + "Wynn Sphere engineering."
            elif cid == "VIT-C-036": row["Notes"] = prefix + "The 31st Sky Villa execution."
            elif cid == "VIT-C-037": row["Notes"] = prefix + "Trogon Twin Towers scaling."
            elif cid == "VIT-C-038": row["Notes"] = prefix + "Gota 150m frontier."
            
        rows.append(row)

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(target_ids)} contacts in {csv_path}")
