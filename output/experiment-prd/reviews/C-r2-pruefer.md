# Review C, Runde 2: Faktenprüfer

Geprüft: `output/experiment-prd/C-PRD.md` gegen `.claude/skills/prd-goal/criteria.md`, Kriterien C3, C5, C6, C7, C8, C9, C10, C11, C13.
Gelesen: PRD, criteria.md, alle zehn Interviews in `input/`, `context/strategy.md`, `context/company.md`, `reviews/C-r2-skript.txt`, `reviews/C-r2-kunde.md`. Keine anderen Dateien in `output/`, also auch nicht die Synthese.

---

## C3 Keine erfundenen Zahlen

### Skriptliste (34 Treffer), Entscheidung je Zahl

| Zeile | Zahl(en) | Entscheidung | Grund |
|---|---|---|---|
| 29 | 8 | zulässig | Verweis-Label O8 |
| 61 | 95 | zulässig | berechnet: 100 − 5 aus Blunt ("They can't do that for 100 leads a day. So they do it for 5") |
| 211 | 8 | zulässig | Regel-Label L8 |
| 242 | 7 | zulässig | Regel-Label L7 |
| 251 | 8 | zulässig | Verweis-Label O8 |
| 252 | 8 | zulässig | Verweis-Label O8 |
| 267 | 7 | zulässig | Label O7 |
| 268 | 8 | zulässig | Label O8 |
| 294 | 7, 4,29, 24, 3,43 | zulässig | berechnet aus den Punkten (B1 Summe 30, B2 Summe 24) und Gewichten; nachgerechnet: 30/7 = 4,286, 24/7 = 3,429 ✓ |
| 295 | 53, 4,42, 44, 3,67 | zulässig | nachgerechnet: B1 = 53, B2 = 44, /12 ✓ |
| 296 | 11, 47, 4,27, 35, 3,18 | zulässig | nachgerechnet: B1 = 10+5+4+8+5+12+3 = 47, B2 = 6+4+4+4+4+9+4 = 35, /11 ✓ |
| 297 | 4,00, 34, 3,40 | zulässig | nachgerechnet: B1 = 40, B2 = 34, /10 ✓ |
| 298 | 39, 3,90, 37, 3,70 | zulässig | nachgerechnet: B1 = 0+5+12+4+5+4+9 = 39, B2 = 0+4+12+2+4+3+12 = 37 ✓ |
| 302 | 35, 35 | zulässig | nachgerechnet, Gewichte 0-1-3-0-1-1-3: B1 = 35, B2 = 35 ✓ |

Grundlage aller Anhang-Zahlen: Punkte als *eigene Bewertung des Autors* gekennzeichnet, Gewichte als *Annahmen* gekennzeichnet (Z. 274). Rechnungen stimmen alle.

### Stichproben außerhalb der Skriptliste

| Zahl im PRD | Fundstelle | Ergebnis |
|---|---|---|
| 15 Min., 4 pro Stunde | Thorne (Gen_08) | ✓ |
| 30 Min. für eine E-Mail | Green (Gen_07) | ✓ |
| 40 Min. ("forty minutes") | O'Neil (Gen_10) | ✓ |
| 20 statt 50 Calls | Jenkins (Gen_01) | ✓ |
| 4 Std. für 10 Personen | Chen (Gen_03) | ✓ |
| 80 % / 20 % | Petit (Gen_09) | ✓ |
| 5 Tabs | Ross (Gen_02) | ✓ |
| 40 % | Jenkins, als Einzelschätzung gekennzeichnet | ✓ |
| 6 Monate | Chen | ✓ |
| 90 % LinkedIn | Kim (Gen_06) | ✓ |
| 2 Std. pro Tag, 80k $ | Kim | ✓ |
| drei Signale | O'Neil ("those three specific things") | ✓ |
| 14 Leute, Pattern-Team 2 | strategy.md ("2 of our 14 people") | ✓ |
| 8 bis 12 Personenwochen | berechnet aus 2 × 4–6 Wochen, als *Schätzung* gekennzeichnet | ✓ |
| 9 von 10 / 5 von 10 | „laut Synthese" (nicht von mir lesbar). Nachgezählt in `input/`: Bedürfnis 1 bei allen außer Kim = 9 ✓. Bedürfnis 2: Jenkins, Baker, Kim, Chen (E-Mails) klar belegt, fünfte Person nur schwach (Thorne "every data point verified"). Zulässig, weil Zählung aus Quelle und offen als Synthese-Zahl ausgewiesen. | ✓ mit Hinweis |

