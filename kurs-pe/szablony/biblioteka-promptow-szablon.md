# Biblioteka promptów — szablon wpisu

> Od Bloku 2 prowadzisz na własnym dysku folder `moj-warsztat/prompty/`. Po **każdym** bloku odkładasz tam **jeden działający prompt** w tym formacie. Na koniec Dnia 3 masz min. 6 pozycji. W Bloku 11 biblioteka staje się folderem `prompty/` w katalogu projektu: agent wykonuje prompty na Twoje wezwanie („Wykonaj `prompty/matryca-z-plikow.md` na plikach z `zrodla/md/`"). W Bloku 12 najczęściej używane prompty zamieniasz w **skills**.
>
> **Jeden plik = jeden prompt.** Nazwa pliku: **czasownik + obiekt** (np. `streszczenie-metod.md`, `weryfikacja-cytowania.md`), bez dat i wersji w nazwie.

---

## Cztery zasady porządku

1. **Jeden prompt = jeden plik**, nazwa „czasownik + obiekt".
2. **Stała budowa pliku:** Kiedy używam · Prompt · Wejście i wyjście · Uwagi po testach.
3. **Spis treści** w `prompty/README.md`: jedna linijka na prompt (nazwa, do czego służy, etap projektu). Agent czyta spis i wskaże pasujący prompt.
4. **Wersjonowanie przez uwagi, nie przez kopie:** poprawki opisujesz w „Uwagach po testach".

> **Powtarzasz? Zrób skill. Jednorazowe? Zostaw prompt.**

---

## Format wpisu (skopiuj do nowego pliku)

```markdown
# [czasownik + obiekt, np. streszczenie-empiryczne]

## Kiedy używam
[Jedno–dwa zdania: w jakiej sytuacji sięgam po ten prompt.]

## Prompt (do wklejenia)
[Gotowy prompt w czterech warstwach: rola → kontekst → zadanie → format.]

## Wejście i wyjście
[Czat: co wklejam. Agent: jakie pliki czyta (np. zrodla/md/*.md) i gdzie zapisuje wynik (np. wyniki/...).]

## Uwagi po testach
[Co poprawiłem względem pierwszej wersji i dlaczego — jaki błąd modelu to naprawiło.]
```

## Format spisu `prompty/README.md`

```markdown
# Spis promptów
| Plik | Do czego | Etap projektu |
|---|---|---|
| streszczenie-metod.md | wierne streszczenie sekcji metod z cytatami | czytanie |
| wiersz-matrycy.md | jeden wiersz matrycy z cytatem-kotwicą | ekstrakcja |
| kwerenda-protokol.md | prompt wyszukiwawczy (B9) | kwerenda |
| dekompozycja-twierdzen.md | rozkład tekstu na twierdzenia do weryfikacji (B4) | kontrola |
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

## Wejście i wyjście
Czat: wklejam sekcję metod. Agent: czyta zrodla/md/<plik>.md, zapisuje
wyniki/metody-<plik>.md.

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

## Wejście i wyjście
Czat: wklejam streszczenie. Agent: czyta jeden plik z zrodla/, dopisuje wiersz
do wyniki/matryca-robocza.md.

## Uwagi po testach
v1 parafrazował cytat-kotwicę. Dodałem słowo „DOSŁOWNY" wielkimi literami —
zaczął przepisywać fragment 1:1. To ten sam prompt, który w B12 pakuję jako skill
(`cwiczenie-formaty/skill-wiersz-matrycy.md`).
```
