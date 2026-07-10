#!/usr/bin/env python3
"""
konwersja-batch.py — seryjne (batch) parsowanie PDF → Markdown.

Wrzuć pliki .pdf do katalogu wejściowego, uruchom skrypt,
a gotowe pliki .md pojawią się w katalogu wyjściowym.

Przykłady:
    python konwersja-batch.py                           # domyślne foldery: pdf_input/ → md_output/
    python konwersja-batch.py -i moje_pdfy/ -o wyniki/  # własne foldery

Wymaga jednorazowej instalacji (patrz instrukcja-python.md):
    pip install pymupdf4llm
"""

import argparse
import sys
import time
from pathlib import Path

# ── Import współdzielonej logiki czyszczenia z konwersja.py (DRY) ──────────
# Jeśli import nie zadziała (np. skrypt przeniesiony bez konwersja.py),
# skrypt użyje własnej, minimalnej wersji.
try:
    from konwersja import wyczysc
except ImportError:
    import re

    def wyczysc(md: str) -> str:
        """Kopia zapasowa: czyszczenie artefaktów (identyczne jak w konwersja.py)."""
        md = re.sub(r"(?m)^\s*\d{1,4}\s*$", "", md)
        md = re.sub(r"(\w)-\n(\w)", r"\1\2", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"(?m)[ \t]+$", "", md)
        return md.strip() + "\n"


def zbierz_pdfy(katalog: Path) -> list[Path]:
    """Zwróć posortowaną listę plików .pdf w katalogu (nie rekursywnie)."""
    return sorted(katalog.glob("*.pdf"), key=lambda p: p.name.lower())


def konwertuj_plik(pdf: Path, katalog_wyjsciowy: Path) -> bool:
    """Konwertuj pojedynczy PDF → MD. Zwraca True przy sukcesie."""
    import pymupdf4llm

    md = pymupdf4llm.to_markdown(str(pdf))
    md = wyczysc(md)

    out = katalog_wyjsciowy / pdf.with_suffix(".md").name
    out.write_text(md, encoding="utf-8")
    return True


def main() -> int:
    # ── Argumenty CLI ──────────────────────────────────────────────────
    parser = argparse.ArgumentParser(
        description="Seryjne (batch) parsowanie plików PDF → Markdown.",
        epilog="Więcej: instrukcja-python.md",
    )
    parser.add_argument(
        "-i", "--input-dir",
        default="pdf_input",
        help="Katalog z plikami PDF (domyślnie: pdf_input/)",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="md_output",
        help="Katalog na wyniki .md (domyślnie: md_output/)",
    )
    args = parser.parse_args()

    katalog_we = Path(args.input_dir).expanduser().resolve()
    katalog_wy = Path(args.output_dir).expanduser().resolve()

    # ── Walidacja katalogu wejściowego ─────────────────────────────────
    if not katalog_we.is_dir():
        print(f"✗ Katalog wejściowy nie istnieje: {katalog_we}")
        print(f"  Utwórz go i wrzuć do niego pliki PDF.")
        return 1

    # ── Tworzenie katalogu wyjściowego (jeśli brak) ───────────────────
    katalog_wy.mkdir(parents=True, exist_ok=True)

    # ── Zebranie kolejki plików ────────────────────────────────────────
    pliki = zbierz_pdfy(katalog_we)
    if not pliki:
        print(f"✗ Brak plików .pdf w: {katalog_we}")
        return 1

    # ── Sprawdzenie biblioteki ─────────────────────────────────────────
    try:
        import pymupdf4llm  # noqa: F401
    except ImportError:
        print("✗ Brak biblioteki. Zainstaluj jednorazowo:  pip install pymupdf4llm")
        return 1

    # ── Pętla batch ────────────────────────────────────────────────────
    razem = len(pliki)
    ok = 0
    bledy: list[tuple[str, str]] = []

    print(f"Znaleziono {razem} plik(ów) PDF w: {katalog_we}")
    print(f"Wyniki trafią do: {katalog_wy}")
    print("-" * 60)

    for i, pdf in enumerate(pliki, start=1):
        etykieta = f"[{i}/{razem}]"
        print(f"{etykieta} Przetwarzanie: {pdf.name} ... ", end="", flush=True)

        t0 = time.perf_counter()
        try:
            konwertuj_plik(pdf, katalog_wy)
            dt = time.perf_counter() - t0
            print(f"Gotowe ({dt:.1f}s)")
            ok += 1
        except Exception as exc:
            dt = time.perf_counter() - t0
            print(f"BŁĄD ({dt:.1f}s)")
            print(f"       ↳ {type(exc).__name__}: {exc}")
            bledy.append((pdf.name, str(exc)))

    # ── Podsumowanie ───────────────────────────────────────────────────
    print("-" * 60)
    print(f"Ukończono: {ok}/{razem} plików skonwertowanych pomyślnie.")
    if bledy:
        print(f"Pominięto z błędem ({len(bledy)}):")
        for nazwa, msg in bledy:
            print(f"  • {nazwa}: {msg}")
        return 2  # kod wyjścia 2 = częściowy sukces

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
