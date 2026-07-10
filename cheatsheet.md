# Ściągawka (*cheatsheet*) po szkoleniu

**Prompt engineering w badaniach naukowych** · kurs półwarsztatowy, 3 dni

> **Kompendium szkolenia** jest dostępne online pod adresem <https://jaroslawchodak.github.io/course-ai-research>, a komplet szablonów i skryptów — w repozytorium <https://github.com/jaroslawchodak/kurs-pe-materialy/>. Obie pozycje to **wersje rozwojowe**: będą sukcesywnie uzupełniane o nowe narzędzia i przykłady, dlatego warto wracać do nich także po zakończeniu kursu.

## 🆕 Co nowego po szkoleniu (aktualizacja materiałów)

Poniższe zmiany trafiły do kompendium i do repozytorium już po zajęciach. Żeby mieć je u siebie, pobierz świeżą paczkę (punkt 4) albo zajrzyj do wersji online.

- **OpenAI: Codex → „ChatGPT for desktop".** Od 9 lipca 2026 aplikacja Codex nosi nazwę **ChatGPT for desktop** i spina trzy tryby pracy: **Chat** (standardowy, jak w przeglądarce), **ChatGPT Work** (tryb agentowy dla początkujących i średnio zaawansowanych) oraz **ChatGPT Codex** (zaawansowany tryb programistyczny). Są to bezpośrednie odpowiedniki trzech trybów Claude Desktop od Anthropic: kolejno **Chat**, **Cowork** i **Claude Code**.
- **Zbiorcze (batch) parsowanie PDF.** Do konwersji wielu plików naraz służy nowy skrypt **`konwersja-batch.py`**: wskazujesz folder z PDF-ami, a otrzymujesz komplet plików `.md`. Instrukcja krok po kroku jest w pliku **`instrukcja-python.md` (Krok 5)**.
- **Nowa architektura szablonów umiejętności (skills).** Szablony wydzielono do osobnego katalogu **`./szablony-skills`** i zapisano w formacie **`[NAZWA_SKILL].md`** — dzięki temu dołączenie gotowej umiejętności do agenta sprowadza się do wskazania jednego, jednoznacznie nazwanego pliku.
- **Praca ze skillem na przykładzie `sylabus-fakultet`** (plik `SKILL.md`):
  1. w podkatalogu `/reference` **dostosuj plik `jak-pisac-sylabusy.md` do własnej dyscypliny** — to on niesie reguły wypełniania sylabusa;
  2. poproś agenta, by **zbudował nową umiejętność na podstawie trzech plików** z katalogu `sylabus-fakultet` i jego podkatalogu `/reference`: `SKILL.md`, `jak-pisac-sylabusy.md` oraz `fakultet-szablon.md`;
  3. wygenerowany **Prompt Wykonawczy (System Prompt)** odłóż we własnym katalogu **`/prompty`**, w dowolnym miejscu na dysku lokalnym.

---

## 🚀 Przygotowanie przed kursem (ściągawka przedkursowa)

> **To zaktualizowana wersja ściągawki `cheatsheet-przed-kursem.md`** — rozszerzona **w trakcie kursu** (po Dniu 1) o czynności, o które prosili uczestnicy. Jeśli przygotowanie przedkursowe masz już za sobą, wróć tylko do **nowych pozycji** poniżej.

> **Po co to?** Żeby kolejne bloki nie schodziły na instalacje i logowanie. Wchodzisz na salę z działającymi narzędziami i jednym odruchem ochrony danych. **Nie musisz niczego umieć z góry — to tylko przygotowanie dostępu.**

---

## 🆕 Co nowego względem ściągawki przedkursowej

Tych pozycji **nie było** w `cheatsheet-przed-kursem.md` :

