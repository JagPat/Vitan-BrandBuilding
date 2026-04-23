#!/usr/bin/env python3
"""Generate branded HTML outreach emails with real Vitan assets."""

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


def build_email_html(contact_id: str, explicit_project: str | None = None) -> tuple[str, str]:
    contact = load_contact(contact_id)
    project = select_project_for_contact(contact, explicit_project)
    hero_image, _ = choose_feature_images(project["display"])

    logo_uri = image_to_data_uri(logo_path(48))
    hero_uri = image_to_data_uri(hero_image)

    subject = f"Regarding {contact.company}'s vertical projects | Vitan Architects"
    greeting_name = contact.name.split()[0] if contact.name else "there"
    city_line = ", ".join(part for part in (contact.city, contact.state) if part)

    social_html = "".join(
        f'<a href="{html.escape(url)}" style="color:#D42B2B;text-decoration:none;font-weight:600;">{html.escape(label)}</a>'
        for label, url in SOCIAL_LINKS.items()
    )
    social_html = " &nbsp;|&nbsp; ".join(
        f'<a href="{html.escape(url)}" style="color:#D42B2B;text-decoration:none;font-weight:600;">{html.escape(label)}</a>'
        for label, url in SOCIAL_LINKS.items()
    )

    notes_html = ""
    if contact.notes:
        notes_html = (
            '<p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">'
            f'{html.escape(contact.notes)}'
            "</p>"
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
                      <img src="{logo_uri}" alt="Vitan Architects logo" width="48" height="48" style="display:block;border:0;">
                    </td>
                    <td align="right" valign="middle" style="color:#F5F5F3;">
                      <div style="font-size:20px;font-weight:700;letter-spacing:0.4px;">Vitan Architects</div>
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
                <div style="font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#D42B2B;font-weight:700;margin-bottom:12px;">Vertical Excellence in {html.escape(contact.city)}</div>
                <h1 style="margin:0 0 16px;font-size:30px;line-height:1.2;color:#1A1A1A;">{html.escape(project['display'])}: Execution credibility for {html.escape(contact.company)}</h1>
                <p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:#4A4A4A;">Hi {html.escape(greeting_name)},</p>
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">I’m sharing a concise Vitan reference that aligns with {html.escape(contact.company)}’s current vertical trajectory in {html.escape(contact.city)}. <strong style="color:#1A1A1A;">{html.escape(project['display'])}</strong> demonstrates our approach to {html.escape(project['type'].lower())} environments where execution clarity and technical rigor are paramount.</p>
                {notes_html}
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">{html.escape(project['description'])}</p>
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="margin:18px 0 24px;background:#F8F6F1;border-left:4px solid #D42B2B;">
                  <tr>
                    <td style="padding:18px 20px;">
                      <div style="font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:#D42B2B;font-weight:700;margin-bottom:8px;">Project Snapshot</div>
                      <div style="font-size:15px;line-height:1.8;color:#1A1A1A;"><strong>Location:</strong> {html.escape(project['location'])}</div>
                      <div style="font-size:15px;line-height:1.8;color:#1A1A1A;"><strong>Type:</strong> {html.escape(project['type'])}</div>
                      <div style="font-size:15px;line-height:1.8;color:#1A1A1A;"><strong>Why it fits:</strong> Strong relevance for {html.escape(contact.company)}'s {html.escape(contact.sector)} direction.</div>
                    </td>
                  </tr>
                </table>
                <p style="margin:0 0 22px;font-size:15px;line-height:1.8;color:#4A4A4A;">If useful, we can tailor a tighter concept packet around an active opportunity at {html.escape(contact.company)} and map it to the speed, identity, and commercial goals you’re driving.</p>
                <table role="presentation" cellspacing="0" cellpadding="0" style="margin-bottom:28px;">
                  <tr>
                    <td bgcolor="#D42B2B" style="border-radius:2px;">
                      <a href="tel:{html.escape(CONTACT_DETAILS['mobile'].replace(' ', ''))}" style="display:inline-block;padding:14px 22px;font-size:14px;line-height:1;font-weight:700;letter-spacing:0.4px;color:#FFFFFF;text-decoration:none;">Schedule a Meeting</a>
                    </td>
                  </tr>
                </table>
                <p style="margin:0;font-size:15px;line-height:1.8;color:#4A4A4A;">
                  Regards,<br>
                  <strong style="color:#1A1A1A;">Vitan Architects</strong><br>
                  {html.escape(CONTACT_DETAILS['address'])}<br>
                  Mobile: {html.escape(CONTACT_DETAILS['mobile'])} | Office: {html.escape(CONTACT_DETAILS['office'])}
                </p>
              </td>
            </tr>
            <tr>
              <td style="padding:20px 32px;background:#F8F6F1;border-top:1px solid #E4DED3;">
                <div style="font-size:13px;line-height:1.8;color:#4A4A4A;margin-bottom:10px;">{social_html}</div>
                <div style="font-size:12px;line-height:1.7;color:#6B655C;">
                  Website: <a href="{html.escape(SOCIAL_LINKS['Website'])}" style="color:#1A1A1A;text-decoration:none;">{html.escape(SOCIAL_LINKS['Website'])}</a><br>
                  Maps: <a href="{html.escape(CONTACT_DETAILS['maps'])}" style="color:#1A1A1A;text-decoration:none;">{html.escape(CONTACT_DETAILS['address'])}</a>
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
        help="Optional output directory. Defaults to Business development/shared-workspace/review/vita189",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    contact = load_contact(args.contact_id)
    output_dir = ensure_output_dir(args.output_dir)
    subject, email_html = build_email_html(args.contact_id, args.project)
    output_path = output_dir / artifact_name(contact, "branded-email", "html")
    output_path.write_text(email_html, encoding="utf-8")
    print(f"Generated {output_path}")
    print(f"Subject: {subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
