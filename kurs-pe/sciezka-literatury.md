# Ścieżka literatury kursu — mapa jednostronicowa

> Praca z literaturą to oczekiwanie nr 1 tej grupy (100%). W kursie jest rozłożona na kilka bloków — ta mapa pokazuje ją jako **jeden ciągły proces**: od kwerendy, przez analizę, po krytyczną weryfikację. Każdy krok ma swój blok i swój artefakt.

| Krok procesu | Co robisz | Blok | Narzędzie / metoda | Artefakt |
|---|---|---|---|---|
| **1. Eksploracja** | znajdź, co w ogóle istnieje na temat | B9 | Perplexity, Deep Research; mapy: Connected Papers / Litmaps / Research Rabbit | lista tropów |
| **2. Kwerenda systematyczna** | zbierz i przesiej wiele prac | B9 | Elicit (ekstrakcja), Consensus (synteza) | protokół deep research + karta oceny |
| **3. Pozyskanie źródeł** | zbierz pliki, uporządkuj metadane | B8 | Zotero (RIS/BibTeX, lokalny magazyn PDF) | biblioteka źródeł |
| **4. Oczyszczenie** | PDF → czysty Markdown, usuń śmieci OCR | B6 | `pymupdf4llm`, `konwersja.py` | czysty `.md` |
| **5. Streszczenie zakotwiczone** | długi artykuł → streszczenie z tagiem źródła | B6 | summarizer (`summarizer-demo/`) | streszczenie z lokalizacją |
| **6. Matryca / „mały RAG"** | ręczna selekcja tez i cytatów-kotwic | B8 | `matryca-literatury-szablon.md` | matryca 3–5 źródeł |
| **7. Lektura wielu źródeł** | odpytaj cały korpus z zakotwiczeniem | Gemini Notebook (Dzień 2) | preambuła + sekwencja 7 kroków | notatki trwałe |
| **8. Weryfikacja cytowań** | trzystopniowy werdykt na każde źródło | B9 | `protokol-weryfikacji-zrodel.md` | karta z werdyktami |
| **9. Skalowanie (opcjonalnie)** | agent grupuje korpus automatycznie | B11 | `clustering-demo/` | raport + outline |

## Reguła spajająca

Na **każdym** kroku obowiązuje ograniczone zaufanie i zakotwiczenie: narzędzie *zbiera, porządkuje, streszcza* — ale **werdykt, selekcja i odpowiedzialność należą do badacza**. Automat (krok 9) skaluje selekcję z kroku 6, nie zastępuje jej.

## Tory dyscyplinarne

Materiał do wszystkich kroków wybierasz w **swoim torze** (`kurs-pe/materialy-dyscyplinarne/`): **A** ścisłe/przyrodnicze · **B** społeczne · **C** humanistyka. Procedura identyczna — różni się tylko materiał i *pytanie badacza* (por. wariacja Gemini Notebook „ta sama książka, trzy pytania dyscyplinarne").
