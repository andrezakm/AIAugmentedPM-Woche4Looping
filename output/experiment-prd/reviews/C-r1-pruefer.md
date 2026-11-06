# Review C, Runde 1: Faktenprüfer

Geprüft: `output/experiment-prd/C-PRD.md` gegen `.claude/skills/prd-goal/criteria.md`
Gelesen: PRD, criteria.md, alle zehn Interviews in `input/`, `context/strategy.md`, `context/company.md`, `reviews/C-r1-skript.txt`, `reviews/C-r1-kunde.md`. Keine anderen Dateien in `output/`.
Kriterien: C3, C5, C6, C7, C8, C9, C10, C11, C13.

---

## C3 Keine erfundenen Zahlen: ✅

**Skriptliste (29 Treffer), Entscheidung je Zahl:**

| Zeile | Zahl(en) | Entscheidung | Grund |
|---|---|---|---|
| 44 | 95 | zulässig | berechnet: 100 − 5 aus Blunt ("So they do it for 5 and ignore the rest", "100 leads a day") |
| 179 | 8 | zulässig | Regelnummer L8, keine Zahlenbehauptung |
| 208 | 7 | zulässig | Verweis auf Regel L7 |
| 254 | 7, 7, 4,29, 24, 7, 3,43 | zulässig | Summe der Gewichte 7; B1 = 5+5+4+4+5+4+3 = 30, 30/7 = 4,29; B2 = 3+4+4+2+4+3+4 = 24, 24/7 = 3,43. Nachgerechnet, stimmt. |
| 255 | 53, 4,42, 44, 3,67 | zulässig | nachgerechnet: B1 53, B2 44, Gewichtssumme 12; 4,42 und 3,67 korrekt gerundet |
| 256 | 11, 47, 11, 4,27, 35, 11, 3,18 | zulässig | nachgerechnet: B1 = 10+5+4+8+5+12+3 = 47, B2 = 6+4+4+4+4+9+4 = 35, Summe 11 |
| 257 | 4,00, 34, 3,40 | zulässig | nachgerechnet: B1 = 40, B2 = 3+4+4+4+4+3+12 = 34, Summe 10 |
| 258 | 39, 3,90, 37, 3,70 | zulässig | nachgerechnet: B1 = 0+5+12+4+5+4+9 = 39, B2 = 0+4+12+2+4+3+12 = 37, Summe 10 |
| 262 | 35, 35 | zulässig | nachgerechnet mit 0-1-3-0-1-1-3: B1 = 35, B2 = 35 |

Die Punktwerte 1–5 sind als *eigene Bewertung des Autors* gekennzeichnet, die Gewichte als *Annahmen* (Z. 234). Damit alle Skript-Treffer zulässig.

**Stichprobe weiterer Zahlen:**

| Zahl | Fundstelle | Ergebnis |
|---|---|---|
| 15 Min., 4 pro Stunde | Thorne | ✅ |
| 30 Min. für eine E-Mail | Green | ✅ |
| 40 Min. ("forty minutes") | O'Neil | ✅ |
| 20 statt 50 Calls | Jenkins | ✅ |
| 4 Std. für 10 Personen | Chen | ✅ |
| 80 % / 20 % | Petit | ✅ |
| "like 40% of the time" | Jenkins | ✅ |
| 2 Std. pro Tag, 80k $ | Kim | ✅ |
| 90 % LinkedIn | Kim | ✅ |
| 6 Monate (neu in der Rolle) | Chen ("less than 6 months") | ✅ |
| drei Signale | O'Neil ("those three specific things") | ✅ |
| 90 Tage Aktualitätsfenster | als *Annahme* markiert | ✅ |
| unter zwei Minuten Laufzeit (L11) | als *Annahme* markiert | ✅ |
| 30 / 200 Tage | Testfall-Eingaben in L4, keine Behauptung | ✅ |
| "9 von 10" / "5 von 10" Interviews | als "laut Synthese" ausgewiesen, also nicht `input/`/`context/`. Nachgezählt in `input/`: 9 von 10 (alle außer Kim) ist haltbar; 5 von 10 (Jenkins, Baker, Kim, Chen, dazu Thorne oder Petit) ist Auslegung, aber vertretbar | ✅ mit Hinweis |

