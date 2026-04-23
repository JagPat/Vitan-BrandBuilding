#!/usr/bin/env python3
"""Generate personalized Stage 1 outreach emails for the 2026 Skyscraper & Luxury Wave."""

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

# Custom content mapping for the 10 targets
TARGET_CONTENT = {
    "VIT-C-009": {  # Rajyash Group
        "project": "PARIJAAT ECLAT",
        "angle": "Acknowledge your 'Royce One' achievement. Vitan brings experience in high-density, high-design luxury to complement your vertical ambitions.",
        "hook": "Your work on Royce One has set a new benchmark for Ahmedabad's skyline. As you scale these vertical ambitions, Vitan’s integrated design-to-execution framework can ensure 10-15% faster delivery while protecting the ultra-luxury design intent."
    },
    "VIT-C-010": {  # NB Group
        "project": "PARIJAAT ECLAT",
        "angle": "Align with your commitment to IGBC-certified green building. Vitan's eco-sensitive approach and diamond-industry precision is a perfect match.",
        "hook": "We've been following the progress of NB Palm and your commitment to IGBC-certified green luxury. Vitan’s 'Profit Centre' model is designed for developers who, like NB Group, value internal accrual efficiency and precision-led execution."
    },
    "VIT-C-011": {  # Sahashya Group
        "project": "PARIJAAT ECLAT",
        "angle": "Position Vitan as a peer in ultra-high-rise residential design, aligning with your 'spaces that breathe' philosophy.",
        "hook": "Skyzenia is a magnificent addition to the Science City skyline. Vitan’s design philosophy of 'Adding Life' aligns perfectly with your vision of 'spaces that breathe,' offering the technical mastery needed for 40+ floor complexity."
    },
    "VIT-C-012": {  # K K Group
        "project": "PARIJAAT ECLAT",
        "angle": "Position Vitan as the expert in the ultra-luxury 'Sky Villa' segment, ensuring execution clarity to avoid vendor friction.",
        "hook": "The Camellia represents a sophisticated shift in Ahmedabad’s sky-villa segment. Vitan’s integrated execution framework ensures the kind of documentation clarity that eliminates site friction and protects your capital investment."
    },
    "VIT-C-013": {  # Adani Realty
        "project": "SEVENTY",
        "angle": "Echo values of eco-friendly design and worker-first site management. Vitan's experience in scaling corporate-grade townships matches your ambitions.",
        "hook": "Your focus on sustainability and worker welfare at Adani Amaris reflects a values-driven approach we deeply respect. Having scaled major townships like Applewoods, Vitan brings the institutional rigor needed to deliver Adani’s vision of sustainable luxury."
    },
    "VIT-C-014": {  # Bakeri Group
        "project": "PARIJAAT ECLAT",
        "angle": "Reference the deep shared history of landmarking Ahmedabad together. Focus on 'next-generation' collaboration for smart-city challenges.",
        "hook": "From the Sakar series to Gyankunj, our shared history is woven into the fabric of Ahmedabad. As you scale new smart-city challenges like Stella in GIFT City, Vitan’s evolved 'e-Architecting' approach is ready to deliver the next generation of Bakeri landmarks."
    },
    "VIT-C-015": {  # Navratna Group
        "project": "SEVENTY",
        "angle": "Technical Optimization for Ultra-High-Rise. Engineer-to-Engineer communication.",
        "hook": "Building Gujarat’s tallest skyscraper at Iskcon Circle is a historic milestone. As engineers yourself, you recognize that 162m introduces unprecedented execution complexity. Vitan can act as your 'Execution Specialist' to ensure the technical precision such a landmark demands."
    },
    "VIT-C-016": {  # Anjey Maruti Group
        "project": "PARIJAAT ECLAT",
        "angle": "Pitch on 'identity + execution clarity' to differentiate from aesthetic-heavy approaches.",
        "hook": "Maruti 360 is set to be a landmark for the group. In the ultra-luxury segment, Vitan differentiates by bridging the gap between high-end aesthetics and execution clarity, ensuring 10-15% savings on project delivery costs."
    },
    "VIT-C-017": {  # Zade Group
        "project": "PARIJAAT ECLAT",
        "angle": "High potential for a long-term partnership as you scale your 'Z' brand in Thaltej.",
        "hook": "Your rapid expansion with the Z brand in Thaltej is impressive. Vitan’s 'Profit Centre' model is specifically built to support developers as they scale, ensuring brand identity remains consistent across increasingly complex vertical projects."
    },
    "VIT-C-018": {  # Sri Lotus Developers
        "project": "SEVENTY",
        "angle": "Bridge the gap between 'Mumbai Vision' and 'Gujarat Execution' for high-prestige projects.",
        "hook": "Bringing a 1 million sq. ft. 'Vertical City' to GIFT City is a bold move. Vitan can position as your local 'Lead Design Consultant,' bringing the institutional-grade documentation and local regulatory mastery needed to realize such a high-prestige vision."
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

    subject = f"Vitan Architects x {contact.company} | {target_info['angle'][:50]}..."
    if contact_id == "VIT-C-014": # Bakeri
        subject = f"Next-generation collaboration: Vitan x Bakeri Group"
    elif contact_id == "VIT-C-015": # Navratna
        subject = f"Technical Execution for Iskcon Circle Skyscraper"
    elif contact_id == "VIT-C-018": # Sri Lotus
        subject = f"Realizing the GIFT City 'Vertical City' vision"
    else:
        subject = f"Peer-level execution for {contact.company}'s 2026 milestones"

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
                <p style="margin:0 0 18px;font-size:15px;line-height:1.8;color:#4A4A4A;">We view architecture not just as design, but as a <strong style="color:#1A1A1A;">Profit Centre</strong>. Vitan’s 35 years of experience in Ahmedabad has proven that structured design-to-execution workflows can save developers 10-15% on overall costs while elevating the landmark status of the project.</p>
                
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="margin:18px 0 24px;background:#F8F6F1;border-left:4px solid #D42B2B;">
                  <tr>
                    <td style="padding:18px 20px;">
                      <div style="font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:#D42B2B;font-weight:700;margin-bottom:8px;">Vitan Reference: {html.escape(project_meta['display'])}</div>
                      <div style="font-size:14px;line-height:1.6;color:#4A4A4A;">{html.escape(project_meta['description'])}</div>
                    </td>
                  </tr>
                </table>
                
                <p style="margin:0 0 22px;font-size:15px;line-height:1.8;color:#4A4A4A;">If you're open to it, I’d like to share how we would map this execution rigor to an upcoming project at {html.escape(contact.company)}.</p>
                
                <table role="presentation" cellspacing="0" cellpadding="0" style="margin-bottom:28px;">
                  <tr>
                    <td bgcolor="#D42B2B" style="border-radius:2px;">
                      <a href="tel:{html.escape(CONTACT_DETAILS['mobile'].replace(' ', ''))}" style="display:inline-block;padding:14px 22px;font-size:14px;line-height:1;font-weight:700;letter-spacing:0.4px;color:#FFFFFF;text-decoration:none;">Book a Studio Visit</a>
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
    output_dir = ensure_output_dir(Path("Business development/shared-workspace/review/VITA-595"))
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
