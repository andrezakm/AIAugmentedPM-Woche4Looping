# PRD: Signal-Dossier-Agent

**Stand:** 2026-11-05 · **Grundlage:** Synthese `output/interview-synthesis-2026-11-03.md`, zehn Interviews in `input/`, `context/strategy.md`, `context/company.md`
**Zitat-Regeln:** Interview-Zitate stehen in englischen doppelten Anführungszeichen (wörtlich, Englisch), Strategie-Zitate in deutschen Anführungszeichen (wörtlich), eigene Umschreibungen *kursiv*. Zahlen ohne Quelle sind als *Annahme* oder *Schätzung* markiert oder stehen als `[Platzhalter]`.

---

## Kurzfassung

**Was wir bauen:** Einen KI-Agenten, der Ihren Vertrieblern zu jedem zugewiesenen Prospect ein kurzes Dossier ins CRM legt: höchstens drei aktuelle Anlässe zum Anrufen (Finanzierungsrunde, Wechsel in der Führung, Neueinstellungen, Themen, über die die Person gerade spricht), jeder mit Quellenlink und einem Vorschlag für den Einstieg ins Gespräch. Vorher prüft der Agent, ob die Person überhaupt noch bei der Firma arbeitet.

**Warum:** Ihre Leute verbringen heute einen großen Teil des Tages mit Recherche statt mit Gesprächen. Ihr VP Sales rechnet es selbst vor: "But does it really take 15 minutes per prospect? 15 minutes! If you do the math, that's only 4 prospects an hour. That's a joke." Ein SDR schafft 20 statt der geforderten 50 Calls am Tag, eine Top-AE recherchiert 4 Stunden am Abend für 10 Kontakte, und von 100 Marketing-Leads werden 5 mit Kontext bearbeitet, der Rest bleibt liegen.

**Was es bringt:** Recherche pro Prospect von heute 15 bis 40 Minuten auf unter zwei Minuten Lesezeit, so wie es Ihre Enablement-Leitung als Ziel formuliert. Dadurch mehr Gespräche pro Tag, ohne dass die persönliche Ansprache verloren geht. Der Vertriebler behält das Urteil, der Agent übernimmt das Suchen und Sortieren.

**Was es nicht ist:** Kein Tool, das selbst E-Mails verschickt. Kein Ersatz für Ihre Vertriebler. Keine Komplett-Bereinigung des CRM (das ist eine mögliche zweite Phase).

**Wie wir vorgehen:** Erst eine Woche messen, wie lange Recherche heute wirklich dauert. Dann ein Pilot mit einer kleinen SDR-Gruppe `[Platzhalter: Anzahl SDRs]`. Weiter geht es nur, wenn die Zeit sinkt und die Antwortquote nicht fällt.

**Aufwand und Preis:** Abrechnung nach Aufwand (Time & Material). MVP-Aufwand *Schätzung:* `[Platzhalter: Personenwochen nach Technik-Spike]`, Tagessatz `[Platzhalter]`.

**Was Sie entscheiden müssen:** (1) Freigabe des Piloten und der Pilotgruppe, (2) welche Datenquellen der Agent nutzen darf (vor allem LinkedIn, rechtlich zu klären), (3) wer auf Ihrer Seite Budget und Erfolgskennzahl verantwortet.

---

## Problem

**Wer leidet:** Alle, die bei unserem Kunden neue Kunden gewinnen sollen: Junior-SDRs, SDRs, Account Executives, Enterprise-AEs, erfahrene Verkäufer. Mittelbar leiden die Führungskräfte, deren Zahlen fehlen: Sales Director, VP Sales (der sich vor dem Board verantworten muss), Leitung Sales Enablement und das Marketing, dessen bezahlte Leads liegen bleiben.

**Woran sie leiden:** Bevor ein Vertriebler jemanden anruft oder anschreibt, braucht er einen *Grund, warum gerade jetzt*: Die Firma hat Geld eingesammelt, die Person ist neu im Job, die Firma stellt ein, die Person schreibt über ein passendes Thema. Diese Informationen sind öffentlich, aber über viele Webseiten verstreut. Jeder sucht sie heute von Hand zusammen und macht daraus einen Gesprächseinstieg. Der Sales Director beschreibt es so: "They’re jumping between five different tabs." Der VP Sales benennt den Kern: "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck."

Ohne diesen Grund zum Anrufen funktioniert die Ansprache nicht. Die Marketing-Managerin räumt ein: "conversion is higher if you know the context, I admit that—but it doesn't scale." Der erfahrenste Verkäufer sagt: "It feels like half the job is just staring at a screen trying to find an angle." Dazu kommt: Oft ist die Person gar nicht mehr bei der Firma. Laut einer SDR ist das "like 40% of the time" der Fall, und dann beginnt die Suche von vorn.

