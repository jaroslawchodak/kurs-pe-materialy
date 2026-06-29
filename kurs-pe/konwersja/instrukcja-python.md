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
