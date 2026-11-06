# PRD: Dossier-Agent (Arbeitstitel), der fertige Grund zum Anrufen

**Stand:** 2026-11-05
**Autor:** Produktmanagement NeoEmployee
**Grundlage:** `output/interview-synthesis-2026-11-03.md` (zwei Bedürfnisse aus zehn Interviews), Originalinterviews in `input/`, `context/company.md`, `context/strategy.md`
**Zitat-Konvention:** Interview-Zitate in "…" (gerade Anführungszeichen), wörtlich aus `input/`. Strategie-Zitate in „…“, wörtlich aus `context/`. Eigene Umschreibungen *kursiv*. Fehlende Zahlen stehen als `[Platzhalter]`.

---

## Kurzfassung

Die Synthese hat zwei Kundenbedürfnisse herausgearbeitet: (1) Vertriebler brauchen den *Grund zum Anrufen* fertig aufbereitet, und (2) Kontaktdaten sollen aktuell und ohne Handarbeit im CRM stehen. Wir bauen zuerst **Bedürfnis 1** und nehmen von Bedürfnis 2 nur den kleinen Teil mit, ohne den Bedürfnis 1 nicht funktioniert: die Prüfung, ob die Person noch dort arbeitet.

**Warum 1 und nicht 2:** Bedürfnis 1 hat die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs. Es betrifft 9 von 10 Befragten statt 5. Der wichtigste Käufer, der VP of Sales, steht unter Druck vom Board und hat die Lösung selbst formuliert: "just hand them the dossier". Der Nutzen ist mehr Umsatz und nicht nur gesparte Kosten. Bedürfnis 2 hat zwar einen klaren Käufer (Sales Ops), der denkt aber in Kosten und vergleicht mit Werkzeugen, die er schon heute zu teuer findet: "they break, or they’re too expensive to run on every single contact record". Dort konkurrieren wir mit Standardsoftware über den Preis. Das passt schlecht zu einem T&M-Projekt. Die Abwägung steht im Abschnitt *Warum dieses Problem* und im Detail in Anhang A.

**Was der Agent tut:** Für jeden Prospect und jeden Account sammelt er die zwei bis drei relevanten Signale aus öffentlichen Quellen (Funding, Hiring, Führungswechsel, Themen). Er prüft, ob die Person noch in der Rolle ist, und liefert ein kurzes Dossier mit Gesprächsaufhänger und Quellenlink. Das Dossier landet dort, wo der Vertriebler arbeitet. Der Agent ersetzt den Skill *Prospect-Researcher*. Das Urteil im Gespräch bleibt beim Menschen.

**Erfolgsmaß:** Die Recherchezeit pro Prospect sinkt von heute 15 bis 40 Minuten auf unter 2 Minuten. Diesen Zielwert hat die Enablement-Direktorin selbst genannt: "can you find it in under two minutes?" Dadurch steigt die Zahl der Calls pro SDR in Richtung des KPI von 50 pro Tag.

**Geschäftsmodell:** Kundenprojekt auf Time-&-Material-Basis, passend zu „We bill on a time-and-material basis.“ Der Agent wird modular gebaut, damit die Signal-Bausteine als Muster für weitere Kunden taugen. Budget, Laufzeit und Tagessätze: `[Platzhalter]`, kaufmännische Entscheidung beim Management.

---

## Problem

**Kern:** Der Kontext für eine gute Ansprache ist öffentlich verfügbar, aber verstreut und verrauscht. Heute baut ein Mensch ihn von Hand zu einem Gesprächsaufhänger zusammen. Das kostet pro Prospect 15 Minuten bis mehrere Tage. Darum fehlt Volumen, oder die Personalisierung fällt weg und die Conversion sinkt.

Der VP of Sales beschreibt den Engpass so: "They’re turning unstructured noise into structured talk tracks manually. That’s the bottleneck." Es fehlen nicht die Daten. Es fehlt die fertige Synthese daraus. Die Enablement-Direktorin bestätigt das: "The problem isn't that the data is missing".

### Was es heute kostet (nur Zahlen aus den Interviews)

