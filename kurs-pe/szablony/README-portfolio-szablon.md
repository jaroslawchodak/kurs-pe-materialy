# Katalog projektu — README i lista kontrolna (Blok 12.4)

> **Wersja 2 (28.10.2026).** Osobne „portfolio" zastąpił **katalog projektu** z Bloku 11, który budujesz przez trzy dni. Ten plik zapisz jako `README.md` w głównym folderze `moj-projekt/`. Lista kontrolna niżej służy do samooceny i sprawdzenia w parach na koniec kursu. Ocena jest formująca (informacja zwrotna, nie ranking). Nazwa pliku szablonu zostaje bez zmian, żeby nie psuć odsyłaczy.

---

## Struktura katalogu

```text
moj-projekt/
├── README.md              ← ten plik: opis projektu + lista kontrolna
├── CLAUDE.md              ← zasady stałe (5 sekcji); kopia lub odsyłacz jako AGENTS.md
├── CONTEXT.md             ← „tu jesteśmy": temat, etap, decyzje, następny krok
├── WORKFLOW.md            ← „tak to robimy": kroki i format wyniku
├── PROTOKOL-AI.md         ← osobisty protokół pracy z AI
├── prompty/               ← biblioteka promptów + README.md ze spisem
├── skills/                ← własne skills (Blok 12)
├── zrodla/                ← WEJŚCIE (tylko do odczytu dla agenta): czyste .md, matryca, JSON
├── notatki/               ← log akceptacji, dziennik weryfikacji, sygnalizator, brief
└── wyniki/                ← WYJŚCIE: wyłącznie to, co wytworzył agent
```

## O projekcie (2–3 zdania)
> Temat, pytanie badawcze, etap. Jakie dane są w `zrodla/` i jaki mają kolor (🟢/🟡).

---

## Lista kontrolna (samoocena → wymiana w parach, 10 min)

| # | W katalogu projektu jest… | Efekt | Kryterium | Ja | Para |
|---|---|---|---|---|---|
| 1 | `prompty/` z co najmniej 6 promptami w stałym formacie i spisem w `README.md`; przy jednym z nich dziennik iteracji v1→v3 | 1 | J | ☐ | ☐ |
| 2 | notatka o doborze narzędzi (mapa z B1 uzupełniona o wnioski z B9) | 2 | J | ☐ | ☐ |
| 3 | **dziennik weryfikacji** z B4 i B9 (twierdzenia, dowody z lokalizacją, werdykty) | 3 | H | ☐ | ☐ |
| 4 | **sygnalizator danych** z decyzją dla każdego 🔴 i datą sprawdzenia ustawień kont | 4, 9 | O | ☐ | ☐ |
| 5 | prompt w wersji Markdown i XML z regułą doboru formatu oraz co najmniej jeden plik danych w JSON | 5 | J | ☐ | ☐ |
| 6 | `zrodla/` z czystymi plikami `.md` po kontroli wierności | 6 | J | ☐ | ☐ |
| 7 | brief kontekstowy dla realnego zadania | 7 | J | ☐ | ☐ |
| 8 | matryca literatury z cytatami-kotwicami i zakotwiczony akapit | 8 | H | ☐ | ☐ |
| 9 | **`CLAUDE.md` (5 sekcji), `CONTEXT.md`, `WORKFLOW.md`; `zrodla/` oddzielone od `wyniki/`; `notatki/log.md` z punktem akceptacji; przetestowany `SKILL.md`** | 10 | J·O·H | ☐ | ☐ |
| 10 | **`PROTOKOL-AI.md` i oświadczenie o użyciu AI** | 10 | J·O·H | ☐ | ☐ |

**Kryteria:** **J** — jasność zadania (prompt, format) · **O** — ochrona danych (sygnalizator 🟢🟡🔴) · **H** — kontrola halucynacji (kotwice, weryfikacja).

**Warunek ukończenia kursu:** co najmniej 8 z 10 punktów, w tym obowiązkowo **3, 4, 9 i 10**.

## Pytania dla osoby sprawdzającej (para)
1. **J:** Czy z `CLAUDE.md` i `WORKFLOW.md` obca osoba wiedziałaby, co agent ma robić i gdzie zapisywać wyniki?
2. **O:** Czy w folderze udostępnianym agentowi nie ma danych 🔴? Czy folder nie jest synchronizowany z OneDrive/iCloud, jeśli są w nim dane 🟡?
3. **H:** Wybierz jedną tezę z `wyniki/` — czy jej cytat-kotwica naprawdę jest w pliku źródłowym?

## Następny krok (punkty niespełnione)
> Wpisz tu, czego brakuje, i przenieś to do `CONTEXT.md` jako plan pracy po kursie.

## Mój przepływ pracy (1 akapit)
> Opisz przebieg z Bloku 12.2: źródła → ekstrakcja → synteza → kontrola → wyjście (`.docx`). Co zrobił agent, co Ty?
