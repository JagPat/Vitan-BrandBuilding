#!/usr/bin/env python3
import csv
from datetime import datetime

file_path = 'Business development/shared-workspace/contacts-master.csv'
today = '2026-04-20'

new_contacts = [
    {
        'Contact ID': 'VIT-C-025',
        'Company': 'Constera Realty',
        'Contact Name': 'Bhavin Mehta',
        'Title / Role': 'Managing Director',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'A',
        'Email (Primary)': 'bhavin.mehta@consterarealty.com',
        'Email (Fallback)': 'contact@consterarealty.com',
        'Email Confidence': 'high',
        'LinkedIn': 'https://www.linkedin.com/in/bhavin-mehta-consterarealty',
        'City': 'Ahmedabad',
        'State': 'Gujarat',
        'Sector': 'luxury residential',
        'Enrichment Source': 'google search + hunter.io',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': 'Anamika High Point (31 Floors). Focus on ultra-premium 4/5 BHK.',
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Flagship project Anamika High Point at Bodakdev.',
        'Communication Guardrails': 'VALUE_LEAD,IDENTITY_FOCUS',
        'Discovery Status': 'complete',
        'Last Discovery Date': today
    },
    {
        'Contact ID': 'VIT-C-026',
        'Company': 'Shypram Group',
        'Contact Name': 'Ankit Patel',
        'Title / Role': 'Partner',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'A',
        'Email (Primary)': 'info@shypram.com',
        'Email Confidence': 'medium',
        'LinkedIn': 'https://www.linkedin.com/in/ankit-patel-shypram-group/',
        'City': 'Ahmedabad',
        'State': 'Gujarat',
        'Sector': 'luxury residential',
        'Enrichment Source': 'google search',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': 'Stateland project (32 Floors) in Science City. JV with Ratnadeep Group.',
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Ultra-luxury skyscraper project Stateland.',
        'Communication Guardrails': 'VALUE_LEAD,TECH_LEAD_FOCUS',
        'Discovery Status': 'complete',
        'Last Discovery Date': today
    },
    {
        'Contact ID': 'VIT-C-027',
        'Company': 'Ratnadeep Group',
        'Contact Name': 'Vishal Patel',
        'Title / Role': 'CMD',
        'Contact Type': 'new_prospect',
        'Relationship Stage': 'cold',
        'Priority': 'A',
        'Email (Primary)': 'info@ratnadeepgroup.com',
        'Email Confidence': 'low',
        'LinkedIn': 'https://www.linkedin.com/in/vishal-patel-ratnadeep-group/',
        'City': 'Ahmedabad',
        'State': 'Gujarat',
        'Sector': 'luxury residential',
        'Enrichment Source': 'google search',
        'Enrichment Date': today,
        'Outreach Channel': 'email',
        'Assigned Agent': 'BB',
        'Draft Message Status': 'pending',
        'Notes': 'Stateland project partner. Established 1987.',
        'Created Date': today,
        'Last Updated': today,
        'Updated By': 'BB',
        'Sensitivity Type': 'none',
        'Sensitivity Level': 'green',
        'Sensitivity Detail': 'Partner in Stateland skyscraper.',
        'Communication Guardrails': 'VALUE_LEAD,WARM_REINTRO',
        'Discovery Status': 'complete',
        'Last Discovery Date': today
    }
]

rows = []
fieldnames = []

with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

for new_c in new_contacts:
    # Ensure all fieldnames are present
    full_row = {fn: new_c.get(fn, '') for fn in fieldnames}
    rows.append(full_row)

with open(file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {len(new_contacts)} new contacts.")
