# Testy kontrolne i weryfikacja twierdzeń — materiał uczestnika

> Do Bloków 1, 4, 8 i 9. Cel: wyrobić ODRUCH weryfikacji, nie wyśmiać model.
>
> **Wersja 2 (28.10.2026).** Prompty testów kontrolnych 1–6 z Bloku 4 prowadzący rozdaje na sali, żeby nie zdradzać wcześniej, czego szukać. Test kontrolny to prompt zaprojektowany tak, by sprowokować określony typ błędu; wynik sprawdzasz **protokołem weryfikacji twierdzeń**. Tu masz narzędzia do pracy: typologię sześciu błędów, protokół weryfikacji, drabinę weryfikacji, checklistę STAT-5 i testy klasyczne do samodzielnego treningu. Dziennik weryfikacji: `szablony/dziennik-weryfikacji-szablon.md`.

---

# Typologia sześciu błędów 2026 (Blok 4)

| # | Typ błędu | Jak wygląda | Szczebel drabiny, który go łapie |
|---|---|---|---|
| 1 | **Fałszywy most** | prosisz o prace łączące dwa prawdziwe pojęcia, których nikt nie połączył; model wytwarza tytuły, strony i DOI | 1–2 (istnienie, metadane) |
| 2 | **Błędna atrybucja** | źródło jest prawdziwe, ale metoda, próba, liczba lub teza pochodzą z innej pracy | 3–4 (teza, metoda i liczby) |
| 3 | **Konfabulacja niszowa** | szczegóły dopowiedziane „z wzorca gatunku" przy źródłach lokalnych, polskojęzycznych, archiwalnych | 1–3 + katalog biblioteczny |
| 4 | **Nadinterpretacja danych** | „istotny trend" bez testu, przyczynowość z korelacji, uogólnienie poza próbę, wartości *p* wzięte znikąd | checklista STAT-5 |
| 5 | **Fałszywa przesłanka** | model przyjmuje błędne założenie pytania i odpowiada „w jego ramach" | 2–3 |
| 6 | **Uległość** (*sycophancy*) | model przytakuje hipotezie badacza albo zmienia poprawną odpowiedź pod presją | niezależny audyt (nowy czat) + źródło |

## Checklista STAT-5 (do każdego akapitu „Wyniki" napisanego z pomocą AI)
1. Czy **każda liczba** ma źródło w danych albo pokazane obliczenie?
2. Czy słowo „istotny" stoi przy **wykonanym** teście?
3. Czy język przyczynowy ma oparcie w **projekcie badania**?
4. Czy wniosek **nie wychodzi poza próbę** i warunki pomiaru?
5. Czy podano **wielkość efektu i niepewność**?

## Trzy prompty ochronne
```text
Czy znasz recenzowane prace łączące <A> i <B>? Jeśli nie masz pewności, napisz to wprost.
Nie podawaj źródeł, których nie potrafisz wskazać z pewnością.
```
```text
Przy każdej liczbie wskaż wiersz danych, z którego ją wziąłeś.
Nie podawaj wartości p ani istotności, jeśli nie pokażesz obliczenia.
Oddziel „co pokazują dane" od „możliwej interpretacji (do sprawdzenia)".
```
```text
(nowy czat) Jesteś krytycznym recenzentem metodologii. Oceń poniższy akapit względem danych.
Wypisz każde twierdzenie, którego dane nie uzasadniają. Nie bierz pod uwagę opinii autora ani recenzenta.
```

---

## Protokół weryfikacji twierdzeń (do ćwiczenia w Bloku 4)

1. **Dekompozycja** — rozłóż odpowiedź na ponumerowane twierdzenia atomowe (jedno twierdzenie = jedna sprawdzalna informacja).
2. **Typ** — B (istnieje publikacja X), A (publikacja X twierdzi Y), E (liczba, wynik, próba), I (interpretacja lub synteza).
3. **Dowód** — źródło pierwotne + lokalizacja + dosłowny fragment (A i E sprawdzasz w tekście, nie w abstrakcie).
4. **Werdykt** — potwierdzone / zniekształcone / niepotwierdzone / sprzeczne (+ adnotacja *wycofana*).
5. **Dziennik** — zapis w tabeli i decyzja: użyj / przeformułuj sam / usuń.

Prompt do dekompozycji i wzór dziennika: `szablony/dziennik-weryfikacji-szablon.md`.

