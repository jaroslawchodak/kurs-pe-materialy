# Skills do pracy badawczej (Blok 12)

> **Skill** to powtarzalna procedura zapisana w pliku `SKILL.md`. Agent zna na co dzień tylko nazwę i opis skilla, a pełną treść wczytuje, gdy zadanie do niego pasuje albo gdy wpiszesz `/nazwa`. Reguła kciuka: *powtarzasz? zrób skill; jednorazowe? zostaw prompt.*

## Spis

| Skill | Typ procedury | Wejście → wyjście | Blok |
|---|---|---|---|
| [`streszczenie-z-tagami`](streszczenie-z-tagami/SKILL.md) | ekstrakcja | `zrodla/md/X.md` → `wyniki/streszczenia/X.md` z tagiem źródła przy każdym akapicie | B6 |
| [`wiersz-matrycy`](../cwiczenie-formaty/skill-wiersz-matrycy.md) | ekstrakcja | plik źródła → wiersz matrycy z cytatem-kotwicą | B8 |
| [`kwerenda-literatury`](kwerenda-literatury/SKILL.md) | wyszukiwanie | protokół kwerendy → raport + `kandydaci.json` + dziennik zapytań | B9 |
| [`weryfikacja-twierdzen`](weryfikacja-twierdzen/SKILL.md) | kontrola | tekst + `zrodla/` → dziennik weryfikacji (werdykty do zatwierdzenia przez badacza) | B4 |
| [`kodowanie-wg-ksiazki-kodow`](kodowanie-wg-ksiazki-kodow/SKILL.md) | analiza jakościowa | materiał zanonimizowany + `kody.md` → tabela kodowań z cytatami | B8 |
| [`analiza-opisowa`](analiza-opisowa/SKILL.md) | analiza ilościowa | `dane/*.csv` → skrypt w `analiza/` + `wyniki/statystyki.md` + STAT-5 | B8 |
| [`recenzja-metodologiczna`](recenzja-metodologiczna/SKILL.md) | kontrola (autor ≠ recenzent) | szkic → raport recenzji, bez poprawiania tekstu | B4, B11 |
| [`eksport-do-worda`](eksport-do-worda/SKILL.md) | format | `wyniki/*.md` → `.docx` (pandoc) i `.xlsx` (`scripts/md2xlsx.py`) | B6 |
| [`research-ideation`](research-ideation/SKILL.md) | scenariusz rozmowy | pomysł → plan badania (szablon do adaptacji) | B12 (pokaz) |
| [`paper-reviewer`](paper-reviewer/SKILL.md) | symulacja wielu ról | tekst → recenzja pięciu ról (szablon do adaptacji) | B12 (pokaz) |
| [`sylabus-fakultet`](sylabus-fakultet/SKILL.md) | generator dokumentu z auto-weryfikacją | źródła → sylabus wg wzorca (szablon do adaptacji) | B12 (pokaz) |

Osiem pierwszych folderów to **gotowe skills do instalacji** (plik zaczyna się od nagłówka `---` z nazwą i opisem). Trzy ostatnie to **szablony do adaptacji**: treść skilla jest w bloku kodu, który kopiujesz do własnego `SKILL.md`.

## Jak zainstalować

> **Aplikacja Claude (czat i Cowork; Windows i macOS tak samo):** spakuj folder skilla do `.zip` (🪟 prawy klik → **Wyślij do** → **Folder skompresowany** · 🍎 prawy klik → **Kompresuj**) → **Ustawienia → Dostosuj (*Customize*) → Skills → „+" → Prześlij**.
>
> **Claude Code:** skopiuj folder do `.claude/skills/` w katalogu projektu albo do katalogu domowego: 🪟 `C:\Users\<nazwa>\.claude\skills\` · 🍎 `~/.claude/skills/`. Folder `.claude` jest ukryty: 🪟 Eksplorator → **Widok → Pokaż → Ukryte elementy** · 🍎 Finder `⌘⇧.`.
>
> **Codex (ChatGPT):** format `SKILL.md` jest zgodny; wskaż agentowi folder ze skillem lub poproś o instalację. Miejsce zapisu sprawdź w aktualnej dokumentacji Codexa.
>
> **Bez instalacji (każdy czat):** wklej treść `SKILL.md` z poleceniem „Działaj dokładnie według tej procedury".

## Zanim użyjesz skilla
1. **Przeczytaj cały `SKILL.md`** (i pliki w `reference/`, `scripts/`) — tak samo jak każdy skill pobrany z internetu.
2. **Dostosuj** opis-wyzwalacz i ścieżki folderów do swojego katalogu projektu.
3. **Przetestuj** na kopii folderu z danymi 🟢 i zapisz poprawki w sekcji „Uwagi po testach" swojej biblioteki promptów.
4. Skills nie zmieniają zasad: do folderu agenta trafiają tylko dane 🟢 i 🟡, a werdykty, interpretacje i decyzje badawcze należą do badacza.
