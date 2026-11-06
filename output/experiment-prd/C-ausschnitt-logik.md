## Lösung

Ein Agent, der für einen Prospect (Person plus Firma) automatisch ein **Signal-Dossier** erstellt und im CRM (Salesforce) am Kontakt ablegt. Das Dossier enthält:

1. **Status-Check:** Arbeitet die Person laut öffentlichem Profil noch bei der Firma, mit welchem Titel? (MVP-Baustein aus Bedürfnis 2)
2. **Bis zu drei Signale**, nach Relevanz sortiert, aus einem festen Katalog: Finanzierungsrunde, Führungswechsel, Neueinstellungen in relevanten Bereichen, neu in der Rolle, Themen, über die die Person öffentlich spricht. Jedes Signal mit Datum und Quellenlink.
3. **Ein Einstiegsvorschlag pro Signal:** ein bis zwei Sätze, die der Vertriebler übernehmen, ändern oder verwerfen kann.
4. **Bewertungsknopf** *brauchbar / nicht brauchbar*, damit wir messen, ob das Dossier hilft.

Der Agent ersetzt das Zusammensuchen und Sortieren, **nicht das Urteil**. Die Erfahrenen wollen die Deutung behalten. Petit: "You have to read between the lines, check their history, see what they actually talk about." Der Agent verschickt nichts, legt keine Kontakte an und sucht keine Nachfolger.

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

- *Illustrativ:* Die SDR öffnet morgens ihre zugewiesenen Leads. Bei jedem liegt ein Dossier. Bei einem steht: Person hat die Firma gewechselt, neuer Arbeitgeber laut Quelle, dazu eine Aufgabe, den Kontakt zu prüfen. Bei einem anderen: Firma hat eine Finanzierungsrunde gemeldet, Link zur Meldung, Einstiegsvorschlag. Sie liest, passt den Satz an und ruft an.
- *Illustrativ:* Der neue Vertriebler muss nicht mehr lernen, wie man sucht. Die Einarbeitung kann sich, wie O'Neil es sich wünscht, auf Gesprächsführung und Einwandbehandlung konzentrieren.
- *Illustrativ:* Die AE öffnet die Kontakte, die ihr zugewiesen sind, und sieht bei jedem sofort, ob es eine frische Finanzierungsrunde oder eine neue Rolle gibt, ohne Abendschicht.

---

## Ziele

Alle Ausgangswerte werden in Woche 1 beim Kunden gemessen. Zahlen aus den Interviews dienen als erste Orientierung.

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| Z1 | Recherche wird kurz | Zeit vom Öffnen eines Leads bis zum Start des Kontakts | laut Interviews 15 Min. (Thorne), 30 Min. (Green), bis 40 Min. (O'Neil); genau: `[Platzhalter: messen in Woche 1]` | *Annahme:* unter zwei Minuten, angelehnt an O'Neils Maßstab "can you find it in under two minutes?"; mit Kunde bestätigen | Ende des Piloten `[Platzhalter: Pilotdauer]` |
| Z2 | Mehr Gespräche | Calls bzw. Erstkontakte pro SDR und Tag | 20 laut Jenkins, KPI 50; genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter: mit Kunde vereinbaren]` | Ende des Piloten |
| Z3 | Mehr Leads werden bearbeitet | Anteil der zugewiesenen Leads, die innerhalb `[Platzhalter: Frist]` kontaktiert werden | Orientierung: 5 von 100 laut Blunt (mit Kontext bearbeitet); genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter: mit Kunde vereinbaren]` | Ende des Piloten |
| Z4 | Das Dossier hilft | Anteil Dossiers, die der Vertriebler als *brauchbar* markiert | 0 (gibt es heute nicht) | `[Platzhalter: Schwelle für Weiter-Entscheidung]` | wöchentlich ab Pilotstart |
| Z5 | Mehr Termine (Business Case des Kunden) | vereinbarte Ersttermine pro SDR und Woche; Ross: "They are starving for good meetings." | `[Platzhalter: messen in Woche 1]` | mindestens der Break-even-Wert aus R10 `[Platzhalter: berechnen nach O3]` | Ende des Piloten |

**Für NeoEmployee:**

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| N1 | Umsatz aus dem Vorhaben | beauftragte und bezahlte Personentage für Phase 0 bis 3 | `[Platzhalter: Stand bei Angebotsannahme]` | `[Platzhalter: Volumen nach Angebot, O3]` | Ende Phase 3 (Pilot) |
| N2 | Folgeauftrag | Angebot Phase 2 (Datenpflege mit Sales Ops) liegt beim Kunden vor und ist beauftragt (ja/nein) | nein | ja | Ende Phase 4 |
| N3 | Baustein für das Pattern-Team | Signal-Katalog, Quellen-Adapter und Ranking sind getrennt vom kundenspezifischen Teil übergeben (ja/nein) | nein | ja | Ende Phase 2 (MVP) |

