# NotebookLM - książka naukowa (scientific book)

> Przed wysłaniem zapytań na temat książki dobrą praktyką jest określenie zasad rozmowy (reguły ograniczające halucynacje).

## Zasady na całą rozmowę:

```
- Odpowiadaj wyłącznie na podstawie wgranych źródeł.
- Wskazuj rozdział/sekcję lub przypisy. Nie zmyślaj numerów stron.
- Zachowuj dokładne terminy autora; cytuj krótką frazę, gdy liczy się brzmienie.
- Oddzielaj twierdzenia autora od własnych wniosków; wnioski oznaczaj „(wniosek)".
- Brak podstaw w źródłach → powiedz to wprost, nie zgaduj.

```

## Zestaw przykładowych promptów do wydobywania informacji z książki

1. Orientacja i główna teza

```
Przeanalizuj tekst i nakreśl jego ogólną orientację. Przedstaw wyniki w zwięzłej formie, wskazując:
- Główny problem badawczy.
- Tezę autora (streść ją w 2–3 zdaniach).
- Pole naukowe oraz główną debatę, w jakiej osadzona jest książka.
- Typ książki (np. monografia empiryczna, praca teoretyczna, polemika, pole/przegląd).
Dodatkowo wypisz od 3 do 5 kluczowych idei (filarów), na których opiera się teza.

```

2. Rekonstrukcja argumentacji

```
Zrekonstruuj główną linię argumentacyjną autora krok po kroku. Jakich głównych argumentów, dowodów empirycznych lub przesłanek logicznych używa autor, aby udowodnić swoją główną tezę?

```

3. Metodologia i ramy teoretyczne

```
Określ metodologię oraz ramy teoretyczne zastosowane w badaniach. Na jakich paradygmatach, teoriach, źródłach lub typach danych bazuje autor tej książki?

```

4. Aparat pojęciowy (Słownik kategorialny)

```
Wybierz od 5 do 12 najważniejszych pojęć naukowych (terminów specjalistycznych), które autor wprowadza, redefiniuje lub na których opiera swój wywód. Przedstaw je w formie tabeli, która zawiera wyłącznie następujące kolumny:
| Pojęcie | Definicja autora (w znaczeniu użytym w tekście) | Rola (jaką funkcję pełni w argumentacji?) | Pojęcie powiązane (inne pojęcie z tekstu) |

```

5. Ograniczenia i kontrargumenty

```
Wskaż słabe punkty lub ograniczenia tych badań wymienione w tekście (np. braki w danych). Z jakimi kontrargumentami lub konkurencyjnymi teoriami mierzy się autor i w jaki sposób na nie odpowiada?

```

6. Konkluzje i wkład w dziedzinę

```
Streść najważniejsze wnioski płynące z zakończenia książki. Jakie jest główne przesłanie autora i w jaki sposób ta książka poszerza wiedzę w swojej dziedzinie naukowej?

```

7. Synteza i notatki trwałe (Zettelkasten)

```
Przygotuj zwięzłą, przekrojową syntezę najważniejszych koncepcji z książki. Następnie wygeneruj dokładnie 8 "notatek trwałych" (permanent notes), które uchwycą najcenniejsze myśli z tekstu. 
Zastosuj rygorystyczne zasady dla notatek:
- Każda notatka ma składać się z dokładnie jednego, samodzielnego zdania.
- Każde zdanie musi wyrażać kompletną i uniwersalną myśl autora (zrozumiałą bez dodatkowego kontekstu).
- Do każdej notatki obowiązkowo dołącz precyzyjną lokalizację w źródle (np. numer/nazwa rozdziału lub podrozdziału).

```

## Wskazówka do NotebookLM:

> Jeśli po użyciu któregoś promptu odpowiedź będzie zbyt ogólna, dodaj polecenie uzupełniające:

```
Wskaż konkretne strony lub rozdziały w załączonym źródle, które o tym mówią

```