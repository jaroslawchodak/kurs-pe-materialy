# 🚀 Przed kursem — ściągawka (*cheatsheet*) uczestnika

**Prompt engineering w badaniach naukowych** · kurs półwarsztatowy, 3 dni
⏱️ **Czas: ~15 minut pracy własnej przed pierwszym dniem.**

> **Po co to?** Żeby pierwszy dzień nie schodził na zakładanie kont i logowanie. Wchodzisz na salę z działającym dostępem do narzędzi i jednym odruchem ochrony danych. **Nie musisz niczego umieć z góry — to tylko przygotowanie dostępu.**

---

## ✅ 1. Załóż konta (darmowe plany w zupełności wystarczą)

Zaznacz, gdy gotowe:

- [ ] **ChatGPT** — `chat.openai.com` · *czat ogólny + tryb research; punkt odniesienia (Dzień 1 i 3)*
- [ ] **Claude** — `claude.ai` · *czat ogólny; główny model agentów (Dzień 3)*
- [ ] **Gemini** — `gemini.google.com` · *czat + Deep Research; brama do NotebookLM (Dzień 2)*
- [ ] **GROK** — `https://grok.com` · *czat + wyszukiwarka AI z odnośnikami do źródeł (Dzień 1-2)*
- [ ] **Perplexity** — `perplexity.ai` · *wyszukiwarka AI z odnośnikami do źródeł (Dzień 1)*

---

## ✅ 2. Sprawdź czy działają (5 min)

- [ ] Zaloguj się do **każdego** z czterech narzędzi.
- [ ] Zadaj w każdym **to samo** proste pytanie, np.:
  > *„Wyjaśnij w 3 zdaniach, czym jest przegląd systematyczny."*
- [ ] Zauważ (nie analizuj jeszcze — tylko zaobserwuj): **które narzędzie podało źródła z klikalnymi odnośnikami, a które odpowiedziało „z pamięci", bez źródeł?**

> To pierwszy zalążek Bloku 1 — różnica między „odpowiedzią do sprawdzenia" a „odpowiedzią ze sprawdzalnym śladem".

---

## 3. Zainstaluj co najmniej jeden z darmowych edytorów markdown 
> dlaczego format markdown jest standardem ery AI dowiesz się w trakcie kursu.
- [ ] **MarkEdit** — `https://github.com/MarkEdit-app/MarkEdit` (MacOS)
- [ ] **CotEditor** — `https://coteditor.com` (MacOS)
- [ ] **Ghostwriter** — `https://ghostwriter.kde.org` (Windows, MacOS, Linux)
- [ ] **MarkText** — `https://github.com/marktext/marktext` (Windows, MacOS, Linux)
- [ ] **Zettlr** — `https://zettlr.com` (Windows, MacOS, Linux)
- [ ] **Obsidian** — `https://obsidian.md` (Windows, MacOS, Linux)

---

## 📦 4. Pobierz materiały do kursu (paczka ZIP — 3 min)

Wszystkie szablony, ściągi i gotowe demonstracje są w **jednej paczce na GitHub**. Pobierasz ją jako **jeden plik ZIP** — nie musisz mieć konta GitHub ani nic instalować.

🔗 **Adres:** `https://github.com/jaroslawchodak/kurs-pe-materialy`

### Krok 1 — pobierz ZIP
- [ ] Wejdź pod powyższy adres w przeglądarce.
- [ ] Kliknij zielony przycisk **`< > Code`** (po prawej, nad listą plików).
- [ ] Z menu wybierz **`Download ZIP`**.
- [ ] Plik **`kurs-pe-materialy-main.zip`** pojawi się w folderze **Pobrane / Downloads**.

> 💡 Wolisz na skróty? Ten link pobiera ZIP od razu, bez klikania:
> `https://github.com/jaroslawchodak/kurs-pe-materialy/archive/refs/heads/main.zip`

### Krok 2 — rozpakuj i przenieś do folderu *Dokumenty*

**🍎 macOS:**
- [ ] Znajdź pobrany plik ZIP (Finder → *Pobrane*).
- [ ] **Kliknij go dwukrotnie** — rozpakuje się automatycznie obok, jako folder `kurs-pe-materialy-main`.
- [ ] Przeciągnij ten folder do ***Dokumenty*** (w bocznym pasku Findera).

**🪟 Windows:**
- [ ] Znajdź pobrany plik ZIP (Eksplorator plików → *Pobrane*).
- [ ] Kliknij go **prawym przyciskiem myszy** → ***Wyodrębnij wszystko…***
- [ ] W oknie wskaż lokalizację ***Dokumenty*** i kliknij ***Wyodrębnij***.

