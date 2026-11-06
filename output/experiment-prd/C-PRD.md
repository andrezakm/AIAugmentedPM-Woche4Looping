# PRD: Signal-Dossier-Agent

**Stand:** 2026-11-05 · **Intern** (NeoEmployee, nicht für den Kunden) · **Grundlage:** Synthese `output/interview-synthesis-2026-11-03.md`, zehn Interviews in `input/`, `context/strategy.md`, `context/company.md`
**Zitat-Regeln:** Interview-Zitate stehen in englischen doppelten Anführungszeichen (wörtlich, Englisch), Strategie-Zitate in deutschen Anführungszeichen (wörtlich), eigene Umschreibungen *kursiv*. Zahlen ohne Quelle sind als *Annahme* oder *Schätzung* markiert oder stehen als `[Platzhalter]`.

---

## Kurzfassung

**Was wir bauen:** Einen KI-Agenten für die Vertriebsorganisation des Kunden. Zu jedem Prospect, der einem Vertriebler zugewiesen wird, legt er ein kurzes Dossier ins CRM (Salesforce): höchstens drei aktuelle, mit Quelle belegte Anlässe zum Anrufen (Finanzierungsrunde, Führungswechsel, Neueinstellungen, neu in der Rolle, Themen, über die die Person schreibt) und je einen Vorschlag für den Gesprächseinstieg. Vorher prüft er, ob die Person noch bei der Firma arbeitet. Er verschickt nichts und ersetzt nicht den Vertriebler, nur dessen Recherche.

**Warum der Kunde dafür zahlt:** Die Vertriebler recherchieren heute 15 bis 40 Minuten pro Prospect. Eine SDR schafft 20 statt der geforderten 50 Calls am Tag, von 100 Marketing-Leads werden 5 mit Kontext bearbeitet. Der VP Sales rechnet selbst: "If you do the math, that's only 4 prospects an hour." Laut Synthese nennen 9 von 10 Befragten das Problem.

**Was es uns kostet (Aufwand):** *Schätzung des PM vor dem Technik-Spike, nicht belastbar:* Spike 1 Person × 1 Woche, MVP 2 Personen × 4 bis 6 Wochen (8 bis 12 Personenwochen), Pilotbegleitung 1 Person in Teilzeit über `[Platzhalter: Pilotdauer]`. Das bindet 2 unserer 14 Leute; das Pattern-Team (2 Personen) bleibt unberührt. Belastbare Zahl nach dem Spike. Tagessatz `[Platzhalter]`.

**Was es uns bringt:** (1) T&M-Umsatz über Phase 0 bis 3, Volumen = Personentage × Tagessatz `[Platzhalter]`, bei der Schätzung oben also Spike plus 8 bis 12 Personenwochen plus Pilot. (2) Einen Folgeauftrag Phase 2 (Datenpflege mit Sales Ops, eigener Käufer), Größe `[Platzhalter: nach Scoping Phase 2]`. (3) Einen wiederverwendbaren Signal-Baustein für das Pattern-Team. Das passt zur Strategie: „every deal we close extends how long we can operate and invest in the product path.“

**Was schiefgehen kann:**
1. **Recht und Datenzugang (LinkedIn) ungeklärt.** Ohne LinkedIn sinkt der Nutzen stark. Gegenmittel: Go/No-Go am Ende von Phase 0, bevor wir das MVP-Team binden (R2).
2. **Technik trägt nicht** (Signale zu ungenau, Laufzeit zu lang). Gegenmittel: Spike vor dem Bau, Abbruch möglich (R9).
3. **Kunde gibt T&M ohne Deckel nicht frei, Business Case unbelegt.** Gegenmittel: Budgetrahmen je Phase, Pilot misst zusätzlich Termine pro SDR (Z5) und liefert eine Break-even-Rechnung (R10).
4. **Zahlungsrisiko** für uns als bootstrapped Firma. Gegenmittel (*Vorschlag*): Abrechnung je Phase, nächste Phase erst nach Zahlung der vorherigen (R11).
5. **Antwortquote fällt**, weil die Ansprache generisch wird. Gegenmittel: Guardrail G1 mit Abbruchregel (R1).

