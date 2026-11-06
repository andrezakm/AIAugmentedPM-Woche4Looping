# Faktenprüfer: O-PRD.md (Runde 1)

Geprüft: `output/experiment-prd/O-PRD.md` gegen `criteria.md` (v2), `skeleton.md`, `input/`, `context/`, Skriptausgabe `O-r1-skript.txt`, Kunden-Einwände `O-r1-kunde.md`. Andere PRDs und Reviews nicht gelesen. Im Zweifel ❌.

## C1 Gerüst (inhaltliche Zuordnung, englische Vorlage)

| skeleton.md | im PRD | Status |
|---|---|---|
| Kurzfassung | „Product Summary“ (Z. 152–154, am Ende) | ✅ vorhanden, gefüllt |
| Problem | „Problem & Opportunity“ (Z. 12–28) | ✅ |
| Warum dieses Problem (Wahl und Strategie) | nur ein Bullet „Why it matters to NeoEmployee“ (Z. 17) und ein Halbsatz in Alternativen (Z. 38) | ❌ keine Wahl zwischen zwei Bedürfnissen, keine Strategie-Belege |
| Lösung | „High-Level Approach“, „Key Features“, „Key Flows“ | ✅ |
| Alternativen | „Alternatives considered“ (Z. 36–39) | ✅ |
| Vorher und nachher | „Narrative“ (Z. 41–45) | ✅ |
| Ziele | „Goals“ | ✅ |
| Nicht-Ziele | „Non-Goals“ | ✅ |
| Logik | „Key Logic“ | ✅ |
| Plan | „Development and Launch Planning“ + Checklist | ✅ |
| Risiken und Einwände | „Risks“ + „FAQ“ | ✅ (inhaltlich dünn, siehe C13) |
| Offene Punkte | fehlt (Operational Checklist ist eine To-do-Liste, keine offenen Fragen, kein Annahmen-Block) | ❌ |
| Anhang A: Bewertung der Bedürfnisse | fehlt („Appendix“ ist nur eine Linkliste) | ❌ |
| Loop-Protokoll | fehlt | ❌ |

**C1 ❌**

## C3 Keine erfundenen Zahlen

Belegt oder nachvollziehbar berechnet: 15 Min. (Thorne), 4 pro Stunde (Thorne), 40 Min. (O'Neil „forty minutes“), 50/20 Calls und Differenz 30 (Jenkins), 5 von 100 bzw. 95 (Blunt), 4 Stunden/10 Personen (Chen), 30 Min. (Green), „days“ (Petit), „five different tabs“ (Ross), 40 % veraltete Kontakte (Jenkins „like 40% of the time“), „under two minutes“ (O'Neil), „double“ (Jenkins, Chen), „9 of 10“ (nachzählbar: alle außer Kim).

Nicht belegt, nicht berechnet, kein Annahmen-Block (der Block „Annahmen (nicht belegt)“ existiert gar nicht):
- **„six weeks“ / Week 1–6** (Z. 34, 57, 102–111, 154): Aufwand/Dauer, nur als Annahme im Block zulässig.
- **„20 test prospects“** (Z. 105): erfunden.
- **„last 90 days“** (Z. 92): konkreter Startwert mit Platzhalter-Etikett vermischt; technischer Startwert gehört in den Annahmen-Block mit Begründung und Ersetzungszeitpunkt.
- **„5 of 10 interviewees“** für Kontaktdaten (Z. 38): aus `input/` klar nur Jenkins, Baker, Kim (Chen allenfalls über E-Mail-Suche); 5 nicht nachvollziehbar.
- **Narrativ:** 60 Leads, 8:30, „eight people“ bis Mittag, „half of them cold“, 40 unberührte Leads, 25 Calls, „three weeks ago“, „four DevOps roles“, „September“: erfunden und nicht als Annahme oder *illustrativ* gekennzeichnet.
- Formgrenzen „three signals / two sentences“ (Z. 93) sind Designvorgaben, ohne Begründung im Annahmen-Block.

Geldbeträge: keine. **C3 ❌**

## C5 Problem breit belegt

