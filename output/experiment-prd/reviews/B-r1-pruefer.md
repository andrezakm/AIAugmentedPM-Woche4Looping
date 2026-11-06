# Review B, Runde 1: Faktenprüfer

Geprüft: `output/experiment-prd/B-PRD.md` gegen `.claude/skills/prd-goal/criteria.md`, Kriterien C3, C5, C6, C7, C8, C9, C10, C11, C13.
Gelesen: PRD, criteria.md, `input/` (alle 10 Interviews), `context/strategy.md`, `context/company.md`, `reviews/B-r1-skript.txt`, `reviews/B-r1-kunde.md`. Sonst nichts aus `output/`.

## C3 Keine erfundenen Zahlen

**Skriptliste (4 Treffer):**

| Zeile | Zahl | Entscheidung |
|---|---|---|
| Z.277 | 7 | zulässig: Bezeichner „F7“, keine Datenaussage |
| Z.278 | 8 | zulässig: Bezeichner „F8“ |
| Z.280 | 7 | zulässig: Verweis auf F7 |
| Z.280 | 8 | zulässig: Verweis auf F8 |

**Stichproben weiterer Zahlen, in `input/`/`context/` nachgeschlagen:**
- 15 Min./4 pro Stunde (Thorne, Interview 08) ✔; 20 Min. (Ross, 02) ✔; 30 Min. (Green, 07) ✔; 4 Std./10 Kontakte (Chen, 03) ✔; 40 Min. (O'Neil, 10) ✔; 50/20 Calls (Jenkins, 01) ✔; 5 von 100 (Blunt, 05) ✔; „like 40%“ (Jenkins, 01) ✔; $80k, 2 hours a day, 90 % LinkedIn (Kim, 06) ✔; „under two minutes“, „9 times out of 10“ (O'Neil, 10) ✔; „A dozen“ (Ross, 02) ✔; 2 Pattern-Leute (strategy.md: „2 of our 14 people“) ✔.
- „9 von 10“ / „5 von 10“: Zählungen über die Befragten, nicht wörtlich in `input/`. Für Bedürfnis 1 nachvollziehbar (alle außer Kim). Für Bedürfnis 2 aus `input/` allein nicht eindeutig nachzählbar, aber als Zählung aus den Quellen zulässig.
- „sechs Faktoren“ im Haupttext gegenüber acht Faktoren in Anhang A: keine erfundene Zahl, aber eine Unstimmigkeit (siehe C6).
- Hinweis: Die 40 % sind korrekt zitiert, im Vorher/Nachher und bei Z4 aber falsch eingeordnet (siehe C9).

Ergebnis: ✅. Keine erfundene Zahl gefunden.

## C5 Problem ist breit belegt

Wörtliche Zitate im Problem-Abschnitt von Thorne, O'Neil, Ross, Green, Chen, Petit, Jenkins, Blunt und Baker, also 9 Personen. Mit Budgetverantwortung: Blunt sagt ausdrücklich „my budget“ (Interview 05), Thorne (VP of Sales) und Ross (Sales Director) haben Führungsverantwortung. ✅

## C6 Wahl ist begründet und robust

- ≥5 benannte Kriterien: ✔ (F1–F8 in Anhang A.2)
- Jede Bewertung begründet: ✔
- **≥3 alternative Gewichtungen durchgerechnet, Ergebnis benannt: ✘.** Es gibt keine Gewichtung und keine Sensitivitätsrechnung. A.4 nennt nur Bedingungen, unter denen die Wahl kippt.
- Schicksal des Verlierers: ✔ (Rollen-Check als MVP-Baustein, CRM-Abgleich als Folgeprojekt, Umkehrbedingung)
- Zusätzlich: Der Haupttext spricht von „sechs Faktoren“ und „fünf von sechs vorn“, Anhang A.2 hat acht. Dass F8 für Bedürfnis 2 spricht, steht nur im Anhang.

Ergebnis: ❌

## C7 Strategie nachgewiesen

