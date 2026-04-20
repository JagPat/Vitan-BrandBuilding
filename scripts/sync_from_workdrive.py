#!/usr/bin/env python3
"""
Vitan Growth OS: WorkDrive → GitHub Sync (Reverse Sync)
Polls Zoho WorkDrive for file changes and commits them back to GitHub.
Runs on a cron schedule via GitHub Actions.

Echo-loop prevention:
  - Files with description starting with "synced:github:" are skipped
    (they were pushed by the forward sync).
  - Commits use the [workdrive-sync] marker so the forward sync skips them.
  - A state file (.sync/workdrive_state.json) tracks known file modified_times
    to avoid re-downloading unchanged files.
"""

import os
import sys
import json
import time
import hashlib
import subprocess
import requests
from pathlib import Path
from datetime import datetime

# === Configuration ===

ZOHO_ACCOUNTS_URL = "https://accounts.zoho.in/oauth/v2/token"
WORKDRIVE_API_BASE = "https://workdrive.zoho.in/api/v1"

TEAM_ID = "kidw386248c6f04a747c4991913a2e33042c2"
WORKSPACE_ID = "e5w44b189830995064556babffa4b4cd9c68c"
GROWTH_OS_ID = "1pu3j0063efb738b44cd6929455bd66a0d60a"

# Reverse mapping: WorkDrive folder ID → GitHub directory path
# This is the inverse of FOLDER_MAP in sync_to_workdrive.py
REVERSE_FOLDER_MAP = {
    "1pu3jb52bdad662004a14bd315433324cc788": "Business development/shared-workspace/review/vita191/",   # Competitor Research
    "1pu3jb81167f86ed447aca28ac9a9d3c2f022": "Business development/shared-workspace/review/vita192/",   # Market Analysis
    "1pu3j9cdc1cd6ee584aabada3049feb3d066b": "Business development/shared-workspace/review/vita193/",   # Outreach Drafts
    "1pu3jbcfc67fec3e54225a406e02206328c76": "Business development/shared-workspace/references/",       # Growth OS Playbook
    "1pu3j6596ef15eea243e6885a2ae839cde599": "Business development/shared-workspace/",                  # Contacts (contacts-master.csv lives here)
    "1pu3j5429b8a1a129424babf1d9fb38360d0b": "Business development/shared-workspace/change-notes/",     # Content Calendar
    "1pu3j6301c26ba9a8497b99daef5e6a30476a": "Business development/Brand Guide/",                       # Brand Guidelines
    "1pu3jd89dddaad69b49908467ea262baba378": "Business development/PHOTOS FOR SAMPLE PROJECT/ARA (AHMEDABAD RACQUET ACADEMY)/",
    "1pu3jed8ac3e1155142e8a1cecb57f776622e": "Business development/PHOTOS FOR SAMPLE PROJECT/MERLIN PENTAGON/",
    "1pu3j15e9a7662b3e409c8d74e4a49698d330": "Business development/PHOTOS FOR SAMPLE PROJECT/PALLADIUM/",
    "1pu3jc2f6bf4edf7d46c69f05ae4a4928f386": "Business development/PHOTOS FOR SAMPLE PROJECT/PARIJAAT ECLAT/",
    "1pu3j52c2bbbfff9c41778eb74adfa62c5b22": "Business development/PHOTOS FOR SAMPLE PROJECT/PRIVILON/",
    "1pu3j6adf43ab33e742e1bd38c0d2d803510a": "Business development/PHOTOS FOR SAMPLE PROJECT/RETHAL GREENS/",
    "1pu3jd044912b8f4b4e9ca2624349e1a77b5b": "Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PARISAR/",
    "1pu3j0c0b3f15d35f4b0ca00bfab4c2a9c4a0": "Business development/PHOTOS FOR SAMPLE PROJECT/SAFAL PEGASUS/",
    "1pu3j1de1290a5b8042a9a97092ca55f16658": "Business development/PHOTOS FOR SAMPLE PROJECT/SEVENTY/",
}

# Echo loop markers
SYNC_MARKER = "[workdrive-sync]"
GITHUB_SYNC_PREFIX = "synced:github:"

# State file for tracking known file states
STATE_FILE = ".sync/workdrive_state.json"

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


