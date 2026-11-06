# Review A, Runde 1: Faktenprüfer

Geprüft: `output/PRD-signal-brief-agent-2026-11-03.md` gegen `.claude/skills/prd-goal/criteria.md`.
Quellen: `input/Interview_Gen_01–10.md`, `context/strategy.md`, `context/company.md`, Skriptausgabe `A-r1-skript.txt`, Kunden-Einwände `A-r1-kunde.md`. Andere Dateien in `output/` wurden nicht gelesen.

---

## C1 Gerüst (gleichwertig)

| Gerüst-Überschrift | Gleichwertiger Abschnitt im PRD | Urteil |
|---|---|---|
| `# PRD: [Produktname]` | `# PRD: Signal-Brief Agent` (Z.1) | ✅ |
| `## Kurzfassung` | `# Auf einer Seite` (Z.16–41) | ✅ |
| `## Problem` | `## Problem & Opportunity` (Z.115) | ✅ |
| `## Warum dieses Problem (Wahl und Strategie)` | **kein eigener Abschnitt.** Verstreut: Absatz „Warum dieses Problem und nicht das zweite" in der Kurzfassung (Z.34), Tabellenzeile „Passt es zur Strategie?" (Z.56), Bullet „Warum es für NeoEmployee zählt" (Z.120), Detail in Anhang A | ❌ |
| `## Lösung` | `## High-Level Approach` (Z.134) + `# Solution Alignment / ## Key Features` (Z.168ff.) | ✅ |
| `### Alternativen` | „**Alternatives considered:**" (fett, Z.140) | ✅ |
| `### Vorher und nachher` | `### Narrative` (Z.146) | ✅ |
| `## Ziele` | `## Goals` (Z.152) | ✅ |
| `## Nicht-Ziele` | `## Non-Goals` (Z.159) | ✅ |
| `## Logik` | `### Key Logic` (Z.196) | ✅ |
| `## Plan` | `# Development and Launch Planning` + `## Operational Checklist` (Z.206ff.) | ✅ |
| `## Risiken und Einwände` | `### Risks` + `### FAQ` (Z.232ff.) | ✅ |
| `## Offene Punkte` | **kein eigener Abschnitt.** Nur ein fetter Absatz „Offene Punkte für den Kunden-Kickoff" im Loop-Protokoll Runde 1 (Z.327) und „Bewusst offen gelassen" in Runde 2 (Z.345) | ❌ |
| `## Anhang A: Bewertung der Bedürfnisse` | `#### Anhang A: Problem-Auswahl im Detail` (Z.261) | ✅ |
| `## Loop-Protokoll` | `#### Anhang B: Loop-Protokoll` (Z.299) | ✅ |

**Ergebnis: ❌.** 13 von 15 haben eine Entsprechung. „Warum dieses Problem" und „Offene Punkte" fehlen als Abschnitt. Ihr Inhalt ist auf vier bzw. zwei Stellen verteilt, die offenen Punkte stehen nur im Loop-Protokoll.

## C2 Zitate (nur Skript-Meldung)

Skript meldet **❌**: 78 belegt, 20 eigene Worte, **3 NICHT BELEGT**: „clarity of the ROI", „revenue in weeks, not months", „prefer the quick fix". Alle drei stammen aus `scripts/PRD-writer.md`, nicht aus `input/` oder `context/` (Anhang A, Z.275–276, und Loop-Protokoll Z.309).

## C3 Keine erfundenen Zahlen

Skriptliste:

| Zeile | Zahl | Zulässig? | Begründung |
|---|---|---|---|
| 150 | 25 („mittags bei Call 25") | ❌ | Steht in keiner Quelle, ist nicht berechnet und nicht als Annahme oder *illustrativ* gekennzeichnet. Green macht im Interview außerdem E-Mails, keine Anrufe. |
| 202 | 60 („unter 60 Sekunden") | ✅ | Als „Zielwert, im Prototyp zu prüfen" gekennzeichnet. |
| 281 | 92 / 63 | ✅ | Nachgerechnet: B1 = (5·20+4·15+5·20+5·10+4·15+5·10+4·10)/5 = 460/5 = 92; B2 = 315/5 = 63. Gewichte summieren sich auf 100. |
| 287 | 92 / 63 | ✅ | Wie oben. |
| 288 | 91 / 66 | ✅ | Gleiche Gewichte: 32/35 = 91,4 → 91; 23/35 = 65,7 → 66. |
| 289 | 90 / 72 | ✅ | Gewichte K2=30, K3=10, K5=10, Rest unverändert (Summe 100): 450/5 = 90; 360/5 = 72. |
| 290 | 92 / 71 | ✅ | B2 mit K1=5: (315+40)/5 = 71. |
| 291 | 92 / 81 | ✅ | B2 mit K3=5 und K7=5: (315+60+30)/5 = 81. |

Stichproben weiterer Zahlen:

| Stelle | Zahl | Zulässig? | Begründung |
|---|---|---|---|
| Z.18 | 15–40 Minuten | ✅ | Thorne „15 minutes per prospect", O'Neil „forty minutes". |
| Z.27–30 | 20/50, 4/Std., 5 von 100, 4 Std./10 Kontakte, 40 Min. | ✅ | Jenkins, Thorne, Blunt, Chen, O'Neil. Hinweis: „eingekaufte" Marketing-Kontakte steht so nicht bei Blunt (Webinare, Whitepaper, Events). |
| Z.32 | 480.000 $ / 240.000 $ | ✅ | Berechnet aus 12 („A dozen", Ross) × ½ („half my day", Jenkins) × 80.000 $ (Kim) und als Schätzung gekennzeichnet. |
| Z.52 | 60 Personentage, 60.000 €, 30 PT | ✅ | Berechnet aus 2 × 6 Wochen (Vorschlag), Tagessatz als Platzhalter gekennzeichnet. |
| Z.51 | 2 von 12 | ✅ | 14 − 2 aus `strategy.md`. |
| Z.148 | „acht E-Mails" bis mittags | ❌ | Steht in keiner Quelle, nicht gekennzeichnet. Das Skript erfasst es nicht, weil die Zahl ausgeschrieben ist. |
| Z.150 | „vor 9 Tagen", „drei offene Stellen", „seit 6 Wochen" | ❌ | Erfundene Beispielwerte im Brief. Kursiv heißt laut Format-Hinweis „eigene Umschreibung", als *illustrativ* sind sie nicht markiert. |
| Z.211 | 20 Test-Prospects, 3–5 Reps | ✅ | Planungsparameter bzw. als Vorschlag gekennzeichnet, keine Tatsachenbehauptung. |

**Ergebnis: ❌.** Alle Bewertungszahlen rechnen sich korrekt nach. Im Nachher-Narrativ stehen aber erfundene Zahlen ohne Kennzeichnung (25, acht, 9 Tage, 6 Wochen).

## C5 Problem breit belegt

Der Problem-Abschnitt (Z.119–132) zitiert wörtlich 9 Personen: Thorne, O'Neil, Ross, Jenkins, Green, Chen, Petit, Baker, Blunt. Alle Zitate habe ich in `input/` gefunden. Einzige Abweichung: Bei Petit steht 'hello' statt "hello" mit doppelten Anführungszeichen. Budgetverantwortung haben Thorne (VP Sales), Ross (Sales Director) und Blunt („my budget", Interview 05). **✅**

## C6 Wahl begründet und robust

- 7 benannte Kriterien K1–K7. Beide Bedürfnisse sind je Kriterium bewertet, jede Bewertung hat eine Begründung. ✅
- Ergebnis benannt (Z.293). ✅
- Schicksal des Verlierers: Beschäftigungs-Check als MVP-Baustein, voller CRM-Abgleich als Phase 2 bzw. Folgeauftrag, beides mit Grund (Z.295). ✅
- **Alternative Gewichtungen: nur 2.** „Alle gleich gewichtet" und „Kostensicht" ändern die Gewichte. „Sales Ops ist der Käufer" und „CRM-Integration trivial" ändern dagegen *Punktwerte*, nicht Gewichte. Sie sind Sensitivitäten der Bewertung, keine Gewichtungen. ❌

**Ergebnis: ❌.** Es fehlt mindestens eine dritte echte Gewichtungsvariante.

## C7 Strategie nachgewiesen

| Punkt | Wörtlicher Satz aus `strategy.md` in „…" | Begründung | Urteil |
|---|---|---|---|
| S1 Vision-Filter | **keiner.** Nur die deutsche Umschreibung „Vision-Filter" (Z.56, 108, 277). Der Satz „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills" wird nicht zitiert. | vorhanden (ersetzt Recherche-Skill) | ❌ |
| S2 Umsatz | „Revenue is runway" (Z.56, 268, 278). Das ist der fett gesetzte Bullet-Anfang, kein ganzer Satz, aber wörtlich. | vorhanden (schnell Umsatz, Runway) | ✅ (knapp) |
| S3 Muster | „The Bridge: Pattern Recognition" (Z.279). Das ist eine **Überschrift**, kein Satz. | vorhanden (K6: generische Signal-Typen) | ❌ (im Zweifel) |

**Ergebnis: ❌.**

## C8 Alternativen ernsthaft

- „Bedürfnis 2 zuerst" ist eine Problemalternative und zählt nicht.
- „Mehr ZoomInfo-/Sales-Navigator-Lizenzen": Lösungsalternative. Der Ausschluss stützt sich auf Interviews (Thorne „unstructured", Kim „too expensive", Jenkins „login is always taken", FAQ Z.244) und auf die Strategie (Vision-Filter). ✅
- „Mehr wählen / Druck": Lösungsalternative. Der Ausschluss stützt sich auf Blunt „conversion is higher if you know the context" (wörtlich belegt) und Ross' Team („the only way to get a response"). ✅
- „Vollautomatische Ansprache": Lösungsalternative, gestützt auf Petit und Green. Die Zitate sind aber umgedeutet: Petit spricht über das Lesen von Profilen, Green über ihren eigenen, erzwungenen Aufhänger, keiner von beiden über Automatik. Diese Alternative ist schwach, aber zwei tragen auch ohne sie.

**Ergebnis: ✅.**

## C9 Narrativ ist echt

Vorher (Z.148):
- 50 Leads: Die Zahl stammt aus der Frage des Interviewers an Green, ist aber sinngemäß ok.
- LinkedIn, Firmenseite, News, scrollt Posts; 30 Minuten; Sauerteig-Aufhänger: Green, Interview 07 ✅ (Sauerteig war auf Twitter).
- Nichts Persönliches, nimmt den „Digital Transformation"-Like, fühlt sich fake an: Green ✅
- Andere sind schneller: Green „Everyone else seems to do it faster" ✅
- **„Mittags hat sie acht E-Mails geschrieben"**: nicht belegt, erfunden, nicht markiert ❌
- Chen kopiert um Mitternacht in eine Tabelle für zehn Leute: Chen ✅

Nachher (Z.150): Die ganze Szene ist erfunden, mit konkretem Brief (Series B vor 9 Tagen, drei Stellen, neuer VP seit 6 Wochen), „Call 25" und „Chen schläft". Das ist zwar ein Zukunftsbild, aber **nicht als *illustrativ* markiert**. Kursiv bedeutet laut Format-Hinweis nur „eigene Umschreibung". ❌

**Ergebnis: ❌.**

## C10 Ziele messbar

| Ziel | Kennzahl | Ausgangswert | Messzeitpunkt | Urteil |
|---|---|---|---|---|
| 1 Recherchezeit | min/Prospect ✅ | 15–40 Min. (Interviews) ✅ | „vor und nach dem Launch", ohne konkreten Zeitpunkt nach Launch | ❌ (im Zweifel) |
| 2 Outreach-Volumen | Calls/Tag, Anteil bearbeiteter Leads ✅ | 20 (Jenkins), ~5/100 (Blunt) ✅ | **keiner** für die Zielerreichung, nur „Zielwerte in Woche 1 festgelegt" | ❌ |
| 3 Gefühl | „Kurzumfrage", **keine konkrete Kennzahl** (Skala/Wert) | **keiner, auch kein Platzhalter** | „vor und nach dem Launch" | ❌ |
| 4 Guardrail | Antwort-/Terminquote, Bounce-Rate ✅ | nicht im Ziel genannt, nur indirekt über „Baseline Woche 1" im Plan | nicht genannt | Guardrail vorhanden ✅, aber unvollständig |

**Ergebnis: ❌.**

## C11 Abgrenzung klar

| Nicht-Ziel | Warum nicht | Wohin | Urteil |
|---|---|---|---|
| 1 Kein Versand/Sequenzierung | ✅ | **fehlt** (Phase 2? nie?) | ❌ |
| 2 Kein CRM-Schreiben | ✅ Integrationsrisiko | Phase 2/Folgeauftrag ✅ | ✅ |
| 3 Marketing-Sales-Konflikt | ✅ Organisationsfrage | **fehlt**, nur „entschärft sich indirekt" | ❌ |
| 4 Enterprise-Mapping | ~ „eigene, größere Ausbaustufe" | „Saved for future" (vage, entspricht Future Consideration 3) | knapp ✅ |

**Ergebnis: ❌.**

## C13 Einwände beantwortet

| Einwand (Kunde) | Antwort im PRD | Urteil |
|---|---|---|
| 1 „Das kann ich schon kaufen", Trigger-Signale liefern vorhandene Tools | FAQ zu ZoomInfo (Kontaktdaten statt Anlass, Thorne „unstructured", Kim, Jenkins). K5 als **Annahme** markiert, „muss im Kickoff bestätigt werden". Offene Punkte (Z.327) und Investorenteil Punkt 5 („keinen Wettbewerber … wird geprüft"). Ein Beleg zu Trigger-Signal-Tools fehlt, aber der Punkt ist ausdrücklich als offen markiert. In der Risikoliste steht er nicht. | ✅ (als offen markiert, knapp) |
| 2 Ohne LinkedIn leerer Brief, halbes Projekt bezahlt vor Nutzen-Nachweis | Risiko 1 ausdrücklich offen. Entscheidungspunkt nach Woche 3 mit Untergrenze 30 PT. Alternativquellen für die Signal-Typen genannt. | ✅ |
| 3 240.000 $ sind kein Umsatz, es zählen Meetings/Pipeline, generische KI-Einstiege verbrennen Accounts | Kurzfassung nennt es „Gehaltsanteil", nicht Umsatz. Risiko 5: Umsatz-Effekt nur geschätzt und nur berichtet. Guardrail: Antwort- und **Terminquote** darf nicht sinken. Risiko 4 und Logik 3: kein generischer Aufhänger, Quelle Pflicht. Gebuchte Meetings und Pipeline sind keine Zielkennzahl, aber als Guardrail bzw. offenes Risiko adressiert. | ✅ |