**Was die Geschäftsführung entscheiden muss:**
1. **Spike und Phase 0 bezahlt anbieten oder auf eigenes Risiko?** *Empfehlung PM:* bezahlt, als kleine eigene Phase, weil Umsatz unsere Runway ist (S2) und der Spike zugleich das Abbruchrisiko für uns begrenzt.
2. **Teambesetzung:** wer die 2 Personen sind, `[Platzhalter: Namen]`.
3. **Tagessatz und Preisuntergrenze** für Pilot und Ausbau (O3).
4. **Budgetdeckel je Phase ja oder nein** (Antwort auf den erwarteten Einwand *T&M ohne Zahl*, O8).

Beim Kunden zu klären, nicht unsere Entscheidung: Freigabe von Pilot und Pilotgruppe, erlaubte Datenquellen, Budget-Owner (O1, O2, O4).

---

## Problem

**Wer leidet:** Alle, die beim Kunden neue Kunden gewinnen sollen. *Der Kunde ist die Vertriebsorganisation, bei der wir die zehn Interviews geführt haben, nicht NeoEmployee.* Betroffen sind vor allem:

- **SDRs** (Sales Development Representatives, auch Junior-SDRs): Sie sprechen neue Kontakte als Erste an, per Anruf oder E-Mail, und vereinbaren Termine.
- **Account Executives (AEs)**: Sie führen diese Termine und schließen Verträge ab. **Enterprise-AEs** tun das für sehr große Kunden.
- **Erfahrene Verkäufer**, die beides selbst machen.

Mittelbar leiden die Führungskräfte, deren Zahlen fehlen: Sales Director, VP Sales (Vertriebsleitung, muss sich vor dem Board verantworten), die Leitung Sales Enablement (zuständig für Einarbeitung und Training der Vertriebler) und das Marketing. Das Marketing gibt Geld für Kampagnen aus, um **Leads** zu gewinnen, also Kontakte, die Interesse gezeigt haben und an den Vertrieb gehen. Bleiben die liegen, war das Geld umsonst.

**Woran sie leiden:** Bevor ein Vertriebler jemanden anruft oder anschreibt, braucht er einen *Grund, warum gerade jetzt*: Die Firma hat Geld eingesammelt, die Person ist neu im Job, die Firma stellt ein, die Person schreibt über ein passendes Thema. Daraus macht er einen **Gesprächseinstieg**, also den ersten Satz, der zeigt, dass er sich mit dem Gegenüber beschäftigt hat (im Vertrieb auch *angle* oder *talk track* genannt). Diese Informationen sind öffentlich, aber über viele Webseiten verstreut, und jeder sucht sie heute von Hand. Der Sales Director: "They’re jumping between five different tabs." (*Sie springen zwischen fünf Browser-Tabs.*) Der VP Sales benennt den Kern: "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck." (*Sie machen von Hand aus ungeordnetem Rauschen brauchbare Gesprächseinstiege, und das ist der Engpass.*)

Ohne diesen Grund zum Anrufen funktioniert die Ansprache schlechter. Die Marketing-Managerin räumt ein: "conversion is higher if you know the context, I admit that—but it doesn't scale." (*Mit Kontext klappt es öfter, aber nicht in der Menge.*) Der erfahrenste Verkäufer: "It feels like half the job is just staring at a screen trying to find an angle." (*Der halbe Job ist, auf den Bildschirm zu starren und einen Aufhänger zu suchen.*) Dazu kommt: Oft ist die Person gar nicht mehr bei der Firma. Eine SDR schätzt das auf "like 40% of the time". Das ist die Schätzung einer einzelnen Person; wir messen den echten Wert in Woche 1 (Guardrail G2).

**Warum das nicht schon jemand anderes löst:** Der Kunde hat bereits ein eigenes Rechercheteam für Leads, aber dessen Ergebnis ist laut Sales Director dünn: "the output is a trickle." Die vorhandenen Daten-Tools liefern Rohdaten, aber keinen fertigen Anlass. Die Enablement-Leitung: "The problem isn't that the data is missing". Das Suchen und Gewichten bleibt Handarbeit.

**Was es kostet** (Zahlen aus den Interviews):