**Guardrails** (dürfen nicht schlechter werden):

| # | Guardrail | Ausgangswert | Grenze | Messzeitpunkt |
|---|---|---|---|---|
| G1 | **Antwortquote** auf Erstkontakte (die persönliche Ansprache darf nicht leiden) | `[Platzhalter: messen in Woche 1]` | darf nicht unter den Ausgangswert fallen | wöchentlich ab Pilotstart |
| G2 | **Kontakte, die nicht mehr da sind** (Person nicht mehr bei der Firma, "Who?"-Anrufe) | laut Jenkins "like 40% of the time"; genau: `[Platzhalter: messen in Woche 1]` | darf nicht steigen | wöchentlich |
| G3 | **Signale ohne Beleg** | 0 | bleibt 0 (Stichprobe `[Platzhalter: Umfang]` pro Woche) | wöchentlich |

---

## Nicht-Ziele

| Nicht-Ziel | Warum nicht | Wohin |
|---|---|---|
| E-Mails oder Sequenzen automatisch verschicken | Risiko für die Antwortquote (Alternative A3), der Vertriebler behält das Urteil | frühestens Phase 2, nur wenn G1 im Pilot stabil bleibt |
| Ersatz der Vertriebler | Der Agent ersetzt die Recherche, nicht Urteil und Gespräch (siehe Lösung) | nie |
| Komplette CRM-Bereinigung, E-Mail-Verifikation, Nachfolger-Suche und Anlage neuer Kontakte | Das ist Bedürfnis 2 in voller Breite, anderer Käufer (Sales Ops), würde den Pilot überladen | Phase 2, eigener Auftrag mit Sales Ops |
| Enterprise-Account-Mapping (Organigramm, Beziehungsnetz, wie Petit es beschreibt) | Andere, deutlich schwerere Aufgabe als Einzelsignale; Petit braucht Beziehungen, nicht drei Anlässe | Phase 2 |
| Listen neuer Prospects erzeugen (z. B. alle frisch finanzierten Firmen) | Der Agent arbeitet nur an zugewiesenen Kontakten (L1), Listenbau wäre Anreicherung auf Vorrat (A4) | Phase 2, wenn der Pilot trägt |
| Gemeinsame Lead-Definition zwischen Marketing und Sales | Organisationsfrage, kein ersetzbarer Skill; fällt durch den Vision-Filter (S1) | nie (nicht unser Auftragsfeld) |
| Ersatz oder Einkauf von ZoomInfo, Sales Navigator & Co. | Lizenzkauf, kein Agent (S1), kein Umsatz für uns | nie |
| Reporting- und Attributions-Dashboard für die Führung | Die Logs des Agenten (Regel L10) liefern die Daten nebenbei, ein eigenes Dashboard ist nicht nötig für den Pilot | Phase 2, wenn der Kunde es verlangt |
| Produkt für viele Kunden | Laut Strategie sind wir noch Custom-Dienstleister, das Muster über Kunden ist unbelegt | Pattern-Team prüft; Entscheidung frühestens nach weiteren Kunden |

---

## Logik

Begriffe: **Prospect** = Kontakt im CRM (Salesforce, Objekt *Contact*) mit Name, Firma, Titel. **Dossier** = Ergebnis des Agenten am Kontakt. **Signal** = ein datiertes, belegtes Ereignis aus dem Signal-Katalog. **Lauf** = eine Ausführung des Agenten für einen Kontakt; Bezugsdatum ist der Startzeitpunkt des Laufs.

**Felder, die der Agent anlegt** (eigene Felder am Kontakt, Namen in Phase 0 mit Sales Ops bestätigen): *Signal-Dossier* (Langtext), *Agent-Status* (Auswahlliste: aktuell, Titel aktualisiert, gewechselt, unklar, nicht geprüft), *Neuer Arbeitgeber laut Quelle* (Text), *Dossier-Stand* (Datum/Uhrzeit), *Dossier-Bewertung* (brauchbar, nicht brauchbar, leer).

**Schreibrechte des Agenten, abschließend:** die fünf eigenen Felder oben, das Standardfeld *Titel* und das Anlegen einer Aufgabe am Kontakt. Sonst nichts: kein Arbeitgeber-/Account-Feld, keine E-Mail, kein Telefon, keine neuen Kontakte.

