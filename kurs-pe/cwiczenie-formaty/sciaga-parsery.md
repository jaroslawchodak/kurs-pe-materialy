# Ściąga — parsery PDF → Markdown (dobór wg zadania)

**Parser** to narzędzie, które wydobywa treść z pliku (PDF, DOCX, skan) i zapisuje ją jako czysty Markdown — bez balastu układu graficznego. Po ludzku: zamienia „format do oglądania" (PDF) w „format czytelny dla człowieka i dla modelu" (Markdown). Dobór zależy od tego, **co** masz na wejściu.

| Narzędzie | Najlepsze do | Uwagi |
|---|---|---|
| **PyMuPDF / `pymupdf4llm`** | PDF z natywną warstwą tekstu | najlżejsze, bez modeli ML/GPU; szybkie; domyślny wybór |
| **Docling** (IBM) | pipeline'y RAG, dobre tabele | solidna struktura dokumentu; sensowny default dla nauki |
| **Granite-Docling** | trudniejsze układy, tabele, wzory | wariant Docling wspomagany modelem; cięższy |
| **marker** | wiele formatów, złożone układy | opcjonalne wspomaganie LLM przy trudnych stronach |
| **GROBID** | **artykuły naukowe** (metadane, bibliografia) | wyspecjalizowany w strukturze publikacji: autor, sekcje, referencje |
| **Science Parse** | artykuły naukowe (tytuł, abstrakt, bibliografia) | lekka alternatywa nastawiona na metadane publikacji |
| **nougat-base** (Meta) | PDF z **wzorami matematycznymi** | model OCR „rozumiejący" notację; wolniejszy, GPU |
| **Markitdown** (Microsoft) | szybka konwersja wielu formatów (DOCX, PPTX, PDF…) | uniwersalny „do Markdown"; mniej kontroli nad układem |
| **Llama Parse** (LlamaIndex) | trudne PDF pod RAG (usługa) | jakość kosztem prywatności — **przetwarza w chmurze**, patrz niżej |
| **Pandoc** | konwersja MD ↔ DOCX/HTML/LaTeX | nie do PDF-skanów; uniwersalny konwerter formatów tekstowych |

## Instalacja — Windows i macOS (podwójna ramka)
> Większość parserów instaluje się przez `pip`; różni się tylko powłoka (PowerShell / Terminal), komenda (`pip` / `pip3`) i drobne zależności systemowe. Wybierz swoją ramkę. Pełna checklista środowiska: `kurs-pe/00_start/instalacje-win-mac.md`.

> 🪟 **Windows** (w **PowerShell**):
> - Domyślny parser: `pip install pymupdf4llm`
> - Docling / marker / Markitdown: `pip install docling` · `pip install marker-pdf` · `pip install markitdown`
> - **GROBID** działa jako usługa w kontenerze — najprościej przez **Docker Desktop for Windows** (`docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0`).
> - **nougat** (wzory): `pip install nougat-ocr` — zalecana karta NVIDIA (CUDA); bez GPU działa wolno.
> - **Pandoc**: instalator `.msi` z [pandoc.org](https://pandoc.org) albo `winget install pandoc`.
> - Ścieżki do plików PDF: `C:\Users\Ty\Documents\...`.

> 🍎 **macOS** (w **Terminalu**; używaj `pip3`):
> - Domyślny parser: `pip3 install pymupdf4llm`
> - Docling / marker / Markitdown: `pip3 install docling` · `pip3 install marker-pdf` · `pip3 install markitdown`
> - **GROBID**: przez **Docker Desktop for Mac** (`docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0`); na Apple Silicon użyj obrazu w wersji `arm`, jeśli dostępny.
> - **nougat** (wzory): `pip3 install nougat-ocr`; na Apple Silicon działa na CPU/MPS (wolniej niż CUDA, ale działa).
> - **Pandoc**: `brew install pandoc` (Homebrew) albo instalator `.pkg` z [pandoc.org](https://pandoc.org).
> - Narzędzie z sieci uruchamiane pierwszy raz → Gatekeeper: **prawy klik → „Otwórz"**. Ścieżki: `~/Documents/...`.

## Przykładowy pipeline demonstracyjny
Skrypt Python łączący kilka narzędzi pod jedno wejście:
```
PDF → PyMuPDF (warstwa tekstu) → Docling / Granite-Docling (tabele, struktura) → czysty .md
```
Dla artykułu naukowego z bogatą bibliografią dołóż **GROBID** (metadane + referencje); dla tekstu z matematyką — **nougat**.

## Dwie reguły kursu (bez nich parser szkodzi)
1. **Kontrola wierności** — po konwersji porównaj `.md` z oryginałem w 2–3 newralgicznych miejscach (tabela z wynikami, kluczowa liczba, przypis). Parser potrafi **cicho** zgubić lub przekręcić dane (most do Bloku 6, „ryzyko i przeciwdziałanie"). Kotwiczysz tezę tylko w tym, co wiernie odwzorowane.
2. **Gdzie trafiają dane** — narzędzia lokalne (PyMuPDF, Docling, GROBID, Markitdown, Pandoc) działają na Twoim komputerze. **Usługi chmurowe** (np. Llama Parse) wysyłają plik na serwer — nie używaj ich do materiałów wrażliwych / pod NDA (zasada `privacy cage`, Blok 10).

> Stan narzędzi: czerwiec 2026 — przed użyciem sprawdź aktualną dokumentację producenta (Blok 12: śledź źródła pierwotne, nie blogi).
