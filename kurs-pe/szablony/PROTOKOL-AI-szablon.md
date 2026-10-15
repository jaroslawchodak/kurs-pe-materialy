# Mój protokół pracy z AI
<!-- Jednostronicowy, osobisty. Efekt całego kursu. Trzymaj pod ręką. -->

## A. Szablon promptu (skrót)
1. **Rola/ton** — kim jest model, jak mówi, „nie zgaduj".
2. **Kontekst/dane** — tylko jawne/zanonimizowane; oddziel dane od instrukcji.
3. **Zadanie/kroki** — cel + ponumerowane kroki + żądanie cytatu-kotwicy.
4. **Format/ograniczenia** — Markdown/XML/JSON; długość; „luki = brak danych".

## B. Sygnalizator danych 🟢🟡🔴 (skrót)
- Trzy pytania: **czy da się rozpoznać osobę?** (→ 🔴) · **czy obiecałem poufność?** (→ 🔴) · **czy to niepublikowane i cenne?** (→ 🟡); wszędzie NIE → 🟢.
- 🟢 dowolne narzędzie · 🟡 trenowanie wyłączone, minimum danych, czat tymczasowy · 🔴 lokalnie, narzędzie zatwierdzone przez IOD albo bez AI.
- Wyłączenie trenowania nie zmienia 🔴 w 🟡; pseudonimizacja nie zmienia koloru; lokalny folder ≠ lokalny model.
- Moja tabela: [link do `sygnalizator-danych.md`]

## C. Checklista weryfikacji halucynacji
- ☐ Czy każda teza ma kotwicę w materiale?
- ☐ Czy sprawdziłem cytowania drabiną weryfikacji (orientacja: szczeble 1–2 na próbce; tekst: 1–4 każde; publikacja: 1–5 każde)?
- ☐ Czy źródło mówi to, co twierdzi model (teza, metoda, liczby — nie tylko „czy DOI działa")?
- ☐ Czy akapit z liczbami przeszedł STAT-5 (istotność, przyczynowość, uogólnienie, wielkość efektu)?
- ☐ Czy model oznaczył luki jako „brak danych", zamiast zgadywać?
- ☐ Czy wynik nie wyszedł poza podany materiał?

## D. Dobór narzędzia
| Sytuacja | Narzędzie |
|---|---|
| Proste pytanie jawne | zwykły czat |
| Trzeba aktualnych źródeł z cytatami | tryb research / Perplexity |
| Przegląd / ekstrakcja danych z wielu prac | Elicit / Consensus / Scite |
| Praca na własnej bibliotece | matryca literatury (Obsidian/Zotero/Bookends) |
| Dane 🔴 | lokalny LLM, narzędzie zatwierdzone przez IOD albo bez AI |
| Wieloetapowy proces na plikach (🟢/🟡) | ChatGPT Work / Claude Cowork (dla zaawansowanych Codex / Claude Code) + `CLAUDE.md`/`AGENTS.md` |

## E. Zasada proporcjonalności
Do prostego zadania — prosty prompt. Agent i RAG tylko tam, gdzie złożoność tego wymaga.

## F. Mój jeden najważniejszy nawyk z kursu
> ___________________________________________
