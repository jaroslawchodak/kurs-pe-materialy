---
name: analiza-opisowa
description: >
  Używaj, gdy użytkownik prosi o statystyki opisowe lub tabelę podsumowującą dla
  pliku danych CSV/XLSX z folderu dane/. Nie używaj do testów istotności,
  o które użytkownik wprost nie prosił, ani do interpretacji przyczynowej.
---
# Analiza opisowa danych (odtwarzalna)

## Co robi ta procedura
Pisze i uruchamia skrypt (Python lub R) liczący statystyki opisowe, tak aby każdą
liczbę w raporcie dało się odtworzyć, uruchamiając skrypt ponownie.

## Wejście i wyjście
Wejście: plik w dane/ wskazany przez użytkownika oraz dane/README.md z opisem kolumn
(jednostki, kodowanie braków danych).
Wyjście: skrypt w analiza/, wyniki/statystyki.md, wpis w notatki/log.md.

## Kroki
1. Przeczytaj opis kolumn. Pokaż PLAN: które zmienne, jakie statystyki (n, braki,
   średnia, SD, mediana, kwartyle, min–max; dla zmiennych jakościowych liczności
   i odsetki), w jakich grupach. CZEKAJ na akceptację.
2. Napisz skrypt w analiza/opis.py (lub .R). Skrypt czyta dane z dane/, nie modyfikuje ich
   i zapisuje tabele wynikowe.
3. Uruchom skrypt. Wynik zapisz w wyniki/statystyki.md: tabele + opis kroków + polecenie,
   którym skrypt uruchomić ponownie.
4. Przepuść raport przez STAT-5: każda liczba z wyjścia skryptu; brak słowa „istotny"
   bez testu; brak języka przyczynowego; brak uogólnień poza próbę; podana niepewność (SD lub przedział).

## Reguły
- Każda liczba w raporcie pochodzi z wyjścia skryptu; nie liczysz „w pamięci".
- Nie wykonujesz testów istotności ani modeli, o które nie poproszono.
- Nie interpretujesz przyczynowo i nie piszesz wniosków merytorycznych.
- Jeśli dane zawierają kolumny identyfikujące osoby — ZATRZYMAJ SIĘ i zgłoś.
