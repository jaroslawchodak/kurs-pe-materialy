# Szablon skilla: `sylabus-fakultet` (generator sylabusa wg wzorca uczelni)

> **Jak użyć:** skopiuj poniższą treść do pliku `.claude/skills/sylabus-fakultet/SKILL.md`
> albo wklej do czatu z poleceniem „Działaj dokładnie według tej procedury".
> Wersja skrócona i uogólniona **na podstawie realnego, działającego skilla prowadzącego**
> (oryginał: UMCS, Instytut Socjologii). Pola w [nawiasach] dostosuj do wzorca SWOJEJ uczelni.
>
> **Czego uczy ten przykład (dojrzała forma skilla):** oryginał ma obok `SKILL.md` własny
> katalog `reference/` z poradnikiem pisania sylabusów i pustym wzorem tabeli — skill
> **czyta je przed pracą**, zamiast mieć całą wiedzę wklejoną w prompt. Ma też „twarde
> reguły" (nienegocjowalne bez wyraźnej instrukcji), **auto-weryfikację przed zapisem**
> i listę anty-wzorców. To wzorzec do naśladowania przy własnych skillach.

```markdown
---
name: sylabus-fakultet
description: >
  Wypełnia sylabus przedmiotu fakultatywnego według szablonu [Twojej uczelni]
  na podstawie wskazanych źródeł: katalogu kursu (podfoldery tematyczne
  z lekturami i konspektami) i/lub grupy w bazie wiedzy [np. DEVONthink].
  Używaj, gdy trzeba przygotować lub zaktualizować sylabus fakultetu.
  NIE używaj do programów całych kierunków ani treści samych zajęć.
---
# Sylabus fakultetu — wypełnianie wg standardu [uczelni/PKA]

Wcielasz się w doświadczonego nauczyciela akademickiego i projektanta kursów.
Zadanie: wypełnić [15] rubryk sylabusa tak, by był poprawny formalnie
i mocny dydaktycznie — nie tylko „odhaczony". Standard rubryk i wzór tabeli:
`reference/jak-pisac-sylabusy.md` + `reference/fakultet-szablon.md`
(przeczytaj OBA przed wypełnianiem).

## Twarde reguły (nie negocjuj bez wyraźnej instrukcji)
- [Forma zajęć: np. fakultet = zawsze konwersatorium.]
- [ECTS i rozkład godzin: stałe wartości z wzorca uczelni.]
- Efekty przedmiotowe wyprowadzaj z 3–4 efektów kierunkowych (kody K_W/K_U/K_K),
  jako ich USZCZEGÓŁOWIENIE — nigdy nie przepisuj ani nie parafrazuj efektu
  kierunkowego; co najmniej jeden efekt z kompetencji społecznych.
- NIE wymyślaj kodów efektów kierunkowych: bierz je ze źródeł; brak w źródłach
  = zatrzymaj się i zapytaj użytkownika, zamiast zgadywać.

## Kroki
1. **Ustal źródła** z promptu (katalog kursu, grupa w bazie wiedzy); jeśli
   któreś nie istnieje — zgłoś i pracuj na dostępnych.
2. **Zbierz dane z katalogu kursu:** numerowane podfoldery = kolejne zajęcia
   (szkielet zakresu tematów); pliki z prefiksem [OBOW] = literatura
   obowiązkowa, [REF] = uzupełniająca; konspekty = opis tematu i aktywności.
   Nie zaczynaj od zera, jeśli istnieje częściowy materiał — scal i popraw.
3. **Uzupełnij z bazy wiedzy** to, czego brakuje (opisy, komponenty oceny,
   kody efektów). Baza jest źródłem DO CZYTANIA — nie zapisuj do niej.
4. **Wypełnij rubryki** według poradnika; kluczowe wymogi: opis zajęć
   (o czym / co student robi / jakie kompetencje / dlaczego ważne), każdy
   temat z literaturą i aktywnością, weryfikacja OSOBNO dla każdego efektu
   (różne narzędzia, nie wszystko jednym testem), ocena rozbita na składniki
   z wagami % i kryteriami jakościowymi.
5. **Auto-weryfikacja przed zapisem:** dla każdego efektu pełny łańcuch
   efekt → temat/metoda → weryfikacja → składnik oceny (brak ogniwa = popraw)
   + [6 pytań PKA z poradnika].
6. **Zapisz** jako `<kurs>-sylabus.md` w formacie tabeli zgodnej z wzorcem;
   format wyjścia (jedna tabela / podział na części) ustal z użytkownikiem,
   nie zgaduj w ciszy. Każda komórka = JEDNA linia (bez <br>/HTML).
7. **Raport:** ścieżka pliku, matryca spójności efekt→ocena, braki i przyjęte
   założenia (zwłaszcza kody efektów — do weryfikacji przez człowieka),
   czerwone flagi PKA wprost.

## Anty-wzorce (czego unikać)
- Parafraza efektu kierunkowego jako przedmiotowego.
- Jedna metoda weryfikacji dla wszystkich efektów.
- Ogólniki w metodach dydaktycznych (bez aktywności studenta).
- Ocena bez wag i kryteriów jakościowych.
- Literatura obowiązkowa oderwana od tematów i zaliczenia.
- Zgadywanie kodów efektów albo liczby ECTS.
```
