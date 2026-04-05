#!/usr/bin/env python3
"""
Vitan Growth OS: GitHub → WorkDrive Sync
Syncs files from the GitHub repo to Zoho WorkDrive on every push to main.
Handles: file upload, folder creation, and initial full migration.
"""

import os
import sys
import json
import time
import subprocess
import requests
from pathlib import Path

# === Configuration ===

ZOHO_ACCOUNTS_URL = "https://accounts.zoho.in/oauth/v2/token"
WORKDRIVE_API_BASE = "https://workdrive.zoho.in/api/v1"
WORKDRIVE_UPLOAD_URL = "https://workdrive.zoho.in/api/v1/upload"

TEAM_ID = "kidw386248c6f04a747c4991913a2e33042c2"
WORKSPACE_ID = "e5w44b189830995064556babffa4b4cd9c68c"

# Folder ID mapping: WorkDrive folder IDs
GROWTH_OS_ID = "1pu3j0063efb738b44cd6929455bd66a0d60a"

FOLDER_MAP = {
    # GitHub path prefix → WorkDrive folder ID
    "Business development/shared-workspace/review/vita191/": "1pu3jb52bdad662004a14bd315433324cc788",  # Competitor Research
    "Business development/shared-workspace/review/vita192/": "1pu3jb81167f86ed447aca28ac9a9d3c2f022",  # Market Analysis
    "Business development/shared-workspace/review/vita193/": "1pu3j9cdc1cd6ee584aabada3049feb3d066b",  # Outreach Drafts
    "Business development/shared-workspace/references/": "1pu3jbcfc67fec3e54225a406e02206328c76",     # Growth OS Playbook
    "Business development/shared-workspace/contacts-master.csv": "1pu3j6596ef15eea243e6885a2ae839cde599",  # Contacts
    "Business development/shared-workspace/change-notes/": "1pu3j5429b8a1a129424babf1d9fb38360d0b",   # Content Calendar
    "Business development/Brand Guide/": "1pu3j6301c26ba9a8497b99daef5e6a30476a",                     # Brand Guidelines
    "Business development/PHOTOS FOR SAMPLE PROJECT/ARA": "1pu3jd89dddaad69b49908467ea262baba378",
    "Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN": "1pu3jed8ac3e1155142e8a1cecb57f776622e",
    "Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM": "1pu3j15e9a7662b3e409c8d74e4a49698d330",
    "Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT": "1pu3jc2f6bf4edf7d46c69f05ae4a4928f386",
    "Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON": "1pu3j52c2bbbfff9c41778eb74adfa62c5b22",
    "Business development/PHOTOS FOR SAMPLE PROJECT/RETHAL": "1pu3j6adf43ab33e742e1bd38c0d2d803510a",
    "Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PARISAR": "1pu3jd044912b8f4b4e9ca2624349e1a77b5b",
    "Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PEGASUS": "1pu3j0c0b3f15d35f4b0ca00bfab4c2a9c4a0",
    "Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY": "1pu3j1de1290a5b8042a9a97092ca55f16658",
}

# Echo loop marker
SYNC_MARKER = "[workdrive-sync]"

# === OAuth Token Management ===

def get_access_token():
    """Get a fresh access token using the refresh token."""
    resp = requests.post(ZOHO_ACCOUNTS_URL, data={
        "refresh_token": os.environ["ZOHO_REFRESH_TOKEN"],
        "client_id": os.environ["ZOHO_CLIENT_ID"],
        "client_secret": os.environ["ZOHO_CLIENT_SECRET"],
        "grant_type": "refresh_token",
    })
    resp.raise_for_status()
    data = resp.json()
    if "access_token" not in data:
        print(f"ERROR: Failed to get access token: {data}")
        sys.exit(1)
    print(f"Got fresh access token (expires in {data.get('expires_in', '?')}s)")
    return data["access_token"]


# === WorkDrive API Helpers ===

def wd_headers(token):
    return {
        "Authorization": f"Zoho-oauthtoken {token}",
        "Content-Type": "application/json;charset=UTF-8",
    }


def list_folder(token, folder_id):
    """List contents of a WorkDrive folder."""
    resp = requests.get(
        f"{WORKDRIVE_API_BASE}/files/{folder_id}/files",
        headers=wd_headers(token),
    )
    resp.raise_for_status()
    items = {}
    for item in resp.json().get("data", []):
        attrs = item.get("attributes", {})
        items[attrs.get("name", "")] = {
            "id": item["id"],
            "type": attrs.get("type", ""),
            "description": attrs.get("description", ""),
        }
    return items


def upload_file(token, parent_id, filepath, description=""):
    """Upload a file to WorkDrive. Overwrites if exists."""
    with open(filepath, "rb") as f:
        resp = requests.post(
            WORKDRIVE_UPLOAD_URL,
            headers={"Authorization": f"Zoho-oauthtoken {token}"},
            files={"content": (os.path.basename(filepath), f)},
            data={
                "parent_id": parent_id,
                "override-name-exist": "true",
            },
        )
    if resp.status_code >= 400:
        print(f"  Upload error ({resp.status_code}): {resp.text[:200]}")
        return None
    data = resp.json()
    file_data = data.get("data", [{}])[0]
    resource_id = file_data.get("attributes", {}).get("resource_id", "")
    print(f"  Uploaded: {os.path.basename(filepath)} → {resource_id}")

    # Set description to mark as synced from GitHub (echo loop prevention)
    if resource_id and description:
        set_description(token, resource_id, description)

    return resource_id


