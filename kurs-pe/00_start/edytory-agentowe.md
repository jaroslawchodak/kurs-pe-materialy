# Edytory i terminale z obsługą agentów — mapa orientacyjna

Agent AI nie działa „w powietrzu" — mieszka w jakimś **środowisku**: edytorze kodu albo terminalu, który daje mu dostęp do plików i narzędzi. Dla badacza ważne są dwie rzeczy: (1) że to wciąż *ten sam* agent z plikami i instrukcjami (Blok 11), tylko w innym „opakowaniu", oraz (2) **gdzie trafiają moje dane** — bo część środowisk wysyła treść do chmury producenta modelu.

> To horyzont „dla chętnych", nie obowiązkowy etap kursu. Najpierw prompt (D1) i kontekst (D2); środowisko agentowe to dopiero D3.

## Agenty (środowiska agentowe) uruchamiane z interfejsem graficznym (GUI/IDE)
Ten sam agent, tylko w „opakowaniu" z oknem zamiast wiersza poleceń — aplikacja desktopowa, webowa lub wtyczka do edytora. Wygodniejszy start dla osób, które nie pracują na co dzień w terminalu.
| Narzędzie | Czym jest |
|---|---|
| **Claude Code** | ten sam agent Anthropic jako aplikacja desktopowa (macOS/Windows), aplikacja webowa (`claude.ai/code`) oraz rozszerzenie do VS Code / JetBrains |
| **OpenAI Codex** | rozszerzenie do IDE (VS Code) oraz wersja chmurowa/webowa |
| **Google Antigravity** | agentowa platforma Google: edytor (IDE, fork VS Code) + osobna aplikacja desktopowa do orkiestracji agentów; model w chmurze Google |
| **OpenCode** | ten sam otwarty agent w wersji z interfejsem graficznym (desktop/web); pozwala wpiąć **model lokalny (Ollama)** → wariant `privacy cage` |

## Agenty (środowiska agentowe) uruchamiane z terminala (CLI)
Ten sam agent uruchamiany z wiersza poleceń — lekki, skryptowalny, łatwy do wpięcia modelu lokalnego.
| Narzędzie | Czym jest |
|---|---|
| **Claude Code** | agent terminalowy Anthropic; czyta/zapisuje pliki, uruchamia komendy, czyta `CLAUDE.md` |
| **OpenAI Codex (CLI)** | agentowy asystent kodu/automatyzacji z linii poleceń |
| **Antigravity CLI** | terminalowy agent Google (komenda `agy`, następca Gemini CLI); ten sam silnik co aplikacja Antigravity 2.0 |
| **OpenCode** | otwarty agent terminalowy; łatwo wpiąć **model lokalny (Ollama)** → wariant `privacy cage` |

## Edytory / terminale (środowisko z interfejsem)
Tu agent jest *dodatkiem* do edytora lub terminala ogólnego przeznaczenia (a nie samodzielnym środowiskiem agentowym jak wyżej).
| Narzędzie | Czym jest | Uwaga o danych |
|---|---|---|
| **VS Code** (+ rozszerzenia AI) | najpopularniejszy edytor; agenci jako wtyczki | zależnie od wtyczki/modelu — sprawdź, dokąd idzie kontekst |
| **Cursor** | edytor (fork VS Code) wbudowany pod pracę z agentem | domyślnie korzysta z modeli w chmurze |
| **Zed** | szybki edytor z trybem asystenta AI | konfigurowalny model; możliwe modele lokalne |
| **Warp** | terminal z wbudowanym asystentem AI | część funkcji AI działa po stronie usługi |


## Jak czytać tę mapę (zasada ograniczonego zaufania, Blok 1)
- Środowisko **nie zmienia** zasad: agent = prompt + kontekst + pliki instrukcji + **nadzór człowieka**.
- Zanim wpuścisz materiał badawczy, zadaj pytanie z Bloku 1: **„gdzie trafią moje dane?"**. Materiały wrażliwe / pod NDA → środowisko z modelem **lokalnym** (OpenCode + Ollama, model lokalny w edytorze), nie chmurowym.
- Wybór środowiska to wygoda; bezpieczeństwo zależy od pliku instrukcji (`INSTRUKCJE-PROJEKTU.md`) i częstości Twojej akceptacji kroków.

## Dla chętnych: spróbuj zainstalować agenta
Jeśli masz sprzęt i ochotę poeksperymentować przed Blokiem 11, zainstaluj jedno ze środowisk agentowych — **Claude Code**, **OpenAI Codex** lub **Google Antigravity**. Każde ma wersję terminalową (CLI) i z interfejsem (GUI/IDE), więc wybierz wygodniejszą dla siebie. Instalacja jest opcjonalna: w każdym bloku jest wariant podstawowy bez instalacji (zob. `cheatsheet-przed-kursem.md`, pkt 3).

## Powiązania
- Pełny obraz agenta nad plikami → Blok 11 + `modul-clustering-demo.md`.
- Decyzja chmura/lokalnie → Blok 10, karta `privacy-cage-szablon.md`.
- Trzy mechanizmy rozszerzania agenta (Skills · MCP · Python) → `sciaga-skills.md`. 
