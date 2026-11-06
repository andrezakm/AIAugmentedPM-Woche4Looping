# Review O-r1 — Entwickler-Perspektive: Ist die Logik baubar?

Gelesen: ausschließlich `output/experiment-prd/O-ausschnitt-logik.md` (Approach, Goals, Non-Goals, Key Features, Key Flows, Key Logic).

Zählweise: Die fünf Punkte unter *Key Logic* enthalten mehrere unabhängig testbare Regeln; ich habe sie in atomare Regeln zerlegt und die Regeln ergänzt, die nur in *Key Flows* / *Key Features* stehen, aber Verhalten festlegen (Eingabe, Signal-Checkliste, Zustellung, Feedback). Jede Regel bekommt einen Testfall; wo eine Annahme nötig ist, steht sie dabei.

## Regeln und Testfälle

| # | Regel (Quelle) | Testfall: Eingabe → erwartetes Verhalten | Offene Frage |
|---|---|---|---|
| R1 | Nur Signale aus den letzten 90 Tagen; Fenster ist `[Platzhalter]` (Logic 1, Flow 3) | Prospect mit Funding-Meldung vom Lauf-Datum −89 Tage und Hiring-Post von −91 Tagen → Brief enthält nur das Funding-Signal. Fenster als Konfigurationswert, Default 90. | F1 |
| R2 | Ranking: Funding, Leadership Change, Hiring vor allgemeinen News (Logic 1) | Prospect mit 1 allgemeinem News-Artikel (−5 Tage), 1 Hiring-Signal (−60 Tage) → Hiring steht vor News. | F2, F3 |
| R3 | Ranking nach Relevanz für das Angebot des Kunden (Logic 1) | Zwei Hiring-Signale (DevOps-Rollen vs. Facility-Rollen), Kundenangebot = DevOps-Tooling → DevOps-Hiring wird gezeigt / rangiert höher. | F4 |
| R4 | Nie mehr als drei Signale (Logic 1, Logic 2) | Prospect mit 5 gültigen Signalen im Fenster → Brief zeigt genau die 3 bestrangierten. | — |
| R5 | Signal-Checkliste: Funding, Hiring in relevanten Funktionen, Leadership Change auf VP-Ebene, Topic-Aktivität; Irrelevantes wird verworfen (Flow 3) | Neuer „Director Marketing" und neuer „VP Engineering" → nur VP Engineering wird als Leadership-Signal geführt. Neuer CTO → wird geführt (Annahme: „VP-Ebene" = VP und höher). | F3, F5 |
| R6 | Jedes Signal eine Zeile (Logic 2) | Generierter Signaltext von 300 Zeichen → wird gekürzt bzw. neu generiert, bis er die Zeilengrenze einhält (Annahme: ≤ 140 Zeichen). | F6 |
| R7 | Genau ein Opening Angle, höchstens zwei Sätze (Logic 2, Feature 1) | Generator liefert drei Sätze → Validierung schlägt fehl, Neugenerierung; ausgeliefert wird 1 Angle mit ≤ 2 Sätzen. | — |
| R8 | Jedes Signal trägt Datum und Quelllink (Logic 2, Feature 1) | Gefundenes Signal ohne ermittelbares Datum oder ohne URL → wird nicht im Brief gezeigt (Annahme), statt ohne Beleg aufzutauchen. | F7 |
| R9 | Brief in unter zwei Minuten lesbar (Logic 2, Goal 1) | Abgeleitet aus R4/R6/R7: Brief-Gesamtlänge ≤ ca. 120 Wörter → Test auf Wortzahl. | — (durch R4/R6/R7 operationalisiert) |
| R10 | Kein relevantes Signal → Brief sagt explizit „No recent signal found", kein Auffüllen (Logic 3) | Prospect, dessen einzige Fundstelle 200 Tage alt ist → Brief-Text enthält „No recent signal found" und kein Füllmaterial. | F8 |
| R11 | Widersprüchliche Quellen → beide Angaben mit Datum zeigen, Rep entscheidet (Logic 3) | Website: „Head of Sales" (Stand 2026-06-10), LinkedIn: „VP Sales" (Stand 2026-09-20) → Brief zeigt beide Angaben mit je Datum und Link, kein automatisches Auswählen. | F9 |
| R12 | Agent überschreibt nie bestehende CRM-Felder (Kontakt, Stage, Notes); Brief nur als separater Anhang/Notiz (Logic 4, Feature 3) | Lauf auf Testrecord, Feld-Snapshot vorher/nachher → alle Felder identisch, genau ein neues Notiz-/Anhang-Objekt. Zweiter Lauf am Folgetag → bestehende Felder weiter unverändert. | F10 |
| R13 | Agent sendet nie etwas an einen Prospect (Logic 4, Non-Goal 1) | Code-/Berechtigungsprüfung: kein Mail-/Telefonie-/Messaging-Scope; Egress-Test während eines Laufs → keine Nachricht an Prospect-Adressen. | — |
| R14 | Batch von `[Platzhalter]` Prospects läuft über Nacht; Briefs vor Arbeitsbeginn verfügbar (Logic 5, Feature 2, Flow 5) | Liste mit N Prospects (Annahme N = 500) um 18:00 eingereicht → alle Briefs bis 07:00 Ortszeit des Reps am Record bzw. im Digest. | F11, F12 |
| R15 | Nur öffentliche und vom Kunden freigegebene Quellen (Logic 5, Flow 2) | Konfigurierte Quellen-Allowlist {Website, News, Funding-DB, Job Postings}; Quelle außerhalb der Liste → wird nicht abgefragt, Log zeigt keinen Zugriff. | F13 |
| R16 | Jeder Lauf wird protokolliert, Quellennutzung nachvollziehbar (Logic 5) | Nach einem Lauf → Log enthält pro Prospect: Lauf-ID, Zeitstempel, abgefragte Quellen/URLs, verwendete Signale. | F14 |
| R17 | Eingabe: Liste aus CRM-Auswahl oder CSV-Upload (Feature 2, Flow 1) | CSV mit Spalten Name, Firma, Firmen-Domain → für jede Zeile ein Brief; Zeile ohne Firma → Fehlermeldung im Lauf-Report, Rest läuft weiter. | F15 |
| R18 | Zustellung am Prospect-Record im CRM, Fallback Daily Digest; Methode in Woche 1 bestätigt (Feature 3, Flow 5) | Konfiguration „CRM" → Brief als Notiz am Record; Konfiguration „Digest" → ein Digest pro Rep mit allen Briefs seiner Liste. | F16 |
| R19 | One-Click-Feedback „useful / not useful" pro Brief (Feature 4, Flow 7) | Rep klickt „not useful" → Feedback mit Brief-ID, Rep, Zeitstempel gespeichert; wöchentlicher Export für das Review. | F17 |

**Anzahl Regeln: 19.**

## Offene Fragen

| # | Frage | Einstufung | Vernünftige Annahme, mit der ich baue |
|---|---|---|---|
| F1 | Wie lang ist das Freshness-Fenster endgültig (90 Tage ist Platzhalter)? | *nicht blockierend* | Konfigurationswert, Default 90 Tage. |
| F2 | Reihenfolge innerhalb der Top-Gruppe (Funding vs. Leadership vs. Hiring) und Tie-Break? | *nicht blockierend* | Feste Reihenfolge Funding > Leadership > Hiring > Topic > News, bei Gleichstand das neuere Signal zuerst. |
| F3 | Gehört „Topic-Aktivität" (Posts, Themen) zur Top-Gruppe oder zu „general news"? | *nicht blockierend* | Unter Hiring, über allgemeinen News. |
| F4 | Wie wird „Relevanz für das Angebot des Kunden" bestimmt, und wo ist das Angebot beschrieben? | *nicht blockierend* | Kunde liefert eine Angebotsbeschreibung + Liste relevanter Funktionen/Themen als Konfiguration; Relevanz = Match gegen diese Liste. |
| F5 | Welche Funktionen gelten als „relevant" fürs Hiring; zählt C-Level als „VP-Ebene"? | *nicht blockierend* | Funktionsliste aus F4-Konfiguration; VP und höher zählt. |
| F6 | Was heißt „eine Zeile" konkret (Zeichenlimit)? | *nicht blockierend* | ≤ 140 Zeichen pro Signal. |
| F7 | Welches Datum gilt: Ereignisdatum oder Veröffentlichungsdatum? Was passiert mit Signalen ohne Datum/Link? | *nicht blockierend* | Ereignisdatum, sonst Veröffentlichungsdatum; ohne beides → verworfen. |
| F8 | Gibt es bei „No recent signal found" trotzdem einen Opening Angle? | *nicht blockierend* | Nein, kein Angle (sonst wäre es Auffüllen). |
| F9 | Zählt ein widersprüchliches Paar als ein oder zwei der max. drei Signale? Was gilt überhaupt als Widerspruch? | *nicht blockierend* | Ein Signal (eine Zeile mit beiden Werten); Widerspruch = unterschiedliche Werte zum selben Attribut derselben Person/Firma. |
| F10 | Wiederholter Lauf für denselben Prospect: neue Notiz oder eigene alte Brief-Notiz ersetzen? Ist Ersetzen der eigenen Notiz „Überschreiben"? | *nicht blockierend* | Immer neue Notiz mit Datum; eigene alte Notizen bleiben unangetastet. |
| F11 | Wie groß ist ein Batch (Platzhalter), wie viele Reps/Listen parallel? | *nicht blockierend* | 500 Prospects pro Nacht, horizontal skalierbar gebaut; Volumen in Woche 1 messen. |
| F12 | Was heißt „vor Arbeitsbeginn": welche Uhrzeit, welche Zeitzone, bis wann muss die Liste eingereicht sein? | *nicht blockierend* | Fertig bis 07:00 Ortszeit des Reps, Einreichschluss 20:00 am Vortag. |
| F13 | Welche Quellen sind konkret freigegeben, und über welchen Zugang wird „LinkedIn public data" gelesen (API, Lizenz, Scraping — Nutzungsbedingungen)? | *nicht blockierend* | Quellen-Allowlist als Konfiguration; LinkedIn-Adapter bleibt aus, bis Zugang und Freigabe geklärt sind; die übrigen Quellen liefern weiter. |
| F14 | Was genau wird geloggt, wie lange aufbewahrt, wer darf es sehen? | *nicht blockierend* | Felder wie in R16, Aufbewahrung 90 Tage, Zugriff Projektteam + Sales Ops. |
| F15 | Welches CSV-Schema / welche Pflichtfelder identifizieren einen Prospect (Domain, LinkedIn-URL)? Welches CRM-System? | *nicht blockierend* | Pflicht: Name + Firma oder Firmen-Domain; CRM-Anbindung als Adapter, Digest als Fallback. |
| F16 | Über welchen Kanal und in welchem Format kommt der Daily Digest (E-Mail, Slack, PDF)? | *nicht blockierend* | E-Mail an den Rep, ein Abschnitt pro Prospect. |
| F17 | Wo wird das Feedback im Digest-Fall abgegeben, und gibt es ein Freitextfeld? | *nicht blockierend* | Zwei Links pro Brief im Digest bzw. Buttons an der CRM-Notiz; kein Freitext. |

**Anzahl offene Fragen: 17, davon blockierend: 0.**

Begründung, warum keine Frage blockiert: Jede offene Stelle ist entweder ein Parameter (Fenster, Batchgröße, Uhrzeit, Zeilenlänge), eine Konfiguration (Quellen, Angebot, relevante Funktionen) oder eine Integrationsvariante, für die der PRD selbst schon einen Fallback nennt (Digest statt CRM). Mit den Annahmen oben kann ich jede Regel bauen und testen; Antworten des Kunden ändern Werte, nicht die Architektur. Die heikelste Frage ist F13 (LinkedIn-Zugang): Sie kann einen Teil der Signalabdeckung kosten, verhindert den Bau aber nicht.

Zum Abgleich durch den Koordinator: Ob F1–F17 unter *Offene Punkte* im PRD stehen, kann ich aus dem Ausschnitt nicht sehen. Im Ausschnitt selbst sind nur F1 (90 Tage `[Platzhalter]`), F11 (Batchgröße `[Platzhalter]`) und F16/F15 teilweise (Zustellmethode „confirmed in Week 1") als offen markiert.

## Urteil

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 „Logik ist baubar" | ✅ | Für alle 19 Regeln lässt sich ein konkreter Testfall formulieren, und keine der 17 offenen Fragen verhindert den Bau mit einer vernünftigen Annahme. | Nichts Blockierendes; die 17 nicht blockierenden Fragen (v. a. F4 Relevanz-Definition, F9 Zählung widersprüchlicher Signale, F13 LinkedIn-Zugang, F11/F12 Batchgröße und Deadline) sollten unter *Offene Punkte* stehen. |
