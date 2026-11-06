# Synthese: Zwei Kundenbedürfnisse aus zehn Interviews

**Datum:** 2026-11-03
**Quellen:** 10 Einzelanalysen in `output/interview-individual-*.md` (Interviews 2025-10-12 bis 2025-10-23), Strategie in `context/strategy.md`, Firmenprofil in `context/company.md`
**Zitate:** wörtlich aus den Interviews (Englisch), über die Einzelanalysen zurückverfolgbar

---

## Ergebnis auf einen Blick

| # | Bedürfnis | Wer (n/10) | Belegte Kosten heute | Ersetzter Mitarbeiter-Skill |
|---|---|---|---|---|
| **1** | **Der „Grund zum Anrufen" muss fertig aufbereitet beim Vertriebler ankommen, in Minuten statt in 15 Minuten bis mehreren Tagen.** Gemeint sind Signale und Kontext pro Prospect und Account: Funding, Jobwechsel, Hiring, Themen, Beziehungen. | 9/10 | 15–40 Min. pro Prospect, 4 Std. pro Nacht für 10 Kontakte, Tage pro Enterprise-Account, 20 statt 50 Calls am Tag, 5 von 100 Leads bearbeitet | Prospect-Researcher / Research-Analyst |
| **2** | **Kontaktdaten müssen aktuell und verifiziert sein und ohne Handarbeit im CRM landen.** Gemeint sind: Wer sitzt noch wo, mit welcher Rolle und welcher E-Mail? | 5/10 | ca. 40 % der Kontakte veraltet, „Half the emails bounce immediately", ca. 2 Std. pro Rep und Tag Pflege von Kontaktfeldern, 80k-$-Leute als „copy-paste machine" | Data Clerk / Data-Steward |

Beide Bedürfnisse bestehen alle drei Strategie-Prüfungen (Abschnitt 4). Kein anderer Kandidat schafft das (Abschnitt 1).

---

## 1. Wie aus allen Problemen zwei Bedürfnisse wurden

Alle in den zehn Analysen genannten Bedürfnisse wurden in Kandidaten gruppiert. Dann wurde jeder Kandidat nach drei Kriterien bewertet:

- **Häufigkeit:** In wie vielen der 10 Interviews kommt das Bedürfnis vor?
- **Belegte Kosten:** Nennt mindestens eine Person eine Zahl (Zeit, Quote, Geld)?
- **Strategie-Fit:** Erfüllt der Kandidat alle drei Kriterien aus `strategy.md`?
  - **S1 Vision-Filter:** Lässt sich ein Mitarbeiter-Skill durch einen KI-Agenten ersetzen?
  - **S2 Revenue is runway:** Gibt es jetzt Budget-Schmerz bei Entscheidern? Ist es als Time-&-Material-Projekt verkaufbar?
  - **S3 Pattern/Produkt:** Ist es ein wiederkehrendes Muster, das nicht kundenspezifisch ist?

| Kandidat | Interviews | n | Zahl belegt | S1 | S2 | S3 | Ergebnis |
|---|---|---|---|---|---|---|---|
| **A: Signale/Kontext fertig aufbereitet** | Jenkins, Ross, Chen, Baker, Blunt, Green, Thorne, Petit, O'Neil | **9** | ja, bei 9 | ✔ | ✔ | ✔ | **→ Bedürfnis 1** |
| **B: Aktuelle Kontaktdaten automatisch im CRM** | Jenkins, Kim, Baker, Chen, Petit (teilweise) | **5** | ja (40 %, 2 Std./Tag, 80k $) | ✔ | ✔ | ✔ | **→ Bedürfnis 2** |
| C: Gemeinsame Definition „guter Lead" (Marketing ↔ Sales) | Blunt, Ross, Jenkins, Thorne | 4 | nein | ✘ Abstimmungsfrage zwischen Teams, kein Skill | ◐ | ◐ | raus |
| D: Transparenz/Attribution über die Research-Arbeit | Ross, Thorne, Blunt, Kim | 4 | nein | ◐ Reporting, kein ersetzter Skill | ◐ | ◐ | raus. Fällt als Nebenprodukt von A/B an |
| E: Schnellere Einarbeitung, Playbook für Research | O'Neil, Green | 2 | ja (40 vs. 2 Min.) | ◐ | ✔ | ◐ | geht in A auf: Wer A löst, nimmt Research aus dem Ramp |
| F: Mehr Tool-Lizenzen (ZoomInfo, Sales Navigator) | Jenkins, Chen | 2 | nein | ✘ Lizenzkauf, kein Agent | ✘ | ✘ | raus |
| G: Authentischer Kanal statt LinkedIn-Posting | Baker | 1 | nein | ✘ | ✘ | ✘ | raus |
| H: „Verkaufen statt Datenpflege" (Rolle, Identität) | Baker, Chen, Green, Jenkins, Petit, O'Neil, Kim | 7 | – | – | – | – | kein eigenes Bedürfnis. Emotionale **Folge** von A und B, verstärkt beide |