> ✅ **Gotowe, gdy:** w folderze *Dokumenty* masz folder `kurs-pe-materialy-main` (nazwę możesz skrócić do `kurs-pe-materialy`), a w środku trzy katalogi: **`kurs-pe`**, **`clustering-demo`**, **`summarizer-demo`**.
>
> 📖 Pliki kończące się na `.md` otwierasz **edytorem markdown z punktu 3**. Zacznij od pliku **`README.md`** w głównym folderze — to drogowskaz po całej paczce.

---

## ⚙️ 5. (Opcjonalnie) Pre-setup na Dzień 3 — dla chętnych ze sprzętem

Potrzebne **tylko**, jeśli chcesz aktywnie ćwiczyć z modelem **lokalnym** (Blok 10) i agentem (Blok 11). Przenosi ~15–20 min instalacji poza salę.

- [ ] Zainstaluj **Ollama** → `ollama.com`. Pobierz i uruchom instalator:
  - Windows: https://ollama.com/download/windows
  - macOS: https://ollama.com/download/mac

- [ ] Pobierz jeden mały model. **Windows** — otwórz *PowerShell*; **macOS** — otwórz *Terminal*; w obu wpisz **to samo** polecenie:
  ```bash
  ollama run gemma4:e4b-it-qat
  ```
  *(wymaga ~8–12 GB RAM/VRAM lub Apple Silicon z pamięcią zunifikowaną)*
  
- [ ] *(dla zaawansowanych)* zainstaluj co najmniej jednego agenta (środowisko agentowe): 
**Claude Code** https://claude.com/product/claude-code 
**Codex** https://openai.com/codex/ 
**Google Antigravity** https://antigravity.google
**OpenCode** https://opencode.ai 
> każdy ma wersję CLI i GUI/IDE (zacznij od wersji GUI/IDE)
### Który wybrać?
— jeśli posiadasz subskrypcję ChatGPT (OpenAI) - wybierz Codex
— jeśli posiadasz subskrypcję Claude (Anthropic) - wybierz Claude Code
— jeśli posiadasz subskrypcję Gemini (Google) - wybierz Antigravity
— jeśli nie posiadasz żadnej subskrypcji wybierz **Codex** (najlepszy plan w wersji darmowej) lub/i **OpenCode** (dostęp do kilku darmowych modeli open source).

> **Nie masz mocnego sprzętu? Nie szkodzi.** W każdym bloku jest wariant podstawowy **bez instalacji** — pre-setup to wygoda, nie warunek udziału. Artefakt zdobędziesz w zwykłym czacie.

> **🛠️ Coś nie zadziałało (logowanie, instalacja)? Nie walcz z tym sam.** Na **starcie Dnia 3** (i opcjonalnie pod koniec Dnia 2) jest **10-minutowa mini-klinika techniczna** — przyjdź wtedy, pomożemy uruchomić Ollama/agenta, żeby blok nie schodził na konfigurację. Pre-setup w domu jest mile widziany, ale nie obowiązkowy.

---

## 🔒 6. Karta BHP danych — przeczytaj przed Blokiem 1

Zanim wkleisz **cokolwiek** do narzędzia AI w chmurze, zadaj sobie jedno pytanie:

> ### *„Gdzie trafią te dane?"*

Trzy reguły obowiązujące przez cały kurs (rozwiniemy je w Blokach 4, 7 i 10):

| # | Reguła |
|---|---|
| 1 | **NIE wklejasz** danych osobowych, medycznych, niezanonimizowanych transkrypcji, cudzych recenzji ani materiałów pod NDA do publicznych modeli. |
| 2 | **Pracujesz na materiale jawnym** — na ćwiczeniach używamy danych jawnych albo zanonimizowanych. |
| 3 | **W razie wątpliwości — nie wklejaj.** Lepiej zapytać prowadzącego, niż cofać wyciek. |

> ⚠️ Wklejenie danych osobowych do modelu w chmurze to **przetwarzanie w rozumieniu RODO**.

---

## 🎒 Co przynieść na kurs

- [ ] Laptop z dostępem do internetu i przeglądarką.
- [ ] **Własny, jawny materiał badawczy** do ćwiczeń (np. artykuł PDF, fragment metod, 5–8 pozycji bibliografii z Zotero/Bookends) — najlepiej uczysz się na *swoich* tekstach. **Tylko materiał jawny lub zanonimizowany.**
- [ ] **Pobrane materiały do kursu** (punkt 4) — paczka `kurs-pe-materialy` w folderze *Dokumenty*.
- [ ] *(opcjonalnie)* wykonany pre-setup z punktu 5.

---

> ### Wchodzisz na kurs z dwiema rzeczami:
> 1. **działającym dostępem** do czterech narzędzi,
> 2. jednym odruchem: ***zanim wkleję — pytam, gdzie trafią dane.***
>
> Resztę zbudujemy razem. Do zobaczenia! 👋
