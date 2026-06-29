# Ściąga: typowe artefakty do wyczyszczenia po konwersji PDF

> Po konwersji przejrzyj plik `.md` i usuń to, co jest „śmieciem układu", a nie treścią.
> Mniej śmieci = chudszy kontekst = lepsza i tańsza odpowiedź modelu.

| Artefakt | Jak wygląda | Co zrobić |
|---|---|---|
| Numery stron | samotna liczba w osobnej linii | usuń (skrypt robi to automatycznie) |
| Powtarzalny nagłówek/stopka | ten sam tekst na każdej stronie (tytuł czasopisma, DOI) | usuń powtórzenia |
| Złamane wyrazy | `po-\ndział` | scal (skrypt scala podstawowe przypadki) |
| Złamane akapity | jedno zdanie pocięte na wiele linii | scal w jeden akapit |
| Przypisy wplątane w tekst | numerki i treść przypisu w środku zdania | przenieś na koniec sekcji lub usuń, jeśli zbędne |
| Tabele rozsypane | kolumny zlane w jeden ciąg | odtwórz jako tabelę Markdown lub opisz |
| Znaki OCR | `l` zamiast `1`, `rn` zamiast `m`, dziwne symbole | popraw ręcznie lub promptem |
| Nagłówki/stopki redakcyjne | „Downloaded from…", „© Wydawca" | usuń |

## Szybki prompt czyszczący (dla fragmentów)
```
Wyczyść poniższy tekst po OCR: usuń numery stron, powtarzalne nagłówki/stopki,
scal złamane wiersze i akapity, popraw oczywiste błędy OCR.
Zachowaj CAŁĄ treść merytoryczną i strukturę nagłówków. Nie streszczaj, nie skracaj.

"""
[wklej fragment]
"""
```
> Po wyczyszczeniu policz, ile „śmieciowych" linii ubyło — to dobra miara jakości kontekstu.
