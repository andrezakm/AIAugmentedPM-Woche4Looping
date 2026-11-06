# PRD: Dossier-Agent (Arbeitstitel), der fertige Grund zum Anrufen

**Stand:** 2026-11-05 (überarbeitet nach Review-Runde 1)
**Autor:** Produktmanagement NeoEmployee
**Grundlage:** `output/interview-synthesis-2026-11-03.md` (zwei Bedürfnisse aus zehn Interviews), Originalinterviews in `input/`, `context/company.md`, `context/strategy.md`
**Zitat-Konvention:** Interview-Zitate in "…" (gerade Anführungszeichen), wörtlich aus `input/`. Strategie-Zitate in „…“, wörtlich aus `context/`. Eigene Umschreibungen *kursiv*. Fehlende Zahlen stehen als `[Platzhalter]`. Werte, die wir setzen, ohne dass sie in den Quellen stehen, sind als *Annahme* markiert.

---

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

## Problem

**Wer spricht hier:** Alle zehn Befragten arbeiten in derselben Vertriebsorganisation, bei einem Kunden von NeoEmployee, nicht bei uns. Die Interviews sind auf Englisch geführt; die Zitate stehen deshalb im Original, die deutsche Bedeutung steht jeweils daneben oder kursiv dahinter.

### Begriffe

| Begriff | Bedeutung hier |
|---|---|
| **Lead / Prospect** | Ein Kontakt, der Kunde werden könnte. Lead: noch unbearbeitet, meist vom Marketing geliefert. Prospect: jemand, den ein Vertriebler gezielt ansprechen will. |
| **Account** | Eine ganze Zielfirma mit mehreren Ansprechpartnern. |
| **SDR** (Sales Development Rep) | Einstiegsrolle im Vertrieb: ruft an, schreibt an und vereinbart Termine. |
| **AE** (Account Executive) | Führt die Termine, verhandelt und schließt ab. **Enterprise AE:** dasselbe für große Firmen mit vielen Beteiligten. |
| **Sales Director / VP of Sales** | Führungskräfte des Vertriebs; der VP of Sales verantwortet die Zahlen gegenüber dem Board (Aufsichtsgremium). |
| **Dir. Sales Enablement** | Verantwortet Einarbeitung und Training der Vertriebler. |
| **Sales Ops** | Betreut CRM und Werkzeuge des Vertriebs. |
| **CRM** | Die Kundendatenbank des Vertriebs, hier Salesforce. |
| **KPI** | Vorgegebene Kennzahl, hier 50 Anrufe pro SDR und Tag. |
| **Conversion / Antwortquote** | Anteil der Angesprochenen, die antworten oder einen Termin machen. |
| **Personalisierung** | Die Ansprache auf die Person zuschneiden, statt allen dasselbe zu schicken. |
| **Signal** | Ein aktueller, öffentlich belegbarer Anlass, jemanden jetzt anzusprechen, z. B. eine Finanzierungsrunde, neue Stellenausschreibungen, ein Führungswechsel, ein Beitrag zu einem Thema. |
| **Gesprächsaufhänger** | Der erste Satz, mit dem man an ein Signal anknüpft. |
| **Dossier** | Eine kurze, fertige Zusammenfassung pro Person: Rolle, Signale, Aufhänger, Quellen. |
| **Talk Track** | Vorbereiteter Gesprächsleitfaden. |
| **Agent** | Eine KI-gestützte Software, die eine Aufgabe selbstständig erledigt. Kein Mensch, kein Chatbot zum Plaudern. |

**Kern:** Die Informationen für eine gute Ansprache sind öffentlich verfügbar, aber verstreut über viele Webseiten und vermischt mit viel Unwichtigem (*verrauscht*). Heute sucht ein Mensch sie von Hand zusammen und macht daraus einen Gesprächsaufhänger. Das kostet pro Prospect 15 Minuten bis mehrere Tage. Darum werden entweder zu wenige Menschen angesprochen, oder die Ansprache wird allgemein und es antworten weniger.

Der VP of Sales beschreibt den Engpass so: "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck." *Sie machen aus ungeordnetem Rauschen von Hand Gesprächsleitfäden.* Es fehlen nicht die Daten. Es fehlt die fertige Zusammenfassung daraus (*Synthese*). Die Enablement-Direktorin bestätigt das: "The problem isn't that the data is missing". Was genau fehlt, zeigt das Beispiel-Dossier im Abschnitt *Lösung*.

### Was es heute kostet (nur Zahlen aus den Interviews)

| Wer | Was | Zitat |
|---|---|---|
| Marcus Thorne, VP of Sales | 15 Min. pro Prospect, also 4 pro Stunde | "If you do the math, that's only 4 prospects an hour. That's a joke." |
| Linda O'Neil, Dir. Sales Enablement | 40 Min. ohne Ergebnis bei neuen Reps | "suddenly forty minutes have passed and they haven't actually found a reason to call" |
| Mike Ross, Sales Director | 20 Min. für eine E-Mail, kaum Output | "the output is a trickle. Droplets." *(Es kommt nur tröpfchenweise etwas heraus.)* |
| Rachel Green, Junior SDR | 30 Min. für eine E-Mail | "30 minutes for one email!" |
| Jessica Chen, AE (Top-Performerin) | 4 Std. abends für 10 Kontakte | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Sam Petit, Enterprise AE | Tage pro Account, um herauszufinden, wer in der Firma wer ist | "I spend days—literal days—just mapping an account" |
| Sarah Jenkins, SDR | 20 statt 50 Calls pro Tag, weil sie Daten von Hand prüft und ins CRM überträgt | "I’m lucky if I get to 20 because I’m stuck copy-pasting job titles from LinkedIn profiles into Salesforce fields" |
| Emily Blunt, Marketing Manager | Kontext nur für 5 von 100 Leads | "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |

**In Geld:** Die Interviews nennen Zeit, keine Gehälter der Vertriebler und keinen Umsatz pro Termin. Der Geldwert ist deshalb `[Platzhalter]` und wird in Phase 0 mit dem Kunden berechnet: *verlorene Recherchezeit × Personalkosten* und *entgangene Termine × Wert eines Termins*. Die einzige Gehaltsangabe betrifft Bedürfnis 2 (Sales Ops: "$80k a year").

### Warum man nicht einfach auf Personalisierung verzichten kann

Die Führung sagt *schneller wählen*. Ross will die Leute "Dialing!" sehen, Thorne sagt "Go faster." Die Basis und das Marketing halten dagegen, dass Kontext die Antwortquote trägt. Blunt räumt ein: "conversion is higher if you know the context". Green hat es erlebt: Mit einem persönlichen Aufhänger kam eine Antwort ("He actually replied!"). Der erfahrenste Verkäufer, Tom Baker, kannte einen Artikel des Kunden nicht: "I looked like a dinosaur."

