# PRD: Signal-Brief Agent

**Prepared by:** NeoEmployee
**Date:** 2026-11-03
**Based on:** Interview research — 10 interviews, 2025-10-12 bis 2025-10-23 (Synthese: `output/interview-synthesis-2026-11-03.md`)
**Wer wir sind:** NeoEmployee ist ein eigenfinanziertes Beratungsunternehmen mit 14 Mitarbeitern. Wir bauen maßgeschneiderte KI-Agenten, die Tätigkeiten von Mitarbeitern übernehmen, und rechnen nach Aufwand ab. Langfristig wollen wir daraus Produkte machen.
**Kunde:** In den Unterlagen nicht namentlich genannt. Es ist ein Technologieanbieter, der an Unternehmen verkauft (ein Interview erwähnt API und SDK des Produkts). Die 10 Interviews stammen aus seinem Vertrieb, Marketing und Vertriebsbetrieb.
**Aktualität:** Die Interviews sind rund ein Jahr alt. Vor dem Angebot kurz bei Thorne bestätigen, dass Problem und Zahlen noch gelten (siehe Risiken).
**Engagement type:** Time & Material / Custom AI Agent Build
**Lesehilfe (internes Dokument, nicht für den Kunden):** CEO → „Auf einer Seite" und „Für den CEO" (den Investorenteil kann der CEO überspringen). Investoren → „Auf einer Seite" und „Für Investoren". Umsetzungsteam → ab „Problem Alignment". Fachbegriffe → „Begriffe".

> **Format:** Originalzitate stehen englisch in "…" und sind wörtlich gegen `input/` geprüft. Eigene Umschreibungen sind *kursiv* und stehen ohne Anführungszeichen. **Währungen:** Gehälter in $, so wie in den Interviews genannt. Unsere eigenen Preise in €.

---

# Auf einer Seite

**Das Problem in einem Satz:** Vertriebsmitarbeiter verbringen pro potenziellem Kunden 15 bis 40 Minuten, bei Großkunden sogar Tage, damit, im Internet einen Anlass für das erste Gespräch zu suchen. Deshalb sprechen sie viel zu wenige Kunden an.

**Die Lösung in einem Satz:** Ein KI-Agent erledigt diese Recherche über Nacht. Jeden Morgen liegt für jeden Kontakt auf der Tagesliste ein kurzer Brief bereit: die drei wichtigsten aktuellen Anlässe (z. B. neue Finanzierung, neuer Chef, offene Stellen), jeweils mit Quelle und einem Vorschlag für den Gesprächseinstieg. Der Brief ist in unter zwei Minuten gelesen.

**Belege:** 9 von 10 befragten Personen beim Kunden beschreiben dieses Problem, vom Einsteiger bis zum Vertriebsvorstand. Die Kosten nennen sie selbst:

| Was heute passiert | Wer es sagt |
|---|---|
| 20 statt der geforderten 50 Anrufe am Tag | Jenkins, Vertriebsmitarbeiterin |
| Nur 4 Kontakte pro Stunde, weil jeder 15 Minuten Recherche braucht | Thorne, Vertriebsvorstand |
| Von 100 eingekauften Marketing-Kontakten werden nur 5 bearbeitet | Blunt, Marketing |
| 4 Stunden Recherche pro Nacht, unbezahlt, für 10 Kontakte | Chen, beste Verkäuferin im Team |
| 40 Minuten Suche, und am Ende oft kein Anlass gefunden | O'Neil, Leiterin Einarbeitung |

**Was es dem Kunden wert ist (Schätzung, in Woche 1 zu messen):** Rund ein Dutzend Mitarbeiter im Neukunden-Team ("A dozen bright kids", Ross) verbringen etwa die Hälfte ihrer Zeit mit Recherche ("half my day", Jenkins; "half the job", Baker). Bei rund 80.000 $ Jahresgehalt (Kims Zahl) sind das **rund 480.000 $ Gehalt pro Jahr, die in Recherche statt in Verkaufsgespräche fließen**. Gewinnt der Agent davon nur die Hälfte zurück, werden rund 240.000 $ Gehaltsanteil pro Jahr wieder für Verkaufsgespräche frei, ohne neue Mitarbeiter. *Die Rechnung beruht auf Aussagen aus den Interviews, nicht auf gemessenen Daten. Darum ist die Messung der Ausgangslage Teil von Woche 1.* **Einschränkung:** Ob wir LinkedIn nutzen dürfen, ist offen. Wie viel Nutzen ohne LinkedIn bleibt, zeigt der Prototyp bis Woche 3 (siehe Risiken, Punkt 1).

**Warum dieses Problem und nicht das zweite:** Die Interviews zeigen auch ein zweites Bedürfnis: veraltete Kontaktdaten im Kundensystem (CRM). Wir haben beide nach sieben Kriterien bewertet (Anhang A). Der Signal-Brief gewinnt klar (92 zu 63 Punkte) und in jedem geprüften Szenario. Er ist in Wochen lieferbar, weil er nur liest und nichts in Kundensysteme schreibt. Er wird von drei Führungskräften mit Budget gewollt. Und nach unserem bisherigen Stand liefert ihn kein Standard-Tool, das der Kunde schon nutzt. *Das ist eine Annahme, die wir vor dem Angebot prüfen.* Das zweite Bedürfnis wird zum geplanten Folgeauftrag.

**Was NeoEmployee davon hat:**
1. **Jetzt:** Ein 6-wöchiges Kundenprojekt, abgerechnet nach Aufwand. Es bringt sofort Umsatz und verlängert unsere finanzielle Reichweite (Runway).
2. **Danach:** Ein vorgezeichneter Folgeauftrag (Phase 2: Kontaktdaten im CRM automatisch aktuell halten).
3. **Später:** Ein Kandidat für unser erstes Produkt. Unsere These: Das Problem ist nicht kundenspezifisch, weil jedes Vertriebsteam, das Kunden über öffentliche Informationen findet, es haben dürfte. *Belegt ist das bisher nur bei diesem einen Kunden.*

**Die Entscheidung:** Ja oder nein dazu, dieses Projekt dem Kunden anzubieten. Empfehlung: **Ja.**

---

# Für den CEO: Was wir entscheiden

