## Kurzfassung

**Worum es geht:** Die Vertriebsorganisation eines Kunden (alle zehn Befragten arbeiten dort) recherchiert vor jedem Anruf von Hand, was sie über Person und Firma wissen muss. Die Synthese hat zwei Kundenbedürfnisse herausgearbeitet: (1) Vertriebler brauchen den *Grund zum Anrufen* fertig aufbereitet, und (2) Kontaktdaten sollen aktuell und ohne Handarbeit im CRM stehen. Wir bauen zuerst **Bedürfnis 1** und nehmen von Bedürfnis 2 nur den kleinen Teil mit, ohne den Bedürfnis 1 nicht funktioniert: die Prüfung, ob die Person noch dort arbeitet.

**Was wir bauen:** Einen KI-Agenten, also eine Software, die für jeden Prospect (*potenziellen Kunden*) zwei bis drei aktuelle Anlässe aus öffentlichen Quellen sammelt (Finanzierungsrunde, Stellenausschreibungen, Führungswechsel, Themen), prüft, ob die Person noch in der Rolle ist, und daraus ein kurzes Dossier mit Gesprächsaufhänger und Quellenlink macht. Das Dossier wird am CRM-Datensatz des Leads abgelegt. Der Agent ersetzt den Skill *Prospect-Researcher*. Anrufen, Schreiben und Urteil bleiben beim Menschen.

**Warum 1 und nicht 2:** Bedürfnis 1 hat die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs. Es betrifft 9 von 10 Befragten statt 5. Der wichtigste Käufer, der VP of Sales, steht unter Druck vom Board und hat die Lösung selbst formuliert: "just hand them the dossier". Der Nutzen ist mehr Umsatz und nicht nur gesparte Kosten. Bedürfnis 2 hat einen klaren Käufer (Sales Ops), der aber in Kosten denkt und mit Werkzeugen vergleicht, die er schon heute zu teuer findet: "they break, or they’re too expensive to run on every single contact record". Bedürfnis 1 liegt bei fünf von acht Faktoren vorn und in drei von vier Gewichtungen insgesamt vorn; nur wenn man unterstellt, dass vorhandene Werkzeuge das Problem schon lösen, steht es gleich (Anhang A).

**Erfolgsmaß:** Gemessen wird am Ergebnis des Kunden, nicht an Minuten. Hauptziel ist **mehr gebuchte Meetings pro SDR** in der Pilotgruppe gegenüber einer Vergleichsgruppe ohne Dossier (Z6). Der Weg dahin: Recherchezeit pro Prospect von heute 15 bis 40 Minuten auf unter 2 Minuten (Zielmarke der Enablement-Direktorin: "can you find it in under two minutes?"), dadurch mehr Calls in Richtung des KPI von 50 pro Tag. Leitplanke: Die Antwortquote darf nicht sinken (Z5).

### Was der VP of Sales fragen wird, und unsere Antwort

| Einwand des Käufers | Antwort |
|---|---|
| *Recherchezeit ist nicht mein Problem, Pipeline ist es.* | Einverstanden. Abgerechnet wird der Pilot an gebuchten Meetings und Antwortquote der Pilotgruppe gegenüber einer Vergleichsgruppe (Z5, Z6), nicht an Minuten. Ross sagt selbst: "They are starving for good meetings." Bringt der Pilot keine Verbesserung, rollen wir nicht aus. |
| *Sales Navigator und ZoomInfo haben wir schon.* | Diese Werkzeuge liefern Rohdaten, und die Leute recherchieren trotzdem von Hand: Jenkins "I end up just Googling stuff half the time because the ZoomInfo login is always taken", Chen zahlt Sales Navigator selbst ("which I pay for myself") und braucht trotzdem 4 Stunden für 10 Kontakte. Der Agent ersetzt diese Lizenzen nicht, er nutzt sie als Quelle, wo die Lizenzbedingungen das erlauben, und macht aus den Rohdaten den fertigen Aufhänger. |
| *Kein offenes T&M-Projekt ohne Budget und Laufzeit.* | Der Einstieg ist begrenzt: Klärung und Machbarkeitstest (Phase 0 und 1) mit fester Obergrenze `[Platzhalter: Personentage]` und Go/No-Go-Entscheidung, bevor ein einziger SDR das Dossier nutzt. Erst danach wird der Pilot beauftragt. |
| *Ein falsches Dossier verbrennt mir den Account. Wer pflegt das danach?* | Kein Signal ohne Quellenlink, Rollen-Check vor jedem Dossier, jedes Dossier mit Datum und Ablaufdatum, unsichere Angaben werden als *unsicher* markiert statt geraten. Abnahmekriterium im Pilot ist eine Fehlerquote in Stichproben unter `[Platzhalter]` (Z7). Monitoring und Wartung nach Projektende sind Teil des Angebots, Umfang `[Platzhalter]`. |

