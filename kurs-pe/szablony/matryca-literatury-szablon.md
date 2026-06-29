# Matryca literatury

> Twój ręczny, w pełni kontrolowalny „mały RAG". Ty decydujesz, co wchodzi do kontekstu.
> Zasada: do matrycy trafiają **cytaty-kotwice** (dokładny tekst + strona), NIE całe PDF-y.

---

| # | Źródło (autor, rok) | Metoda | Główna teza | Luka / krytyka | Cytat-kotwica (str.) |
|---|---|---|---|---|---|
| 1 | | | | | „..." (s. ) |
| 2 | | | | | „..." (s. ) |
| 3 | | | | | „..." (s. ) |
| 4 | | | | | „..." (s. ) |
| 5 | | | | | „..." (s. ) |

---

## Prompt zakotwiczony do użycia z tą matrycą

```
Na podstawie WYŁĄCZNIE poniższej matrycy literatury:
1. Porównaj podejścia metodologiczne źródeł.
2. Przy każdej tezie wskaż numer wiersza-źródła.
3. Nie dodawaj wiedzy spoza tabeli; luki oznacz jako „brak danych".

[wklej matrycę]
```

## Kontrola jakości
- ☐ Każda teza ma cytat-kotwicę z numerem strony.
- ☐ Model w odpowiedzi nie „wyszedł" poza materiał z tabeli.
- ☐ Inny badacz odtworzyłby mój wniosek z tej matrycy.
