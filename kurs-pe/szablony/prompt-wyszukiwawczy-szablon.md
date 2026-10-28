# Prompt wyszukiwawczy — szablon (Blok 9)

> O jakości kwerendy decyduje przede wszystkim **prompt**, czyli protokół wyszukiwania. Ten sam szablon działa w czacie z wyszukiwaniem, w trybie deep research (ChatGPT, Claude, Gemini, Grok, Perplexity) i jako polecenie dla agenta.
> Wynik każdego narzędzia to **lista tropów do weryfikacji**, nie przegląd literatury. Weryfikacja: `dziennik-weryfikacji-szablon.md`.

---

## Wypełnij przed uruchomieniem

| Element | Twoja treść |
|---|---|
| Pytanie (stan wiedzy, nie teza do potwierdzenia) | |
| Pojęcie 1 + synonimy (PL i EN) | |
| Pojęcie 2 + synonimy (PL i EN) | |
| Zakres lat | |
| Włącz (typy prac) | |
| Wyklucz | |
| Szara literatura? (raporty, dokumenty instytucji) | ☐ tak, osobna sekcja ☐ nie |
| Kolor danych w pytaniu | ☐ 🟢 (pytanie jawne) — inaczej nie wysyłaj |

---

## Szablon promptu (do czatu z wyszukiwaniem i deep research)

```text
[ROLA] Jesteś bibliotekarzem dziedzinowym wspierającym przegląd literatury.
Nie podajesz prac, których nie odnalazłeś w trakcie tego wyszukiwania.

[PYTANIE] <pytanie o stan wiedzy>

[POJĘCIA I SYNONIMY]
- <pojęcie 1>: <synonimy, także po angielsku>
- <pojęcie 2>: <synonimy, także po angielsku>
Szukaj po angielsku i po polsku.

[ZAKRES I KRYTERIA]
- lata <od–do>; prace recenzowane, preprinty oznaczone jako preprint,
  szara literatura w osobnej sekcji
- WŁĄCZ: <typy prac>
- WYKLUCZ: <np. komentarze bez danych, wpisy blogowe, materiały marketingowe>

[FORMAT RAPORTU]
1. Tabela: autorzy | rok | tytuł | czasopismo/wydawca | DOI lub URL | typ pracy |
   jedno zdanie z abstraktu (dosłownie, w cudzysłowie) | dlaczego spełnia kryteria
2. Osobno: prace sprzeczne z dominującym stanowiskiem.
3. Osobno: prace znalezione, ale odrzucone (1 zdanie powodu).
4. Na końcu: lista zapytań, których użyłeś, i luki („czego nie udało się znaleźć").

[REGUŁY] Jeśli nie masz pewności, że praca istnieje, nie umieszczaj jej w tabeli.
Nie uzupełniaj brakujących DOI ani stron z pamięci; wpisz „brak".
```

**Pięć elementów, które robią różnicę:** synonimy · kryteria włączenia i wyłączenia · dosłowne zdanie z abstraktu · lista zapytań i odrzuconych · zakaz uzupełniania z pamięci.

---

## Wariant agentowy (Claude z Cowork, ChatGPT Work, Claude Code, Codex)

Zapisz wypełnioną tabelę z góry jako `notatki/protokol-kwerendy.md` w katalogu projektu, a potem wydaj polecenie:

```text
Przeczytaj CLAUDE.md. Zadanie: kwerenda według protokołu z notatki/protokol-kwerendy.md.

1. Zaplanuj co najmniej 6 zapytań (polskie i angielskie terminy, synonimy).
   Pokaż plan i czekaj na moje OK.
2. Szukaj w: OpenAlex (api.openalex.org), Crossref, PubMed (jeśli temat jest
   biomedyczny) oraz w sieci ogólnej — tylko dla szarej literatury.
3. Dla każdego kandydata zapisz: autorzy, rok, tytuł, źródło, DOI, typ pracy,
   jedno zdanie z abstraktu (dosłownie) i powód włączenia.
4. Sprawdź każdy DOI w Crossref lub na doi.org. Kandydatów bez potwierdzenia oznacz
   „DOI niepotwierdzony". Usuń duplikaty.
5. Zapisz: wyniki/kandydaci.json, wyniki/raport-kwerendy.md (metoda: zapytania,
   daty, bazy, liczba trafień, odrzucone z powodem; potem wyniki i luki)
   oraz wpis w notatki/log.md.
Nie dopisuj prac z pamięci. Nie oceniaj jakości badań — to zrobię ja.
```

> OpenAlex wymaga od lutego 2026 r. bezpłatnego klucza do API dla zapytań automatycznych; wyszukiwarka w przeglądarce działa bez niego. Klucza nie zapisuj w folderze, który udostępniasz agentowi.
> Agent czyta pobrane strony, więc mogą w nich być ukryte polecenia (*prompt injection*): raport trafia do `wyniki/`, nigdy do `zrodla/`.

---

## Po kwerendzie

1. Wylosuj co najmniej 3 prace z wyniku i sprawdź twierdzenia B (istnienie) i A (zdanie z abstraktu, spełnienie kryteriów) → `dziennik-weryfikacji-szablon.md`.
2. Oceń wynik soczewką czterech trybów porażki: błąd chronologiczny · nadmiarowość · „przypadkowy sukces" · wynik nietrafny.
3. Działający prompt odłóż do `prompty/kwerenda-protokol.md` — w Bloku 12 może stać się skillem `kwerenda-literatury`.