| Wer | Was | Zitat |
|---|---|---|
| Marcus Thorne, VP of Sales | 15 Min. pro Prospect, also 4 pro Stunde | "If you do the math, that's only 4 prospects an hour. That's a joke." |
| Linda O'Neil, Dir. Sales Enablement | 40 Min. ohne Ergebnis bei neuen Reps | "suddenly forty minutes have passed and they haven't actually found a reason to call" |
| Mike Ross, Sales Director | 20 Min. für eine E-Mail, kaum Output | "the output is a trickle. Droplets." |
| Rachel Green, Junior SDR | 30 Min. für eine E-Mail | "30 minutes for one email!" |
| Jessica Chen, AE (Top-Performerin) | 4 Std. abends für 10 Kontakte | "I spend maybe 4 hours a night just building a list of 10 people to email the next day." |
| Sam Petit, Enterprise AE | Tage pro Account | "I spend days—literal days—just mapping an account" |
| Sarah Jenkins, SDR | 20 statt 50 Calls pro Tag | "I’m supposed to be making 50 calls a day. That's the KPI. But I’m lucky if I get to 20" |
| Emily Blunt, Marketing Manager | Kontext für 5 von 100 Leads | "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." |

### Warum man nicht einfach auf Personalisierung verzichten kann

Die Führung sagt *schneller wählen*. Ross will die Leute "Dialing!" sehen, Thorne sagt "Go faster." Die Basis und das Marketing halten dagegen, dass Kontext die Antwortquote trägt. Blunt räumt ein: "conversion is higher if you know the context". Der erfahrenste Verkäufer, Tom Baker, hat es selbst erlebt, als er einen Artikel des Kunden nicht kannte: "I looked like a dinosaur." *Personalisierung muss also billig werden, nicht wegfallen.*

### Was bleibt beim Menschen

Erfahrene Verkäufer wollen die Deutung behalten. Petit: "You have to read between the lines". Chen: "Because I have to know *everything* about them." *Der Agent übernimmt das Sammeln, Filtern und Strukturieren, nicht das Urteil.* Das ist zugleich eine Anforderung an die Lösung: Jedes Signal braucht eine Quelle, damit der Mensch nachlesen kann.

### Das Datenproblem darunter

Ein Dossier über jemanden, der nicht mehr im Unternehmen ist, schadet. Laut Jenkins ist das "like 40% of the time" der Fall, und "Half the emails bounce immediately". Das ist Bedürfnis 2 aus der Synthese. Es betrifft dieses Produkt nur an einer Stelle: Vor jedem Dossier muss geprüft werden, ob die Person noch in der Rolle ist.

---

## Warum dieses Problem (Wahl und Strategie)

### Die Wahl

Die Synthese lässt zwei Bedürfnisse übrig. Beide bestehen die drei Strategie-Prüfungen. Die Frage ist also nicht *passt es?*, sondern *welches bringt mit höherer Wahrscheinlichkeit Geld?* Wir haben beide Bedürfnisse nach sechs Faktoren verglichen (Bewertung in Anhang A):

