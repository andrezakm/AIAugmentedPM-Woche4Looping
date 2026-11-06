# Review B, Runde 2: Faktenprüfer

Geprüft: `output/experiment-prd/B-PRD.md` gegen `.claude/skills/prd-goal/criteria.md`, Kriterien C3, C5, C6, C7, C8, C9, C10, C11, C13.
Gelesen: PRD, criteria.md, `input/` (alle 10 Interviews), `context/` (company.md, strategy.md), `reviews/B-r2-skript.txt`, `reviews/B-r2-kunde.md`. Keine anderen Dateien aus `output/`.

---

## C3 Keine erfundenen Zahlen

### Skriptliste (35 Treffer), Entscheidung je Zahl

| Zeile | Zahl(en) | Was es ist | Zulässig? |
|---|---|---|---|
| 27 | 7 | Verweis auf Ziel Z7 | ✅ Bezeichner |
| 41 | 7 | „Z5 bis Z7“ | ✅ Bezeichner |
| 131 | 7, 8 | „fünf von acht Faktoren“, F7, F8 | ✅ Zählung bzw. Bezeichner aus dem PRD (8 Faktoren in A.2) |
| 189 | 8 | Regel B8 | ✅ Bezeichner |
| 192 | 11 | Regel B11 | ✅ Bezeichner |
| 194 | 13 | Regel B13 | ✅ Bezeichner |
| 205 | 11 | Verweis auf B11 | ✅ Bezeichner |
| 248 | 7 | Z7 | ✅ Bezeichner |
| 267 | 7 | „Z5 und Z7“ | ✅ Bezeichner |
| 271 | 8 | B8 | ✅ Bezeichner |
| 321 | 7 | Z7 | ✅ Bezeichner |
| 322 | 7, 7 | „Z1 bis Z7“, Z7 | ✅ Bezeichner |
| 335 | 7, 7 | B7, Z7 | ✅ Bezeichner |
| 345 | 7 | „Z5 bis Z7“ | ✅ Bezeichner |
| 354 | 7 | „Z2 bis Z7“ | ✅ Bezeichner |
| 356 | 8, 7 | B8, B7 | ✅ Bezeichner |
| 384 | 7 | F7 | ✅ Bezeichner |
| 385 | 8 | F8 | ✅ Bezeichner |
| 387 | 7, 8 | F7, F8 | ✅ Bezeichner |
| 393 | 7, 8 | Tabellenkopf F7, F8 | ✅ Bezeichner |
| 403 | 26, 13 | Summen G2 | ✅ berechnet; nachgerechnet: B1 3×(2+2+2)+(2+2+2+1+1)=26, B2 3×(1+1+0)+(1+2+1+1+2)=13 |
| 404 | 7, 8 (sowie 22, 19) | F7, F8; Summen G3 | ✅ berechnet; nachgerechnet: B1 3×(2+1+1)+10=22, B2 3×(2+1+2)+4=19 |
| 405 | 8 | F8 | ✅ Bezeichner |
| 407 | 8, 26, 7, 13 | Rechenweg G2 | ✅ berechnet, stimmt |

Ebenfalls nachgerechnet (nicht in der Skriptliste): G1 B1 = 14, B2 = 9 ✅; G4 B1 = 9 + 3 = 12, B2 = 6 + 6 = 12 ✅. Die Punktetabelle A.3 passt zu den Symbolen in A.2 ✅.

**Alle 35 Skripttreffer sind zulässig** (Bezeichner, Zählungen aus dem PRD oder nachvollziehbar berechnet).

### Stichprobe weiterer Zahlen gegen `input/` und `context/`

