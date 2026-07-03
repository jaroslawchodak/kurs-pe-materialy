# Przykładowy skill: `wiersz-matrycy` (anatomia pliku SKILL.md)

> To gotowy przykład do obejrzenia w Bloku 11: jak zamienić powtarzalny prompt z biblioteki (`prompty/wiersz-matrycy.md`) w **umiejętność (skill)**, którą agent ładuje na żądanie i uruchamia komendą `/wiersz-matrycy`. Ten sam efekt co ręczny prompt — tylko spakowany i wywoływany jednym poleceniem.
>
> Reguła kciuka: *powtarzasz procedurę? zrób skill. Robisz raz? zostaw prompt.*

---

## Anatomia pliku `SKILL.md` (trzy części)

1. **Nazwa** — czasownik + obiekt, krótka i jednoznaczna (`wiersz-matrycy`).
2. **Opis-wyzwalacz** — zdanie mówiące agentowi, KIEDY sięgnąć po ten skill (to po nim agent rozpoznaje, że pasuje do zadania).
3. **Procedura** — kroki do wykonania, deterministyczne i sprawdzalne.

---

## Zawartość pliku `SKILL.md`

```markdown
---
name: wiersz-matrycy
description: >
  Buduje JEDEN wiersz matrycy literatury z pliku streszczenia artykułu.
  Uruchom, gdy użytkownik prosi o dodanie źródła do matrycy albo o wiersz
  matrycy z konkretnego streszczenia.
---

# Skill: wiersz-matrycy

## Kiedy się uruchamiam
Gdy w kontekście jest streszczenie jednego artykułu (`.md`), a użytkownik
prosi o wiersz matrycy literatury.

## Procedura
1. Wczytaj wskazany plik streszczenia ze `zrodla/`.
2. Wypełnij pola WYŁĄCZNIE na jego podstawie: źródło | rok | metoda | teza |
   luka | cytat-kotwica. Brakujące pola oznacz „N/A" — nie zgaduj.
3. W polu „cytat-kotwica" wstaw DOSŁOWNY fragment + lokalizację (strona/sekcja),
   nigdy parafrazę.
4. Zwróć wynik jako jeden wiersz tabeli Markdown i dopisz go do
   `wyniki/matryca.md` (nigdy nie nadpisuj wcześniejszych wierszy).
5. Zatrzymaj się i poczekaj na akceptację, zanim przejdziesz do kolejnego źródła.

## Czego nie wolno
- Nie dodawaj tez spoza streszczenia.
- Nie czytaj plików spoza `zrodla/` (powierzchnia ataku — por. prompt injection).
```

---

## Jak to wywołać

W agencie (Claude Code / OpenCode) po prostu:

```
/wiersz-matrycy zrodla/Lazer-2009.md
```

Agent ładuje procedurę, wykonuje 5 kroków, zatrzymuje się na akceptację. To dokładnie ta sama logika, którą w Bloku 8 wykonujesz ręcznie — decyzję „co jest istotne" wciąż firmuje badacz.