**Was es kostet** (Zahlen aus den Interviews):

| Wer | Was | Zitat |
|---|---|---|
| VP Sales | 15 Min. pro Prospect, also nur 4 pro Stunde | "If you do the math, that's only 4 prospects an hour." |
| Leitung Enablement | 40 Min. Recherche ohne Ergebnis bei neuen Leuten, verlängert die Einarbeitung | "suddenly forty minutes have passed and they haven't actually found a reason to call." / "It's a massive drain on our ramp time." |
| Junior-SDR | 30 Min. für eine einzige persönliche E-Mail | "But that took me 30 minutes to find. 30 minutes for one email!" |
| SDR | 20 statt 50 Calls am Tag | "I’m supposed to be making 50 calls a day. That's the KPI. But I’m lucky if I get to 20" |
| Top-AE | 4 Stunden am Abend für eine Liste von 10 Personen | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Enterprise-AE | Tage pro großem Account, Verhältnis 80 % Lesen zu 20 % Strategie | "It’s 80% reading LinkedIn profiles and 20% actual sales strategy." |
| Marketing | 5 von 100 Leads bekommen Kontext, 95 bleiben liegen, obwohl Marketing-Budget dafür ausgegeben wurde | "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |
| Sales Director | Die Abschlussstarken bekommen zu wenige Termine | "My guys are great closers, absolute sharks, but they’re starving, man." |

**Kurz gesagt:** Gut bezahlte Vertriebler arbeiten einen großen Teil ihrer Zeit als Rechercheure. Darum gibt es zu wenige Gespräche, zu wenige Termine und zu viele ungenutzte Leads. Wer schneller wählen soll, verliert die persönliche Ansprache, und wer persönlich ansprechen will, schafft das Volumen nicht. Der Sales Director fasst das Dilemma zusammen: "I want speed, they want quality, and right now we have neither."

---

## Warum dieses Problem (Wahl und Strategie)

### Die Wahl

Die Synthese liefert zwei Bedürfnisse:

- **Bedürfnis 1 (gewählt):** *Der Grund zum Anrufen kommt fertig aufbereitet beim Vertriebler an.* Laut Synthese in 9 von 10 Interviews genannt.
- **Bedürfnis 2:** *Kontaktdaten sind aktuell, verifiziert und landen ohne Handarbeit im CRM.* Laut Synthese in 5 von 10 Interviews genannt.

**Entscheidung: Bedürfnis 1 hat die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs.** Es gewinnt in allen fünf durchgerechneten Gewichtungen (Anhang A). Die Gründe in einem Satz je Punkt:

1. **Breiter und höher aufgehängt:** Es betrifft fast alle Befragten und mehrere Führungskräfte mit Zahlenverantwortung (VP Sales, Sales Director, Leitung Enablement, Marketing), nicht nur eine Funktion.
2. **Direkter Umsatzhebel beim Kunden:** Die Betroffenen beziffern den Effekt selbst. Die Top-AE: "I'd double my numbers." Der VP Sales: "just hand them the dossier—we’d be unstoppable." Damit ist das Projekt für den Kunden leicht zu rechtfertigen, und das ist für uns die Voraussetzung, dass bezahlt wird.
3. **Weniger Konkurrenz durch vorhandene Tools:** Für Bedürfnis 2 gibt es beim Kunden bereits ZoomInfo und Clearbit. Die liefern Rohdaten, aber keinen fertigen Gesprächsaufhänger. Für Bedürfnis 1 zahlt der Kunde heute nur mit der Zeit seiner Leute.

**Schicksal von Bedürfnis 2: MVP-Baustein, Rest in Phase 2.** Ein Dossier über jemanden, der die Firma verlassen hat, ist wertlos (Baker: "No, he left six months ago, look at his LinkedIn!"). Darum prüft der Agent als ersten Schritt, ob Arbeitgeber und Titel noch stimmen, und schreibt Änderungen ins CRM (Regel L2, L9). Die vollständige Datenpflege, also E-Mail-Verifikation, Bereinigung aller Bestandskontakte und Nachfolger-Suche, geht als eigener Folgeauftrag an Sales Ops (Phase 2). Das hält den Käufer von Bedürfnis 2 (Sales Ops Manager David Kim) im Spiel, ohne den Pilot zu überladen.

### Belegt mit wörtlichen Zitaten von mindestens vier Personen

