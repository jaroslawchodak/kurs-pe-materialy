# Instalacje krok po kroku — Windows i macOS (checklista przed kursem)

> Ten dokument obowiązuje w **obu** systemach. Znajdź swoją ramkę — 🪟 **Windows** albo 🍎 **macOS** — i wykonaj tylko ją. Nic tu nie wymaga umiejętności programowania; instalatory są graficzne („dalej → dalej"), a jedyne komendy to gotowce do skopiowania.
>
> **Zasada par:** w całym kursie skróty i ścieżki podajemy parami: `Ctrl+C` / `⌘C`, `Ctrl+V` / `⌘V`, **Eksplorator plików** / **Finder**, **PowerShell** / **Terminal**, `C:\Users\Ty\...` / `~/Documents/...`.

---

## 0. Co jest naprawdę potrzebne, a co opcjonalne

| Element | Kiedy potrzebny | Obowiązkowy? |
|---|---|---|
| Konta AI (ChatGPT, Claude, Gemini, Perplexity) | cały kurs | **TAK** (darmowe plany wystarczą) |
| Python + `pymupdf4llm` | Blok 6 (PDF → Markdown) | opcjonalny (jest wariant bez Pythona) |
| Ollama lub LM Studio (model lokalny) | Blok 10 | opcjonalny (pokaz prowadzącego) |
| Agent terminalowy (Claude Code / OpenCode) | Blok 11 (rozszerzenie) | opcjonalny |

**Nikt nie zostaje z tyłu bez instalacji** — Dzień 3 da się przejść w wariancie „zrozum i zdecyduj". Instalacje to wygoda dla chętnych.

---

## 1. Konta AI (5 minut, oba systemy tak samo)

- [ ] **ChatGPT** — chat.openai.com
- [ ] **Claude** — claude.ai
- [ ] **Gemini** — gemini.google.com (brama do NotebookLM: notebooklm.google.com)
- [ ] **Perplexity** — perplexity.ai

Test: zadaj w każdym to samo pytanie („Wyjaśnij w 3 zdaniach, czym jest przegląd systematyczny") i zauważ, które **podało źródła z odnośnikami**.

---

## 2. Python (Blok 6) — opcjonalny

> 🪟 **Windows**
> 1. Otwórz **Microsoft Store** → wpisz „Python" → zainstaluj najnowszą wersję. *(Albo: instalator z [python.org](https://python.org) — przy instalacji **zaznacz „Add python.exe to PATH"**.)*
> 2. Otwórz **PowerShell** (menu Start → wpisz „PowerShell").
> 3. Sprawdź: `python --version` (powinno pokazać `Python 3.x`).
> 4. Zainstaluj bibliotekę: `pip install pymupdf4llm`.

> 🍎 **macOS**
> 1. macOS ma wbudowany `python3`. Sprawdź w **Terminalu** (Spotlight `⌘Space` → „Terminal"): `python3 --version`.
> 2. Zalecane: doinstaluj świeżą wersję przez **Homebrew** — najpierw zainstaluj Homebrew ([brew.sh](https://brew.sh)), potem `brew install python`.
> 3. Zainstaluj bibliotekę: `pip3 install pymupdf4llm`.
> 4. Uwaga: na Macu używaj `python3` i `pip3` (nie `python`/`pip`).

---

## 3. Model lokalny (Blok 10) — opcjonalny

> 🪟 **Windows**
> 1. Pobierz `OllamaSetup.exe` z [ollama.com](https://ollama.com) → uruchom → „Install".
> 2. Otwórz **PowerShell** i pobierz mały model: `ollama pull granite4.1:8b`.
> 3. **Wymagania:** ~8–12 GB wolnej pamięci RAM dla modelu 8B; karta NVIDIA z ≥8 GB VRAM przyspiesza. Za mało? `ollama pull granite4.1:3b`.
> 4. Alternatywa graficzna: **LM Studio** ([lmstudio.ai](https://lmstudio.ai)) — pobierz `.exe`, klikaj zamiast pisać komendy.

> 🍎 **macOS**
> 1. Pobierz `Ollama.dmg` z [ollama.com](https://ollama.com) → przeciągnij do folderu **Aplikacje**.
> 2. Pierwsze uruchomienie: **prawy klik na ikonie → „Otwórz"** (obejście Gatekeepera dla aplikacji spoza App Store).
> 3. Otwórz **Terminal** i pobierz model: `ollama pull granite4.1:8b`.
> 4. **Apple Silicon (M1–M4):** pamięć współdzielona (unified memory) → modele działają szybciej i można sięgnąć po większe (`gemma4:26b-mlx`). **Intel Mac:** trzymaj się modeli 3–8B.
> 5. Alternatywa graficzna: **LM Studio** (`.dmg` → prawy klik → „Otwórz").

---

## 4. Agent terminalowy (Blok 11, rozszerzenie) — opcjonalny

> 🪟 **Windows**
> - Claude Code / OpenCode instalujesz w **PowerShell** lub w **WSL** (Windows Subsystem for Linux — zalecane dla narzędzi z rodowodem linuksowym; instrukcja włączenia WSL: `wsl --install` w PowerShell z uprawnieniami administratora).
> - Katalog projektu otwierasz w **Eksploratorze plików**; ścieżki `C:\Users\Ty\moj-projekt\`.

> 🍎 **macOS**
> - Instalujesz w **Terminalu**; z **Homebrew** instalacja bywa jedną komendą.
> - Katalog otwierasz w **Finderze**; ścieżki `~/moj-projekt/`. Gatekeeper przy pierwszym uruchomieniu → **prawy klik → „Otwórz"**.

---

## 5. Siatka bezpieczeństwa

Jeśli coś nie zadziała w domu — na **starcie Dnia 3** działa **10-minutowa mini-klinika techniczna**. Prowadzący pomaga uruchomić Ollama/agenta, zanim ruszą Bloki 10–11. Nikt nie traci na to czasu bloku.

*(Miejsce na zrzuty ekranu: instalator Ollama 🪟/🍎, „Add to PATH" w instalatorze Pythona, prawy klik → „Otwórz" na Macu.)*