In `context/strategy.md` nachgeschlagen:
- S1 Vision-Filter: „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ ✔ wörtlich, mit Begründung (Prospect-Researcher)
- S2 Umsatz: „anything that brings in money and aligns with our vision, we do.“ und „Revenue is runway“ ✔ wörtlich (im Original fett), mit Begründung
- S3 Muster: „These patterns are the seeds of future products“ ✔ wörtlich, mit Begründung

Die Zeilen zu Geschäftsmodell und Prozess zitieren `context/company.md`. Das ist zulässig, gehört aber nicht zu S1–S3. ✅

## C8 Alternativen ernsthaft

A und B sind Problemalternativen (welches Bedürfnis zuerst). Lösungsalternativen sind C (mehr Lizenzen), D (Schulung/Checklisten), E (mehr Druck auf Volumen) und F (automatischer Versand). Sie haben folgende Ausschlussgründe:
- C: Jenkins (ZoomInfo-Login belegt, sie googelt trotzdem) und Chen (zahlt Sales Navigator selbst, recherchiert trotzdem 4 Std.) stützen *Rohdaten statt Synthese*.
- D: O'Neil will Training für Verkaufen statt Suchen nutzen (Interview 10) ✔
- E: Thorne „keep yelling“ und Blunt „conversion is higher“ ✔
- F: Petit „read between the lines“, Chen ✔

Ergebnis: ✅

## C9 Narrativ ist echt