- [ ] **Nowe pliki i katalogi ćwiczeń w paczce `kurs-pe/`** — zaktualizuj lokalną paczkę → *punkt 4 → „Aktualizacja"*
- [ ] **Komercyjne edytory markdown** (dla chętnych) — iA Writer, Typora → *punkt 3a*
- [ ] **Instalacja Pythona 3** (Windows i macOS) → *punkt 5*
- [ ] **Parser PDF → Markdown `pymupdf4llm`** (przyda się w Bloku 6, Dzień 2) → *punkt 5*
- [ ] **LM Studio** — graficzna („klikalna") alternatywa dla Ollama przy modelu lokalnym → *punkt 6*

> Reszta ściągawki (konta, edytory darmowe, paczka ZIP, karta BHP danych) jest bez zmian — jeśli masz to z domu, możesz pominąć.

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

## 3a.  (Opcjonalnie - dla chętnych) możesz przetestować komercyjne wersje edytorów markdown
- [ ] **iA Writer** — `https://ia.net/writer` (Windows, MacOS)
- [ ] **Typora** — `https://typora.io` (Windows, MacOS, Linux)

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

### 🔄 Aktualizacja — w trakcie kursu doszły NOWE pliki i katalogi

> **W paczce `kurs-pe/` przybyło materiałów** dodanych w trakcie kursu — m.in.:
> - **`kurs-pe/materialy-dyscyplinarne/`** — trzy tory ćwiczeń (**tor-a** ścisłe/przyrodnicze · **tor-b** społeczne · **tor-c** humanistyka) z gotowymi materiałami i wzorcowym rozwiązaniem,
> - **`kurs-pe/sciezka-literatury.md`** — spójna ścieżka pracy z literaturą,
> - **`kurs-pe/pulapki/prompt-injection-demo.md`** — demonstracja ataku na agenta,
> - nowe szablony w **`kurs-pe/szablony/`** (biblioteka promptów, protokół weryfikacji źródeł),
> - **`kurs-pe/00_start/instalacje-win-mac.md`** (checklista instalacji w dwóch kolumnach) i **`plan-b-darmowe-konta.md`**.

Najprostszy sposób (dla wszystkich — **nie wymaga GitHub ani gita**): **pobierz paczkę ZIP jeszcze raz** i podmień folder.

- [ ] Powtórz **Krok 1 i Krok 2** z góry (pobierz świeży ZIP → rozpakuj).
- [ ] W *Dokumentach* **zastąp** stary folder `kurs-pe-materialy` nowym.
  > 🍎 macOS: przeciągnij nowy folder na stary → *„Scal / Zastąp"*. 🪟 Windows: przy kopiowaniu wybierz *„Zastąp pliki w miejscu docelowym"*.
- [ ] Nie chcesz nadpisywać? **Zmień nazwę** starego folderu (np. `kurs-pe-materialy-STARE`) i rozpakuj nowy obok — potem porównasz.

> 🔒 **Twoja praca jest bezpieczna.** Materiały kursowe to zasób „tylko do czytania" — swoje notatki, prompty i artefakty trzymasz w **osobnym** folderze `moj-warsztat/` (poza paczką). Ponowne pobranie ZIP **niczego Twojego nie skasuje**. Jeśli edytowałeś coś *wewnątrz* paczki, najpierw skopiuj to gdzie indziej.
>
> 💻 **Dla znających `git`** (jeśli pobierałeś przez `git clone`, nie ZIP): wystarczy w folderze paczki wpisać `git pull` — dociągnie tylko zmiany.

---

## 🐍 5. 🆕 Zainstaluj Python 3 i parser PDF → Markdown (`pymupdf4llm`)

> **Nowość (prośba z Dnia 1).** Przyda się w **Bloku 6** (Dzień 2), gdzie zamieniamy własny PDF na czysty Markdown gotowy dla modelu. Instalatory są graficzne, a cała „obsługa" to jedna komenda. **Kto nie chce instalować Pythona — nie musi:** na sali jest wariant awaryjny („prompt czyszczący" w czacie), a rano na Dniu 3 działa mini-klinika techniczna.
>
> 🔒 **Zaleta prywatności:** `pymupdf4llm` działa **w całości na Twoim komputerze** — PDF nie jest wysyłany do chmury.

### Krok 1 — zainstaluj Python 3

