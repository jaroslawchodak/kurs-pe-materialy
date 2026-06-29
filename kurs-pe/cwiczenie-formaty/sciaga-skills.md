# Ściąga — Skills (umiejętności agenta)

**Skill (umiejętność)** to zapisana w pliku `SKILL.md` instrukcja-procedura, którą agent (np. Claude Code) **ładuje dopiero wtedy, gdy jest potrzebna**, i wykonuje na żądanie. W odróżnieniu od pliku kontekstowego (`CLAUDE.md`/`CONTEXT.md`), który opisuje *stan rzeczy* i jest czytany zawsze, Skill opisuje *powtarzalną czynność* i „kosztuje" kontekst tylko w chwili użycia.

> Po ludzku: jeśli wciąż wklejasz tę samą wielokrotną instrukcję albo checklistę do czatu — zamień ją w Skill. Raz opisana procedura, wywoływana komendą.

## Kiedy warto utworzyć Skill
- powtarzasz tę samą procedurę (np. streszczanie artykułu wg stałej struktury, audyt cytowań, budowa wiersza matrycy),
- sekcja `CLAUDE.md` rozrosła się z *faktu* do *procedury*,
- chcesz, żeby krok był uruchamiany świadomie, na komendę, a nie „przy okazji".

## Anatomia (minimum)
```
moja-umiejetnosc/
└── SKILL.md          # instrukcja (wymagana)
    ├── (opcjonalnie) szablon.md, przyklady/, scripts/
```

`SKILL.md` zaczyna się od krótkiego nagłówka YAML:
```yaml
---
name: streszczenie-artykulu
description: Streszcza artykuł naukowy wg stałej struktury i reguł grounding. Użyj, gdy mam plik .md z tekstem do streszczenia.
---

Streść wskazany plik .md zgodnie z regułami:
1) każdy akapit kończ tagiem referencyjnym ze źródłem,
2) nie dodawaj twierdzeń spoza tekstu,
3) brakujące sekcje oznacz „N/A".
```
- `description` decyduje, **kiedy** agent sięgnie po Skill — pisz w nim słowa, których realnie użyjesz.
- Wywołanie ręczne: `/streszczenie-artykulu` (lub agent sam, gdy zadanie pasuje do opisu).

## Demonstracja w kursie (Blok 11)
Dwie gotowe umiejętności prowadzącego, uruchamiane jednym poleceniem — pokazują, że Skill = **spakowana procedura badawcza**:

```
Use bridge-finder skill
Find non-obvious bridges around `sycophancy`
```
```
Use knowledge-gap-finder skill
Find knowledge gaps for `sycophantic-ai`
```
Efekt: agent przeszukuje *Twoje* notatki i tworzy nowe **knowledge chunks** (zwięzłe notatki-cegiełki: most między pojęciami albo nazwana luka badawcza), które wracają do bazy wiedzy.

## Skills · MCP · Python — trzy mechanizmy rozszerzania agenta
- **Skills** — *co* agent ma zrobić (powtarzalna procedura w `SKILL.md`).
- **MCP** — *do czego* agent sięga (bezpieczny dostęp do zewnętrznych źródeł/narzędzi, np. bazy DEVONthink).
- **Skrypty Pythona** — *czym* liczy/przetwarza (deterministyczna praca: konwersja PDF→MD, parsowanie, obliczenia).

## Granica (zasada kursu)
Skill nie zwalnia z nadzoru. Procedura zaszyta w `SKILL.md` musi zawierać reguły grounding i ochrony danych — inaczej skaluje błąd zamiast pracy. Por. „pięć reguł" z `INSTRUKCJE-PROJEKTU-szablon.md` i rozdział „Etyka i granice AI".
