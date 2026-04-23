#!/usr/bin/env python3
"""Generate personalized Stage 1 outreach email for CEPT University."""

from __future__ import annotations

import html
from pathlib import Path
import sys

# Add scripts directory to path to import branded_content_utils
sys.path.append(str(Path(__file__).resolve().parent))

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

# Custom content mapping for CEPT
TARGET_CONTENT = {
    "VIT-C-019": {  # Sachin Soni
        "project": "ARA",
        "angle": "Bridging Heritage Sensitivity with Technical Rigor.",
        "hook": "The Sankdi Sheri Heritage project is a brilliant model for Ahmedabad’s urban renewal. At Vitan, we deeply respect this balance—where the preservation of a facade meets the demands of modern mobility. Having delivered 100+ projects in Gujarat, including institutional landmarks like the Ahmedabad Racquet Academy, we believe there is a unique bridge between CEPT’s research-led vision and Vitan’s execution-first approach."
    },
    "VIT-C-024": {  # Barjor Mehta
        "project": "ARA",
        "angle": "Strategic Execution for Gujarat's Institutional Landmarks.",
        "hook": "Under your leadership, CEPT continues to define the architectural discourse in India. As Ahmedabad pivots toward massive vertical and institutional transformation, Vitan offers 35 years of 'Ahmedabad Intimacy.' We see a strategic alignment in translating high-level urban research into executable, performance-led landmarks."
    },
}

def build_personalized_email_html(contact_id: str) -> tuple[str, str]:
    target_info = TARGET_CONTENT.get(contact_id)
    if not target_info:
        raise ValueError(f"No personalized content for {contact_id}")

    contact = load_contact(contact_id)
    project_meta = select_project_for_contact(contact, target_info["project"])
    hero_image, _ = choose_feature_images(project_meta["display"])

    logo_uri = image_to_data_uri(logo_path(48))
    hero_uri = image_to_data_uri(hero_image)

    if contact_id == "VIT-C-019":
        subject = f"Heritage vs Rigor: A conversation with Vitan Architects"
    else:
        subject = f"Institutional Transformation in Ahmedabad | Vitan x CEPT"

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
                <img src="{hero_uri}" alt="{html.escape(project_meta['display'])}" width="680" style="display:block;width:100%;max-width:680px;height:auto;border:0;">
              </td>
            </tr>
            <tr>
              <td style="padding:32px;">
                <div style="font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#D42B2B;font-weight:700;margin-bottom:12px;">Stage 1 Outreach: {html.escape(contact.company)}</div>
                <h1 style="margin:0 0 16px;font-size:30px;line-height:1.2;color:#1A1A1A;">{target_info['angle']}</h1>
                <p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:#4A4A4A;">Hi {html.escape(greeting_name)},</p>
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">{target_info['hook']}</p>
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">Vitan Architects views institutional design as a commitment to <strong style="color:#1A1A1A;">Operational Survival</strong>. Our 35 years in Ahmedabad have proven that great design must be backed by technical mastery to ensure landmarks remain vibrant and high-performing for generations.</p>
                
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="margin:18px 0 24px;background:#F8F6F1;border-left:4px solid #D42B2B;">
                  <tr>
                    <td style="padding:18px 20px;">
                      <div style="font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:#D42B2B;font-weight:700;margin-bottom:8px;">Vitan Reference: {html.escape(project_meta['display'])}</div>
                      <div style="font-size:14px;line-height:1.6;color:#4A4A4A;">{html.escape(project_meta['description'])}</div>
                    </td>
                  </tr>
                </table>
                
                <p style="margin:0 0 22px;font-size:15px;line-height:1.8;color:#4A4A4A;">I would welcome the opportunity to discuss how Vitan can support CEPT’s upcoming initiatives.</p>
                
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

def main():
    output_dir = ensure_output_dir(Path("Business development/shared-workspace/review/VITA-560"))
    for contact_id in TARGET_CONTENT.keys():
        try:
            subject, email_html = build_personalized_email_html(contact_id)
            contact = load_contact(contact_id)
            output_path = output_dir / artifact_name(contact, "stage1-personalized", "html")
            output_path.write_text(email_html, encoding="utf-8")
            print(f"Generated {output_path} (Subject: {subject})")
        except Exception as e:
            print(f"Failed to generate for {contact_id}: {e}")

if __name__ == "__main__":
    main()
