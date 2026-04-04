#!/usr/bin/env python3
"""Generate branded one-page PDFs with real Vitan images and logo assets."""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

from branded_content_utils import (
    CONTACT_DETAILS,
    SOCIAL_LINKS,
    artifact_name,
    choose_feature_images,
    ensure_output_dir,
    load_contact,
    logo_path,
    project_metadata,
)


def dependency_error(exc: Exception) -> int:
    print(
        "Missing PDF generation dependency. Install reportlab and Pillow in the target runtime "
        f"before using this script. Details: {exc}",
        file=sys.stderr,
    )
    return 2


def fit_box(src_width: float, src_height: float, box_x: float, box_y: float, box_w: float, box_h: float) -> tuple[float, float, float, float]:
    scale = min(box_w / src_width, box_h / src_height)
    draw_w = src_width * scale
    draw_h = src_height * scale
    draw_x = box_x + (box_w - draw_w) / 2
    draw_y = box_y + (box_h - draw_h) / 2
    return draw_x, draw_y, draw_w, draw_h


def render_pdf(contact_id: str, project_name: str, output_dir: Path | None = None) -> Path:
    try:
        from PIL import Image
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfgen import canvas
    except Exception as exc:  # pragma: no cover - runtime dependency branch
        raise RuntimeError(exc) from exc

    contact = load_contact(contact_id)
    project = project_metadata(project_name)
    hero_image_path, secondary_image_path = choose_feature_images(project_name)
    output_root = ensure_output_dir(output_dir)
    output_path = output_root / artifact_name(contact, f"{project_name.lower().replace(' ', '-')}-brochure", "pdf")

    page_w, page_h = A4
    doc = canvas.Canvas(str(output_path), pagesize=A4)
    margin = 36

    def pil_reader(path: Path, *, preserve_alpha: bool = False) -> ImageReader:
        image = Image.open(path)
        if preserve_alpha and image.mode == "RGBA":
            output_image = image
        else:
            output_image = image.convert("RGB")
        output_image.thumbnail((1800, 1800))
        buffer = io.BytesIO()
        if preserve_alpha and output_image.mode == "RGBA":
            output_image.save(buffer, format="PNG", optimize=True)
        else:
            output_image.save(buffer, format="JPEG", quality=82, optimize=True)
        buffer.seek(0)
        return ImageReader(buffer)

    logo_reader = pil_reader(logo_path(200), preserve_alpha=True)
    hero_reader = pil_reader(hero_image_path)
    secondary_reader = pil_reader(secondary_image_path)

    hero_width, hero_height = hero_reader.getSize()
    secondary_width, secondary_height = secondary_reader.getSize()

    doc.setFillColor(colors.HexColor("#F5F5F3"))
    doc.rect(0, 0, page_w, page_h, fill=1, stroke=0)
    doc.setFillColor(colors.HexColor("#D42B2B"))
    doc.rect(0, page_h - 10, page_w, 10, fill=1, stroke=0)

    doc.drawImage(logo_reader, margin, page_h - 88, width=56, height=56, mask="auto")
    doc.setFillColor(colors.HexColor("#1A1A1A"))
    doc.setFont("Helvetica-Bold", 20)
    doc.drawString(margin + 70, page_h - 52, "Vitan Architects")
    doc.setFillColor(colors.HexColor("#4A4A4A"))
    doc.setFont("Helvetica", 10)
    doc.drawString(margin + 70, page_h - 68, CONTACT_DETAILS["tagline"])
    doc.setFont("Helvetica-Bold", 11)
    doc.setFillColor(colors.HexColor("#D42B2B"))
    doc.drawRightString(page_w - margin, page_h - 52, f"Prepared for {contact.company}")
    doc.setFillColor(colors.HexColor("#4A4A4A"))
    doc.setFont("Helvetica", 9)
    doc.drawRightString(page_w - margin, page_h - 68, f"{contact.name} | {contact.title}")

    hero_box = (margin, page_h - 340, page_w - (margin * 2), 210)
    doc.setFillColor(colors.white)
    doc.roundRect(hero_box[0], hero_box[1], hero_box[2], hero_box[3], 10, fill=1, stroke=0)
    draw_x, draw_y, draw_w, draw_h = fit_box(hero_width, hero_height, *hero_box)
    doc.drawImage(hero_reader, draw_x, draw_y, width=draw_w, height=draw_h, mask="auto")

    stats_y = page_h - 400
    doc.setFillColor(colors.HexColor("#1A1A1A"))
    doc.roundRect(margin, stats_y, page_w - (margin * 2), 54, 8, fill=1, stroke=0)
    stat_labels = ("Location", "Type", "Area", "Year")
    stat_values = (project["location"], project["type"], project["area"], project["year"])
    col_w = (page_w - (margin * 2)) / 4
    for index, (label, value) in enumerate(zip(stat_labels, stat_values)):
        x = margin + (col_w * index) + 12
        doc.setFillColor(colors.HexColor("#D42B2B"))
        doc.setFont("Helvetica-Bold", 8)
        doc.drawString(x, stats_y + 36, label.upper())
        doc.setFillColor(colors.HexColor("#F5F5F3"))
        doc.setFont("Helvetica", 10)
        doc.drawString(x, stats_y + 18, value)

    body_top = stats_y - 20
    doc.setFillColor(colors.HexColor("#1A1A1A"))
    doc.setFont("Helvetica-Bold", 22)
    doc.drawString(margin, body_top, project["display"])
    doc.setFillColor(colors.HexColor("#4A4A4A"))
    doc.setFont("Helvetica", 11)
    doc.drawString(margin, body_top - 16, f"Relevant for {contact.company}'s {contact.sector} pipeline")

    text_box_w = 280
    text = doc.beginText(margin, body_top - 46)
    text.setFont("Helvetica", 11)
    text.setFillColor(colors.HexColor("#4A4A4A"))
    for line in (
        project["description"],
        "",
        f"Contact route: {contact.email_primary or contact.email_fallback or 'Manual outreach'}",
        f"LinkedIn: {contact.linkedin or 'Not listed'}",
        "",
        "This one-pager is intended as a fast visual reference for founder-led outreach.",
    ):
        for wrapped in wrap_line(line, 62):
            text.textLine(wrapped)
    doc.drawText(text)

    secondary_box = (page_w - margin - 220, body_top - 182, 220, 150)
    doc.setFillColor(colors.white)
    doc.roundRect(secondary_box[0], secondary_box[1], secondary_box[2], secondary_box[3], 8, fill=1, stroke=0)
    draw_x, draw_y, draw_w, draw_h = fit_box(secondary_width, secondary_height, *secondary_box)
    doc.drawImage(secondary_reader, draw_x, draw_y, width=draw_w, height=draw_h, mask="auto")

    footer_y = 46
    doc.setStrokeColor(colors.HexColor("#D9D2C6"))
    doc.line(margin, footer_y + 26, page_w - margin, footer_y + 26)
    doc.setFillColor(colors.HexColor("#4A4A4A"))
    doc.setFont("Helvetica", 8.5)
    social_text = " | ".join(f"{label}: {url}" for label, url in SOCIAL_LINKS.items())
    doc.drawString(margin, footer_y + 10, social_text)
    doc.drawString(
        margin,
        footer_y - 2,
        f"{CONTACT_DETAILS['address']} | {CONTACT_DETAILS['mobile']} | {CONTACT_DETAILS['office']}",
    )

    doc.showPage()
    doc.save()
    return output_path


def wrap_line(text: str, width: int) -> list[str]:
    if not text:
        return [""]
    words = text.split()
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        probe = f"{current} {word}"
        if len(probe) <= width:
            current = probe
            continue
        lines.append(current)
        current = word
    lines.append(current)
    return lines


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contact_id", help="VIT contact identifier, for example VIT-C-001")
    parser.add_argument("project_name", help="Project name or alias, for example 'Privilon'")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional output directory. Defaults to Business development/shared-workspace/review/vita189",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output_path = render_pdf(args.contact_id, args.project_name, args.output_dir)
    except RuntimeError as exc:
        return dependency_error(exc)
    print(f"Generated {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
