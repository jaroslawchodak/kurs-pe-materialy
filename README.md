# Materiały do kursu „Prompt engineering w badaniach naukowych"

> **Od pojedynczych zapytań do agentów AI i inżynierii kontekstu**

To repozytorium zawiera **gotowe szablony, ściągi i demonstracje agentów AI**, których używamy podczas kursu. Możesz pobrać całość jako jeden plik ZIP i pracować lokalnie na swoim komputerze.

---

## Jak pobrać (najprostsza droga — ZIP)

1. Na górze tej strony kliknij zielony przycisk **`< > Code`**.
2. Wybierz **`Download ZIP`**.
3. Plik `kurs-pe-materialy-main.zip` trafi do folderu **Pobrane / Downloads**.
4. Rozpakuj i przenieś folder do katalogu **Dokumenty**:
   - **macOS:** dwuklik na pliku ZIP rozpakuje go automatycznie → przeciągnij folder do `Dokumenty`.
   - **Windows:** prawy przycisk myszy → *Wyodrębnij wszystko…* → wskaż `Dokumenty`.

> Po rozpakowaniu folder będzie się nazywał `kurs-pe-materialy-main` — możesz zmienić nazwę na `kurs-pe-materialy`.

---

## Co jest w środku

| Katalog | Zawartość |
|---|---|
| **`kurs-pe/`** | Szablony (briefy kontekstowe, protokół AI, sygnalizator danych, dziennik weryfikacji, prompt wyszukiwawczy, lista kontrolna katalogu projektu), ściągi (Markdown, XML, parsery, skills), skrypty konwersji (PDF → Markdown, Markdown → Excel) i ćwiczenia. To „skrzynka z narzędziami" uczestnika. |
| **`kurs-pe/szablony-skills/`** | Gotowe **skills** do pracy badawczej (streszczenie, kwerenda, weryfikacja twierdzeń, kodowanie jakościowe, analiza opisowa, recenzja, eksport do Worda) i szablony do adaptacji. Instrukcja instalacji w `README.md` katalogu. |
| **`kurs-pe/dla-chetnych/`** | Ćwiczenia rozszerzające DC-1 … DC-14 — do wykonania po zajęciach albo gdy skończysz minimum na sali. |
| **`clustering-demo/`** | Pełne demo **agenta AI** w działaniu (Dzień 3): czyta streszczenia literatury, grupuje je tematycznie, wykrywa napięcia i luki, zapisuje raport oraz strukturę przeglądu. Zawiera profil agenta, kontekst, workflow i prompt wykonawczy. |
| **`summarizer-demo/`** | Demo **kontrolowanego streszczania** literatury — prompty (PL/EN) i profil agenta. |

### Dema agentowe — od czego zacząć
Każde demo ma własny opis. Zacznij od pliku **`README.md`** (lub `AGENTS.md`) w danym katalogu.

Pliki w demach (`AGENTS.md`, `CONTEXT.md`, `WORKFLOW.md`, `EXECUTION-PROMPT.md`) są **agnostyczne względem narzędzia** — uruchomisz je dowolnym agentem nad plikami (Claude Code, Codex, Antigravity, OpenCode + model lokalny).

> **Prywatność — sygnalizator danych 🟢🟡🔴:** zanim udostępnisz agentowi folder, nadaj danym kolor (szablon: `kurs-pe/szablony/sygnalizator-danych-szablon.md`). Agenci w chmurze (Claude Code, Codex, ChatGPT Work, Claude Cowork) czytają pliki z Twojego dysku, ale ich treść wysyłają do modelu w chmurze — w folderze mogą być tylko dane 🟢 i 🟡. Dla danych 🔴 uruchom demo z modelem **lokalnym** (np. OpenCode + Ollama): materiały nie opuszczają wtedy komputera.

---

## Zasada ograniczonego zaufania

AI traktujemy jako **asystenta roboczego pod nadzorem człowieka** — nie jako autonomiczny autorytet. Każdy wynik weryfikuj, a źródła sprawdzaj. **Nie wklejaj** danych osobowych, medycznych, niezanonimizowanych transkrypcji ani materiałów objętych NDA do publicznych modeli AI.
