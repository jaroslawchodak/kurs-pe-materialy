# Protokół weryfikacji źródeł — procedura pięciu kroków (ściąga do wydruku)

> **Wersja 2 (28.10.2026):** od tej wersji kursu podstawowym narzędziem jest **protokół weryfikacji twierdzeń** i dziennik (`dziennik-weryfikacji-szablon.md`). Ta ściąga zostaje jako skrót dla twierdzeń typu B i A (istnienie publikacji i to, co publikacja twierdzi). Trzystopniowy werdykt odpowiada werdyktom z dziennika: istnieje+trafne = potwierdzone, istnieje+przekręcone = zniekształcone, nie istnieje = niepotwierdzone.

> Używasz, gdy model (czat, deep research, narzędzie literaturowe) poda Ci cytowanie, które ma trafić do Twojego przeglądu. Cel: odróżnić **trzy** stany źródła, nie dwa. Najgroźniejszy nie jest „źródło nie istnieje" — tylko **„źródło istnieje, ale teza przekręcona"**, bo przechodzi przez pobieżną kontrolę.

## Procedura na JEDNO cytowanie

1. **DOI → [doi.org](https://doi.org).** Wklej DOI. *Istnieje? Prowadzi do tego samego tytułu, który podał model?* Zmyślony DOI ma poprawny format, ale nie rozwija się w nic.
2. **Tytuł → Google Scholar / [OpenAlex](https://openalex.org) / PubMed.** *Praca istnieje? Autorzy i rok się zgadzają?*
3. **Teza → źródło (KROK KRYTYCZNY).** Otwórz abstrakt lub pełny tekst. *Czy praca rzeczywiście TWIERDZI to, co przypisał jej model?* Najczęstszy błąd: praca jest, ale mówi co innego — albo wręcz przeciwnie.
4. **[Scite](https://scite.ai) — druga opinia.** Smart Citations (wspiera / podważa / wzmiankuje): *jak inni traktują tę pracę? Czy teza raportu nie stoi w sprzeczności z jej recepcją?*
5. **Werdykt do karty oceny (trzystopniowy).**

## Karta oceny (kopiuj do notatek)

| # | Cytowanie (autor, rok, DOI) | Krok 1 DOI | Krok 2 istnieje | Krok 3 teza zgodna | Werdykt |
|---|---|---|---|---|---|
| 1 |  | ☐ tak ☐ nie | ☐ tak ☐ nie | ☐ tak ☐ nie/częściowo | ☐ istnieje+trafne ☐ istnieje+przekręcone ☐ nie istnieje |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## Co robisz z werdyktem

- **istnieje + trafne** → wolno użyć, z **cytatem-kotwicą** (dosłowny fragment + strona).
- **istnieje + przekręcone** → **NIE używaj sformułowania modelu.** Wróć do źródła i napisz tezę sam. To jest ta halucynacja, której nie łapie sprawdzenie samego DOI.
- **nie istnieje** → skreśl. Jeśli teza ważna — szukaj realnego źródła od zera.

## Próg intensywności

- **Do orientacji / burzy mózgów:** sprawdź **próbkę** (np. 3 wylosowane cytowania).
- **Do publikacji / recenzji:** sprawdź **KAŻDE** cytowanie. To, co idzie pod Twoje nazwisko, weryfikujesz w całości — „tak podała AI" nie jest usprawiedliwieniem (por. Blok 12, część „Etyka i granice AI").
