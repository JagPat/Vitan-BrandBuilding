#!/usr/bin/env python3
"""Generate branded HTML Google Business Profile review request emails."""

from __future__ import annotations

import argparse
import html
from pathlib import Path

from branded_content_utils import (
    CONTACT_DETAILS,
    SOCIAL_LINKS,
    artifact_name,
    choose_feature_images,
    ensure_output_dir,
    image_to_data_uri,
    load_contact,
    logo_path,
    select_project_for_contact,
)


def build_review_email_html(contact_id: str, explicit_project: str | None = None) -> tuple[str, str]:
    contact = load_contact(contact_id)
    project = select_project_for_contact(contact, explicit_project)
    
    try:
        hero_image, _ = choose_feature_images(project["display"])
    except (FileNotFoundError, ValueError):
        hero_image = logo_path(200)

    logo_uri = image_to_data_uri(logo_path(48))
    hero_uri = image_to_data_uri(hero_image)

    # Use the proposed updated business name
    business_name = "Vitan Architects"
    review_link = "https://g.page/r/CU9qP-G9z6hEEAg/review"
    
    subject = f"Strengthening {business_name}’s Digital Presence – Your Feedback Matters"
    greeting_name = contact.name.split()[0] if contact.name else "there"

    social_html = " &nbsp;|&nbsp; ".join(
        f'<a href="{html.escape(url)}" style="color:#D42B2B;text-decoration:none;font-weight:600;">{html.escape(label)}</a>'
        for label, url in SOCIAL_LINKS.items()
    )

    body = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(subject)}</title>
  </head>
  <body style="margin:0;padding:0;background:#F2F0EC;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#F2F0EC;margin:0;padding:24px 0;">
      <tr>
        <td align="center">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:680px;background:#FFFFFF;border-collapse:collapse;font-family:Arial,sans-serif;color:#1A1A1A;">
            <tr>
              <td style="background:#1A1A1A;padding:24px 32px;">
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
                  <tr>
                    <td align="left" valign="middle">
                      <img src="{logo_uri}" alt="{business_name} logo" width="48" height="48" style="display:block;border:0;">
                    </td>
                    <td align="right" valign="middle" style="color:#F5F5F3;">
                      <div style="font-size:20px;font-weight:700;letter-spacing:0.4px;">{business_name}</div>
                      <div style="font-size:12px;line-height:1.5;letter-spacing:1px;text-transform:uppercase;color:#D8D5CF;">{html.escape(CONTACT_DETAILS['tagline'])}</div>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td>
                <img src="{hero_uri}" alt="{html.escape(project['display'])}" width="680" style="display:block;width:100%;max-width:680px;height:auto;border:0;">
              </td>
            </tr>
            <tr>
              <td style="padding:32px;">
                <h1 style="margin:0 0 16px;font-size:24px;line-height:1.2;color:#1A1A1A;">A brief favor for {business_name}</h1>
                <p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:#4A4A4A;">Dear {html.escape(greeting_name)},</p>
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">It has been a privilege working with {html.escape(contact.company)} on <strong style="color:#1A1A1A;">{html.escape(project['display'])}</strong>. At {business_name}, we are currently focusing on strengthening our digital presence to better reflect the scale and quality of the projects we deliver with partners like you.</p>
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">Google reviews have become a key way for new partners to discover our work and our commitment to "Adding life, every square foot." If you have a moment, we would greatly appreciate it if you could share a brief review of your experience working with Ar. Jagrut Patel and the Vitan team.</p>
                
                <table role="presentation" cellspacing="0" cellpadding="0" style="margin:28px 0;">
                  <tr>
                    <td bgcolor="#D42B2B" style="border-radius:2px;">
                      <a href="{review_link}" style="display:inline-block;padding:16px 24px;font-size:14px;line-height:1;font-weight:700;letter-spacing:0.4px;color:#FFFFFF;text-decoration:none;">Leave a Review</a>
                    </td>
                  </tr>
                </table>

                <p style="margin:0;font-size:15px;line-height:1.8;color:#4A4A4A;">
                  Thank you for your continued trust and partnership.<br><br>
                  Best regards,<br>
                  <strong style="color:#1A1A1A;">Jagrut Patel</strong><br>
                  Founder & Principal Architect, {business_name}<br>
                  {html.escape(CONTACT_DETAILS['address'])}
                </p>
              </td>
            </tr>
            <tr>
              <td style="padding:20px 32px;background:#F8F6F1;border-top:1px solid #E4DED3;">
                <div style="font-size:13px;line-height:1.8;color:#4A4A4A;margin-bottom:10px;">{social_html}</div>
                <div style="font-size:12px;line-height:1.7;color:#6B655C;">
                  Website: <a href="{html.escape(SOCIAL_LINKS['Website'])}" style="color:#1A1A1A;text-decoration:none;">{html.escape(SOCIAL_LINKS['Website'])}</a>
                </div>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
"""
    return subject, body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contact_id", help="VIT contact identifier, for example VIT-C-001")
    parser.add_argument("--project", help="Optional explicit project name override")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional output directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    contact = load_contact(args.contact_id)
    output_dir = ensure_output_dir(args.output_dir)
    subject, email_html = build_review_email_html(args.contact_id, args.project)
    output_path = output_dir / artifact_name(contact, "review-request", "html")
    output_path.write_text(email_html, encoding="utf-8")
    print(f"Generated {output_path}")
    print(f"Subject: {subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
