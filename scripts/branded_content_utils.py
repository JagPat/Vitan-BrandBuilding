#!/usr/bin/env python3
"""Shared helpers for branded outreach artifact generation."""

from __future__ import annotations

import base64
import csv
import io
import mimetypes
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BRAND_GUIDE_DIR = REPO_ROOT / "Business development" / "Brand Guide"
PROJECT_PHOTO_DIR = REPO_ROOT / "Business development" / "PHOTOS FOR SAMPLE PROJECT"
SHARED_WORKSPACE_DIR = REPO_ROOT / "Business development" / "shared-workspace"
DEFAULT_OUTPUT_DIR = SHARED_WORKSPACE_DIR / "review" / "VITA-595"
CONTACTS_CSV = SHARED_WORKSPACE_DIR / "contacts-master.csv"

SOCIAL_LINKS = {
    "LinkedIn": "https://in.linkedin.com/company/vitanarchitects",
    "Instagram": "https://www.instagram.com/vitanarchitects/",
    "Facebook": "https://www.facebook.com/jagrutnpartners/",
    "ArchDaily": "https://www.archdaily.com/office/vitan-architects",
    "Website": "https://vitan.in",
}

CONTACT_DETAILS = {
    "tagline": "Adding life, every square foot",
    "address": "702, Hetdev Square, Thaltej, Ahmedabad 380054",
    "mobile": "+91 99250 11639",
    "office": "079 2768 1033",
    "maps": "https://maps.google.com/?q=702+Hetdev+Square+Thaltej+Ahmedabad+380054",
}

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


@dataclass(frozen=True)
class Contact:
    contact_id: str
    company: str
    name: str
    title: str
    city: str
    state: str
    sector: str
    email_primary: str
    email_fallback: str
    linkedin: str
    notes: str
    raw: dict[str, str]


PROJECT_CATALOG: dict[str, dict[str, str]] = {
    "PARIJAAT ECLAT": {
        "folder": "PARIJAAT ECLAT",
        "display": "Parijaat Eclat",
        "location": "Ahmedabad, Gujarat",
        "type": "Residential",
        "area": "Luxury apartment towers",
        "year": "Undisclosed",
        "description": (
            "A premium residential development used to anchor outreach around livability, "
            "high-rise housing identity, and premium buyer positioning."
        ),
    },
    "PRIVILON": {
        "folder": "PRIVILON",
        "display": "Privilon",
        "location": "Ahmedabad, Gujarat",
        "type": "Commercial",
        "area": "Office and retail high-rise",
        "year": "Undisclosed",
        "description": (
            "A commercial tower reference suited to conversations about workplace identity, "
            "retail frontage, and premium mixed-use execution."
        ),
    },
    "SAFAL PARISAR": {
        "folder": "SAFAL PARISAR",
        "display": "Safal Parisar",
        "location": "Ahmedabad, Gujarat",
        "type": "Residential",
        "area": "Urban housing community",
        "year": "Undisclosed",
        "description": (
            "A residential portfolio reference that supports outreach about community-led "
            "planning, daily usability, and delivery discipline."
        ),
    },
    "SAFAL PEGASUS": {
        "folder": "SAFAL PEGASUS",
        "display": "Safal Pegasus",
        "location": "Ahmedabad, Gujarat",
        "type": "Commercial",
        "area": "Premium commercial complex",
        "year": "Undisclosed",
        "description": (
            "A flagship commercial project often used to demonstrate premium frontage, "
            "urban presence, and a polished business environment."
        ),
    },
    "PALLADIUM": {
        "folder": "PALLADIUM",
        "display": "Palladium",
        "location": "Ahmedabad, Gujarat",
        "type": "Commercial",
        "area": "Retail and lifestyle destination",
        "year": "Undisclosed",
        "description": (
            "A retail-led portfolio reference that helps frame destination building, "
            "customer experience, and premium public-facing design."
        ),
    },
    "MERLIN PENTAGON": {
        "folder": "MERLIN PENTAGON",
        "display": "Merlin Pentagon",
        "location": "Kolkata, West Bengal",
        "type": "Commercial",
        "area": "Corporate office development",
        "year": "Undisclosed",
        "description": (
            "A corporate-scale commercial reference that supports positioning around "
            "business-ready environments and sharp architectural expression."
        ),
    },
    "ARA": {
        "folder": "ARA (AHMEDABAD RACQUET ACADEMY)",
        "display": "Ahmedabad Racquet Academy",
        "location": "Ahmedabad, Gujarat",
        "type": "Institutional",
        "area": "Sports campus",
        "year": "Undisclosed",
        "description": (
            "An institutional sports facility reference for conversations that need "
            "community use, activity planning, and operational clarity."
        ),
    },
    "SEVENTY": {
        "folder": "SEVENTY",
        "display": "Seventy",
        "location": "Ahmedabad, Gujarat",
        "type": "Mixed-use",
        "area": "Mixed-format development",
        "year": "Undisclosed",
        "description": (
            "A mixed-use reference that helps frame identity, flexibility, and strong "
            "visual character across different occupier needs."
        ),
    },
    "RETHAL GREENS": {
        "folder": "RETHAL GREENS",
        "display": "Rethal Greens",
        "location": "Ahmedabad, Gujarat",
        "type": "Mixed-use",
        "area": "Landscape-led development",
        "year": "Undisclosed",
        "description": (
            "A landscape-forward project reference that supports outdoor experience, "
            "master planning, and lower-density premium positioning."
        ),
    },
}

