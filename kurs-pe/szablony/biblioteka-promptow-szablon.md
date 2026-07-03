# Biblioteka promptów — szablon wpisu

> Od Bloku 2 prowadzisz na własnym dysku folder `moj-warsztat/prompty/`. Po **każdym** bloku odkładasz tam **jeden działający prompt** w tym formacie. Na koniec Dnia 3 masz min. 6 pozycji — to część portfolio i „skills w wersji ręcznej" dla agenta z Bloku 11.
>
> **Jeden plik = jeden prompt.** Nazwa pliku: **czasownik + obiekt** (np. `streszczenie-metod.md`, `weryfikacja-cytowania.md`).

---

## Format wpisu (skopiuj do nowego pliku)

```markdown
# [czasownik + obiekt, np. streszczenie-empiryczne]

## Kiedy używam
[Jedno–dwa zdania: w jakiej sytuacji sięgam po ten prompt.]

## Prompt (do wklejenia)
[Gotowy prompt w czterech warstwach: rola → kontekst → zadanie → format.]

## Uwagi po testach
[Co poprawiłem względem pierwszej wersji i dlaczego — jaki błąd modelu to naprawiło.]
```

---

## Przykład 1 — `streszczenie-metod.md`

```markdown
# streszczenie-metod

## Kiedy używam
Gdy mam czysty `.md` artykułu i chcę wiernego streszczenia samej sekcji metod,
bez zgadywania brakujących szczegółów.

## Prompt (do wklejenia)
[ROLA] Jesteś recenzentem metodologii. Nie zgadujesz; czego nie ma w materiale,
oznaczasz jako „brak danych".
[KONTEKST] Materiał (zanonimizowany):
"""
<wklej sekcję metod>
"""
[ZADANIE] 1) Wypisz projekt badania i dobór próby. 2) Wskaż 3 ryzyka trafności.
Przy każdym punkcie zacytuj zdanie, na którym się opierasz.
[FORMAT] Tabela Markdown: aspekt | ustalenie | cytat-kotwica. Maks. 200 słów.

## Uwagi po testach
v1 dopisywał wielkość próby, której nie było w tekście. Dodałem regułę „brak danych"
w warstwie roli + wymóg cytatu-kotwicy — przestał zgadywać.
```

## Przykład 2 — `wiersz-matrycy.md`

```markdown
# wiersz-matrycy

## Kiedy używam
Gdy mam streszczenie jednego artykułu i chcę z niego zbudować jeden wiersz matrycy
literatury do dalszej syntezy.

## Prompt (do wklejenia)
[ROLA] Jesteś asystentem porządkującym literaturę. Wypełniasz pola WYŁĄCZNIE
na podstawie podanego streszczenia; brakujące pola oznaczasz „N/A".
[KONTEKST] Streszczenie:
"""
<wklej streszczenie>
"""
[ZADANIE] Zbuduj jeden wiersz: źródło | rok | metoda | teza | luka | cytat-kotwica.
W „cytat-kotwica" wstaw DOSŁOWNY fragment + lokalizację, nie parafrazę.
[FORMAT] Jeden wiersz tabeli Markdown. Nic poza tabelą.

## Uwagi po testach
v1 parafrazował cytat-kotwicę. Dodałem słowo „DOSŁOWNY" wielkimi literami —
zaczął przepisywać fragment 1:1. To ten sam prompt, który w B11 pakuję jako SKILL.
```