Alle Problem-Zitate in `input/` nachgeschlagen, wörtlich (bis auf Typografie ’/' und Kürzung „…“): Thorne, Ross, Blunt, O'Neil, Jenkins, Chen, Green, Petit, Baker = 9 Personen. Budgetverantwortung: Thorne (VP Sales, Board), Ross (Sales Director), Blunt („my budget“). **C5 ✅**

## C6 Wahl begründet und robust

Keine Bewertung der beiden Bedürfnisse auf ≥5 Kriterien, keine Begründungen je Bewertung, keine alternativen Gewichtungen, kein Anhang A. Nur das Schicksal des Verlierers (Kontaktdaten-Sync → Phase 2, Z. 38, 76) ist benannt. **C6 ❌**

## C7 Strategie nachgewiesen

Kein einziger wörtlicher Satz aus `context/strategy.md` in „…“. Z. 17 umschreibt Vision-Filter, T&M-Umsatz und Pattern-Team nur. **C7 ❌**

## C8 Alternativen ernsthaft

- „Buy more data licenses“: Lösungsalternative, Ausschluss gestützt auf O'Neil (Noise) und Kim („too expensive to run on every single contact record“). ✅
- „Train reps / research playbook“: Lösungsalternative, Ausschluss gestützt auf O'Neil („high-priced data miners“, will Signale „on a platter“ statt Recherche lehren). ✅
- „Full contact-data sync agent“: ist eine Problemalternative (anderes Bedürfnis), zählt nicht.

Zwei gültige Lösungsalternativen. **C8 ✅**

## C9 Narrativ echt

- Sinngemäß belegt: Tab-Springen zwischen Website, News, LinkedIn, Crunchbase (Ross, Jenkins); KPI 50, real ~20 Calls (Jenkins); schwacher Aufhänger (Green „a bit fake“); Chen 4 Stunden abends für 10 Personen.
- Nicht in Interviews, nicht als *illustrativ* markiert: 60-Leads-Liste, 8:30 Montag, „eight people by lunch“, „half of them cold and generic“, 40 unberührte Leads, Küchentisch, der gesamte Brief-Text („Series B closed three weeks ago … four DevOps roles“), 25 Calls bis Mittag, Jessica „bekommt ihre Liste“. Das Skript meldet den Brief-Text zusätzlich als NICHT BELEGTES Zitat.

**C9 ❌**

## C10 Ziele messbar

| Ziel | Kennzahl | Ausgangswert | Messzeitpunkt |
|---|---|---|---|
| 1 Recherchezeit | ✅ Min./Prospect | ✅ 15–40 Min. + Messung Woche 1 | ❌ nicht genannt |
| 2 Call-Volumen, Anteil personalisierter Leads | ✅ | ✅ 20 / 5 von 100 | ❌ nicht genannt (Ziel = Platzhalter, ok) |
| 3 „Reps feel they are selling“ | ❌ keine | ❌ | ❌ |
| 4 Guardrail Reply-/Meeting-Rate | ✅ | ❌ „today's baseline“ ohne Wert oder `[Platzhalter: messen in Woche 1]` | ❌ |

Guardrail vorhanden. **C10 ❌**

## C11 Abgrenzung klar

| Nicht-Ziel | Warum | Wohin |
|---|---|---|
| 1 keine E-Mails/Calls senden | ✅ | ❌ (nie? Phase 2? nicht gesagt) |
| 2 keine Kontaktverifikation | ✅ | ❌ im Nicht-Ziel nur „out of scope“; Phase 2 steht nur unter Future considerations |
| 3 kein Lead-Scoring | ✅ | ❌ „later phase, if at all“ ist kein Ziel |
| 4 kein Multi-Client-Produkt | ⚠️ implizit | ❌ „if the pattern repeats“ ist kein Ziel |

**C11 ❌**

## C13 Einwände beantwortet (Abgleich mit O-r1-kunde.md)

- **K1 „Gibt es schon (Sales Navigator, ZoomInfo, Apollo-Alerts); wo landet der Brief?“** Teilweise: Ablage im CRM-Datensatz (Feature 3, Risiko 2) und FAQ „raw data vs. synthesis“ mit O'Neil-Beleg. Nicht beantwortet: Vergleich mit vorhandenen Signal-Alerts plus Filter, Sequencing-Plattform, Gefahr „Tab Nummer sechs“ als Adoptionsrisiko. ❌
- **K2 „Vertrauen / ein falsches Signal verbrennt den Account; Pipeline statt Zeitersparnis“** Teilweise: Quelle und Datum je Signal, Konflikte werden gezeigt (Logik 3), Adoptionsrisiko 3, Guardrail „nicht schlechter“. Nicht beantwortet: falsches/halluziniertes Signal als Risiko, Wirkung der Nachprüfung auf die Zeitersparnis, ein Ziel für steigende Reply-Rate, Meetings oder Pipeline nach sechs Wochen; nicht als offenes Risiko markiert. ❌
- **K3 „T&M ohne Deckel; wir finanzieren euer Produkt; Code- und Datenrechte“** Gar nicht beantwortet, nicht als Risiko markiert. Die Kurzfassung (Z. 154) verstärkt den Einwand sogar („seed of a reusable NeoEmployee product“). ❌

**C13 ❌**

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C1 | ❌ | 11 von 14 Gerüst-Abschnitten sind inhaltlich vorhanden, drei fehlen ganz und „Wahl und Strategie“ ist nur ein Bullet. | Abschnitte „Offene Punkte“ (mit Annahmen-Block), „Anhang A: Bewertung der Bedürfnisse“, „Loop-Protokoll“; eigener Abschnitt „Warum dieses Problem (Wahl und Strategie)“ |
| C3 | ❌ | Mehrere Zahlen sind weder belegt noch berechnet, und es gibt keinen Annahmen-Block. | „six weeks“/Wochenplan, „20 test prospects“, „90 days“, „5 of 10“, Narrativ-Zahlen (60 Leads, 8 und 25 Calls, „three weeks“, „four DevOps roles“) → in Block „Annahmen (nicht belegt)“ mit Begründung und Ersetzungszeitpunkt, oder belegen, oder `[Platzhalter]` |
| C5 | ✅ | Neun Personen wörtlich zitiert, Zitate in `input/` verifiziert, darunter Thorne, Ross und Blunt mit Budgetverantwortung. | nichts |
| C6 | ❌ | Es gibt keine Bewertung der beiden Bedürfnisse, nur das Schicksal des Verlierers (Phase 2). | Bewertung beider Bedürfnisse auf ≥5 benannten Kriterien mit Begründung je Wert, ≥3 alternative Gewichtungen mit Ergebnis (Anhang A) |
| C7 | ❌ | Die Strategie wird nur umschrieben, kein Satz aus `strategy.md` steht wörtlich in „…“. | Je ein wörtliches Zitat aus `context/strategy.md` plus Begründung für S1 Vision-Filter, S2 Umsatz, S3 Muster |
| C8 | ✅ | Zwei echte Lösungsalternativen (Lizenzen kaufen, Reps schulen) mit Ausschlussgrund aus O'Neil und Kim. | nichts (die Kontaktdaten-Option ist eine Problemalternative und zählt nicht mit) |
| C9 | ❌ | Das Narrativ enthält viele erfundene Szenen und einen erfundenen Brief-Text, nichts davon ist als *illustrativ* markiert. | Kennzeichnung *illustrativ* für 60-Leads-Liste, Uhrzeiten, 8/25 Calls, Brief-Text „Series B … DevOps roles“, oder Ersetzen durch Szenen aus `input/` |
| C10 | ❌ | Kein Ziel hat einen Messzeitpunkt, Ziel 3 hat weder Kennzahl noch Ausgangswert, und der Guardrail hat keinen Ausgangswert. | Messzeitpunkt je Ziel; Kennzahl und Ausgangswert für Ziel 3; Guardrail-Ausgangswert als `[Platzhalter: messen in Woche 1]` |
| C11 | ❌ | Jedes Nicht-Ziel sagt warum, aber keines sagt eindeutig, wohin es geht. | Je Nicht-Ziel: Phase 2, anderer Auftrag oder nie (z. B. NZ1 „nie“, NZ2 „Phase 2“, NZ3/NZ4 eindeutig zuordnen) |
| C13 | ❌ | Von drei Kunden-Einwänden sind zwei nur teilweise und K3 gar nicht beantwortet, keiner davon ist als offenes Risiko markiert. | K1: Abgrenzung zu Signal-Alerts in Sales Navigator/ZoomInfo/Apollo, Sequencing-Integration; K2: Risiko falsches Signal, Ziel für Reply-Rate/Meetings/Pipeline; K3: Kostendeckel, Code- und Datenrechte, Wiederverwendung (als offenes Risiko oder `[Platzhalter]` zur Entscheidung) |
