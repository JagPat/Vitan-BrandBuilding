#!/usr/bin/env python3
"""Send emails via Zoho Mail API using OAuth2."""

import json
import os
import sys
import requests
from pathlib import Path

def get_access_token():
    token_url = os.environ.get("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.in/oauth/v2/token")
    refresh_token = os.environ.get("ZOHO_MAIL_REFRESH_TOKEN") or os.environ.get("ZOHO_REFRESH_TOKEN")
    client_id = os.environ.get("ZOHO_MAIL_CLIENT_ID") or os.environ.get("ZOHO_CLIENT_ID")
    client_secret = os.environ.get("ZOHO_MAIL_CLIENT_SECRET") or os.environ.get("ZOHO_CLIENT_SECRET")
    
    if not all([refresh_token, client_id, client_secret]):
        raise RuntimeError("Missing Zoho OAuth credentials in environment.")

    print(f"Requesting token from {token_url}...")
    resp = requests.post(
        token_url,
        data={
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
        },
        timeout=60,
    )
    if resp.status_code != 200:
        print(f"Token error: {resp.status_code} {resp.text}")
    resp.raise_for_status()
    print("Token received successfully.")
    return resp.json().get("access_token")

def send_mail_batch(targets):
    """targets: list of (to_email, subject, html_content)"""
    account_id = os.environ.get("ZOHO_MAIL_ACCOUNT_ID")
    from_address = os.environ.get("ZOHO_MAIL_FROM_ADDRESS", "growthos@vitan.in")
    base_url = os.environ.get("ZOHO_MAIL_BASE_URL", "https://mail.zoho.in").rstrip("/")
    
    if not account_id:
        raise RuntimeError("Missing ZOHO_MAIL_ACCOUNT_ID in environment.")

    token = get_access_token()
    url = f"{base_url}/api/accounts/{account_id}/messages"
    
    results = []
    for to_email, subject, html_content in targets:
        payload = {
            "fromAddress": from_address,
            "toAddress": to_email,
            "subject": subject,
            "content": html_content,
            "mailFormat": "html"
        }
        
        print(f"Sending mail to {to_email}...")
        resp = requests.post(
            url,
            headers={
                "Authorization": f"Zoho-oauthtoken {token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        
        if resp.status_code not in (200, 201):
            print(f"Error sending mail to {to_email}: {resp.status_code} {resp.text}")
            results.append(False)
        else:
            print(f"Successfully sent mail to {to_email}")
            results.append(True)
    
    return all(results)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  zoho_mail_send_api.py <to_email> <subject> <html_file>")
        print("  zoho_mail_send_api.py --batch <json_file>")
        sys.exit(1)
        
    if sys.argv[1] == "--batch":
        batch_file = Path(sys.argv[2])
        batch_data = json.loads(batch_file.read_text(encoding="utf-8"))
        targets = []
        for item in batch_data:
            html_content = Path(item["html_file"]).read_text(encoding="utf-8")
            targets.append((item["to_email"], item["subject"], html_content))
        
        if send_mail_batch(targets):
            sys.exit(0)
        else:
            sys.exit(1)
    
    if len(sys.argv) < 4:
        print("Usage: zoho_mail_send_api.py <to_email> <subject> <html_file>")
        sys.exit(1)

    to_email = sys.argv[1]
    subject = sys.argv[2]
    html_file = sys.argv[3]
    
    html_path = Path(html_file)
    if not html_path.exists():
        print(f"Error: HTML file not found: {html_file}")
        sys.exit(1)
        
    html_content = html_path.read_text(encoding="utf-8")
    if send_mail_batch([(to_email, subject, html_content)]):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
