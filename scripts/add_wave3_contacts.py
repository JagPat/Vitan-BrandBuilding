#!/usr/bin/env python3
import csv
from datetime import datetime

file_path = 'Business development/shared-workspace/contacts-master.csv'
today = '2026-04-23'

new_contacts = [
    {
        'Contact ID': 'VIT-C-039',
        'Company': 'Lulu Group International',
        'Contact Name': 'Ananth Ram',
        'Title / Role': 'Director of Indian Operations',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'A',
        'Email (Primary)': 'sunilagarwal@in.lulumea.com',
        'Email Confidence': 'medium',
        'City': 'Ahmedabad',
        'State': 'Gujarat',
        'Sector': 'retail',
        'Enrichment Source': 'google search',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': "Developing Lulu Mall Ahmedabad in Chandkheda (India's largest mall). Major retail hub prospect.",
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Large scale international developer entry into Gujarat.',
        'Communication Guardrails': 'VALUE_LEAD,IDENTITY_FOCUS',
        'Discovery Status': 'complete',
        'Last Discovery Date': today
    },
    {
        'Contact ID': 'VIT-C-040',
        'Company': 'Shilp Group',
        'Contact Name': 'Yash Brahmbhatt',
        'Title / Role': 'Founder & CEO',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'A',
        'Email (Primary)': 'yash@shilp.co.in',
        'Email (Fallback)': 'sales@shilp.co.in',
        'Email Confidence': 'high',
        'City': 'Ahmedabad',
        'State': 'Gujarat',
        'Sector': 'commercial',
        'Enrichment Source': 'google search',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': 'Shilp Business Gateway on SG Highway. Prominent Ahmedabad developer.',
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Market leader in commercial and high-end residential.',
        'Communication Guardrails': 'VALUE_LEAD,WARM_REINTRO',
        'Discovery Status': 'complete',
        'Last Discovery Date': today
    },
    {
        'Contact ID': 'VIT-C-041',
        'Company': 'GIFT City (GIFTCL)',
        'Contact Name': '',
        'Title / Role': 'Leadership',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'B',
        'City': 'Gandhinagar',
        'State': 'Gujarat',
        'Sector': 'mixed-use',
        'Enrichment Source': 'google search',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': 'GIFT City expansion and Vertical City initiative 2026.',
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Government-backed smart city project.',
        'Communication Guardrails': 'VALUE_LEAD,TECHNICAL_FOCUS',
        'Discovery Status': 'partial',
        'Last Discovery Date': today
    }
]

rows = []
fieldnames = []

with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        # Update Zade Group (VIT-C-017) with Z2 project info
        if row['Contact ID'] == 'VIT-C-017':
            row['Notes'] += ' Also developing Z2 commercial skyscraper (32 floors) in Thaltej.'
            row['Last Updated'] = today
            row['Updated By'] = 'BB'
        rows.append(row)

for new_c in new_contacts:
    full_row = {fn: new_c.get(fn, '') for fn in fieldnames}
    rows.append(full_row)

with open(file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {len(new_contacts)} new contacts and updated VIT-C-017.")
