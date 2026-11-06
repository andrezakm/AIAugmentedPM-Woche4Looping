# PRD: Signal-Dossier-Agent

**Stand:** 2026-11-05 · **Autor:** Produktmanagement NeoEmployee · **Status:** Entwurf zur Entscheidung, intern
**Grundlage:** `output/interview-synthesis-2026-11-03.md`, zehn Interviews in `input/`, `context/company.md`, `context/strategy.md`
**Konventionen:** Interview-Zitate in "…", wörtlich aus `input/`. Strategie-Zitate in „…“, wörtlich aus `context/`. Eigene Umschreibungen *kursiv*. Fehlende Daten als `[Platzhalter]`. Nicht belegte Aufwände und Startwerte nur als Annahme mit Verweis (A1 bis A12, gesammelt unter *Offene Punkte*).

---

## Kurzfassung

**Was wir bauen:** Einen KI-Agenten, der für jeden Prospect, den ein Vertriebler ansprechen will, ein kurzes Dossier liefert: Ist die Person noch in dieser Rolle? Welche höchstens drei aktuellen Anlässe gibt es (Finanzierung, Neueinstellungen, Führungswechsel, neue Rolle, Themen)? Welcher Gesprächsaufhänger folgt daraus? Zu jedem Anlass steht die Quelle dabei. Das Dossier landet am CRM-Datensatz. Der Agent ersetzt den Skill *Prospect-Researcher*. Schreiben, Senden und das Urteil im Gespräch bleiben beim Menschen.

**Warum dieses Bedürfnis:** Die Synthese lässt zwei Bedürfnisse übrig: (1) den fertig aufbereiteten Grund zum Anrufen und (2) aktuelle Kontaktdaten im CRM. Wir wählen (1). Es betrifft 9 der 10 Befragten statt 5, es ist ein Umsatzhebel statt einer Kostensenkung, und es tritt nicht gegen Standardwerkzeuge an, die der Kunde schon bezahlt. Die Wahl hält in 3 von 4 durchgerechneten Gewichtungen. Sie kippt nur, wenn man Umsetzungsrisiko und Abhängigkeit doppelt gewichtet. Darum bauen wir den Kern von (2), den Rollen-Check, als festen MVP-Baustein ein (Anhang A). Der volle CRM-Abgleich wird ein eigenes Folgeangebot.

**Was es bringt (belegt):** Heute kostet die Recherche 15 bis 40 Minuten pro Prospect. Der VP of Sales rechnet: "that's only 4 prospects an hour". Eine SDR schafft 20 statt 50 Calls am Tag. Von 100 bezahlten Marketing-Leads bekommen 5 Kontext. Das Ziel setzt der Kunde selbst: "can you find it in under two minutes?"

**Was es kostet (Aufwand, nicht belegt):** Bis zum Pilot-Ergebnis 33 bis 50 Personentage (A1 + A2 + A3), mit 2 bis 3 Personen (A6). Bis zum vollen Rollout 48 bis 75 Personentage (zusätzlich A5). Tagessatz und Angebotssumme: `[Platzhalter]`.

**Was schiefgehen kann:** (a) Die wichtigste Datenquelle ist LinkedIn, und der zulässige Zugriff ist ungeklärt. (b) Falsche Anlässe zerstören das Vertrauen der Nutzer. (c) Das Budget liegt vielleicht bei Sales Ops und nicht beim VP of Sales. Gegenmaßnahmen stehen unter *Risiken und Einwände*.

**Was zu entscheiden ist:** (1) Go für Phase 0 und 1 mit 13 bis 20 Personentagen (A1 + A2). (2) Tagessatz und ob Phase 0 berechnet wird: `[Platzhalter]`. (3) Rechtliche Prüfung des Datenzugriffs vor dem Pilot beauftragen.

---

## Problem

**Wer leidet:** Die Vertriebsorganisation eines Kunden. Das sind die Leute, die neue Kunden zuerst anrufen oder anschreiben (SDRs), die Verkäufer, die Abschlüsse machen (Account Executives), und deren Führung: VP of Sales, Sales Director, die Leiterin der Einarbeitung (Sales Enablement) und die Marketing-Managerin, die die Leads bezahlt.

**Woran:** Bevor ein Vertriebler einen Fremden anruft, braucht er einen Grund: *Die Firma hat gerade Geld eingesammelt, sie stellt ein, die Person ist neu in der Rolle.* Ohne diesen Grund antwortet kaum jemand. Die Informationen sind öffentlich, aber über viele Seiten verstreut. Heute sucht ein Mensch sie von Hand zusammen und formt daraus einen Gesprächsaufhänger. Der VP of Sales sagt es so: "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck." Die Leiterin Sales Enablement bestätigt: "The problem isn't that the data is missing; it's that they have to sift through so much irrelevant noise to find those three specific things."

Darunter liegt ein zweites Problem: Oft arbeitet die Person gar nicht mehr dort. Eine SDR prüft jeden Kontakt von Hand: "If they aren’t, which is like 40% of the time, I have to go hunt for who the new person is."

**Was es kostet:**

