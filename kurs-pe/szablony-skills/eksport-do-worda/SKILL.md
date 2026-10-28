---
name: eksport-do-worda
description: >
  Używaj, gdy użytkownik prosi o zamianę pliku Markdown z wyniki/ na dokument
  Worda (.docx) lub tabel z pliku .md na arkusz Excela (.xlsx).
  Nie używaj do zmiany treści dokumentu.
---
# Eksport do Worda i Excela

## Co robi ta procedura
Zamienia plik Markdown na .docx programem pandoc, a tabele Markdown na .xlsx
skryptem scripts/md2xlsx.py, bez zmiany treści.

## Wejście i wyjście
Wejście: plik .md wskazany przez użytkownika; opcjonalnie szablon stylów moj-szablon.docx,
plik bibliografii .bib i styl cytowania .csl.
Wyjście: plik .docx lub .xlsx o tej samej nazwie w tym samym folderze.

## Kroki
1. Sprawdź, czy pandoc jest zainstalowany (`pandoc --version`). Jeśli nie, podaj
   użytkownikowi polecenie instalacji: Windows `winget install --id JohnMacFarlane.Pandoc`,
   macOS `brew install pandoc`, i zatrzymaj się.
2. Word: `pandoc <plik>.md -o <plik>.docx`; z szablonem stylów dodaj
   `--reference-doc=moj-szablon.docx`; z bibliografią dodaj
   `--citeproc --bibliography=<plik>.bib --csl=<styl>.csl`.
3. Excel: `python3 scripts/md2xlsx.py <plik>.md <plik>.xlsx` (Windows: `py` zamiast `python3`;
   wymaga openpyxl).
4. Kontrola: podaj liczbę nagłówków i tabel w pliku .md oraz w wyniku; przy .xlsx liczbę
   wierszy każdej tabeli. Zgłoś każdą rozbieżność.

## Reguły
- Nie zmieniasz treści pliku źródłowego. Markdown jest wersją źródłową, .docx/.xlsx to wydruk.
- Nie nadpisujesz istniejącego pliku .docx/.xlsx bez pytania.
- Liczby z przecinkiem dziesiętnym zostają w Excelu tekstem — powiedz o tym użytkownikowi.