**Wer entscheidet, und löst das den Streit?** Entscheiden tut beim Kunden die Vertriebsführung. Sie will aber selbst beides: Thorne "I need shotgun coverage with sniper precision. I need both." *(Breite Abdeckung und trotzdem gezielt.)* Ross: "I want speed, they want quality, and right now we have neither." Der Streit entsteht nur, weil Personalisierung heute teuer ist. *Personalisierung muss also billig werden, nicht wegfallen.* Ob das Dossier den Streit wirklich löst, zeigt der Pilot: mehr Calls bei gleicher oder besserer Antwortquote (Z2, Z5).

### Was bleibt beim Menschen

Erfahrene Verkäufer wollen die Deutung behalten. Petit: "You have to read between the lines" *(zwischen den Zeilen lesen)*. Chen: "Because I have to know *everything* about them." *Der Agent übernimmt das Sammeln, Filtern und Strukturieren, nicht das Urteil.* Daraus folgt eine Anforderung: Jedes Signal braucht einen Link auf die Quelle, damit der Mensch in Sekunden nachlesen kann, ob der Anlass stimmt, bevor er sich darauf beruft.

### Das Datenproblem darunter

Ein Dossier über jemanden, der nicht mehr im Unternehmen ist, schadet. Jenkins prüft deshalb heute *vor* jedem Kontakt auf LinkedIn, ob die Person noch dort ist, "to see if the person is actually still employed there. If they aren’t, which is like 40% of the time". Rutscht etwas durch, fällt es erst beim Anruf oder an der zurückgekommenen E-Mail auf: "Half the emails bounce immediately". Veraltete Kontaktdaten im CRM sind das zweite Bedürfnis, das die Interviews zeigen (Bedürfnis 2). Für den Dossier-Agenten zählt davon nur ein Teil: Vor jedem Dossier wird automatisch geprüft, ob die Person noch in der Rolle ist. Das nimmt Jenkins genau den Prüfschritt ab, den sie als Grund für ihre niedrige Call-Zahl nennt: "if I didn't have to verify every single lead, I could double my quota".

---

## Warum dieses Problem (Wahl und Strategie)

### Die Wahl

Die Synthese lässt zwei Bedürfnisse übrig. Beide bestehen die drei Strategie-Prüfungen. Die Frage ist also nicht *passt es?*, sondern *welches bringt mit höherer Wahrscheinlichkeit Geld?* Wir haben beide Bedürfnisse nach acht Faktoren verglichen (Bewertung und Gewichtungen in Anhang A):

1. **Wie viele haben das Problem?** Bedürfnis 1: 9 von 10, über alle Ebenen von Junior SDR bis VP. Bedürfnis 2: 5 von 10.
2. **Wer kauft, und wie dringend?** Bedürfnis 1 hat drei Käufer mit Druck. Der VP of Sales kam gerade aus dem Board-Meeting: "dress for the job you want, or the job you're trying to save". Der Sales Director nennt den Engpass als Erstes: "They are starving for good meetings." Die Enablement-Direktorin hat einen eigenen KPI: "It's a massive drain on our ramp time." Bedürfnis 2 hat einen Käufer, David Kim (Sales Ops). Sein Schmerz ist echt ("Data integrity. 100%."), aber er ist für den Stack zuständig, nicht für den Umsatz.
3. **Umsatz oder Kostenersparnis?** Bei Bedürfnis 1 rechnen die Betroffenen selbst in Umsatz. Chen: "I'd double my numbers." Thorne: "we’d be unstoppable." Bei Bedürfnis 2 rechnet der Käufer in Kosten: "Why do I have a human being paid $80k a year acting as a copy-paste machine?" *Ein Umsatzhebel rechtfertigt ein T&M-Budget leichter als eine Kostensenkung, die man gegen bestehende Lizenzen aufrechnet.*
4. **Gegen wen treten wir an?** Bei Bedürfnis 2 hat der Kunde schon ZoomInfo und Clearbit. Kim sagt, sie seien zu teuer für jeden Datensatz. Ein maßgeschneiderter Agent auf T&M-Basis muss sich also an einem Preis messen lassen, den der Käufer schon heute zu hoch findet. Bei Bedürfnis 1 gibt es beim Kunden kein Werkzeug, das die Synthese macht. Die vorhandenen Lizenzen liefern Rohdaten, und die Leute recherchieren trotzdem von Hand.
5. **Wie gut lässt sich Erfolg zeigen?** Bei Bedürfnis 1 gibt es eine Zielmarke, die der Kunde selbst gesetzt hat (unter 2 Minuten), und einen bestehenden KPI (50 Calls pro Tag). Bei Bedürfnis 2 ist Erfolg ebenfalls messbar (Bounce-Quote, veraltete Datensätze). Hier liegen beide gleich.
6. **Taugt es als Muster für spätere Produkte?** Die Signal-Typen sind generisch. O'Neils Checkliste ist kein Sonderfall dieses Kunden: "1. Recent funding news—Series B or C preferably. 2. New hiring in engineering or ops. 3. Recent leadership changes at the VP level." Bedürfnis 2 ist ebenfalls ein Muster, aber eines, für das es schon Standardsoftware gibt. *Ein Produktkeim in einem besetzten Markt ist weniger wert.*
7. **Wie hoch ist das technische Risiko?** Bei beiden mittel: gleicher Quellenzugriff (vor allem LinkedIn). Bedürfnis 1 hat zusätzlich das Risiko falscher Signale, Bedürfnis 2 den Schreibzugriff ins CRM. Gleichstand.
8. **Wie abhängig ist es vom anderen?** Hier liegt Bedürfnis 2 vorn: Es steht für sich, während Bedürfnis 1 aktuelle Kontaktdaten braucht. Diesen Nachteil gleichen wir aus, indem der Rollen-Check Teil des Dossier-Agenten wird.

**Ergebnis:** Bedürfnis 1 liegt bei fünf von acht Faktoren vorn (F1 bis F4, F6), bei zwei gleichauf (F5, F7) und bei einem hinten (F8). Wir haben das Ergebnis mit vier Gewichtungen durchgerechnet (Anhang A.3): Bei gleicher Gewichtung, bei Betonung von Umsatz und Runway und bei Betonung des Lieferrisikos liegt Bedürfnis 1 vorn. Nur wenn man unterstellt, dass die vorhandenen Werkzeuge den Unterschied bei Nutzen und Wettbewerb aufheben, steht es gleich. Wir wählen Bedürfnis 1.

**Was wir von Bedürfnis 2 trotzdem mitnehmen:** Den Abgleich *ist die Person noch in dieser Rolle?* für jeden Prospect, der ein Dossier bekommt. Mehr nicht. Ein vollständiger CRM-Abgleich für alle Kontakte ist ein eigenes Projekt (siehe Nicht-Ziele und Offene Punkte). Die Prüfung im Dossier-Agenten ist aber der natürliche Einstieg dafür: Sie liefert Kim schon im ersten Projekt Belege, und sie öffnet ein zweites Gespräch mit einem zweiten Budget.

