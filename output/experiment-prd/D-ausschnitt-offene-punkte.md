## Offene Punkte

Keine dieser Fragen blockiert den Bau. Jede hat eine Startannahme, die gilt, bis die Antwort da ist.

| # | Frage | Startannahme | Klärung |
|---|---|---|---|
| 1 | Zulässiger Zugriff auf LinkedIn, Datenschutz | Start ohne LinkedIn-Adapter, Freischaltung nach Rechtsprüfung (R16) | Phase 0, vor Go Phase 1 |
| 2 | Wer hat das Budget? | VP of Sales; kippt es, gilt Anhang A.5 | Phase 0 |
| 3 | Darf NeoEmployee in Salesforce ein eigenes Objekt und eine Komponente anlegen? Welcher Notiz-Typ, falls nicht? | Eigenes Dossier-Objekt plus Komponente (R12). Ohne Freigabe nur Text-Notiz; dann sind R14, Z5 und G2 nicht messbar | Phase 0 mit Kim |
| 4 | Ausgabekanal zusätzlich E-Mail oder Chat? | Nur Komponente im CRM | Phase 0 mit Kim und Nutzern |
| 5 | Wie wird Z1 gemessen? | Zeitstempel Aufruf des Kontakts bis zur ersten geloggten Aktivität (Call, E-Mail), gleich in beiden Gruppen | Messplan Phase 0 |
| 6 | Woran erkennt der Stapel die Prospects für morgen? | Offene Aufgaben des Nutzers, fällig am nächsten Arbeitstag; Zeiten A13 (R17) | Phase 0 |
| 7 | Wann ist es *dieselbe Firma* (Schreibweisen, Töchter)? | Normalisierter Name plus Web-Domain; Tochterfirma zählt als gleiche Firma | Phase 1 |
| 8 | Wann meint eine Quelle dieselbe Person? | Name plus Firma (alt oder neu) plus ähnlicher Titel, sonst zählt die Quelle für R2 nicht | Phase 1 |
| 9 | Mehrere oder kein Nachfolger-Kandidat, Titelvarianten? | Höchstens ein Kandidat (jüngster Rollenbeginn), keiner → Feld leer; nur Titel-Match nach Normalisierung, Liste der Titelvarianten in Phase 1 | Phase 1 |
| 10 | Anlässe bei `gewechselt`? | Alle Kategorien für die neue Firma; zur alten Firma nur der Nachfolger-Kandidat | Phase 0 |
| 11 | Kategorien, Themenliste, Priorität | O'Neils Checkliste. Stellenanzeigen zählen als `Neueinstellungen`; `Führungswechsel` ab VP inkl. C-Level; `Thema` nur Beiträge der Person; leere Themenliste → Kategorie aus | Phase 0 |
| 12 | Startwerte für Zeitfenster, Gültigkeit, Länge, Laufzeit | A7 bis A10, konfigurierbar, Tests parametrisiert | Pilot |
| 13 | Wie wird R7 geprüft (*`inhalt` nur aus dem Belegauszug*)? | Automatischer Abgleich von `inhalt` gegen `belegauszug`, bei Verstoß verwerfen; die Stichprobe (A14) prüft den Abgleich | Phase 1 |
| 14 | Reihenfolge beim Kürzen (R11) | Erst Aufhänger, dann `inhalt` der Anlässe; Quellen und Warnhinweise zählen nicht zur Wortzahl | Phase 1 |
| 15 | Gilt ein gespeichertes Dossier für alle Nutzer? Was passiert mit dem alten bei *Neu erzeugen*? | Je Prospect für alle; neuer Datensatz, der alte bleibt | Phase 1 |
| 16 | Zielwerte Z2 bis Z6, Mindest-Trefferquote | `[Platzhalter]`, mit dem Kunden | Phase 0 |
| 17 | Kaufmännisches: Tagessatz, Angebotssumme, Phase 0 berechnen | `[Platzhalter]`; Empfehlung in der Kurzfassung, Entscheidung beim Management von NeoEmployee | vor Phase 0 |
| 18 | Muster bei anderen Kunden | Frage an das Pattern-Team | nach N3 |

