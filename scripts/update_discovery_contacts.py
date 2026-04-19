#!/usr/bin/env python3
import csv
import io
from datetime import datetime

file_path = 'Business development/shared-workspace/contacts-master.csv'

updates = {
    'VIT-C-003': {
        'Sensitivity Type': 'competitive,reputational',
        'Sensitivity Level': 'amber',
        'Sensitivity Detail': 'IT and ED raids (2021/2022). Deep partnership with INI Design Studio.',
        'Communication Guardrails': 'NO_COMPETITOR_MENTION,VALUE_LEAD,INDEPENDENCE_FRAME',
        'Discovery Status': 'complete',
        'Last Discovery Date': '2026-04-19'
    },
    'VIT-C-004': {
        'Sensitivity Type': 'competitive',
        'Sensitivity Level': 'amber',
        'Sensitivity Detail': 'Long-standing collaboration with Apurva Amin. JV history with HN Safal.',
        'Communication Guardrails': 'NO_COMPETITOR_MENTION,VALUE_LEAD,WARM_REINTRO',
        'Discovery Status': 'complete',
        'Last Discovery Date': '2026-04-19'
    }
}

rows = []
fieldnames = []

with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        cid = row['Contact ID']
        if cid in updates:
            row.update(updates[cid])
            row['Last Updated'] = '2026-04-19'
            row['Updated By'] = 'BB'
        rows.append(row)

with open(file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(updates)} contacts.")
