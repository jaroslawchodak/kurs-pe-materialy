# DC-5 (B7) — JSON dla opornych: konwersja tabel i kontrast CSV/JSON

> Ćwiczenie z części „Dla chętnych" kursu *Prompt engineering w badaniach naukowych* (wersja 2, 28.10.2026). Wykonujesz je po oddaniu minimum na sali z bloku B7, w domu albo na mini-klinice. Pominięcie nie blokuje ukończenia kursu.

*(Dawna rozgrzewka techniczna Dnia 3. Domyka Blok 7: tam definicja i fiszka, tu pełne oswojenie formatu.)*

## Analogia segregatora z teczkami (zamiast definicji technicznej)
Wyobraź sobie, że przekazujesz dokumenty asystentowi na dwa sposoby:

- **karton luźnych kartek** — to wklejona tabela z Excela: po drodze kartki się przetasowały i asystent zgaduje, która liczba to rok, a która numer strony;
- **segregator z opisanymi teczkami** — na każdej teczce etykieta (*rok*, *metoda*, *cytat*), w środku dokładnie jedna informacja. Nic nie może się pomylić, bo **każda wartość nosi swoją etykietę**.

**JSON to ten segregator zapisany jako zwykły tekst.** Formalnie (jedno zdanie wystarczy): JSON to tekstowy zapis danych jako pary *etykieta: wartość* — standard opisany na [json.org](https://www.json.org/json-pl.html). Do czytania wystarczą trzy znaki:

| Znak | Po ludzku |
|---|---|
| `{ }` | jedna teczka (rekord, np. jedna pozycja literatury) |
| `[ ]` | półka z teczkami (lista rekordów) |
| `"etykieta": wartość` | napis na teczce + jej zawartość |

```json
{ "autor": "Lazer i in.", "rok": 2009, "metoda": "artykuł stanowiskowy" }
```

To ta sama fiszka bibliograficzna, którą znasz z Bloku 7 — nic nowego, tylko nazwane na spokojnie.

## Jak przekształcić tabelę do JSON bez programowania
Nie potrzebujesz żadnego narzędzia programistycznego — **konwerterem jest sam model**:

1. **Prompt-konwerter (droga podstawowa).** Zaznacz tabelę w Excelu lub Wordzie, skopiuj (`Ctrl+C` / `⌘C`), wklej do czatu z poleceniem:

   ```
   Przekształć poniższą tabelę do formatu JSON.
   Każdy wiersz zapisz jako osobny obiekt { },
   a nazwy kolumn użyj jako etykiet pól.
   Niczego nie dodawaj ani nie poprawiaj — jeśli komórka
   jest pusta, wpisz null.
   ```

2. **Kontrola odwrotna (obowiązkowa — zasada ograniczonego zaufania).** Model *może pomylić komórki* przy konwersji, dokładnie tak jak przy wklejonej tabeli. Dlatego w nowym czacie (albo drugim kroku) każ mu przekształcić otrzymany JSON **z powrotem w tabelę** i porównaj ją z oryginałem: liczba wierszy, wartości liczbowe, pola tekstowe. Dopiero zgodność w obie strony = konwersja zaliczona.

3. **Eksport z narzędzi, które już masz.** Zotero i arkusze eksportują do **CSV** — i to często wystarcza. Reguła rozstrzygająca: **CSV do prostych, płaskich list; JSON, gdy pola są opisowe (długie zdania, przecinki w treści), zagnieżdżone (np. lista autorów) albo wynik ma trafić do dalszego przetworzenia** (agent, arkusz, API). Ograniczenia CSV: etykiety są tylko w wierszu nagłówka (po wklejeniu do czatu „odklejają się" od danych), a pola z przecinkami w środku zdania rozjeżdżają komórki.

> 🧪 **Dla nauk ścisłych — ten sam mechanizm na danych eksperymentalnych (XLSX używa 80% grupy).** Gdy prosisz model o pomoc w interpretacji małej tabeli wyników, nie wklejaj jej „na oko" — zapisz każdy pomiar jednoznacznie:
> ```json
> {"grupa": "dawka_10mg", "n": 8, "srednia": 4.21, "sd": 0.63, "jednostka": "U/mg", "test_zaplanowany": "ANOVA + Tukey"}
> ```

> 🚦 **Sygnalizator przy konwersji:** do prompta-konwertera w chmurze wklejasz **wyłącznie dane jawne lub zagregowane**. Tabela z danymi respondentów/pacjentów najpierw przechodzi pseudonimizację i minimalizację pól (Blok 7), a najlepiej — konwersję u modelu lokalnego (Blok 10).

## Mini-ćwiczenie (10 min)
Weź **jedną własną, jawną tabelę** (fragment bibliografii, tabela wyników, harmonogram badania), przekonwertuj ją promptem-konwerterem i wykonaj **kontrolę odwrotną**. Wynik zapisz jako `dane-projekt.json` — trafi do folderu `zrodla/` Twojego katalogu projektu w Bloku 11.


## Konwersja skryptem Pythona: lokalnie, bez chmury

Prompt-konwerter wystarcza przy małych, prostych tabelach. Po skrypt sięgasz w dwóch sytuacjach:

1. **Tabela jest duża albo złożona**: dziesiątki wierszy, scalone komórki, długie teksty z przecinkami i znakami nowej linii. Wklejona do czatbota lub agenta taka tabela często gubi komórki albo przesuwa je między kolumnami, a model przy przepisywaniu potrafi skrócić lub „poprawić” wartość. Skrypt przepisuje każdą komórkę dosłownie.
2. **Dane są wrażliwe (🔴)**: skrypt działa na Twoim komputerze, więc tabela nie trafia do modelu w chmurze. Do LLM wysyłasz dopiero wynik po pseudonimizacji i minimalizacji pól albo nie wysyłasz go wcale.

**Czego potrzebujesz.** Pythona 3 (na macOS i Linuksie zwykle jest zainstalowany) i dwóch bibliotek do plików Office: `pip install openpyxl python-docx`. Polecenie wpisujesz w Terminalu, w folderze z plikiem. Pierwszy argument to plik wejściowy, drugi to plik JSON, który powstanie.

**CSV → JSON**

```bash
python3 -c '
import csv, json, sys
with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
    first = f.readline(); f.seek(0)
    sep = max(",;\t", key=first.count)
    rows = list(csv.DictReader(f, delimiter=sep))
with open(sys.argv[2], "w", encoding="utf-8") as out:
    json.dump(rows, out, ensure_ascii=False, indent=2)
' dane.csv dane.json
```

Separator (przecinek, średnik albo tabulator) skrypt rozpoznaje z pierwszego wiersza. To ważne, bo polski Excel zapisuje CSV ze średnikami. CSV nie zna typów, więc wszystkie wartości wychodzą jako tekst (`"rok": "2021"`).

**XLSX → JSON**

```bash
python3 -c '
import json, sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], data_only=True, read_only=True)
ws = wb[sys.argv[3]] if len(sys.argv) > 3 else wb.active
rows = ws.iter_rows(values_only=True)
header = []
for i, c in enumerate(next(rows), 1):
    name = str(c).strip() if c is not None else f"kolumna_{i}"
    header.append(name if name not in header else f"{name}_{i}")
data = [dict(zip(header, r)) for r in rows if any(v is not None for v in r)]
with open(sys.argv[2], "w", encoding="utf-8") as out:
    json.dump(data, out, ensure_ascii=False, indent=2, default=str)
' dane.xlsx dane.json
```

Skrypt czyta aktywny arkusz. Inny arkusz podajesz jako trzeci argument: `… dane.xlsx dane.json "Arkusz2"`. Zapisuje wartości wyliczone przez formuły, nie same formuły. Liczby zostają liczbami, pusta komórka to `null`, pustych wierszy skrypt nie przepisuje.

**DOCX → JSON (tabele z dokumentu Word)**

```bash
python3 -c '
import json, sys
from docx import Document
tables = []
for table in Document(sys.argv[1]).tables:
    rows = [[c.text.strip() for c in row.cells] for row in table.rows]
    if len(rows) < 2:
        continue
    header = []
    for i, name in enumerate(rows[0], 1):
        name = name or f"kolumna_{i}"
        header.append(name if name not in header else f"{name}_{i}")
    tables.append([dict(zip(header, r)) for r in rows[1:]])
with open(sys.argv[2], "w", encoding="utf-8") as out:
    json.dump(tables, out, ensure_ascii=False, indent=2)
' dane.docx dane.json
```

Wynik to zawsze lista tabel (każda tabela to lista wierszy), także gdy dokument ma jedną tabelę. Pierwszy wiersz tabeli jest nagłówkiem. Tabele z jednym wierszem skrypt pomija.

**Wspólne zabezpieczenia.** Pusty nagłówek dostaje nazwę `kolumna_3`, powtórzony nagłówek dostaje numer (`rok_4`), więc żadna kolumna nie nadpisuje innej. Plik zapisuje się w UTF-8 z polskimi znakami.

**Kontrola wyniku.** Skrypt nie myli komórek, ale nie wie, co jest nagłówkiem. Otwórz JSON i sprawdź liczbę rekordów i nazwy pól. Scalona komórka w Wordzie powtarza tekst w każdej kolumnie, którą obejmuje (pola z końcówką `_2`, `_3`).

**Windows.** Polecenia `python3 -c '…'` działają w Terminalu macOS i Linuksa. W Windows zapisz kod spomiędzy apostrofów jako plik, np. `xlsx2json.py`, i uruchom: `py xlsx2json.py dane.xlsx dane.json`.

## Kontrast CSV/JSON
Wyeksportuj 5–8 pozycji bibliograficznych do **CSV** lub wklej je jako „brudną" tabelę. Celowo zostaw w którymś polu **przecinek w środku zdania** (np. w tezie) i sprawdź, czy model rozjeżdża komórki albo myli, która wartość to rok, a która strona. Porównaj z wersją JSON tego samego zestawu.

**Kryterium (DC-5):** masz plik JSON, w którym każda wartość nosi etykietę, a kontrola odwrotna potwierdziła zgodność z oryginałem; przy kontraście potrafisz pokazać konkretną różnicę między wersją CSV a JSON.
