#!/usr/bin/env python3
import csv
import io

file_path = 'Business development/shared-workspace/contacts-master.csv'

ids_to_complete = ['VIT-C-006', 'VIT-C-007', 'VIT-C-008']

rows = []
fieldnames = []

with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        cid = row['Contact ID']
        if cid in ids_to_complete:
            row['Discovery Status'] = 'complete'
            row['Last Discovery Date'] = '2026-04-19'
            row['Sensitivity Level'] = 'green' # Default for flex space unless research says otherwise
            row['Sensitivity Type'] = 'none'
            row['Last Updated'] = '2026-04-19'
            row['Updated By'] = 'BB'
        rows.append(row)

with open(file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(ids_to_complete)} flexible workspace contacts.")