| Zahl im PRD | Fundstelle | Ergebnis |
|---|---|---|
| 15 Min. / 4 pro Stunde | Thorne, Interview_Gen_08 | ✅ |
| 40 Min. | O'Neil, „forty minutes“, Interview_Gen_10 | ✅ |
| 20 Min. für eine E-Mail | Ross, „spend 20 minutes reading … just to write one email“ | ✅ |
| 30 Min. | Green, Interview_Gen_07 | ✅ |
| 4 Std. für 10 Kontakte | Chen, Interview_Gen_03 | ✅ |
| 20 statt 50 Calls | Jenkins, Interview_Gen_01 | ✅ (nur eine Person; im PRD als Jenkins gekennzeichnet) |
| 40 % nicht mehr im Unternehmen | Jenkins, „like 40% of the time“ | ✅ |
| 5 von 100 Leads | Blunt, Interview_Gen_05 | ✅ |
| $80k, 2 hours a day, 90 % | Kim, Interview_Gen_06 | ✅ |
| 9 times out of 10 | O'Neil | ✅ |
| unter 2 Minuten | O'Neil, „under two minutes“ | ✅ (O'Neil meint *finden*, der PRD auch *lesen*; vertretbar) |
| 12 Leute (14 minus 2) | strategy.md „2 of our 14 people“ | ✅ berechnet |
| „A dozen“ SDRs im Lead-Gen-Team | Ross | ✅ |
| 5 Bausteine (N3) | Zählung der im PRD genannten Bausteine | ✅ |
| zwei bis drei / höchstens drei Signale | O'Neils „three things“ | ✅ abgeleitet |
| 9 von 10 (Bedürfnis 1), 5 von 10 (Bedürfnis 2), „davon einer nur teilweise“ | Zählung über die Interviews; die Zuordnung der Personen steht nicht im PRD | ✅ mit Vorbehalt: nachvollziehbar (Bedürfnis 1: alle außer Kim; Bedürfnis 2: Jenkins, Baker, Kim, Chen sowie teilweise Thorne), aber im PRD nicht aufgeschlüsselt. Empfehlung: Namen nennen. |
| drei Käufer | Zählung der genannten Rollen | ✅ |

Ergebnis: Ich habe keine Zahl ohne Quelle, ohne Rechnung, ohne Kennzeichnung oder ohne Platzhalter gefunden. **C3 ✅**

### Als Annahme / Schätzung gekennzeichnete Zahlen, die nicht aus einer Quelle stammen

1. **70 %** als Startwert für die Go-Schwelle in L1 (Anteil der Prospects mit zwei belegten Signalen und korrektem Rollen-Check), *Annahme*.
2. **70 %** als Startwert für die Nutzungsquote in L2, *Annahme*.
3. **Gewichte ×3 / ×1 / ×0** in den Gewichtungen G2, G3 und G4 (A.3), als *Annahme* („gesetzte Perspektiven“) markiert.
4. **Punkteskala 2 / 1 / 0** (● / ◐ / ○) in A.2, gekennzeichnet als „begründetes Urteil …, keine Messung“.

Diese Zahlen sind an eine Quelle *angelehnt*, werden aber in einer anderen Bedeutung als *Annahme* verwendet (zur Vollständigkeit):

5. **7 Tage** Zeitfenster Themen-Signale (B7), angelehnt an Green: „in the last week“.
6. **6 Monate** Zeitfenster Führungswechsel (B7), angelehnt an Chen: „less than 6 months“. Chen meint damit die *Betriebszugehörigkeit* der Person, nicht das Alter eines Signals.
7. **Dossier-Ablaufdatum = kürzestes Zeitfenster der Signale** (B12), Regel als *Annahme*; die Obergrenze ist ein `[Platzhalter]`.

---

## C5 Problem ist breit belegt

Im Abschnitt *Problem* stehen wörtliche Zitate von Thorne, O'Neil, Ross, Green, Chen, Petit, Jenkins, Blunt und Baker (9 Personen). Alle Stichproben stimmen wörtlich mit `input/` überein, und das Skript meldet 75 belegte Zitate und 0 nicht belegte. Budgetverantwortung: Blunt sagt ausdrücklich „We spend serious budget—my budget“ (Interview_Gen_05) und ist mit zwei wörtlichen Zitaten im Problem vertreten. Thorne (VP of Sales) ist zusätzlich als Verantwortlicher gegenüber dem Board belegt. **✅**

