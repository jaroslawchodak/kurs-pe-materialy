# Ściąga: XML w prompcie (podstawy)

> XML (eXtensible Markup Language) to język znaczników: treść otaczasz parami znaczników otwierających i zamykających `<nazwa> ... </nazwa>`, które tworzą nazwane bloki. Pierwotnie powstał do wymiany danych między programami; w promptach wykorzystujemy go do **twardego, nazwanego oddzielania bloków** — model nie myli instrukcji z danymi.

## Podstawowa składnia
```
<rola>
Jesteś recenzentem metodologii w naukach społecznych.
</rola>

<kontekst>
Analizuję sekcję metod artykułu z socjologii.
</kontekst>

<material>
[tu wklejasz cytat lub dane — nawet jeśli zawierają własne nagłówki, są bezpiecznie odgrodzone]
</material>

<zadanie>
1. Wskaż 3 mocne strony.
2. Wskaż 3 słabe strony.
</zadanie>

<format>
Tabela: aspekt | ocena | uzasadnienie.
</format>
```

## Kiedy XML, a kiedy Markdown?
| Sytuacja | Lepszy format |
|---|---|
| Krótki, prosty prompt | Markdown (lekki, czytelny) |
| Wiele bloków (instrukcja + kilka cytatów + dane + format) | XML (twarde granice) |
| Materiał zawiera własne nagłówki/`#`/tabele | XML (odgradza dane od instrukcji) |
| Dokument do czytania przez człowieka | Markdown |

## Uwaga
XML to nie magia. Do prostego zadania niepotrzebnie dokłada szumu. **Format dobieraj do złożoności, nie z mody.**
