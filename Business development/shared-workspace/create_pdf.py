#!/usr/bin/env python3
"""Compatibility wrapper for branded PDF generation."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def _resolve_paths() -> tuple[Path, Path]:
    this_file = Path(__file__).resolve()
    workspace_dir = this_file.parent
    repo_root = workspace_dir.parent.parent
    scripts_dir = repo_root / "scripts"
    return repo_root, scripts_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a branded outreach PDF artifact for a contact and project."
    )
    parser.add_argument("contact_id", help="VIT contact identifier, for example VIT-C-001")
    parser.add_argument("project_name", help="Project name or alias, for example 'Privilon'")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional output directory. Defaults to shared-workspace/review/vita189",
    )
    return parser.parse_args()


def _venv_python_path(venv_dir: Path) -> Path:
    return venv_dir / "bin" / "python3"


def _venv_has_reportlab(venv_python: Path) -> bool:
    if not venv_python.exists():
        return False
    result = subprocess.run(
        [str(venv_python), "-c", "import reportlab"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def _has_reportlab() -> bool:
    try:
        import reportlab  # noqa: F401
    except Exception:
        return False
    return True


def _ensure_pdf_runtime(repo_root: Path) -> None:
    if _has_reportlab():
        return

    venv_dir = repo_root / ".venvs" / "vitan-content-tools"
    venv_python = _venv_python_path(venv_dir)
    if not _venv_has_reportlab(venv_python):
        venv_dir.parent.mkdir(parents=True, exist_ok=True)
        if not venv_python.exists():
            subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        subprocess.run(
            [
                str(venv_python),
                "-m",
                "pip",
                "install",
                "--upgrade",
                "pip",
                "reportlab",
                "Pillow",
            ],
            check=True,
        )

    env = os.environ.copy()
    env["VITAN_PDF_RUNTIME_READY"] = "1"
    os.execve(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]], env)


def main() -> int:
    args = parse_args()
    repo_root, scripts_dir = _resolve_paths()
    if os.environ.get("VITAN_PDF_RUNTIME_READY") != "1":
        _ensure_pdf_runtime(repo_root)

    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    from generate_branded_pdf import dependency_error, render_pdf

    try:
        output_path = render_pdf(args.contact_id, args.project_name, args.output_dir)
    except RuntimeError as exc:
        return dependency_error(exc)
    print(f"Generated {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
