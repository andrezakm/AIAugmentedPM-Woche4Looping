# PRD-Zielkriterien

Diese Kriterien ersetzen die Ausfüll-Anweisungen des PRD-Templates. Das Template sagte, *was* in jeden Abschnitt gehört. Die Kriterien sagen, *wann* ein Abschnitt gut genug ist, und *wer* das prüft.

Ein Kriterium gilt nur dann als erfüllt, wenn sein Prüfer es bestätigt. Der Autor prüft sich nie selbst.

## Prüfer

| Kürzel | Prüfer | Bekommt |
|---|---|---|
| **SKRIPT** | `scripts/check_prd.py` | PRD, `input/`, `context/` |
| **PRÜFER** | Subagent „Faktenprüfer“ | PRD, diese Kriterien, `input/`, `context/` |
| **LAIE** | Subagent „Nicht-Techniker aus dem Vertrieb“ | nur den Abschnitt *Problem* |
| **ENTW** | Subagent „Entwickler, der das bauen soll“ | nur die Abschnitte *Lösung* und *Logik* |
| **KUNDE** | Subagent „VP Sales beim Kunden“ | nur die Kurzfassung |
| **CEO** | Subagent „CEO von NeoEmployee“ | den ganzen PRD, mit 2 Minuten Lesezeit |

## Kriterien

| # | Kriterium | Prüfer | Erfüllt, wenn |
|---|---|---|---|
| C1 | **Gerüst vollständig** | SKRIPT | Alle Überschriften aus `skeleton.md` sind vorhanden, keine ist leer |
| C2 | **Zitate echt** | SKRIPT | `/quote-check` meldet 0 NICHT BELEGT |
| C3 | **Keine erfundenen Zahlen** | SKRIPT + PRÜFER | Jede Zahl ist (a) in `input/` oder `context/` belegt, (b) aus belegten Zahlen nachvollziehbar berechnet, (c) ein `[Platzhalter]` oder (d) eine **Annahme im Annahmen-Block** (siehe Datenregel). Eine Zahl, die nur im Fließtext als *Schätzung* markiert ist, zählt als ❌. Preise, Tagessätze und Summen in Geld sind immer `[Platzhalter]`. |
| C4 | **Problem steht für sich** | LAIE | Der Laie kann nach dem Problem-Abschnitt in 2–3 eigenen Sätzen sagen: wer leidet, woran, was es kostet. Der Prüfer vergleicht das mit der Synthese: kein wesentlicher Punkt fehlt, nichts ist falsch. |
| C5 | **Problem ist breit belegt** | PRÜFER | Das gewählte Problem ist mit wörtlichen Zitaten von mindestens 4 verschiedenen Personen belegt, darunter mindestens eine mit Budgetverantwortung |
| C6 | **Wahl ist begründet und robust** | PRÜFER | Beide Bedürfnisse der Synthese sind auf mindestens 5 benannten Kriterien bewertet, jede Bewertung hat eine Begründung. Mindestens 3 alternative Gewichtungen sind durchgerechnet und das Ergebnis ist benannt. Der Verlierer hat ein ausdrückliches Schicksal (MVP-Baustein, Phase 2 oder verworfen, mit Grund). |
| C7 | **Strategie nachgewiesen** | PRÜFER | S1 Vision-Filter, S2 Umsatz und S3 Muster sind je mit einem wörtlichen Satz aus `context/strategy.md` in „…“ und einer Begründung belegt |
| C8 | **Alternativen ernsthaft** | PRÜFER | Mindestens 2 Lösungsalternativen (nicht Problemalternativen). Jede hat einen Ausschlussgrund, der sich auf Interview oder Strategie stützt. |
| C9 | **Narrativ ist echt** | PRÜFER | Jede Situation im Vorher/Nachher-Narrativ kommt so oder sinngemäß in mindestens einem Interview vor. Erfundene Szenen sind als *illustrativ* markiert. |
| C10 | **Ziele messbar** | PRÜFER | Jedes Ziel hat eine Kennzahl, einen Ausgangswert (aus Interview oder `[Platzhalter: messen in Woche 1]`) und einen Messzeitpunkt. Mindestens ein Guardrail, also etwas, das nicht schlechter werden darf. |
| C11 | **Abgrenzung klar** | PRÜFER | Jedes Nicht-Ziel sagt, warum nicht und wohin es geht (Phase 2, anderer Auftrag oder nie) |
| C12 | **Logik ist baubar** | ENTW | Für jede Regel unter *Logik* lässt sich ein Testfall formulieren (Eingabe → erwartetes Verhalten). Keine offene Frage **blockiert den Bau**. Nicht blockierende Fragen sind erlaubt, wenn sie unter *Offene Punkte* stehen. Blockierend heißt: Ohne Antwort kann der Entwickler die Regel nicht einmal mit einer vernünftigen Annahme bauen. |
| C13 | **Einwände beantwortet** | KUNDE + PRÜFER | Runde 1: Der Kunde nennt blind seine 3 stärksten Einwände. Ab Runde 2: Er prüft die **gesammelten Einwände** der Vorrunden und darf höchstens 1 neuen nennen, nur wenn er ihn für einen K.-o.-Grund hält. Der Prüfer bestätigt, dass der PRD jeden Einwand der Liste beantwortet, mit Beleg oder als offen markiertem Risiko. |
| C14 | **Entscheidbar in 2 Minuten** | CEO | Der CEO kann nach 2 Minuten sagen: was wir bauen, was es kostet (Aufwand), was es bringt, was schiefgehen kann und was er entscheiden muss. Sein Urteil: *klar und überzeugend*. |

