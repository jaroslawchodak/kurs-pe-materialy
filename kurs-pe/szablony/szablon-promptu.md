# Szablon promptu — struktura 4-warstwowa

> Wypełnij cztery warstwy w kolejności. Każda warstwa odpowiada na inne pytanie modelu.
> Buduj iteracyjnie: uruchom → znajdź błąd → popraw jedną warstwę → uruchom ponownie.

---

## WARSTWA 1 — Rola i ton
*Kim ma być model i jak ma mówić?*

```
Jesteś [rola, np. „doświadczonym recenzentem metodologii w naukach społecznych"].
Piszesz w sposób [ton: rzeczowy / akademicki / zwięzły].
Zachowujesz zasadę ograniczonego zaufania: nie zgadujesz; jeśli czegoś nie ma w materiale, piszesz „brak danych".
```

## WARSTWA 2 — Kontekst i dane
*Co model musi wiedzieć/widzieć, żeby wykonać zadanie?*

> ⚠️ Tylko materiał JAWNY lub ZANONIMIZOWANY. Żadnych danych osobowych, medycznych, recenzji pod NDA, niezanonimizowanych transkrypcji.

```
Kontekst sytuacji: [1–3 zdania tła]
Materiał do analizy:
"""
[wklej tu fragment / cytaty / matrycę — najlepiej oddzielony cudzysłowem potrójnym albo znacznikiem XML]
"""
```

## WARSTWA 3 — Zadanie i kroki
*Co dokładnie ma zrobić, krok po kroku?*

```
Zadanie: [jedno zdanie celu]
Wykonaj kolejno:
1. ...
2. ...
3. ...
Przy każdej tezie wskaż fragment materiału, na którym ją opierasz.
```

## WARSTWA 4 — Format wyjścia i ograniczenia
*Jak ma wyglądać odpowiedź i czego ma NIE robić?*

```
Format: [np. tabela Markdown z kolumnami ... / lista punktów / JSON wg schematu ...]
Długość: [np. maks. 200 słów / 5 punktów]
Ograniczenia: nie dodawaj wiedzy spoza materiału; nie wymyślaj cytatów; oznacz luki jako „brak danych".
```

---

## Dziennik iteracji

| Wersja | Co zmieniłem(am) | Co poprawiło to w odpowiedzi |
|---|---|---|
| v1 | wersja wyjściowa (jedno zdanie) | — |
| v2 | przejście na 4 warstwy | |
| v3 | | |

**Wniosek:** Która warstwa najmocniej zmieniła jakość? → ___________