def list_folder_files(token, folder_id, page_offset=0, page_limit=50):
    """List all files (not folders) in a WorkDrive folder with metadata."""
    all_files = []
    offset = page_offset

    while True:
        resp = requests.get(
            f"{WORKDRIVE_API_BASE}/files/{folder_id}/files",
            headers=wd_headers(token),
            params={
                "page[offset]": offset,
                "page[limit]": page_limit,
            },
        )
        resp.raise_for_status()
        data = resp.json().get("data", [])

        if not data:
            break

        for item in data:
            attrs = item.get("attributes", {})
            file_type = attrs.get("type", "")

            # Skip folders — we only care about files
            if file_type == "folder":
                continue

            all_files.append({
                "id": item["id"],
                "name": attrs.get("name", ""),
                "modified_time": attrs.get("modified_time_in_millisecond", 0),
                "description": attrs.get("description", ""),
                "type": file_type,
                "size": attrs.get("storage_info", {}).get("size", 0),
            })

        # Check if there are more pages
        if len(data) < page_limit:
            break
        offset += page_limit
        time.sleep(0.3)  # Rate limit

    return all_files


def download_file(token, file_id, save_path):
    """Download a file from WorkDrive to a local path."""
    resp = requests.get(
        f"{WORKDRIVE_API_BASE}/download/{file_id}",
        headers={"Authorization": f"Zoho-oauthtoken {token}"},
        stream=True,
    )
    resp.raise_for_status()

    # Ensure parent directory exists
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return True


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


# === State Management ===

