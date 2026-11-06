# Review D, Runde 1: Entwickler-Sicht auf *Lösung* und *Logik*

Gelesen: nur `output/experiment-prd/D-ausschnitt-logik.md`. Rolle: der Entwickler, der das bauen soll.

**Ergebnis:** 17 Regeln (R1–R17), 17 offene Fragen, davon **0 blockierend**. Zu jeder Regel lässt sich ein Testfall formulieren. Die A-Werte (A7–A10) stehen nicht im Ausschnitt; die zugehörigen Tests sind deshalb parametrisiert (laut PRD sind sie konfigurierbar).

---

## 1. Testfälle je Regel

| Regel | Testfall (Eingabe → erwartetes Verhalten) | Offene Frage |
|---|---|---|
| R1 Pflichtfelder | a) Prospect mit Name, ohne Firma → Status `Eingabe unvollständig`, kein Dossier, keine CRM-Notiz, Meldung an den Auslösenden. b) Ohne Name, mit Firma → dasselbe. c) Im Stapel: ein unvollständiger Prospect → nur dieser fällt aus, der Rest des Stapels läuft weiter. | F12, F17 |
| R2 Rollen-Check | a) CRM: Firma X; Quelle: aktuell bei X → `bestätigt`, `rollen_quelle` gesetzt. b) CRM: X; Quelle: aktuell bei Y → `gewechselt`, `neue_firma` = Y. c) Keine Quelle findet die Person → `unklar`. d) Quelle 1: X, Quelle 2: Y → `unklar` (Annahme, siehe F1). e) Rollen-Check läuft vor der Anlass-Suche (Reihenfolge im Protokoll prüfbar). | F1, F2, F3, F16 |
| R3 Bei Wechsel | a) Wechsel X → Y; bei X hat Person P den Titel „vp sales“ (CRM-Titel „VP  Sales“) → `nachfolger_kandidat` = P mit Quelle; keine personenbezogenen Anlässe zu X; Anlass `neue Rolle` bei Y mit Datum des Rollenbeginns. b) Kein Titelmatch bei X → `nachfolger_kandidat` leer, Dossier trotzdem erzeugt. c) Rollenbeginn bei Y unbekannt → Anlass `neue Rolle` wird nach R7 verworfen. | F4, F5 |
| R4 Bei unklar | Status `unklar` → Dossier erzeugt, `warnhinweise` enthält *Rolle nicht bestätigt*, Hinweis steht oben im Dossier. | – |
| R5 Kategorien | a) Fund „Urlaubsfoto“ → verworfen. b) Fund „Series-B-Runde“ → `Finanzierung`. c) Stellenanzeige Marketing bei Konfiguration Engineering/Ops → verworfen. d) Neuer Director (nicht VP) → kein `Führungswechsel`. e) Beitrag zu einem Thema außerhalb der Kunden-Themenliste → verworfen. | F6 |
| R6 Zeitfenster | a) `Finanzierung` mit Alter A7 + 1 Tag → verworfen; Alter A7 − 1 Tag → behalten. b) `neue Rolle` Beginn vor 5 Monaten → behalten; vor 7 Monaten → verworfen. c) `Thema` von vor 8 Tagen → verworfen; vor 6 Tagen → behalten. Stichtag jeweils `erstellt_am`. | F6, F7 |
| R7 Quellenpflicht | a) Anlass ohne `datum` → nicht im Dossier. b) Ohne `quell_url` → nicht im Dossier. c) Ohne `belegauszug` → nicht im Dossier. d) `inhalt` behauptet eine Summe, die im `belegauszug` nicht steht → verworfen oder gekürzt. | F8 |
| R8 Auswahl | a) Fünf gültige Anlässe (2× Thema, 1× Finanzierung, 1× neue Rolle, 1× Führungswechsel) → Finanzierung, Führungswechsel, neue Rolle; beide Thema verworfen. b) Zwei Finanzierungsanlässe → der neuere zuerst. c) Kunde stellt Priorität um (Thema zuerst) → Auswahl folgt der Konfiguration. | – |
| R9 Null-Fall | Keine gültigen Funde → Dossier mit *Kein aktueller Anlass gefunden*, `aufhaenger` leer, Prospect-Markierung gesetzt; kein erfundener Ersatz (z. B. kein generisches Like). | F9 |
| R10 Aufhänger | a) Ein Anlass `Finanzierung` → Aufhänger nennt die Finanzierung ausdrücklich. b) Kein Anlass → kein Aufhänger (siehe R9). c) Es gibt in UI und API keinen Versand-Aufruf (negativer Test). | – |
| R11 Länge | a) Entwurf mit A9 + 50 Wörtern → gekürzt auf ≤ A9; alle `quell_url` bleiben erhalten. b) Entwurf ≤ A9 → unverändert. | F7, F10 |
| R12 Ausgabe | a) Status `bestätigt` → nur Notiz am Kontakt, keine Feldänderung (Feld-Diff vorher/nachher leer). b) Status `gewechselt` → Notiz plus Hinweis-Feld gesetzt, Feld *Firma* unverändert. | F11 |
| R13 Gültigkeit | a) Zweite Anfrage innerhalb A8 → gespeichertes Dossier mit Erstelldatum, kein neuer Quellenaufruf (Adapter-Log leer). b) Anfrage nach Ablauf von A8 → neuer Lauf. c) *Neu erzeugen* innerhalb von A8 → neuer Lauf. | F7, F14 |
| R14 Rückmeldung | Klick auf *falsch* an Anlass 2 → Markierung gespeichert, Anlass 2 im Dossier als falsch gekennzeichnet, G2-Zähler +1; zweiter Klick desselben Nutzers zählt nicht doppelt (Annahme). | F12, F17 |
| R15 Protokoll | a) Erzeugung → Eintrag mit Zeit, Nutzer, Auslöser (`einzeln`/`stapel`), `gepruefte_quellen`. b) Dossier geöffnet → Ereignis mit Zeitstempel. | F12 |
| R16 Quellen-Freigabe | a) LinkedIn-Adapter gesperrt → kein LinkedIn-Aufruf (Adapter-Log), Dossier aus den übrigen Quellen, Kopfzeile *LinkedIn nicht geprüft*. b) Alle Adapter gesperrt → Rolle `unklar`, Null-Fall nach R9. | F15, F16 |
| R17 Laufzeit | a) Einzel-Dossier → fertig innerhalb A10 (Zeit zwischen Auslöser und Notiz im Protokoll). b) Stapel mit allen für morgen zugeordneten Prospects, gestartet am Vorabend → alle Notizen liegen vor Arbeitsbeginn vor. | F7, F13 |

