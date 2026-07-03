# Tor A — wzorcowe rozwiązanie: wiersz matrycy z abstraktu A1

> Do porównania po ćwiczeniu B8. To *poprawnie wykonana procedura*, nie jedyna słuszna treść. Zwróć uwagę: cytat-kotwica to dosłowny fragment, teza nie wykracza poza abstrakt, luka nazwana wprost.

| # | źródło | rok | metoda | teza główna | luka badawcza | cytat-kotwica (lokalizacja) |
|---|---|---|---|---|---|---|
| 1 | Abstrakt A1 (aktywność antyoksydacyjna) | — | ekstrakcja + 3 metody oznaczania (DPPH/ABTS/FRAP), ANOVA+Tukey | dobór metody oznaczania wpływa na wynik; DPPH i ABTS silnie skorelowane, FRAP mierzy częściowo inny mechanizm | brak walidacji na modelu komórkowym; jeden sezon zbioru | „korelacja DPPH–ABTS wysoka (r=0,89); FRAP korelował słabiej (r=0,61)" (A1, WYNIKI) |

## Wzorzec JSON tego samego rekordu (ćwiczenie B7)

```json
{
  "zrodlo": "Abstrakt A1 — aktywność antyoksydacyjna ekstraktów",
  "metoda": "3 metody oznaczania (DPPH, ABTS, FRAP) + Folin-Ciocalteu; ANOVA+Tukey",
  "teza": "Dobór metody oznaczania wpływa na wynik; do porównań międzygatunkowych zaleca się co najmniej dwie metody.",
  "luka": "brak walidacji na modelu komórkowym; jeden sezon zbioru",
  "cytat_kotwica": "korelacja DPPH–ABTS wysoka (r=0,89); FRAP korelował słabiej (r=0,61)",
  "lokalizacja": "A1, sekcja WYNIKI"
}
```

## Wzorzec — plan analizy dla `dane-pomiarowe.csv` (wariant „tutor statystyczny", B2)

Zmienna zależna: aktywność (ciągła). Czynnik: dawka (5 poziomów). Zalecenie startowe: **ANOVA jednoczynnikowa**, ale **przed** testem sprawdź: (1) normalność reszt (Shapiro-Wilk), (2) homogeniczność wariancji (Levene). Uwaga: różnica kontrola→dawka_niska duża, a dawka_wysoka→bardzo_wysoka minimalna (plateau) — rozważ model nieliniowy (dawka-odpowiedź) zamiast liniowego trendu. **Decyzję statystyczną podejmuje badacz** — model wskazuje warunki, nie werdykt.
