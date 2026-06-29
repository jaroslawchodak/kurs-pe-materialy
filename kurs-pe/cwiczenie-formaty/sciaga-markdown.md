# Ściąga: Markdown (podstawy)

> Markdown to lekki język znaczników: czysty tekst, który ma strukturę. Czytelny dla człowieka i dla modelu AI.

| Element | Zapis | Efekt |
|---|---|---|
| Nagłówki | `# H1`, `## H2`, `### H3` | hierarchia sekcji |
| Pogrubienie | `**tekst**` | **tekst** |
| Kursywa | `*tekst*` | *tekst* |
| Lista punktowana | `- pozycja` | wypunktowanie |
| Lista numerowana | `1. pozycja` | numeracja |
| Cytat | `> tekst` | blok cytatu |
| Kod / dane | ` ```...``` ` | blok dosłowny |
| Tabela | `\| a \| b \|` + `\|---\|---\|` | tabela |
| Link | `[opis](url)` | odnośnik |

## Dlaczego Markdown dla AI?
- Model dostaje **treść + strukturę** bez balastu formatowania (jak w DOCX/PDF).
- Mniej tokenów idzie na „śmieci" układu → tańszy i czystszy kontekst.
- Nagłówki i listy pomagają modelowi rozpoznać, co jest czym.

## Mini-przykład promptu w Markdown
```
## Rola
Jesteś recenzentem metodologii.

## Zadanie
Oceń poniższy fragment metod.

## Materiał
> [cytat]

## Format
Lista 3 mocnych i 3 słabych stron.
```