| Wer | Was | Zitat |
|---|---|---|
| VP Sales | 15 Min. pro Prospect, also nur 4 pro Stunde | "If you do the math, that's only 4 prospects an hour." |
| Leitung Enablement | 40 Min. Recherche ohne Ergebnis bei neuen Leuten, das verlängert die Einarbeitung | "suddenly forty minutes have passed and they haven't actually found a reason to call." / "It's a massive drain on our ramp time." |
| Junior-SDR | 30 Min. für eine einzige persönliche E-Mail | "But that took me 30 minutes to find. 30 minutes for one email!" |
| SDR | 20 statt 50 Calls am Tag | "I’m supposed to be making 50 calls a day. That's the KPI. But I’m lucky if I get to 20" |
| Top-AE | 4 Stunden am Abend für eine Liste von 10 Personen | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Enterprise-AE | Tage pro großem Account, Verhältnis 80 % Lesen zu 20 % Strategie | "It’s 80% reading LinkedIn profiles and 20% actual sales strategy." |
| Marketing | 5 von 100 Leads bekommen Kontext, 95 bleiben liegen, obwohl Marketing-Budget dafür ausgegeben wurde | "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |
| Sales Director | Die Abschlussstarken bekommen zu wenige Termine (*sie hungern nach Terminen*) | "My guys are great closers, absolute sharks, but they’re starving, man." |

**Warum die Zahlen verschieden sind:** Jede Rolle recherchiert für etwas anderes. Für einen einzelnen Anruf reichen 15 Minuten, für eine persönliche E-Mail werden es 30, neue Leute verlieren sich in 40 Minuten, und die Top-AE bereitet abends gleich 10 Kontakte vor. Gemeinsam ist allen: Ein großer Teil der Arbeitszeit geht in Suche statt in Gespräche. **In Geld** hat das beim Kunden noch niemand ausgerechnet. Wir messen es in Woche 1: Recherchestunden × Kosten je Vertriebler-Stunde `[Platzhalter: messen in Woche 1]`.

**Kurz gesagt:** Gut bezahlte Vertriebler arbeiten einen großen Teil ihrer Zeit als Rechercheure. Darum gibt es zu wenige Gespräche, zu wenige Termine und zu viele ungenutzte Leads. Die Teams stecken in einer Zwickmühle: *Wer schnell viele anruft, tut das ohne persönlichen Anlass und kommt schlechter an. Wer jeden persönlich vorbereitet, schafft die Menge nicht.* Der Sales Director: "I want speed, they want quality, and right now we have neither." (*Ich will Tempo, sie wollen Qualität, und gerade haben wir keins von beidem.*)

---

## Warum dieses Problem (Wahl und Strategie)

### Die Wahl

Die Synthese liefert zwei Bedürfnisse:

- **Bedürfnis 1 (gewählt):** *Der Grund zum Anrufen kommt fertig aufbereitet beim Vertriebler an.* Laut Synthese in 9 von 10 Interviews genannt (alle außer Sales Ops).
- **Bedürfnis 2:** *Kontaktdaten sind aktuell, verifiziert und landen ohne Handarbeit im CRM.* Laut Synthese in 5 von 10 Interviews genannt (u. a. Jenkins, Baker, Kim, Chen).

**Entscheidung: Bedürfnis 1 hat die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs.** Es gewinnt in allen fünf durchgerechneten Gewichtungen (Anhang A). Die Gründe in einem Satz je Punkt:

1. **Breiter und höher aufgehängt:** Es betrifft fast alle Befragten und mehrere Führungskräfte mit Zahlenverantwortung (VP Sales, Sales Director, Leitung Enablement, Marketing), nicht nur eine Funktion.
2. **Direkter Umsatzhebel beim Kunden:** Die Betroffenen beziffern den Effekt selbst. Die Top-AE: "I'd double my numbers." Der VP Sales: "just hand them the dossier—we’d be unstoppable." Damit ist das Projekt für den Kunden leicht zu rechtfertigen, und das ist für uns die Voraussetzung, dass bezahlt wird.
3. **Weniger Konkurrenz durch vorhandene Tools:** Für Bedürfnis 2 gibt es beim Kunden bereits ZoomInfo und Clearbit. Für Bedürfnis 1 gibt es kein Tool, das den fertigen Aufhänger liefert; der Kunde zahlt dafür heute vor allem mit der Zeit seiner Leute, dazu mit Lizenzen für Rohdaten (die Top-AE bezahlt Sales Navigator sogar selbst).

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

## Plan

