# Mój protokół pracy z AI
<!-- Jednostronicowy, osobisty. Efekt całego kursu. Trzymaj pod ręką. -->

## A. Szablon promptu (skrót)
1. **Rola/ton** — kim jest model, jak mówi, „nie zgaduj".
2. **Kontekst/dane** — tylko jawne/zanonimizowane; oddziel dane od instrukcji.
3. **Zadanie/kroki** — cel + ponumerowane kroki + żądanie cytatu-kotwicy.
4. **Format/ograniczenia** — Markdown/XML/JSON; długość; „luki = brak danych".

## B. Karta `privacy cage` (skrót)
- Pytanie odruchowe: **gdzie trafią te dane?**
- Minimalizacja: najmniej, ile trzeba.
- Wrażliwe → lokalnie albo wcale.
- Moja tabela: [link do `privacy-cage.md`]

## C. Checklista weryfikacji halucynacji
- ☐ Czy każda teza ma kotwicę w materiale?
- ☐ Czy sprawdziłem próbkę cytowań u źródła (DOI/PubMed/OpenAlex)?
- ☐ Czy model oznaczył luki jako „brak danych", zamiast zgadywać?
- ☐ Czy wynik nie wyszedł poza podany materiał?

## D. Dobór narzędzia
| Sytuacja | Narzędzie |
|---|---|
| Proste pytanie jawne | zwykły czat |
| Trzeba aktualnych źródeł z cytatami | tryb research / Perplexity |
| Przegląd / ekstrakcja danych z wielu prac | Elicit / Consensus / Scite |
| Praca na własnej bibliotece | matryca literatury (Obsidian/Zotero/Bookends) |
| Dane wrażliwe | lokalny LLM lub bez AI |
| Wieloetapowy proces na plikach | nadzorowany agent + plik instrukcji |

## E. Zasada proporcjonalności
Do prostego zadania — prosty prompt. Agent i RAG tylko tam, gdzie złożoność tego wymaga.

## F. Mój jeden najważniejszy nawyk z kursu
> ___________________________________________