**Warum A und B herausstechen:** Nur diese beiden Kandidaten haben zugleich (a) Zahlen aus mehreren Interviews, (b) einen klar abgrenzbaren menschlichen Skill, den ein Agent übernehmen kann, und (c) Entscheider mit Budget unter den Betroffenen. Kandidat H ist zwar häufig, beschreibt aber das *Gefühl*, das A und B erzeugen, und kein eigenes Bedürfnis.

**Warum es zwei bleiben und nicht eins werden:** A und B sind verschiedene Skills mit verschiedenen Käufern. A beantwortet *„Warum soll ich diese Person jetzt anrufen und was sage ich?"*. Das ist der Research-Analyst, den VP Sales, Sales Director und Enablement bezahlen. B beantwortet *„Gibt es diese Person noch unter dieser Adresse, und steht das korrekt im System?"*. Das ist der Data Clerk, den Sales Ops bezahlt. Ein Kontext-Dossier über jemanden, der vor drei Jahren gegangen ist, hilft niemandem. Darum ist B die Datengrundlage, ohne die A nicht trägt.

---

## 2. Bedürfnis 1: Der „Grund zum Anrufen" kommt fertig an

> **Vertriebler brauchen pro Prospect und Account die zwei bis drei relevanten Signale (Funding, Jobwechsel, Hiring, Themen, Beziehungen), aus öffentlichen Quellen zusammengeführt und als Gesprächsaufhänger aufbereitet, damit sie ihre Zeit auf Gespräche statt auf Recherche verwenden und Personalisierung nicht mehr mit Volumen konkurriert.**

### 2.1 Zitat-Spur (rückverfolgbar)