1. **Wie viele haben das Problem?** Bedürfnis 1: 9 von 10, über alle Ebenen von Junior SDR bis VP. Bedürfnis 2: 5 von 10.
2. **Wer kauft, und wie dringend?** Bedürfnis 1 hat drei Käufer mit Druck. Der VP of Sales kam gerade aus dem Board-Meeting: "dress for the job you want, or the job you're trying to save". Der Sales Director nennt den Engpass als Erstes: "They are starving for good meetings." Die Enablement-Direktorin hat einen eigenen KPI: "It's a massive drain on our ramp time." Bedürfnis 2 hat einen Käufer, David Kim (Sales Ops). Sein Schmerz ist echt ("Data integrity. 100%."), aber er ist für den Stack zuständig, nicht für den Umsatz.
3. **Umsatz oder Kostenersparnis?** Bei Bedürfnis 1 rechnen die Betroffenen selbst in Umsatz. Chen: "I'd double my numbers." Thorne: "we’d be unstoppable." Bei Bedürfnis 2 rechnet der Käufer in Kosten: "Why do I have a human being paid $80k a year acting as a copy-paste machine?" *Ein Umsatzhebel rechtfertigt ein T&M-Budget leichter als eine Kostensenkung, die man gegen bestehende Lizenzen aufrechnet.*
4. **Gegen wen treten wir an?** Bei Bedürfnis 2 hat der Kunde schon ZoomInfo und Clearbit. Kim sagt, sie seien zu teuer für jeden Datensatz. Ein maßgeschneiderter Agent auf T&M-Basis muss sich also an einem Preis messen lassen, den der Käufer schon heute zu hoch findet. Bei Bedürfnis 1 gibt es beim Kunden kein Werkzeug, das die Synthese macht. Die vorhandenen Lizenzen liefern Rohdaten, und die Leute recherchieren trotzdem von Hand.
5. **Wie gut lässt sich Erfolg zeigen?** Bei Bedürfnis 1 gibt es eine Zielmarke, die der Kunde selbst gesetzt hat (unter 2 Minuten), und einen bestehenden KPI (50 Calls pro Tag). Bei Bedürfnis 2 ist Erfolg ebenfalls messbar (Bounce-Quote, veraltete Datensätze). Hier liegen beide etwa gleich.
6. **Taugt es als Muster für spätere Produkte?** Die Signal-Typen sind generisch. O'Neils Checkliste ist kein Sonderfall dieses Kunden: "1. Recent funding news—Series B or C preferably. 2. New hiring in engineering or ops. 3. Recent leadership changes at the VP level." Bedürfnis 2 ist ebenfalls ein Muster, aber eines, für das es schon Standardsoftware gibt. *Ein Produktkeim in einem besetzten Markt ist weniger wert.*

**Ergebnis:** Bedürfnis 1 liegt bei fünf von sechs Faktoren vorn, beim fünften gleichauf. Wir wählen Bedürfnis 1.

**Was wir von Bedürfnis 2 trotzdem mitnehmen:** Den Abgleich *ist die Person noch in dieser Rolle?* für jeden Prospect, der ein Dossier bekommt. Mehr nicht. Ein vollständiger CRM-Abgleich für alle Kontakte ist ein eigenes Projekt (siehe Nicht-Ziele und Offene Punkte). Die Prüfung im Dossier-Agenten ist aber der natürliche Einstieg dafür: Sie liefert Kim schon im ersten Projekt Belege, und sie öffnet ein zweites Gespräch mit einem zweiten Budget.

**Was gegen die Wahl spricht:** Bedürfnis 2 hat den klarer abgrenzbaren Käufer, und Kim hat die Lösung ebenfalls fast selbst beschrieben. Wenn sich in der Klärung zeigt, dass beim VP of Sales kein Budget frei ist, beim Sales Ops aber schon, kehrt sich die Reihenfolge um. Das ist der wichtigste offene Punkt (siehe Offene Punkte, Nr. 1).

### Abgleich mit der Strategie

| Strategie (`context/`) | Wie der Dossier-Agent passt |
|---|---|
| **Vision-Filter:** „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ | Der Agent ersetzt einen abgrenzbaren Skill: den Prospect-Researcher. O'Neil beschreibt ihn so: "We’re essentially teaching them to be high-priced data miners." |
| **Bootstrap:** „anything that brings in money and aligns with our vision, we do.“ und „Revenue is runway“ | Drei Käufer mit Druck und eine Kennzahl, auf die das Board schaut. Das erhöht die Chance auf einen schnellen Abschluss. Ein schneller Abschluss verlängert die Runway. |
| **Geschäftsmodell:** „We bill on a time-and-material basis.“ und „Every agent is built custom for the client“ | Das Projekt wird für diesen Kunden gebaut und nach Aufwand abgerechnet. Quellen, Signal-Regeln und Ausgabekanal sind kundenspezifisch. |
| **Prozess:** „Identify bottlenecks“ → Skill-Gap → Agent bauen | Der Engpass wurde vom Kunden selbst benannt ("That’s the bottleneck."), der Skill-Gap ist klar. |
| **Die Brücke:** „These patterns are the seeds of future products“ | Die Signal-Bausteine (Funding, Hiring, Führungswechsel, Themen, Rollen-Check) sind nicht kundenspezifisch. Wir bauen sie modular und übergeben das Muster an die zwei Pattern-Leute. Wir bauen aber **kein** Produkt, denn: „We are not currently building AI agents as products, only as custom software solutions.“ |

