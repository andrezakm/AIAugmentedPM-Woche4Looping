# Experiment: PRD aus Template vs. PRD aus Zielkriterien

**Datum:** 2026-11-05
**Frage:** Funktioniert der PRD auch loop-basiert unter `/goal`, wenn das Template in Zielkriterien umformuliert wird? Und: Wie viel Unterstützung gehört in die Konstruktion, wie viel in die Überprüfung?
**Material:** [criteria.md](../../.claude/skills/prd-goal/criteria.md) (14 Kriterien), [skeleton.md](../../.claude/skills/prd-goal/skeleton.md) (nur Überschriften), [check_prd.py](../../.claude/skills/prd-goal/scripts/check_prd.py), [reviewers.md](../../.claude/skills/prd-goal/reviewers.md). Ergebnisse je Zelle: [scoreboard.md](scoreboard.md), Einzelberichte in `reviews/`.

---

## Kurzfassung

1. **Ja, es funktioniert, und es ist strenger als das Template.** Der Template-PRD (A), der unter dem alten Goal als fertig galt, erfüllt nur **4 von 14** Kriterien. Beide Kriterien-PRDs kommen nach zwei Runden auf **11 von 14**.
2. **Unterstützung beim Bauen spart einen Durchgang, ersetzt aber keine Prüfung.** C (Kriterien vorher bekannt) startet mit 10/14, B (nur Gerüst) mit 8/14. Nach Runde 2 stehen beide bei 11/14. Die Prüfer-Rückmeldung allein bringt B also auf dasselbe Niveau, sie kostet nur eine Runde mehr und macht den Text länger (304 → 436 Zeilen gegenüber 272 → 312).
3. **Alle drei Varianten wählen dasselbe Bedürfnis** (Grund zum Anrufen). Die Entscheidung ist robust gegenüber der Methode.
4. **Die letzten Kriterien konvergieren nicht, und das liegt am Prüfdesign, nicht am Text.** Siehe „Was nicht konvergiert“.

---

## Ergebnis

| | A Template | B nur Gerüst | C Gerüst + Kriterien |
|---|---|---|---|
| Runde 1 | 4/14 | 8/14 | 10/14 |
| Runde 2 | — | 11/14 | 11/14 |
| Noch offen | — | C12, C13, C14 | C11, C12, C13 |
| Länge Runde 1 → 2 | 351 | 304 → 436 (+43 %) | 272 → 312 (+15 %) |
| Gewähltes Bedürfnis | 1 | 1 | 1 |
| Subagenten | 5 Prüfer | 2 Autoren + 10 Prüfer | 2 Autoren + 10 Prüfer |

### Was das Template übersehen hat (A, 10 Kriterien ❌)
- **C2:** Drei „Zitate“ stammen aus dem alten Skript `PRD-writer.md`, nicht aus Interview oder Strategie. Seit dem Umbau haben sie keine Quelle mehr.
- **C3/C9:** Im Nachher-Narrativ stehen erfundene Details („Call 25“, „vor 9 Tagen“, „acht E-Mails“), ohne Kennzeichnung als illustrativ.
- **C6:** Nur zwei echte Gewichtungsvarianten. Die anderen „Szenarien“ ändern Punktwerte, nicht Gewichte.
- **C7:** S1 und S3 ohne wörtlichen Strategie-Satz.
- **C12:** 6 von 23 Regeln sind für einen Entwickler nicht testbar („Relevanz“, „Signalstärke“ undefiniert).
- **C14:** Ein frischer CEO-Testleser urteilt *verständlich mit Lücken*. Der CEO-Testleser in Goal 4 hatte *klar und überzeugend* gesagt.

Der alte Loop prüfte, ob die Abschnitte gefüllt waren. Ob sie gut waren, prüfte er nicht.

### Was nur durch Prüfung herauskam (B und C)
- **B r1, C9:** Ein Jenkins-Zitat war der falschen Situation zugeordnet. Die 40 % veraltete Kontakte fallen ihr beim Check *vor* dem Anruf auf, nicht beim Anruf.
- **C r2, C6:** Zwei Belege für Bedürfnis 1 gehören inhaltlich eher zu Bedürfnis 2. Korrigiert stünde eine Gewichtung 37 : 37. Das ist ein inhaltlicher Fund, kein Formfehler, und kein Autor hat ihn selbst bemerkt.

---

## Was nicht konvergiert, und warum