| Person, Rolle | Zitat (wörtlich) | Ableitung | Quelle |
|---|---|---|---|
| **Marcus Thorne**, VP of Sales | "But does it really take 15 minutes per prospect? 15 minutes! If you do the math, that's only 4 prospects an hour. That's a joke." | 15 Min. Research pro Prospect begrenzen die Reichweite auf 4 pro Stunde. Genau diese Kennzahl schaut sich der Board an. | `interview-individual-thorne-2025-10-21.md` §4, §6 |
| Marcus Thorne | "They're turning unstructured noise into structured talk tracks manually. That's the bottleneck. It's the 'manual' part that kills me." | Der Engpass ist nicht das Finden der Daten. Es ist das manuelle Strukturieren zu einem Gesprächsaufhänger. | thorne §3 #3 |
| Marcus Thorne | "If we could automate that 'intel gathering' piece—just hand them the dossier—we'd be unstoppable." | Der Käufer formuliert selbst die Lösung: ein fertiges Dossier. | thorne §5, §6 |
| **Linda O'Neil**, Dir. Sales Enablement | "The problem isn't that the data is missing; it's that they have to sift through so much irrelevant noise to find those three specific things. It's not just "is the data there?" — it's "can you find it in under two minutes?"" | Gebraucht werden **drei Signale in unter zwei Minuten**. Heute dauert es 40 Minuten („forty minutes have passed"), also rund das 20-Fache. | `interview-individual-oneil-2025-10-23.md` §3, §4 |
| Linda O'Neil | "If we could just hand them the "signals" on a platter—"Hey, here are the three things you need for this prospect"—we could spend our training time teaching them how to actually *sell*…" | Zweiter Käufer, gleiche Lösung. Dazu kommt ein messbarer Nutzen: kürzere Ramp-Zeit. | oneil §6 |
| **Mike Ross**, Sales Director | "My guys are great closers, absolute sharks, but they're starving, man. They are starving for good meetings." | Die Closing-Kapazität liegt brach, weil oben im Funnel zu wenig ankommt. | `interview-individual-ross-2025-10-14.md` §3 #1 |
| Mike Ross | "They're jumping between five different tabs. Corporate website, some news aggregator, LinkedIn, maybe Crunchbase." | Der Kontext liegt verstreut in mehreren Quellen. Ross nennt außerdem „20 minutes" pro E-Mail. | ross §4, §6 |
| **Sarah Jenkins**, SDR | "I'm supposed to be making 50 calls a day. That's the KPI. But I'm lucky if I get to 20…" | 60 % Rückstand auf den KPI, jeden Tag. Laut ihr: „half my day just trying to figure out who I'm supposed to actually call". | `interview-individual-jenkins-2025-10-12.md` §4 |
| Sarah Jenkins | "It's totally random. It feels like I'm fishing without bait." | Es gibt kein System für Trigger-Signale wie Jobwechsel oder Beförderungen. | jenkins §3 #9, §6 |
| **Rachel Green**, Junior SDR | "But that took me 30 minutes to find. 30 minutes for one email!" | 30 Min. pro personalisierter E-Mail. Bei rund 50 Leads ist das nicht machbar („I don't know"). | `interview-individual-green-2025-10-20.md` §4 |
| Rachel Green | "Like, "Show me everyone who posted about Cloud Migration in the last week." That would save me hours of scrolling." | Gesucht ist kein persönlicher Small Talk, sondern ein **intent-basiertes Signal**. | green §3 #7, §6 |
| **Jessica Chen**, Account Executive (Top-Performerin) | "I spend maybe 4 hours a night just building a list of 10 people to email the next day. 4 hours!" | Rund 24 Min. pro Prospect, unbezahlt in der „second shift". | `interview-individual-chen-2025-10-15.md` §3 #6 |
| Jessica Chen | "If I could just snap my fingers and have that list of "New CTOs at Series B companies" with their emails, I'd kill it. I'd double my numbers." | Trigger (Series B) wird mit der richtigen Person verknüpft. Sie beziffert den Effekt selbst: doppelter Umsatz. | chen §4, §6 |
| **Sam Petit**, Enterprise AE | "I spend days—literal days—just mapping an account before I even send the first 'hello' email." | Enterprise-Variante desselben Bedürfnisses: Account- und Beziehungs-Kontext statt Einzelsignal. | `interview-individual-petit-2025-10-22.md` §3 #2 |
| Sam Petit | "It's 80% reading LinkedIn profiles and 20% actual sales strategy. Which, when you think about it, is completely backwards." | Das Verhältnis von Recherche zu Strategie ist umgedreht. | petit §6 |
| **Tom Baker**, Senior Sales Rep | "It feels like half the job is just staring at a screen trying to find an angle." | Selbst der Beziehungsverkäufer braucht heute den Aufhänger. Ohne ihn: „I looked like a dinosaur". | `interview-individual-baker-2025-10-16.md` §3 #1, #3 |
| **Emily Blunt**, Marketing Manager | "I get why they do it—conversion is higher if you know the context, I admit that—but it doesn't scale. They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." | Der Kontext erhöht die Conversion, skaliert aber nicht. Darum bleiben 95 von 100 bezahlten Leads liegen. | `interview-individual-blunt-2025-10-18.md` §4, §6 |

### 2.2 Ableitung

1. **Muster:** Neun von zehn Personen beschreiben dieselbe Kette, ohne voneinander zu wissen: *Daten sind öffentlich vorhanden* („It's all out there in plain sight", Thorne) → *aber verstreut und verrauscht* („scattered across fifty tabs", Petit; „irrelevant noise", O'Neil) → *ein Mensch strukturiert sie von Hand zum Aufhänger* → *das dauert 15 Min. bis Tage* → *dadurch fehlt das Volumen* (20 statt 50 Calls, 4 pro Stunde, 5 von 100 Leads, „a trickle. Droplets.").
2. **Gesagt vs. gebraucht:** Die Führung sagt „schneller/mehr wählen" (Ross: „Dialing!", Thorne: „keep yelling at them"). Die Basis sagt „mehr Daten" (Green: LinkedIn-Scraper, Jenkins: mehr Lizenzen). Gebraucht wird weder Druck noch mehr Rohdaten, sondern **die fertige Synthese**. Personalisierung ist Voraussetzung für Antworten, das bestätigen Ross („they insist it's the only way"), Blunt („conversion is higher") und Baker („you can't get the meeting without the 'research' now"). Also muss die Personalisierung billig werden und nicht wegfallen.
3. **Wichtige Randbedingung:** Die Erfahrenen wollen die *Interpretation* behalten (Petit: „You have to read between the lines", Chen: „I have to know *everything* about them"). Der Agent ersetzt das Zusammentragen und Strukturieren, nicht das Urteil im Gespräch.

---

## 3. Bedürfnis 2: Kontaktdaten sind aktuell und landen ohne Handarbeit im CRM

> **Sales-Organisationen brauchen Kontakt- und Rollendaten (Arbeitgeber, Titel, E-Mail), die automatisch mit der realen Quelle (vor allem LinkedIn) abgeglichen und sauber ins CRM geschrieben werden. Wechsel sollen erkannt und Nachfolger gefunden werden. Dann wird das CRM wieder zur verlässlichen Quelle, und kein Vertriebler arbeitet mehr als Datenerfasser.**

### 3.1 Zitat-Spur (rückverfolgbar)

| Person, Rolle | Zitat (wörtlich) | Ableitung | Quelle |
|---|---|---|---|
| **David Kim**, Sales Ops Manager (Budget für den Stack) | "Our CRM is a graveyard. It's a graveyard of outdated info." | Datenintegrität ist sein größtes Problem: „Data integrity. 100%. No doubt about it." | `interview-individual-kim-2025-10-19.md` §3 #2, §6 |
| David Kim | "Why do I have a human being paid $80k a year acting as a copy-paste machine? It makes no sense." | Der Käufer beziffert selbst, dass ein Skill fehl-besetzt ist. Laut den Reps sind das „2 hours a day" pro Person für Kontaktfelder. | kim §2, §4 |
| David Kim | "But I see the web traffic logs. I know the truth. It's 90% LinkedIn. They just keep that tab open all day. It's their real database." | Die eigentliche Quelle liegt außerhalb des CRM. Gebraucht wird eine Brücke von LinkedIn ins CRM, die nicht von menschlicher Disziplin abhängt. | kim §4, §6 |
| David Kim | (zu ZoomInfo/Clearbit) "…they break, or they're too expensive to run on every single contact record. So we rely on humans." | Bestehende Anreicherungs-Tools scheitern an Zuverlässigkeit und Kosten. Das ist die Lücke, die ein Agent füllen kann. | kim §3 #6 |
| **Sarah Jenkins**, SDR | "It's zombie data. Half the emails bounce immediately, or I call and they're like "Who?" or the person left the company three years ago to go raise alpacas in Vermont." | Die Lead-Daten sind beim Arbeiten schon veraltet, ca. 40 % der Kontakte sind weg („like 40% of the time"). | jenkins §3 #1, #3, §6 |
| Sarah Jenkins | "…because I'm stuck copy-pasting job titles from LinkedIn profiles into Salesforce fields." | Sie nennt selbst als Grund für 20 statt 50 Calls: manuelle Übertragung ins CRM. | jenkins §6 |
| Sarah Jenkins | "I swear, if I didn't have to verify every single lead, I could double my quota. Easy." | Sie beziffert den Effekt selbst. | jenkins §4 |
| **Tom Baker**, Senior Sales Rep | "And the data in our CRM? It's always wrong anyway. 'Oh, he's at Oracle.' No, he left six months ago, look at his LinkedIn!" | Dasselbe Muster aus Sicht des Erfahrensten: CRM falsch, LinkedIn richtig. | baker §3 #2, §6 |
| **Jessica Chen**, Account Executive | "I use like three different chrome extensions just to guess their email address." / "I'm manually copying data into a spreadsheet at midnight." | E-Mails werden geraten statt verifiziert, und Daten werden von Hand in ein Schatten-System neben dem CRM kopiert. | chen §3 #5, #7 |
| **Sam Petit**, Enterprise AE (teilweise) | "titles are completely made up—"Head of Global Synergy" could mean anything." | Rohdaten müssen normalisiert werden, bevor sie im System nutzbar sind. | petit §3 #5 |

### 3.2 Ableitung

1. **Muster:** Fünf Personen auf drei Ebenen (SDR, AE/Senior Rep, Ops) beschreiben dieselbe Umkehr. Die Wahrheit steht auf LinkedIn, das CRM hinkt hinterher, und Menschen gleichen beides von Hand ab. Kim fasst es zusammen: „Ours is just where they log the result so they get paid commissions. It's backwards."
2. **Gesagt vs. gebraucht:** Gesagt wird „bessere Listen von Marketing" (Jenkins), „mehr Lizenzen" (Jenkins), „Reps sollen sauberer pflegen" (Kim: „Fat fingers, lazy entries"). Gebraucht wird ein **dauerhafter Abgleich, ausgelöst durch Veränderungen**, und kein einmaliger Export und keine Disziplin-Kampagne. Kim formuliert es selbst: Anreicherung muss bei erkannter Änderung laufen, nicht als teurer Komplett-Refresh.
3. **Verhältnis zu Bedürfnis 1:** B ist die Grundlage für A. Signale über Personen, die nicht mehr dort arbeiten, erzeugen Bounces und peinliche Calls („Who?"). Jenkins nennt Jobwechsel zugleich als Problem (Bedürfnis 2: wer ist weg?) und als Chance (Bedürfnis 1: „who the new person is" als neuer Lead).

---

## 4. Nachweis: Ausrichtung an der Firmenstrategie

| Strategie-Kriterium (`strategy.md`) | Bedürfnis 1: Signale fertig aufbereitet | Bedürfnis 2: Kontaktdaten aktuell im CRM |
|---|---|---|
| **Vision-Filter:** „AI agents that replace employee skills", „We do not chase work outside that frame" | ✔ Ersetzt den Skill **Prospect-Researcher**. O'Neil: „teaching them to be high-priced data miners… expert search engine operators". Thorne: „just hand them the dossier". | ✔ Ersetzt den Skill **Data Clerk**. Kim: „copy-paste machine". Baker: „I want to sell, not be a data clerk." |
| **Bootstrap / „Revenue is runway":** „anything that brings in money and aligns with our vision, we do" | ✔ Die Käufer haben Budget-Verantwortung und Druck: VP Sales vor dem Board („the job you're trying to save"), Sales Director (nennt es als Erstes auf die Interviewer-Frage „What keeps you up at night?"), Enablement-Director (Ramp-KPI). Der Schaden ist beziffert (nur 4 Prospects/Std., 20 statt 50 Calls, doppelte Zahlen laut Chen und Jenkins). Damit ist es als T&M-Projekt gut argumentierbar. | ✔ Klarer Budget-Owner (Sales Ops). Die Kosten stehen schon in seiner eigenen Rechnung: 80k-$-Gehälter, rund 2 Std. pro Rep und Tag, bestehende ZoomInfo/Clearbit-Ausgaben, die er für zu teuer hält. Der Agent ersetzt Ausgaben, die schon existieren. |
| **Business Model T&M, Prozess aus `company.md`:** Identify bottlenecks → Identify skill gaps → Build the agents | ✔ Der Engpass ist von den Befragten selbst benannt („That's the bottleneck", Thorne) und der Skill-Gap klar abgegrenzt. Das passt genau zum Beratungsprozess. | ✔ Ebenso: Engpass („Data integrity. 100%", Kim), Skill-Gap (manueller Abgleich), Agent (Abgleich LinkedIn ↔ CRM). |
| **„The Bridge: Pattern Recognition"**, wiederkehrende Muster als Produkt-Keim | ✔ Rollenübergreifend (SDR bis VP) und unabhängig vom Produkt des Kunden. Gebraucht wird es in jeder B2B-Sales-Organisation, die auf öffentlichen Signalen prospektiert. Die Signal-Typen sind generisch (Funding, Leadership Change, Hiring, Themen). Siehe O'Neils Checkliste: „Recent funding news—Series B or C preferably. 2. New hiring in engineering or ops. 3. Recent leadership changes at the VP level." | ✔ Jede Firma mit CRM und LinkedIn-basiertem Vertrieb hat dasselbe Problem. Kim: „the source of truth isn't the CRM anymore". Die Schnittstellen sind standardisiert (Salesforce o. Ä.), also ist das gut für ein nicht-kundenspezifisches Agent-Produkt geeignet. |

**Einschränkung beim Pattern-Kriterium:** Alle zehn Interviews stammen aus *einer* Kunden-Organisation. Die Wiederholung über zehn Rollen zeigt ein starkes internes Muster, aber noch kein Muster über mehrere Kunden. Laut Strategie ist genau das die Aufgabe der zwei Pattern-Leute: Sie prüfen bei weiteren Kunden aus anderen Branchen, ob Bedürfnis 1 und 2 dort genauso auftreten. Bis dahin gilt: **Jetzt als T&M-Projekt für diesen Kunden bauen (Runway), so modular, dass die Signal- und Abgleichs-Bausteine wiederverwendbar sind (Bridge).**

---

## 5. Bewusst ausgeschlossen

- **Abstimmung Marketing ↔ Sales und Lead-Definition** (Blunt, Ross): Das ist ein echter Konflikt, aber eine Organisationsfrage und kein ersetzbarer Mitarbeiter-Skill. Er fällt laut Strategie-Vision-Filter heraus. Er entschärft sich teilweise, wenn Bedürfnis 1 gelöst ist, denn dann gibt es Kontext für alle Leads statt für 5 von 100.
- **Mehr Tool-Lizenzen** (Jenkins, Chen): Das ist Einkauf und keine Agent-Arbeit. Kein Umsatz für uns.
- **LinkedIn-Posting („thought leadership")** (Baker): Einzelnennung, kein Kosten-Beleg.
- **Onboarding-Playbook** (Green, O'Neil): Es geht in Bedürfnis 1 auf. O'Neil will Research aus der Einarbeitung *herausnehmen* und nicht besser lehren.
- **Transparenz und Attribution** (Ross, Thorne): Sie entsteht als Nebenprodukt, wenn A und B Signale und Datenquellen protokollieren. Kein eigenes Projekt.

---

## 6. Loop-Protokoll: Wie diese Synthese entstanden ist

Ziel des Loops: *Synthese aller zehn Einzelanalysen, bis sie auf höchstens zwei Kundenbedürfnisse reduziert ist, die über Zitate und Ableitungen eindeutig herausstechen und rückverfolgbar sind und sich nachweisbar an `context/strategy.md` orientieren.*

Vorlauf (vorheriger Loop): 10 Subagenten haben je ein Interview aus `input/` nach `scripts/interview-analysis.md` (Schritt 1) analysiert. Alle 10 Dateien lagen vor, jede mit den 6 Pflichtabschnitten. Eine zusätzlich gestartete Skript-Synthese (Schritt 2) wurde auf Wunsch abgebrochen, bevor eine Datei entstand.

| Durchgang | Was gemacht wurde | Ergebnis | Abbruchkriterium erfüllt? |
|---|---|---|---|
| **1: Bestandsaufnahme** | `strategy.md`, `company.md` und alle 10 Einzelanalysen vollständig gelesen, Abschnitte 3–6 (Probleme, Dringlichkeit, Bedürfnisse, Zitate) ausgewertet | Alle „Underlying Needs" aller 10 Personen (5–8 pro Person) als Rohmaterial erfasst | Nein. Noch keine Verdichtung. |
| **2: Clustern** | Ähnliche Bedürfnisse über Personen hinweg zusammengelegt, nach dem *Kern* gruppiert und nicht nach Wortlaut (z. B. Greens „LinkedIn-Scraper" und Thornes „Dossier" → beides „Signale fertig aufbereitet") | 8 Kandidaten A–H | Nein. 8 > 2. |
| **3: Filtern und reduzieren** | Jeder Kandidat bewertet nach Häufigkeit (n/10), belegter Zahl und den drei Strategie-Kriterien S1 Vision-Filter, S2 Revenue/Runway, S3 Pattern/Produkt (Tabelle Abschnitt 1) | A (9/10) und B (5/10) bestehen alle Prüfungen. C, D, F, G scheitern an S1 (kein ersetzbarer Skill). E geht in A auf. H ist eine Folge von A/B und kein eigenes Bedürfnis. | Teilweise. Genau 2 übrig. Offene Frage: Sind A und B in Wahrheit eins? |
| **3b: Zusammenlegen prüfen** | Getestet, ob A und B zu einem Bedürfnis verschmelzen sollten | Nein: verschiedene Skills (Research-Analyst vs. Data Clerk), verschiedene Käufer (VP Sales/Enablement vs. Sales Ops). B ist die Datengrundlage für A. | Ja, für die Reduktion: ≤ 2 Bedürfnisse. |
| **4: Zitat-Spur schreiben** | Für jedes Bedürfnis eine Tabelle Person → wörtliches Zitat → Ableitung → Quelldatei/Abschnitt, dazu „Gesagt vs. gebraucht" und ein Strategie-Nachweis pro Kriterium | Entwurf dieser Datei | Noch offen: Sind die Zitate wirklich wörtlich? |
| **5a: Zitate prüfen, erster Versuch** | Shell-Skript (sed + grep) gleicht Zitat-Fragmente mit `input/*.md` ab | 60 von 60 als „fehlt" gemeldet. Ursache war ein Fehler im Prüfskript (Unicode-Anführungszeichen mit sed), nicht in den Zitaten. **Ergebnis verworfen.** | Nein. Prüfung ungültig. |
| **5b: Zitate prüfen, Python** | Dieselben 60 Fragmente mit Python geprüft, typografische Anführungszeichen normalisiert | **57 OK, 3 Abweichungen:** (1) Petit „'Head of Global Synergy'": Im Original steht es in doppelten Anführungszeichen. (2) Petit „reading between the lines": Original „read between the lines". (3) O'Neils Checkliste war als Zitat formatiert, ist aber eine Umschreibung. Außerdem ein stehengebliebener Platzhalter „4 statt X". | Nein. Korrektur nötig. |
| **5c: Korrigieren** | Alle 3 Zitate durch den Originalwortlaut ersetzt, Platzhalter durch „nur 4 Prospects/Std." ersetzt | Datei korrigiert | Erneute Prüfung nötig. |
| **6: Gesamtprüfung aller Anführungszeichen** | Jede Stelle in Anführungszeichen automatisch gegen die Interviews und gegen `strategy.md`/`company.md` geprüft. Satzzeichen-Stil (', ", —) wird dabei ignoriert. | 58 Interview-Zitate und 5 Strategie-Zitate OK. 5 Treffer waren deutsche Begriffe (keine Zitate). **6 weitere Abweichungen:** Groß/Klein bei „Half the emails bounce" und „Droplets"; „what keeps you up at night" ist die Frage des Interviewers und nicht Ross' Aussage; der `company.md`-Prozess war verkürzt als Zitat formatiert; „Thought Leadership" ist im Original klein geschrieben. | Nein. Korrektur nötig. |
| **6b: Korrigieren** | Alle 6 Stellen an den Originalwortlaut angepasst bzw. als Umschreibung gekennzeichnet. Die Interviewer-Frage ist jetzt als solche benannt. | Datei korrigiert | Erneute Prüfung nötig. |
| **7: Abschlussprüfung** | Prüfung aus Durchgang 6 erneut über die fertige Datei (Abschnitte 1–5) | **62 Interview-Zitate und 5 Strategie-Zitate wörtlich belegt, 0 Abweichungen** (11 Treffer waren deutsche Begriffe, keine Zitate) | **Ja. Loop beendet.** |

**Kriterien zum Abbruch des Loops:**

1. Höchstens zwei Bedürfnisse → ✔ (Bedürfnis 1 und 2)
2. Herausstechend erkennbar → ✔ (Abschnitt 1: Nur A und B bestehen Häufigkeit, Zahlen-Beleg und alle drei Strategie-Kriterien)
3. Rückverfolgbar über Zitate und Ableitungen → ✔ (Abschnitte 2.1/3.1: jede Zeile mit Person, wörtlichem Zitat, Ableitung, Quelldatei und Abschnitt. Zitate maschinell gegen `input/` geprüft, Durchgang 7)
4. Nachweisbar an der Strategie orientiert → ✔ (Abschnitt 4: jedes Bedürfnis gegen jedes Strategie-Kriterium, mit einer Einschränkung beim Pattern-Kriterium, weil alle Interviews von einem Kunden stammen)