| Person | Rolle | Budget- oder Zahlenverantwortung | Zitat |
|---|---|---|---|
| Marcus Thorne | VP of Sales | verantwortet die Zahlen vor dem Board ("I had a meeting with the board this morning") | "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck." |
| Emily Blunt | Marketing Manager | **eigenes Budget** ausdrücklich genannt: "We spend serious budget—my budget—getting these people into the funnel" | "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |
| Linda O'Neil | Director of Sales Enablement | verantwortet die Einarbeitungszeit | "The problem isn't that the data is missing; it's that they have to sift through so much irrelevant noise to find those three specific things." |
| Mike Ross | Sales Director | führt das Vertriebsteam | "So they spend 20 minutes reading the guy’s posts about his dog or his vacation to Cabo just to write one email." |
| Sarah Jenkins | SDR | – | "It feels like I'm fishing without bait." |
| Rachel Green | Junior SDR | – | "But that took me 30 minutes to find. 30 minutes for one email!" |
| Jessica Chen | Account Executive | – | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Sam Petit | Enterprise AE | – | "I spend days—literal days—just mapping an account" |
| Tom Baker | Senior Sales Rep | – | "It feels like half the job is just staring at a screen trying to find an angle." |

### Nachweis Strategie

| Prüfung | Satz aus `context/strategy.md` | Begründung |
|---|---|---|
| **S1 Vision-Filter** | „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills. We do not chase work outside that frame.“ | Der Agent ersetzt einen klar abgrenzbaren Skill: den *Prospect-Researcher*. O'Neil beschreibt ihn selbst: "We’re essentially teaching them to be high-priced data miners." Es ist kein Reporting, kein Lizenzkauf und keine Organisationsberatung, sondern genau die Arbeit, die heute ein Mensch von Hand macht. |
| **S2 Umsatz** | „every deal we close extends how long we can operate and invest in the product path.“ | Es gibt Schmerz mit Zahlen bei Führungskräften, die Budget haben oder Zahlen verantworten (Thorne vor dem Board, Blunt mit eigenem Budget, O'Neil mit Ramp-Zeit). Das macht den Auftrag jetzt verkaufbar, und zwar im heutigen Modell: „Every engagement is scoped and billed individually.“ Ein messbarer Pilot mit klarer Weiter-Entscheidung senkt die Hürde für den ersten Auftrag. |
| **S3 Muster** | „Their job is to identify recurring patterns — skills, workflows, and agent types that appear across multiple clients in different industries.“ | Die Signal-Typen sind nicht kundenspezifisch: O'Neils Checkliste (Funding, Hiring, Führungswechsel) gilt für jede B2B-Vertriebsorganisation, die auf öffentlichen Signalen prospektiert. **Einschränkung:** Alle zehn Interviews stammen aus *einer* Organisation. Das Muster über mehrere Kunden ist noch nicht belegt. Darum bauen wir die Bausteine (Signal-Katalog, Quellen-Adapter, Ranking) getrennt vom kundenspezifischen Teil (CRM-Felder, Ton der Einstiegssätze), damit die Pattern-Leute sie bei weiteren Kunden prüfen können. |

---

## Lösung

Ein Agent, der für einen Prospect (Person plus Firma) automatisch ein **Signal-Dossier** erstellt und im CRM am Kontakt ablegt. Das Dossier enthält:

1. **Status-Check:** Arbeitet die Person laut öffentlichem Profil noch bei der Firma, mit welchem Titel? (MVP-Baustein aus Bedürfnis 2)
2. **Bis zu drei Signale**, nach Relevanz sortiert, aus einem festen Katalog: Finanzierungsrunde, Führungswechsel, Neueinstellungen in relevanten Bereichen, neu in der Rolle, Themen, über die die Person öffentlich spricht. Jedes Signal mit Datum und Quellenlink.
3. **Ein Einstiegsvorschlag pro Signal:** ein bis zwei Sätze, die der Vertriebler übernehmen, ändern oder verwerfen kann.
4. **Bewertungsknopf** *brauchbar / nicht brauchbar*, damit wir messen, ob das Dossier hilft.

Der Agent ersetzt das Zusammensuchen und Sortieren, **nicht das Urteil**. Die Erfahrenen wollen die Deutung behalten. Petit: "You have to read between the lines, check their history, see what they actually talk about." Der Agent verschickt nichts.

### Alternativen

| # | Lösungsalternative | Warum nicht |
|---|---|---|
| A1 | **Mehr Lizenzen für vorhandene Daten-Tools** (ZoomInfo, Sales Navigator) | Die Tools liefern Rohdaten, nicht den fertigen Aufhänger. O'Neil: "The problem isn't that the data is missing". Kim: Die Tools "break, or they’re too expensive to run on every single contact record." Strategisch: Lizenzkauf ersetzt keinen Skill durch einen Agenten und bringt uns keinen Umsatz (S1, S2). |
| A2 | **Bessere Checklisten und Training** | Ist beim Kunden schon im Einsatz und reicht nicht: O'Neil gibt den Neuen strikte Checklisten, trotzdem vergehen "forty minutes" ohne Ergebnis. Strategisch: Training ist kein Agent (S1). |
| A3 | **Vollautomatischer Outreach-Agent**, der Signale findet und E-Mails selbst verschickt | Gefährdet genau das, was die Ansprache wirksam macht. Ross: Das Team "insist it's the only way to get a response", gemeint ist die persönliche Recherche. Green empfindet schon heute generische Aufhänger als unecht: "It feels a bit fake, honestly." Risiko für die Antwortquote ist zu hoch für einen ersten Auftrag. |
| A4 | **Komplett-Anreicherung aller CRM-Kontakte auf Vorrat** | Kim nennt genau das als zu teuer ("too expensive to run on every single contact record"). Das Dossier entsteht deshalb nur bei Bedarf, wenn ein Lead zugewiesen oder angefragt wird (Regel L1). |

### Vorher und nachher

**Vorher** (jede Szene steht so in einem Interview):

- Eine Junior-SDR sucht im Netz nach einem persönlichen Aufhänger, findet einen Thread über Sauerteigbrot, schreibt darüber und bekommt eine Antwort. Dauer: "30 minutes for one email!" (Green)
- Eine SDR hat Salesforce auf dem einen Bildschirm und LinkedIn im anderen Tab, prüft, ob die Person noch dort arbeitet, und kopiert Titel von Hand ins CRM. Ergebnis: 20 statt 50 Calls am Tag. (Jenkins)
- Ein neuer Vertriebler klickt von einem Artikel zum Autorenprofil zu alten Fotos, und nach "forty minutes" hat er keinen Grund zum Anrufen gefunden. (O'Neil)
- Die beste AE sitzt nach Feierabend 4 Stunden am Rechner, um 10 Kontakte für den nächsten Tag vorzubereiten. (Chen)

**Nachher** (*illustrativ*, so soll es im Pilot aussehen):

- *Illustrativ:* Die SDR öffnet morgens ihre zugewiesenen Leads. Bei jedem liegt ein Dossier. Bei einem steht: Person hat die Firma verlassen, Nachfolger im CRM als neuer Kontakt angelegt. Bei einem anderen: Firma hat eine Finanzierungsrunde gemeldet, Link zur Meldung, Einstiegsvorschlag. Sie liest, passt den Satz an und ruft an.
- *Illustrativ:* Der neue Vertriebler muss nicht mehr lernen, wie man sucht. Die Einarbeitung kann sich, wie O'Neil es sich wünscht, auf Gesprächsführung und Einwandbehandlung konzentrieren.
- *Illustrativ:* Die AE bekommt ihre Liste neu ernannter Entscheider bei frisch finanzierten Firmen, ohne Abendschicht.

---

## Ziele

Alle Ausgangswerte werden in Woche 1 beim Kunden gemessen. Zahlen aus den Interviews dienen als erste Orientierung.

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| Z1 | Recherche wird kurz | Zeit vom Öffnen eines Leads bis zum Start des Kontakts | laut Interviews 15 Min. (Thorne), 30 Min. (Green), bis 40 Min. (O'Neil); genau: `[Platzhalter: messen in Woche 1]` | unter zwei Minuten (O'Neils Formulierung "can you find it in under two minutes?") | Ende des Piloten `[Platzhalter: Pilotdauer]` |
| Z2 | Mehr Gespräche | Calls bzw. Erstkontakte pro SDR und Tag | 20 laut Jenkins, KPI 50; genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter: mit Kunde vereinbaren]` | Ende des Piloten |
| Z3 | Mehr Leads werden bearbeitet | Anteil der zugewiesenen Leads, die innerhalb `[Platzhalter: Frist]` kontaktiert werden | 5 von 100 laut Blunt; genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter: mit Kunde vereinbaren]` | Ende des Piloten |
| Z4 | Das Dossier hilft | Anteil Dossiers, die der Vertriebler als *brauchbar* markiert | 0 (gibt es heute nicht) | `[Platzhalter: Schwelle für Weiter-Entscheidung]` | wöchentlich ab Pilotstart |

**Guardrails** (dürfen nicht schlechter werden):

| # | Guardrail | Ausgangswert | Grenze | Messzeitpunkt |
|---|---|---|---|---|
| G1 | **Antwortquote** auf Erstkontakte (die persönliche Ansprache darf nicht leiden) | `[Platzhalter: messen in Woche 1]` | darf nicht unter den Ausgangswert fallen | wöchentlich ab Pilotstart |
| G2 | **Kontakte, die nicht mehr da sind** (Bounces, "Who?"-Anrufe) | laut Jenkins "like 40% of the time"; genau: `[Platzhalter: messen in Woche 1]` | darf nicht steigen | wöchentlich |
| G3 | **Signale ohne Beleg** | 0 | bleibt 0 (Stichprobe `[Platzhalter: Umfang]` pro Woche) | wöchentlich |

**Für NeoEmployee:** T&M-Umsatz aus Pilot und Ausbau `[Platzhalter: Volumen nach Angebot]`, plus ein wiederverwendbarer Signal-Baustein für die Pattern-Prüfung bei weiteren Kunden.

---

## Nicht-Ziele

| Nicht-Ziel | Warum nicht | Wohin |
|---|---|---|
| E-Mails oder Sequenzen automatisch verschicken | Risiko für die Antwortquote (Alternative A3), der Vertriebler behält das Urteil | frühestens Phase 2, nur wenn G1 im Pilot stabil bleibt |
| Komplette CRM-Bereinigung, E-Mail-Verifikation, Nachfolger-Suche für alle Bestandskontakte | Das ist Bedürfnis 2 in voller Breite, anderer Käufer (Sales Ops), würde den Pilot überladen | Phase 2, eigener Auftrag mit Sales Ops |
| Enterprise-Account-Mapping (Organigramm, Beziehungsnetz, wie Petit es beschreibt) | Andere, deutlich schwerere Aufgabe als Einzelsignale; Petit braucht Beziehungen, nicht drei Anlässe | Phase 2 |
| Gemeinsame Lead-Definition zwischen Marketing und Sales | Organisationsfrage, kein ersetzbarer Skill; fällt durch den Vision-Filter (S1) | nie (nicht unser Auftragsfeld) |
| Ersatz oder Einkauf von ZoomInfo, Sales Navigator & Co. | Lizenzkauf, kein Agent (S1), kein Umsatz für uns | nie |
| Reporting- und Attributions-Dashboard für die Führung | Die Logs des Agenten (Regel L10) liefern die Daten nebenbei, ein eigenes Dashboard ist nicht nötig für den Pilot | Phase 2, wenn der Kunde es verlangt |
| Produkt für viele Kunden | Laut Strategie sind wir noch Custom-Dienstleister, das Muster über Kunden ist unbelegt | Pattern-Team prüft; Entscheidung frühestens nach weiteren Kunden |

---

## Logik

Begriffe: **Prospect** = Kontakt im CRM mit Name, Firma, Titel. **Dossier** = Ergebnis des Agenten am Kontakt. **Signal** = ein datiertes, belegtes Ereignis aus dem Signal-Katalog.

| # | Regel | Eingabe → erwartetes Verhalten |
|---|---|---|
| L1 | **Auslöser.** Ein Dossier entsteht, wenn ein Kontakt einem Vertriebler zugewiesen wird oder wenn der Vertriebler es per Knopf anfordert. Es gibt keinen Lauf über alle Kontakte. | Kontakt wird zugewiesen → Dossier-Job startet. Kontakt ohne Zuweisung und ohne Anfrage → kein Job. |
| L2 | **Status-Check zuerst.** Der Agent vergleicht Arbeitgeber und Titel im CRM mit der öffentlichen Quelle. (a) Gleich → weiter mit L3. (b) Titel anders, Arbeitgeber gleich → Titel nach L9 aktualisieren, weiter mit L3. (c) Arbeitgeber anders → kein Dossier für die alte Firma; Kontakt als *gewechselt* markieren, neuen Arbeitgeber eintragen (L9), Hinweis an den Vertriebler. (d) Keine öffentliche Quelle gefunden → Dossier mit Vermerk *Status nicht geprüft*, weiter mit L3. | CRM nennt Oracle als Arbeitgeber, Profil nennt eine andere Firma → Status *gewechselt*, kein Signal-Teil, Hinweis erscheint. |
| L3 | **Signal-Katalog (fest im MVP).** Erlaubte Signal-Typen: (1) Führungswechsel auf VP-Ebene oder höher, (2) Person ist neu in der Rolle, (3) Finanzierungsrunde, (4) Neueinstellungen in Engineering oder Operations, (5) Person hat öffentlich über ein Thema aus der Themenliste des Kunden geschrieben. Andere Fundstücke (Urlaub, Hobbys, private Fotos) werden nicht als Signal ausgegeben. | Post über Urlaub → kein Signal. Meldung über Finanzierungsrunde → Signal Typ 3. |
| L4 | **Aktualität.** Ein Signal zählt nur, wenn sein Datum innerhalb eines Fensters liegt. Startwert (*Annahme*): 90 Tage, pro Signal-Typ konfigurierbar. *Neu in der Rolle* (Typ 2) gilt bis 6 Monate nach Start, wie Chen es nutzt ("less than 6 months"). | Finanzierungsmeldung vor 30 Tagen → Signal. Vor 200 Tagen → kein Signal. |
| L5 | **Höchstens drei Signale.** Gibt es mehr, wird nach Typ sortiert (Reihenfolge wie in L3, *Annahme*, mit Kunde in Woche 1 bestätigen), bei gleichem Typ das neuere zuerst. Grundlage für die Grenze drei: O'Neil, "those three specific things". | Fünf gültige Signale → die drei mit höchstem Rang erscheinen, zwei werden verworfen und geloggt. |
| L6 | **Kein Signal ohne Beleg.** Jedes Signal braucht Quellen-URL und Datum. Fehlt eines davon, wird das Signal nicht angezeigt. Der Agent erfindet keine Fakten und schließt nicht auf Fakten, die nicht in der Quelle stehen. | Fund ohne URL → nicht im Dossier, im Log als *verworfen: ohne Beleg*. |
| L7 | **Einstiegsvorschlag.** Pro Signal ein Vorschlag mit höchstens zwei Sätzen, der nur das belegte Signal verwendet. Er ist als *Vorschlag* gekennzeichnet und wird nie automatisch verschickt. | Signal Finanzierungsrunde → Vorschlag nennt die Runde, enthält keine weiteren Behauptungen. Kein Versand-Knopf am Vorschlag. |
| L8 | **Kein Signal gefunden.** Das Dossier sagt ausdrücklich *kein aktuelles Signal gefunden*. Es gibt dann keinen Einstiegsvorschlag. | Kontakt ohne gültige Signale → Dossier mit diesem Vermerk, Vorschlagsfeld leer. |
| L9 | **Schreiben ins CRM.** Dossier wird als Notiz bzw. eigenes Feld am Kontakt gespeichert. Titel und Arbeitgeber werden bei Abweichung (L2) automatisch aktualisiert; der alte Wert bleibt in der Feld-Historie, Quelle und Zeitpunkt werden mitgeschrieben. E-Mail-Adressen und alle anderen Felder ändert der Agent nicht. | Titel weicht ab → Feld aktualisiert, Historie zeigt alten Wert, Quelle und Zeitpunkt. E-Mail-Feld bleibt unverändert. |
| L10 | **Protokoll.** Pro Dossier werden geloggt: genutzte Quellen, gefundene und verworfene Signale mit Grund, Laufzeit, Bewertung des Vertrieblers (*brauchbar / nicht brauchbar*). | Dossier erstellt und bewertet → Log-Eintrag mit allen Feldern vorhanden. |
| L11 | **Laufzeit.** Das Dossier liegt vor, bevor der Vertriebler den Lead bearbeitet. Ziel für die Erstellung (*Annahme*): unter zwei Minuten nach Auslöser. Dauert es länger, zeigt das CRM *Dossier in Arbeit*. | Lead geöffnet, Job läuft noch → Anzeige *Dossier in Arbeit*. |

**Offene Frage für die Entwicklung:** Welche öffentlichen Quellen der Agent technisch und rechtlich nutzen darf, vor allem LinkedIn (L2, L3). Siehe Offene Punkte, O1.

---

## Plan

| Phase | Inhalt | Ergebnis / Entscheidung | Dauer |
|---|---|---|---|
| 0: Klären | Datenquellen und Rechtslage klären (O1), CRM-Zugang, Pilotgruppe festlegen, Signal-Reihenfolge und Themenliste mit dem Kunden bestätigen | Go/No-Go für den Bau | `[Platzhalter]` |
| 1: Messen | Ausgangswerte für Z1–Z3 und G1–G2 in der Pilotgruppe erheben | Baseline steht | Woche 1 |
| 2: MVP bauen | Regeln L1–L11, Status-Check, Signal-Katalog, CRM-Anbindung | lauffähiger Agent in der Testumgebung | *Schätzung:* `[Platzhalter: Personenwochen nach Technik-Spike]` |
| 3: Pilot | Pilotgruppe `[Platzhalter: Anzahl SDRs]` nutzt die Dossiers im Alltag, wöchentliche Messung | Weiter-Entscheidung anhand Z1–Z4 und G1–G3 | `[Platzhalter: Pilotdauer]` |
| 4: Ausbau oder Stopp | Ausrollen auf das Team; Angebot Phase 2 (Datenpflege mit Sales Ops, Account-Mapping) | Folgeauftrag | `[Platzhalter]` |

**Abbruchregel für den Piloten:** Fällt G1 (Antwortquote) unter den Ausgangswert oder enthält eine Stichprobe ein Signal ohne Beleg (G3), wird der Pilot angehalten und nachgebessert, bevor er weiterläuft.

**Parallel (für NeoEmployee):** Das Pattern-Team bekommt Signal-Katalog und Ergebnisse, um zu prüfen, ob das Muster bei Kunden aus anderen Branchen auftritt.

---

## Risiken und Einwände

| # | Einwand oder Risiko | Antwort | Status |
|---|---|---|---|
| R1 | ***Das wird generisch, die persönliche Note geht verloren.*** Ross: "I want speed, they want quality, and right now we have neither." | Der Agent liefert Signale und einen Vorschlag, der Vertriebler entscheidet und formuliert. Kein Versand (L7). Private Fundstücke sind ausgeschlossen (L3). Die Antwortquote ist Guardrail G1 mit Abbruchregel. | beantwortet, im Pilot zu belegen |
| R2 | **Datenzugang und Recht** (LinkedIn-Nutzungsbedingungen, Datenschutz bei personenbezogenen öffentlichen Daten) | Noch nicht geklärt. Ohne geklärten Zugang zu LinkedIn sinkt der Nutzen stark, weil fast alle Befragten LinkedIn als Hauptquelle nennen (Kim: "It’s 90% LinkedIn."). Phase 0 klärt das vor dem Bau. | **offen**, siehe O1 |
| R3 | ***Lohnt sich das, wir zahlen doch schon für ZoomInfo?*** | ZoomInfo liefert Kontaktdaten, nicht den Grund zum Anrufen; die Recherche-Zeit entsteht trotz vorhandener Tools. Der Pilot misst den Effekt gegen die eigene Baseline, bevor mehr Geld fließt. Preis und Aufwand: `[Platzhalter]`. | beantwortet bis auf Preis (O3) |
| R4 | **Falsche oder erfundene Signale** schaden dem Ruf des Vertrieblers im Gespräch (Baker: "It was embarrassing. I looked like a dinosaur.") | Kein Signal ohne Quelle und Datum (L6), keine Schlüsse über die Quelle hinaus (L6), wöchentliche Stichprobe (G3). | beantwortet |
| R5 | **Veraltete Kontakte** machen das Dossier wertlos | Status-Check vor jedem Dossier (L2), Guardrail G2. | beantwortet |
| R6 | **Die Leute nutzen es nicht** (Thorne: Das Team will "every data point verified") | Jedes Signal hat einen Link zur Quelle, das Dossier liegt im CRM statt in einem neuen Tool, Nutzung wird gemessen (Z4). | im Pilot zu belegen |
| R7 | **Für NeoEmployee: Muster nur bei einem Kunden belegt** | Bau als T&M-Auftrag, der sich allein trägt (S2). Produktentscheidung erst nach Prüfung durch das Pattern-Team (S3). | bewusst offen |
| R8 | **Erfahrene Vertriebler (Enterprise) brauchen mehr als drei Signale** | Stimmt (Petit). Account-Mapping ist ausdrücklich Nicht-Ziel und Phase 2. | abgegrenzt |

---

## Offene Punkte

| # | Punkt | Wer entscheidet | Bis wann |
|---|---|---|---|
| O1 | Welche Quellen darf der Agent technisch und rechtlich nutzen, insbesondere LinkedIn? (offene Frage der Entwicklung zu L2/L3) | Kunde (Recht/Datenschutz) mit NeoEmployee | Ende Phase 0 |
| O2 | Wer auf Kundenseite ist Budget-Owner und verantwortet die Erfolgskennzahl: VP Sales, Sales Director oder Sales Ops? | Kunde | vor Angebot |
| O3 | Tagessatz, Aufwand und Budgetrahmen für Pilot und Ausbau | NeoEmployee-Geschäftsführung (kaufmännische Zusage, nicht vom PM) | vor Angebot |
| O4 | Größe der Pilotgruppe, Pilotdauer, Zielwerte für Z2–Z4 | Kunde mit NeoEmployee | Phase 0 |
| O5 | Bestätigung der Signal-Reihenfolge (L5), des Aktualitätsfensters (L4) und der Themenliste (L3) | Kunde (Enablement, O'Neil) | Woche 1 |
| O6 | Welches CRM-Objekt bzw. Feld nimmt das Dossier auf (Salesforce laut Jenkins) | Sales Ops (Kim) | Phase 0 |

---

## Anhang A: Bewertung der Bedürfnisse

**Methode:** Beide Bedürfnisse der Synthese werden auf sieben Kriterien von 1 (schwach) bis 5 (stark) bewertet. Die Punkte sind eine *eigene Bewertung des Autors* auf Basis der Interviews und der Strategie, keine gemessenen Werte. Die Gewichtungen sind *Annahmen*, darum werden fünf verschiedene durchgerechnet.

### Bewertung je Kriterium

| # | Kriterium | B1: Grund zum Anrufen | Begründung B1 | B2: Kontaktdaten aktuell im CRM | Begründung B2 |
|---|---|---|---|---|---|
| K1 | **Verbreitung** | 5 | laut Synthese 9 von 10 Personen, alle Ebenen von Junior-SDR bis VP | 3 | laut Synthese 5 von 10, vor allem SDR, AE und Ops |
| K2 | **Belegte Kosten** | 5 | viele unabhängige Zahlen: 15 Min., 30 Min., 40 Min., 4 Std. für 10 Kontakte, 20 statt 50 Calls, 5 von 100 Leads | 4 | starke, aber weniger Zahlen: "like 40% of the time", 2 Std. pro Tag, 80k $ Gehalt |
| K3 | **Budget-Owner mit Schmerz jetzt (S2)** | 4 | mehrere Führungskräfte mit Druck (Thorne vor dem Board, Blunt mit eigenem Budget, O'Neil mit Ramp-Zeit); kein Befragter nennt aber ausdrücklich ein Budget für genau diese Lösung | 4 | ein klarer Owner (Kim, verantwortet den Stack), Kosten stehen in seiner eigenen Rechnung; nur ein Käufer |
| K4 | **Abstand zu vorhandenen Tools** | 4 | kein vorhandenes Tool liefert den fertigen Aufhänger; Wettbewerber ist die Handarbeit | 2 | ZoomInfo und Clearbit sind beim Kunden schon für genau diese Aufgabe gekauft; unser Vorteil ist nur, dass sie laut Kim "break" und zu teuer sind |
| K5 | **Umsatzhebel beim Kunden** | 5 | direkt mehr Gespräche und Termine; Chen: "I'd double my numbers." Ross: Closer "starving" | 4 | Jenkins: "if I didn't have to verify every single lead, I could double my quota"; wirkt aber eher über eingesparte Zeit als über bessere Gespräche |
| K6 | **Muster- und Produktpotenzial (S3)** | 4 | generische Signal-Typen, jede B2B-Vertriebsorganisation; nur bei einem Kunden belegt | 3 | generisch, aber in einem Markt mit etablierten Anbietern schwer als eigenes Produkt zu positionieren |
| K7 | **Umsetzbarkeit / geringes Risiko** | 3 | Synthese-Qualität und Halluzinationen sind ein echtes Risiko, Datenzugang offen | 4 | einfachere Logik (Abgleich von Feldern), gleicher offener Datenzugang |

### Fünf Gewichtungen

Rechnung: Summe aus Punkte × Gewicht, geteilt durch die Summe der Gewichte.

| Gewichtung | Gewichte K1–K7 | B1 | B2 | Ergebnis |
|---|---|---|---|---|
| **G-a Gleich** | 1-1-1-1-1-1-1 (Summe 7) | 30 / 7 = **4,29** | 24 / 7 = **3,43** | B1 |
| **G-b Runway zuerst (S2)** | 1-2-3-1-3-1-1 (Summe 12) | 53 / 12 = **4,42** | 44 / 12 = **3,67** | B1 |
| **G-c Produkt zuerst (S3)** | 2-1-1-2-1-3-1 (Summe 11) | 47 / 11 = **4,27** | 35 / 11 = **3,18** | B1 |
| **G-d Risiko zuerst** | 1-1-1-2-1-1-3 (Summe 10) | 40 / 10 = **4,00** | 34 / 10 = **3,40** | B1 |
| **G-e Sicht Sales Ops** (Verbreitung egal, Budget und Umsetzbarkeit dreifach) | 0-1-3-1-1-1-3 (Summe 10) | 39 / 10 = **3,90** | 37 / 10 = **3,70** | B1, knapp |

**Rechenweg G-b als Beispiel:** B1 = 5×1 + 5×2 + 4×3 + 4×1 + 5×3 + 4×1 + 3×1 = 5 + 10 + 12 + 4 + 15 + 4 + 3 = 53. B2 = 3×1 + 4×2 + 4×3 + 2×1 + 4×3 + 3×1 + 4×1 = 3 + 8 + 12 + 2 + 12 + 3 + 4 = 44.

**Kipppunkt:** B2 holt erst gleich, wenn man Verbreitung (K1) **und** den Abstand zu vorhandenen Tools (K4) ganz ignoriert und Budget und Umsetzbarkeit dreifach gewichtet (Gewichte 0-1-3-0-1-1-3: B1 35, B2 35). Dafür müsste man unterstellen, dass es egal ist, wie viele Leute das Problem haben und dass der Kunde schon Tools für B2 bezahlt. Das halten wir für nicht plausibel.

**Ergebnis:** **Bedürfnis 1 gewinnt in allen fünf Gewichtungen.** Am knappsten ist es aus Sicht von Sales Ops (G-e). Das passt: Für Sales Ops ist B2 das wichtigere Problem. Darum bekommt B2 im MVP den Status-Check (L2, L9) und in Phase 2 einen eigenen Auftrag mit Sales Ops.

**Schicksal des Verlierers (B2):** *MVP-Baustein* (Status-Check Arbeitgeber/Titel und Rückschreiben ins CRM), Rest *Phase 2* (E-Mail-Verifikation, Bereinigung aller Bestandskontakte, Nachfolger-Suche). Grund: Ohne Status-Check trägt B1 nicht; die volle Datenpflege konkurriert mit vorhandenen Tools und hat nur einen Käufer, darum ist sie als Folgeauftrag wirtschaftlich sicherer als als Startpunkt.

---

## Loop-Protokoll

wird vom Koordinator geführt