**Hinweis (kein ❌):** Kurzfassung Z. 14 sagt, die Enablement-Leitung formuliere "unter zwei Minuten" als Ziel. O'Neil stellt es als Frage zur Auffindbarkeit ("can you find it in under two minutes?"), nicht als Zielwert für Lesezeit. Zahl belegt, Zuschreibung leicht gedehnt.

## C5 Problem ist breit belegt: ✅

Tabelle Z. 70–80 zitiert neun verschiedene Personen wörtlich. Alle in `input/` gefunden. Budgetverantwortung: Blunt, "We spend serious budget—my budget—getting these people into the funnel" (Interview 05), wörtlich vorhanden. Thorne mit Board-Bezug zusätzlich. Bedingung (≥ 4 Personen, ≥ 1 mit Budget) klar erfüllt.

## C6 Wahl ist begründet und robust: ✅

- Beide Bedürfnisse auf 7 benannten Kriterien (K1–K7) bewertet, jede Zelle mit Begründung. Begründungen gegen `input/` geprüft (Kim zu ZoomInfo/Clearbit, Jenkins "double my quota", Chen "I'd double my numbers", Ross "starving"): stimmen.
- 5 Gewichtungen durchgerechnet, alle Rechnungen nachgerechnet und korrekt, Ergebnis je Zeile und gesamt benannt, Kipppunkt zusätzlich ausgewiesen.
- Schicksal des Verlierers ausdrücklich: MVP-Baustein (Status-Check) plus Phase 2, mit Grund (Z. 66, Z. 266).

Kleine Unschärfe: Z. 64 "Für Bedürfnis 1 zahlt der Kunde heute nur mit der Zeit seiner Leute". Chen bezahlt Sales Navigator selbst, ZoomInfo wird laut Jenkins auch zur Recherche genutzt. Die Aussage stimmt also nicht ganz, ändert aber nichts am Ergebnis.

## C7 Strategie nachgewiesen: ✅

| Prüfung | Satz im PRD | In `context/strategy.md` wörtlich? | Begründung vorhanden? |
|---|---|---|---|
| S1 | „we pursue any revenue-generating opportunity … We do not chase work outside that frame.“ | ja (Abschnitt Constraints, Vision filter) | ja |
| S2 | „every deal we close extends how long we can operate and invest in the product path.“ + „Every engagement is scoped and billed individually.“ | ja, beide | ja |
| S3 | „Their job is to identify recurring patterns — skills, workflows, and agent types that appear across multiple clients in different industries.“ | ja (per grep zeichengenau bestätigt) | ja, inklusive ehrlicher Einschränkung (nur ein Kunde) |

## C8 Alternativen ernsthaft: ✅