| Kriterium | Beobachtung | Ursache |
|---|---|---|
| **C12 Logik baubar** | B: 10 → 6 offene Regeln, aber 23 → 27 Regeln. C: 3 → 4 offene Regeln, obwohl die drei alten Fragen beantwortet sind. | Jeder frische Entwickler-Prüfer findet neue Randfälle. Mehr Regeln erzeugen mehr Randfälle. „Höchstens 1 offen“ ist mit wechselnden Prüfern praktisch unerreichbar. |
| **C13 Einwände** | Jeder frische Kunden-Prüfer bringt drei neue Einwände. B war in Runde 1 ✅ und in Runde 2 ❌. | Das Ziel wandert mit dem Prüfer. Ein Kriterium, das sich jede Runde neu definiert, kann nicht stabil erfüllt werden. |
| **C11 Nicht-Ziele** | C war in Runde 1 ✅ und in Runde 2 ❌ (ein strengerer Prüfer bemängelt, dass „Phase 2“ mehrdeutig ist). | Prüfer-Varianz. Die Grenze zwischen ✅ und ❌ verschiebt sich von Prüfer zu Prüfer. |
| **C14 CEO** | B bleibt ❌, weil B nur Platzhalter setzt. C wird ✅, weil der Autor eigene Aufwandsschätzungen eingesetzt hat (8–12 Personenwochen, 2 von 14 Leuten, als *Schätzung* markiert). | **Konflikt der Regeln.** C14 verlangt Zahlen, CLAUDE.md verbietet Zahlen ohne Quelle. C3 lässt gekennzeichnete Schätzungen zu und hat damit eine Lücke. Die Prüfung erzeugt Druck in Richtung Schätzung. |

**Lehre:** Frische Prüfer sind gut gegen Gefälligkeit (sie kennen den Autor nicht), aber schlecht für Konvergenz (jeder misst ein bisschen anders). Für einen Loop mit Abbruch braucht es beides: frische Prüfer für die erste Runde, danach **dieselbe Liste offener Punkte**, abgehakt statt neu erfunden.

---

## Antwort auf die Ausgangsfragen

**1. Funktioniert der PRD loop-basiert auf Zielkriterien?**
Ja. Die Kriterien finden mehr als das Template: 10 Mängel im fertigen Template-PRD, darunter zwei inhaltliche. Ein Template wird ausgefüllt, ein Kriterium wird geprüft. Das ist der Unterschied.

**2. Wie viel Unterstützung beim Bauen, wie viel beim Prüfen?**
- **Bauen:** Das Gerüst (nur Überschriften) reicht, um Struktur und Vergleichbarkeit zu halten. Die Kriterien vorher zu kennen spart etwa einen Durchgang und hält den Text kürzer. Ein Autor, der nur über Rückmeldungen lernt, repariert additiv: Er hängt an, statt umzubauen.
- **Prüfen:** Hier entsteht der Qualitätsgewinn. Mechanische Prüfungen (Skript) sind stabil und billig. Rollen-Testleser finden das, was kein Skript findet, schwanken aber.
- **Empfehlung:** Kriterien beim Bauen *zeigen*, Prüfung aber *unabhängig* halten. Dem Autor die Kriterien zu verschweigen bringt nichts außer Länge und einer Extrarunde.

**3. Wer prüft unter `/goal`?**
Laut Doku ein eigenes, kleines Modell, das nur das Gespräch sieht und keine Dateien liest ([code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal)). Unabhängige Prüfung entsteht also nur, wenn der Erbauer Skripte und Testleser startet und deren Urteil ins Gespräch holt. Das Experiment hat diese Rollen ausdrücklich getrennt: Autor-Subagent, Prüfer-Subagenten, Skript, Koordinator.

---

## Offen für einen Menschen

1. **Schätzungen im PRD:** Darf ein interner PRD markierte Aufwandsschätzungen enthalten (wie C), oder bleibt alles ohne Quelle `[Platzhalter]` (wie B)? Davon hängt ab, ob C14 erreichbar ist.
2. **Prüfdesign für Konvergenz:** In Runde 2 und später entweder dieselben Prüfer wieder einsetzen oder neuen Prüfern die offene Liste aus der Vorrunde mitgeben (abhaken statt neu suchen). Und C12 eventuell von „höchstens 1 offen“ auf „keine Frage, die den Bau blockiert“ umstellen.
3. **Befund aus C r2, C6:** Zwei Belege sind möglicherweise falsch zugeordnet, und korrigiert stünde in einer Gewichtung ein Patt. Das betrifft auch den echten PRD. Lohnt es sich, das in der Synthese nachzuprüfen?

---

## Loop-Protokoll

| Durchgang | Was gemacht | Ergebnis | Abbruchkriterium erfüllt? |
|---|---|---|---|
| 0 | `check_prd.py` gebaut und am Template-PRD getestet. Uhrzeiten (8:00) erzeugten Fehltreffer, Regex ergänzt. | Skript stabil | – |
| A | Template-PRD mit allen 6 Prüfern bewertet (C1 sinngemäß) | 4/14 | nein (Referenz, nicht überarbeitet) |
| B r1 | Autor nur mit Gerüst, 5 frische Prüfer | 8/14 | nein: C6, C9–C12, C14 |
| C r1 | Autor mit Gerüst + Kriterien, 5 frische Prüfer | 10/14 | nein: C10, C12–C14 |
| B r2 | Neuer Autor überarbeitet mit allen Berichten (ohne criteria.md), 5 frische Prüfer | 11/14 | nein: C12, C13, C14 |
| C r2 | Neuer Autor überarbeitet mit Berichten + criteria.md, 5 frische Prüfer | 11/14 | nein: C11, C12, C13 |
| Stopp | Abbruch nach Runde 2 statt Runde 4: Die offenen Kriterien schwanken mit dem Prüfer (C11, C12, C13) oder stehen im Konflikt mit CLAUDE.md (C14). Eine weitere Runde mit dem gleichen Design hätte neue Funde erzeugt, aber keinen Abschluss. | — | bewusst abgebrochen, offene Punkte oben |

