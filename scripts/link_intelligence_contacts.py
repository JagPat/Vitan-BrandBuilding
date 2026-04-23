import os
import re
import csv
import sys
import argparse

def load_contacts(csv_path):
    contacts_by_name = {}
    contacts_by_id = {}
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return contacts_by_name, contacts_by_id
    
    with open(csv_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Company'].strip()
            cid = row['Contact ID'].strip()
            # If multiple contacts for same company, we keep a list or the first one
            if name not in contacts_by_name:
                contacts_by_name[name] = cid
            contacts_by_id[cid] = name
    return contacts_by_name, contacts_by_id

def parse_markdown(md_path):
    if not os.path.exists(md_path):
        print(f"Error: MD file not found at {md_path}")
        return None
    
    with open(md_path, mode='r', encoding='utf-8') as f:
        return f.read()

def find_mentions(content, contacts_by_name):
    mentions = {}
    for company, cid in contacts_by_name.items():
        # Match company name if not preceded by [ and not followed by ] or (
        pattern = rf'(?<!\[){re.escape(company)}(?!\]|\()'
        if re.search(pattern, content):
            mentions[company] = cid
    return mentions

def get_existing_links(content):
    # Find all VIT-C-NNN occurrences
    return set(re.findall(r'VIT-C-\d+', content))

def validate_contacts_map(content):
    map_match = re.search(r'## \[CONTACTS_MAP\]\n(.*?)(?=\n##|$)', content, re.DOTALL)
    if not map_match:
        return False, []
    
    map_text = map_match.group(1)
    mapped_ids = re.findall(r'VIT-C-\d+', map_text)
    return True, mapped_ids

def generate_contacts_map(mentions, contacts_by_id):
    if not mentions:
        return ""
    
    lines = ["## [CONTACTS_MAP]"]
    lines.append("| Entity | Contact ID | Link |")
    lines.append("| --- | --- | --- |")
    # Sort by ID
    for company, cid in sorted(mentions.items(), key=lambda x: x[1]):
        lines.append(f"| {company} | {cid} | [{cid}](/VITA/contacts/{cid}) |")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description='Link intelligence briefs to contacts-master.csv')
    parser.add_argument('md_file', help='Path to the markdown intelligence brief')
    parser.add_argument('--csv', default='Business development/shared-workspace/contacts-master.csv', help='Path to contacts-master.csv')
    parser.add_argument('--fix', action='store_true', help='Update or append [CONTACTS_MAP]')
    
    args = parser.parse_args()
    
    contacts_by_name, contacts_by_id = load_contacts(args.csv)
    content = parse_markdown(args.md_file)
    
    if content is None:
        sys.exit(1)
    
    print(f"--- Analyzing: {args.md_file} ---")
    
    # 1. Find all mentions (unlinked)
    mentions = find_mentions(content, contacts_by_name)
    
    # 2. Find all existing links in text
    existing_links = get_existing_links(content)
    
    # 3. Check for map block
    has_map, mapped_ids = validate_contacts_map(content)
    
    # All relevant IDs for this document
    all_doc_ids = existing_links.union(set(mapped_ids))
    for cid in mentions.values():
        all_doc_ids.add(cid)
        
    # Validation
    invalid_ids = [cid for cid in all_doc_ids if cid not in contacts_by_id]
    if invalid_ids:
        print(f"CRITICAL: Found invalid Contact IDs in document: {', '.join(invalid_ids)}")
    
    print(f"Total contacts identified: {len(all_doc_ids)}")
    for cid in sorted(all_doc_ids):
        name = contacts_by_id.get(cid, "UNKNOWN")
        status = []
        if cid in existing_links: status.append("Linked in text")
        if cid in mapped_ids: status.append("In [CONTACTS_MAP]")
        if cid in mentions.values(): status.append("Mentioned unlinked")
        print(f"  - {cid}: {name} ({', '.join(status)})")

    if not has_map:
        print("\nStatus: [CONTACTS_MAP] block is missing.")
        if args.fix and all_doc_ids:
            # Create a map for ALL doc IDs
            doc_mentions = {contacts_by_id[cid]: cid for cid in all_doc_ids if cid in contacts_by_id}
            new_map = "\n\n" + generate_contacts_map(doc_mentions, contacts_by_id) + "\n"
            with open(args.md_file, 'a', encoding='utf-8') as f:
                f.write(new_map)
            print("Action: Appended [CONTACTS_MAP] block.")
    else:
        print("\nStatus: [CONTACTS_MAP] block present.")
        missing_from_map = [cid for cid in all_doc_ids if cid not in mapped_ids and cid in contacts_by_id]
        if missing_from_map:
            print(f"Items missing from map: {', '.join(missing_from_map)}")
            if args.fix:
                # Re-generate the whole map block
                doc_mentions = {contacts_by_id[cid]: cid for cid in all_doc_ids if cid in contacts_by_id}
                new_map_block = generate_contacts_map(doc_mentions, contacts_by_id)
                
                # Replace the old map block
                new_content = re.sub(r'## \[CONTACTS_MAP\].*?(\n##|$)', new_map_block + r'\1', content, flags=re.DOTALL)
                with open(args.md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("Action: Updated [CONTACTS_MAP] block with all identified contacts.")

if __name__ == "__main__":
    main()
