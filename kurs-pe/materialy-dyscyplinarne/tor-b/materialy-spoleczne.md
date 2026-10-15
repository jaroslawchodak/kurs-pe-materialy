# Tor B — materiały społeczne (psychologia, prawo)

> Materiał jawny/zanonimizowany do ćwiczeń B3, B6, B8. Uzupełnia gotowy korpus w `clustering-demo/summaries/` (m.in. Lazer 2009, Edelmann 2020 — computational social science).

---

## B1 · Fragment zanonimizowanej transkrypcji wywiadu (do ćwiczeń z anonimizacji i zakotwiczenia)

> Uwaga: identyfikatory zastąpiono kluczem (R-017). Pseudonimizacja nie zmienia koloru danych (sygnalizator 🟢🟡🔴): prawdziwa transkrypcja z kluczem R-017 wciąż byłaby 🔴. Ten fragment jest fikcyjny i jawny, dlatego wolno na nim ćwiczyć w chmurze.

**Badacz:** Jak zmieniła się Pani praca po wdrożeniu nowego systemu?
**R-017:** Na początku było trudno, bo nikt nie tłumaczył, jak to działa. Uczyliśmy się metodą prób i błędów. Po dwóch miesiącach było już lepiej, ale wciąż nie ufam automatycznym podpowiedziom — wolę sprawdzić sama.
**Badacz:** Co konkretnie sprawdza Pani ręcznie?
**R-017:** Wszystko, co idzie do dokumentacji pacjenta. Tam nie ma miejsca na błąd systemu.

*(Ćwiczenie: zbuduj wiersz matrycy „temat | teza uczestnika | cytat-kotwica"; oznacz, które dane trzeba by usunąć przed wysłaniem do modelu chmurowego.)*

---

## B2 · Szkielet projektu badania ankietowego (do ćwiczenia „projektowanie badań", B2/B5)

**Problem:** Czy sposób wprowadzenia narzędzia AI (szkolenie vs brak) wiąże się z poziomem zaufania użytkowników?
**Zmienne:** niezależna — typ wdrożenia (szkolenie / samodzielne); zależna — zaufanie (skala 1–7); kontrolne — wiek, staż, wcześniejsze doświadczenie.
**Luka:** brak danych podłużnych — pomiar tylko po wdrożeniu.

*(Ćwiczenie: użyj AI jako partnera do namysłu — niech zada pytania doprecyzowujące, zanim zaproponuje hipotezy; oznacz, które zależności to spekulacja.)*

---

## Wzorzec

Poprawnie wykonany wiersz matrycy z B1: *temat = zaufanie do automatyzacji; teza = użytkownik zachowuje ręczną weryfikację danych krytycznych mimo adaptacji do systemu; cytat-kotwica = „Wszystko, co idzie do dokumentacji pacjenta. Tam nie ma miejsca na błąd systemu."* Dane do usunięcia przed chmurą: kontekst medyczny + wszelkie szczegóły umożliwiające identyfikację (efekt mozaikowy).
