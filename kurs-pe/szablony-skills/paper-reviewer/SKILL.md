# Szablon skilla: `paper-reviewer` (recenzja wieloperspektywiczna)

> **Jak użyć:** skopiuj poniższą treść do pliku `.claude/skills/paper-reviewer/SKILL.md`
> albo wklej do czatu z poleceniem „Działaj dokładnie według tej procedury".
> Wersja skrócona (3 role zamiast 5) na potrzeby kursu — na wzór pełnego skilla
> `social-science-paper-reviewer` prowadzącego.

```markdown
---
name: paper-reviewer
description: >
  Wieloperspektywiczna recenzja tekstu naukowego z [nauk społecznych].
  Używaj, gdy użytkownik prosi o recenzję, krytyczną ocenę draftu
  albo „świeże oko" przed wysłaniem do czasopisma.
  NIE używaj do korekty językowej ani do pisania tekstu.
---
# Paper Reviewer — recenzja w trzech rolach

## Co robi ta procedura
Symuluje proces recenzencki: model KOLEJNO wciela się w trzy niezależne
role i dopiero na końcu składa werdykt. Każda rola pracuje osobno —
nie zagląda do ocen poprzedniej.

## Zasady nadrzędne
- Oceniaj wyłącznie tekst dostarczony przez użytkownika (zakotwiczenie);
  każdy zarzut musi wskazywać konkretny fragment/sekcję.
- Krytyka konstruktywna: zarzut + propozycja naprawy.
- Werdykt agenta to OPINIA POMOCNICZA — nie zastępuje wiedzy dziedzinowej
  i strategii publikacyjnej autora.

## Kroki
1. **Rola 1 — Recenzent metodologiczny:** oceń poprawność metody, dobór
   danych, zasadność wniosków wobec dowodów. Wynik: lista uwag M1, M2…
2. **Rola 2 — Recenzent dziedzinowy:** oceń osadzenie w literaturze
   [Twojego pola], nowość wkładu, trafność pojęć. Wynik: lista uwag D1, D2…
3. **Rola 3 — Adwokat diabła:** znajdź najmocniejszy argument PRZECIW
   publikacji; wskaż, czego tekst nie broni. Wynik: 1–3 zarzuty zasadnicze.
4. **Synteza — Redaktor:** zważ uwagi wszystkich ról; wydaj werdykt
   (accept / minor / major / reject) i ułóż MAPĘ POPRAWEK:
   uwagi uszeregowane od krytycznych do kosmetycznych.
5. Zapisz całość do `recenzje/review-agent-[data].md`.
```
