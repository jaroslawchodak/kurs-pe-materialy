# Sygnalizator moich danych 🟢🟡🔴

> Wypełniasz w Bloku 4, uzupełniasz w Bloku 10, trzymasz przy biurku.
> Reguła: **najpierw kolor danych, dopiero potem prompt albo udostępnienie folderu.**
> Ten szablon zastępuje `mapa-ryzyka-szablon.md` i `privacy-cage-szablon.md` (wersja z października 2026).

Imię / dyscyplina: ...
Data ostatniej kontroli ustawień kont: ...

---

## Trzy pytania (zawsze w tej kolejności)

```text
1. Czy z tych danych da się rozpoznać konkretną osobę
   (wprost albo z kombinacji cech: wiek + miejscowość + diagnoza)?   TAK → 🔴
2. Czy to nie moje albo obiecałem poufność
   (cudza recenzja, manuskrypt do recenzji, NDA, zgoda uczestników,
   warunki komisji etycznej)?                                          TAK → 🔴
3. Czy to niepublikowane i cenne
   (mój manuskrypt, wniosek grantowy, nowy pomysł, surowe wyniki)?    TAK → 🟡
Wszędzie NIE                                                           → 🟢
```

## Co oznacza każdy kolor

| Światło | Przykłady | Gdzie wolno pracować | Jak |
|---|---|---|---|
| 🟢 **Zielone** | opublikowane artykuły, metadane bibliograficzne, publiczne zbiory danych (GUS, Eurostat, GenBank), źródła drukowane domeny publicznej, sylabus, własny tekst bez danych osób trzecich | dowolne narzędzie z kursu, także konto darmowe | dobra higiena: trenowanie modelu wyłączone |
| 🟡 **Żółte** | niepublikowany manuskrypt, wniosek grantowy, dane zagregowane lub spseudonimizowane, kod analizy, notatki zespołu bez nazwisk, niepublikowane wyniki pomiarów | konto z **wyłączonym trenowaniem** albo czat tymczasowy / incognito; narzędzie instytucjonalne; model lokalny | podaj minimum potrzebne do zadania; nie zapisuj w pamięci ani w stałych projektach; usuń rozmowę po pracy |
| 🔴 **Czerwone** | dane osobowe, dane pacjentów i dokumentacja medyczna, nagrania i transkrypcje przed anonimizacją, dane szczególnych kategorii (RODO art. 9: zdrowie, poglądy, wyznanie, dane genetyczne), cudze recenzje i manuskrypty do recenzji, materiały pod NDA | **nie** do chmury konsumenckiej, także z wyłączonym trenowaniem | model lokalny (Blok 10), narzędzie zatwierdzone przez IOD albo bez AI; przy danych osobowych konsultacja z IOD uczelni |

---

## Moje dane

| Typ danych | Kolor | Narzędzie, którego używam | Warunki (minimum danych, czat tymczasowy, kopia) | Dla 🔴: lokalnie / instytucjonalnie / bez AI — i dlaczego |
|---|---|---|---|---|
| np. artykuły open access do przeglądu | 🟢 | ChatGPT, Claude, NotebookLM | — | — |
| np. mój niepublikowany manuskrypt | 🟡 | Claude (trenowanie wyłączone) | tylko fragment; rozmowę usuwam po pracy | — |
| np. surowe wyniki pomiarów przed publikacją | 🟡 | ChatGPT Work (folder projektu) | tylko zagregowane tabele, bez notatek laboratoryjnych | — |
| np. transkrypcje wywiadów | 🔴 | — | — | lokalnie: Ollama + `granite4.2:8b`, po konsultacji z IOD |
| np. recenzja dla czasopisma | 🔴 | — | — | bez AI (polityka wydawcy) |
| | | | | |
| | | | | |
| | | | | |

---

## Moje konta (zaznacz po sprawdzeniu)

- [ ] **ChatGPT:** Ustawienia → Kontrola danych → „Ulepszaj model dla wszystkich" (*Improve the model for everyone*) = WYŁ.
- [ ] **Claude:** Ustawienia → Prywatność → „Pomóż ulepszać Claude" (*Help improve Claude*) = WYŁ. (adres: `claude.ai/settings/data-privacy-controls`)
- [ ] **Gemini** (jeśli używam): Aktywność → „Zachowuj aktywność" (*Keep Activity*) = WYŁ.
- [ ] Wiem, gdzie jest **czat tymczasowy** (ChatGPT) i **czat incognito** (Claude).
- [ ] Folder udostępniony agentowi (ChatGPT Work / Claude Cowork) zawiera **tylko 🟢 i 🟡**.
- [ ] Folder projektu z danymi 🟡 **nie jest synchronizowany** z OneDrive (🪟) ani iCloud „Biurko i Dokumenty" (🍎).

> Ustawienia są na koncie, więc działają tak samo w przeglądarce i w aplikacjach na Windows i macOS. Sprawdzaj je po każdej dużej aktualizacji aplikacji — nazwy pozycji menu potrafią się zmieniać (stan: 15.10.2026).

---

## Trzy reguły

1. **Wyłączenie trenowania nie zmienia 🔴 w 🟡.** Przełącznik decyduje tylko o tym, czy rozmowa posłuży do uczenia kolejnych modeli. Dostawca nadal przechowuje rozmowy (zwykle ok. 30 dni).
2. **Pseudonimizacja nie zmienia koloru.** Kod `R-017` zamiast nazwiska jest odwracalny, więc dane wciąż są osobowe. W razie wątpliwości kolor zostaje 🔴.
3. **Lokalny folder ≠ lokalny model.** ChatGPT Work i Claude Cowork czytają pliki z Twojego dysku, ale ich treść wysyłają do modelu w chmurze.

## Test mozaikowy (przed zmianą koloru z 🔴 na niższy)

Czy po „anonimizacji" rzadka kombinacja cech (wiek + miejscowość + zawód + diagnoza, styl wypowiedzi, znane fakty) wciąż wskazuje konkretną osobę — zwłaszcza w małej grupie?
☐ TAK → kolor zostaje 🔴   ☐ NIE → można rozważyć 🟡 (decyzja przy danych osobowych: IOD)

> ⚠️ To nie porada prawna. Przy danych osobowych i medycznych decyduje IOD (inspektor ochrony danych) Twojej uczelni.
