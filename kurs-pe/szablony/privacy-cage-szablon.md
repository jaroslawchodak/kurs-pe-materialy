# Karta decyzyjna `privacy cage`

> `privacy cage` (klatka prywatności) = świadome ograniczanie przepływu danych badawczych do kontrolowanego, w miarę możliwości lokalnego środowiska.
> Wypełnij i trzymaj przy biurku. Reguła: **najpierw decyzja o środowisku, dopiero potem prompt.**

---

## Tabela decyzyjna: zadanie/dane → środowisko

| Typ zadania / danych | Frontier w chmurze | Lokalny LLM | Bez AI | Uzasadnienie |
|---|---|---|---|---|
| Burza mózgów na temat jawnym | ✅ | ✅ | | brak ryzyka |
| Analiza publikacji open access | ✅ | ✅ | | dane jawne |
| Redakcja własnego tekstu (bez danych osób) | ✅ | ✅ | | |
| Notatki z nazwiskami / instytucjami | ⚠️ po anonimizacji | ✅ | | minimalizacja |
| Transkrypcje wywiadów | ❌ | ⚠️ po anonimizacji | możliwe | ryzyko reidentyfikacji |
| Dane medyczne / osobowe wrażliwe | ❌ | ❌ | ✅ | bezwzględny zakaz |
| Cudza recenzja / manuskrypt pod NDA | ❌ | ❌ | ✅ | zobowiązanie poufności |

Legenda: ✅ dozwolone · ⚠️ warunkowo · ❌ niedozwolone

---

## Moje 3 stałe reguły

1. Zanim wkleję cokolwiek, pytam: **gdzie trafią te dane?**
2. Podaję **najmniej danych, ile trzeba** (minimalizacja).
3. Co wrażliwe — **zostaje lokalnie albo nie idzie do AI w ogóle.**

## Kompromis lokalny LLM
Lokalnie = dane nie opuszczają komputera, ALE: niższa jakość, wolniej, brak wiedzy webowej, większe ryzyko halucynacji. Używam go tam, gdzie **prywatność > jakość**.
