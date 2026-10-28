# Dziennik weryfikacji — szablon

> Do Bloków 4, 8, 9 i 12. Dziennik dokumentuje, **co** sprawdziłeś w wyniku AI, **gdzie** i **z jakim rezultatem**. Dołączasz go do dokumentacji projektu i przywołujesz w oświadczeniu o użyciu AI.
> Zasada: sprawdzasz **twierdzenie po twierdzeniu**, nie ogólne wrażenie z całej odpowiedzi.

---

## Protokół w pięciu krokach

| Krok | Co robisz |
|---|---|
| 1. Dekompozycja | rozkładasz tekst na ponumerowane **twierdzenia atomowe** (jedno twierdzenie = jedna informacja, którą da się osobno sprawdzić) |
| 2. Typ | **B** — istnieje publikacja X · **A** — publikacja X twierdzi Y · **E** — liczba, wynik, próba · **I** — interpretacja lub synteza |
| 3. Dowód | dla B, A, E: źródło pierwotne + lokalizacja (strona, sekcja, tabela) + dosłowny fragment; dla I: numery twierdzeń, na których wniosek stoi |
| 4. Werdykt | **potwierdzone** · **zniekształcone** (źródło istnieje, ale mówi co innego lub mniej) · **niepotwierdzone** (brak dowodu) · **sprzeczne** (dowód mówi coś przeciwnego); adnotacja: *wycofana/skorygowana* |
| 5. Decyzja | **użyj** · **przeformułuj sam** (na podstawie źródła) · **usuń** |

**Gdzie szukać dowodu (drabina weryfikacji):** B → szczeble 1–2 (doi.org, Google Scholar, OpenAlex, PubMed; źródła polskie: Biblioteka Nauki, BazHum, NUKAT) · A i E → szczeble 3–4 (**tekst źródła, nie abstrakt**) · status pracy → szczebel 5 (baner wydawcy, Retraction Watch przez Crossref, Scite).

**Próg zależy od stawki:**
- orientacja w temacie → losowa próbka twierdzeń B i A (min. 3), szczeble 1–2,
- własny tekst → wszystkie twierdzenia B, A, E, szczeble 1–4,
- publikacja → wszystkie twierdzenia, szczeble 1–5.

---

## Prompt do kroku 1 (dekompozycja)

```text
Rozłóż poniższy tekst na ponumerowane twierdzenia atomowe:
jedno twierdzenie = jedna informacja, którą da się osobno sprawdzić.
Przy każdym podaj typ: B (istnienie publikacji), A (publikacja X twierdzi Y),
E (liczba, wynik, próba), I (interpretacja lub synteza).
Nie oceniaj prawdziwości, nie poprawiaj i nie dodawaj treści.
Format: tabela | nr | twierdzenie | typ | fragment tekstu, z którego pochodzi |
"""
<wklejony tekst do sprawdzenia>
"""
```

## Opcjonalnie: pytania kontrolne (Chain-of-Verification)

```text
[rozmowa 1] Do każdego twierdzenia typu A i E z tabeli sformułuj jedno pytanie
kontrolne, na które da się odpowiedzieć z tekstu źródła. Nie odpowiadaj na nie.

[rozmowa 2, NOWA, z załączonym źródłem] Odpowiedz na pytania wyłącznie na podstawie
załączonego tekstu. Przy każdej odpowiedzi podaj stronę lub sekcję.
Jeśli tekst nie zawiera odpowiedzi, napisz „brak w źródle".
```
Rozbieżności między tekstem a odpowiedziami kontrolnymi wskazują twierdzenia, które sprawdzasz w pierwszej kolejności. Werdykt wydajesz Ty, nie model.

---

## Dziennik (kopiuj do `notatki/dziennik-weryfikacji-<nazwa>.md`)

```markdown
# Dziennik weryfikacji — [czego dotyczy, np. akapit przeglądu z 28.10.2026]

Sprawdzany tekst: [plik lub opis] · Narzędzie, które go wytworzyło: [model, tryb, data]
Stawka: ☐ orientacja ☐ własny tekst ☐ publikacja · Sprawdzający: [imię]

| nr | twierdzenie | typ | źródło i lokalizacja | dosłowny fragment | werdykt | decyzja | data |
|----|-------------|-----|----------------------|-------------------|---------|---------|------|
| 1  |             |     |                      |                   |         |         |      |
| 2  |             |     |                      |                   |         |         |      |
| 3  |             |     |                      |                   |         |         |      |

## Podsumowanie
- Sprawdzono: __ twierdzeń (B: __, A: __, E: __, I: __)
- Potwierdzone: __ · zniekształcone: __ · niepotwierdzone: __ · sprzeczne: __
- Reguła promptu, która zapobiegłaby znalezionym błędom (→ `PROTOKOL-AI.md`):
```

## Przykład wypełnienia

| nr | twierdzenie | typ | źródło i lokalizacja | dosłowny fragment | werdykt | decyzja | data |
|----|-------------|-----|----------------------|-------------------|---------|---------|------|
| 3 | Travers i Milgram (1969) zaczęli od 296 osób | E | *Sociometry* 32(4), sekcja metod | „…" | potwierdzone | użyj | 28.10 |
| 4 | Milgram (1967) opisał 64 ukończone łańcuchy | A | *Psychology Today* 1(1) | brak | zniekształcone (liczba z pracy z 1969 r.) | przeformułuj | 28.10 |

**Wszystkie twierdzenia potwierdzone?** To też wynik. Zapisz liczbę sprawdzonych twierdzeń. Jedna poprawna odpowiedź nie dowodzi rzetelności narzędzia.