**Was gegen die Wahl spricht:** Bedürfnis 2 hat den klarer abgrenzbaren Käufer, und Kim hat die Lösung ebenfalls fast selbst beschrieben. Wenn sich in der Klärung zeigt, dass beim VP of Sales kein Budget frei ist, beim Sales Ops aber schon, kehrt sich die Reihenfolge um. Das ist der wichtigste offene Punkt (siehe Offene Punkte, Nr. 1).

### Abgleich mit der Strategie

| Strategie (`context/`) | Wie der Dossier-Agent passt |
|---|---|
| **Vision-Filter:** „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ | Der Agent ersetzt einen abgrenzbaren Skill: den Prospect-Researcher. O'Neil beschreibt ihn so: "We’re essentially teaching them to be high-priced data miners." |
| **Bootstrap:** „anything that brings in money and aligns with our vision, we do.“ und „Revenue is runway“ | Drei Käufer mit Druck und eine Kennzahl, auf die das Board schaut. Das erhöht die Chance auf einen schnellen Abschluss. Der gedeckelte Einstieg bringt früh die erste Rechnung. |
| **Geschäftsmodell:** „We bill on a time-and-material basis.“ und „Every agent is built custom for the client“ | Das Projekt wird für diesen Kunden gebaut und nach Aufwand abgerechnet. Quellen, Signal-Regeln und Ausgabekanal sind kundenspezifisch. |
| **Prozess:** „Identify bottlenecks“ → Skill-Gap → Agent bauen | Der Engpass wurde vom Kunden selbst benannt ("That’s the bottleneck."), der Skill-Gap ist klar. |
| **Die Brücke:** „These patterns are the seeds of future products“ | Die Signal-Bausteine (Funding, Hiring, Führungswechsel, Themen, Rollen-Check) sind nicht kundenspezifisch. Wir bauen sie modular und übergeben das Muster an die zwei Pattern-Leute. Wir bauen aber **kein** Produkt, denn: „We are not currently building AI agents as products, only as custom software solutions.“ |

**Einschränkung:** Alle zehn Interviews stammen aus einer Organisation. Ob das Muster bei anderen Kunden in anderen Branchen genauso auftritt, ist nicht belegt. Das prüft das Pattern-Team, nicht dieses Projekt.

---

## Lösung

**Ein Agent, der pro Prospect ein kurzes Dossier liefert: zwei bis drei relevante Signale, ein Rollen-Check, ein Vorschlag für den Gesprächsaufhänger, und zu jedem Signal die Quelle.** Für Enterprise-Accounts folgt in Stufe 2 eine Account-Karte.

### Beispiel-Dossier (*illustrativ, erfundene Person und Firma*)

> **Anna Beispiel, VP Operations, Beispiel AG** · erstellt `[Datum]` · gültig bis `[Datum]`
> **Rolle:** aktiv, VP Operations seit `[Monat/Jahr]` (Quelle: Link)
> **Signale:**
> 1. Finanzierungsrunde Series B, gemeldet am `[Datum]` (Quelle: Pressemitteilung, Link)
> 2. Mehrere neue Stellen im Bereich Operations ausgeschrieben (Quelle: Karriereseite, Link)
> **Warum jetzt:** *Nach einer Finanzierungsrunde baut das Operations-Team aus; das passt zu unserem Angebot `[Angebot des Kunden]`.*
> **Aufhänger:** *Glückwunsch zur Series B, beim Aufbau des Ops-Teams …*

Lesedauer: unter 2 Minuten. Der Mensch klickt die Quellen an, wenn er sich darauf berufen will, und schreibt die Nachricht selbst.

### Was das Dossier enthält

1. **Rollen-Check:** Ist die Person noch im Unternehmen, in welcher Rolle, seit wann? Wenn nicht: Hinweis darauf und, falls mit Quelle belegbar, wer nachgefolgt ist. Jenkins sucht das heute von Hand: "I have to go hunt for who the new person is."
2. **Zwei bis drei Signale** aus festen Kategorien. Wir starten mit O'Neils Checkliste (Funding, Hiring, Führungswechsel) und ergänzen Themen-Signale, wie Green sie beschreibt: "Show me everyone who posted about Cloud Migration in the last week."
3. **Warum jetzt:** ein Satz, warum das Signal für das Angebot des Kunden relevant ist.
4. **Gesprächsaufhänger:** ein Vorschlag für den ersten Satz von E-Mail oder Call. Ein Vorschlag, keine fertige Nachricht.
5. **Quellen:** ein Link pro Signal, damit der Mensch nachprüfen und deuten kann.
6. **Zeitstempel:** Erstellzeitpunkt des Dossiers und Datum jeder Quelle.

### Regeln für den Bau

Diese Regeln sind die Grundlage für Testfälle. Werte, die als *Annahme* markiert sind, sind Startwerte, die in Phase 0 mit dem Kunden bestätigt oder geändert werden; sie stehen als Konfiguration im System, nicht im Code.