| Phase | Inhalt | Ergebnis / Entscheidung | Dauer |
|---|---|---|---|
| 0: Klären und Spike | Datenquellen und Rechtslage klären (O1), CRM-Zugang und Felder (O6), Pilotgruppe festlegen, Signal-Reihenfolge und Themenliste mit dem Kunden bestätigen (O5); Technik-Spike: Status-Check und zwei Signal-Typen gegen echte Quellen testen | Go/No-Go für den Bau; belastbare Aufwandsschätzung für Phase 2 | *Schätzung:* Spike 1 Person × 1 Woche; Klärung `[Platzhalter]` |
| 1: Messen | Ausgangswerte für Z1–Z3, Z5 und G1–G2 in der Pilotgruppe erheben | Baseline steht | Woche 1 |
| 2: MVP bauen | Regeln L1–L11, Status-Check, Signal-Katalog, CRM-Anbindung | lauffähiger Agent in der Testumgebung | *Schätzung:* 2 Personen × 4 bis 6 Wochen, nach Spike bestätigen |
| 3: Pilot | Pilotgruppe `[Platzhalter: Anzahl SDRs]` nutzt die Dossiers im Alltag, wöchentliche Messung | Weiter-Entscheidung anhand Z1–Z5 und G1–G3, Break-even-Rechnung (R10) | `[Platzhalter: Pilotdauer]` |
| 4: Ausbau oder Stopp | Ausrollen auf das Team; Angebot Phase 2 (Datenpflege mit Sales Ops, Account-Mapping) | Folgeauftrag | `[Platzhalter]` |

**Abrechnung (*Vorschlag*, Entscheidung Geschäftsführung):** jede Phase mit eigenem Budgetrahmen `[Platzhalter]`, Rechnung am Phasenende, die nächste Phase startet nach Zahlung der vorigen.

**Abbruchregel für den Piloten:** Fällt G1 (Antwortquote) unter den Ausgangswert oder enthält eine Stichprobe ein Signal ohne Beleg (G3), wird der Pilot angehalten und nachgebessert, bevor er weiterläuft.

**Parallel (für NeoEmployee):** Das Pattern-Team bekommt Signal-Katalog und Ergebnisse, um zu prüfen, ob das Muster bei Kunden aus anderen Branchen auftritt.

---

## Risiken und Einwände

