# Review A, Runde 1: Entwickler-Sicht auf `A-ausschnitt-logik.md`

Rolle: Entwickler, der das bauen soll. Gelesen: nur `output/experiment-prd/A-ausschnitt-logik.md`.
Frage: Kann ich für jede Regel einen konkreten Testfall (Eingabe → erwartetes Verhalten) schreiben?

Legende: **testbar** = Testfall eindeutig formulierbar · **teilweise** = testbar nur mit einer Annahme, die ich treffen muss · **offen** = kein Testfall ohne Raten möglich.

## Regeln aus „Key Logic"

| # | Regel (Quelle) | Testfall: Eingabe → erwartetes Verhalten | Status | Offene Frage |
|---|---|---|---|---|
| R1 | Nur Signale aus den letzten 90 Tagen (KL 1a) | Prospect mit Funding-News vom Tag −89 und Tag −91 → nur −89 erscheint. | teilweise | Zählt das Veröffentlichungsdatum der Quelle oder das Datum des Ereignisses (z. B. Funding-Runde im Januar, Artikel im April)? Stichtag = Lauf-Datum? |
| R2 | Nur vereinbarte Signal-Typen (KL 1b, Feature 1) | Funding Series B → gezeigt; neue Stelle „Senior Backend Engineer" → gezeigt; neuer VP Sales → gezeigt; Produkt-Launch-Pressemitteilung → nicht gezeigt. | offen | Thornes „about to go under" ist kein operationalisierter Typ: Woran erkennt der Agent das (Entlassungen, Insolvenzmeldung, negative News)? Ist die Typ-Liste abschließend, oder wird sie „vereinbart" (mit wem, wann)? Zählen auch Series A / D, Hiring außerhalb Engineering/Ops, Wechsel unterhalb VP? |
| R3 | Nur Signale mit prüfbarer Quelle (KL 1c) | Signal ohne Link oder mit totem Link (HTTP 404) → verworfen. | teilweise | Gilt ein Link hinter Paywall/Login als „prüfbar"? Wird der Link zum Zeitpunkt der Erstellung geprüft? |
| R4 | Höchstens 3 pro Prospect, nach Relevanz sortiert (KL 1, Flow 4) | 5 gültige Signale → genau 3 im Brief. | offen (Sortierung) | „Relevanz" ist nicht definiert: Welche Gewichtung von Typ, Aktualität und Angebotsbezug? Was bei Gleichstand? Gleiches Ereignis aus 3 Quellen = 1 Signal oder 3? |
| R5 | Keine persönlichen Details ohne Geschäftsbezug (KL 1) | Quelle enthält Urlaubspost „Cabo" und Reunion-Fotos → erscheinen nicht, auch nicht im Aufhänger. | testbar | (Randfall: privater Post über einen Jobwechsel, hat Geschäftsbezug? Ich nehme „ja" an.) |
| R6 | Format: pro Signal ein Satz, plus ein Aufhänger, keine Biografie, lesbar < 2 Min. (KL 2) | Brief mit 3 Signalen → 3 Signalzeilen à 1 Satz + Datum + Link + „Warum relevant", 1 Aufhänger, kein weiterer Fließtext. | teilweise | „Unter 2 Minuten" braucht ein messbares Proxy: maximale Wortzahl pro Brief? |
| R7 | Keine Signale → „Keine relevanten Signale", kein generischer Aufhänger (KL 3) | Prospect ohne Treffer → Brief zeigt exakt „Keine relevanten Signale", Aufhänger-Feld leer. | testbar | – |
| R8 | Widersprüchliche Quellen → beide mit Datum zeigen (KL 3) | Quelle A (01.10.): „CTO ist X", Quelle B (15.10.): „CTO ist Y" → beide Aussagen mit Datum, kein Auflösen. | teilweise | Was gilt als Widerspruch (nur gleiche Eigenschaft, unterschiedlicher Wert)? Zählen die zwei Einträge gegen das Limit von 3? |
| R9 | Unsicher, ob ausgeschieden → Status *unsicher*, nicht als Tatsache (KL 3, Feature 2) | Profil sagt „noch bei Firma", Firmenseite listet Person nicht mehr → Status *unsicher*. | offen | Ab wann ist es *ausgeschieden*, ab wann *unsicher*? Welche Quelle schlägt welche? Läuft für *unsicher* die Signal-Suche (Flow 3 nennt nur „aktive")? |
| R10 | Überschreibt keine CRM-Felder, ändert keine Kontaktdaten, versendet nichts, hängt nur Notizen an (KL 4, Flow 5) | Lauf über Test-CRM → Diff aller Felder vorher/nachher = 0; einzige Schreiboperation = neue Notiz; keine ausgehende Mail/Nachricht. | testbar | – |
| R11 | Nur freigegebene Quellen (KL 4) | Quelle nicht auf der Freigabeliste (z. B. nicht freigegebene Datenbank) → wird nicht abgefragt, Signal daraus erscheint nicht. | testbar | (Freigabeliste kommt aus der Operational Checklist, muss vor Bau vorliegen.) |
| R12 | Bis zu 100 Prospects pro Rep bis 8:00 fertig (KL 5, Feature 3) | 100 Prospects, Liste um 20:00 hochgeladen → alle Briefs um 08:00 vorhanden. | teilweise | Zeitzone des Reps oder des Systems? Spätester Upload-Zeitpunkt, ab dem 8:00 garantiert ist? Verhalten bei 101+ Prospects? |
| R13 | Einzel-Brief auf Abruf < 60 s (KL 5) | Abruf für einen Prospect → Brief in < 60 s. | testbar | (als Zielwert markiert, OK) |
| R14 | Quellenausfall → übrige Signale liefern, Lücke kennzeichnen (KL 5) | News-Quelle liefert Timeout → Brief mit Signalen aus den anderen Quellen + Hinweis „Quelle News nicht erreichbar". | testbar | – |
| R15 | Jeder Brief mit Quellen und Zeitstempel protokolliert (KL 5) | Nach Lauf → Log-Eintrag pro Brief mit allen Quell-URLs und Erstellungszeit. | testbar | (Aufbewahrungsdauer nicht genannt, für Test nicht nötig.) |