| # | Regel | Festlegung |
|---|---|---|
| B1 | **Auslöser** | Ein Dossier entsteht, (a) wenn ein Lead im CRM einem Vertriebler zugewiesen wird oder (b) wenn ein Vertriebler es für einen Kontakt anfordert (Knopf am CRM-Datensatz). *Bearbeiteter Lead* heißt: einem Vertriebler zugewiesen. |
| B2 | **Eingabe** | Mindestens Name und Firma; zusätzlich CRM-ID, wenn vorhanden. Mit CRM-ID wird das Dossier dem Datensatz zugeordnet. |
| B3 | **Eindeutigkeit** | Gibt es bei derselben Firma mehrere Personen gleichen Namens und lässt sich über Titel oder Profil nicht eindeutig zuordnen, entsteht kein Dossier, sondern der Hinweis *Person nicht eindeutig*. |
| B4 | **Rollen-Check** | Ergebnis ist einer von drei Zuständen: *aktiv* (mit Rolle und Beginn, falls belegt), *nicht mehr im Unternehmen* (mit Nachfolger nur, wenn mit Quelle belegt, sonst ohne Namen), *unsicher* (widersprüchliche Quellen: beide Angaben mit Quelle anzeigen, nichts entscheiden). Bei *nicht mehr im Unternehmen* werden keine Signale zur Person gesucht. |
| B5 | **Signalauswahl** | Höchstens drei Signale. Bei mehr Treffern: Reihenfolge der Kategorien nach O'Neils Checkliste (Funding, Hiring, Führungswechsel), dann Themen; innerhalb einer Kategorie das neueste zuerst. |
| B6 | **Zu wenige Signale** | Ein Signal: Dossier mit einem Signal. Kein Signal: Dossier mit Rollen-Check und dem Hinweis *Keine aktuellen Signale gefunden*; dann kein *Warum jetzt* und kein Aufhänger. Der Agent erfindet keinen Anlass. |
| B7 | **Zeitfenster** | Ein Signal ist nur gültig, wenn die Quelle jünger als das Zeitfenster der Kategorie ist. Startwerte (*Annahme*): Themen 7 Tage (angelehnt an Green: "in the last week"), Führungswechsel 6 Monate (angelehnt an Chen: "less than 6 months"), Funding und Hiring `[Platzhalter]`. |
| B8 | **Themenliste** | Die Themen für Themen-Signale legt der Kunde fest, verantwortlich Sales Enablement, als eine Liste pro Kunde in der Konfiguration. |
| B9 | **Quellenpflicht** | Kein Signal ohne erreichbaren Link, der das Signal belegt. Lässt sich kein Link setzen, entfällt das Signal. |
| B10 | **Zulässige Quellen** | (1) Frei zugängliche Quellen ohne Login: Firmenwebseiten, Karriereseiten, Pressemitteilungen, Nachrichten. (2) Vorhandene Lizenzen des Kunden (z. B. ZoomInfo, Sales Navigator) nur über offizielle Schnittstellen und nur, wenn die Lizenzbedingungen das erlauben. (3) Kein automatisiertes Auslesen hinter Logins ohne ausdrückliche Erlaubnis. Welche Wege für LinkedIn zulässig sind, entscheidet die rechtliche Prüfung in Phase 1 (Go/No-Go, siehe Plan). |
| B11 | **Ablage** | Das Dossier wird am Lead- bzw. Kontakt-Datensatz im CRM (Salesforce) gespeichert und dort angezeigt. Ob es zusätzlich in einem zweiten Kanal (z. B. Chat oder E-Mail) erscheint, ist eine Option, die in Phase 0 mit Kim und den Nutzern entschieden wird; der Standard ist das CRM. |
| B12 | **Aktualität** | Ein Dossier ist bis zu seinem Ablaufdatum gültig (Startwert *Annahme*: so lange wie das kürzeste Zeitfenster seiner Signale, höchstens `[Platzhalter]`). Wird ein abgelaufenes Dossier geöffnet, erstellt der Agent es neu. |
| B13 | **Kein Versand** | Der Agent hat keine Schnittstelle und keine Berechtigung, E-Mails oder Nachrichten zu senden. |
| B14 | **Sprache** | Das Dossier erscheint in der Arbeitssprache des Vertriebsteams; Zitate aus Quellen bleiben im Original. |
| B15 | **Nutzungsprotokoll** | Der Agent protokolliert, ob ein Dossier vor dem ersten Kontaktversuch geöffnet wurde. Das ist die Grundlage für die Nutzungsquote (L2). |

### Zwei Ausbaustufen innerhalb des Projekts

- **Stufe 1, Prospect-Dossier:** für SDRs und AEs, eine Person, ein Dossier. Hier liegt die meiste Zeit (15 bis 40 Min. pro Prospect).
- **Stufe 2, Account-Karte:** für Enterprise-AEs wie Petit. Inhalt: die Personen einer Zielfirma mit Rolle (je mit Rollen-Check), öffentlich erkennbare Berichtslinien, öffentlich erkennbare gemeinsame frühere Arbeitgeber, je mit Quelle. Petit beschreibt genau das: "Who reports to who?" Stufe 2 wird nur beauftragt, wenn Stufe 1 *trägt*, das heißt: Die Go-Kriterien des Pilots (siehe Plan, Phase 2) sind erfüllt.

### Wo das Dossier landet

Am CRM-Datensatz (Regel B11), damit es nicht wieder in Tabs verschwindet. Kim weiß, wo die Leute wirklich arbeiten: "It’s 90% LinkedIn." Deshalb klären wir in Phase 0, ob ein zweiter Kanal nötig ist, damit das Dossier dort ankommt, wo die Vertriebler tatsächlich sitzen.

### Alternativen

| Alternative | Warum nicht (oder nicht zuerst) |
|---|---|
| **A: Erst Bedürfnis 2 bauen, den CRM-Abgleich** | Kleinere Zielgruppe (5 von 10), ein Käufer, der in Kosten denkt, und Konkurrenz durch vorhandene Standardwerkzeuge. Siehe Abwägung oben und Anhang A. Bleibt die naheliegende Folgeoption. |
| **B: Beides zugleich bauen** | Doppelter Umfang, zwei Käufer, zwei Budgets, zwei Abnahmen. Für ein Bootstrap-Unternehmen steigt das Risiko, dass das Projekt zu groß wird, bevor der erste Nutzen sichtbar ist. Der Rollen-Check deckt den Teil von Bedürfnis 2 ab, den Bedürfnis 1 braucht. |
| **C: Mehr Lizenzen für vorhandene Tools** | Jenkins und Chen wünschen sich das. Es liefert aber Rohdaten, nicht die Synthese: Chen hat Sales Navigator und braucht trotzdem 4 Stunden für 10 Kontakte. Für uns ist es kein Projekt, denn es ist Einkauf und keine Agent-Arbeit. |
| **D: Schulung, bessere Checklisten** | Das macht O'Neil heute schon. Es verkürzt die Recherche, ersetzt sie aber nicht. Sie will Research aus der Einarbeitung herausnehmen und nicht besser lehren. |
| **E: Mehr Druck auf Call-Volumen** | Das ist der Weg der Führung heute ("keep yelling at them to make more calls"). Er senkt die Personalisierung und damit die Conversion. |
| **F: Fertige Nachrichten automatisch versenden** | Nimmt den Menschen aus dem Urteil heraus, das die Erfahrenen behalten wollen. Risiko für Ruf und Antwortquote. Bewusst ausgeschlossen (siehe Nicht-Ziele). |

### Vorher und nachher

Die Vorher-Spalte stammt aus den Interviews. Die Nachher-Spalte ist **Zielbild (*illustrativ*)**, keine Aussage aus den Interviews und kein gemessener Wert; ob es eintritt, zeigt der Pilot.