# Corrected after VITA-189 issue comment: Parijaat Eclat is residential; Privilon is commercial.
SECTOR_PROJECT_MAP = {
    "residential": ["PARIJAAT ECLAT", "SAFAL PARISAR"],
    "luxury residential": ["PARIJAAT ECLAT"],
    "commercial": ["PRIVILON", "SAFAL PEGASUS", "PALLADIUM", "MERLIN PENTAGON"],
    "institutional": ["ARA"],
    "mixed": ["SEVENTY", "RETHAL GREENS"],
    "mixed-use": ["SEVENTY", "PRIVILON"],
}


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "artifact"


def normalize_project_name(value: str) -> str:
    probe = re.sub(r"[^a-z0-9]+", "", value.lower())
    for key, meta in PROJECT_CATALOG.items():
        aliases = {key, meta["display"], meta["folder"]}
        for alias in aliases:
            if re.sub(r"[^a-z0-9]+", "", alias.lower()) == probe:
                return key
    raise ValueError(f"Unsupported project name: {value}")


def ensure_output_dir(output_dir: Path | None = None) -> Path:
    destination = output_dir or DEFAULT_OUTPUT_DIR
    destination.mkdir(parents=True, exist_ok=True)
    return destination


def load_contact(contact_id: str) -> Contact:
    if not CONTACTS_CSV.exists():
        raise FileNotFoundError(f"Contact sheet not found: {CONTACTS_CSV}")

    with CONTACTS_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if (row.get("Contact ID") or "").strip() != contact_id:
                continue
            return Contact(
                contact_id=contact_id,
                company=(row.get("Company") or "").strip(),
                name=(row.get("Contact Name") or "").strip(),
                title=(row.get("Title / Role") or "").strip(),
                city=(row.get("City") or "").strip(),
                state=(row.get("State") or "").strip(),
                sector=(row.get("Sector") or "").strip().lower(),
                email_primary=(row.get("Email (Primary)") or "").strip(),
                email_fallback=(row.get("Email (Fallback)") or "").strip(),
                linkedin=(row.get("LinkedIn") or "").strip(),
                notes=(row.get("Notes") or "").strip(),
                raw=row,
            )

    raise ValueError(f"Contact ID not found in contacts-master.csv: {contact_id}")


def project_metadata(project_name: str) -> dict[str, str]:
    key = normalize_project_name(project_name)
    return PROJECT_CATALOG[key]


def projects_for_sector(sector: str) -> list[dict[str, str]]:
    keys = SECTOR_PROJECT_MAP.get(sector.lower(), ["SEVENTY", "RETHAL GREENS"])
    return [PROJECT_CATALOG[key] for key in keys]


def select_project_for_contact(contact: Contact, explicit_project: str | None = None) -> dict[str, str]:
    if explicit_project:
        return project_metadata(explicit_project)
    return projects_for_sector(contact.sector)[0]


def available_project_images(project_name: str) -> list[Path]:
    meta = project_metadata(project_name)
    project_dir = PROJECT_PHOTO_DIR / meta["folder"]
    if not project_dir.exists():
        raise FileNotFoundError(f"Project photo directory not found: {project_dir}")

    images = [
        path
        for path in project_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS and "thumbs.db" not in path.name.lower()
    ]
    if not images:
        raise FileNotFoundError(f"No supported images found in: {project_dir}")
    return sorted(images)


def choose_feature_images(project_name: str) -> tuple[Path, Path]:
    images = sorted(available_project_images(project_name), key=lambda path: (-path.stat().st_size, path.name.lower()))
    hero = images[0]
    secondary = images[1] if len(images) > 1 else images[0]
    return hero, secondary


def logo_path(size_px: int) -> Path:
    if size_px == 48:
        return BRAND_GUIDE_DIR / "vitan-logo-48.png"
    if size_px == 200:
        return BRAND_GUIDE_DIR / "vitan-logo-200.png"
    raise ValueError(f"Unsupported logo size requested: {size_px}")


def image_to_data_uri(path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(path.name)
    payload_bytes = path.read_bytes()
    if path.suffix.lower() != ".png":
        try:
            from PIL import Image

            image = Image.open(io.BytesIO(payload_bytes)).convert("RGB")
            image.thumbnail((1600, 1600))
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=80, optimize=True)
            payload_bytes = buffer.getvalue()
            mime_type = "image/jpeg"
        except Exception:
            pass
    payload = base64.b64encode(payload_bytes).decode("ascii")
    return f"data:{mime_type or 'application/octet-stream'};base64,{payload}"


def artifact_name(contact: Contact, suffix: str, extension: str) -> str:
    return f"{slugify(contact.contact_id)}-{slugify(contact.company)}-{suffix}.{extension}"