## Datenregel (gilt für C3 und C14)

- Belegt ist, was in `input/` oder `context/` steht.
- Ein interner PRD darf **Aufwand** (Personentage, Teamgröße, Dauer) und **technische Startwerte** (Schwellen, Zeitfenster) als Annahme nennen, aber nur gesammelt in einem Block **„Annahmen (nicht belegt)“** unter *Offene Punkte*. Jede Annahme hat eine Begründung und einen Zeitpunkt, an dem sie durch einen Messwert ersetzt wird.
- Preise, Tagessätze, Umsatz in Geld und alles, was der Kunde als Zusage lesen könnte, sind immer `[Platzhalter]` und werden dem Menschen zur Entscheidung vorgelegt.
- Im Fließtext darf eine Annahme nur mit Verweis stehen, z. B. „8–12 PW (Annahme A2)“.

## Rangfolge bei Konflikten

Wenn sich zwei Kriterien widersprechen (z. B. kurz vs. vollständig), gilt diese Reihenfolge:

1. Wahrheit: C2, C3, C9
2. Beleg: C5, C6, C7
3. Entscheidbarkeit: C14, C4, C13
4. Baubarkeit: C12, C10, C11, C8
5. Form: C1

Was weiter unten steht, gibt nach. Länge ist kein Kriterium. Ein Abschnitt ist so lang, wie die Kriterien es verlangen.

## Loop-Regeln

- **Runde 1 (Suche):** Skript laufen lassen, alle Prüfer parallel und frisch starten. Der Koordinator trägt die Urteile in die Anzeigetafel ein und sammelt jedes ❌ und jeden Einwand als nummerierten Punkt in der **offenen Liste** (`offene-punkte.md`).
- **Ab Runde 2 (Abhaken):** Neue Prüfer, aber jeder bekommt seinen Teil der offenen Liste und hakt ab: *erledigt / nicht erledigt*, mit einem Satz Begründung. Neue Funde zählen nur, wenn sie blockieren (C12) oder ein K.-o.-Grund sind (C13), und je Prüfer höchstens 1. So misst jede Runde gegen dasselbe Ziel.
- Ein Kriterium ist ab Runde 2 ✅, wenn alle seine Punkte der offenen Liste *erledigt* sind und kein neuer Blocker dazukam.
- Jeder Durchgang wird im Loop-Protokoll mit der Kriterien-Tabelle C1–C14 festgehalten.
- Abbruch: alle 14 Kriterien ✅ in **einem** Durchgang. Nach 4 Durchgängen ohne vollen Erfolg ist trotzdem Schluss, dann mit offenen Punkten berichten.

## Änderungen

- v2 (2026-11-05): Datenregel mit Annahmen-Block (C3, C14). C12 „blockierend“ statt „höchstens 1 offen“. C13 kumulative Einwandliste. Ab Runde 2 abhaken statt neu suchen. Anlass: Experiment Template vs. Kriterien, Runde 2 konvergierte nicht.