| | Vorher (Interviews) | Nachher (*Zielbild, illustrativ*) |
|---|---|---|
| **Recherche pro Prospect** | 15 bis 40 Minuten, verteilt auf viele Tabs | *Unter 2 Minuten zum Lesen eines fertigen Dossiers* |
| **Wer recherchiert** | SDRs, AEs, Top-Performer abends in der "second shift" | *Der Agent. Der Mensch liest, prüft und deutet.* |
| **Calls pro SDR und Tag** | Etwa 20 bei einem KPI von 50; Jenkins nennt als Grund das Prüfen und Übertragen von Daten ins CRM | *Näher am KPI, weil der Rollen-Check und die Recherche entfallen. Zielwert: `[Platzhalter]`* |
| **Leads mit Kontext** | 5 von 100 laut Marketing | *Jeder zugewiesene Lead bekommt ein Dossier (Regel B1)* |
| **Rollen-Prüfung vor dem Kontakt** | Jenkins prüft jeden Kontakt von Hand auf LinkedIn; bei etwa 40 % ist die Person nicht mehr im Unternehmen | *Der Agent prüft automatisch und markiert den Kontakt vor dem Anruf, mit Nachfolger, wenn belegt* |
| **Einarbeitung** | Research ist der größte Lehrinhalt | *Einarbeitung kann sich auf Gesprächsführung konzentrieren, wie O'Neil es will* |
| **Transparenz** | Thorne: "It’s a black box." | *Jedes Dossier mit Quellen und Zeitstempel, also nachvollziehbar* |

---

## Ziele

Messzeitpunkte beziehen sich auf den Pilot (Phase 2): **Woche 1** = Ausgangsmessung bei Pilot- und Vergleichsgruppe, **Ende Pilot** = Abschlussmessung. Pilotdauer `[Platzhalter]`.

**Ziele für den Kunden:**

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| Z1 | Recherchezeit pro Prospect senken | Minuten pro Prospect bis zum ersten Kontaktversuch | 15 bis 40 Min. (Interviews); `[Platzhalter: messen in Woche 1]` | unter 2 Min., gesetzt von O'Neil | Woche 1, Ende Pilot |
| Z2 | Calls pro SDR und Tag steigern | Calls pro SDR und Tag | etwa 20 bei KPI 50 (Jenkins); `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Woche 1, Ende Pilot |
| Z3 | Anteil bearbeiteter Leads mit Kontext erhöhen | Anteil zugewiesener Leads mit Dossier bzw. recherchiertem Kontext | 5 von 100 (Blunt); `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Woche 1, Ende Pilot |
| Z4 | Kontaktversuche bei Personen, die nicht mehr im Unternehmen sind, senken | Anteil Kontaktversuche (Anruf, E-Mail) an Personen, die nicht mehr in der Rolle sind | `[Platzhalter: messen in Woche 1]` (Kontext: Jenkins findet beim Vorab-Check bei etwa 40 % der Kontakte, dass sie nicht mehr im Unternehmen sind) | `[Platzhalter]` | Woche 1, Ende Pilot |
| Z5 | **Leitplanke:** Antwortquote mindestens halten | Antworten pro Kontaktversuch, Pilot- gegen Vergleichsgruppe | `[Platzhalter: messen in Woche 1]` | Pilotgruppe ≥ Vergleichsgruppe | Woche 1, Ende Pilot |
| Z6 | **Hauptziel:** Mehr gebuchte Meetings | Gebuchte Meetings pro SDR und Woche, Pilot- gegen Vergleichsgruppe | `[Platzhalter: messen in Woche 1]` | Pilotgruppe > Vergleichsgruppe, Abstand `[Platzhalter]` | Woche 1, Ende Pilot |
| Z7 | Qualität des Dossiers sichern | Anteil fehlerhafter Angaben (falsches Signal, falsche Rolle, toter Link) in einer Stichprobe von `[Platzhalter]` Dossiers | `[Platzhalter: erste Stichprobe in Phase 1]` | unter `[Platzhalter]` | Ende Phase 1, wöchentlich im Pilot |

Z5 ist die Leitplanke: Wenn das Volumen steigt und die Quote fällt, haben wir nur Druck automatisiert und keinen Kontext. Wird Z5 im Pilot verletzt, wird nicht ausgerollt (siehe Plan, Phase 2).

**Ziele für NeoEmployee:**

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| N1 | Einstiegsauftrag gewinnen | Unterschriebenes Angebot für Phase 0 und 1; abgerechnete Personentage | 0 (kein Auftrag) | Auftrag erteilt; `[Platzhalter: Personentage]` | Ende Phase 0 |
| N2 | Folgeauftrag eröffnen | Anzahl beauftragter Folgeangebote (Pilot und Ausrollen, Account-Karte, CRM-Abgleich für Sales Ops) | 0 | mindestens eines, `[Platzhalter: Umfang]` | Ende Phase 2 |
| N3 | Signal-Bausteine an das Pattern-Team übergeben | Anzahl dokumentiert übergebener Bausteine | 0 | 5 (Funding, Hiring, Führungswechsel, Themen, Rollen-Check) | Projektende |

---

## Nicht-Ziele

| Nicht-Ziel | Warum nicht | Wohin |
|---|---|---|
| **Kein vollständiger CRM-Abgleich für alle Kontakte.** Der Rollen-Check gilt nur für Prospects, die ein Dossier bekommen. | Das ist Bedürfnis 2 mit eigenem Käufer und eigenem Budget; im Einstieg würde es den Umfang verdoppeln. | Mögliches Folgeprojekt mit Sales Ops (Kim), eigenes Angebot (Plan, Option). |
| **Kein automatischer Versand.** Der Agent schlägt einen Aufhänger vor. Schreiben und Senden bleibt beim Menschen. | Erfahrene wollen das Urteil behalten ("You have to read between the lines"), und ein falscher automatischer Versand schadet dem Ruf des Kunden mehr als er an Zeit spart. | Nie in diesem Projekt. Eine spätere Prüfung wäre ein eigener Auftrag und setzt voraus, dass Z5 und Z7 über längere Zeit halten. |
| **Keine Lösung für den Konflikt Marketing ↔ Sales** über die Definition eines guten Leads. | Das ist eine Organisationsfrage, kein ersetzbarer Skill. | Bleibt beim Kunden (Vertriebs- und Marketingleitung). Wir liefern nur die Messwerte Z3 und Z6, die das Gespräch versachlichen können. |
| **Keine Lizenzbeschaffung** für ZoomInfo, Sales Navigator oder Ähnliches. | Einkauf ist keine Agent-Arbeit und kein T&M-Umsatz für uns; vorhandene Lizenzen nutzt der Agent als Quelle, wo erlaubt (Regel B10). | Entscheidung und Einkauf beim Kunden (Sales Ops). |
| **Kein Produkt.** | „We are not currently building AI agents as products, only as custom software solutions.“ | Die Muster gehen an das Pattern-Team; ein Produkt wäre eine eigene Entscheidung von NeoEmployee. |
| **Keine Beratung zur Vertriebsstrategie.** Welche Zielkunden die richtigen sind, entscheidet der Kunde. | Liegt außerhalb des Vision-Filters (kein ersetzbarer Mitarbeiter-Skill). | Bleibt beim Kunden. Seine Vorgaben fließen nur als Konfiguration ein (Themenliste, Regel B8). |