- **„Veraltete Kontakte: etwa 40 % laut Jenkins, auffällig erst beim Anruf“ ist falsch.** Laut Interview 01 stellt Jenkins das *vor* dem Anruf fest, beim manuellen LinkedIn-Check: „to see if the person is actually still employed there. If they aren’t, which is like 40% of the time“. Die Szene „erst beim Anruf“ gibt es nur anekdotisch („I call and they’re like "Who?"“), nicht mit 40 %. Derselbe Fehler steckt in Z4.
- „Calls pro SDR: etwa 20 bei KPI 50“: Die Szene ist echt. Jenkins nennt als Ursache aber das Copy-Pasten von Jobtiteln ins Salesforce, also Bedürfnis 2, nicht die Signal-Recherche.
- Die Nachher-Spalte ist durchgehend eine Zielvorstellung (z. B. „Jeder Lead, der bearbeitet wird, bekommt ein Dossier“, „Einarbeitung kann sich auf Gesprächsführung konzentrieren“). Das kommt so in keinem Interview vor und ist nicht als *illustrativ* markiert.
- Echt sind: „second shift“ (Chen), 5 von 100 (Blunt), „black box“ (Thorne), Tabs/15–40 Min., Research als Lehrinhalt (O'Neil sinngemäß).

Ergebnis: ❌

## C10 Ziele messbar

- Z1–Z4: Kennzahl ✔, Ausgangswert aus Interview ✔ (bei Z4 inhaltlich falsch eingeordnet, siehe C9)
- Z5 (Leitplanke): Ausgangswert „nicht erhoben / im Pilot messen“, nicht in der Form `[Platzhalter: messen in Woche 1]`. Inhaltlich gerade noch akzeptabel.
- **Messzeitpunkt:** Pro Ziel gibt es keinen, nur pauschal „vor und nach dem Pilot“, und die Pilotdauer ist `[Platzhalter]`. ✘
- **N1–N3:** Kennzahl und Ausgangswert fehlen (N1 „abschließen“, N2 „Entscheidung beim Kunden“, N3 „bei Projektende“). ✘
- Guardrail vorhanden (Z5). ✔

Ergebnis: ❌

## C11 Abgrenzung klar

| Nicht-Ziel | Warum | Wohin |
|---|---|---|
| CRM-Abgleich | ✔ nur Dossier-Prospects | ✔ Folgeprojekt Sales Ops |
| Kein automatischer Versand | ◐ nur wiederholt („bleibt beim Menschen“) | ✘ fehlt (nie?) |
| Konflikt Marketing ↔ Sales | ✔ Organisationsfrage | ✘ fehlt |
| Keine Lizenzbeschaffung | ✘ fehlt | ✘ fehlt |
| Kein Produkt | ✔ | ✔ Pattern-Team |
| Keine Vertriebsstrategie-Beratung | ✔ Kunde entscheidet | ✘ fehlt |

Ergebnis: ❌

## C13 Einwände beantwortet

1. *Pipeline statt Recherchezeit:* Beantwortet über die Wirkungskette mit L4/L5 als offen markierten Annahmen („Nicht in unserem Projekt messbar“), Z5 mit Vergleichsgruppe und Z2. Schwäche: Es gibt kein Ziel für *mehr* Meetings, Z5 soll die Quote nur halten. ✔ als offenes Risiko
2. *Gibt es schon (Navigator, ZoomInfo), offenes T&M:* F4 und Alternative C (Rohdaten statt Synthese). Durch Jenkins und Chen in `input/` gedeckt, im PRD an dieser Stelle aber ohne Zitat. Budget, Laufzeit und Preis sind als offen markiert (Offene Punkte 5, `[Platzhalter]`). ✔
3. *Falsches Dossier verbrennt den Account, wer pflegt das?* R2 (Quellenlink, Stichproben), Rollen-Check gegen veraltete Daten, R9 (Wartung im Angebot, `[Platzhalter]`). Es gibt keine Qualitätsschwelle bzw. kein Abnahmekriterium für die Fehlerquote. ✔ als offenes Risiko

Ergebnis: ✅, knapp

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 | ✅ | Die 4 Skript-Treffer sind Faktor-Bezeichner (F7/F8), alle Stichproben-Zahlen stehen in `input/`/`context/` oder sind Zählungen daraus. | — (Hinweis: 40 % in Z4/Vorher falsch eingeordnet, siehe C9) |
| C5 | ✅ | Zitate von 9 Personen belegen das Problem, darunter Blunt („my budget“) sowie VP und Director Sales. | — |
| C6 | ❌ | 8 Faktoren sind bewertet und begründet, der Verlierer hat ein Schicksal, aber es gibt keine einzige alternative Gewichtung. | Mindestens 3 durchgerechnete Gewichtungen mit benanntem Ergebnis. Haupttext („sechs Faktoren“, „fünf von sechs“) an Anhang A.2 (acht Faktoren, F8 für Bedürfnis 2) angleichen. |
| C7 | ✅ | S1, S2 und S3 sind je wörtlich aus `strategy.md` zitiert und begründet. | — |
| C8 | ✅ | Vier Lösungsalternativen (C–F), jede mit einem Ausschlussgrund aus Interview oder Strategie. | — |
| C9 | ❌ | „40 % … auffällig erst beim Anruf“ widerspricht Interview 01 (Jenkins prüft vorher auf LinkedIn), und die Nachher-Szenen sind nicht als illustrativ markiert. | Zeile „Veraltete Kontakte“ und Z4 korrigieren (40 % = beim Vorab-Check nicht mehr im Unternehmen). Nachher-Spalte als *illustrativ*/Zielbild kennzeichnen. Optional: Jenkins' Ursache für 20 statt 50 Calls korrekt benennen (Copy-Paste ins CRM). |
| C10 | ❌ | Die Kundenziele haben Kennzahl und Ausgangswert, aber keinen Messzeitpunkt, und N1–N3 haben weder Kennzahl noch Ausgangswert. | Messzeitpunkt je Ziel (z. B. Woche 1 Baseline, Ende Pilot). Z5 als `[Platzhalter: messen in Woche 1]`. N1–N3 mit Kennzahl und Ausgangswert oder aus den Zielen herausnehmen. |
| C11 | ❌ | Nur 2 von 6 Nicht-Zielen sagen Warum und Wohin. | „Wohin“ (Phase 2/anderer Auftrag/nie) für Versand, Marketing↔Sales, Lizenzen, Beratung ergänzen, dazu „Warum“ für Lizenzbeschaffung (und ein echtes Warum für Versand). |
| C13 | ✅ | Alle drei Kundeneinwände sind beantwortet: Pipeline über L4/L5 als offene Annahmen, Bestandstools über F4/Alt. C plus offene Kaufmännik, Qualität und Wartung über R2/R9. | Knapp: Es fehlt ein Ziel für mehr Meetings (Z5 nur „halten“) und eine Qualitätsschwelle für Dossiers. Zu Einwand 2 fehlt im PRD-Text das Zitat (Jenkins/Chen). |
