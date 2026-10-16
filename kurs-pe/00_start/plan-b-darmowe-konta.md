# Plan B dla kont darmowych

> 40% grupy pracuje wyłącznie na planach darmowych. Limity (Deep Research, załączniki PDF, Projects/custom instructions) mogą zablokować ćwiczenie w połowie. Ta tabela daje obejście do **każdego** zagrożonego kroku — tak, aby brak subskrypcji nigdy nie oznaczał „nie zrobiłem ćwiczenia".
>
> **Reguła prowadzenia:** narzędzia z limitem uruchamiamy **na początku** bloku (generacja trwa). Prowadzący ma zapasowe konto z subskrypcją do demonstracji.

| Blok | Ćwiczenie / funkcja | Funkcja premium, która może zawieść | Obejście darmowe |
|---|---|---|---|
| B1 | porównanie narzędzi | limit wiadomości w trybie research | zadaj jedno pytanie, nie serię; użyj Perplexity (darmowy tryb ma odnośniki) |
| B6 | załącznik PDF do czatu | limit rozmiaru/liczby załączników | skonwertuj PDF → Markdown skryptem (Blok 6) i wklej **tekst**, nie plik — mniej tokenów, brak limitu załączników |
| B8 | matryca + Gemini Notebook | — | **Gemini Notebook jest darmowy i bez instalacji** — dlatego jest osią Dnia 2 |
| B9 | Deep Research | darmowy limit ChatGPT/Gemini (często 1–5 raportów/mies.) | uruchom **na starcie bloku**; 1 raport wystarcza do ćwiczenia. Alternatywa: Perplexity (darmowe „Pro Search") lub Elicit (darmowy limit ekstrakcji) |
| B9 | narzędzia literaturowe | limit Elicit/Consensus | rozłóż zapytania; użyj **OpenAlex** i **Semantic Scholar** (w pełni darmowe API/web) do weryfikacji |
| B10 | model lokalny | — | model lokalny jest **darmowy z definicji**; brak sprzętu → artefaktem jest karta decyzyjna, nie uruchomienie |
| B11 | Projects / custom instructions | funkcja płatna w niektórych czatach | ścieżka ręczna: wklej `INSTRUKCJE-PROJEKTU.md` **na początku każdej rozmowy** jako stały nagłówek — daje ten sam efekt „konstytucji" bez Projects |
| B11 | agent (Claude Code) | koszt API/subskrypcji | **OpenCode + model lokalny (Ollama)** — darmowy i offline; albo zostań przy ścieżce ręcznej w czacie (trzon ćwiczenia jej nie wymaga) |

## Zasada ogólna

Darmowy plan wystarcza na **cały kurs**, jeśli:
1. ciężkie generacje (Deep Research) uruchamiasz **raz, na początku bloku**,
2. do modelu wysyłasz **czysty tekst** (Markdown), nie duże pliki PDF,
3. do weryfikacji używasz w pełni darmowych źródeł: **doi.org, OpenAlex, Semantic Scholar, PubMed, Google Scholar**.

Płatna subskrypcja przyspiesza pracę, ale **nie jest warunkiem** zdobycia żadnego artefaktu kursowego.