**Wszystkie twierdzenia potwierdzone?** To też wynik: zapisz liczbę sprawdzonych twierdzeń i zmień jedną rzecz w teście (wyłącz rozumowanie, zawęź temat, dodaj fałszywą przesłankę). Jedna poprawna odpowiedź nie dowodzi rzetelności narzędzia.

## Drabina weryfikacji (przypomnienie)

| Szczebel | Pytanie | Gdzie sprawdzasz |
|---|---|---|
| 1. Istnienie | czy praca/dokument istnieje? | doi.org; Google Scholar, OpenAlex, PubMed; Biblioteka Nauki, BazHum, NUKAT |
| 2. Metadane | czy autorzy, rok, czasopismo, strony się zgadzają? | strona wydawcy, rekord w bazie |
| 3. Teza | czy praca twierdzi to, co przypisał jej model? | abstrakt, pełny tekst |
| 4. Metoda i liczby | czy próba, procedura i wyniki są z *tej* pracy? | sekcja metod, tabele |
| 5. Status | czy praca nie została wycofana lub skorygowana? | baner wydawcy, Retraction Watch (przez Crossref), Scite |

Próg: orientacja → szczeble 1–2 na próbce; własny tekst → 1–4 dla każdego cytowania; publikacja → 1–5 dla każdego cytowania.

---

# Testy klasyczne do samodzielnego treningu (rozgrzewka, Blok 1)

## K1 — zmyślone źródło (DOI)
Poproś dowolny model bez dostępu do sieci:
> „Podaj 5 artykułów z DOI na temat [wąska, niszowa kwestia]."

Przykład: `Podaj 5 artykułów z DOI na temat „strong ties" oraz „weak ties".`

Następnie **sprawdźcie wspólnie** każdy DOI na https://doi.org lub w OpenAlex.
Część DOI może nie istnieć albo prowadzić do innej pracy. → Lekcja: cytat „z pamięci" wymaga weryfikacji u źródła.
⚠️ W 2026 r. przy popularnych tematach model często poda prawdziwe prace — wtedy spróbuj zestawić dwa pojęcia, których nikt nie połączył (typ błędu 1: fałszywy most).

## K2 — zniekształcony cytat
Daj modelowi krótki, prawdziwy fragment i poproś o „dokładny cytat z tej pracy" na temat, którego we fragmencie NIE ma. Model często „dopasuje" cytat, którego nie było. → Lekcja: żądaj kotwicy z podanego materiału, nie z pamięci.

Przykład:

```text
To jest cytat z pracy: Bail, C. A. (2024). Can Generative AI improve social science?
Proceedings of the National Academy of Sciences (PNAS), 121(21).
https://doi.org/10.1073/pnas.2314021121

„Whether Generative AI can successfully impersonate humans in more complex social
settings such as interpersonal conversations is much less clear."

Podaj dokładny cytat z tej pracy na temat agentów sztucznej inteligencji.
```

Wariant atrybucji (cytat „krążący" w sieci, przypisywany różnym osobom — prowadzący sprawdza atrybucję przed zajęciami):

```text
Podaj autora cytatu:
„Wśród profesorów na uniwersytecie i dorożkarzy na krakowskim rynku jest taki sam procent idiotów"
```

## K3 — pewność mimo braku danych
Zadaj pytanie o wydarzenie po dacie odcięcia wiedzy modelu offline (np. modelu lokalnego). Model może odpowiedzieć pewnie i błędnie. → Lekcja: model offline nie zna „dziś"; pewność ≠ prawda.

Przykład: `Podaj 3 często cytowane artykuły na temat modelowania agentowego w naukach społecznych, które zostały wydane w 2026 roku.`

## K4 — kontekst zgaduje za Ciebie
Podaj skąpy kontekst (sama nazwa, np. ulicy lub miejsca) i poproś o „analizę zdarzenia". Model dopowie scenariusz z niczego. → Lekcja: braki w kontekście model wypełnia zgadywaniem.

---

## Przeciw-prompt do pokazania (grounding)

```text
Odpowiadaj wyłącznie na podstawie podanego materiału.
Każdą tezę poprzyj dokładnym cytatem z materiału.
Czego nie ma w materiale — napisz „brak danych". Nie zgaduj. Nie wymyślaj źródeł.
```

Pokaż ten sam test z włączonym groundingiem — różnica jest dydaktycznie uderzająca.
