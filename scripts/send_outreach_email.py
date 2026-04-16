#!/usr/bin/env python3
"""Send branded HTML outreach emails via Zoho SMTP."""

import argparse
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

def send_email(to_email, subject, html_content):
    host = os.environ.get("ZOHO_SMTP_HOST", "smtp.zoho.in")
    port = int(os.environ.get("ZOHO_SMTP_PORT", 465))
    user = os.environ.get("ZOHO_SMTP_USER")
    password = os.environ.get("ZOHO_SMTP_PASS")
    sender = user # Usually jp@vitan.in

    if not all([user, password]):
        print("Error: SMTP credentials not found in environment.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Chitrang (Vitan Architects) <{sender}>"
    msg["To"] = to_email
    msg["Reply-To"] = "connect@vitan.in"

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL(host, port) as server:
            server.login(user, password)
            server.send_message(msg)
        print(f"Successfully sent email to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Send branded outreach email.")
    parser.add_argument("to_email", help="Recipient email address")
    parser.add_argument("subject", help="Email subject")
    parser.add_argument("html_file", help="Path to HTML content file")
    
    args = parser.parse_args()
    
    html_path = Path(args.html_file)
    if not html_path.exists():
        print(f"Error: HTML file not found: {args.html_file}")
        return

    html_content = html_path.read_text(encoding="utf-8")
    send_email(args.to_email, args.subject, html_content)

if __name__ == "__main__":
    main()
