# 📖 Słowniczek pojęć AI

Krótkie, „ludzkie" definicje pojęć używanych na kursie — do zaglądania w razie potrzeby. Pojęcia są dwojakiego rodzaju:

- **rdzeń (bez oznaczenia)** — musisz je rozumieć, by wykonać ćwiczenia (token, prompt, zakotwiczenie (grounding), halucynacja, kontekst, RAG, agent…).
- 📚 **horyzont (dla chętnych)** — pogłębienia, które *tłumaczą* mechanizm, ale nie są niezbędne do pracy (MoE, kwantyzacja, uprzęż (harness)…). Pominięcie niczego nie blokuje.

Przy pięciu najtrudniejszych pojęciach jest 🔑 **metafora** — punkt zaczepienia dla pamięci.

| Termin | Po ludzku |
|---|---|
| **Token** | Najmniejszy kawałek tekstu, którym operuje model (≈ 3/4 słowa). 🔑 *Metafora:* **sylaba**, którą model czyta i przewiduje — układa tekst kawałek po kawałku, nie „rozumie zdania naraz” (stąd potrafi zmyślać płynnie). |
| **Prompt** | Instrukcja dla modelu — to, co wpisujesz, żeby uzyskać odpowiedź. |
| **Okno kontekstowe** | Ile tekstu model „widzi” naraz. Duże ≠ dobra pamięć — jakość spada na bardzo długim kontekście. 🔑 *Metafora:* **biurko o ograniczonej powierzchni** — im więcej walających się papierów, tym łatwiej zgubić właściwy. |
| **Kontekst** | Wszystko, co podajesz modelowi razem z pytaniem (tekst źródłowy, dane, przykłady, instrukcje) — materiał, na którym ma się oprzeć. |
| **Inżynieria kontekstu** | Decyzja, *jaką konfigurację* informacji podać modelowi, by uzyskać pożądane zachowanie. 🔑 *Metafora:* **przygotowanie biurka przed pracą zastępcy** — nie chodzi o to, *jak* poprosisz, lecz *co położysz na biurku*: za mało = zgaduje, za dużo = gubi się w stosie. |
| **Zaśmiecenie kontekstu (*context rot*)** | Spadek jakości, gdy w oknie kontekstowym narasta nadmiarowy, zaszumiony tekst. Dlatego „minimalny, ale wystarczający” kontekst bije „wszystko na raz”. |
| **Halucynacja** | Zmyślenie przedstawione z pełną pewnością — brzmi wiarygodnie, ale nie ma pokrycia w faktach. |
| **Zakotwiczenie / ugruntowanie (*grounding*)** | Oparcie odpowiedzi na *podanym* materiale i sprawdzalnych źródłach, a nie na „pamięci” modelu. |
| **RAG** | *Retrieval-Augmented Generation* — najpierw wyszukaj właściwe fragmenty, potem każ modelowi odpowiedzieć **tylko na ich podstawie**. 🔑 *Metafora:* **egzamin z otwartą książką — ale wyłącznie z Twoją książką** |
| **Dzielenie na fragmenty (*chunking*)** | Cięcie długiego materiału na mniejsze kawałki, którymi łatwiej nakarmić model. |
| **Streszczanie (*summarizer*)** | Procedura zamiany długiego tekstu w uporządkowane, zakotwiczone w źródle streszczenie — punkt wejścia do matrycy literatury i pracy z RAG. |
| **Matryca literatury** | Tabela, w której każdemu źródłu odpowiada wiersz z ustalonymi polami (np. teza, metoda, wynik, cytat-kotwica). Podstawa zakotwiczonego przeglądu — model syntetyzuje **Twoją** tabelę, zamiast zmyślać źródła. |
| **Parser** | Narzędzie, które wydobywa treść z PDF/DOCX/skanu do czystego Markdown (usuwa numery stron, stopki, śmieci OCR), zanim model to przeczyta. |
| **Gemini Notebook** (dawniej NotebookLM) | Narzędzie Google: wczytuje wiele źródeł i odpytuje je z zakotwiczeniem w nich; generuje notatki, slajdy, audio/wideo. Działa w chmurze → wgrywasz tylko źródła jawne. |
| **Agent** | Model z narzędziami (czyta/zapisuje pliki, wyszukuje) i instrukcją, wykonujący wieloetapowe zadania. 🔑 *Metafora:* **asystent z dostępem do szafy z dokumentami i listą procedur** — czyta i odkłada pliki, ale tylko wedle spisanych reguł i tylko za Twoją zgodą na każdym kroku. |
| **Model agentyczny vs chatbot** | Agentyczny potrafi wywoływać narzędzia, trzymać format i działać w pętli; chatbot świetnie rozmawia, ale w roli agenta zawodzi. |
| **MCP** | *Model Context Protocol* — standard bezpiecznego sięgania modelu do zewnętrznych źródeł i narzędzi. |
| **Umiejętność (*skill*)** | Powtarzalna procedura zapisana w pliku `SKILL.md`, którą agent ładuje *na żądanie* i uruchamia komendą `/nazwa`. |
| **Plik kontekstowy („konstytucja projektu”)** | Stały plik instrukcji agenta (`CLAUDE.md` / `CONTEXT.md` / `AGENTS.md` / `WORKFLOW.md`) opisujący rolę, zasady i procedurę. Agent czyta go na starcie każdej sesji. |
| 📚 **Uprzęż (*harness*)** | *Rusztowanie* wokół modelu: pętla działania, wywoływanie narzędzi, zarządzanie kontekstem i pamięcią, dostęp do plików. To ono z „gołego” modelu czyni agenta. Claude Code, Cursor, OpenCode to różne uprzęże nad *tym samym* modelem. |
| 📚 **Hak (*hook*)** | Krótki skrypt uruchamiany **automatycznie** przez uprzęż przy zdarzeniu w cyklu pracy agenta (np. *przed każdym* odczytem pliku), działający **deterministycznie** — niezależnie od tego, co model „postanowi”. Twardy bezpiecznik tam, gdzie reguła w prompcie bywa zawodna: np. blokuje wczytanie danych osobowych do okna kontekstowego. |
| 📚 **MoE** | *Mixture of Experts*, mieszanka ekspertów — model aktywujący dla danego tokenu tylko część parametrów („ekspertów”). Lżejszy dla sprzętu niż model gęsty (*dense*) o tej samej wielkości. |
| 📚 **Kwantyzacja** | Kompresja wag modelu (mniej bitów) → mniej RAM kosztem nieco niższej jakości; `Q4` / `qat` to zwykle najlepszy kompromis. |
| **Sygnalizator danych 🟢🟡🔴** | Trzy pytania przed wklejeniem danych lub udostępnieniem folderu: czy da się rozpoznać osobę? czy obiecałem poufność? czy to niepublikowane i cenne? Kolor wyznacza dozwolone narzędzie: 🟢 dowolne, 🟡 tylko z wyłączonym trenowaniem lub lokalnie, 🔴 nie do chmury. Zastępuje dawną „klatkę prywatności” (*privacy cage*). |
| **Drabina weryfikacji** | Pięć szczebli sprawdzania źródła: istnienie → metadane → teza → metoda i liczby → status (wycofanie, recepcja). |
| **Pseudonimizacja (klucz zastępczy)** | Zastąpienie bezpośrednich identyfikatorów neutralnym kodem (np. `R-017`); mapę kod → dane osobowe trzymasz lokalnie, poza promptem. |
| **Oświadczenie o użyciu AI (*AI disclosure*)** | Jawny opis, co w pracy zrobił człowiek, a co narzędzie — element rzetelności naukowej. |

---