Vier Lösungsalternativen (A1 Lizenzen, A2 Checklisten/Training, A3 Vollautomatischer Outreach, A4 Vorrats-Anreicherung), alle Lösungs- und keine Problemalternativen. Jeder Ausschlussgrund stützt sich auf ein Interview (O'Neil, Kim, Ross, Green) und/oder die Strategie (S1/S2). Zitate geprüft: "The problem isn't that the data is missing", "break, or they’re too expensive to run on every single contact record", "insist it's the only way to get a response", "It feels a bit fake, honestly." sind wörtlich vorhanden und werden im richtigen Sinn verwendet.

## C9 Narrativ ist echt: ✅

Vorher-Szenen gegen `input/` geprüft:
- Green und Sauerteig-Thread, Antwort bekommen, "30 minutes for one email!": Interview 07 ✅
- Jenkins, Salesforce auf einem Bildschirm, LinkedIn im Tab, Beschäftigungsstatus prüfen, Titel kopieren, 20 statt 50: Interview 01 ✅
- O'Neil, Artikel → Autorenprofil → alte Fotos, "forty minutes", kein Grund zum Anrufen: Interview 10 ✅
- Chen, 4 Stunden nach Feierabend für 10 Kontakte: Interview 03 ✅

Alle Nachher-Szenen sind als *illustrativ* markiert. Die Bedingung aus „Erfüllt, wenn“ ist damit erfüllt.

**Hinweis für die Überarbeitung (Widerspruch im PRD, nicht C9-relevant):** Nachher-Szene 1 sagt "Nachfolger im CRM als neuer Kontakt angelegt". Nachfolger-Suche ist aber laut Z. 66 und Nicht-Ziele Phase 2, und L2(c) legt keinen Nachfolger an. Nachher-Szene 3 ("Liste neu ernannter Entscheider bei frisch finanzierten Firmen") beschreibt Listen-Erzeugung. Die Lösung erstellt aber nur Dossiers für bereits zugewiesene Kontakte (L1). Beide illustrativen Szenen versprechen also mehr als den MVP.

## C10 Ziele messbar: ❌

- Z1–Z4: Kennzahl ✅, Ausgangswert (Interview und/oder `[Platzhalter: messen in Woche 1]`, Z4 = 0 mit Grund) ✅, Messzeitpunkt ✅.
- Guardrails G1–G3 vorhanden ✅.
- **Aber:** Z. 148, im Abschnitt Ziele: "**Für NeoEmployee:** T&M-Umsatz aus Pilot und Ausbau `[Platzhalter: Volumen nach Angebot]`, plus ein wiederverwendbarer Signal-Baustein …". Das ist ein Ziel ohne Ausgangswert und ohne Messzeitpunkt, der Baustein hat auch keine Kennzahl. Nach „Jedes Ziel hat …“ nicht erfüllt.
- Nebenbefund: Ausgangswert Z3 "5 von 100 laut Blunt" passt nicht genau zur Kennzahl. Blunt spricht von Leads, die mit Kontext bearbeitet werden, die Kennzahl misst Kontakt innerhalb einer Frist. Das wird in Woche 1 ohnehin gemessen.

## C11 Abgrenzung klar: ✅

Alle sieben Zeilen der Nicht-Ziele-Tabelle haben „Warum nicht“ und „Wohin“ (Phase 2, eigener Auftrag oder nie). "Produkt für viele Kunden → Pattern-Team prüft" ist als Ziel weniger scharf, aber benannt.
Hinweis: Die Kurzfassung nennt zusätzlich "Kein Ersatz für Ihre Vertriebler". Das steht nicht in der Tabelle, ein „Wohin“ fehlt (inhaltlich: nie). Das Warum steht in *Lösung* ("nicht das Urteil"). Für Konsistenz in die Tabelle aufnehmen.

## C13 Einwände beantwortet: ❌

| # | Einwand (Kunde, blind) | Antwort im PRD | Urteil |
|---|---|---|---|
| E1 | Datenqualität ist der Engpass, nicht Recherchezeit; CRM-Bereinigung geparkt → Agent setzt auf Müll auf | Status-Check vor jedem Dossier (L2, L9), Guardrail G2, R5, Begründung der Bedürfnis-Wahl mit Belegen aus 9 Interviews, Schicksal B2 als MVP-Baustein + Phase 2 | ✅ beantwortet mit Beleg. Rest-Lücke: Bounces kommen vor allem von falschen E-Mail-Adressen (Jenkins "Half the emails bounce"). Der Agent ändert E-Mails nicht (L9), G2 verlangt nur "darf nicht steigen". Das sollte als offenes Restrisiko benannt werden. |
| E2 | Ohne LinkedIn wertlos, rechtlich ungeklärt → kein Pilot | R2 **offen**, O1, Phase 0 mit Go/No-Go vor dem Bau, Nutzenverlust ohne LinkedIn ausdrücklich eingeräumt (Kim "It’s 90% LinkedIn.") | ✅ als offen markiertes Risiko |
| E3 | T&M ohne Zahl nicht CFO-fähig; "mehr Gespräche" ist kein Business Case; will Kosten und Break-even über Meetings/Pipeline | Preis/Aufwand: O3 offen (zulässig, kaufmännische Zusage). **Business Case fehlt:** keine Kennzahl für Termine/Meetings oder Pipeline (Z1–Z4 messen Zeit, Calls, Lead-Bearbeitung, Brauchbarkeit), keine Break-even-Logik (auch nicht als Formel mit Platzhaltern), und die fehlende Wirtschaftlichkeitsrechnung ist nicht als offenes Risiko eingetragen. R3 behandelt nur "Lohnt sich das neben ZoomInfo". | ❌ nur zur Hälfte beantwortet |

---

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 | ✅ | Alle 29 Skript-Treffer sind nachgerechnete Ableitungen oder Regelnummern, Bewertungen und Gewichte sind als Annahme markiert, und die Stichprobe weiterer Zahlen steht wörtlich in `input/`. | Nichts zwingend; optional "9/10, 5/10" direkt aus `input/` belegen statt "laut Synthese" und die Zwei-Minuten-Zuschreibung an O'Neil (Frage, kein Ziel) entschärfen. |
| C5 | ✅ | Neun Personen wörtlich zitiert, Blunt mit ausdrücklich eigenem Budget ("my budget"). | – |
| C6 | ✅ | 7 begründete Kriterien, 5 korrekt gerechnete Gewichtungen plus Kipppunkt, Verlierer hat ausdrückliches Schicksal mit Grund. | – (optional: Z. 64 "zahlt nur mit Zeit" korrigieren, Chen zahlt Sales Navigator selbst) |
| C7 | ✅ | S1, S2 und S3 sind je mit einem zeichengenau in `strategy.md` gefundenen Satz und einer Begründung belegt. | – |
| C8 | ✅ | Vier echte Lösungsalternativen, jede mit Ausschlussgrund aus Interview und/oder Strategie. | – |
| C9 | ✅ | Alle vier Vorher-Szenen stehen so in den Interviews, alle Nachher-Szenen sind als *illustrativ* markiert. | – (aber: Nachher-Szenen 1 und 3 versprechen Nachfolger-Anlage und Listen-Erzeugung, die laut L1/L2 und Nicht-Zielen nicht im MVP sind, bitte angleichen) |
| C10 | ❌ | Z1–Z4 und die Guardrails sind vollständig, aber das NeoEmployee-Ziel (T&M-Umsatz, wiederverwendbarer Baustein) hat weder Ausgangswert noch Messzeitpunkt. | Für das NeoEmployee-Ziel Kennzahl, Ausgangswert (`[Platzhalter]`) und Messzeitpunkt ergänzen oder es aus *Ziele* herausnehmen. |
| C11 | ✅ | Jedes Nicht-Ziel der Tabelle nennt Grund und Ziel (Phase 2, eigener Auftrag oder nie). | – (optional: "Kein Ersatz für Ihre Vertriebler" aus der Kurzfassung mit "nie" in die Tabelle aufnehmen) |
| C13 | ❌ | Einwand 1 (Datenqualität) ist mit Beleg beantwortet, Einwand 2 (LinkedIn) als offenes Risiko markiert, aber Einwand 3 (Business Case) bleibt nur halb beantwortet. | Kennzahl für Termine/Meetings oder Pipeline im Pilot, Break-even-Logik mit `[Platzhalter]` (z. B. Kosten Pilot ÷ Wert je zusätzlichem Termin) oder ein Eintrag „Wirtschaftlichkeit offen“ in Risiken; dazu Restrisiko falsche E-Mails/Bounces (E-Mail-Verifikation erst Phase 2) benennen. |
