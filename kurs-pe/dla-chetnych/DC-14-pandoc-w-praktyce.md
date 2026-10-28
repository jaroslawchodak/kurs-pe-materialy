# DC-14 (B6) — Pandoc w praktyce

> Ćwiczenie z części „Dla chętnych" kursu *Prompt engineering w badaniach naukowych* (wersja 2, 28.10.2026). Wykonujesz je po oddaniu minimum na sali z bloku B6, w domu albo na mini-klinice. Pominięcie nie blokuje ukończenia kursu.

1. Utwórz własny szablon stylów: `pandoc -o moj-szablon.docx --print-default-data-file reference.docx`, otwórz go w Wordzie, zmień style „Nagłówek 1", „Tekst podstawowy" i tabel, zapisz.
2. Skonwertuj swoją matrycę z B8 albo raport z B9: `pandoc matryca.md -o matryca.docx --reference-doc=moj-szablon.docx`.
3. Wyeksportuj z Zotero bibliografię do `.bib`, pobierz styl `.csl` (np. APA z repozytorium Zotero Style Repository) i wygeneruj dokument z przypisami: `pandoc tekst.md -o tekst.docx --citeproc --bibliography=biblioteka.bib --csl=apa.csl` (w tekście cytujesz kluczem, np. `[@lazer2009]`).
4. Przenieś matrycę do Excela skryptem `md2xlsx.py` z B6 i sprawdź liczbę wierszy.
