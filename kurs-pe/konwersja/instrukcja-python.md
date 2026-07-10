# Instrukcja: konwersja PDF → Markdown (bez programowania)

> Cel: zamienić swój PDF na czysty plik `.md`, który jest dobrym kontekstem dla AI.
> Uwaga: NIE programujesz. Uruchamiasz gotowy skrypt jedną komendą.

---

## Krok 1. Sprawdź, czy masz Python 3

**macOS** — otwórz aplikację *Terminal* i wpisz:
```
python3 --version
```
**Windows** — otwórz *PowerShell* i wpisz:
```
python --version
```
Jeśli widzisz numer (np. `Python 3.12`) — masz. Jeśli nie:
- Windows: zainstaluj z Microsoft Store („Python 3") albo z https://www.python.org/downloads/
- macOS: zainstaluj z https://www.python.org/downloads/ albo przez Homebrew (`brew install python`).

## Krok 2. Zainstaluj bibliotekę (raz)

macOS:
```
pip3 install pymupdf4llm
```
Windows:
```
pip install pymupdf4llm
```

## Krok 3. Uruchom konwersję

Przeciągnij plik PDF do okna terminala po komendzie (wstawi ścieżkę):
```
python3 konwersja.py /sciezka/do/artykul.pdf      # macOS
python konwersja.py C:\sciezka\do\artykul.pdf      # Windows
```
Wynik: `artykul.md` obok PDF-a.

## Krok 4. Sprawdź wynik
Otwórz `artykul.md` w edytorze Markdown i przejrzyj wg `sciaga-artefakty-ocr.md`.

---

## Krok 5. Konwersja wielu plików naraz (batch)

> Osobny skrypt `konwersja-batch.py` — seryjne przetwarzanie całego katalogu PDF-ów.
>
> **Dlaczego osobny skrypt?** Oryginalny `konwersja.py` jest celowo prosty
> (jedno polecenie = jeden plik). Tryb batch wymaga argumentów CLI, pętli
> i raportowania błędów — dołożenie tego do prostego skryptu skomplikowałoby
> go użytkownikom, którzy potrzebują tylko jednorazowej konwersji.
> Współdzielona funkcja czyszcząca (`wyczysc`) jest importowana
> z `konwersja.py`, więc logika nie jest powielona (DRY).

### Gdzie wrzucić pliki PDF?

Domyślnie skrypt szuka plików w folderze `pdf_input/` (obok skryptu).
Wyniki `.md` trafiają do `md_output/`. Oba foldery możesz zmienić flagami.

### Uruchomienie

1. Utwórz folder i wrzuć do niego PDF-y:
   ```
   mkdir pdf_input
   # skopiuj swoje pliki .pdf do folderu pdf_input/
   ```

2. Uruchom konwersję wsadową:

   macOS:
   ```
   python3 konwersja-batch.py
   ```
   Windows:
   ```
   python konwersja-batch.py
   ```

3. Własne katalogi (opcjonalnie):
   ```
   python3 konwersja-batch.py -i moje_pdfy/ -o wyniki/
   python  konwersja-batch.py -i moje_pdfy/ -o wyniki/    # Windows
   ```

4. Pomoc:
   ```
   python3 konwersja-batch.py --help
   ```

### Co się dzieje?

- Skrypt wypisuje postęp: `[1/15] Przetwarzanie: raport.pdf ... Gotowe (2.3s)`
- Jeśli jakiś PDF jest uszkodzony — zostanie pominięty z ostrzeżeniem,
  reszta przetworzy się normalnie.
- Na końcu pojawi się podsumowanie: ile plików udało się, ile pominięto.

---

## Wariant awaryjny (bez Pythona)
Jeśli instalacja nie zadziała — nie blokuje to celu kursu:
1. Skopiuj tekst z PDF do edytora Markdown ręcznie, **albo**
2. Użyj polecenia do modelu: *„Przepisz poniższy tekst do czystego Markdown: dodaj nagłówki, usuń numery stron, stopki i artefakty OCR, zachowaj treść i strukturę."*

## Skan zamiast tekstu?
`pymupdf4llm` czyta warstwę tekstu. Jeśli PDF to skan (obraz), najpierw zrób OCR (np. w Zotero, w czytniku PDF z OCR, albo narzędziem `ocrmypdf`), potem uruchom skrypt.

## Inne narzędzia (gdy potrzeba więcej)
- **Docling** — lepsze tabele i struktura, pod pipeline'y RAG.
- **marker** — wiele formatów, opcjonalne wspomaganie LLM przy trudnych układach.
- **Pandoc** — konwersja MD ↔ DOCX i inne.