### Für NeoEmployee: Aufwand, Ertrag, Risiken

**Aufwand:** Personentage pro Phase `[Platzhalter]`, Teamgröße `[Platzhalter]` von den 12 Leuten, die nicht im Pattern-Team sind (*14 minus 2*, aus „2 of our 14 people“). Gebunden wird das Team stufenweise: Phase 0 und 1 klein und gedeckelt, Pilot und Ausrollen erst nach Go. Gesamtlaufzeit bis Stufe 1 live: `[Platzhalter]`.

**Ertrag:** *Umsatz = Personentage × Tagessatz*, beides `[Platzhalter]`, abgerechnet nach „We bill on a time-and-material basis.“ Erste Rechnung nach Phase 0 und 1 `[Platzhalter: Abrechnungsrhythmus]`. Folgepotenzial: Stufe 2 (Account-Karte) und ein CRM-Abgleich für Sales Ops als eigenes Angebot, Umfang je `[Platzhalter]`. Dazu wiederverwendbare Signal-Bausteine für das Pattern-Team.

**Top-Risiken:**

1. **Datenzugriff und Recht** (die wichtigste Quelle ist LinkedIn, Personendaten): rechtliche Prüfung in Phase 1, vor dem Pilot. Ohne zulässigen Zugriffsweg kein Pilot.
2. **Falsche Signale beschädigen das Vertrauen:** Quellenpflicht, Stichproben, Fehlerquote als Abnahmekriterium.
3. **Budget liegt beim falschen Käufer:** Phase 0 klärt das; liegt es nur bei Sales Ops, drehen wir die Reihenfolge um.
4. **Scope Creep** Richtung Account-Karte und CRM-Abgleich: beide nur als eigene Beauftragung, nicht im Einstiegsumfang.
5. **Abnahme und Zahlung:** Abnahmekriterien (Go/No-Go, Z5 bis Z7) stehen vor Projektstart im Angebot; Abrechnung in kurzen Intervallen begrenzt das Ausfallrisiko.
6. **Nur eine Organisation befragt:** kein Produktversprechen, das Muster prüft das Pattern-Team.

### Entscheidung heute (Management NeoEmployee)

| Frage | Optionen und Folgen | Empfehlung |
|---|---|---|
| **E1: Mit welchem Bedürfnis gehen wir zum Kunden?** | (a) Bedürfnis 1 zum VP of Sales: größere Käufergruppe, Umsatzhebel. (b) Bedürfnis 2 zu Sales Ops: klarer Käufer, aber Preiskampf mit Standardwerkzeugen. | (a) |
| **E2: Wie steigen wir ein?** | (a) Gedeckelter Einstieg Phase 0 und 1, dann Go/No-Go: kleines Risiko, bindet wenige Leute, erste Rechnung früh. (b) Gesamtprojekt bis Ausrollen direkt anbieten: höherer Auftragswert, aber offene Machbarkeit und Rechtslage im Angebot. | (a) |
| **E3: Kaufmännische Eckwerte** | Tagessatz, Obergrenze für Phase 0 und 1, Wartungsanteil | Festlegen durch Management, `[Platzhalter]` |

Bis wann: vor dem Angebotstermin beim VP of Sales, `[Platzhalter: Datum]`.

---