**Einschränkung:** Alle zehn Interviews stammen aus einer Organisation. Ob das Muster bei anderen Kunden in anderen Branchen genauso auftritt, ist nicht belegt. Das prüft das Pattern-Team, nicht dieses Projekt.

---

## Lösung

**Ein Agent, der pro Prospect und pro Account ein kurzes Dossier liefert: zwei bis drei relevante Signale, ein Rollen-Check, ein Vorschlag für den Gesprächsaufhänger, und zu jedem Signal die Quelle.**

### Was das Dossier enthält

1. **Rollen-Check:** Ist die Person noch im Unternehmen, in welcher Rolle, seit wann? Wenn nicht: Hinweis darauf und, falls erkennbar, wer nachgefolgt ist. Jenkins sucht das heute von Hand: "I have to go hunt for who the new person is."
2. **Zwei bis drei Signale** aus festen Kategorien. Wir starten mit O'Neils Checkliste (Funding, Hiring, Führungswechsel) und ergänzen Themen-Signale, wie Green sie beschreibt: "Show me everyone who posted about Cloud Migration in the last week."
3. **Warum jetzt:** ein Satz, warum das Signal für unser Angebot relevant ist.
4. **Gesprächsaufhänger:** ein Vorschlag für den ersten Satz von E-Mail oder Call. Ein Vorschlag, keine fertige Nachricht.
5. **Quellen:** ein Link pro Signal, damit der Mensch nachprüfen und deuten kann.

### Zwei Ausbaustufen innerhalb des Projekts

- **Stufe 1, Prospect-Dossier:** für SDRs und AEs, eine Person, ein Dossier. Hier liegt die meiste Zeit (15 bis 40 Min. pro Prospect).
- **Stufe 2, Account-Karte:** für Enterprise-AEs wie Petit. Wer sitzt wo, wer berichtet an wen, welche Beziehungen sind öffentlich erkennbar. Das ist schwieriger und kommt erst, wenn Stufe 1 trägt.

### Wo das Dossier landet

Dort, wo der Vertriebler ohnehin arbeitet. Welcher Kanal das ist (CRM-Datensatz, Liste, E-Mail, Chat), klären wir in der ersten Projektphase. Kim weiß, wo die Leute wirklich arbeiten: "It’s 90% LinkedIn." Das CRM ist trotzdem der Ort, an dem das Ergebnis gespeichert werden sollte, damit es nicht wieder in Tabs verschwindet.

### Alternativen

| Alternative | Warum nicht (oder nicht zuerst) |
|---|---|
| **A: Erst Bedürfnis 2 bauen, den CRM-Abgleich** | Kleinere Zielgruppe (5 von 10), ein Käufer, der in Kosten denkt, und Konkurrenz durch vorhandene Standardwerkzeuge. Siehe Abwägung oben und Anhang A. Bleibt die naheliegende Folgeoption. |
| **B: Beides zugleich bauen** | Doppelter Umfang, zwei Käufer, zwei Budgets, zwei Abnahmen. Für ein Bootstrap-Unternehmen steigt das Risiko, dass das Projekt zu groß wird, bevor der erste Nutzen sichtbar ist. Der Rollen-Check deckt den Teil von Bedürfnis 2 ab, den Bedürfnis 1 braucht. |
| **C: Mehr Lizenzen für vorhandene Tools** | Jenkins und Chen wünschen sich das. Es liefert aber Rohdaten, nicht die Synthese. Für uns ist es kein Projekt, denn es ist Einkauf und keine Agent-Arbeit. |
| **D: Schulung, bessere Checklisten** | Das macht O'Neil heute schon. Es verkürzt die Recherche, ersetzt sie aber nicht. Sie will Research aus der Einarbeitung herausnehmen und nicht besser lehren. |
| **E: Mehr Druck auf Call-Volumen** | Das ist der Weg der Führung heute ("keep yelling at them to make more calls"). Er senkt die Personalisierung und damit die Conversion. |
| **F: Fertige Nachrichten automatisch versenden** | Nimmt den Menschen aus dem Urteil heraus, das die Erfahrenen behalten wollen. Risiko für Ruf und Antwortquote. Bewusst ausgeschlossen (siehe Nicht-Ziele). |

