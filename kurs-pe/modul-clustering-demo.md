# Moduł kursu: Clustering Demo — agent w działaniu

> **Plik-wskaźnik (pointer).** Pełny, sprawdzony pipeline znajduje się w katalogu **`../clustering-demo`** i NIE jest tu kopiowany — pracujemy na źródle, żeby nie duplikować plików.
> Ten moduł realizujemy jako **demonstrację na żywo** (Dzień 3, blok integracyjny). Spina cały kurs: prompt → kontekst → nadzorowany agent nad plikami.

---

## Po co ten moduł

Pokazuje, jak **agent AI** wykonuje realne, wieloetapowe zadanie badawcze: czyta zbiór streszczeń literatury, **grupuje je tematycznie (klastrowanie)**, wykrywa napięcia i luki, a na końcu zapisuje dwa artefakty: raport (`report.md`) i strukturę przeglądu (`outline.opml`).

To zwieńczenie łuku kursu — uczestnik widzi, że agent to nie magia, lecz **prompt + kontekst + pliki instrukcji + nadzór człowieka**, które już zna z bloków 1–11.

## Struktura pipeline'u (w `../clustering-demo`)

| Element | Rola |
|---|---|
| `AGENTS.md` | Profil agenta: rola „Principal Research Synthesizer", kompetencje, ton, reguły (grounding, format). |
| `CONTEXT.md` | Wiedza dziedzinowa: pogranicze AI i nauk społecznych, oczekiwane osie tematyczne. |
| `WORKFLOW.md` | Dokładna procedura krok po kroku + wymagana struktura outputu każdego klastra. |
| `EXECUTION-PROMPT.md` | Prompt wykonawczy uruchamiający cały proces. |
| `README.md` | Opis projektu i instrukcja startu. |
| `./summaries/` | **Wejście:** streszczenia artykułów `*.md` do sklastrowania. |
| `./outputs/` | **Wyjście:** `report.md` + `outline.opml`. |
| `./agent_logs/` | Ślad rozumowania agenta (przejrzystość). |

## Wykonawcy (do wyboru)

Pipeline jest **agnostyczny względem narzędzia** — uruchomisz go dowolnym agentem nad plikami:

- **Claude Code / Claude Cowork** — główny rekomendowany.
- **Codex**.
- **Antigravity** (dostęp do nowych modeli Gemini oraz cenionych starszych: Opus 4.6, Sonnet).
- **OpenCode** — w połączeniu z **modelem lokalnym** (Ollama) **albo** z darmowymi modelami dostępnymi w OpenCode (m.in. od Nvidii).

> **`privacy cage`:** uruchomienie z modelem **lokalnym** = streszczenia nie opuszczają komputera. Idealne dla materiałów wrażliwych.

## Jak uruchomić (skrót)

1. Umieść streszczenia `*.md` w `./summaries/` (na demo: 50–100 plików dla pełniejszego „wrażenia" możliwości agentic-LLM).
2. Wczytaj pliki systemowe (`AGENTS.md`, `CONTEXT.md`, `WORKFLOW.md`) do kontekstu agenta.
3. Odpal `EXECUTION-PROMPT.md`.
4. Sprawdź `./outputs/report.md` i `./outputs/outline.opml` oraz logi w `./agent_logs/`.

## Powiązania z kursem
- Blok 2 (struktura promptu) → `EXECUTION-PROMPT.md`.
- Blok 8 (RAG, matryca, OPML jako struktura) → `outline.opml`.
- Blok 11 (instrukcje projektowe, człowiek-w-pętli) → `AGENTS.md` + logowanie.
- Blok 10 (lokalne LLM) → uruchomienie offline przez OpenCode + Ollama.