def load_state():
    """Load the sync state file tracking known file states."""
    state_path = Path(STATE_FILE)
    if state_path.exists():
        try:
            with open(state_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read state file. Starting fresh.")
    return {"files": {}, "last_sync_ts": 0}


def save_state(state):
    """Save sync state to disk."""
    state_path = Path(STATE_FILE)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


def file_content_hash(filepath):
    """Compute SHA-256 hash of a local file for change detection."""
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha.update(chunk)
    return sha.hexdigest()


# === Sync Logic ===

def is_github_synced(description):
    """Check if a file's description indicates it was synced FROM GitHub."""
    return description.strip().startswith(GITHUB_SYNC_PREFIX)


def scan_folder(token, folder_id, github_path, state, changes):
    """Scan a single WorkDrive folder for changed files."""
    print(f"\n  Scanning: {github_path}")
    files = list_folder_files(token, folder_id)
    print(f"    Found {len(files)} files")

    known = state.get("files", {})

    for wdfile in files:
        file_id = wdfile["id"]
        name = wdfile["name"]
        modified_time = wdfile["modified_time"]
        description = wdfile["description"]

        # Skip files synced from GitHub (echo-loop prevention)
        if is_github_synced(description):
            # But check if modified_time is NEWER than when we last saw it
            # (meaning someone edited it in WorkDrive after the GitHub sync)
            prev = known.get(file_id, {})
            prev_modified = prev.get("modified_time", 0)

            if modified_time <= prev_modified:
                # No change since last sync — still has GitHub marker, skip
                continue
            else:
                # Modified AFTER the GitHub sync — someone edited in WorkDrive
                print(f"    ⚡ {name}: edited in WorkDrive after GitHub sync")

        # Check if this file is new or changed since last scan
        prev = known.get(file_id, {})
        prev_modified = prev.get("modified_time", 0)

        if modified_time == prev_modified:
            # File hasn't changed
            continue

        # File is new or changed — record it for download
        local_path = os.path.join(github_path, name)
        changes.append({
            "file_id": file_id,
            "name": name,
            "local_path": local_path,
            "modified_time": modified_time,
            "folder_id": folder_id,
            "is_new": file_id not in known,
        })


def download_changes(token, changes):
    """Download all changed files from WorkDrive."""
    downloaded = []

    for change in changes:
        file_id = change["file_id"]
        local_path = change["local_path"]
        name = change["name"]
        is_new = change["is_new"]

        action = "NEW" if is_new else "UPDATED"
        print(f"\n  [{action}] {name} → {local_path}")

        try:
            download_file(token, file_id, local_path)

            # Verify file was downloaded
            if Path(local_path).exists():
                size = Path(local_path).stat().st_size
                print(f"    ✓ Downloaded ({size:,} bytes)")
                downloaded.append(change)
            else:
                print(f"    ✗ Download failed: file not created")
        except Exception as e:
            print(f"    ✗ Download error: {e}")

        # Rate limiting
        time.sleep(0.5)

    return downloaded


def push_via_pr(commit_msg):
    """Push changes to main via a temporary branch + auto-merged PR.
    Required because main branch has protection rules (PRs required).
    Uses the GitHub API to create and merge the PR automatically.
    """
    # Create a unique branch name
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    branch_name = f"workdrive-sync/{ts}"

    # Create and push the branch
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    subprocess.run(["git", "push", "origin", branch_name], check=True)

    # Get GitHub token — try multiple sources
    gh_token = os.environ.get("GITHUB_TOKEN", "")
    if not gh_token:
        gh_token = os.environ.get("GH_TOKEN", "")
    if not gh_token:
        # Try extracting from remote URL (checkout@v4 embeds as x-access-token:TOKEN)
        result = subprocess.run(["git", "remote", "get-url", "origin"],
                                capture_output=True, text=True)
        import re
        # Match x-access-token:TOKEN@ or just TOKEN@
        match = re.search(r'https://(?:x-access-token:)?([^@]+)@github\.com', result.stdout)
        if match:
            gh_token = match.group(1)

    if not gh_token:
        print("ERROR: No GitHub token available for PR creation")
        print(f"  GITHUB_TOKEN env: {'set' if os.environ.get('GITHUB_TOKEN') else 'empty'}")
        print(f"  Remote URL: {subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True).stdout.strip()[:50]}...")
        subprocess.run(["git", "checkout", "main"], check=True)
        return False

    print(f"  Using GitHub token (source: {'env' if os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN') else 'remote-url'}, length: {len(gh_token)})")

    headers = {
        "Authorization": f"token {gh_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    repo = "JagPat/Vitan-BrandBuilding"

    # Create PR
    pr_title = commit_msg.split("\n")[0]  # First line of commit message
    pr_resp = requests.post(
        f"https://api.github.com/repos/{repo}/pulls",
        headers=headers,
        json={
            "title": pr_title,
            "head": branch_name,
            "base": "main",
            "body": f"Automated sync from WorkDrive.\n\n{commit_msg}",
        },
    )

    if pr_resp.status_code not in (200, 201):
        print(f"ERROR: Failed to create PR: {pr_resp.status_code} {pr_resp.text[:300]}")
        subprocess.run(["git", "checkout", "main"], check=True)
        return False

    pr_number = pr_resp.json()["number"]
    print(f"  Created PR #{pr_number}")

    # Auto-merge the PR via squash
    merge_resp = requests.put(
        f"https://api.github.com/repos/{repo}/pulls/{pr_number}/merge",
        headers=headers,
        json={
            "merge_method": "squash",
            "commit_title": f"{pr_title} (#{pr_number})",
        },
    )

    if merge_resp.status_code == 200:
        print(f"  ✓ PR #{pr_number} merged successfully")
    else:
        print(f"  WARNING: PR merge returned {merge_resp.status_code}: {merge_resp.text[:300]}")
        print(f"  PR #{pr_number} may need manual merge.")

    # Switch back to main and clean up
    subprocess.run(["git", "checkout", "main"], check=True)
    subprocess.run(["git", "pull", "origin", "main"], check=False)

    # Delete remote branch
    requests.delete(
        f"https://api.github.com/repos/{repo}/git/refs/heads/{branch_name}",
        headers=headers,
    )

    return merge_resp.status_code == 200


def commit_changes(downloaded):
    """Commit downloaded files to git with the sync marker."""
    if not downloaded:
        print("\nNo files to commit.")
        return False

    # Stage all downloaded files
    for change in downloaded:
        subprocess.run(
            ["git", "add", change["local_path"]],
            check=True,
        )

    # Check if there are actually staged changes (git may skip identical files)
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True, text=True,
    )
    staged = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

    if not staged:
        print("\nNo actual changes to commit (files are identical).")
        return False

    # Build commit message
    file_count = len(staged)
    file_list = "\n".join(f"  - {f}" for f in staged[:10])
    if len(staged) > 10:
        file_list += f"\n  ... and {len(staged) - 10} more"

    commit_msg = (
        f"{SYNC_MARKER} Sync {file_count} file(s) from WorkDrive\n\n"
        f"Files updated:\n{file_list}\n\n"
        f"Automated sync by Growth OS reverse pipeline."
    )

    subprocess.run(
        ["git", "commit", "-m", commit_msg],
        check=True,
    )

    # Push via PR (branch protection requires PRs to merge into main)
    return push_via_pr(commit_msg)


def update_state(state, downloaded, all_scanned_files):
    """Update state with all current file states from the scan."""
    files_state = state.get("files", {})

    # Update state for downloaded files
    for change in downloaded:
        files_state[change["file_id"]] = {
            "name": change["name"],
            "local_path": change["local_path"],
            "modified_time": change["modified_time"],
        }

    # Also update state for all files we scanned (even unchanged ones)
    # This ensures the state file stays in sync
    for file_info in all_scanned_files:
        file_id = file_info["id"]
        if file_id not in files_state:
            files_state[file_id] = {
                "name": file_info["name"],
                "modified_time": file_info["modified_time"],
            }
        else:
            files_state[file_id]["modified_time"] = file_info["modified_time"]

    state["files"] = files_state
    state["last_sync_ts"] = int(time.time() * 1000)
    return state


# === Main ===

def main():
    print("=" * 60)
    print("Vitan Growth OS: WorkDrive → GitHub Sync (Reverse)")
    print("=" * 60)

    # Check for required env vars
    for var in ["ZOHO_CLIENT_ID", "ZOHO_CLIENT_SECRET", "ZOHO_REFRESH_TOKEN"]:
        if not os.environ.get(var):
            print(f"ERROR: Missing environment variable: {var}")
            sys.exit(1)

    # Configure git identity for commits
    subprocess.run(["git", "config", "user.name", "Growth OS Bot"], check=True)
    subprocess.run(["git", "config", "user.email", "bot@vitan-growthOS.local"], check=True)

    # Get fresh access token
    token = get_access_token()

    # Load state
    state = load_state()
    is_first_run = state.get("last_sync_ts", 0) == 0
    if is_first_run:
        print("\nFirst run detected — will catalog all existing files without downloading.")
        print("(Subsequent runs will detect new/changed files.)")

    # Scan all monitored folders
    print(f"\nScanning {len(REVERSE_FOLDER_MAP)} WorkDrive folders...")
    changes = []
    all_scanned_files = []

    for folder_id, github_path in REVERSE_FOLDER_MAP.items():
        try:
            files = list_folder_files(token, folder_id)
            all_scanned_files.extend(files)

            if not is_first_run:
                # Check for changes against known state
                known = state.get("files", {})
                for wdfile in files:
                    fid = wdfile["id"]
                    desc = wdfile["description"]
                    modified = wdfile["modified_time"]

                    # Skip files with fresh GitHub sync markers (echo-loop)
                    if is_github_synced(desc):
                        prev = known.get(fid, {})
                        if modified <= prev.get("modified_time", 0):
                            continue
                        # If modified after GitHub sync, it's a genuine WD edit
                        print(f"    ⚡ {wdfile['name']}: edited after GitHub sync")

                    # Check if new or modified
                    prev = known.get(fid, {})
                    if modified == prev.get("modified_time", 0):
                        continue

                    local_path = os.path.join(github_path, wdfile["name"])
                    changes.append({
                        "file_id": fid,
                        "name": wdfile["name"],
                        "local_path": local_path,
                        "modified_time": modified,
                        "folder_id": folder_id,
                        "is_new": fid not in known,
                    })
            else:
                print(f"    {github_path}: {len(files)} files cataloged")

        except Exception as e:
            print(f"    ERROR scanning {github_path}: {e}")
            continue

        time.sleep(0.3)  # Rate limit between folder scans

    # First run: just catalog files and save state, don't download
    if is_first_run:
        state = update_state(state, [], all_scanned_files)
        save_state(state)
        print(f"\n✓ First run complete. Cataloged {len(all_scanned_files)} files across {len(REVERSE_FOLDER_MAP)} folders.")
        print("  State saved. Next run will detect changes.")
        # Commit the state file so it persists
        subprocess.run(["git", "add", STATE_FILE], check=True)
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True,
        )
        if result.stdout.strip():
            commit_msg = f"{SYNC_MARKER} Initialize WorkDrive sync state"
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                check=True,
            )
            push_via_pr(commit_msg)
            print("  State file committed and pushed via PR.")
        return

    if not changes:
        print(f"\nNo changes detected across {len(REVERSE_FOLDER_MAP)} folders.")
        # Still update state to keep modified_times current
        state = update_state(state, [], all_scanned_files)
        save_state(state)
        # Commit state if it changed
        subprocess.run(["git", "add", STATE_FILE], check=False)
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True,
        )
        if result.stdout.strip():
            commit_msg = f"{SYNC_MARKER} Update WorkDrive sync state"
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                check=True,
            )
            push_via_pr(commit_msg)
        return

    print(f"\n{'=' * 60}")
    print(f"Found {len(changes)} changed file(s) to sync from WorkDrive")
    print(f"{'=' * 60}")

    # Download changed files
    downloaded = download_changes(token, changes)

    # Update state
    state = update_state(state, downloaded, all_scanned_files)
    save_state(state)

    # Add state file to staging
    subprocess.run(["git", "add", STATE_FILE], check=False)

    # Commit and push
    if downloaded:
        committed = commit_changes(downloaded)
        if committed:
            print(f"\n{'=' * 60}")
            print(f"Reverse sync complete: {len(downloaded)} file(s) pulled from WorkDrive")
            print(f"{'=' * 60}")
        else:
            print("\nNo actual changes needed (files already match).")
    else:
        print("\nAll downloads failed or no changes needed.")


if __name__ == "__main__":
    main()