Ergebnis C3: keine unzulässige Zahl gefunden. **✅**

### Als Schätzung/Annahme gekennzeichnete Zahlen ohne Quelle

1. Spike: 1 Person × 1 Woche (*Schätzung*, Kurzfassung und Plan Phase 0)
2. MVP: 2 Personen × 4 bis 6 Wochen = 8 bis 12 Personenwochen (*Schätzung*)
3. Pilotbegleitung: 1 Person in Teilzeit (*Schätzung*)
4. Daraus abgeleitet: „bindet 2 unserer 14 Leute" (14 aus der Quelle, die 2 aus der Schätzung)
5. Z1-Zielwert: unter 2 Minuten (*Annahme*, angelehnt an O'Neils "under two minutes", als Zielwert aber nicht aus der Quelle)
6. L3: Schwelle Neueinstellungen ≥ 3 Stellen (*Annahme*)
7. L4: Aktualitätsfenster 90 Tage (*Annahme*)
8. L11: Laufzeitziel unter 2 Minuten (*Annahme*)
9. L11: Zeitüberschreitung nach 10 Minuten (*Annahme*)
10. Anhang A: alle 14 Punktwerte 1–5 (*eigene Bewertung des Autors*)
11. Anhang A: Gewichte G-a bis G-e und Kipppunkt-Gewichtung 0-1-3-0-1-1-3 (*Annahmen*)

Nicht gekennzeichnet, aber eine Design-Festlegung und keine Behauptung: L11 „ein automatischer zweiter Versuch" (also 1 Wiederholung). Die Tage und Monate in den Testfällen von L4 (30, 90, 200 Tage, 5/7 Monate) sind Testeingaben, keine Behauptungen.

---

## C5 Problem ist breit belegt

Alle neun Zitate der Belegtabelle Zeichen für Zeichen in `input/` nachgeschlagen: Thorne, Blunt, O'Neil, Ross, Jenkins, Green, Chen, Petit, Baker, jeweils richtig zugeordnet. Budgetverantwortung: Blunt, wörtlich "We spend serious budget—my budget—getting these people into the funnel" (Gen_05). Thorne mit Board-Bezug ("I had a meeting with the board this morning") ✓. Mindestens 4 Personen, mindestens eine mit Budget. **✅**

Hinweis: Jenkins' "fishing without bait" bezieht sich auf das Durchscrollen des Feeds nach Jobwechseln. Das ist eher ein Signal (B1) als Datenpflege, also passt es.

## C6 Wahl ist begründet und robust

- Beide Bedürfnisse auf 7 benannten Kriterien bewertet, jede Zelle hat eine Begründung ✓
- 5 Gewichtungen durchgerechnet, Rechnungen stimmen, Ergebnis benannt („B1 gewinnt in allen fünf") ✓, Kipppunkt ausgewiesen ✓
- Schicksal des Verlierers ausdrücklich: MVP-Baustein (Status-Check) plus Rest Phase 2, mit Grund ✓

**✅**, mit inhaltlichem Hinweis: Zwei Belege für B1 gehören in der Quelle eher zu B2.
(a) K2/Kurzfassung „20 statt 50 Calls": Jenkins nennt als Ursache "because I’m stuck copy-pasting job titles from LinkedIn profiles into Salesforce fields", also Datenpflege.
(b) K5/Wahl Punkt 2 Chen "I'd double my numbers": Chen wünscht sich dafür eine *Liste* "New CTOs at Series B companies" *mit E-Mails*. Listenbau und E-Mail-Suche schließt der PRD aber als Nicht-Ziel aus.
Senkt man B1 bei K2 und K5 deshalb je um einen Punkt, steht G-e 37 : 37. Dann stimmt „gewinnt in allen fünf" nicht mehr. Formal ist das Kriterium erfüllt, die Robustheit hängt aber an diesen beiden Zuordnungen.

## C7 Strategie nachgewiesen

S1, S2 und S3 wörtlich in `context/strategy.md` gefunden (Z. 25, Z. 24, Z. 19), dazu „Every engagement is scoped and billed individually." (Z. 11). Jede Zeile hat eine Begründung, S3 mit ehrlicher Einschränkung (nur eine Organisation). **✅**

## C8 Alternativen ernsthaft

Vier Lösungsalternativen (A1 Lizenzen, A2 Checklisten/Training, A3 Vollautomat-Outreach, A4 Anreicherung auf Vorrat), keine davon eine Problemalternative. Jede hat einen Ausschlussgrund aus Interview und/oder Strategie. Die Zitate sind geprüft: O'Neil, Kim "break, or they’re too expensive to run on every single contact record", Ross "insist it's the only way to get a response", Green "It feels a bit fake, honestly." **✅**

## C9 Narrativ ist echt

Vorher-Szenen gegen `input/` geprüft:
1. Green, Sauerteig-Thread, Antwort, 30 Minuten (Gen_07) ✓
2. Jenkins, Salesforce auf einem Bildschirm, LinkedIn im Tab, prüft Anstellung, kopiert Titel, 20 statt 50 (Gen_01) ✓
3. O'Neil, Artikel → Autorenprofil → alte Fotos, "forty minutes" ohne Grund (Gen_10) ✓
4. Chen, 4 Stunden abends für 10 Kontakte, nach Feierabend ("after my kid goes to sleep") (Gen_03) ✓

Alle Nachher-Szenen sind als *illustrativ* markiert. **✅**

## C10 Ziele messbar

Z1–Z5 und N1–N3 haben je Kennzahl, Ausgangswert und Messzeitpunkt. Ausgangswerte stammen aus Interviews plus `[Platzhalter: messen in Woche 1]`, oder sind definitorisch (Z4 = 0, weil es die Bewertung heute nicht gibt; N2/N3 = nein). Guardrails G1–G3 sind vorhanden, G1 mit Abbruchregel. **✅**

Kleiner Hinweis: Die Ausgangswerte von Z4, G3 und N1–N3 sind weder Interviewwert noch „messen in Woche 1". Sie sind aber logisch zwingend bzw. ein Platzhalter, darum zulässig.

## C11 Abgrenzung klar

Jedes Nicht-Ziel nennt *warum nicht* und *wohin* ✓. **Aber:** Das Ziel „Phase 2" ist im selben Dokument doppelt belegt. Im *Plan* heißt Phase 2 „MVP bauen" (auch N3: „Ende Phase 2 (MVP)"). In Kurzfassung, Nicht-Zielen, Anhang A, R5, R12 und Plan Phase 4 („Angebot Phase 2") heißt „Phase 2" dagegen der Folgeauftrag mit Sales Ops. Dazu kommt die Kurzfassung mit „T&M-Umsatz über Phase 0 bis 3" *und* „Folgeauftrag Phase 2". Damit ist bei „Enterprise-Account-Mapping → Phase 2" oder „E-Mails verschicken → frühestens Phase 2" nicht eindeutig, ob das in den MVP-Bau oder in einen späteren Auftrag fällt. Im Zweifel ❌. **❌**

## C13 Einwände beantwortet

| Einwand des Kunden | Antwort im PRD | Urteil |
|---|---|---|
| 1. Ohne LinkedIn wertlos, Zugang ungeklärt; Phase 0 zahlt der Kunde fürs Herausfinden | R2 **offen**, O1, Go/No-Go am Ende Phase 0 vor dem MVP-Team (Kurzfassung Risiko 1, Plan Phase 0). Wer Phase 0 bezahlt, steht als offene Entscheidung O7 im PRD. | ✅ als offenes Risiko markiert |
| 2. Weniger Recherchezeit bringt nichts, Termine pro SDR müssen **Kernmetrik** sein; gleiche Aufhänger bei jedem Anbieter senken die Antwortquote | Z5 (Termine) existiert, R10 koppelt die Mindeststeigerung an Terminen an den Break-even, G1 und R1 schützen die Antwortquote. Die Kurzfassung führt Termine aber ausdrücklich als „Pilot misst **zusätzlich** Termine pro SDR (Z5)", die Weiter-Entscheidung läuft gleichrangig über Z1–Z5. Die Forderung *Kernmetrik* ist also weder angenommen noch begründet abgelehnt. Das Risiko *Zeitersparnis wird nicht zu Terminen* fehlt als offenes Risiko. Das Teilargument *alle Anbieter liefern dieselben Aufhänger* (Signal-Kommodifizierung) wird nicht behandelt; G1 misst nur die Folge. | ❌ teilweise |
| 3. T&M ohne Zahl nicht CFO-fähig; Datenpflege nicht noch mal extra kaufen, Agent ohne Phase 2 halb fertig | Teil 1: R10 **offen**, Budgetrahmen je Phase, Break-even-Formel, O3/O8 ✓. Teil 2: Funktional decken R5 (Status-Check im MVP) und R12 (**offen**, E-Mails bleiben falsch) das ab. Der kaufmännische Einwand *Phase 2 wirkt wie Doppelt-Bezahlen, MVP ohne Phase 2 halb fertig* fehlt aber: Der PRD führt Phase 2 nur als eigenes Umsatzziel (N2), nicht als Risiko für die Annahme des Angebots. | ❌ teilweise |

**❌**

---

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 | ✅ | Alle 34 Skript-Treffer sind Labels oder nachgerechnete Ergebnisse aus gekennzeichneten Bewertungen; die Stichproben stimmen mit `input/`/`context/` überein, alle quellenlosen Zahlen sind als Schätzung/Annahme markiert. | – (optional: L11 „zweiter Versuch" als Festlegung markieren) |
| C5 | ✅ | Neun wörtlich geprüfte Zitate von neun Personen, Blunt mit ausdrücklich eigenem Budget. | – |
| C6 | ✅ | 2 Bedürfnisse × 7 begründete Kriterien, 5 korrekt gerechnete Gewichtungen plus Kipppunkt, Verlierer hat ein Schicksal mit Grund. | Formal nichts. Inhaltlich: „20 statt 50 Calls" (Jenkins, Ursache Titel-Kopieren) und Chens "double my numbers" (Liste mit E-Mails) sind eher B2-Belege; korrigiert stünde G-e 37 : 37. |
| C7 | ✅ | S1, S2, S3 je mit wörtlichem Satz aus strategy.md und Begründung. | – |
| C8 | ✅ | Vier echte Lösungsalternativen, jede mit Ausschlussgrund aus Interview und Strategie, Zitate geprüft. | – |
| C9 | ✅ | Alle vier Vorher-Szenen stehen so in Green, Jenkins, O'Neil und Chen; alle Nachher-Szenen sind *illustrativ* markiert. | – |
| C10 | ✅ | Jedes Ziel hat Kennzahl, Ausgangswert (Interview, Platzhalter oder definitorisch) und Messzeitpunkt, dazu drei Guardrails. | – |
| C11 | ❌ | Jedes Nicht-Ziel hat Grund und Ziel, aber „Phase 2" heißt im Plan „MVP bauen" und sonst „Folgeauftrag mit Sales Ops", sodass *wohin* mehrdeutig ist. | Eindeutige Benennung, z. B. Folgeauftrag als „Folgeauftrag Datenpflege" oder „Phase 5", in Kurzfassung, Nicht-Zielen, R5, R12, N2, Plan Phase 4 und Anhang A angleichen. |
| C13 | ❌ | Einwand 1 ist als offenes Risiko beantwortet, Einwände 2 und 3 nur teilweise. | (2) Entscheidung, ob Termine pro SDR die primäre Erfolgskennzahl wird (oder begründet, warum nicht), dazu offenes Risiko *Zeitersparnis ≠ mehr Termine* und eine Antwort auf *gleiche Aufhänger bei allen Anbietern*. (3) Risiko bzw. Antwort auf *Phase 2 als Nachkauf, MVP ohne Datenpflege halb fertig* (z. B. was der MVP allein liefert, oder Datenpflege-Optionen im Angebot). |