| Wer | Kosten heute | Wörtlich |
|---|---|---|
| Marcus Thorne, VP of Sales | 15 Min. pro Prospect, also nur 4 pro Stunde | "If you do the math, that's only 4 prospects an hour. That's a joke." |
| Linda O'Neil, Director of Sales Enablement | 40 Min. bei neuen Reps, oft ohne Ergebnis; verlängert die Einarbeitung | "suddenly forty minutes have passed and they haven't actually found a reason to call" / "It's a massive drain on our ramp time." |
| Rachel Green, Junior SDR | 30 Min. für eine einzige E-Mail | "30 minutes for one email!" |
| Mike Ross, Sales Director | 20 Min. pro E-Mail; die Abschluss-Profis bekommen zu wenig Termine | "They are starving for good meetings." |
| Sarah Jenkins, SDR | 20 statt 50 Calls am Tag, also 40 % des Tagesziels | "I’m supposed to be making 50 calls a day. That's the KPI. But I’m lucky if I get to 20" |
| Jessica Chen, Account Executive (Top-Performerin) | 4 Std. abends für 10 Kontakte, also 24 Min. pro Kontakt, unbezahlt | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Sam Petit, Enterprise Account Executive | Tage pro Großkunde, bevor die erste E-Mail rausgeht | "I spend days—literal days—just mapping an account" |
| Emily Blunt, Marketing Manager (eigenes Budget) | Bezahlte Leads bleiben liegen, weil Kontext nur für wenige reicht | "We spend serious budget—my budget—getting these people into the funnel" / "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |

**Warum man die Recherche nicht einfach weglässt:** Ohne Kontext sinkt die Antwortquote. Die Marketing-Managerin räumt ein: "conversion is higher if you know the context, I admit that". Der erfahrenste Verkäufer kannte einmal den Artikel eines Kunden nicht und sagt: "I looked like a dinosaur." Die Führung will beides zugleich. Ross: "I want speed, they want quality, and right now we have neither." *Personalisierung muss also billig werden, nicht wegfallen.*

**Was beim Menschen bleiben muss:** Erfahrene Verkäufer wollen die Deutung selbst machen. Petit: "You have to read between the lines". *Gebraucht wird die Vorarbeit, nicht das Urteil.*

---

## Warum dieses Problem (Wahl und Strategie)

### Die Abwägung in Kürze

Beide Bedürfnisse der Synthese bestehen die Strategie-Prüfung. Die Frage ist darum, welches mit höherer Wahrscheinlichkeit zu bezahlter Arbeit führt. Wir haben beide auf acht benannten Kriterien bewertet und vier Gewichtungen durchgerechnet (Anhang A).

| | Bedürfnis 1: Grund zum Anrufen fertig aufbereitet | Bedürfnis 2: Kontaktdaten aktuell im CRM |
|---|---|---|
| Betroffene | 9 von 10 (alle außer Kim) | 5 von 10 (Jenkins, Kim, Baker, Chen, Petit teilweise) |
| Käufer | VP of Sales, Sales Director, Dir. Sales Enablement; Marketing mit eigenem Budget | Sales Ops Manager (verantwortet den Tool-Stack) |
| Art des Nutzens | Mehr Umsatz: "I'd double my numbers." (Chen) | Weniger Kosten: "Why do I have a human being paid $80k a year acting as a copy-paste machine?" (Kim) |
| Wettbewerb | Kein vorhandenes Werkzeug liefert die Synthese, die Leute recherchieren trotz Lizenzen von Hand | ZoomInfo und Clearbit sind schon da: "they break, or they’re too expensive to run on every single contact record" |
| Ergebnis gleichgewichtet | **19 Punkte** | 18 Punkte |

**Ergebnis:** Bedürfnis 1 gewinnt bei gleicher Gewichtung, bei Runway-Gewichtung und bei Brücken-Gewichtung. Bei Risiko-Gewichtung gewinnt Bedürfnis 2 (21 zu 23), weil Bedürfnis 1 auf aktuellen Kontaktdaten aufbaut. Nehmen wir den Rollen-Check aus Bedürfnis 2 in den MVP auf, steht es auch dort unentschieden (23 zu 23). **Wir wählen Bedürfnis 1 mit Rollen-Check.**

**Was wir ehrlich zugeben:** Bedürfnis 2 hat den besser belegten Budget-Inhaber. Kim bezahlt heute schon Anreicherungs-Tools. Für den VP of Sales belegen die Interviews Druck ("I had a meeting with the board this morning"), aber kein freigegebenes Budget. Wenn Phase 0 zeigt, dass nur Sales Ops Budget hat, kehrt sich die Reihenfolge um (Anhang A.5).

**Schicksal von Bedürfnis 2:**
- **MVP-Baustein:** Der Rollen-Check (*arbeitet die Person noch dort, und wer folgt ihr nach?*) läuft vor jedem Dossier. Ohne ihn erzeugt der Agent Dossiers über Leute, die gegangen sind.
- **Phase 2, eigenes Angebot an Sales Ops:** Der dauerhafte Abgleich aller CRM-Kontakte mit Schreibrechten. Die Rollen-Checks aus dem Pilot liefern Kim dafür schon Belege.

### Strategie-Nachweis

| | Satz aus `context/strategy.md` | Begründung |
|---|---|---|
| **S1 Vision-Filter** | „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ | Der Agent ersetzt einen klar abgrenzbaren Skill: das Recherchieren und Strukturieren von Anlässen. O'Neil beschreibt genau diesen Skill: "We’re essentially teaching them to be high-priced data miners." Er ersetzt kein Urteil und keine Vertriebsstrategie. Das bleibt außerhalb des Rahmens. |
| **S2 Umsatz** | „anything that brings in money and aligns with our vision, we do.“ und „every deal we close extends how long we can operate and invest in the product path“ | Das Projekt wird als Kundenprojekt abgerechnet, passend zu „We bill on a time-and-material basis.“ (`company.md`). Es hat mehrere Käufer mit beziffertem Schmerz. Thorne beschreibt die Lösung selbst: "just hand them the dossier—we’d be unstoppable". Das macht einen schnellen Abschluss wahrscheinlicher. Der Pilot ist klein genug (A1 bis A3), um früh Umsatz zu erzeugen, statt lange vorzufinanzieren. |
| **S3 Muster** | „These patterns are the seeds of future products: non-custom, reusable agents built on real-world demand rather than speculation.“ | Die Signal-Kategorien sind nicht kundenspezifisch. O'Neils Checkliste gilt für jede B2B-Vertriebsorganisation: "1. Recent funding news—Series B or C preferably. 2. New hiring in engineering or ops. 3. Recent leadership changes at the VP level." Wir bauen die Bausteine (Quellen-Adapter, Signal-Regeln, Rollen-Check) modular und übergeben sie dem Pattern-Team. **Einschränkung:** Alle zehn Interviews stammen aus einer Organisation. Ob das Muster bei Kunden in anderen Branchen auftritt, ist unbelegt und Aufgabe des Pattern-Teams. Wir bauen kein Produkt, denn: „Every agent is built custom for the client; we do not sell AI agents as off-the-shelf products.“ (`company.md`) |