---

## Logik

Die Wirkungskette, von unserer Arbeit bis zum Geld, mit den Annahmen, an denen sie hängt:

```
Agent sammelt und filtert öffentliche Signale + prüft Rolle
        │  Annahme L1: Die Signale sind zulässig und zuverlässig abrufbar
        ▼
Fertiges Dossier pro Prospect in unter 2 Minuten lesbar
        │  Annahme L2: Die Vertriebler vertrauen dem Dossier und nutzen es
        ▼
Weniger Recherchezeit pro Prospect (Z1)
        │  Annahme L3: Gesparte Zeit fließt in Gespräche, nicht in neue Recherche
        ▼
Mehr Calls und mehr bearbeitete Leads mit Kontext (Z2, Z3)
        │  Annahme L4: Die Qualität des Kontexts hält die Antwortquote (Z5)
        ▼
Mehr Meetings für die Closer ("starving for good meetings") (Z6)
        │  Annahme L5: Mehr Meetings führen zu mehr Abschlüssen
        ▼
Mehr Pipeline und Umsatz beim Kunden → Budget für Folgeaufträge bei uns (N1, N2)
        │  Annahme L6: Die Bausteine sind über diesen Kunden hinaus wiederverwendbar
        ▼
Muster für das Pattern-Team (N3) → möglicher Produktkeim
```