**Abbruchkriterien**
- ✅ Template-PRD und zwei Kriterien-PRDs mit denselben Prüfern bewertet
- ✅ Unterschied Bauhilfe vs. Prüfung gemessen (B vs. C)
- ❌ Ein Kriterien-PRD mit 14/14: nicht erreicht, Ursache dokumentiert

---

## Nachtrag: Variante D (Kriterien v2, Neuschrift, Abhaken)

**D** = Blindentwurf (B r1) als Material, Neuschrift mit Kriterien v2, ab Runde 2 haken die Prüfer die offene Liste ab.

| | Runde 1 | Runde 2 | Länge |
|---|---|---|---|
| D | 10/14 (offen C10, C12, C13, C14) | **14/14** | 326 → 342 (+5 %) |

- **Konvergenz erreicht.** Erstmals 14/14, nach zwei Runden. Kein Prüfer hat in Runde 2 einen neuen Blocker oder K.-o.-Grund genannt.
- **Goodhart entschärft.** C14 ist ✅, ohne dass Zahlen erfunden wurden: Aufwand steht als Annahmen A1–A14 im Annahmen-Block, Geld als `[Platzhalter]`. Der Faktenprüfer hat alle Zahlen nachgerechnet.
- **Kaum Wachstum.** +5 % statt +43 % (B) bzw. +15 % (C).

**Vorsicht bei der Deutung**
- D läuft mit Kriterien v2. Zwei Regeln sind dort leichter erreichbar (C12 „blockierend“ statt „höchstens 1 offen“, C13 kumulative Liste). Der Gewinn ist also Prüfdesign **und** Methode, nicht trennbar.
- Abhaken ist milder als Neu-Suchen. Die Prüfer nennen unter „Hinweise, nicht bewertet“ weiterhin echte Lücken, z. B. „Phase 2“ hat zwei Bedeutungen (genau das hatte C r2 bei C11 durchfallen lassen) und die Kurzfassung sagt „verfehlt → kein Pilot“, der Plan erlaubt einmal Nachmessen. Grün heißt: die gesammelten Punkte sind erledigt, nicht: der Text ist fehlerfrei.
- Ein Durchlauf, ein Thema. Für eine belastbare Aussage bräuchte es Wiederholungen.

**Konsequenz:** Für einen Loop mit Abbruch ist v2 + Abhaken das Design, das konvergiert. Die Hinweise aus der letzten Runde gehören in die äußere Schleife: Der Mensch entscheidet, ob daraus ein neues Kriterium wird.

---

## Lackmustest: ursprünglicher Skill ohne Loop (O)

**O** = `scripts/PRD-writer.md` und `My-PRD-Template.md` aus dem letzten Commit, dieselbe Synthese, **ein Durchgang**: kein `/goal`, kein Quote-Check, keine Testleser. Bewertet in einer Runde mit denselben frischen Prüfern und Kriterien v2 wie D.

| | O ohne Loop | D mit Loop |
|---|---|---|
| Kriterien erfüllt | **3/14** (C4, C5, C8) | **14/14** |
| Zitate ohne Quelle | 4 | 0 |
| Annahmen gekennzeichnet | keine, Zahlen im Fließtext | A1–A14 im Block |
| CEO-Urteil | verständlich mit Lücken | klar und überzeugend |
| Kunden-Einwände beantwortet | 0 von 3 voll | 3 von 3 |
| Verständnisfragen Laie | 16 | 12 |
| Länge | 154 Zeilen | 342 Zeilen |
| Gewähltes Bedürfnis | 1 | 1 |

**Was der Ein-Schuss-PRD falsch macht:**
- **Wahrheit:** vier „Zitate“ ohne Quelle, ein erfundenes Nachher-Narrativ (60 Leads, Uhrzeiten, ein Beispiel-Brief) ohne Kennzeichnung, Zahlen wie „six weeks“ und „20 test prospects“ ohne Herkunft.
- **Entscheidbarkeit:** kein Aufwand außer „6 Wochen T&M“, kein Nutzen für NeoEmployee, keine Entscheidungen für den CEO. Der Kunde liest „seed of a reusable NeoEmployee product“ als: Wir bezahlen eure Produktentwicklung.
- **Abwägung:** Die beiden Bedürfnisse werden nicht bewertet, die Strategie nur umschrieben.

**Fairness:** C1, C6 und C7 verlangen Strukturen, die das alte Skript nie verlangt hat. Ohne diese drei steht O bei 3 von 11. Bei den Kriterien, die jeder gute PRD erfüllen sollte (Wahrheit C2, C3, C9; Entscheidbarkeit C13, C14), steht O bei **0 von 5**, D bei 5 von 5.

**Bemerkenswert:** Die Produktwahl ist dieselbe. Der Loop ändert nicht *was* gebaut wird, sondern ob man dem Dokument glauben und darauf entscheiden kann.