---

## Lösung

**Ein Agent, der pro Prospect ein Dossier erzeugt und am CRM-Datensatz ablegt. Das Dossier ist in unter zwei Minuten lesbar und besteht aus vier Teilen:**

1. **Rollen-Check:** `bestätigt`, `gewechselt` oder `unklar`, mit Quelle. Bei `gewechselt`: die neue Firma der Person und, falls gefunden, ein Nachfolger-Kandidat in der alten Firma. Das ersetzt Jenkins' Handarbeit: "I have to go hunt for who the new person is."
2. **Höchstens drei Anlässe** aus festen Kategorien: Finanzierung, Neueinstellungen, Führungswechsel auf VP-Ebene (O'Neils Checkliste), neue Rolle der Person (Chen sucht Leute unter 6 Monaten im Amt) und Themen-Beiträge (Green: "Show me everyone who posted about Cloud Migration in the last week."). Jeder Anlass hat Datum, einen Satz Inhalt und einen Quell-Link.
3. **Ein Vorschlag für den Gesprächsaufhänger**, der sich auf mindestens einen der Anlässe bezieht. Er ist ein Vorschlag und keine fertige Nachricht.
4. **Kopfzeile:** Erstellzeit, geprüfte Quellen, Warnhinweise.

**Auslöser:** Einzeln auf Knopfdruck am Prospect, oder als Stapel für alle Prospects, die einem Vertriebler für den nächsten Arbeitstag zugeordnet sind. Der Stapel ersetzt Chens Abendschicht.

**Wo es landet:** Als Notiz am Kontakt im CRM des Kunden. Laut Jenkins ist das Salesforce. Der Agent schreibt keine Kontaktfelder um, er hängt nur an. Damit bleibt das CRM der Ort des Ergebnisses, und das Dossier verschwindet nicht in Tabs.

**Quellen:** Nur Quellen auf einer Freigabeliste je Kunde, jede über einen eigenen austauschbaren Adapter: Firmenwebseiten, Pressemitteilungen und Nachrichten, Finanzierungsdatenbanken wie Crunchbase (von Ross, Kim und O'Neil genannt) und LinkedIn, sobald ein zulässiger Zugriffsweg geklärt ist (*Offene Punkte*, Nr. 1).

**Ausbaustufen:** Stufe 1 ist das Prospect-Dossier (dieser PRD). Stufe 2 ist die Account-Karte für Großkunden (Petit) und kommt erst, wenn Stufe 1 trägt (siehe *Nicht-Ziele*).

### Alternativen

Alle drei sind Lösungsalternativen für dasselbe Problem.

| Alternative | Was sie wäre | Warum nicht |
|---|---|---|
| **A1: Signal-Feed ohne Synthese** | Ein Agent sammelt alle Rohsignale je Prospect und zeigt sie als Liste, ohne Auswahl und ohne Aufhänger. Billiger zu bauen. | Das löst das falsche Problem. Es fehlen nicht die Daten, es fehlt die Auswahl: "The problem isn't that the data is missing" (O'Neil). Ein längerer Feed verstärkt das Rauschen, das Thorne als Engpass benennt. |
| **A2: Vollautomatische Ansprache** | Der Agent schreibt und versendet die personalisierte E-Mail selbst. Maximal skalierbar. | Die Erfahrenen wollen die Deutung behalten ("You have to read between the lines", Petit), und Green spürt schon heute, wenn ein Aufhänger nicht echt ist: "It feels a bit fake, honestly." Automatischer Versand gefährdet genau die Antwortquote, die Kontext erst bringt. |
| **A3: Vorhandene Anreicherungs-Tools ausbauen** | Mehr ZoomInfo-Lizenzen oder Sales Navigator für alle, plus Schulung. | Das ist Einkauf und keine Agent-Arbeit, also nach S1 nicht unser Auftrag. Diese Tools liefern Rohdaten, und die Leute recherchieren trotzdem von Hand. Der Stack-Verantwortliche hält sie schon heute für unzuverlässig und zu teuer: "they break, or they’re too expensive to run on every single contact record". |

### Vorher und nachher

**Vorher (aus den Interviews):**
- Jenkins öffnet Salesforce, dann LinkedIn, um zu sehen, ob die Person noch da ist. Oft ist sie weg, dann sucht sie den Nachfolger. Danach kopiert sie Titel von Hand ins CRM und schafft 20 statt 50 Calls.
- Green sucht 30 Minuten, findet einen Thread über Sauerteig und schreibt damit eine E-Mail. Findet sie nichts, nimmt sie ein allgemeines Like auf LinkedIn als Aufhänger.
- Chen sitzt abends 4 Stunden an einer Liste von 10 Leuten, mit drei Browser-Erweiterungen, um E-Mail-Adressen zu raten.
- Baker kennt im Termin den Artikel des Kunden nicht und steht schlecht da.
- Thorne geht an den Tischen vorbei, sieht nur Browser-Tabs und nennt es "a black box".

**Nachher (*illustrativ*, so noch nicht beobachtet):**
- *Jenkins findet morgens an jedem Prospect ihrer Liste ein Dossier. Bei einem Teil steht `gewechselt`, mit neuer Firma und einem Nachfolger-Kandidaten. Diese Kontakte ruft sie nicht mehr blind an.*
- *Green liest pro Prospect einen Anlass (zum Beispiel einen Beitrag zu Cloud Migration aus der letzten Woche) und einen Aufhänger-Vorschlag. Sie formuliert die E-Mail selbst.*
- *Chen bekommt die Dossiers als Stapel für den nächsten Tag und muss abends nicht mehr recherchieren.*
- *Baker sieht vor dem Call, dass der Kunde kürzlich einen Artikel veröffentlicht hat, mit Link.*
- *Thorne sieht im CRM-Protokoll, wie viele Dossiers erzeugt und geöffnet wurden.*

---

## Ziele

Messung in der Pilotgruppe gegen eine Vergleichsgruppe ohne Dossier (Größe: A4). Zielwerte außer Z1 legt der Kunde in Phase 0 fest.

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| Z1 | Recherche pro Prospect verkürzen | Minuten von Prospect-Auswahl bis Kontaktversuch | 15 bis 40 Min. laut Interviews; genau: `[Platzhalter: messen in Woche 1]` | unter 2 Min. (O'Neils eigene Marke) | Woche 1 des Pilots und Ende des Pilots (A4) |
| Z2 | Mehr Kontaktversuche | Calls pro SDR und Tag | etwa 20 bei Tagesziel 50 (Jenkins); genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Ende des Pilots (A4) |
| Z3 | Mehr Leads mit Kontext | Anteil bearbeiteter Leads, die vor dem Erstkontakt ein Dossier haben | 5 von 100 (Blunt) | `[Platzhalter]` | Ende des Pilots (A4) |
| Z4 | Weniger tote Kontakte im Gespräch | Anteil Kontaktversuche, bei denen die Person nicht mehr in der Rolle ist | etwa 40 % (Jenkins); genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Ende des Pilots (A4) |
| Z5 | Nutzung | Anteil erzeugter Dossiers, die vor dem Kontaktversuch geöffnet werden | neue Funktion, kein Ausgangswert | `[Platzhalter]` | wöchentlich im Pilot, Bericht am Ende (A4) |

**Guardrails (dürfen nicht schlechter werden):**

| # | Guardrail | Kennzahl | Ausgangswert | Messzeitpunkt |
|---|---|---|---|---|
| G1 | Antwortquote hält | Antworten oder Termine pro Kontaktversuch, Pilot- gegen Vergleichsgruppe | `[Platzhalter: messen in Woche 1]` | Ende des Pilots (A4) |
| G2 | Keine falschen Anlässe | Anteil Anlässe, die Nutzer als falsch markieren (Regel R14), und Anteil Anlässe ohne Quelle (muss null sein, Regel R7) | neue Funktion | wöchentlich im Pilot |

G1 ist die wichtigste Leitplanke: Steigt das Volumen und fällt die Antwortquote, haben wir nur Druck automatisiert und keinen Kontext.

**Ziele für NeoEmployee:**

| # | Ziel | Kennzahl | Ausgangswert | Messzeitpunkt |
|---|---|---|---|---|
| N1 | Bezahlter Auftrag | Unterschriebenes T&M-Angebot für Phase 1 und 2 | kein Auftrag | Ende Phase 0 |
| N2 | Folgeauftrag | Beauftragung von Rollout oder CRM-Abgleich (Sales Ops) | kein Auftrag | Ende des Pilots (A4) |
| N3 | Brücke | Bausteine (Adapter, Signal-Regeln, Rollen-Check) dokumentiert an das Pattern-Team übergeben | nicht vorhanden | Ende Phase 3 |

---

## Nicht-Ziele

| Nicht-Ziel | Warum nicht | Wohin |
|---|---|---|
| **Voller CRM-Abgleich aller Kontakte** mit Überschreiben von Feldern | Das ist Bedürfnis 2 mit eigenem Käufer und eigenem Risiko (Schreibrechte, "The API sync broke again at 3 AM."). Im MVP läuft der Rollen-Check nur für Prospects mit Dossier. | Phase 2, eigenes Angebot an Sales Ops |
| **Automatischer Versand** von E-Mails oder Nachrichten | Gefährdet Antwortquote und Vertrauen (Alternative A2). | Nie in diesem Auftrag |
| **Account-Karte** für Großkunden (wer berichtet an wen, wer ist Blocker) | Deutlich schwieriger, braucht stabile Stufe 1. Petit beschreibt Tage Arbeit, das ist ein eigener Umfang. | Phase 2, nach dem Pilot |
| **Listenbau aus Anlässen** (*zeig mir alle neuen CTOs bei Series-B-Firmen*, wie Chen und Green es wollen) | Ist Prospect-Suche, nicht Prospect-Vorbereitung. Nutzt dieselben Bausteine, ist aber ein anderer Ablauf. | Phase 2 |
| **Einigung Marketing und Sales** auf einen guten Lead | Organisationsfrage, kein ersetzbarer Skill (S1). | Anderer Auftrag (kein Agent-Projekt) |
| **Lizenzbeschaffung** (ZoomInfo, Sales Navigator) | Einkauf, keine Agent-Arbeit (Alternative A3). | Nie |
| **Produkt für viele Kunden** | Strategie: wir bauen kundenspezifisch. | Pattern-Team entscheidet nach Übergabe (N3) |

---

## Logik

Jede Regel ist als Testfall formuliert: Eingabe → erwartetes Verhalten. Startwerte mit Verweis auf A-Nummern sind Annahmen und konfigurierbar.

**Datenmodell Dossier:** `prospect_id`, `erstellt_am`, `rollen_status` (`bestätigt` | `gewechselt` | `unklar`), `rollen_quelle`, `neue_firma` (optional), `nachfolger_kandidat` (optional, mit Quelle), `anlaesse[]` (je `kategorie`, `datum`, `inhalt`, `quell_url`, `belegauszug`), `aufhaenger` (optional), `gepruefte_quellen[]`, `warnhinweise[]`.

| Regel | Was gilt | Testfall (Eingabe → erwartet) |
|---|---|---|
| **R1 Pflichtfelder** | Ohne Name und Firma wird kein Dossier erzeugt. | Prospect ohne Firma → Status `Eingabe unvollständig`, kein Dossier, Meldung an den Nutzer |
| **R2 Rollen-Check zuerst** | Vor allen Anlässen sucht der Agent die aktuelle Firma der Person in den freigegebenen Quellen. Gleiche Firma wie im CRM → `bestätigt`. Andere aktuelle Firma in mindestens einer Quelle → `gewechselt`. Keine Quelle oder Quellen widersprechen sich → `unklar`. | CRM: Firma X; Quelle: aktuell bei Firma Y → `gewechselt`, `neue_firma` = Y |
| **R3 Bei Wechsel** | Für die alte Firma werden keine personenbezogenen Anlässe erzeugt. Der Agent sucht in der alten Firma eine Person mit gleichem Titel nach Normalisierung (Kleinschreibung, Leerzeichen bereinigt) und trägt sie als `nachfolger_kandidat` mit Quelle ein. Der Wechsel selbst wird als Anlass `neue Rolle` für die neue Firma geführt. | Person wechselte von X zu Y; bei X hat jemand denselben Titel → Dossier zeigt Y, Nachfolger-Kandidat bei X mit Link, keine X-Anlässe zur Person |
| **R4 Bei unklar** | Das Dossier wird erzeugt, `warnhinweise` enthält *Rolle nicht bestätigt*. | Keine Quelle findet die Person → Dossier mit Warnhinweis oben |
| **R5 Kategorien** | Erlaubt sind nur: `Finanzierung`, `Neueinstellungen` (Bereiche je Kunde konfigurierbar, Start: Engineering und Ops laut O'Neil), `Führungswechsel` (VP-Ebene), `neue Rolle` der Person, `Thema` (Themenliste je Kunde). | Fund passt in keine Kategorie (z. B. Urlaubsfoto) → wird verworfen |
| **R6 Zeitfenster** | `Finanzierung`, `Neueinstellungen`, `Führungswechsel`: nicht älter als A7. `neue Rolle`: Rollenbeginn vor weniger als 6 Monaten (Chen). `Thema`: Beitrag aus den letzten 7 Tagen (Green: "in the last week"). | Finanzierungsmeldung älter als A7 → verworfen |
| **R7 Quellenpflicht** | Jeder Anlass braucht `quell_url`, `datum` und einen gespeicherten `belegauszug` aus der Quelle. Fehlt eines davon, wird er verworfen. `inhalt` darf nur aussagen, was im Belegauszug steht. | Anlass ohne Datum → nicht im Dossier |
| **R8 Auswahl** | Höchstens drei Anlässe. Reihenfolge nach Kategorie-Priorität (Start: Finanzierung, Neueinstellungen, Führungswechsel, neue Rolle, Thema; je Kunde änderbar), innerhalb einer Kategorie der neueste zuerst. | Fünf gültige Anlässe → die drei nach Priorität, Rest verworfen |
| **R9 Null-Fall** | Kein gültiger Anlass → Dossier zeigt *Kein aktueller Anlass gefunden*, kein Aufhänger, Prospect wird markiert. Der Agent erfindet keinen Ersatz. | Keine Funde → Dossier ohne Aufhänger, Markierung gesetzt |
| **R10 Aufhänger** | Nur wenn mindestens ein Anlass vorhanden ist. Er nennt mindestens einen Anlass ausdrücklich. Es gibt keine Versandfunktion. | Ein Anlass `Finanzierung` → Aufhänger bezieht sich auf die Finanzierung |
| **R11 Länge** | Das ganze Dossier hat höchstens A9 Wörter, damit es in unter zwei Minuten lesbar ist. | Entwurf zu lang → Inhalte kürzen, nie Quellen entfernen |
| **R12 Ausgabe** | Das Dossier wird als Notiz am CRM-Kontakt abgelegt. Kontaktfelder werden nie überschrieben. Bei `gewechselt` wird zusätzlich ein Hinweis-Feld gesetzt. | Status `gewechselt` → Notiz plus Hinweis, Feld *Firma* im CRM unverändert |
| **R13 Gültigkeit** | Ein Dossier gilt A8. Fragt jemand innerhalb dieser Zeit erneut an, kommt das gespeicherte Dossier mit Erstelldatum. *Neu erzeugen* erzwingt einen neuen Lauf. | Zweite Anfrage am selben Tag → gespeichertes Dossier, kein neuer Lauf |
| **R14 Rückmeldung** | Nutzer können jeden Anlass als *falsch* markieren. Das wird gespeichert und für G2 gezählt. | Klick auf *falsch* → Zähler G2 erhöht, Anlass im Dossier markiert |
| **R15 Protokoll** | Jede Erzeugung speichert Zeit, Nutzer, Auslöser, geprüfte Quellen und ob das Dossier geöffnet wurde. | Dossier geöffnet → Ereignis mit Zeitstempel im Protokoll (für Z1, Z5) |
| **R16 Quellen-Freigabe** | Nur Quellen-Adapter auf der Freigabeliste des Kunden laufen. Das Dossier listet in `gepruefte_quellen`, was geprüft wurde. | LinkedIn-Adapter gesperrt → Dossier entsteht aus den übrigen Quellen, Kopfzeile zeigt *LinkedIn nicht geprüft* |
| **R17 Laufzeit** | Einzel-Dossier fertig innerhalb von A10. Der Stapel für den nächsten Arbeitstag ist vor Arbeitsbeginn fertig. | Stapel mit allen zugeordneten Prospects → alle Dossiers liegen am Morgen vor |

---

## Plan

| Phase | Was | Aufwand (Annahme) | Ergebnis | Entscheidung am Ende |
|---|---|---|---|---|
| **0: Klärung** | Budget-Inhaber klären (VP Sales, Enablement oder Sales Ops). Zugang zum CRM, Freigabeliste der Quellen, Themenliste und Kategorie-Priorität festlegen. Messplan für Z1 bis Z5 und G1, G2. | A1 | Angebot für Phase 1 und 2, Messplan | Go für Bedürfnis 1, oder Umkehr auf Bedürfnis 2 (Anhang A.5) |
| **1: Spike** | Quellen-Adapter für die freigegebenen Quellen, Rollen-Check (R2, R3), Signal-Regeln (R5 bis R9) an echten Prospects des Kunden. Rechtliche Prüfung des LinkedIn-Zugriffs parallel. | A2 | Machbarkeitsnachweis: Anteil Prospects mit mindestens einem gültigen Anlass, Fehlerquote in Stichprobe | Weiter, Quellen einschränken oder stoppen |
| **2: Pilot** | Dossier im CRM für die Pilotgruppe aus dem Lead-Gen-Team (Ross: "A dozen bright kids"), Vergleichsgruppe ohne Dossier. Ausgangswerte in Woche 1. | A3, Dauer A4 | Messwerte Z1 bis Z5, G1, G2 | Rollout, nachbessern oder abbrechen |
| **3: Rollout** | Alle SDRs und AEs. Einarbeitung neuer Reps mit Dossier, gemeinsam mit O'Neil. Übergabe der Bausteine an das Pattern-Team (N3). | A5 | Laufender Betrieb, Wartung (A12) | Phase 2 beauftragen? |
| **Phase 2 (Option)** | CRM-Abgleich für Sales Ops, Account-Karte, Listenbau aus Anlässen | `[Platzhalter]`, eigenes Angebot | eigenes Angebot | Kunde |

Team: 2 bis 3 Personen (A6). Bis zum Pilot-Ergebnis 33 bis 50 Personentage (A1 + A2 + A3).

---

## Risiken und Einwände

Antworten mit Beleg, oder ausdrücklich als offenes Risiko markiert.

| # | Risiko oder Einwand | Antwort | Stand |
|---|---|---|---|
| E1 | **Datenzugriff und Recht:** *Darf der Agent LinkedIn überhaupt auslesen? Und personenbezogene Daten verarbeiten?* LinkedIn ist die Hauptquelle: "9 times out of 10? LinkedIn." (O'Neil), "It’s 90% LinkedIn." (Kim) | Rechtliche Prüfung in Phase 1, vor dem Pilot. Der Agent läuft nur über freigegebene Adapter (R16) und funktioniert auch ohne LinkedIn mit Firmenseiten, Pressemitteilungen und Finanzierungsdatenbanken, dann mit mehr `unklar`-Status. | **Offenes Risiko**, Entscheidung in Phase 1 |
| E2 | **Erfundene oder falsche Anlässe:** *Wenn das Dossier einmal falsch liegt, blamiert sich der Rep, wie Baker mit dem Artikel.* | Kein Anlass ohne Quelle, Datum und Belegauszug (R7). Kein Aufhänger ohne Anlass (R9, R10). Rückmeldung *falsch* (R14) und Guardrail G2. | Beantwortet; Fehlerquote wird im Pilot gemessen |
| E3 | **Die Erfahrenen nutzen es nicht**, weil sie selbst deuten wollen ("You have to read between the lines"). | Das Dossier ist Vorarbeit: höchstens drei Anlässe, Quellen zum Nachlesen, kein Versand (R10). Z5 misst die Nutzung. Petit und Chen als frühe Testnutzer in Phase 2. | Beantwortet; Nutzung wird gemessen |
| E4 | **Automatisierte Massenansprache:** *Das Volumen steigt, die Qualität fällt, wir verlieren die persönliche Note.* Ross: "I want speed, they want quality, and right now we have neither." | Kein automatischer Versand (Nicht-Ziel). G1 vergleicht die Antwortquote mit einer Vergleichsgruppe. | Beantwortet |
| E5 | **Das löst unser CRM-Problem nicht.** *Unsere Daten sind zur Hälfte veraltet.* Kim: "Our CRM is a graveyard." | Stimmt für den Bestand. Der Rollen-Check markiert veraltete Kontakte vor jedem Dossier (R2, R3, Z4) und schreibt einen Hinweis ins CRM (R12). Den vollen Abgleich bieten wir als Phase 2 an. | Beantwortet, mit Grenze |
| E6 | **Wir haben schon ZoomInfo.** *Warum noch ein Werkzeug?* | Vorhandene Lizenzen liefern Rohdaten. Trotzdem recherchieren die Leute von Hand, und Kim sagt: "they break, or they’re too expensive to run on every single contact record". Der Agent liefert die Auswahl und den Aufhänger, nicht die Rohdaten (Alternative A3). | Beantwortet |
| E7 | **Was kostet es, und wann zahlt es sich aus?** | Aufwand bis Pilot-Ergebnis 33 bis 50 Personentage (A1 + A2 + A3). Preis: `[Platzhalter]`. Der Nutzen wird im Pilot gegen die eigene Rechnung des VP gemessen (4 Prospects pro Stunde, Z1, Z2). Eine Umsatzwirkung in Geld behaupten wir nicht. | **Offen**, kaufmännische Entscheidung |
| E8 | **Budget liegt woanders:** Druck beim VP ist belegt, Budget nicht. | Phase 0 klärt es. Hat nur Sales Ops Budget, kehrt sich die Reihenfolge um (Anhang A.5). Der Rollen-Check ist in beiden Fällen der gemeinsame Kern. | **Offenes Risiko** |
| E9 | **Wartung:** Quellen ändern sich, der Agent bricht, wie Kims Tools: "The API sync broke again at 3 AM." | Adapter je Quelle, Ausfall einer Quelle stoppt nicht das Dossier (R16). Wartungsaufwand A12 im Angebot. | Beantwortet, Aufwand Annahme |
| E10 | **Nur ein Kunde befragt:** Das Muster trägt vielleicht nicht über diesen Kunden hinaus. | Für dieses Projekt egal, es ist kundenspezifisch. Für die Produktidee: Übergabe an das Pattern-Team (N3), kein Produktversprechen. | Offenes Risiko für S3, nicht für das Projekt |
| E11 | **Integration ins CRM:** *Noch ein Tab mehr?* Ross: "They’re jumping between five different tabs." | Das Dossier liegt am CRM-Kontakt (R12), kein eigenes Werkzeug. | Beantwortet; CRM-Zugang wird in Phase 0 geklärt |

---

## Offene Punkte

Keine dieser Fragen blockiert den Bau. Für jede gibt es eine Startannahme.

1. **Zulässiger Zugriff auf LinkedIn und Datenschutz.** Start ohne LinkedIn-Adapter, Freischaltung nach rechtlicher Prüfung (R16). Klärung in Phase 1.
2. **Wer hat das Budget?** Klärung in Phase 0. Kippt die Wahl, gilt Anhang A.5.
3. **Ausgabekanal.** Start: Notiz am CRM-Kontakt (R12). Ob zusätzlich E-Mail oder Chat gewünscht sind, klären wir in Phase 0 mit Kim und den Nutzern.
4. **Themenliste und Kategorie-Priorität.** Start: O'Neils Checkliste. Die Themen hängen vom Produkt des Kunden ab. Festlegung in Phase 0.
5. **Zielwerte für Z2 bis Z5.** Festlegung mit dem Kunden in Phase 0.
6. **Kaufmännisches:** Tagessatz, Angebotssumme, ob Phase 0 berechnet wird: `[Platzhalter]`, Entscheidung beim Management von NeoEmployee.
7. **Muster bei anderen Kunden:** Frage an das Pattern-Team.

### Annahmen (nicht belegt)

| # | Annahme | Begründung | Ersetzt durch Messwert |
|---|---|---|---|
| A1 | Aufwand Phase 0: 3 bis 5 Personentage | Gespräche mit vier Käufer-Rollen (VP Sales, Sales Director, Enablement, Sales Ops) plus Messplan | Gebuchte Stunden am Ende von Phase 0 |
| A2 | Aufwand Phase 1: 10 bis 15 Personentage, Dauer 2 Wochen | Drei bis vier Quellen-Adapter, Rollen-Check, Signal-Regeln, an echten Prospects | Gebuchte Stunden am Ende von Phase 1 |
| A3 | Aufwand Phase 2: 20 bis 30 Personentage | CRM-Integration, Stapel-Lauf, Protokoll, Betreuung des Piloten und Auswertung | Gebuchte Stunden am Ende des Piloten |
| A4 | Pilotdauer 4 Wochen; Pilot- und Vergleichsgruppe je 4 bis 6 SDRs | Genug Arbeitstage für einen Vergleich; beide Gruppen passen in das Lead-Gen-Team von zwölf Leuten (Ross: "A dozen") | Statistische Prüfung der Messwerte nach Woche 2 des Piloten; bei zu wenig Daten verlängern |
| A5 | Aufwand Phase 3: 15 bis 25 Personentage | Ausrollen auf alle Reps, Einarbeitung, Übergabe an das Pattern-Team | Plan nach dem Pilot auf Basis der echten Pilot-Aufwände |
| A6 | Team 2 bis 3 Personen | Von 14 Leuten sind 2 im Pattern-Team, also 12 verfügbar; 2 bis 3 belasten die übrigen Projekte nicht zu stark | Ressourcenplanung in Phase 0 |
| A7 | Zeitfenster Finanzierung, Neueinstellungen, Führungswechsel: 90 Tage | Ältere Anlässe taugen kaum als Grund, *jetzt* anzurufen | Auswertung im Pilot: Antwortquote nach Alter des Anlasses (G1) |
| A8 | Dossier gilt 7 Tage | Anlässe ändern sich selten täglich; spart Läufe und Kosten | Auswertung im Pilot: Anteil Dossiers, die nach Neu-Erzeugung anders aussehen |
| A9 | Dossier höchstens 150 Wörter | Lesbar in unter 2 Minuten (O'Neils Marke) | Lesezeit aus Protokoll R15 im Pilot |
| A10 | Einzel-Dossier fertig in höchstens 5 Minuten | Schneller als jede heutige Handrecherche (15 bis 40 Min.) | Laufzeitmessung in Phase 1 |
| A11 | Bewertungsskala 1 bis 3 und Gewichte 1 oder 2 in Anhang A | Einfache Setzung, damit die Gewichtungen vergleichbar sind; die Begründungen tragen die Bewertung | Nach Phase 0 mit dem tatsächlichen Budget-Inhaber neu bewerten |
| A12 | Wartung nach Rollout: 2 bis 4 Personentage pro Monat | Quellen und Schnittstellen brechen erfahrungsgemäß (Kim: "they break") | Tatsächlicher Wartungsaufwand nach drei Monaten Betrieb |

---

## Anhang A: Bewertung der Bedürfnisse

### A.1 Kriterien und Bewertung

Skala 1 bis 3 (A11): 3 = stark für wirtschaftlichen Erfolg, 1 = schwach.

| # | Kriterium | B1 | Begründung B1 | B2 | Begründung B2 |
|---|---|---|---|---|---|
| K1 | **Verbreitung** | 3 | 9 von 10, alle Ebenen von Junior SDR bis VP | 2 | 5 von 10, Petit nur teilweise |
| K2 | **Käufer und Budgetnähe** | 2 | Mehrere Käufer mit Druck: Board beim VP, Einarbeitungs-KPI bei O'Neil, Blunt mit eigenem Budget ("my budget"). Freigegebenes Budget für dieses Thema ist aber nicht belegt. | 3 | Ein klarer Käufer, der den Stack verantwortet und heute schon für Anreicherungs-Tools zahlt ("too expensive to run on every single contact record") |
| K3 | **Art des Nutzens** | 3 | Umsatzhebel: "I'd double my numbers." (Chen), Termine für die Closer (Ross) | 2 | Vor allem Kostensenkung aus Käufersicht ("copy-paste machine"); Jenkins sieht zwar auch Umsatz ("I could double my quota"), sie ist aber nicht der Käufer |
| K4 | **Abgrenzung vom Wettbewerb** | 3 | Kein vorhandenes Werkzeug liefert die Synthese; trotz Lizenzen wird von Hand recherchiert | 1 | ZoomInfo und Clearbit sind vorhanden; wir müssten gegen Werkzeuge antreten, die der Kunde schon bezahlt |
| K5 | **Musterpotenzial (S3)** | 3 | Generische Signal-Kategorien (O'Neils Checkliste), keine Standard-Lösung für die Synthese | 2 | Generisch, aber der Markt ist mit Standardwerkzeugen besetzt; als Produktkeim weniger wert |
| K6 | **Umsetzungsrisiko** (3 = gering) | 1 | Auswahl und Aufhänger sind Interpretation; Fehler wirken sofort im Gespräch; Quellenzugriff ungeklärt | 2 | Abgleich ist eher Datenabgleich als Deutung; dafür Schreibrechte im CRM und Sync-Probleme ("The API sync broke again at 3 AM.") |
| K7 | **Eigenständigkeit** | 1 | Braucht aktuelle Kontaktdaten, sonst Dossiers über Leute, die gegangen sind | 3 | Steht für sich und ist Grundlage für B1 |
| K8 | **Messbarkeit** | 3 | Zielmarke vom Kunden ("under two minutes"), bestehender KPI (50 Calls) | 3 | Anteil veralteter Kontakte (etwa 40 %), Bounces |

### A.2 Gewichtungen

Gewicht 1 = normal, 2 = doppelt (A11). Summe = Punkte × Gewicht.

| Gewichtung | Was doppelt zählt | B1 | B2 | Ergebnis |
|---|---|---|---|---|
| **G-a Gleich** | nichts | 19 | 18 | B1 knapp vorn |
| **G-b Runway** (S2: schneller bezahlter Abschluss) | K2, K3 | 24 | 23 | B1 knapp vorn |
| **G-c Brücke** (S3: Produktkeim) | K4, K5 | 25 | 21 | B1 deutlich vorn |
| **G-d Risiko** (Bootstrap: kein Fehlschlag leisten) | K6, K7 | 21 | 23 | **B2 vorn** |

Rechenweg G-a: B1 = 3+2+3+3+3+1+1+3 = 19; B2 = 2+3+2+1+2+2+3+3 = 18. Die anderen Zeilen addieren die doppelt gezählten Kriterien ein zweites Mal (z. B. G-d: B1 = 19+1+1 = 21; B2 = 18+2+3 = 23).

### A.3 Ergebnis und Robustheit

B1 gewinnt in drei von vier Gewichtungen. Der Vorsprung ist aber knapp, außer bei der Brücken-Gewichtung. Er beruht vor allem auf Verbreitung, Nutzenart und Wettbewerb. Die Schwäche von B1 ist K7: Ohne aktuelle Kontaktdaten trägt es nicht.

**Variante B1 mit Rollen-Check:** Übernimmt B1 den Rollen-Check aus B2 als MVP-Baustein, steigt K7 für B1 von 1 auf 2 (*abhängig, aber selbst abgesichert*). Dann gilt: G-a 20 zu 18, G-b 25 zu 23, G-c 26 zu 21, G-d 23 zu 23. B1 mit Rollen-Check verliert in keiner Gewichtung mehr. **Das ist die gewählte Variante.**

### A.4 Strategie-Prüfung beider Bedürfnisse

| | B1 | B2 |
|---|---|---|
| S1 Vision-Filter: ersetzt einen Mitarbeiter-Skill | ✔ Prospect-Researcher | ✔ Data Clerk ("I want to sell, not be a data clerk.", Baker) |
| S2 Umsatz: als T&M-Projekt verkaufbar | ✔ mehrere Käufer mit Druck | ✔ ein Käufer mit vorhandenen Ausgaben |
| S3 Muster: nicht kundenspezifisch | ✔ mit Einschränkung (ein Kunde) | ✔ mit Einschränkung (ein Kunde) |

Die Strategie lässt beide zu. Den Ausschlag geben K1, K3 und K4, und alle drei hängen an S2: Wir nehmen das Bedürfnis, bei dem ein bezahlter Abschluss und ein Folgeauftrag wahrscheinlicher sind.

### A.5 Schicksal des Verlierers und wann die Wahl kippt

**B2:** Rollen-Check als MVP-Baustein (R2, R3, R12). Voller CRM-Abgleich als Phase 2, eigenes Angebot an Sales Ops.

**Wir wechseln auf B2 zuerst, wenn:**
- Phase 0 zeigt, dass nur Sales Ops Budget freigibt (E8).
- Phase 1 zeigt, dass Anlässe nicht zuverlässig mit Quelle zu finden sind, der Rollen-Abgleich aber schon.
- Der Kunde zuerst seine Datenbasis bereinigen will.

---

## Loop-Protokoll

wird vom Koordinator geführt