### Vorher und nachher

| | Vorher | Nachher |
|---|---|---|
| **Recherche pro Prospect** | 15 bis 40 Minuten, verteilt auf viele Tabs | Unter 2 Minuten zum Lesen eines fertigen Dossiers |
| **Wer recherchiert** | SDRs, AEs, Top-Performer abends in der "second shift" | Der Agent. Der Mensch liest, prüft und deutet. |
| **Calls pro SDR und Tag** | Etwa 20 bei einem KPI von 50 | Näher am KPI. Zielwert: `[Platzhalter]`, mit dem Kunden festzulegen |
| **Leads mit Kontext** | 5 von 100 laut Marketing | Jeder Lead, der bearbeitet wird, bekommt ein Dossier |
| **Veraltete Kontakte im Gespräch** | Etwa 40 % laut Jenkins, auffällig erst beim Anruf | Vor dem Anruf markiert, mit Nachfolger, wenn erkennbar |
| **Einarbeitung** | Research ist der größte Lehrinhalt | Einarbeitung kann sich auf Gesprächsführung konzentrieren, wie O'Neil es will |
| **Transparenz** | Thorne: "It’s a black box." | Jedes Dossier mit Quellen und Zeitstempel, also nachvollziehbar |

---

## Ziele

**Ziele für den Kunden** (Messung vor und nach dem Pilot, Ausgangswerte aus den Interviews, Zielwerte gemeinsam mit dem Kunden festzulegen):

| # | Ziel | Ausgangswert (Interview) | Zielwert |
|---|---|---|---|
| Z1 | Recherchezeit pro Prospect senken | 15 bis 40 Min. | unter 2 Min., gesetzt von O'Neil |
| Z2 | Calls pro SDR und Tag steigern | etwa 20, KPI 50 | `[Platzhalter]` |
| Z3 | Anteil bearbeiteter Leads mit Kontext erhöhen | 5 von 100 | `[Platzhalter]` |
| Z4 | Anteil veralteter Kontakte, die erst im Gespräch auffallen, senken | etwa 40 % | `[Platzhalter]` |
| Z5 | Antwort- bzw. Meeting-Quote mindestens halten | nicht erhoben | `[Platzhalter]`, Ausgangswert im Pilot messen |

Z5 ist die Leitplanke: Wenn das Volumen steigt und die Quote fällt, haben wir nur Druck automatisiert und keinen Kontext.

**Ziele für NeoEmployee:**

| # | Ziel | Wert |
|---|---|---|
| N1 | Projekt auf T&M-Basis abschließen | Umfang und Budget `[Platzhalter]` |
| N2 | Folgeauftrag eröffnen (Account-Karte oder CRM-Abgleich für Sales Ops) | Entscheidung beim Kunden nach dem Pilot |
| N3 | Signal-Bausteine modular dokumentiert an das Pattern-Team übergeben | bei Projektende |

---

## Nicht-Ziele

- **Kein vollständiger CRM-Abgleich für alle Kontakte.** Der Rollen-Check gilt nur für Prospects, die ein Dossier bekommen. Den Gesamtabgleich behandeln wir als mögliches Folgeprojekt mit Sales Ops.
- **Kein automatischer Versand.** Der Agent schlägt einen Aufhänger vor. Schreiben und Senden bleibt beim Menschen.
- **Keine Lösung für den Konflikt Marketing ↔ Sales** über die Definition eines guten Leads. Das ist eine Organisationsfrage, kein ersetzbarer Skill. Sie entschärft sich vielleicht, wenn mehr Leads Kontext bekommen.
- **Keine Lizenzbeschaffung** für ZoomInfo, Sales Navigator oder Ähnliches.
- **Kein Produkt.** Wir bauen für diesen Kunden. Die Muster gehen an das Pattern-Team, das Produkt ist nicht Teil dieses PRD.
- **Keine Beratung zur Vertriebsstrategie.** Welche Zielkunden die richtigen sind, entscheidet der Kunde.

---

## Logik

Die Wirkungskette, von unserer Arbeit bis zum Geld, mit den Annahmen, an denen sie hängt:

```
Agent sammelt und filtert öffentliche Signale + prüft Rolle
        │  Annahme L1: Die Signale sind öffentlich und zuverlässig abrufbar
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
Mehr Meetings für die Closer ("starving for good meetings")
        │  Annahme L5: Mehr Meetings führen zu mehr Abschlüssen
        ▼
Mehr Pipeline und Umsatz beim Kunden → Budget für Folgeaufträge bei uns (N1, N2)
        │  Annahme L6: Die Bausteine sind über diesen Kunden hinaus wiederverwendbar
        ▼
Muster für das Pattern-Team (N3) → möglicher Produktkeim
```

| Annahme | Was dafür spricht | Was dagegen spricht | Wie wir sie prüfen |
|---|---|---|---|
| **L1** Signale abrufbar | Thorne: "It’s all out there in plain sight." O'Neil: "9 times out of 10? LinkedIn." | Die meisten Signale liegen auf einer Plattform, deren Zugriffsregeln wir nicht kontrollieren. | Technischer Spike in Phase 1: Quellen, Zugriffswege, Rechtslage |
| **L2** Vertrauen und Nutzung | Käufer und Nutzer wünschen sich genau das (Thorne, O'Neil, Green, Chen) | Erfahrene wollen selbst deuten (Petit, Chen). Ein falsches Signal kann das Vertrauen zerstören. | Quellen pro Signal. Nutzungsquote im Pilot messen. |
| **L3** Zeit fließt in Gespräche | Jenkins nennt Verifikation als Grund für 20 statt 50 Calls | Die Leute könnten trotzdem weiter selbst recherchieren, aus Gewohnheit oder Misstrauen | Zeitmessung vorher/nachher, Calls pro Tag |
| **L4** Quote hält | Blunt: "conversion is higher if you know the context" | Unbelegt, ob ein Agent-Dossier so gut wirkt wie Handrecherche | Z5 im Pilot gegen eine Vergleichsgruppe messen |
| **L5** Meetings → Abschlüsse | Ross: "My guys are great closers" | Andere Engpässe im Funnel sind möglich | Nicht in unserem Projekt messbar, beim Kunden nachfragen |
| **L6** Wiederverwendbar | Generische Signal-Typen (O'Neils Checkliste) | Nur ein Kunde befragt | Übergabe an das Pattern-Team |

Die kritischsten Annahmen sind **L1** (ohne Daten kein Produkt) und **L2** (ohne Vertrauen keine Nutzung). Beide prüfen wir zuerst.

---

## Plan

Dauer der Phasen, Teamgröße und Budget: `[Platzhalter]`. Der Plan legt die Reihenfolge und die Entscheidungspunkte fest, nicht den Kalender.

| Phase | Was | Ergebnis | Entscheidung am Ende |
|---|---|---|---|
| **0: Klärung beim Kunden** | Budget-Owner bestätigen (VP Sales, Enablement oder Sales Ops). Ausgabekanal und Zugriff auf CRM klären. Ausgangswerte für Z1 bis Z5 festlegen. | Unterschriebenes Angebot, Messplan | Go für Bedürfnis 1 oder Umkehr auf Bedürfnis 2 (siehe Offene Punkte, Nr. 1) |
| **1: Technischer Spike** | Quellen und Zugriffswege prüfen (L1). Rechtliche Prüfung des Datenzugriffs. Drei Signal-Kategorien prototypisch umsetzen. | Machbarkeitsnachweis mit echten Prospects des Kunden | Weiter, umbauen oder Quellen einschränken |
| **2: Pilot Stufe 1** | Prospect-Dossier für eine kleine Gruppe von SDRs, z. B. aus dem Lead-Gen-Team ("A dozen bright kids"). Vergleichsgruppe ohne Dossier. | Messwerte Z1 bis Z5, Feedback der Nutzer | Ausrollen, nachbessern oder abbrechen |
| **3: Ausrollen Stufe 1** | Alle SDRs und AEs. Einarbeitung neuer Reps mit Dossier (mit O'Neil). | Laufender Betrieb, Messung gegen Ausgangswerte | Stufe 2 beauftragen? |
| **4: Stufe 2, Account-Karte** | Für Enterprise-AEs. Nur wenn Stufe 1 trägt. | Account-Karte für einen Pilot-Account | Folgeauftrag |
| **Parallel: Muster-Übergabe** | Signal-Bausteine dokumentieren, an das Pattern-Team übergeben | Dokumentation | — |
| **Option: CRM-Abgleich** | Mit Sales Ops (Kim) als eigenes Projekt, auf Basis der Rollen-Checks aus Stufe 1 | Eigenes Angebot | Entscheidung beim Kunden |

---

## Risiken und Einwände

| # | Risiko / Einwand | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|---|
| R1 | **Datenzugriff:** Die wichtigste Quelle ist eine Plattform, deren Nutzungsbedingungen automatisierten Zugriff einschränken können. Dazu kommt Datenschutz bei personenbezogenen Daten. | hoch | hoch | Rechtliche Prüfung in Phase 1, vor dem Pilot. Nur zulässige Zugriffswege. Quellen breit streuen (Pressemitteilungen, Funding-Datenbanken, Firmenseiten). |
| R2 | **Falsche oder erfundene Signale** im Dossier | mittel | hoch | Jedes Signal mit Quellenlink. Kein Signal ohne Quelle. Stichproben im Pilot. |
| R3 | **Erfahrene nutzen es nicht**, weil sie selbst deuten wollen | mittel | mittel | Dossier als Vorarbeit, nicht als Ersatz für das Urteil. Quellen zum Nachlesen. Petit und Chen früh als Testnutzer einbinden. |
| R4 | **Kein Budget beim VP of Sales**, dafür bei Sales Ops | unbekannt | hoch | Phase 0 klärt das. Dann Reihenfolge umkehren (Bedürfnis 2 zuerst), der Rollen-Check ist die gemeinsame Basis. |
| R5 | **Volumen steigt, Qualität fällt:** Das Dossier wird zur Ausrede für Massenansprache | mittel | mittel | Z5 als Leitplanke. Kein automatischer Versand. |
| R6 | **Nur ein Kunde:** Das Muster ist vielleicht nicht übertragbar | mittel | niedrig für dieses Projekt, hoch für die Produktidee | Kein Produktversprechen. Übergabe an das Pattern-Team. |
| R7 | **Einwand Sales Ops:** *Das löst mein CRM-Problem nicht.* | hoch | mittel | Ehrlich so benennen. Der Rollen-Check liefert Belege und ist der Einstieg in ein Folgeprojekt. |
| R8 | **Einwand Führung:** *Das ist nur ein weiteres Tool, wir brauchen mehr Calls.* | mittel | mittel | Mit der eigenen Rechnung des VP argumentieren: 4 Prospects pro Stunde. Messung Z2. |
| R9 | **Wartungsaufwand:** Quellen ändern sich, der Agent bricht. Kim kennt das von seinen Tools ("they break"). | mittel | mittel | Monitoring und Wartung im Angebot vorsehen, Umfang `[Platzhalter]`. |

---

## Offene Punkte

1. **Wer hat das Budget?** Die Wahl von Bedürfnis 1 stützt sich darauf, dass VP of Sales oder Enablement Budget freigeben können. Die Interviews belegen Druck, nicht Budget. Entscheidung in Phase 0. Wenn das Budget nur bei Sales Ops liegt, gilt die Abwägung in Anhang A neu.
2. **Rechtliche Zulässigkeit des Datenzugriffs** auf die wichtigste Quelle und Datenschutz bei Personendaten. Klärung vor dem Pilot, mit fachkundiger Beratung.
3. **Ausgabekanal:** CRM, Liste, E-Mail oder Chat? Mit Kim und den Nutzern klären.
4. **Ausgangswerte und Zielwerte** für Z2 bis Z5 fehlen. Werden in Phase 0 mit dem Kunden festgelegt.
5. **Kaufmännisches:** Umfang, Tagessätze, Laufzeit, Wartungsanteil `[Platzhalter]`. Entscheidung beim Management von NeoEmployee.
6. **Welche Signale zählen für dieses Angebot?** O'Neils Checkliste ist der Start. Welche Themen-Signale relevant sind, hängt vom Produkt des Kunden ab.
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

Skala: ● stark, ◐ mittel, ○ schwach. Die Bewertung ist ein begründetes Urteil auf Basis der Interviews, keine Messung.

| Faktor | Bedürfnis 1 | Begründung | Bedürfnis 2 | Begründung |
|---|---|---|---|---|
| **F1 Verbreitung** | ● | 9 von 10, alle Ebenen | ◐ | 5 von 10, davon einer nur teilweise |
| **F2 Dringlichkeit beim Käufer** | ● | Board-Druck beim VP ("the job you're trying to save"), Ramp-KPI bei Enablement | ◐ | Großer Schmerz ("Our CRM is a graveyard."), aber kein Umsatzdruck beim Käufer belegt |
| **F3 Art des Nutzens** | ● | Umsatz: "I'd double my numbers." (Chen) | ◐ | Kosten: 80k-$-Leute als "copy-paste machine", "2 hours a day" laut Reps. Jenkins sieht auch Umsatz: "I could double my quota." |
| **F4 Wettbewerb beim Kunden** | ● | Kein Werkzeug macht die Synthese, vorhandene Lizenzen liefern nur Rohdaten | ○ | ZoomInfo und Clearbit vorhanden, laut Käufer zu teuer und unzuverlässig. Wir konkurrieren über den Preis. |
| **F5 Messbarkeit** | ● | Zielmarke vom Kunden selbst (unter 2 Min.), bestehender KPI (50 Calls) | ● | Bounce-Quote und Anteil veralteter Datensätze (etwa 40 %) |
| **F6 Musterpotenzial (Brücke)** | ● | Generische Signal-Typen, keine Standardsoftware für die Synthese beim Kunden | ◐ | Generisch, aber Markt durch Standardwerkzeuge besetzt |
| **F7 Technisches Risiko** | ◐ | Quellenzugriff (R1), Fehlerrisiko bei Signalen (R2) | ◐ | Gleiches Quellenrisiko, zusätzlich Schreibzugriff ins CRM |
| **F8 Abhängigkeit** | ◐ | Braucht aktuelle Kontaktdaten, gelöst durch Rollen-Check | ● | Steht für sich, ist Basis für Bedürfnis 1 |

**Zusammenfassung:** Bedürfnis 1 liegt bei F1, F2, F3, F4 und F6 vorn. Bei F5 und F7 sind beide gleich. Bei F8 liegt Bedürfnis 2 vorn. Diesen Nachteil gleichen wir aus, indem der Rollen-Check aus Bedürfnis 2 Teil des Dossier-Agenten wird.

### A.3 Strategie-Prüfung (aus der Synthese übernommen und bestätigt)

| Kriterium | Bedürfnis 1 | Bedürfnis 2 |
|---|---|---|
| Vision-Filter: ersetzt einen Mitarbeiter-Skill | ✔ Prospect-Researcher | ✔ Data Clerk |
| Revenue is runway: Budget-Schmerz, als T&M verkaufbar | ✔ drei Käufer mit Druck | ✔ ein Käufer, Kosten schon im Budget |
| Brücke: wiederkehrendes Muster | ✔ mit Einschränkung (ein Kunde) | ✔ mit Einschränkung (ein Kunde) |

Beide bestehen. Die Strategie entscheidet also nicht zwischen den beiden. Den Unterschied machen die Faktoren in A.2, vor allem Dringlichkeit, Art des Nutzens und Wettbewerb. Alle drei hängen direkt an „Revenue is runway“: Wir wählen das Bedürfnis, bei dem der Abschluss wahrscheinlicher und der Folgeauftrag naheliegender ist.

### A.4 Wann die Wahl kippt

Wir würden auf Bedürfnis 2 umschwenken, wenn eine der folgenden Bedingungen eintritt:

- Beim VP of Sales und bei Enablement gibt es kein Budget, bei Sales Ops schon (Offene Punkte, Nr. 1).
- Der technische Spike zeigt, dass Signale nicht zuverlässig abrufbar sind, der Rollen-Abgleich aber schon.
- Der Kunde will zuerst seine Datenbasis bereinigen, bevor er etwas darauf aufbaut.

---

## Loop-Protokoll

wird vom Koordinator geführt