---

## 2. Offene Fragen

Keine ist **blockierend**: Zu jeder gibt es eine vernünftige Annahme, mit der ich anfangen kann. Die mit ⚠ markierten ändern bei falscher Annahme die Architektur oder den Kundenwert und sollten vor Sprint 1 entschieden sein.

| # | Regel | Frage | Einstufung | Meine Annahme bis zur Antwort |
|---|---|---|---|---|
| F1 | R2 | R2 widerspricht sich: „Andere aktuelle Firma in mindestens einer Quelle → `gewechselt`“ und „Quellen widersprechen sich → `unklar`“ greifen beide, wenn eine Quelle X und eine andere Y sagt. Was hat Vorrang? | *nicht blockierend* | `unklar` hat Vorrang. |
| F2 | R2 | Wie wird „gleiche Firma“ bestimmt (Acme Inc. vs. ACME GmbH, Tochterfirmen, Übernahmen)? | *nicht blockierend* | Normalisierter Name plus Web-Domain; Tochterfirma zählt als gleiche Firma. |
| F3 | R2, R16 | Wie wird sichergestellt, dass die Quelle dieselbe Person meint (Namensgleichheit)? Welche Mindest-Übereinstimmung? | *nicht blockierend* | Name + Firma (alt oder neu) + ähnlicher Titel; sonst `unklar`. |
| F4 | R3 | Mehrere oder kein Nachfolger-Kandidat? Titelvarianten („VP Sales“ vs. „Vice President, Sales“) fängt die Normalisierung (Kleinschreibung, Leerzeichen) nicht. | *nicht blockierend* | Höchstens ein Kandidat (jüngster Rollenbeginn); keiner → Feld leer; nur exakter Match nach Normalisierung. |
| F5 | R3 | Gibt es bei `gewechselt` auch firmenbezogene Anlässe der neuen Firma Y (Finanzierung, Neueinstellungen, Führungswechsel)? Und was zeigt das Dossier zur alten Firma X außer dem Nachfolger? | *nicht blockierend* | Ja, alle Kategorien für Y; zu X nur der Nachfolger-Kandidat. |
| F6 | R5, R6 | Kategorie-Definitionen: Zählen bei `Neueinstellungen` Stellenanzeigen oder nur gemeldete Einstellungen? Gilt `Führungswechsel` auch für C-Level? Ist `Thema` ein Beitrag der Person, der Firma oder beides? Wer pflegt die Themenliste, wie lautet sie zum Start? | *nicht blockierend* | Stellenanzeigen zählen; VP und C-Level; `Thema` nur Beiträge der Person; leere Themenliste → Kategorie aus. |
| F7 | R6, R11, R13, R17 | Startwerte A7 (Zeitfenster), A8 (Gültigkeit), A9 (Wortzahl), A10 (Laufzeit) stehen nicht im Ausschnitt. | *nicht blockierend* | Konfigurierbar, Tests parametrisiert; Werte aus dem Annahmen-Abschnitt übernehmen. |
| F8 | R7 | Wie wird geprüft, dass `inhalt` nur sagt, was im `belegauszug` steht: automatisch (zweiter Modellaufruf) oder durch Stichproben? Was passiert bei Verstoß: verwerfen oder umformulieren? | *nicht blockierend* | Automatischer Abgleich; bei Verstoß verwerfen. |
| F9 | R9 | „Prospect wird markiert“: wo? Ein CRM-Feld widerspräche R12 („Kontaktfelder werden nie überschrieben“). | *nicht blockierend* | Markierung nur im Dossier und im Protokoll, nicht am Kontakt. |
| F10 | R11 | In welcher Reihenfolge wird gekürzt? Was, wenn Kopfzeile, drei Anlässe und Quellen schon über A9 liegen? | *nicht blockierend* | Erst Aufhänger, dann `inhalt` der Anlässe kürzen; Quellen und Warnhinweise zählen nicht zur Wortzahl. |
| F11 ⚠ | R12 | „Hinweis-Feld“: Welches Feld? Es ist selbst ein Kontaktfeld und steht damit im Widerspruch zu „Kontaktfelder werden nie überschrieben“. Braucht es ein Custom Field (Admin-Freigabe beim Kunden)? Wird es beim nächsten Lauf (z. B. Rolle wieder `bestätigt`) zurückgesetzt? Und welcher Notiz-Typ in Salesforce (Notes, Task, eigenes Objekt)? | *nicht blockierend* | Eigenes Custom Field `Dossier-Hinweis`, nur vom Agent geschrieben, beim nächsten Lauf aktualisiert; Notiz als Salesforce Note (ContentNote). |
| F12 ⚠ | R1, R13, R14, R15 | Oberfläche: Eine CRM-Notiz ist statischer Text. Wo sind die Knöpfe *Dossier erzeugen*, *Neu erzeugen*, *falsch*, wo erscheint die Meldung aus R1, und wie wird „geöffnet“ gemessen (Notiz-Öffnungen protokolliert Salesforce nicht von sich aus)? Ohne Antwort sind R14, R15 und damit Z1, Z5, G2 nicht messbar. | *nicht blockierend* | Eine Komponente auf der Kontaktseite (Lightning Web Component) zeigt das Dossier, trägt die Knöpfe und protokolliert Öffnungen; die Notiz ist eine zusätzliche Textkopie. Das ist ein eigener Bauumfang. |
| F13 ⚠ | R17 | Stapel-Eingabe: Woran erkenne ich in Salesforce, welche Prospects einem Vertriebler „für den nächsten Arbeitstag zugeordnet“ sind (Tasks mit Fälligkeit, Listenansicht, Sequenz-Tool)? Wann ist „Arbeitsbeginn“, in welcher Zeitzone? Was passiert, wenn der Stapel bis dahin nicht fertig ist? | *nicht blockierend* | Offene Tasks des Owners mit Fälligkeit nächster Arbeitstag; Arbeitsbeginn je Nutzer konfigurierbar (Start 08:00 Ortszeit); Unfertiges läuft weiter, Protokoll meldet Verspätung. |
| F14 | R13 | Gilt das gespeicherte Dossier für alle Nutzer oder je Nutzer? Nutzt der Stapel ein noch gültiges Dossier wieder? Ersetzt *Neu erzeugen* die alte Notiz oder kommt eine weitere dazu? | *nicht blockierend* | Je Prospect für alle; Stapel nutzt gültige Dossiers wieder; neue Notiz, alte bleibt (CRM nur anhängen). |
| F15 | R16 | Adapter ist freigegeben, fällt aber aus (Timeout, Fehler): gleiche Behandlung wie gesperrt? | *nicht blockierend* | Dossier aus den übrigen Quellen, Warnhinweis *Quelle X nicht erreichbar*. |
| F16 ⚠ | R2, R16 | Solange LinkedIn gesperrt ist (*Offene Punkte* Nr. 1), woher kommt die aktuelle Firma einer Person? Firmenwebseiten und Presse nennen selten Einzelpersonen. Dann endet der Rollen-Check meist mit `unklar`, und Jenkins' Kernproblem bleibt ungelöst. | *nicht blockierend* (baubar, aber Wertrisiko) | Bauen mit Adapter-Schnittstelle; Anteil `unklar` im Pilot messen. |
| F17 | R1, R9, R12, R14 | Das Datenmodell enthält keine Felder für Status `Eingabe unvollständig` (R1), Null-Fall-Markierung (R9), Hinweis (R12) und *falsch*-Markierungen je Anlass mit Nutzer und Zeit (R14). | *nicht blockierend* | Felder ergänzen: `status`, `markiert_null_fall`, `anlaesse[].falsch_markiert[]`. |

**Zum Abgleich durch den Koordinator:** Alle 17 Fragen sind nicht blockierend und müssten unter *Offene Punkte* im PRD stehen. Im Ausschnitt sichtbar ist nur der Verweis auf *Offene Punkte* Nr. 1 (LinkedIn-Zugriff), passend zu F16. Für F1–F15 und F17 kann ich nicht sehen, ob sie dort stehen.

---

## 3. Urteil

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 „Logik ist baubar“ | ✅ | Jede der 17 Regeln hat einen formulierbaren Testfall, und keine der 17 offenen Fragen blockiert, weil es für jede eine vernünftige Annahme gibt. | Nichts Blockierendes. Vor Sprint 1 klären: F12 (Oberfläche für Knöpfe und Öffnungs-Messung; ohne sie sind R14, R15, Z1, Z5, G2 nicht messbar), F11 (Hinweis-Feld widerspricht „Felder nie überschreiben“), F13 (woran der Stapel die Prospects für morgen erkennt), F1 (Widerspruch innerhalb von R2), F16 (Rollen-Check ohne LinkedIn). Prüfen, ob alle 17 Fragen unter *Offene Punkte* stehen. |
