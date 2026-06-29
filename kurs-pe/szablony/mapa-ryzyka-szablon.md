# Mapa ryzyka danych

> Wypełnij dla TYPÓW danych, z którymi realnie pracujesz. Zasada `privacy cage`: zanim coś wkleisz, wiedz, gdzie to trafi.
> Poziomy: **jawne** / **wrażliwe** / **osobowe** / **medyczne** / **pod NDA**.
> Środowiska: **chmura (model frontier)** / **tylko lokalnie (LLM lokalny)** / **nigdy do AI**.

---

| Typ danych | Poziom wrażliwości | Dozwolone środowisko | Wymagana anonimizacja? | Uwagi |
|---|---|---|---|---|
| np. metadane bibliograficzne | jawne | chmura | nie | bezpieczne |
| np. cytaty z publikacji open access | jawne | chmura | nie | |
| np. moje notatki robocze (bez nazwisk) | jawne/wrażliwe | chmura | sprawdź | |
| np. transkrypcje wywiadów | osobowe | nigdy do AI / tylko lokalnie po anonimizacji | TAK | ryzyko reidentyfikacji |
| np. dane medyczne pacjentów | medyczne | nigdy do AI | — | bezwzględny zakaz |
| np. cudza recenzja / manuskrypt pod NDA | pod NDA | nigdy do AI | — | |
| ... | | | | |

---

## Zasada minimalizacji
Podaję modelowi **najmniej danych, ile trzeba** do wykonania zadania.

## Test reidentyfikacji
Czy po „anonimizacji" rzadka kombinacja cech (wiek + miejscowość + zawód + diagnoza) wciąż wskazuje konkretną osobę?  ☐ TAK → nie wysyłam ☐ NIE