**Ergebnis: ✅.**

---

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C1 | ❌ | 13 von 15 Gerüst-Überschriften haben eine Entsprechung (Auf einer Seite, Problem & Opportunity, High-Level Approach/Key Features, Alternatives considered, Narrative, Goals, Non-Goals, Key Logic, Development and Launch Planning, Risks/FAQ, Anhang A, Anhang B). | Eigener Abschnitt „Warum dieses Problem (Wahl und Strategie)" (heute verteilt auf Z.34, 56, 120, Anhang A) und eigener Abschnitt „Offene Punkte" (heute nur im Loop-Protokoll Z.327/345). |
| C2 | ❌ | Das Skript meldet 3 NICHT BELEGT (nur vermerkt). | „clarity of the ROI", „revenue in weeks, not months", „prefer the quick fix" stammen aus `scripts/PRD-writer.md`, nicht aus `input/` oder `context/`. |
| C3 | ❌ | Die Bewertungszahlen 92/63/91/66/90/72/71/81 und 60 Sek. sind nachgerechnet bzw. gekennzeichnet, im Nachher-Narrativ stehen aber erfundene Zahlen ohne Kennzeichnung. | „Call 25" (Z.150), „acht E-Mails" (Z.148), „vor 9 Tagen"/„drei offene Stellen"/„seit 6 Wochen" (Z.150) als *illustrativ* oder Annahme markieren oder streichen. |
| C5 | ✅ | 9 Personen sind wörtlich und gegen `input/` geprüft zitiert, darunter Thorne, Ross und Blunt („my budget") mit Budgetverantwortung. | Nichts (nur Kleinigkeit: Petit 'hello' statt "hello"). |
| C6 | ❌ | Es gibt 7 begründete Kriterien, ein benanntes Ergebnis und ein Schicksal für den Verlierer, aber nur 2 echte alternative Gewichtungen. | Mindestens eine dritte Gewichtungsvariante; „Sales Ops als Käufer" und „Integration trivial" ändern Punktwerte, nicht Gewichte. |
| C7 | ❌ | S2 ist mit „Revenue is runway" belegt, S1 hat kein wörtliches Strategie-Zitat und S3 nur eine Überschrift. | Für S1 ein wörtlicher Satz, z. B. „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills", für S3 ein Satz statt der Überschrift, je mit Begründung. |
| C8 | ✅ | Mindestens 2 echte Lösungsalternativen (mehr Lizenzen, „mehr wählen") sind mit Interview- und Strategiebeleg ausgeschlossen. | Nichts zwingend; die Zitate zur Vollautomatik (Petit, Green) sind umgedeutet. |
| C9 | ❌ | Das Vorher ist großteils durch Green und Chen belegt, das Nachher ist eine erfundene Szene ohne Kennzeichnung. | Nachher und das Detail „acht E-Mails bis mittags" als *illustrativ* markieren. |
| C10 | ❌ | Ziel 1 und 2 haben Kennzahl und Ausgangswert, Ziel 3 hat weder Kennzahl noch Ausgangswert, und für die Zielerreichung fehlen konkrete Messzeitpunkte; ein Guardrail ist vorhanden. | Ziel 3: konkrete Kennzahl plus `[Platzhalter: messen in Woche 1]`; konkrete Messzeitpunkte (z. B. Woche X nach Launch) für alle Ziele; Ausgangswert für den Guardrail. |
| C11 | ❌ | Nicht-Ziel 2 und knapp 4 sagen warum und wohin, Nicht-Ziel 1 und 3 nennen kein Ziel. | Für „Kein Versand" und „Marketing-Sales-Konflikt" angeben: Phase 2, anderer Auftrag oder nie. |
| C13 | ✅ | Alle drei Kundeneinwände sind beantwortet: LinkedIn und Umsatz über Risiken, Guardrail und Entscheidungspunkt, „schon kaufbar" als ausdrücklich offene Annahme (K5, Offene Punkte, Investorenteil). | Empfohlen: Einwand 1 in die Risikoliste aufnehmen, mit konkretem Abgleich gegen Trigger-Signal-Tools. |