| # | Regel | Eingabe → erwartetes Verhalten |
|---|---|---|
| L1 | **Auslöser.** Ein Lauf startet, wenn ein Kontakt einem Vertriebler zugewiesen wird (auch bei Neuzuweisung) oder wenn der Vertriebler per Knopf *Dossier anfordern* klickt. Es gibt keinen Lauf über alle Kontakte. Ein neuer Lauf ersetzt das bestehende Dossier (L9). | Kontakt wird zugewiesen → Lauf startet. Erneuter Klick bei vorhandenem Dossier → neuer Lauf, altes Dossier ersetzt, alte Version im Log. Kontakt ohne Zuweisung und ohne Klick → kein Lauf. |
| L2 | **Status-Check zuerst.** Der Agent vergleicht Arbeitgeber und Titel im CRM mit der öffentlichen Quelle, nach Normalisierung: Groß-/Kleinschreibung, Satzzeichen und doppelte Leerzeichen ignoriert; Rechtsformzusätze entfernt (Inc, Corp, Corporation, LLC, Ltd, GmbH, AG); Titel-Kürzel aus einer festen Liste aufgelöst (VP = Vice President, SVP = Senior Vice President, Sr = Senior, CRO, CTO, CEO, CFO, COO, CMO ausgeschrieben). Hat eine Person mehrere aktuelle Stellen, zählt die, deren Arbeitgeber zum CRM passt. Ergebnis: (a) beides gleich → *Agent-Status* = aktuell, weiter mit L3. (b) Arbeitgeber gleich, Titel anders → Titel nach L9 aktualisieren, *Agent-Status* = Titel aktualisiert, weiter mit L3. (c) Arbeitgeber anders → *Agent-Status* = gewechselt, *Neuer Arbeitgeber laut Quelle* füllen, Aufgabe *Kontakt hat gewechselt, prüfen* an den zuständigen Vertriebler, **kein** Signal-Teil, Kontakt bleibt bei der bisherigen Firma. (d) Quellen widersprechen sich (z. B. zwei Profile mit verschiedenen Arbeitgebern) → *Agent-Status* = unklar, keine Änderung an *Titel*, Dossier mit Vermerk *Status unklar, bitte prüfen*, weiter mit L3. (e) keine öffentliche Quelle gefunden → *Agent-Status* = nicht geprüft, weiter mit L3. | CRM *Oracle*, Profil *Oracle Corporation* → gleich (a). CRM *VP Sales*, Profil *Vice President Sales* → gleich (a). CRM *Acme / Head of Sales*, Profil *Acme / VP Sales* → (b). CRM *Oracle*, Profil *Salesforce* → (c), Aufgabe angelegt, Arbeitgeber im CRM unverändert. Zwei Profile, zwei Arbeitgeber → (d). |
| L3 | **Signal-Katalog (fest im MVP).** (1) **Führungswechsel:** neue Person bei der Firma des Prospects mit Titel auf VP-Ebene oder höher (Titel enthält nach Normalisierung Vice President oder Chief, oder ist ein C-Level-Kürzel aus L2), in jedem Bereich. (2) **Neu in der Rolle:** Prospect hat seine aktuelle Rolle innerhalb des Fensters aus L4 angetreten. (3) **Finanzierungsrunde** der Firma. (4) **Neueinstellungen:** die Firma hat innerhalb des Fensters mindestens *Annahme:* 3 Stellen in Engineering oder Operations ausgeschrieben (Schwelle konfigurierbar). (5) **Thema:** die Person hat innerhalb des Fensters einen Beitrag veröffentlicht, der mindestens ein Stichwort aus der Themenliste des Kunden enthält (Stichwortabgleich, Groß-/Kleinschreibung egal). Die Themenliste ist eine Stichwortliste, die Enablement in Phase 0 liefert (O5); solange sie fehlt, ist Typ 5 abgeschaltet. Alles andere (Urlaub, Hobbys, private Fotos) wird nicht als Signal ausgegeben. | Urlaubs-Post → kein Signal. Finanzierungsmeldung → Typ 3. Neuer CRO → Typ 1. Neuer Team Lead → kein Signal. 2 Stellen in Engineering → kein Signal; 3 → Typ 4. Beitrag mit Stichwort der Liste → Typ 5; Themenliste leer → nie Typ 5. |
| L4 | **Aktualität.** Ein Signal zählt nur, wenn sein Datum innerhalb des Fensters liegt, gerechnet vom Bezugsdatum des Laufs, Grenztag eingeschlossen. Startwert (*Annahme*): 90 Tage, pro Signal-Typ konfigurierbar. *Neu in der Rolle* (Typ 2) gilt bis 6 Monate nach Start, wie Chen es nutzt ("less than 6 months"). | Finanzierung vor 30 Tagen → Signal. Vor 90 Tagen → Signal. Vor 200 Tagen → kein Signal. Rollenstart vor 5 Monaten → Typ 2; vor 7 Monaten → nicht. |
| L5 | **Höchstens drei Signale.** Gleiches Ereignis aus mehreren Quellen (gleicher Typ, gleiche Firma bzw. Person, gleiches Datum) zählt als ein Signal mit mehreren Quellenlinks. Gibt es danach mehr als drei, wird nach Typ sortiert (Reihenfolge wie in L3, *Annahme*, mit Kunde in Woche 1 bestätigen), bei gleichem Typ das neuere zuerst. Grundlage für die Grenze drei: O'Neil, "those three specific things". | Dieselbe Finanzierungsrunde aus zwei Quellen → ein Signal, zwei Links. Fünf gültige Signale Typ 3, 1, 5, 1, 4 → angezeigt: Typ 1 (neuer), Typ 1 (älter), Typ 3; Typ 4 und 5 verworfen und geloggt. |
| L6 | **Kein Signal ohne Beleg.** Jedes Signal braucht Quellen-URL und Datum. Fehlt eines davon, wird das Signal nicht angezeigt. Der Agent erfindet keine Fakten und schließt nicht auf Fakten, die nicht in der Quelle stehen (geprüft per Stichprobe, G3). | Fund ohne URL oder ohne Datum → nicht im Dossier, im Log als *verworfen: ohne Beleg*. |
| L7 | **Einstiegsvorschlag.** Pro Signal ein Vorschlag mit höchstens zwei Sätzen, der nur das belegte Signal verwendet. Er ist als *Vorschlag* gekennzeichnet und wird nie automatisch verschickt. | Signal Finanzierungsrunde → Vorschlag nennt die Runde, enthält keine weiteren Behauptungen. Kein Versand-Knopf, kein Aufruf an ein Mail- oder Sequenz-System. |
| L8 | **Kein Signal gefunden.** Liefert L3 bis L6 kein gültiges Signal, sagt das Dossier ausdrücklich *kein aktuelles Signal gefunden*, ohne Einstiegsvorschlag. Gilt nicht im Fall L2(c); dort zeigt das Dossier nur den Status. | Kontakt ohne gültige Signale → Vermerk, Vorschlagsfeld leer. Fall L2(c) → nur Status *gewechselt*, kein Vermerk. |
| L9 | **Schreiben ins CRM.** Das Dossier steht im Feld *Signal-Dossier*, *Dossier-Stand* bekommt den Zeitpunkt. Ein neuer Lauf überschreibt beide; die vorige Version bleibt im Log (L10). Bei L2(b) wird *Titel* überschrieben; der alte Wert bleibt in der Feld-Historie des CRM, und der Agent schreibt alten Wert, neuen Wert, Quelle und Zeitpunkt zusätzlich ins Log (damit es auch ohne aktivierte Feld-Historie nachvollziehbar ist). Alle anderen Felder bleiben unberührt (siehe Schreibrechte oben). | Titel weicht ab → *Titel* neu, Log enthält alten Wert, Quelle, Zeitpunkt. E-Mail, Telefon, Arbeitgeber vorher = nachher. Zweiter Lauf → *Signal-Dossier* neu, alte Version im Log. |
| L10 | **Protokoll.** Pro Lauf werden geloggt: genutzte Quellen, gefundene und verworfene Signale mit Grund, Feldänderungen (L9), Laufzeit, Bewertung des Vertrieblers. Die Bewertung ist änderbar, es zählt die letzte. Das Log liegt in der Umgebung des Kunden; Aufbewahrungsdauer klärt O1 (Datenschutz). | Dossier erstellt und bewertet → Log-Eintrag mit allen Feldern. Nicht bewertet → Bewertung leer. Bewertung von *brauchbar* auf *nicht brauchbar* geändert → Z4 zählt *nicht brauchbar*. |
| L11 | **Laufzeit.** Ziel (*Annahme*): Dossier liegt unter zwei Minuten nach Auslöser vor. Solange der Lauf läuft, zeigt das CRM *Dossier in Arbeit*. Ist er nach *Annahme:* 10 Minuten nicht fertig oder scheitert, startet ein automatischer zweiter Versuch; scheitert auch der, zeigt das Feld *Dossier fehlgeschlagen* und der Knopf *Dossier anfordern* ist wieder aktiv. | Lead geöffnet, Lauf läuft → *Dossier in Arbeit*. Lauf fertig → Dossier sichtbar. Zweimal Zeitüberschreitung → *Dossier fehlgeschlagen*, Knopf aktiv. |

**Offene Frage für die Entwicklung:** Welche öffentlichen Quellen der Agent technisch und rechtlich nutzen darf, vor allem LinkedIn (betrifft L2 und L3). Testfälle lassen sich mit nachgebildeten Quellen schreiben, gebaut werden kann der Status-Check erst nach dieser Entscheidung. Siehe Offene Punkte, O1.

---

