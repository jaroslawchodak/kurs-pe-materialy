# DC-10 (B9) — Kwerenda agentowa z raportem w pliku

> Ćwiczenie z części „Dla chętnych" kursu *Prompt engineering w badaniach naukowych* (wersja 2, 28.10.2026). Wykonujesz je po oddaniu minimum na sali z bloku B9, w domu albo na mini-klinice. Pominięcie nie blokuje ukończenia kursu.

1. Załóż bezpłatny klucz do API OpenAlex (wymagany od lutego 2026 r. dla zapytań automatycznych) i zapisz go w pliku poza folderem projektu udostępnianym agentowi; agentowi podaj go w poleceniu albo jako zmienną środowiskową.
2. Zapisz protokół kwerendy w `notatki/protokol-kwerendy.md` i uruchom polecenie agentowe z B9.
3. Sprawdź raport: czy zawiera listę zapytań, daty, bazy, liczby trafień i odrzucone prace z powodem; czy DOI zostały potwierdzone w Crossref; czy `kandydaci.json` ma tyle rekordów, ile tabela w raporcie.
4. Uruchom ten sam protokół drugi raz (nowa sesja) i porównaj listy. Różnica pokazuje granice powtarzalności wyszukiwania agentowego.