## Harte Regeln aus Features/Flows

| # | Regel (Quelle) | Testfall: Eingabe → erwartetes Verhalten | Status | Offene Frage |
|---|---|---|---|---|
| R16 | Beschäftigungs-Check vor dem Brief; ausgeschieden → Status *ausgeschieden* + Nachfolger-Vorschlag „wenn möglich" (Feature 2, Flow 2) | Kontakt laut Quelle seit September bei anderer Firma → Status *ausgeschieden*, keine Signal-Suche; Quelle nennt Nachfolger → Name + Link als Vorschlag. | teilweise | Woran wird ein Nachfolger erkannt (gleicher Titel, gleiche Firma, neu in den letzten X Tagen)? Ohne Treffer: leeres Feld oder Hinweis? |
| R17 | Signal-Suche nur für aktive Kontakte (Flow 3) | Kontakt *ausgeschieden* → kein Signal-Teil im Brief. | testbar | (*unsicher* siehe R9) |
| R18 | Priorisierung: starke, aktuelle Signale zuerst, „keine Signale" zuletzt (Feature 4) | Liste mit Prospects ohne Signale und mit Signalen → ohne Signale stehen am Ende. | offen | „Stark" ist nicht definiert: Ist Funding stärker als Hiring? Wie verrechnen sich Stärke und Alter? Wo stehen *ausgeschieden*/*unsicher*? |
| R19 | Bewertung nach Bezug zum Angebot des Kunden (Flow 4) | – | offen | Wo kommt „das Angebot des Kunden" her (Konfiguration pro Kunde, Freitext, Kategorien)? Wie wird „Bezug" gemessen? |
| R20 | Pro Prospect ein Aufhänger (Feature 1, Flow 4) | Prospect mit ≥ 1 Signal → genau 1 Aufhänger, der sich auf eines der gezeigten Signale bezieht. | testbar | – |
| R21 | Feedback per Klick „hilfreich / nicht hilfreich" (Flow 6) | Klick „nicht hilfreich" → Feedback mit Brief-ID, Rep, Zeitstempel gespeichert. | testbar | – |
| R22 | Feedback und Antwortquoten fließen in die Gewichtung der Signal-Typen (Flow 7) | – | offen | Gehört das zum MVP? Wenn ja: Mit welcher Regel ändert Feedback die Gewichte (pro Rep, pro Kunde, global; ab wie vielen Klicks)? Woher kommen Antwortquoten, wenn der Agent nichts versendet? |
| R23 | Auslieferungskanal: CRM-Notiz (Flow 5) vs. „Kanal wird im Kickoff festgelegt" (Flow 5) | Bau gegen CRM-Notiz → Notiz am Datensatz bis 8:00. | teilweise | Widerspruch im selben Flow-Schritt: Ist die CRM-Notiz gesetzt und E-Mail/Slack zusätzlich, oder ist der Kanal noch offen? |

## Zählung

- Regeln gesamt: **23** (15 aus Key Logic, 8 aus Features/Flows)
- testbar: 10 · teilweise (mit Annahme testbar): 7 · **offen: 6** (R2, R4, R9, R18, R19, R22)

## Urteil

Die Leitplanken (was nicht gezeigt wird, was der Agent nicht anfasst, Verhalten bei fehlenden Daten und Quellenausfall) sind sauber und direkt testbar. Offen ist dagegen der Kern der Logik: welche Signale zählen, wie sie bewertet und sortiert werden, und wann jemand als ausgeschieden gilt. Damit kann ich das Herzstück, Auswahl und Ranking, nicht bauen, ohne selbst Produktentscheidungen zu treffen.

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 „Logik ist baubar" | ❌ | 6 von 23 Regeln bleiben ohne formulierbaren Testfall offen, erlaubt ist höchstens 1. | (1) Abschließende Signal-Typ-Liste inkl. Operationalisierung von „about to go under"; (2) Relevanz-/Stärke-Formel für Auswahl der Top 3 und Sortierung der Tagesliste (Typ × Alter × Angebotsbezug, Tie-Break, Dedup); (3) Definition und Quelle von „Angebot des Kunden"; (4) Schwelle *ausgeschieden* vs. *unsicher* und Umgang mit *unsicher* in Signal-Suche und Ranking; (5) Lern-Regel für Feedback oder Klarstellung „nicht im MVP". |
