# Pułapki na halucynacje (materiał prowadzącego)

> Do Bloków 1, 4 i 9. Pokazuj na żywo — najmocniejszy moment dydaktyczny to złapana halucynacja.
> Cel: nauczyć uczestników ODRUCHU weryfikacji, nie wyśmiać model.

---

## Pułapka 1 — zmyślone źródło (DOI)
Poproś dowolny model bez dostępu do sieci:
> „Podaj 5 artykułów z DOI na temat [wąska, niszowa kwestia]."

Następnie **sprawdźcie wspólnie** każdy DOI na https://doi.org lub w OpenAlex.
Często część DOI nie istnieje albo prowadzi do innej pracy. → Lekcja: cytat „z pamięci" wymaga weryfikacji u źródła.

## Pułapka 2 — zniekształcony cytat
Daj modelowi krótki, prawdziwy fragment i poproś o „dokładny cytat z tej pracy" na temat, którego we fragmencie NIE ma.
Model często „dopasuje" cytat, którego nie było. → Lekcja: żądaj kotwicy z podanego materiału, nie z pamięci.

## Pułapka 3 — pewność mimo braku danych
Zadaj pytanie o wydarzenie po dacie odcięcia wiedzy modelu offline.
Model może odpowiedzieć pewnie i błędnie. → Lekcja: model lokalny/offline nie zna „dziś"; pewność ≠ prawda.

## Pułapka 4 — kontekst zgaduje za Ciebie
Podaj skąpy kontekst (sama nazwa, np. ulicy/miejsca) i poproś o „analizę zdarzenia".
Model dopowie scenariusz z niczego. → Lekcja: braki w kontekście model wypełnia zgadywaniem.

---

## Przeciw-prompt do pokazania (grounding)
```
Odpowiadaj wyłącznie na podstawie podanego materiału.
Każdą tezę poprzyj dokładnym cytatem z materiału.
Czego nie ma w materiale — napisz "brak danych". Nie zgaduj. Nie wymyślaj źródeł.
```
Pokaż tę samą pułapkę z włączonym groundingiem — różnica jest dydaktycznie uderzająca.