- [ ] 🪟 **Windows:** zainstaluj ze sklepu **Microsoft Store** (wyszukaj „Python 3") albo instalatorem z `https://www.python.org/downloads/`.
  > ⚠️ Instalując z python.org **koniecznie zaznacz `Add python.exe to PATH`** na pierwszym ekranie instalatora — bez tego komenda `pip` z Kroku 2 nie zadziała.
- [ ] 🍎 **macOS:** zainstaluj z `https://www.python.org/downloads/` (system ma wbudowany `python3`, ale świeża wersja jest wygodniejsza).

Sprawdź, że działa — otwórz **PowerShell** (🪟 menu Start → „PowerShell") / **Terminal** (🍎 Spotlight `⌘Space` → „Terminal") i wpisz:

```
🪟 Windows:  python --version
🍎 macOS:    python3 --version
```

Powinna wyświetlić się wersja, np. `Python 3.13.x`.

### Krok 2 — zainstaluj bibliotekę `pymupdf4llm`

W tym samym oknie (PowerShell / Terminal) wpisz **jedną** komendę:

```
🪟 Windows:  pip install pymupdf4llm
🍎 macOS:    pip3 install pymupdf4llm
```

> ✅ **Gotowe, gdy:** komenda kończy się bez czerwonego błędu (`Successfully installed …`). To najlżejszy parser — nie wymaga karty graficznej ani modeli AI i pokrywa większość artykułów z natywną warstwą tekstu. Na Bloku 6 użyjemy gotowego skryptu `konwersja.py` z paczki (`kurs-pe/konwersja/`). *Parser dla trudniejszych PDF-ów (tabele, skany) poznasz na sali.*

---

## ⚙️ 6. (Opcjonalnie) Pre-setup na Dzień 3 — dla chętnych ze sprzętem

Potrzebne **tylko**, jeśli chcesz aktywnie ćwiczyć z modelem **lokalnym** (Blok 10) i agentem (Blok 11). Przenosi ~15–20 min instalacji poza salę.

- [ ] Zainstaluj **Ollama** → `ollama.com`. Pobierz i uruchom instalator:
  - Windows: https://ollama.com/download/windows
  - macOS: https://ollama.com/download/mac

- [ ] 🆕 **Wolisz klikać niż wpisywać komendy? Zainstaluj LM Studio** → `https://lmstudio.ai` — graficzna alternatywa dla Ollama (ten sam efekt: model działa **lokalnie**, dane nie opuszczają komputera). 🪟 Windows: pobierz `.exe`; 🍎 macOS: pobierz `.dmg` → przy pierwszym uruchomieniu **prawy klik → „Otwórz"**. Modele pobierasz i uruchamiasz z okna aplikacji — bez terminala.
  > Wystarczy **jedno** z dwóch: Ollama **albo** LM Studio. Na sali pokaz robimy w LM Studio (wygląda identycznie na Windows i macOS).

- [ ] Pobierz jeden **mały, lekki** model. **Windows** — otwórz *PowerShell*; **macOS** — otwórz *Terminal*; wpisz **jedno** z poleceń:
  ```bash
  ollama run gemma4:e2b
  ```
  albo
  ```bash
  ollama run granite4.1:3b
  ```
  *(oba działają na laptopie z ~8 GB RAM; Apple Silicon z pamięcią zunifikowaną — bez problemu). W LM Studio wybierz analogicznie mały model (2–3 mld parametrów, np. Gemma 2B lub Granite 3B).*
  
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

## 🔒 7. Karta BHP danych

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
- [ ] *(opcjonalnie)* wykonane instalacje z punktów 5–6: Python + parser `pymupdf4llm` (Blok 6) oraz model lokalny Ollama/LM Studio (Bloki 10–11).

---

> ### Wchodzisz na kurs z dwiema rzeczami:
> 1. **działającym dostępem** do czterech narzędzi,
> 2. jednym odruchem: ***zanim wkleję — pytam, gdzie trafią dane.***
>
> Resztę zbudujemy razem. Do zobaczenia! 👋
