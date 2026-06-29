#!/usr/bin/env python3
"""
konwersja.py — PDF -> czysty Markdown (gotowy skrypt dla uczestników kursu).

Nie musisz umieć programować. Wystarczy uruchomić jedną komendą:

    python konwersja.py sciezka/do/artykul.pdf

Wynik zapisze się jako 'artykul.md' obok pliku PDF.

Wymaga jednorazowej instalacji (patrz instrukcja-python.md):
    pip install pymupdf4llm

Działa najlepiej na PDF-ach z NATYWNĄ warstwą tekstu (nie skan).
Dla skanów potrzebny jest najpierw OCR — patrz instrukcja-python.md.
"""

import sys
import re
from pathlib import Path


def wyczysc(md: str) -> str:
    """Lekkie, bezpieczne czyszczenie typowych artefaktów."""
    # 1) Usuń samotne numery stron (linia będąca tylko liczbą)
    md = re.sub(r"(?m)^\s*\d{1,4}\s*$", "", md)
    # 2) Scal wyrazy przedzielone myślnikiem na końcu wiersza (po-\ndział -> podział)
    md = re.sub(r"(\w)-\n(\w)", r"\1\2", md)
    # 3) Zredukuj 3+ pustych linii do jednej pustej
    md = re.sub(r"\n{3,}", "\n\n", md)
    # 4) Usuń spacje na końcach linii
    md = re.sub(r"(?m)[ \t]+$", "", md)
    return md.strip() + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print("Użycie: python konwersja.py sciezka/do/pliku.pdf")
        return 1

    pdf = Path(sys.argv[1]).expanduser()
    if not pdf.exists():
        print(f"Nie znaleziono pliku: {pdf}")
        return 1

    try:
        import pymupdf4llm
    except ImportError:
        print("Brak biblioteki. Zainstaluj jednorazowo:  pip install pymupdf4llm")
        return 1

    print(f"Konwertuję: {pdf.name} ...")
    md = pymupdf4llm.to_markdown(str(pdf))
    md = wyczysc(md)

    out = pdf.with_suffix(".md")
    out.write_text(md, encoding="utf-8")
    print(f"Gotowe -> {out}")
    print("Otwórz plik w edytorze i sprawdź: nagłówki, stopki, tabele, artefakty OCR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