def set_description(token, file_id, description):
    """Set file description (used for sync markers)."""
    try:
        requests.patch(
            f"{WORKDRIVE_API_BASE}/files/{file_id}",
            headers=wd_headers(token),
            json={
                "data": {
                    "attributes": {"description": description},
                    "type": "files",
                }
            },
        )
    except Exception as e:
        print(f"  Warning: Could not set description: {e}")


def create_folder(token, parent_id, name):
    """Create a folder in WorkDrive. Returns folder ID."""
    resp = requests.post(
        f"{WORKDRIVE_API_BASE}/files",
        headers=wd_headers(token),
        json={
            "data": {
                "attributes": {
                    "name": name,
                    "parent_id": parent_id,
                },
                "type": "files",
            }
        },
    )
    if resp.status_code >= 400:
        print(f"  Folder creation error ({resp.status_code}): {resp.text[:200]}")
        return None
    folder_id = resp.json().get("data", {}).get("id", "")
    print(f"  Created folder: {name} → {folder_id}")
    return folder_id


# === Sync Logic ===

def get_changed_files():
    """Get list of files changed in the latest push."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except subprocess.CalledProcessError:
        print("Warning: Could not get git diff. Running full sync.")
        return None


def resolve_workdrive_folder(filepath):
    """Map a GitHub file path to its WorkDrive folder ID."""
    for prefix, folder_id in sorted(FOLDER_MAP.items(), key=lambda x: -len(x[0])):
        if filepath.startswith(prefix) or filepath == prefix:
            return folder_id
    return None


def get_all_sync_files():
    """Get all files that should be synced (for full migration)."""
    files = []
    for prefix in FOLDER_MAP:
        path = Path(prefix)
        if path.is_file():
            files.append(str(path))
        elif path.is_dir():
            for f in path.rglob("*"):
                if f.is_file() and not f.name.startswith("."):
                    files.append(str(f))
    return files


def sync_file(token, filepath):
    """Sync a single file from GitHub to WorkDrive."""
    folder_id = resolve_workdrive_folder(filepath)
    if not folder_id:
        print(f"  Skipping (no mapping): {filepath}")
        return False

    local_path = Path(filepath)
    if not local_path.exists():
        print(f"  Skipping (deleted): {filepath}")
        return False

    if local_path.name.startswith("."):
        print(f"  Skipping (hidden): {filepath}")
        return False

    # Get current commit SHA for sync marker
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        sha = "unknown"

    description = f"synced:github:{sha}"
    resource_id = upload_file(token, folder_id, str(local_path), description)
    return resource_id is not None


def sync_new_folders(token, changed_files):
    """If new folders appear in changed files, create them in WorkDrive."""
    # Check if any changed file is in a new subfolder that doesn't exist in WorkDrive
    # For now, folders are pre-mapped so this mainly handles new subfolders
    seen_dirs = set()
    for filepath in changed_files:
        parent = str(Path(filepath).parent)
        if parent in seen_dirs:
            continue
        seen_dirs.add(parent)

        folder_id = resolve_workdrive_folder(filepath)
        if folder_id:
            # Check if the file is in a subdirectory of the mapped folder
            for prefix in FOLDER_MAP:
                if filepath.startswith(prefix):
                    relative = filepath[len(prefix):]
                    subdirs = Path(relative).parent.parts
                    if subdirs:
                        # Need to create nested subdirectory
                        current_parent = folder_id
                        for subdir in subdirs:
                            existing = list_folder(token, current_parent)
                            if subdir in existing:
                                current_parent = existing[subdir]["id"]
                            else:
                                new_id = create_folder(token, current_parent, subdir)
                                if new_id:
                                    current_parent = new_id
                    break


def main():
    print("=" * 60)
    print("Vitan Growth OS: GitHub → WorkDrive Sync")
    print("=" * 60)

    # Check for required env vars
    for var in ["ZOHO_CLIENT_ID", "ZOHO_CLIENT_SECRET", "ZOHO_REFRESH_TOKEN"]:
        if not os.environ.get(var):
            print(f"ERROR: Missing environment variable: {var}")
            sys.exit(1)

    # Check for echo loop
    try:
        commit_msg = subprocess.run(
            ["git", "log", "-1", "--pretty=%B"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if SYNC_MARKER in commit_msg:
            print(f"Skipping: commit is from WorkDrive sync ({SYNC_MARKER} found)")
            return
    except Exception:
        pass

    # Get access token
    token = get_access_token()

    # Determine which files to sync
    full_sync = os.environ.get("FULL_SYNC", "false").lower() == "true"

    if full_sync:
        print("\nRunning FULL SYNC (migration mode)")
        files_to_sync = get_all_sync_files()
    else:
        print("\nChecking changed files...")
        files_to_sync = get_changed_files()
        if files_to_sync is None:
            files_to_sync = get_all_sync_files()

    if not files_to_sync:
        print("No files to sync.")
        return

    # Filter to only mapped files
    mapped_files = [f for f in files_to_sync if resolve_workdrive_folder(f)]
    print(f"Found {len(mapped_files)} files to sync (out of {len(files_to_sync)} changed)")

    if not mapped_files:
        print("No mapped files to sync.")
        return

    # Create any needed subdirectories first
    print("\nChecking for new folders...")
    sync_new_folders(token, mapped_files)

    # Sync each file
    print(f"\nSyncing {len(mapped_files)} files...")
    success = 0
    failed = 0
    for filepath in mapped_files:
        print(f"\n  → {filepath}")
        if sync_file(token, filepath):
            success += 1
        else:
            failed += 1
        # Rate limiting: small delay between uploads
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"Sync complete: {success} uploaded, {failed} failed")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
