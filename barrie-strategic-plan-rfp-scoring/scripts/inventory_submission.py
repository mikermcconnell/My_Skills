#!/usr/bin/env python3
"""
Inventory a FIN2026-064P proponent folder before scoring.

- Lists PDFs found.
- Suggests likely Section F file mapping from filenames.
- Flags missing or unclear sections.
- Prints short text previews when PyPDF2 is available.
- Does not write files or edit the workbook.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    from PyPDF2 import PdfReader  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    PdfReader = None  # type: ignore


@dataclass(frozen=True)
class Section:
    code: str
    name: str
    keywords: Tuple[str, ...]


SECTIONS: Tuple[Section, ...] = (
    Section(
        "F.1",
        "Company Overview",
        (
            "company overview",
            "corporate overview",
            "firm overview",
            "firm profile",
            "company profile",
            "company",
            "corporate",
            "office locations",
            "subconsultant",
            "subcontractor",
        ),
    ),
    Section(
        "F.2",
        "Project Team Qualifications and Experience",
        (
            "project team qualifications",
            "team qualifications",
            "project team",
            "qualifications and experience",
            "organization chart",
            "organisational chart",
            "org chart",
            "project manager",
            "senior transit planner",
            "additional team",
            "cv",
            "resume",
            "résumé",
        ),
    ),
    Section(
        "F.3",
        "Relevant Project Experience",
        (
            "relevant project experience",
            "project experience",
            "project references",
            "reference 1",
            "reference 2",
            "client reference",
            "past projects",
            "similar projects",
            "relevant experience",
        ),
    ),
    Section(
        "F.4",
        "Project Understanding and Approach",
        (
            "project understanding",
            "understanding and approach",
            "project approach",
            "approach and methodology",
            "methodology",
            "work approach",
            "qa/qc",
            "quality assurance",
            "risk mitigation",
        ),
    ),
    Section(
        "F.5",
        "Work Plan and Schedule",
        (
            "work plan and schedule",
            "work plan",
            "workplan",
            "schedule",
            "gantt",
            "critical path",
            "time task matrix",
            "uncosted",
            "task matrix",
            "timeline",
        ),
    ),
)


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[_\-.]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_filename(path: Path, section: Section) -> int:
    name = normalize(path.stem)
    score = 0
    for keyword in section.keywords:
        if keyword in name:
            score += 4 if " " in keyword else 1
    # Boost exact section labels if used in filenames.
    compact_name = name.replace(" ", "")
    compact_code = section.code.lower().replace(".", "")
    if compact_code in compact_name or section.code.lower() in name:
        score += 5
    return score


def find_pdfs(folder: Path, recursive: bool) -> List[Path]:
    pattern = "**/*.pdf" if recursive else "*.pdf"
    return sorted(folder.glob(pattern), key=lambda p: str(p).lower())


def likely_sections(path: Path) -> List[Tuple[Section, int]]:
    scored = [(section, score_filename(path, section)) for section in SECTIONS]
    scored = [(section, score) for section, score in scored if score > 0]
    return sorted(scored, key=lambda item: item[1], reverse=True)


def extract_preview(path: Path, preview_chars: int) -> str:
    if preview_chars <= 0:
        return ""
    if PdfReader is None:
        return "Preview unavailable: PyPDF2 is not installed."
    try:
        reader = PdfReader(str(path))
        text_parts: List[str] = []
        for page in reader.pages[:2]:
            text_parts.append(page.extract_text() or "")
        text = " ".join(" ".join(text_parts).split())
        if not text:
            return "Preview unavailable: no extractable text found."
        return text[:preview_chars]
    except Exception as exc:
        return f"Preview unavailable: {exc}"


def pricing_flag(path: Path, preview: str, likely_code: str) -> str:
    if likely_code != "F.5" or not preview:
        return ""
    words = normalize(preview)
    pricing_terms = ["hourly rate", "price", "pricing", "cost", "fee", "hst", "$", "subtotal"]
    if any(term in words for term in pricing_terms):
        return "Possible pricing/cost wording found in F.5 preview. Check the uncosted matrix."
    return ""


def print_inventory(folder: Path, pdfs: List[Path], preview_chars: int) -> int:
    print(f"Proponent folder: {folder}")
    print(f"PDFs found: {len(pdfs)}")
    if not pdfs:
        print("\nNo PDFs found. Add the proponent submission PDFs before scoring.")
        return 1

    section_matches: Dict[str, List[Path]] = {section.code: [] for section in SECTIONS}
    unclear: List[Path] = []
    file_results: List[Tuple[Path, str, str, str]] = []

    print("\nFiles:")
    for path in pdfs:
        rel = path.relative_to(folder) if path.is_relative_to(folder) else path
        matches = likely_sections(path)
        if matches:
            top_section, top_score = matches[0]
            second_score = matches[1][1] if len(matches) > 1 else 0
            if second_score and top_score - second_score <= 2:
                likely = f"Unclear: {top_section.code} or {matches[1][0].code}"
                unclear.append(path)
            else:
                likely = f"{top_section.code} {top_section.name}"
                section_matches[top_section.code].append(path)
        else:
            likely = "Unclear"
            unclear.append(path)
        print(f"- {rel} -> {likely}")
        file_results.append((path, likely, "", ""))

    print("\nSection check:")
    missing = []
    for section in SECTIONS:
        files = section_matches[section.code]
        if not files:
            missing.append(section)
            print(f"- {section.code} {section.name}: MISSING or unclear")
        elif len(files) == 1:
            print(f"- {section.code} {section.name}: {files[0].name}")
        else:
            names = "; ".join(path.name for path in files)
            print(f"- {section.code} {section.name}: multiple possible files -> {names}")

    if missing or unclear:
        print("\nItems to confirm before scoring:")
        for section in missing:
            print(f"- Missing/unclear file for {section.code} {section.name}.")
        for path in unclear:
            print(f"- Confirm section mapping for {path.name}.")

    if preview_chars > 0:
        print("\nText previews:")
        for path, likely, _, _ in file_results:
            preview = extract_preview(path, preview_chars)
            flag = ""
            if likely.startswith("F.5"):
                flag = pricing_flag(path, preview, "F.5")
            print(f"\n--- {path.name} ({likely}) ---")
            print(preview)
            if flag:
                print(f"FLAG: {flag}")

    return 0


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inventory FIN2026-064P proponent PDFs before scoring.")
    parser.add_argument("folder", help="Path to the proponent folder.")
    parser.add_argument("--recursive", action="store_true", help="Search subfolders for PDFs.")
    parser.add_argument("--preview-chars", type=int, default=700, help="Preview characters per PDF. Use 0 to disable.")
    args = parser.parse_args(list(argv) if argv is not None else None)

    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists():
        print(f"Folder not found: {folder}", file=sys.stderr)
        return 2
    if not folder.is_dir():
        print(f"Path is not a folder: {folder}", file=sys.stderr)
        return 2

    pdfs = find_pdfs(folder, args.recursive)
    return print_inventory(folder, pdfs, max(args.preview_chars, 0))


if __name__ == "__main__":
    raise SystemExit(main())