| # | Einwand oder Risiko | Antwort | Status |
|---|---|---|---|
| R1 | ***Das wird generisch, die persönliche Note geht verloren.*** Ross: "I want speed, they want quality, and right now we have neither." | Der Agent liefert Signale und einen Vorschlag, der Vertriebler entscheidet und formuliert. Kein Versand (L7). Private Fundstücke sind ausgeschlossen (L3). Die Antwortquote ist Guardrail G1 mit Abbruchregel. | beantwortet, im Pilot zu belegen |
| R2 | **Datenzugang und Recht** (LinkedIn-Nutzungsbedingungen, Datenschutz bei personenbezogenen öffentlichen Daten) | Noch nicht geklärt. Ohne geklärten Zugang zu LinkedIn sinkt der Nutzen stark, weil fast alle Befragten LinkedIn als Hauptquelle nennen (Kim: "It’s 90% LinkedIn."). Phase 0 klärt das vor dem Bau, mit Go/No-Go. | **offen**, siehe O1 |
| R3 | ***Lohnt sich das, wir zahlen doch schon für ZoomInfo?*** | ZoomInfo liefert Kontaktdaten, nicht den Grund zum Anrufen; die Recherche-Zeit entsteht trotz vorhandener Tools. Der Pilot misst den Effekt gegen die eigene Baseline, bevor mehr Geld fließt. Preis und Aufwand: `[Platzhalter]`. | beantwortet bis auf Preis (O3) |
| R4 | **Falsche oder erfundene Signale** schaden dem Ruf des Vertrieblers im Gespräch (Baker: "It was embarrassing. I looked like a dinosaur.") | Kein Signal ohne Quelle und Datum (L6), keine Schlüsse über die Quelle hinaus (L6), wöchentliche Stichprobe (G3). | beantwortet |
| R5 | ***Der Engpass ist die Datenqualität, nicht die Recherchezeit; der Agent setzt auf veralteten Daten auf.*** | Das Dossier beginnt immer mit dem Status-Check (L2) und korrigiert Titel im CRM (L9); wer gewechselt hat, bekommt kein Dossier, sondern eine Prüfaufgabe. Guardrail G2. Die Wahl von Bedürfnis 1 vor Bedürfnis 2 ist in Anhang A belegt; die volle Datenpflege ist als Phase 2 mit Sales Ops vorgesehen. | beantwortet, Rest siehe R12 |
| R6 | **Die Leute nutzen es nicht** (Thorne: Das Team will "every data point verified") | Jedes Signal hat einen Link zur Quelle, das Dossier liegt im CRM statt in einem neuen Tool, Nutzung wird gemessen (Z4). | im Pilot zu belegen |
| R7 | **Für NeoEmployee: Muster nur bei einem Kunden belegt** | Bau als T&M-Auftrag, der sich allein trägt (S2). Produktentscheidung erst nach Prüfung durch das Pattern-Team (S3). | bewusst offen |
| R8 | **Erfahrene Vertriebler (Enterprise) brauchen mehr als drei Signale** | Stimmt (Petit). Account-Mapping ist ausdrücklich Nicht-Ziel und Phase 2. | abgegrenzt |
| R9 | **Technik trägt nicht:** Signale zu ungenau, Quellen nicht stabil abrufbar, Laufzeit zu lang | Spike in Phase 0 testet Status-Check und zwei Signal-Typen gegen echte Quellen, bevor das MVP-Team gebunden wird. Fällt er durch, stoppen wir mit kleinem Aufwand. | offen bis Ende Phase 0 |
| R10 | ***T&M ohne Zahl kann der Kunde seinem CFO nicht vorlegen; mehr Gespräche sind kein Business Case.*** | Zwei Antworten. (1) Kosten begrenzen: Budgetrahmen je Phase, Freigabe Phase für Phase (Plan, O8). (2) Break-even rechnen: Der Pilot rechnet sich für den Kunden, wenn *zusätzliche Termine × Wert je Termin + eingesparte Recherchestunden × Kosten je Stunde ≥ Pilotkosten*. Pilotkosten aus O3, Wert je Termin vom Kunden (Sales Director oder VP Sales), Termine aus Z5, Stunden aus Z1, alle Werte `[Platzhalter]`. Daraus ergibt sich die Mindeststeigerung an Terminen, die vor dem Pilot vereinbart wird. Blunt beschreibt den Verlust heute schon in Pipeline: "And we lose pipeline." | **offen**: Wirtschaftlichkeit erst nach O3 und Pilot belegbar |
| R11 | **Zahlungsrisiko für NeoEmployee** (bootstrapped, keine Reserven aus Fremdkapital) | Abrechnung je Phase, nächste Phase erst nach Zahlung der vorigen; Zahlungsziel `[Platzhalter]`. | offen, Entscheidung Geschäftsführung (O8) |
| R12 | **Falsche E-Mail-Adressen bleiben.** Jenkins: "Half the emails bounce immediately" | Der Agent prüft Arbeitgeber und Titel, ändert aber keine E-Mail-Adressen (L9). Bounces wegen falscher Adressen sinken durch den MVP nicht. E-Mail-Verifikation ist Phase 2 mit Sales Ops. | **offen**, bewusstes Restrisiko |

---

## Offene Punkte

| # | Punkt | Wer entscheidet | Bis wann |
|---|---|---|---|
| O1 | Welche Quellen darf der Agent technisch und rechtlich nutzen, insbesondere LinkedIn? Wie lange darf das Log (L10) aufbewahrt werden? (offene Frage der Entwicklung zu L2/L3) | Kunde (Recht/Datenschutz) mit NeoEmployee | Ende Phase 0 |
| O2 | Wer auf Kundenseite ist Budget-Owner und verantwortet die Erfolgskennzahl: VP Sales, Sales Director oder Sales Ops? | Kunde | vor Angebot |
| O3 | Tagessatz, Aufwand und Budgetrahmen für Pilot und Ausbau, Preisuntergrenze | NeoEmployee-Geschäftsführung (kaufmännische Zusage, nicht vom PM) | vor Angebot |
| O4 | Größe der Pilotgruppe, Pilotdauer, Zielwerte für Z2–Z5, Wert je Termin für R10 | Kunde mit NeoEmployee | Phase 0 |
| O5 | Bestätigung der Signal-Reihenfolge (L5), des Aktualitätsfensters (L4), der Schwelle für Typ 4 und Lieferung der Themenliste (L3) | Kunde (Enablement, O'Neil) | Woche 1 |
| O6 | Bestätigung der eigenen Felder, Schreibrechte und Feld-Historie in Salesforce (Logik, L9) | Sales Ops (Kim) | Phase 0 |
| O7 | Spike und Phase 0 bezahlt oder auf eigenes Risiko; Teambesetzung | NeoEmployee-Geschäftsführung | vor Angebot |
| O8 | Budgetdeckel je Phase ja/nein, Zahlungsbedingungen | NeoEmployee-Geschäftsführung | vor Angebot |

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