| Frage | Antwort |
|---|---|
| **Was verkaufen wir?** | Einen maßgeschneiderten KI-Agenten, der die Recherche-Arbeit im Neukundenvertrieb übernimmt. Abrechnung nach Aufwand (Time & Material), wie in unserem Geschäftsmodell. |
| **An wen?** | Hauptansprechpartner ist der Vertriebsvorstand (Thorne). Er steht beim Aufsichtsgremium unter Druck, weil sein Team zu wenig vom Markt abdeckt, und er beschreibt die Lösung selbst: "just hand them the dossier". Mitstreiter sind der Vertriebsdirektor (Ross) und die Leiterin der Einarbeitung (O'Neil). |
| **Wer baut es? (Vorschlag)** | **2 Personen für 6 Wochen:** eine Person baut den Agenten und die Anbindung an die Datenquellen, eine Person führt das Projekt beim Kunden (Kickoff, Messung der Ausgangslage, Tests mit den Vertriebsleuten). Das sind 2 von 12 Leuten außerhalb des Pattern-Teams. Das 2-köpfige Pattern-Team baut nicht mit, bekommt aber am Ende eine Übergabe für die Produkt-Prüfung. Die Personalplanung wird intern bestätigt. |
| **Wie viel Umsatz, wie schnell?** | **Volumen:** 2 Personen × 6 Wochen ≈ 60 Personentage × unser Tagessatz. Beispiel: Bei einem Tagessatz von 1.000 € sind das rund 60.000 €. *Der Tagessatz ist ein Platzhalter und wird vom CEO festgelegt.* **Abrechnung:** nach Aufwand, Vorschlag alle zwei Wochen. Damit fließt das erste Geld nach 2 Wochen. **Untergrenze:** Bricht der Kunde am Entscheidungspunkt nach Woche 3 ab, sind es rund 30 Personentage (im Beispiel ca. 30.000 €). **Ausbau:** Phase 2 (Kontaktdaten im CRM) ist als Folgeauftrag vorgezeichnet. |
| **Ab wann?** | Start, sobald der Kunde zusagt und 2 Personen frei sind. Das Startdatum ist offen und wird mit der internen Auslastung abgeglichen. Woche 1 beginnt mit der rechtlichen Prüfung der Datenquellen. |
| **Was kostet es uns?** | Bis zur Zusage: Vertriebsaufwand (Angebot, ein Termin mit Thorne) und die erste rechtliche Einschätzung der Datenquellen. Danach nur Projektzeit, die bezahlt wird. Keine Vorab-Investition. Datenquellen und Rechenkosten laufen über das Projekt. Wer eine tiefere Rechtsprüfung bezahlt, wird im Angebot geregelt (Vorschlag: Kunde, als Teil von Woche 1). |
| **Gibt es schon ein Kaufsignal?** | **Noch nicht.** Die Interviews belegen Schmerz und einen ausdrücklichen Lösungswunsch beim Entscheider ("If we could automate that 'intel gathering' piece—just hand them the dossier—we'd be unstoppable.", Thorne). Budget ist damit noch nicht freigegeben. Auch wer unterschreibt, ist offen. **Nächster Schritt:** Angebot an Thorne. Dafür braucht es eine eigene, kundentaugliche Fassung: Problem, Lösung, Ablauf, Messung und Preis. *Dieses PRD ist intern* (Personalplanung, Tagessatz-Logik, Produkt- und Investorenthesen) *und geht so nicht an den Kunden.* Kaufsignal ist seine Zusage zu Woche 1 (Messung der Ausgangslage). |
| **Passt es zur Strategie?** | Ja, in allen drei Punkten. (1) Es ersetzt einen Mitarbeiter-Skill, die Recherche, und erfüllt damit unseren Vision-Filter. (2) Es bringt schnell Umsatz („Revenue is runway"). (3) Es ist voraussichtlich ein wiederkehrendes Muster und damit ein Baustein für spätere Produkte. *Das ist eine These, belegt bisher nur bei diesem Kunden (siehe „Für Investoren", Punkt 5).* |
| **Was ist das größte Risiko?** | Der rechtlich saubere Zugriff auf Datenquellen, vor allem LinkedIn. Gegenmaßnahme: rechtliche Prüfung in Woche 1, und das erste Produkt stützt sich auf Firmenseiten, News, Finanzierungs- und Stellenmeldungen. Zweites Risiko: schlechte Gesprächsaufhänger blamieren den Verkäufer. Gegenmaßnahme: Jeder Hinweis braucht eine Quelle, sonst wird er nicht gezeigt. |
| **Was, wenn es nicht klappt?** | Der Agent wird abgeschaltet und das Team arbeitet wie heute weiter. Weil er nichts in Kundensysteme schreibt, muss nichts zurückgebaut werden. Unser Risiko ist auf die Projektzeit begrenzt, und die wird bezahlt. |
| **Woran messen wir Erfolg?** | **Zielkennzahl:** Die Recherchezeit pro Kontakt sinkt auf höchstens 2 Minuten. Zusätzlich berichtet: Anrufe pro Tag, bearbeitete Marketing-Kontakte. Die Antwortquote darf nicht sinken. *Das ist eine Ziel- und Abnahme-Kennzahl, keine Haftung.* Wir rechnen nach Aufwand ab, unabhängig davon, ob das Ziel erreicht wird. **Entscheidungspunkt nach Woche 3:** Der Kunde sieht den Prototyp auf echten Kontakten und entscheidet, ob es weitergeht. Bricht er ab, endet das Projekt nach rund 30 Personentagen. |
| **Was brauchen wir vom Kunden?** | Lesezugriff auf das CRM, eine Liste der Kontakte, 3–5 Testpersonen aus dem Vertrieb und einen Ansprechpartner für die Messung der Ausgangslage. |

---

# Für Investoren: Vom Projekt zum Produkt

> *Hinweis:* Laut unserer Strategie nehmen wir derzeit kein Fremdkapital auf. Dieser Abschnitt erklärt das Vorhaben so, dass es auch einem Investor einleuchtet. Das ist zugleich ein Test, ob die Produkt-These trägt.

**1. Das Problem: bei einem Kunden durchgängig belegt, am Markt noch zu prüfen.** Vertriebsteams finden neue Kunden heute vor allem über öffentliche Informationen: Unternehmensnachrichten, Finanzierungsrunden, Stellenanzeigen, Berufsprofile. Diese Informationen sind frei verfügbar, aber unstrukturiert: "It's all out there in plain sight… It's just unstructured." (Thorne). Das Sortieren erledigen heute gut bezahlte Menschen von Hand. Beim befragten Kunden sind das schätzungsweise rund 480.000 $ Gehalt pro Jahr in einem einzigen Team. *Das ist der Gehaltsanteil eines Teams, keine Marktgröße.* Belegt ist: 9 von 10 Befragten aus allen Ebenen dieses einen Kunden beschreiben das Problem. Nicht belegt ist, wie viele andere Firmen es in dieser Stärke haben.

**2. Warum jetzt.** Bisherige Vertriebsdaten-Tools liefern Rohdaten (Kontakte, Firmenlisten). Die eigentliche Arbeit, aus vielen verstreuten Quellen *den einen relevanten Gesprächsanlass* herauszufiltern, war bisher Menschenarbeit. Die Interviews belegen, *dass* genau hier der Engpass liegt: "That's the bottleneck." (Thorne). Sie belegen nicht, *dass* KI das schon gut genug kann. Das ist unsere technische These: Sprachmodelle können verstreute Texte inzwischen so zusammenfassen, dass ein Verkäufer damit arbeiten kann, solange jede Aussage mit Quelle belegt ist. **Geprüft wird das im Prototyp (Woche 2–3)** an echten Kontakten: Welcher Anteil der Briefs wird von den Verkäufern als hilfreich markiert?

**3. Kapitaleffizienter Weg zum Produkt.** Der Kunde bezahlt die Entwicklung:

| Stufe | Was passiert | Wer bezahlt | Weiter zur nächsten Stufe nur, wenn … (Vorschlag) |
|---|---|---|---|
| 1. Kundenprojekt | Signal-Brief Agent für diesen Kunden, 6 Wochen | Kunde (Time & Material) | … die Recherchezeit pro Kontakt messbar auf höchstens 2 Minuten sinkt, die Antwortquote nicht fällt **und** die Mehrheit der Briefs als hilfreich markiert wird. |
| 2. Wiederholung | Derselbe Agent bei 2–3 weiteren Kunden aus anderen Branchen | Jeweilige Kunden | … bei mindestens 2 von 3 weiteren Kunden dieselben Signal-Typen funktionieren, und zwar nur durch Einstellungen, ohne neuen Code. Außerdem muss eine systematische Wettbewerbsprüfung zeigen, dass niemand genau das schon als Standard verkauft. |
| 3. Produkt | Standard-Agent mit einstellbaren Signal-Typen, für viele Firmen ohne Einzelanpassung | Lizenz bzw. Abo (Modell offen) | – |

Die Prüfung übernimmt unser 2-köpfiges Pattern-Team, das bei uns gezielt nach wiederkehrenden Mustern über Kunden hinweg sucht. Die Schwellen sind Vorschläge und werden vor Stufe 2 festgelegt.

**4. Was uns verteidigbar machen könnte, ehrlich eingeordnet.** Jeder Brief bekommt eine Rückmeldung des Verkäufers (hilfreich ja/nein). Später, wenn wir Lesezugriff auf Termin-Daten im CRM haben, kommt dazu, ob daraus ein Termin wurde. So lernen wir, *welche Signal-Typen in welcher Situation zu Terminen führen*. **Heute ist das noch ein dünner Vorsprung:** Ja/Nein-Klicks allein schützen nicht vor Nachahmern. Zum echten Vorsprung wird es nur unter zwei Bedingungen. (a) Die Termin-Zuordnung kommt hinzu, frühestens in Phase 2. (b) Kunden erlauben vertraglich, dass wir aus ihren Rückmeldungen anonymisiert über Kunden hinweg lernen. Die Daten selbst gehören dem jeweiligen Kunden. Diese Klausel muss ab dem ersten Vertrag verhandelt werden.

**5. Was wahr sein muss und noch nicht bewiesen ist.**
- **Das Muster gilt auch bei anderen Kunden.** Bisher kommen alle 10 Interviews aus *einem* Unternehmen. Das Muster zieht sich zwar durch alle Ebenen dort, die Bestätigung bei weiteren Kunden steht aber aus. Das ist die wichtigste offene Annahme.
- **Der wirtschaftliche Effekt ist messbar.** Die Werte oben beruhen auf Aussagen der Befragten. Das Projekt misst sie in Woche 1 und nach dem Launch.
- **Es gibt keinen Wettbewerber, der genau das schon als Standard liefert.** Datenanbieter und KI-Vertriebstools könnten diese Funktion nachrüsten. Das wird während Stufe 2 systematisch geprüft und ist Bedingung für den Schritt zu Stufe 3 (siehe Tabelle).
- **Der Datenzugang bleibt rechtlich sauber, und der Agent ist auch ohne LinkedIn wertvoll.** Laut Kim läuft die Recherche heute zu 90 % über LinkedIn. Ob LinkedIn genutzt werden darf, ist offen. Wie viel Nutzen ohne LinkedIn bleibt, zeigt erst der Prototyp.
- **Ein Projektgeschäft kann zum Produkt werden.** Dienstleister scheitern oft an diesem Übergang. Unser Schutz ist, dass Stufe 3 nur beginnt, wenn Stufe 2 zeigt, dass Einstellungen statt neuem Code reichen.

---

# Begriffe

| Begriff | Bedeutung |
|---|---|
| **SDR** (Sales Development Rep) | Vertriebsmitarbeiter, der neue Kontakte anspricht und Termine für die Verkäufer vereinbart |
| **AE** (Account Executive) | Verkäufer, der aus Terminen Abschlüsse macht |
| **Prospect** | Potenzieller Kunde bzw. Ansprechpartner, der noch nicht kauft |
| **Lead / MQL** | Kontakt, den das Marketing gewonnen hat (z. B. über ein Webinar) und an den Vertrieb übergibt |
| **CRM** | Kundendatenbank des Vertriebs (hier: Salesforce) |
| **Signal** | Öffentlicher Hinweis, dass jetzt ein guter Moment für ein Gespräch ist: Finanzierung, Führungswechsel, Stellenaufbau, ein Thema, über das die Person schreibt |
| **Gesprächsaufhänger** | Der konkrete Anlass, mit dem der Verkäufer das erste Gespräch beginnt |
| **Ramp-Zeit** | Zeit, bis ein neuer Vertriebsmitarbeiter voll produktiv ist |
| **KPI** | Messgröße, an der ein Mitarbeiter gemessen wird, hier z. B. 50 Anrufe pro Tag |
| **Time & Material (T&M)** | Abrechnung nach tatsächlichem Aufwand statt Festpreis |
| **Runway** | Wie lange NeoEmployee mit den vorhandenen Einnahmen weiterarbeiten kann. Wir sind eigenfinanziert, jeder Auftrag verlängert sie („Revenue is runway") |
| **Vision-Filter** | Unsere Regel: Wir nehmen nur Aufträge an, bei denen ein KI-Agent eine Tätigkeit von Mitarbeitern übernimmt |
| **Pattern-Team / Bridge** | 2 unserer 14 Mitarbeiter suchen gezielt nach Mustern, die bei mehreren Kunden wiederkehren. Diese Muster sind die „Brücke" (Bridge) vom Einzelprojekt zum Produkt |

---

# Problem Alignment

## Problem & Opportunity

**Vertriebler verbringen 15 Minuten bis mehrere Tage pro Prospect damit, aus verstreuten öffentlichen Quellen von Hand einen „Grund zum Anrufen" zusammenzusuchen. Deshalb fehlt im ganzen Funnel das Volumen, obwohl die Daten öffentlich vorhanden sind.**

- **Warum es für den Kunden zählt:** Der VP Sales verliert die Marktabdeckung, auf die der Board schaut: „that's only 4 prospects an hour. That's a joke." (Thorne). Die Closer haben zu wenig Termine: „They are starving for good meetings." (Ross). Teuer eingekaufte Marketing-Leads bleiben liegen: „They ignore 90% of what we send", weil die Recherche nicht skaliert: „So they do it for 5 and ignore the rest." (Blunt).
- **Warum es für NeoEmployee zählt:** Das Problem besteht alle Strategie-Filter (siehe Anhang A). Mehrere Budget-Owner leiden aktiv darunter, ein erster Nutzen ist in wenigen Wochen zeigbar, und das Muster ist vermutlich generisch genug für die Produkt-Bridge (These, bisher bei einem Kunden belegt).
- **Belege aus den Interviews:**
  - Thorne (VP Sales): "They're turning unstructured noise into structured talk tracks manually. That's the bottleneck."
  - O'Neil (Dir. Enablement): "The problem isn't that the data is missing; it's that they have to sift through so much irrelevant noise to find those three specific things." und "can you find it in under two minutes?"
  - Ross (Sales Director): "They're jumping between five different tabs."
  - Jenkins (SDR): "I'm supposed to be making 50 calls a day. That's the KPI. But I'm lucky if I get to 20"
  - Green (Junior SDR): "30 minutes for one email!"
  - Chen (AE): "I spend maybe 4 hours a night just building a list of 10 people to email the next day."
  - Petit (Enterprise AE): "I spend days—literal days—just mapping an account before I even send the first 'hello' email."
  - Baker (Senior Rep): "It feels like half the job is just staring at a screen trying to find an angle."
- **Am stärksten betroffen:** SDRs (Jenkins, Green, rund ein Dutzend im Lead-Gen-Team laut Ross: "A dozen bright kids"), AEs (Chen, Baker, Petit) und die Führung, die das Volumen verantwortet (Thorne, Ross, O'Neil).
- **Warum dringend, was geht täglich verloren:** Jeder Rep verliert täglich Stunden. Jenkins schafft 20 statt 50 Calls am Tag. Jede neue SDR-Kohorte verliert Ramp-Zeit. Die Top-Performerin hält ihre Zahlen nur durch unbezahlte Nachtarbeit, ein Ausfallrisiko: "It's my "second shift."" (Chen). Wettbewerber warten nicht: "The competition isn't waiting for your ducks to line up." (Thorne).
- **Warum jetzt (Stand der Interviews, Oktober 2025, vor dem Angebot zu bestätigen):** Thorne kam direkt aus dem Board, wo die Abdeckung Thema war. O'Neil startete am Tag des Interviews eine neue Kohorte. Jenkins steckte mitten im Quartalsende. Der Druck war deutlich sichtbar, und die Käufer formulieren die Lösung selbst: "just hand them the dossier" (Thorne), "hand them the "signals" on a platter" (O'Neil).

## High-Level Approach

**Ein Agent, der für jeden Prospect auf der Tagesliste eines Reps einen Signal-Brief erstellt: die drei relevantesten aktuellen Signale aus öffentlichen Quellen, jeweils mit Quelle und einem Gesprächsaufhänger. Der Brief ist in unter zwei Minuten gelesen und hängt dort, wo der Rep arbeitet.**

Warum dieser Ansatz: Er setzt genau an dem Engpass an, den die Befragten selbst benennen, dem *Strukturieren*. Daten fehlen nicht („It's all out there in plain sight", Thorne). Personalisierung bleibt erhalten, sie wird nur billiger. Damit löst sich Ross' Zwickmühle „I want speed, they want quality, and right now we have neither." auf, ohne dass Qualität geopfert wird.

**Alternatives considered:**
- **Lead-Validierung und CRM-Datenabgleich (Bedürfnis 2) als erster Auftrag:** Zurückgestellt, siehe Anhang A. Das Liefer- und Integrationsrisiko ist höher, und die Tool-Kategorie existiert schon. Ein leichter Teil davon ist als Feature 2 im MVP, der Rest kommt als Phase 2.
- **Mehr Lizenzen für ZoomInfo oder Sales Navigator kaufen:** Verworfen. Lizenzen liefern Rohdaten, keinen Aufhänger. Das Kernproblem bleibt: Ein Mensch strukturiert von Hand. Außerdem sind es keine NeoEmployee-Leistungen (Vision-Filter).
- **„Mehr wählen", also Druck statt Werkzeug** (Thorne: "I just have to keep yelling at them to make more calls"; Ross: "Dialing!"): Verworfen. Ohne Kontext fallen die Antwortquoten, darauf bestehen Ross' eigenes Team und Blunt („conversion is higher if you know the context, I admit that").
- **Vollautomatische Ansprache (Agent schreibt und versendet selbst):** Verworfen fürs MVP. Erfahrene Reps wollen die Interpretation behalten („You have to read between the lines", Petit). Generische Automatik erzeugt genau die „fake" Aufhänger, die Green ablehnt.

### Narrative

**Vorher, Rachel (Junior SDR, Monat 2):** Rachel hat 50 Leads auf ihrer Liste. Beim ersten öffnet sie LinkedIn, die Firmenseite und Google News und scrollt durch Posts. Nach 30 Minuten hat sie einen Aufhänger, ein Sauerteig-Foto, und eine E-Mail. Beim zweiten Lead findet sie nichts Persönliches und nimmt den „Digital Transformation"-Like, der sich *fake* anfühlt. Mittags hat sie acht E-Mails geschrieben und fragt sich, warum die anderen schneller sind. Abends, im Bild ihrer Kollegin Chen: Eine AE kopiert um Mitternacht Daten in eine Tabelle, damit sie morgen zehn Leute anschreiben kann.

**Nachher:** Um 8:00 liegt für jeden der 50 Leads ein Signal-Brief bereit. Beim ersten Lead steht dort: *Series-B-Finanzierung vor 9 Tagen (Quelle), drei offene Stellen im Bereich Cloud-Infrastruktur (Quelle), neuer VP Engineering seit 6 Wochen (Quelle). Aufhänger: Neuer VP, frisches Budget, Infrastruktur-Ausbau.* Beim zweiten Lead steht ehrlich: *Keine relevanten Signale in den letzten 90 Tagen, Priorität niedrig.* Beim dritten: *Kontakt laut öffentlichem Profil nicht mehr im Unternehmen, möglicher Nachfolger: …* Rachel liest jeden Brief in unter zwei Minuten, entscheidet selbst, was sie daraus macht, und ist mittags bei Call 25. Chen schläft.

## Goals

1. **Recherche-Zeit pro Prospect von heute 15–40 Minuten auf höchstens 2 Minuten** (O'Neils Benchmark: "can you find it in under two minutes?"). Gemessen per Zeit-Stichprobe vor und nach dem Launch.
2. **Mehr Outreach-Volumen pro Rep:** SDR-Calls pro Tag in Richtung KPI 50 (Jenkins heute: 20) und ein höherer Anteil bearbeiteter Inbound-Leads (Blunt heute: *rund 5 von 100*). Die Zielwerte werden in Woche 1 mit dem Kunden auf Basis der Baseline festgelegt.
3. **Gefühl:** Reps erleben sich wieder als Verkäufer und nicht als Rechercheure. Gegenbild aus den Interviews: "not be a professional lurker" (Green), "not a salesperson" (Jenkins). Gemessen per Kurzumfrage vor und nach dem Launch.
4. **Guardrail:** Antwort- und Terminquote pro Outreach darf **nicht sinken**. Die Personalisierung muss mindestens so gut bleiben wie heute (Ross' Zwickmühle). Die Bounce-Rate darf nicht steigen.

## Non-Goals

1. **Kein Versand und keine Sequenzierung durch den Agenten.** Der Rep entscheidet und schreibt. Gründe: das Urteil bleibt beim Menschen, Akzeptanz bei Erfahrenen (Petit, Baker), kein Risiko generischer „fake" Ansprache.
2. **Kein Schreiben in CRM-Felder und keine Datenbereinigung des Bestands.** Das ist Bedürfnis 2 und für Phase 2 bzw. einen Folgeauftrag reserviert (Integrationsrisiko, siehe Anhang A).
3. **Keine Lösung des Marketing-Sales-Konflikts um die Lead-Definition** (Blunt, Ross). Das ist eine Organisationsfrage und kein Agent-Skill. Er entschärft sich indirekt, wenn mehr Leads bearbeitbar werden.
4. **Kein vollständiges Einfluss-Mapping großer Enterprise-Accounts** (Petits „conspiracy wall"). Saved for future: Das ist eine eigene, größere Ausbaustufe desselben Musters.

---

# Solution Alignment

## Key Features

**Plan of record (MVP):**

1. **Signal-Brief pro Prospect.** Bis zu 3 Signale aus den letzten 90 Tagen, jedes mit Datum, Quelle (Link) und einem Satz „Warum relevant". Dazu ein vorgeschlagener Gesprächsaufhänger. Die Signal-Typen sind O'Neils Checkliste ("Recent funding news—Series B or C preferably. 2. New hiring in engineering or ops. 3. Recent leadership changes at the VP level."), ergänzt um Thornes Prüfliste: "You need to know if they are hiring, if they just raised money, if they're about to go under."
2. **Beschäftigungs-Check (nur lesend).** Vor dem Brief prüft der Agent, ob die Person laut öffentlicher Quelle noch im Unternehmen ist. Wenn nicht, markiert er das und schlägt einen möglichen Nachfolger vor (Jenkins: "who the new person is"). Das ist der leichte Teil von Bedürfnis 2.
3. **Tagesliste über Nacht vorbereitet.** Der Rep lädt seine Liste hoch (CSV/CRM-Export) oder sie kommt automatisch aus einer CRM-Ansicht. Bis Arbeitsbeginn liegen alle Briefs bereit. Ersetzt Chens „second shift".
4. **Priorisierung nach Signalstärke.** Die Liste wird sortiert: starke, aktuelle Signale zuerst, „keine Signale" zuletzt. So geht die begrenzte Zeit an Prospects mit echtem Anlass (Green, Blunt).

**Future considerations:**

1. **Phase 2: CRM-Abgleich (Bedürfnis 2).** Erkannte Wechsel und Titel nach Freigabe ins CRM schreiben, dazu Anreicherung, die nur bei erkannter Änderung läuft (Kims Kostenargument). Folgeauftrag für Sales Ops.
2. **Themen-Intent-Suche:** "Show me everyone who posted about Cloud Migration in the last week." (Green), also Prospects über Themen finden statt Listen abarbeiten.
3. **Account-Map für Enterprise** (Petit): Beziehungen, Champions und Blocker aus Signalen ableiten.
4. **Signal-Reporting für die Führung:** welche Signal-Typen zu Terminen führen. Das löst Ross' Attributionsproblem ("They attribute leads to 'Outbound' in the CRM, but that could mean anything.").

### Key Flows

1. **Liste rein:** Am Vorabend exportiert der Rep seine Tagesliste (oder die CRM-Ansicht wird automatisch gezogen).
2. **Beschäftigungs-Check:** Für jeden Kontakt prüft der Agent die aktuelle Firma und Rolle. Ausgeschiedene Kontakte bekommen den Status *ausgeschieden* und, wenn möglich, einen Nachfolger-Vorschlag.
3. **Signal-Suche:** Für aktive Kontakte und ihre Firma durchsucht der Agent die freigegebenen Quellen (Firmenseite, Pressemitteilungen, News, Funding-Datenbanken, Stellenanzeigen, öffentliche Profile) nach Signalen aus den letzten 90 Tagen.
4. **Filtern und Strukturieren:** Der Agent bewertet die Signale nach Typ, Aktualität und Bezug zum Angebot des Kunden und behält höchstens 3. Dazu formuliert er pro Prospect einen Aufhänger.
5. **Ausliefern:** Bis 8:00 hängt der Brief als Notiz am CRM-Datensatz (ohne Felder zu überschreiben) und erscheint als priorisierte Tagesliste. Der Kanal (CRM-Notiz, E-Mail-Digest oder Slack) wird im Kickoff festgelegt.
6. **Rep arbeitet:** Der Rep liest den Brief (Ziel unter 2 Minuten), klickt bei Bedarf auf die Quellen, schreibt bzw. ruft selbst an und gibt per Klick Feedback („Aufhänger hilfreich / nicht hilfreich").
7. **Lernen:** Das Feedback und später die Antwortquoten fließen in die Gewichtung der Signal-Typen ein.

### Key Logic

1. **Was der Agent zeigt:** Nur Signale, die (a) aus den letzten 90 Tagen stammen, (b) zu einem der vereinbarten Signal-Typen gehören und (c) eine prüfbare Quelle haben. Höchstens 3 pro Prospect, nach Relevanz sortiert. Persönliche Details ohne Geschäftsbezug (Urlaub, Familie, Fotos) werden **nicht** gezeigt. Gegenbild: Ross' "his vacation to Cabo" und O'Neils "college reunion photos".
2. **Format:** Lesbar in unter 2 Minuten. Pro Signal ein Satz, plus ein Aufhänger. Keine Fließtext-Biografie (Ross: "It's like they're writing a biography before they say hello.").
3. **Fehlende oder widersprüchliche Daten:** Findet der Agent nichts Relevantes, sagt er das ausdrücklich („Keine relevanten Signale") und erfindet keinen generischen Aufhänger. Bei widersprüchlichen Quellen zeigt er beide mit Datum. Ist unsicher, ob jemand ausgeschieden ist, wird das als *unsicher* markiert und nicht als Tatsache.
4. **Was der Agent nicht anfasst:** Er überschreibt keine CRM-Felder, ändert keine Kontaktdaten und versendet nichts. Er hängt nur Notizen an (MVP). Er nutzt nur Quellen, die in der Datenquellen-Prüfung (Operational Checklist) freigegeben sind.
5. **Nicht-funktional:** Die Tagesliste von bis zu 100 Prospects pro Rep ist bis 8:00 fertig. Ein Einzel-Brief auf Abruf dauert unter 60 Sekunden (Zielwert, im Prototyp zu prüfen). Fällt eine Quelle aus, liefert der Agent die übrigen Signale und kennzeichnet die Lücke, statt ganz auszufallen (Kims Erfahrung mit nächtlichen Sync-Ausfällen). Jeder Brief wird mit Quellen und Zeitstempel protokolliert.

---

# Development and Launch Planning

| Milestone | Target | Description |
|-----------|--------|-------------|
| Kickoff | Week 1 | Scope bestätigen, Signal-Typen und Quellen festlegen, CRM-Lesezugriff, Baseline messen (Recherche-Zeit, Calls/Tag, Antwortquote) — *Termine mit dem Kunden zu bestätigen* |
| Agent prototype | Week 2–3 | Erste Version auf 20 Test-Prospects aus echten Listen (z. B. einer SDR- und einer AE-Liste) |
| Client feedback round | Week 3 | 3–5 Reps testen (Vorschlag: je ein SDR, Junior-SDR, AE, Senior-Rep). Bewertet werden Treffsicherheit der Signale und Nutzbarkeit der Aufhänger. |
| Integration complete | Week 4–5 | Brief als CRM-Notiz angehängt (kein Feld-Write-back), Tagesliste über Nacht automatisiert, Lieferkanal live |
| QA & edge case hardening | Week 5–6 | Ausgeschiedene Kontakte, „keine Signale", widersprüchliche Quellen, Ausfall von Quellen, Format |
| Launch | Week 6 | Alle Reps des Lead-Gen-Teams eingebunden, Messung gegen Baseline startet |

## Operational Checklist

- [ ] CRM credentials and API access confirmed (MVP: **nur lesen** und Notizen anhängen)
- [ ] Prospect list format agreed (CSV / CRM export / live sync)
- [ ] Output delivery method confirmed (email digest / CRM attachment / Slack)
- [ ] Data sources and scraping permissions reviewed (insbesondere Nutzungsbedingungen von LinkedIn, rechtliche Prüfung vor Woche 2)
- [ ] Signal-Typen und 90-Tage-Fenster mit Vertriebsleitung abgestimmt
- [ ] Rep team onboarding session scheduled (gemeinsam mit Enablement, O'Neil)
- [ ] Success metrics baseline captured before launch
- [ ] Rollback / pause plan documented (Agent abschalten = Reps arbeiten wie heute weiter, keine Datenänderung rückgängig zu machen)

---

## Other

### Risks

1. **Zugang zu und Verlässlichkeit der Datenquellen:** LinkedIn ist die Hauptquelle der Reps ("It's 90% LinkedIn", Kim). Ein automatisierter Zugriff kann gegen Nutzungsbedingungen verstoßen. Ohne LinkedIn ist ein Teil des geschätzten Nutzens (480.000 $ / 240.000 $) unsicher. Die Signal-Typen aus O'Neils Checkliste (Finanzierung, Stellenaufbau, Führungswechsel) gibt es aber auch in Pressemitteilungen, Finanzierungsdatenbanken, Stellenbörsen und auf Firmenseiten. *Gegenmaßnahme:* Das MVP stützt sich auf diese Quellen und nutzt LinkedIn nur im rechtlich geprüften Rahmen. Juristische Prüfung in Woche 1. Wie viel Nutzen ohne LinkedIn bleibt, ist die Kernfrage am Entscheidungspunkt nach Woche 3.
2. **Komplexität der CRM-Integration:** Bewusst klein gehalten (nur lesen und Notiz anhängen). Bestehende Syncs sind fragil (Kim). *Gegenmaßnahme:* Kein Schreibzugriff auf Felder im MVP, Lieferung notfalls per E-Mail-Digest.
3. **Akzeptanz bei den Reps:** Skeptiker wie Baker ("Just buzzwords") und Perfektionisten ("Paralysis by analysis", Thorne). *Gegenmaßnahme:* Quellen immer sichtbar (Vertrauen), ehrliches „keine Signale" statt Füllstoff, frühe Testgruppe aus Skeptikern und Top-Performern (Chen).
4. **Qualität der Aufhänger und erfundene Inhalte:** Ein falscher Aufhänger blamiert den Rep. Genau diese Angst treibt heute das Über-Recherchieren: "I looked like a dinosaur" (Baker). *Gegenmaßnahme:* Jedes Signal braucht eine Quelle, sonst wird es nicht gezeigt. Feedback-Knopf pro Brief.
5. **Wirtschaftliches Risiko für NeoEmployee:** Der Umsatz-Effekt ist von den Befragten geschätzt („I'd double my numbers") und nicht gemessen. *Gegenmaßnahme:* Baseline in Woche 1. Die Recherche-Zeit ist die Ziel- und Abnahme-Kennzahl (sicher messbar), keine Haftung. Der Umsatz-Effekt wird nur berichtet.
6. **Veraltete Belege:** Die Interviews sind rund ein Jahr alt (Oktober 2025). Problem, Teamgröße oder Prioritäten können sich geändert haben. *Gegenmaßnahme:* Vor dem Angebot ein kurzes Gespräch mit Thorne, das Problem und Zahlen bestätigt. Die Messung der Ausgangslage in Woche 1 ersetzt die Interview-Zahlen dann ohnehin durch gemessene Werte.

### FAQ

**Q: Why not just buy more ZoomInfo licenses?**
A: Mehr Lizenzen beheben einen Engpass, der nicht der Hauptengpass ist. ZoomInfo liefert Kontaktdaten, keinen Grund zum Anrufen. Thorne sagt ausdrücklich, dass die Daten öffentlich vorliegen ("It's not secret… It's just unstructured") und der Engpass das manuelle Strukturieren ist. Kim hält die Tools zudem für unzuverlässig und teuer ("they break, or they're too expensive to run on every single contact record"). Und selbst mit Lizenz recherchiert Jenkins am Ende per Google ("the ZoomInfo login is always taken").

**Q: How is this different from what the SDRs are doing today?**
A: Inhaltlich ist es dasselbe, was gute Reps heute tun: Signale finden und daraus einen Aufhänger machen. Ross beschreibt es: "They're jumping between five different tabs." Der Unterschied: Die Arbeit dauert Sekunden statt 15–40 Minuten, sie ist auf drei relevante Signale fokussiert statt auf "college reunion photos" (O'Neil), sie folgt für alle Reps derselben Methode statt nach individuellem Talent, und sie läuft über Nacht statt in Chens "second shift".

**Q: Warum nicht zuerst das CRM aufräumen (Bedürfnis 2)?**
A: Siehe Anhang A. Es ist wichtig, aber langsamer lieferbar, riskanter und gegen eine bestehende Tool-Kategorie schwerer zu verkaufen. Der Beschäftigungs-Check deckt den akuten Teil (Ansprache ausgeschiedener Kontakte) schon im MVP ab. Der volle Abgleich ist als Folgeauftrag geplant.

### Appendix

- Interview synthesis: `output/interview-synthesis-2026-11-03.md`
- Individual interview analyses: `output/interview-individual-*-2025-10-*.md` (10 Dateien)
- Company context: `context/company.md`
- Strategy context: `context/strategy.md`
- Älteres PRD auf Basis eines Interviews: `output/PRD-lead-validator-2026-08-31.md`
- Kundenfassung des Angebots (Englisch, für Thorne): `output/proposal-signal-brief-agent-2026-11-03.md`

#### Anhang A: Problem-Auswahl im Detail. Welches Bedürfnis hat die höhere Chance auf wirtschaftlichen Erfolg?

Die Synthese nennt zwei Bedürfnisse:

- **Bedürfnis 1, Signale fertig aufbereitet:** Der „Grund zum Anrufen" kommt fertig beim Vertrieb an. Der Agent ersetzt den Skill *Prospect-Researcher*. Belegt in 9 von 10 Interviews.
- **Bedürfnis 2, Kontaktdaten aktuell im CRM:** Kontaktdaten sind verifiziert und landen ohne Handarbeit im CRM. Der Agent ersetzt den Skill *Data Clerk*. Belegt in 5 von 10 Interviews.

Dieses PRD baut nur **eines** davon als ersten Auftrag. Bewertet wurde mit den Kriterien aus `scripts/PRD-writer.md` (Dringlichkeit, ROI-Klarheit, Liefergeschwindigkeit, Vision-Fit), ergänzt um die Bedingungen aus `context/strategy.md`: Bootstrap, „Revenue is runway", Bridge zu Produkten.

##### Bewertung (1 = schwach, 5 = stark)

| # | Kriterium | Gewicht | Woher | Bedürfnis 1: Signale | Bedürfnis 2: Kontaktdaten/CRM |
|---|---|---|---|---|---|
| K1 | **Dringlichkeit beim Budget-Owner** | 20 | PRD-writer: „urgency"; Strategie: Deal muss jetzt zustande kommen | **5.** Drei Entscheider mit Budget und Druck: VP Sales direkt aus dem Board („the job you're trying to save", Thorne), Sales Director („starving for good meetings", Ross), Director Enablement mit Ramp-KPI („It's a massive drain on our ramp time", O'Neil) | **3.** Ein Entscheider (Sales Ops, Kim) mit starkem Schmerz („Our CRM is a graveyard"). Er ist aber eine Ebene tiefer, und das Thema wird nicht im Board diskutiert. |
| K2 | **ROI-Klarheit** | 15 | PRD-writer: „clarity of the ROI" | **4.** Zeitkosten genau beziffert: 15 Min. pro Prospect (Thorne), 30 Min. pro E-Mail (Green), 40 Min. ohne Ergebnis (O'Neil), 4 Std. für 10 Kontakte (Chen). Der Umsatz-Effekt ist von den Befragten selbst geschätzt („I'd double my numbers", Chen) und muss erst gemessen werden. | **5.** Sehr direkte Kostenrechnung: 2 Std. pro Rep und Tag Kontaktpflege (Kim gibt die Angabe der Reps wieder), „paid $80k a year acting as a copy-paste machine". Dazu Jenkins: „I could double my quota. Easy." Das bezieht sich ausdrücklich auf die Verifikation, spricht also für Bedürfnis 2. |
| K3 | **Time-to-Revenue: lieferbar in Wochen** | 20 | PRD-writer: „revenue in weeks, not months", „prefer the quick fix" | **5.** Das MVP ist **nur lesend**: öffentliche Quellen rein, Brief raus. Es muss nicht ins CRM schreiben, kein Altbestand muss bereinigt werden, und das Ergebnis lässt sich ab Woche 2 an 20 Test-Prospects zeigen. | **2.** Braucht Schreibzugriff auf das System of Record, Dubletten- und Konfliktlogik und dauerhaften Abgleich über den ganzen Bestand. Die vorhandene Integration ist schon fragil („The API sync broke again at 3 AM", Kim). Ein Fehler beschädigt die Daten aller. |
| K4 | **Vision-Fit: ersetzt Mitarbeiter-Skill** | 10 | Strategie: Vision-Filter | **5.** Ersetzt die Research-Arbeit, die O'Neil so beschreibt: „high-priced data miners" | **5.** Ersetzt die Datenpflege, die Baker so beschreibt: „I want to sell, not be a data clerk." |
| K5 | **Abgrenzung zu vorhandenen Tools, Bereitschaft für Custom-Bau** | 15 | Strategie: „Revenue is runway". Wir gewinnen nur, wo Standard-Tools nicht reichen. | **4.** Vorhandene Tools liefern *Daten*, aber keinen *Aufhänger*. Thorne: „It's all out there in plain sight… It's just unstructured." Der Engpass ist laut ihm das Strukturieren: „That's the bottleneck." Annahme: Das Zusammenführen zum Gesprächsaufhänger ist kein fertig gekauftes Standard-Feature beim Kunden. Muss im Kickoff bestätigt werden. | **2.** Hier gibt es eine etablierte Tool-Kategorie (ZoomInfo, Clearbit), die der Kunde schon kennt und bezahlt. Kim kritisiert sie („they break, or they're too expensive"), aber die naheliegende Antwort des Kunden wäre *Tool besser konfigurieren oder mehr Lizenzen kaufen*. Das macht es schwer, ein Custom-Projekt zu verkaufen. |
| K6 | **Produktisierung: Bridge, Pattern** | 10 | Strategie: „The Bridge: Pattern Recognition" | **5.** 9 von 10 Interviews, von SDR bis VP. Die Signal-Typen sind generisch und nicht kundenspezifisch: Funding, Hiring, Leadership-Wechsel (O'Neils Checkliste), dazu Themen-Intent (Green). | **4.** Jedes Unternehmen mit CRM hat das Problem. Als Produkt konkurriert es aber mit der etablierten Kategorie aus K5. |
| K7 | **Liefer- und Technikrisiko** (hoch = wenig Risiko) | 10 | Bootstrap: Ein gescheitertes Projekt kostet Runway und Referenz. | **4.** Risiken: Qualität der Aufhänger und Zugang zu Quellen. Ein Fehler im Brief bleibt beim Rep sichtbar und richtet keinen Schaden im System an. | **2.** Schreibzugriff auf die Kerndaten, dauerhaft auf LinkedIn als Quelle angewiesen („It's 90% LinkedIn", Kim). Damit ist es rechtlich und technisch das größere Risiko. |
| | **Gewichtete Punktzahl (von 100)** | | | **92** | **63** |

##### Robustheit: Kippt die Entscheidung bei anderen Gewichten?

| Szenario | Bedürfnis 1 | Bedürfnis 2 | Gewinner |
|---|---|---|---|
| Basis (Gewichte oben) | 92 | 63 | 1 |
| Alle Kriterien gleich gewichtet | 91 | 66 | 1 |
| „Kostensicht": ROI-Klarheit doppelt (30), Time-to-Revenue und Abgrenzung halbiert (je 10) | 90 | 72 | 1 |
| Sales Ops ist der Käufer (K1 für Bedürfnis 2 = 5) | 92 | 71 | 1 |
| Günstigster Fall für Bedürfnis 2: CRM-Integration wäre trivial (K3 und K7 = 5) | 92 | 81 | 1 |

**Ergebnis:** **Bedürfnis 1 hat die höhere Wahrscheinlichkeit auf wirtschaftlichen Erfolg.** Das gilt in jedem geprüften Szenario. Bedürfnis 2 ist nur bei einem Kriterium vorn, der ROI-Klarheit. Seine Kosten sind am direktesten belegt. Das reicht aber nicht gegen die zwei Kriterien, die in der Bootstrap-Phase am meisten zählen: **schnell lieferbar** und **gegen bestehende Tools verkaufbar**.

**Was wir von Bedürfnis 2 trotzdem mitnehmen:** Ein Brief über jemanden, der die Firma verlassen hat, ist wertlos. Darum enthält das MVP einen **nur lesenden Beschäftigungs-Check** (Feature 2). Der volle CRM-Abgleich ist als Phase 2 geplant und damit ein **natürlicher Folgeauftrag** auf Time-&-Material-Basis, sobald Vertrauen und Integration stehen.

**Abgrenzung zum älteren PRD** (`output/PRD-lead-validator-2026-08-31.md`): Es stützte sich auf **ein** Interview (Jenkins) und wählte deshalb die Lead-Validierung. Mit zehn Interviews verschiebt sich das Bild. Jenkins' Schmerz ist echt und wird hier mitbedient (Feature 2). Der größere und schneller verkaufbare Hebel ist aber der fehlende Gesprächsaufhänger, den 9 von 10 Personen beschreiben.

#### Anhang B: Loop-Protokoll

##### Runde 1: PRD erstellen und Probleme abwägen (2026-11-03)

Ziel des Loops: *PRD auf Basis der Gesamtsynthese nach `scripts/PRD-writer.md` schreiben, bis abgewogen und dokumentiert ist, welches der Probleme die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat. Dabei die Strategie beachten und die Loops dokumentieren.*

| Durchgang | Was gemacht wurde | Ergebnis | Abbruchkriterium erfüllt? |
|---|---|---|---|
| **1: Vorgaben finden** | `scripts/` durchsucht. Gefunden: `PRD-writer.md` (Skript mit Vorlage), `My-PRD-Template.md` (allgemeinere Vorlage), `interview-to-PRD.md` (Pipeline, die `PRD-writer.md` aufruft) | `PRD-writer.md` ist das maßgebliche Skript: Es nennt die Inputs, die Auswahlkriterien und die Ausgabedatei. | Nein. Noch kein Inhalt. |
| **2: Inputs lesen** | `company.md`, `strategy.md`, Synthese vom 2026-11-03 (2 Bedürfnisse) und das ältere PRD gelesen | Das ältere PRD (1 Interview) wählte Bedürfnis 2. Diese Abweichung musste ausdrücklich begründet werden. | Nein. |
| **3: Kriterien festlegen** | Die vier Auswahlkriterien aus `PRD-writer.md` (urgency, ROI clarity, speed to deliver, vision fit) übernommen und um drei Strategie-Kriterien ergänzt: Abgrenzung zu vorhandenen Tools („Revenue is runway"), Produktisierung („Bridge"), Lieferrisiko (Bootstrap). Gewichte nach der Skript-Vorgabe „revenue in weeks, not months": Dringlichkeit und Time-to-Revenue je 20. | 7 Kriterien, Gewichtssumme 100 | Nein. |
| **4: Bewerten** | Beide Bedürfnisse pro Kriterium mit Interview-Beleg bewertet | Bedürfnis 1: 92, Bedürfnis 2: 63. Bedürfnis 2 gewinnt nur bei der ROI-Klarheit (5 vs. 4). Das Jenkins-Zitat „double my quota" wurde fair Bedürfnis 2 zugeordnet. | Teilweise. Gewinner da, aber ist er robust? |
| **5: Robustheit prüfen** | Vier Alternativ-Szenarien gerechnet: gleiche Gewichte, Kostensicht, Sales Ops als Käufer, trivialer Integrationsaufwand für Bedürfnis 2 | Bedürfnis 1 gewinnt in allen Szenarien (90–92 vs. 66–81). | **Ja, für die Abwägung.** |
| **6: Gewinner schärfen** | Geprüft, was der Verlierer zum Gewinner beitragen muss | Der nur lesende Beschäftigungs-Check (Feature 2) kommt ins MVP, weil ein Brief über Ausgeschiedene wertlos ist. Der volle CRM-Abgleich wird zu Phase 2 und Folgeauftrag. | Ja. |
| **7: Template füllen** | Alle Abschnitte der Vorlage aus `PRD-writer.md` gefüllt. Fehlende Termine relativ angegeben (Week 1–6) und zur Bestätigung durch den Kunden markiert, wie das Skript es verlangt | PRD-Entwurf | Noch offen: alle Abschnitte vorhanden? Zitate korrekt? |
| **8a: Prüfen, erster Lauf** | Automatisch geprüft: (a) jede Abschnittsüberschrift der Vorlage im PRD vorhanden, (b) jedes Zitat wörtlich in `input/` bzw. `strategy.md`/`company.md`/`PRD-writer.md`, (c) Punktzahlen aus der Tabelle nachgerechnet | (a) 17/17 Überschriften vorhanden. 3 Oberkapitel ohne eigenen Text, wie in der Vorlage. (b) 7 „Abweichungen" gemeldet, die ein Fehler im Prüfskript waren: Es hat deutsche („…") und englische ("…") Anführungszeichen vermischt und falsche Textstücke herausgeschnitten. **Ergebnis verworfen.** | Nein. Prüfung ungültig. |
| **8b: Prüfen, korrigiertes Skript** | Anführungszeichen-Typen getrennt ausgewertet | 66 Interview-Zitate und 7 Skript-/Strategie-Zitate belegt, 11 eigene deutsche Formulierungen (keine Zitate). **1 echte Abweichung:** "hiring signals, funding news, financial distress" ist eine Umschreibung aus der Thorne-Einzelanalyse und nicht Thornes Wortlaut. | Nein. Korrektur nötig. |
| **8c: Korrigieren** | Durch Thornes Originalsatz ersetzt: "You need to know if they are hiring, if they just raised money, if they're about to go under." | PRD korrigiert | Erneute Prüfung nötig. |
| **9: Abschlussprüfung** | Prüfung 8b erneut, dazu Punktzahlen direkt aus der Bewertungstabelle nachgerechnet | **67 Interview-Zitate und 7 Skript-/Strategie-Zitate wörtlich belegt, 0 nicht belegt.** Gewichte summieren sich auf 100, Punktzahlen 92 / 63 bestätigt. | **Ja. Loop beendet.** |

**Kriterien zum Abbruch des Loops:**

1. PRD nach vorgegebenem Skript → ✔ (alle Abschnitte der Vorlage aus `PRD-writer.md` gefüllt, Dateiname nach Skript-Konvention)
2. Basierend auf der Gesamtsynthese → ✔ (beide Bedürfnisse aus `interview-synthesis-2026-11-03.md` bewertet, Belege aus allen 10 Interviews)
3. Abgewogen und dokumentiert, welches Problem die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat → ✔ (Anhang A „Problem-Auswahl im Detail": 7 Kriterien, 5 Szenarien, Bedürfnis 1 gewinnt in allen)
4. Strategie beachtet → ✔ (Vision-Filter, Revenue is runway, Time-to-Revenue in Wochen, Bridge/Produktisierung als Kriterien. Das Verliererbedürfnis wird zum geplanten Folgeauftrag.)
5. Loops dokumentiert → ✔ (diese Tabelle, inklusive verworfenem Prüflauf)

**Offene Punkte für den Kunden-Kickoff** (laut Skript markiert, nicht vom Loop lösbar): konkrete Termine, Zielwerte nach Baseline-Messung, rechtliche Freigabe der Datenquellen, Bestätigung der Annahme in K5 (kein bestehendes Tool, das Signale schon zu Aufhängern verdichtet).


##### Runde 2: Überarbeitung für CEO und Investoren (2026-11-03)

Ziel des Loops: *Den PRD bearbeiten, bis er sowohl Investoren als auch dem CEO gut zu erklären ist.*
Prüfmethode: Zwei Subagenten lesen das PRD ohne Vorwissen über den Entstehungsprozess, einer in der Rolle des NeoEmployee-CEO (kennt `strategy.md` und `company.md`), einer als skeptischer B2B-Investor (kennt nur das PRD). Beide erklären es zurück und geben ein Urteil ab. Der Loop endet, wenn beide das beste Urteil geben.

| Durchgang | Was gemacht wurde | Ergebnis | Abbruchkriterium erfüllt? |
|---|---|---|---|
| **R2-1: Lesergruppen klären** | Festgelegt, was jede Gruppe wissen will. CEO: Entscheidung, Aufwand, Umsatz, Risiko, Strategie. Investor: Problemgröße, „Warum jetzt", Weg zum Produkt, Verteidigbarkeit, offene Annahmen. | Struktur: Kurzfassung „Auf einer Seite", eigener CEO-Teil, eigener Investorenteil, Begriffe, Lesehilfe. Die Detailbewertung wandert in Anhang A. | Nein. |
| **R2-2: Umbau** | Neue Abschnitte geschrieben. Wertabschätzung aus Interview-Zahlen (Dutzend Reps × halbe Zeit × 80.000 $ ≈ 480.000 $/Jahr), klar als Schätzung markiert. Verweise auf den verschobenen Abschnitt angepasst. | PRD v2 | Prüfung nötig. |
| **R2-3: Testlesung 1** | CEO- und Investor-Subagent lesen parallel | **CEO: „fast".** Es fehlten Teamgröße, Preislogik, Startdatum, Kaufsignal und Kundenname. Die Interviews sind ein Jahr alt, der LinkedIn-Vorbehalt war nicht in den Wert eingerechnet, unklar war das Verhältnis von Zielkennzahl zu Abrechnung nach Aufwand, und die Kosten vor Vertragsschluss fehlten. **Investor: „fast".** „Kein Standard-Tool" und „kein Einzelfall" standen als Tatsache da, obwohl das Dokument selbst Vorbehalte nennt. Es fehlten prüfbare Kriterien für die Produkt-Stufen, die Verteidigbarkeit war überzeichnet und das Dateneigentum offen. Firmenprofil fehlte, Fachjargon war unerklärt, „Warum jetzt" unbelegt. | Nein. |
| **R2-4: Einarbeiten** | CEO-Teil: Teamvorschlag (2 Personen × 6 Wochen ≈ 60 Personentage), Umsatz-Rechenbeispiel mit Tagessatz als Platzhalter, Abrechnung alle 2 Wochen, ehrliches „noch kein Kaufsignal" mit nächstem Schritt, Startdatum als offene Entscheidung, Kosten vor Vertragsschluss, Zielkennzahl ohne Haftung plus Entscheidungspunkt nach Woche 3. Kopf: Firmenprofil, Kundenbeschreibung, Hinweis auf das Alter der Interviews. Investorenteil: Behauptungen auf Belegtes zurückgeführt, Schwellen pro Stufe, Verteidigbarkeit als „dünn" eingeordnet mit zwei Bedingungen und Datenklausel, „Warum jetzt" als technische These, die der Prototyp prüft. Neue Begriffe erklärt. Neues Risiko 6 (veraltete Belege). | PRD v3, Zitat-Prüfung: 0 nicht belegt | Erneute Testlesung nötig. |
| **R2-5: Testlesung 2** | Dieselben Subagenten lesen erneut und haken ihre Punkte ab | **CEO: „verständlich und entscheidungsreif"** (9 von 10 Punkten gelöst, LinkedIn-Abschlag „teilweise, vertretbar"). Neue Kleinigkeiten: Das PRD ist intern und darf nicht ans Angebot, die Kurzfassung war zu lang, und die Untergrenze bei Abbruch fehlte in der Umsatzzeile. **Investor: „verständlich und überzeugend erklärt"** (alle 7 Punkte gelöst). Neue Kleinigkeiten: Zeitpunkt der Wettbewerbsprüfung uneinheitlich, „Warum jetzt" nicht datiert, $/€ gemischt, zwei Muster-Aussagen noch als Tatsache formuliert. | **Ja, beide Urteile erreicht.** |
| **R2-6: Kleinigkeiten bereinigen** | Alle redaktionellen Punkte aus R2-5 umgesetzt. LinkedIn-Details aus der Kurzfassung in die Risiken verschoben. Das PRD ist als intern markiert, für das Angebot ist eine eigene Kundenfassung vorgesehen. Den Investorenteil kann der CEO laut Lesehilfe überspringen. Der Vorschlag des CEO-Lesers, den Investorenteil zu kürzen, wurde *nicht* umgesetzt, weil das Ziel ausdrücklich auch Investoren einschließt. | PRD final | – |
| **R2-7: Abschlussprüfung** | Abschnitte der Vorlage, Zitate und Punktzahlen automatisch geprüft | Alle 17 Abschnitte der Vorlage vorhanden. 75 Interview-Zitate und 10 Strategie-/Skript-Zitate wörtlich belegt, 0 nicht belegt. Punktzahlen 92 / 63 unverändert. Kurzfassung 510 Wörter. | **Ja. Loop beendet.** |

**Bewusst offen gelassen**, weil nur CEO oder Kunde es liefern können und das Dokument es nicht erfinden darf: konkreter Tagessatz, Startdatum, Kundenname, Budgetfreigabe beim Kunden, Bestätigung der ein Jahr alten Interview-Zahlen. Jeder Punkt ist im Dokument als offene Entscheidung mit nächstem Schritt benannt.

---

## Product Summary

Der Signal-Brief Agent ist ein KI-Agent für B2B-Vertriebsteams. Er übernimmt die Prospect-Recherche, die heute pro Kontakt 15 Minuten bis mehrere Tage kostet. Jeden Morgen liefert er für jeden Prospect auf der Tagesliste die drei relevantesten aktuellen Signale wie Funding, Hiring oder Leadership-Wechsel, jeweils mit Quelle und einem fertigen Gesprächsaufhänger, und prüft vorher, ob die Person überhaupt noch im Unternehmen ist. Er ersetzt damit den Skill des Prospect-Researchers, nicht das Urteil des Verkäufers: Der Rep liest den Brief in unter zwei Minuten und entscheidet selbst. Ab dem Launch-Tag verbringen SDRs und AEs ihre Zeit mit Gesprächen statt mit Tab-Wechseln, und die Personalisierung, die Antworten bringt, skaliert auf die ganze Liste statt auf fünf von hundert Leads.