| Annahme | Was dafür spricht | Was dagegen spricht | Wie wir sie prüfen, und was als bestanden gilt |
|---|---|---|---|
| **L1** Signale abrufbar | Thorne: "It’s all out there in plain sight." O'Neil: "9 times out of 10? LinkedIn." | Die meisten Signale liegen auf einer Plattform, deren Zugriffsregeln wir nicht kontrollieren. | Spike in Phase 1 mit `[Platzhalter: Anzahl]` echten Prospects des Kunden. **Go**, wenn (a) die rechtliche Prüfung mindestens einen zulässigen Zugriffsweg für Rollen-Check und Signale bestätigt und (b) bei mindestens `[Platzhalter]` % der Prospects zwei belegte Signale und ein korrekter Rollen-Check entstehen (Startwert *Annahme*: 70 %). **No-Go** bei (a) nicht erfüllt. Bei (b) nicht erfüllt: Quellen einschränken oder abbrechen. |
| **L2** Vertrauen und Nutzung | Käufer und Nutzer wünschen sich genau das (Thorne, O'Neil, Green, Chen) | Erfahrene wollen selbst deuten (Petit, Chen). Ein falsches Signal kann das Vertrauen zerstören. | Quellen pro Signal. **Genutzt** heißt: Dossier vor dem ersten Kontaktversuch geöffnet (Regel B15). Bestanden, wenn die Nutzungsquote in der Pilotgruppe mindestens `[Platzhalter]` % erreicht (Startwert *Annahme*: 70 %). |
| **L3** Zeit fließt in Gespräche | Jenkins nennt das Prüfen jedes Leads als Grund für 20 statt 50 Calls: "if I didn't have to verify every single lead, I could double my quota" | Die Leute könnten trotzdem weiter selbst recherchieren, aus Gewohnheit oder Misstrauen | Z1 und Z2 in Woche 1 und am Ende des Pilots messen. Bestanden, wenn Recherchezeit sinkt und Calls steigen. |
| **L4** Quote hält | Blunt: "conversion is higher if you know the context" | Unbelegt, ob ein Agent-Dossier so gut wirkt wie Handrecherche | Z5 gegen die Vergleichsgruppe. Bei Verletzung kein Ausrollen; Ursachen-Analyse und Nachbessern oder Abbruch. |
| **L5** Meetings → Abschlüsse | Ross: "My guys are great closers" | Andere Engpässe im Funnel sind möglich | Nicht Teil der Abnahme, weil Abschlüsse länger dauern als der Pilot. Der Kunde wertet nach `[Platzhalter: Monate]` im CRM aus, wie viele Meetings aus Pilot- und Vergleichsgruppe zu Abschlüssen wurden; wir bitten in Phase 0 um diese Zusage. |
| **L6** Wiederverwendbar | Generische Signal-Typen (O'Neils Checkliste) | Nur ein Kunde befragt | Übergabe von 5 dokumentierten Bausteinen (N3); Wiederverwendung prüft das Pattern-Team bei weiteren Kunden. |

Die kritischsten Annahmen sind **L1** (ohne Daten kein Dossier) und **L2** (ohne Vertrauen keine Nutzung). Beide prüfen wir zuerst.

---

## Plan

Dauer der Phasen, Teamgröße und Budget: `[Platzhalter]`. Der Plan legt Reihenfolge, Abnahme und Entscheidungspunkte fest. Beauftragt wird stufenweise: Phase 0 und 1 als gedeckelter Einstieg, jede weitere Phase erst nach Go.

| Phase | Was | Ergebnis | Entscheidung am Ende | Aufwand |
|---|---|---|---|---|
| **0: Klärung beim Kunden** | Budget-Owner bestätigen (VP Sales, Enablement oder Sales Ops). Zweiten Ausgabekanal klären. Zugriff auf CRM. Startwerte (Zeitfenster, Themenliste, Schwellen) bestätigen. Zusage zur Auswertung von L5. | Unterschriebenes Angebot, Messplan, Konfiguration | Go für Bedürfnis 1 oder Umkehr auf Bedürfnis 2 (Offene Punkte, Nr. 1) | `[Platzhalter: PT]`, gedeckelt |
| **1: Technischer Spike** | Quellen und Zugriffswege prüfen, rechtliche Prüfung des Datenzugriffs. Rollen-Check und drei Signal-Kategorien prototypisch umsetzen. Erste Qualitätsstichprobe (Z7). | Machbarkeitsnachweis mit echten Prospects des Kunden | Go/No-Go nach den Kriterien von L1 | `[Platzhalter: PT]`, gedeckelt |
| **2: Pilot Stufe 1** | Prospect-Dossier für eine kleine Gruppe von SDRs, z. B. aus dem Lead-Gen-Team ("A dozen bright kids"). Vergleichsgruppe ohne Dossier. | Messwerte Z1 bis Z7, Feedback der Nutzer | **Ausrollen**, wenn Z5 gehalten, Z6 verbessert, Z7 unter Schwelle und L2 bestanden. Sonst nachbessern oder abbrechen. | `[Platzhalter: PT]` |
| **3: Ausrollen Stufe 1** | Alle SDRs und AEs. Einarbeitung neuer Reps mit Dossier (mit O'Neil). Monitoring und Wartung einrichten. | Laufender Betrieb, Messung gegen Ausgangswerte | Stufe 2 beauftragen? | `[Platzhalter: PT]` |
| **4: Stufe 2, Account-Karte** | Für Enterprise-AEs. Nur wenn Stufe 1 trägt (Go-Kriterien Phase 2 erfüllt). Eigene Beauftragung. | Account-Karte für einen Pilot-Account | Folgeauftrag | `[Platzhalter: PT]` |
| **Parallel: Muster-Übergabe** | Signal-Bausteine dokumentieren, an das Pattern-Team übergeben | 5 dokumentierte Bausteine (N3) | — | intern |
| **Option: CRM-Abgleich** | Mit Sales Ops (Kim) als eigenes Projekt, auf Basis der Rollen-Checks aus Stufe 1 | Eigenes Angebot | Entscheidung beim Kunden | eigenes Angebot |

---

## Risiken und Einwände

| # | Risiko / Einwand | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|---|
| R1 | **Datenzugriff:** Die wichtigste Quelle ist eine Plattform, deren Nutzungsbedingungen automatisierten Zugriff einschränken können. Dazu kommt Datenschutz bei personenbezogenen Daten. | hoch | hoch | Rechtliche Prüfung in Phase 1, vor dem Pilot, als No-Go-Kriterium. Nur zulässige Zugriffswege (Regel B10). Quellen breit streuen (Pressemitteilungen, Funding-Datenbanken, Firmenseiten). |
| R2 | **Falsche oder erfundene Signale** im Dossier, die einen Account verbrennen | mittel | hoch | Kein Signal ohne Quelle (B9), Zeitfenster (B7), *unsicher* statt raten (B4), kein erfundener Anlass (B6). Fehlerquote Z7 als Abnahmekriterium. |
| R3 | **Erfahrene nutzen es nicht**, weil sie selbst deuten wollen | mittel | mittel | Dossier als Vorarbeit, nicht als Ersatz für das Urteil. Quellen zum Nachlesen. Petit und Chen früh als Testnutzer einbinden. |
| R4 | **Kein Budget beim VP of Sales**, dafür bei Sales Ops | unbekannt | hoch | Phase 0 klärt das. Dann Reihenfolge umkehren (Bedürfnis 2 zuerst), der Rollen-Check ist die gemeinsame Basis. |
| R5 | **Volumen steigt, Qualität fällt:** Das Dossier wird zur Ausrede für Massenansprache | mittel | mittel | Z5 als Leitplanke mit Konsequenz (kein Ausrollen). Kein automatischer Versand. |
| R6 | **Nur ein Kunde:** Das Muster ist vielleicht nicht übertragbar | mittel | niedrig für dieses Projekt, hoch für die Produktidee | Kein Produktversprechen. Übergabe an das Pattern-Team. |
| R7 | **Einwand Sales Ops:** *Das löst mein CRM-Problem nicht.* | hoch | mittel | Ehrlich so benennen. Der Rollen-Check liefert Belege und ist der Einstieg in ein Folgeprojekt. |
| R8 | **Einwand Führung:** *Recherchezeit ist nicht mein Problem, Pipeline ist es.* | mittel | hoch | Hauptziel ist Z6 (gebuchte Meetings) gegen eine Vergleichsgruppe, nicht die gesparte Zeit. |
| R9 | **Einwand Führung:** *Das haben wir schon (Sales Navigator, ZoomInfo).* | hoch | mittel | Belegen, dass die Lizenzen Rohdaten liefern und trotzdem von Hand recherchiert wird (Jenkins, Chen). Vorhandene Lizenzen als Quelle nutzen statt ersetzen. |
| R10 | **Wartungsaufwand:** Quellen ändern sich, der Agent bricht. Kim kennt das von seinen Tools ("they break"). | mittel | mittel | Monitoring und Wartung im Angebot vorsehen, Umfang `[Platzhalter]`. Zuständigkeit nach Projektende vertraglich festlegen. |
| R11 | **Scope Creep** Richtung Account-Karte, CRM-Abgleich oder zusätzliche Kanäle | mittel | mittel | Einstiegsumfang ist Stufe 1; alles andere nur als eigene Beauftragung (Plan). |
| R12 | **Abnahme und Zahlung:** Streit über die Abnahme oder verspätete Zahlung | niedrig bis mittel | hoch für einen Bootstrap-Betrieb | Abnahmekriterien (L1, Z5 bis Z7) vorab im Angebot; Abrechnung in kurzen Intervallen `[Platzhalter]`; gedeckelter Einstieg begrenzt das offene Volumen. |

---

## Offene Punkte

1. **Wer hat das Budget?** Die Wahl von Bedürfnis 1 stützt sich darauf, dass VP of Sales oder Enablement Budget freigeben können. Die Interviews belegen Druck, nicht Budget. Entscheidung in Phase 0. Wenn das Budget nur bei Sales Ops liegt, gilt die Abwägung in Anhang A neu.
2. **Rechtliche Zulässigkeit des Datenzugriffs** auf die wichtigste Quelle, Nutzung vorhandener Lizenzen als Quelle, Datenschutz bei Personendaten. Klärung in Phase 1, mit fachkundiger Beratung; No-Go-Kriterium.
3. **Zweiter Ausgabekanal** neben dem CRM: nötig oder nicht? Mit Kim und den Nutzern in Phase 0 klären.
4. **Ausgangswerte und Zielwerte** für Z2 bis Z7 und die Schwellen für L1 und L2 fehlen bzw. sind Startwerte. Ausgangswerte in Woche 1 des Pilots, Zielwerte und Schwellen in Phase 0 mit dem Kunden.
5. **Kaufmännisches:** Personentage pro Phase, Tagessätze, Obergrenze des Einstiegs, Abrechnungsrhythmus, Wartungsanteil `[Platzhalter]`. Entscheidung beim Management von NeoEmployee (E3).
6. **Welche Signale zählen für dieses Angebot?** O'Neils Checkliste ist der Start. Die Themenliste legt Sales Enablement fest (B8). Zeitfenster für Funding und Hiring offen (B7).
7. **Muster bei anderen Kunden:** Gibt es das Bedürfnis auch in anderen Branchen? Frage an das Pattern-Team.

---

## Anhang A: Bewertung der Bedürfnisse

### A.1 Die beiden Kandidaten

| | Bedürfnis 1: Grund zum Anrufen fertig aufbereitet | Bedürfnis 2: Kontaktdaten aktuell im CRM |
|---|---|---|
| **Kern** | Zwei bis drei relevante Signale pro Prospect, als Aufhänger | Arbeitgeber, Titel, E-Mail automatisch abgeglichen und im CRM |
| **Ersetzter Skill** | Prospect-Researcher | Data Clerk |
| **Betroffene** | 9 von 10 | 5 von 10 |
| **Käufer** | VP of Sales, Sales Director, Dir. Sales Enablement | Sales Ops Manager |

### A.2 Bewertung nach Wahrscheinlichkeit wirtschaftlichen Erfolgs

Skala: ● stark (2 Punkte), ◐ mittel (1 Punkt), ○ schwach (0 Punkte). Die Bewertung ist ein begründetes Urteil auf Basis der Interviews, keine Messung.

| Faktor | Bedürfnis 1 | Begründung | Bedürfnis 2 | Begründung |
|---|---|---|---|---|
| **F1 Verbreitung** | ● | 9 von 10, alle Ebenen | ◐ | 5 von 10, davon einer nur teilweise |
| **F2 Dringlichkeit beim Käufer** | ● | Board-Druck beim VP ("the job you're trying to save"), Ramp-KPI bei Enablement | ◐ | Großer Schmerz ("Our CRM is a graveyard."), aber kein Umsatzdruck beim Käufer belegt |
| **F3 Art des Nutzens** | ● | Umsatz: "I'd double my numbers." (Chen) | ◐ | Kosten: 80k-$-Leute als "copy-paste machine", "2 hours a day" laut Reps. Jenkins sieht auch Umsatz: "I could double my quota." |
| **F4 Wettbewerb beim Kunden** | ● | Kein Werkzeug macht die Synthese, vorhandene Lizenzen liefern nur Rohdaten | ○ | ZoomInfo und Clearbit vorhanden, laut Käufer zu teuer und unzuverlässig. Wir konkurrieren über den Preis. |
| **F5 Messbarkeit** | ● | Zielmarke vom Kunden selbst (unter 2 Min.), bestehender KPI (50 Calls) | ● | Bounce-Quote und Anteil veralteter Datensätze (Jenkins: etwa 40 % beim Vorab-Check nicht mehr im Unternehmen) |
| **F6 Musterpotenzial (Brücke)** | ● | Generische Signal-Typen, keine Standardsoftware für die Synthese beim Kunden | ◐ | Generisch, aber Markt durch Standardwerkzeuge besetzt |
| **F7 Technisches Risiko** | ◐ | Quellenzugriff (R1), Fehlerrisiko bei Signalen (R2) | ◐ | Gleiches Quellenrisiko, zusätzlich Schreibzugriff ins CRM |
| **F8 Abhängigkeit** | ◐ | Braucht aktuelle Kontaktdaten, gelöst durch Rollen-Check | ● | Steht für sich, ist Basis für Bedürfnis 1 |

**Zusammenfassung:** Bedürfnis 1 liegt bei F1, F2, F3, F4 und F6 vorn. Bei F5 und F7 sind beide gleich. Bei F8 liegt Bedürfnis 2 vorn. Diesen Nachteil gleichen wir aus, indem der Rollen-Check aus Bedürfnis 2 Teil des Dossier-Agenten wird.

### A.3 Gewichtungen (Sensitivität)

Punkte je Faktor aus A.2 (B1 = Bedürfnis 1, B2 = Bedürfnis 2):

| | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 |
|---|---|---|---|---|---|---|---|---|
| B1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 |
| B2 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 2 |

Die Gewichte sind gesetzte Perspektiven (*Annahme*), keine Messwerte. Summe = Σ (Punkte × Gewicht).

| Gewichtung | Gewichte | B1 | B2 | Ergebnis |
|---|---|---|---|---|
| **G1 Gleichgewichtet** | alle × 1 | 14 | 9 | B1 vorn |
| **G2 Runway** (Umsatz schnell sichern) | F2, F3, F4 × 3; übrige × 1 | 26 | 13 | B1 deutlich vorn |
| **G3 Lieferrisiko** (Machbarkeit zuerst) | F5, F7, F8 × 3; übrige × 1 | 22 | 19 | B1 knapp vorn |
| **G4 Skeptiker** (der Kunde hat recht, dass vorhandene Werkzeuge reichen; Nutzen und Wettbewerb zählen nicht, Abhängigkeit dreifach) | F3, F4 × 0; F8 × 3; übrige × 1 | 12 | 12 | Gleichstand |

Rechenweg G2, B1: 3 × (2 + 2 + 2) + (2 + 2 + 2 + 1 + 1) = 18 + 8 = 26; B2: 3 × (1 + 1 + 0) + (1 + 2 + 1 + 1 + 2) = 6 + 7 = 13.
Rechenweg G3, B1: 3 × (2 + 1 + 1) + (2 + 2 + 2 + 2 + 2) = 12 + 10 = 22; B2: 3 × (2 + 1 + 2) + (1 + 1 + 1 + 0 + 1) = 15 + 4 = 19.
Rechenweg G4, B1: (2 + 2 + 2 + 2 + 1) + 3 × 1 = 9 + 3 = 12; B2: (1 + 1 + 2 + 1 + 1) + 3 × 2 = 6 + 6 = 12.

**Ergebnis:** Bedürfnis 1 gewinnt in drei von vier Gewichtungen und verliert in keiner. Die Wahl kippt nur, wenn man den Umsatzhebel und den fehlenden Wettbewerb ganz ignoriert; genau diesen Einwand testet der Pilot über Z6 gegen die Vergleichsgruppe.

### A.4 Strategie-Prüfung (aus der Synthese übernommen und bestätigt)

| Kriterium | Bedürfnis 1 | Bedürfnis 2 |
|---|---|---|
| Vision-Filter: ersetzt einen Mitarbeiter-Skill | ✔ Prospect-Researcher | ✔ Data Clerk |
| Revenue is runway: Budget-Schmerz, als T&M verkaufbar | ✔ drei Käufer mit Druck | ✔ ein Käufer, Kosten schon im Budget |
| Brücke: wiederkehrendes Muster | ✔ mit Einschränkung (ein Kunde) | ✔ mit Einschränkung (ein Kunde) |

Beide bestehen. Die Strategie entscheidet also nicht zwischen den beiden. Den Unterschied machen die Faktoren in A.2, vor allem Dringlichkeit, Art des Nutzens und Wettbewerb. Alle drei hängen direkt an „Revenue is runway“: Wir wählen das Bedürfnis, bei dem der Abschluss wahrscheinlicher und der Folgeauftrag naheliegender ist.

### A.5 Wann die Wahl kippt

Wir würden auf Bedürfnis 2 umschwenken, wenn eine der folgenden Bedingungen eintritt:

- Beim VP of Sales und bei Enablement gibt es kein Budget, bei Sales Ops schon (Offene Punkte, Nr. 1).
- Der technische Spike zeigt, dass Signale nicht zuverlässig abrufbar sind, der Rollen-Abgleich aber schon.
- Der Kunde will zuerst seine Datenbasis bereinigen, bevor er etwas darauf aufbaut.
- Der Pilot zeigt keinen Vorsprung bei Z6, der Rollen-Check aber messbar weniger Fehlkontakte (Z4); dann trägt die Skeptiker-Gewichtung G4.

---

## Loop-Protokoll

wird vom Koordinator geführt
