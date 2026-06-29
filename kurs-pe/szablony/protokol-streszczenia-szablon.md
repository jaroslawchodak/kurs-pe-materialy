# Szablon — protokół streszczania artykułu naukowego (summarizer)

**Summarizer** to powtarzalna procedura: model zamienia długi tekst naukowy w **ustrukturyzowane streszczenie gotowe do dalszej analizy** (wejście do matrycy literatury i RAG). Sens jest taki sam jak w całym kursie: streszczenie ma być *zakotwiczone w źródle i sprawdzalne*, a nie „opowiedziane z pamięci modelu".

Działający przykład tej procedury masz w katalogu `summarizer-demo/` (`AGENTS.md` + `summarize-prompt.md` + `summarizer-BIG-prompt.md`).

## Co MUSI zawierać dobry prompt/plik do streszczenia
1. **Rola + reguła grounding** — „streszczasz wiernie, nie oceniasz, nie dodajesz twierdzeń spoza tekstu".
2. **Ślad do źródła w każdym akapicie** — tag referencyjny `{Autor, Rok #ID}` (a gdy dostępne znaczniki `== page N ==` — z numerem strony `@N`). To operacjonalizacja kryterium kontroli halucynacji.
3. **Stała struktura wyjścia** (poniżej) — żeby każde streszczenie było porównywalne między artykułami.
4. **Reguła „N/A"** — brakującej sekcji nie wymyślamy (np. artykuł teoretyczny bez danych empirycznych → metodologia „N/A").
5. **Język = język artykułu** (tekst EN → streszczenie EN; PL → PL).
6. **Zakaz parafrazy terminów** — zachowaj terminologię dziedzinową bez „upraszczania".

## Struktura wyjścia (rekomendowana)
```
### METADANE         (tytuł, autorzy, rok, źródło, DOI, typ, dyscyplina)
### PROBLEM BADAWCZY  (luka / pytanie / motywacja)
### RAMA TEORETYCZNA  (nazwane teorie i modele)
### METODOLOGIA       (podejście, metoda, dane/próba, analiza)
### KLUCZOWE USTALENIA (3–6 akapitów; konkretne liczby/efekty, każdy z tagiem źródła)
### POJĘCIA I DEFINICJE (**Termin** — definicja jak w tym artykule)
### POWIĄZANIA I IMPLIKACJE (co autorzy twierdzą; ograniczenia)
### TAGI              (3–8, do cross-referencji)
```

## Dwa tory uruchomienia (demonstracja z Bloku 6)
- **Długi prompt samowystarczalny** (`summarizer-BIG-prompt.md`) — całość reguł i wzorzec w jednym; dobry do czatu / pojedynczego uruchomienia w Codex/Claude Code.
- **Krótki prompt wykonawczy + reguły w pliku** (`summarize-prompt.md` + `AGENTS.md`) — agent czyta `AGENTS.md` (stałe reguły) i wykonuje krótkie polecenie. To wzorzec „prompt wykonawczy ↔ plik kontekstowy" z Bloku 11.

## Lokalnie czy w chmurze? (decyzja `privacy cage`)
- **Lokalnie** (materiały wrażliwe): model lokalny (Ollama) lub **AI Document Assistant w DEVONthink** — tekst nie opuszcza komputera.
- **Komercyjnie** (materiał jawny, publikowany): silniejszy model frontier dla trudnych, długich artykułów.

## Powiązania
- Wynik tej procedury = wejście do **matrycy literatury** (Blok 8) i do **agenta klastrującego** (`clustering-demo/`, Blok 11).
- Możesz spakować tę procedurę jako **Skill** (`sciaga-skills.md`).
