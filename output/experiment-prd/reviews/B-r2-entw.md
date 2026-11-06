# Review B, Runde 2: Entwickler

Rolle: der Entwickler, der das bauen soll. Grundlage: nur `output/experiment-prd/B-ausschnitt-logik.md` (Lösung, Ziele, Nicht-Ziele, Logik).

Vorgehen: Für jede Regel ein Testfall *Eingabe → erwartetes Verhalten*. Werte, die der PRD ausdrücklich als Konfiguration ausweist (*Annahme*, `[Platzhalter]` mit Startwert oder Konfigurationsparameter), teste ich parametrisch; das zählt nicht als offen. Offen ist eine Regel, wenn ich für einen realistischen Fall das erwartete Verhalten nicht ableiten kann.

## Testfälle: Regeln für den Bau (B1–B15)

| # | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|
| B1 | (a) Lead im CRM wird Vertriebler X zugewiesen → Dossier wird erzeugt. (b) Vertriebler klickt den Knopf am Kontakt-Datensatz → Dossier wird erzeugt. Lead ohne Zuweisung → kein Dossier. | ✅ testbar (Randfrage: Neu-Zuweisung eines Leads mit noch gültigem Dossier, neues Dossier oder nicht?) |
| B2 | Name + Firma + CRM-ID → Dossier am Datensatz. Name ohne Firma → ? Name + Firma ohne CRM-ID → Dossier entsteht, aber wohin? Beide Auslöser in B1 laufen über einen CRM-Datensatz, und B11 legt am Datensatz ab. | ❌ offen |
| B3 | Zwei „Max Muster" bei Beispiel AG, CRM-Titel „VP Ops" passt nur auf einen → Dossier für diesen. Zwei Treffer, kein unterscheidender Titel → kein Dossier, Hinweis *Person nicht eindeutig*. | ✅ testbar |
| B4 | Aktuelles Profil + Firmenseite bestätigen Rolle → *aktiv* mit Rolle und Beginn. Quelle belegt Wechsel, Nachfolger ohne Quelle → *nicht mehr im Unternehmen*, kein Name. Zwei Quellen widersprechen sich → *unsicher*, beide Angaben mit Quelle. Aber: Person wird gar nicht gefunden → welcher Zustand? Bei *unsicher*: werden Signale gesucht? Bei *nicht mehr im Unternehmen*: „keine Signale zur Person", werden Firmen-Signale (Funding) weiter gesucht, gibt es *Warum jetzt* und Aufhänger? | ❌ offen |
| B5 | 5 Treffer: 1 Funding, 2 Hiring, 1 Führungswechsel, 1 Thema → Funding, Hiring (neuestes), Hiring (zweitneuestes). 4 Funding-Treffer → die drei neuesten Funding-Signale. | ✅ testbar (Randfrage: Gleichstand im Datum) |
| B6 | Ein gültiges Signal → Dossier mit einem Signal. Null Signale → Rollen-Check + *Keine aktuellen Signale gefunden*, kein *Warum jetzt*, kein Aufhänger. | ✅ testbar |
| B7 | Themen-Signal 6 Tage alt → gültig; 8 Tage alt → entfällt. Führungswechsel 5 Monate → gültig; 7 Monate → entfällt. Funding/Hiring: gegen Konfigurationswert, parametrisch. Aber: Quelle ohne Datum (typisch: Stellenanzeige auf Karriereseite) → gültig oder nicht? Und „jünger als" gemessen ab Erstellzeitpunkt des Dossiers, ab Veröffentlichungs- oder Ereignisdatum? | ❌ offen |
| B8 | Kunde konfiguriert Themenliste [„Cloud Migration"] → Post zu „Cloud Migration" ist Signal, Post zu „ERP" nicht. Leere Liste → keine Themen-Signale. | ✅ testbar |
| B9 | Signal mit Link, der HTTP 200 liefert und das Signal belegt → bleibt. Link 404 oder kein Link → Signal entfällt. | ✅ testbar (Randfrage: Paywall-Link gilt als „erreichbar"?) |
| B10 | Quelle auf der Freigabeliste (frei zugänglich bzw. lizenzierte API) → wird genutzt. Quelle hinter Login ohne Freigabe → wird nicht abgefragt. LinkedIn: Freigabe als Konfigurationsschalter, den die Rechtsprüfung setzt. | ✅ testbar |
| B11 | Dossier erzeugt → am Lead- bzw. Kontakt-Datensatz in Salesforce gespeichert und sichtbar. Zweiter Kanal: Konfigurationsschalter, Standard aus. | ✅ testbar |
| B12 | Dossier mit Themen-Signal (7 Tage) und Funding-Signal → Ablauf = 7 Tage nach Erstellung, gedeckelt durch Maximalwert. Abgelaufenes Dossier wird geöffnet → Neuerstellung. Aber: Dossier ohne Signale (B6) hat kein „kürzestes Zeitfenster" → Ablaufdatum? Gilt das Zeitfenster ab Erstellung oder ab Alter des ältesten Signals? Sieht der Nutzer beim Öffnen das alte Dossier, bis das neue fertig ist? | ❌ offen |
| B13 | Agent versucht E-Mail-/Nachrichten-Versand → es existiert keine Schnittstelle, Berechtigungsprüfung zeigt keine Send-Rechte. | ✅ testbar |
| B14 | Arbeitssprache Deutsch konfiguriert, englische Quelle → Dossiertext deutsch, Zitat aus der Quelle englisch im Original. | ✅ testbar (Sprache als Konfiguration pro Kunde angenommen) |
| B15 | Dossier geöffnet um 10:00, erster Anruf 10:05 → „vor Kontakt geöffnet = ja". Anruf ohne vorheriges Öffnen → „nein". Aber: Woran erkennt der Agent den ersten Kontaktversuch? Welche CRM-Aktivitätstypen zählen (Call, E-Mail, LinkedIn-Nachricht außerhalb des CRM)? Kontakte, die nur über LinkedIn laufen („90% LinkedIn"), sind im CRM unsichtbar. | ❌ offen |

## Testfälle: harte Regeln in Lösung, Zielen, Nicht-Zielen

| # | Regel | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|---|
| H1 | Dossier-Inhalt (Rollen-Check, 2–3 Signale, *Warum jetzt*, Aufhänger, Quelle pro Signal, Zeitstempel) | Prospect mit 2 Signalen → alle sechs Bestandteile vorhanden, je Signal Link und Quelldatum, Erstellzeitpunkt gesetzt. Aber: *Warum jetzt* bezieht sich auf „das Angebot des Kunden". Woher kennt der Agent das Angebot? Anders als die Themenliste (B8) ist das nirgends als Konfiguration festgelegt. | ❌ offen |
| H2 | Stufe 2 nur, wenn Stufe 1 trägt | Projektentscheidung, kein Code. Prüfbar als Gate: Stufe 2 wird erst nach dokumentiertem Go aus dem Pilot begonnen. Die Go-Kriterien stehen im Plan, nicht im Ausschnitt. | ✅ prüfbar (Abhängigkeit zum Plan) |
| H3 | Nicht-Ziel: Rollen-Check nur für Prospects mit Dossier | Kontakt ohne Zuweisung und ohne Knopfdruck → kein Rollen-Check, kein Datensatz-Update. | ✅ testbar |
| H4 | Nicht-Ziel: kein automatischer Versand | identisch mit B13. | ✅ (über B13) |
| H5 | Z5 Leitplanke: kein Ausrollen bei Verletzung | Antwortquote Pilotgruppe < Vergleichsgruppe am Pilotende → Entscheidung „kein Ausrollen". | ✅ prüfbar |
| H6 | Z7 Qualität: Fehleranteil in Stichprobe | Stichprobe von n Dossiers (konfiguriert), Fehler = falsches Signal, falsche Rolle oder toter Link → Anteil berechnet, gegen Schwelle verglichen. | ✅ prüfbar (parametrisch) |

## Testfälle: Annahmen der Wirkungskette (L1–L6)

| # | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|
| L1 | Rechtsprüfung bestätigt keinen Zugriffsweg → No-Go. Bestätigt einen Weg, Spike liefert bei 75 % der Prospects zwei belegte Signale + korrekten Rollen-Check (Schwelle 70 %) → Go. 60 % → Quellen einschränken oder abbrechen. | ✅ prüfbar |
| L2 | Nutzungsquote aus B15 in der Pilotgruppe 72 % bei Schwelle 70 % → bestanden. Hängt an der offenen Definition des Kontaktversuchs (B15). | ✅ prüfbar (abhängig von B15) |
| L3 | Woche 1 vs. Pilotende: Recherchezeit sinkt und Calls steigen → bestanden; eines davon nicht → nicht bestanden. | ✅ prüfbar |
| L4 | identisch mit Z5 (H5). | ✅ prüfbar |
| L5 | Bewusst nicht Teil der Abnahme; Auswertung beim Kunden nach `[Platzhalter: Monate]`. Kein Testfall für den Bau nötig. | ✅ (bewusst ausgeschlossen) |
| L6 | Übergabe: 5 Bausteine (Funding, Hiring, Führungswechsel, Themen, Rollen-Check) dokumentiert übergeben → bestanden. | ✅ prüfbar |

## Offene Fragen

1. **B2 Eingabe ohne CRM-ID:** Wo wird ein Dossier ohne CRM-ID abgelegt, und welcher Auslöser erzeugt es, wenn beide Auslöser (B1) über einen CRM-Datensatz laufen? Was passiert bei fehlender Firma?
2. **B4 Rollen-Check:** Welcher Zustand, wenn die Person in keiner Quelle gefunden wird? Werden bei *unsicher* Signale gesucht? Gibt es bei *nicht mehr im Unternehmen* Firmen-Signale, *Warum jetzt* und Aufhänger?
3. **B7 Zeitfenster:** Wie wird eine Quelle ohne Datum behandelt (häufig bei Stellenanzeigen)? Ab welchem Zeitpunkt wird das Alter gemessen?
4. **B12 Aktualität:** Welches Ablaufdatum hat ein Dossier ohne Signale? Zählt das Fenster ab Erstellung oder ab Alter des Signals? Was sieht der Nutzer während der Neuerstellung?
5. **B15 Nutzungsprotokoll:** Welche Ereignisse gelten als „erster Kontaktversuch", und wie werden Kontakte außerhalb des CRM (LinkedIn) erfasst?
6. **H1 Warum jetzt:** Woher kommt „das Angebot des Kunden", gegen das die Relevanz bewertet wird? Konfiguration pro Kunde wie bei B8?

Randfragen ohne Einfluss auf das Urteil: Neu-Zuweisung (B1), Gleichstand im Datum (B5), Paywall-Links (B9).

## Urteil

27 Regeln geprüft (B1–B15, H1–H6, L1–L6), 21 testbar oder prüfbar, **6 offen**. Die Regeltabelle ist deutlich besser als üblich: Zustände, Reihenfolgen und Abbruchfälle sind fast überall festgelegt. Die Lücken liegen an den Rändern: fehlende Eingaben, fehlende Daten, leere Dossiers.

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 Logik ist baubar | ❌ | Sechs Regeln lassen für realistische Randfälle offen, was das System tun soll; erlaubt ist höchstens eine. | Ablage ohne CRM-ID (B2); Rollen-Zustand „nicht gefunden" und Signalsuche bei *unsicher*/*nicht mehr im Unternehmen* (B4); Umgang mit undatierten Quellen und Bezugspunkt des Zeitfensters (B7); Ablaufdatum für Dossiers ohne Signal (B12); Definition „erster Kontaktversuch" inkl. LinkedIn (B15); Quelle für „Angebot des Kunden" im *Warum jetzt* (H1). |