## C6 Wahl ist begründet und robust

- Beide Bedürfnisse sind auf 8 benannten Faktoren bewertet (A.2), jede Zelle hat eine Begründung. ✅
- Es gibt 3 alternative Gewichtungen neben G1 (G2, G3, G4). Alle sind durchgerechnet und richtig, das Ergebnis ist benannt (3× B1 vorn, 1× Gleichstand). ✅
- Schicksal des Verlierers: Der Rollen-Check aus Bedürfnis 2 wird ein MVP-Baustein, der volle CRM-Abgleich ein eigenes Folgeprojekt. Beides ist begründet (doppelter Umfang, eigener Käufer und eigenes Budget). Kippbedingungen stehen in A.5. ✅
- Kleiner Mangel: Die Zählung „5 von 10, davon einer nur teilweise“ (F1) lässt sich nicht nachvollziehen, weil die Namen fehlen. Für das Kriterium ist das nicht entscheidend. **✅**

## C7 Strategie nachgewiesen

- S1 Vision-Filter: „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ steht wörtlich in strategy.md, mit Begründung (Skill Prospect-Researcher, O'Neil-Zitat). ✅
- S2 Umsatz: „anything that brings in money and aligns with our vision, we do.“ und „Revenue is runway“ stehen wörtlich in strategy.md (dort fett gesetzt). Begründet mit drei Käufern unter Druck und dem gedeckelten Einstieg. ✅
- S3 Muster: „These patterns are the seeds of future products“ steht wörtlich, begründet mit den modularen Signal-Bausteinen und der Übergabe an das Pattern-Team. ✅
- Auch die übrigen Strategie- und Firmenzitate stehen wörtlich in den Quellen („We bill on a time-and-material basis.“, „Every agent is built custom for the client“, „Identify bottlenecks“, „We are not currently building AI agents as products, only as custom software solutions.“, „2 of our 14 people“). **✅**

## C8 Alternativen ernsthaft

A und B sind Alternativen auf der Ebene der Probleme (welches Bedürfnis). Echte Lösungsalternativen sind C (mehr Lizenzen), D (Schulung/Checklisten), E (mehr Druck auf das Call-Volumen) und F (automatischer Versand). Jede hat einen Ausschlussgrund mit Stütze:
- C: Chen hat Sales Navigator und braucht trotzdem 4 Std. Dazu: Einkauf ist keine Agent-Arbeit.
- D: O'Neil macht das schon und will Research aus der Einarbeitung heraushaben.
- E: Thorne „keep yelling at them to make more calls“ und Blunt zur Conversion.
- F: Petit „read between the lines“.

**✅**

## C9 Narrativ ist echt

Die Vorher-Spalte habe ich gegen `input/` geprüft:
- 15–40 Min. und viele Tabs: Thorne, O'Neil, Ross („five different tabs“), Petit („fifty tabs“). ✅
- „second shift“: Chen. ✅
- Etwa 20 statt 50 Calls: Jenkins (eine Person, als solche benannt). ✅
- 5 von 100: Blunt. ✅
- Rollen-Prüfung, 40 %: Jenkins. ✅
- „Research ist der größte Lehrinhalt“: O'Neil nennt Recherche das Schwerste beim Einarbeiten, sinngemäß. ✅
- „black box“: Thorne. ✅

Die Nachher-Spalte ist ausdrücklich als *Zielbild, illustrativ* markiert, das Beispiel-Dossier als *illustrativ, erfundene Person und Firma*. Die Szenen im Problem-Abschnitt stimmen mit den Interviews überein: Baker und der Artikel, Green und die Antwort, Jenkins und die Bounces. **✅**

## C10 Ziele messbar

- Z1–Z6 haben je Kennzahl, Ausgangswert (aus dem Interview und/oder `[Platzhalter: messen in Woche 1]`) und Messzeitpunkt. ✅
- Z7 hat als Ausgangswert `[Platzhalter: erste Stichprobe in Phase 1]`, also einen Messplatzhalter mit festem Zeitpunkt vor dem Pilot. Das weicht vom Wortlaut ab, erfüllt aber den Sinn; ich werte es als erfüllt. ✅
- N1–N3 haben Ausgangswert 0, Kennzahl und Messzeitpunkt. ✅
- Leitplanke: Z5 (Antwortquote halten), mit Konsequenz (kein Ausrollen). ✅

**✅**

## C11 Abgrenzung klar

Alle sechs Nicht-Ziele haben eine Spalte *Warum nicht* und eine Spalte *Wohin*:
- CRM-Abgleich: anderer Auftrag.
- Automatischer Versand: nie in diesem Projekt bzw. eigener Auftrag.
- Konflikt Marketing ↔ Sales, Lizenzbeschaffung und Vertriebsstrategie: bleiben beim Kunden, also *nie bei uns*.
- Produkt: Pattern-Team, eigene Entscheidung.

**✅**

## C13 Einwände beantwortet (Einwände aus `B-r2-kunde.md`)

**Einwand 1: „Ihr messt euch an Meetings, nehmt aber kein Risiko darauf.“** Der Kunde zahlt Phase 0, Phase 1 und den Pilot und trägt das Risiko allein.
- Der PRD antwortet nur teilweise. Der Einstieg ist gedeckelt (Obergrenze `[Platzhalter: Personentage]`), es gibt ein Go/No-Go vor dem Pilot und die stufenweise Beauftragung (Z. 26, 49, 316).
- Der Kern des Einwands bleibt offen: wer das Ergebnisrisiko trägt, also ob es eine erfolgsabhängige Komponente oder einen Risikoanteil von NeoEmployee gibt. Er ist weder beantwortet noch als offenes Risiko markiert. E3 („Tagessatz, Obergrenze, Wartungsanteil“) nennt keine Risikoteilung. R12 betrifft nur das Zahlungsrisiko von NeoEmployee.
- Zusätzlich widerspricht sich der PRD. Z. 24 sagt „Abgerechnet wird der Pilot an gebuchten Meetings und Antwortquote …“, Z. 33 sagt dagegen *Umsatz = Personentage × Tagessatz*, T&M. Genau diesen Widerspruch greift der Kunde auf. → **❌**

**Einwand 2: „Ohne LinkedIn ist das Ding wertlos, und genau das ist ungeklärt“**, dazu: Rechtsprüfung bezahlen, obwohl das Legal-Team des Kunden prüft.
- Als offenes Risiko markiert sind R1 (hoch/hoch), das No-Go-Kriterium in L1 und Offene Punkte Nr. 2. Als Gegenmaßnahme nennt der PRD, die Quellen breit zu streuen (Pressemitteilungen, Funding-Datenbanken, Karriereseiten). → im Kern beantwortet.
- Lücke: Der PRD sagt nicht, *wer* die rechtliche Prüfung macht und bezahlt, und ob das Legal-Team des Kunden sie übernehmen kann (das würde Phase 1 verbilligen). Er belegt auch nicht, welche Signale ohne LinkedIn übrig bleiben (Funding und Hiring wären über andere Quellen erreichbar, der Rollen-Check kaum). → **✅ mit Vorbehalt**

**Einwand 3: „Meine Leute arbeiten nicht im CRM-Datensatz, sondern in der Sequenz.“** Dazu: Der Pilot mit Vergleichsgruppe bindet das Team ein Quartal, und Fehlerquote, Tagessatz und Laufzeit sind Platzhalter.
- Ablage: Der zweite Kanal ist als offener Punkt markiert (B11, Z. 205, Offene Punkte Nr. 3). Die Nutzung wird über L2/B15 gemessen. Das *Sequenz-Tool* wird aber nirgends genannt, als Optionen stehen nur „Chat oder E-Mail“. Die Kurzfassung (Z. 14) nennt die CRM-Ablage als feste Tatsache, ohne Hinweis, dass der Kanal offen ist.
- Platzhalter: Sie sind als offene Punkte markiert (Nr. 4, 5, E3, „vor dem Angebotstermin“). → beantwortet als offen.
- Belastung des Kundenteams durch den Pilot: Laufzeit, Aufwand für Pilot- und Vergleichsgruppe und Messaufwand beim Kunden stehen weder als Risiko noch als offener Punkt im PRD. → nicht beantwortet.
- Gesamt: **❌** (zur Hälfte beantwortet; das Sequenz-Tool und die Pilotlast fehlen)

**C13 gesamt: ❌**, weil Einwand 1 nicht beantwortet ist und Einwand 3 nur teilweise.

---

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 Keine erfundenen Zahlen | ✅ | Alle 35 Skripttreffer sind Bezeichner, Zählungen oder richtig nachgerechnete Summen; die Stichproben stehen wörtlich in `input/`/`context/`, nicht belegte Werte sind *Annahme* oder `[Platzhalter]`. | Nichts zwingend; Empfehlung: bei „9 von 10“ / „5 von 10, davon einer nur teilweise“ die Personen nennen. |
| C5 Problem breit belegt | ✅ | Wörtliche Zitate von 9 Personen im Problem-Abschnitt, darunter Blunt mit nachweislicher Budgetverantwortung („my budget“). | — |
| C6 Wahl begründet und robust | ✅ | 8 Faktoren mit Begründung je Zelle, 3 alternative Gewichtungen richtig durchgerechnet, Ergebnis benannt, Bedürfnis 2 hat ein ausdrückliches Schicksal (Rollen-Check als MVP-Baustein, CRM-Abgleich als Folgeprojekt). | — |
| C7 Strategie nachgewiesen | ✅ | S1, S2 und S3 sind je mit einem wörtlichen Satz aus strategy.md in „…“ und einer Begründung belegt. | — |
| C8 Alternativen ernsthaft | ✅ | Vier echte Lösungsalternativen (C–F), jede mit einem Ausschlussgrund aus Interview oder Strategie. | — |
| C9 Narrativ echt | ✅ | Jede Vorher-Situation steht so oder sinngemäß in einem Interview; Nachher und Beispiel-Dossier sind als *illustrativ* markiert. | — |
| C10 Ziele messbar | ✅ | Jedes Ziel hat Kennzahl, Ausgangswert (Interview oder Messplatzhalter) und Messzeitpunkt; Z5 ist die Leitplanke. | Z7 nutzt `[Platzhalter: erste Stichprobe in Phase 1]` statt des Formats „messen in Woche 1“ (inhaltlich ausreichend). |
| C11 Abgrenzung klar | ✅ | Alle sechs Nicht-Ziele nennen einen Grund und ein Ziel (Folgeauftrag, nie, beim Kunden, Pattern-Team). | — |
| C13 Einwände beantwortet | ❌ | Einwand 2 ist als offenes Risiko beantwortet, aber Einwand 1 (Risikoteilung bei T&M) gar nicht und Einwand 3 (Sequenz statt CRM, Pilotlast beim Kunden) nur teilweise. | (1) Aussage zur Risikoteilung oder Erfolgskomponente, alternativ ein offenes Risiko „Kunde trägt das Ergebnisrisiko allein“; Widerspruch Z. 24 („abgerechnet … an gebuchten Meetings“) gegen T&M in Z. 33 auflösen. (2) Sagen, wer die Rechtsprüfung macht und bezahlt (Legal des Kunden?). (3) Sequenz-Tool als Ausgabekanal nennen; Kurzfassung Z. 14 nicht als fest formulieren; Pilotlast beim Kunden (Laufzeit, Vergleichsgruppe, Messaufwand) als Risiko oder offenen Punkt aufnehmen. |
