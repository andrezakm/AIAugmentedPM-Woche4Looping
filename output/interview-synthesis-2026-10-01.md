# Interview-Synthese: Lead-Generierung und Prospect-Recherche

**Basis:** 10 Einzelanalysen (Interviews vom 12.–23.10.2025)
**Erstellt:** 2026-10-01
**Quellen:** `output/interview-individual-*.md`

---

## 1. Stimmung in der Gruppe

| Interviewte Person | Rolle | Dominante Stimmung |
|---|---|---|
| Sarah Jenkins | Sales Development Rep | Erschöpft und überdreht zum Quartalsende, Humor als Ventil; misst sich an einer Call-KPI, die sie strukturell nicht erreichen kann |
| Mike Ross | Sales Director | Ungeduldig und misstrauisch gegenüber dem Lead-Gen-Team („I don't know what they do all day"), räumt beim Zusehen widerwillig ein, dass die Arbeit mühsam ist |
| Jessica Chen | Account Executive (Platz 1) | Stolz auf ihre Leistung, darunter verdeckte Erschöpfung und leise Verbitterung; ihr Erfolg hängt an einer unbezahlten Nachtschicht |
| Tom Baker | Senior Sales Rep | Fremd im eigenen Beruf, gekränkter Stolz, Scham („I looked like a dinosaur"); passt sich widerwillig an |
| Emily Blunt | Marketing Manager | Sarkastische Empörung, weil Sales ihre Leads ignoriert; am Ende kippt der Ärger in ein Verlustgefühl („heartbreaking") |
| David Kim | Sales Operations Manager | Zynisch erschöpft (API-Ausfall um 3 Uhr nachts), empört über ein System, das „backwards" gebaut ist |
| Rachel Green | Junior SDR | Überfordert und voller Selbstzweifel; sucht den Fehler bei sich und fühlt sich als „professional lurker" |
| Marcus Thorne | VP of Sales | Gereizte Ungeduld unter Board-Druck; hat außer „Anschreien und Hoffen" keinen Hebel |
| Sam Petit | Enterprise Account Executive | Gut gelaunt und engagiert, aber in seinem professionellen Selbstbild gekränkt („a waste of my experience") |
| Linda O'Neil | Director of Sales Enablement | Müde, wohlwollend-zynisch; erlebt mit jeder Kohorte denselben Ernüchterungszyklus, zeigt aber Hoffnung in der Lösungsvision |

**Emotionales Klima.** Die Organisation ist chronisch erschöpft, nicht akut in der Krise. Fast alle verpacken ihren Frust in Humor und Bilder („zombie data", „graveyard", „rabbit hole", „conspiracy wall"). Das ist Bewältigung, kein Zeichen von Leichtigkeit. Durch alle Ebenen zieht sich ein Gefühl von **Rollenentfremdung**: Sieben von zehn Personen beschreiben, dass Verkäufer:innen als etwas anderes arbeiten, als wofür sie eingestellt wurden. Sie nennen sich „private investigator or a stalker" (Jenkins), „data clerk" (Baker), „professional lurker" (Green), „copy-paste machine" (Kim), „high-priced data miners" (O'Neil). Chen und Petit sagen „overqualified" und „a waste of my experience".

**Muster nach Ebenen.** Die Ebenen deuten dasselbe Problem unterschiedlich:
- **Führung (Ross, Thorne)** sieht vor allem fehlenden Output und deutet das als Haltungsproblem: „paralysis by analysis", „I just want them on the phones". Beide bezeichnen die Arbeit ihrer Teams als „black box". Beide benennen aber auch selbst, dass der eigentliche Engpass die manuelle Recherche ist. Ihre Diagnose und ihre Beobachtung widersprechen sich.
- **Front-Line (Jenkins, Green, Baker, Chen, Petit)** erlebt das Problem als Zeitverlust und Identitätsverlust. Recherche wird nicht verweigert, sondern als notwendig akzeptiert („You kinda have to", „I have to do it to win").
- **System-Rollen (Kim, O'Neil)** diagnostizieren am klarsten strukturell: Die Daten sind vorhanden, aber niemand bereitet sie auf. Kim: „It's all public info! It's right there!" O'Neil: „can you find it in under two minutes?"

**Ausreißer.**
- **Sam Petit** ist als Einziger gut gelaunt. Sein Problem ist eine Enterprise-Variante: Er sucht nicht einen Kontakt, sondern die informelle Machtstruktur eines Fortune-500-Accounts.
- **Emily Blunt** sitzt auf der anderen Seite des Konflikts. Sie gibt Sales die Schuld, bestätigt aber im selben Interview deren Logik: „conversion is higher if you know the context, I admit that—but it doesn't scale."
- **Jessica Chen** ist der lebende Beweis für die These: Die Top-Performerin ist die Person, die am meisten recherchiert. Ihr Erfolg ist aber privat finanziert (Sales Navigator aus eigener Tasche), nachts erarbeitet und nicht übertragbar.

---

## 2. Hauptprobleme (über alle Interviews)

Gerankt nach Häufigkeit und Schmerztiefe.

### P1 — Manuelle, fragmentierte Prospect-Recherche frisst die Verkaufszeit
**Genannt von: 10 von 10 · Schmerz: sehr hoch**

Vor jedem Kontakt wird von Hand über viele Quellen recherchiert: LinkedIn, Firmenwebsite, News, Crunchbase, Pressemitteilungen, Stellenanzeigen. Die Ergebnisse werden im Kopf zusammengeführt. Jede Person nennt eigene Zahlen, alle in derselben Größenordnung:

| Person | Aufwand |
|---|---|
| Thorne | 15 Min pro Prospect („only 4 prospects an hour. That's a joke.") |
| Ross | 20 Min LinkedIn-Lektüre für eine einzige E-Mail, „five different tabs" |
| Chen | 4 Stunden pro Nacht für 10 Kontakte (≈ 24 Min pro Kontakt) |
| Green | 30 Min für einen einzigen Hook („30 minutes for one email!") |
| O'Neil | ≈ 40 Min bei neuen Reps, oft ohne Ergebnis |
| Jenkins | „half my day" für Verifikation und Recherche |
| Baker | „half the job is just staring at a screen trying to find an angle" |
| Petit | „days, literal days" pro Enterprise-Account; 80 % Recherche, 20 % Strategie |
| Kim | ≈ 2 Std pro Tag pro Rep nur für Feldpflege im CRM |
| Blunt | Kontext-Recherche schaffen SDRs für ≈ 5 statt 100 Leads pro Tag |

**Spanne: 15–40 Minuten pro Prospect, in Summe etwa die Hälfte der Arbeitszeit.** Das ist das einzige Problem, das ausnahmslos alle beschreiben.

### P2 — Die Signale sind da, aber unter Rauschen begraben
**Genannt von: 9 von 10 (alle außer Kim) · Schmerz: hoch**

Fast alle wissen recht genau, *welche* Signale einen Kontakt lohnend machen. Das Problem ist das Finden und Filtern:
- **O'Neil** nennt drei Signale: Funding (Series B/C), Hiring in Engineering/Ops, VP-Wechsel. „The problem isn't that the data is missing."
- **Chen** nutzt ein präzises Raster: Series-B-Funding plus neuer CTO/VP Ops mit weniger als 6 Monaten im Amt („Fresh blood").
- **Green** formuliert die Suche: „Show me everyone who posted about Cloud Migration in the last week."
- **Thorne** nennt Hiring, Funding und Risikosignale und will „just hand them the dossier".
- **Jenkins** scrollt durch ihren Feed, um Jobwechsel zu erwischen („fishing without bait").
- **Baker** braucht einen „angle" und blamierte sich, weil er den AI-Ethics-Artikel eines Prospects nicht kannte.
- **Petit** kämpft mit aufgeblasenen Titeln („Head of Global Synergy") und „fifty tabs".
- **Blunt** sagt, der Tech-Stack-Kontext sei „scattered" und erfordere „a lot of manual correlation".
- **Ross** weiß nicht, welche Signale überhaupt wirken: „I don't know. Maybe?"

Der Engpass ist nicht der Zugang zu Daten, sondern **Filterung und Synthese**.

### P3 — Rollenentfremdung: Verkäufer:innen arbeiten als Rechercheur:innen
**Genannt von: 8 von 10 · Schmerz: hoch (emotional am stärksten)**

Jenkins, Chen, Baker, Green, Petit, O'Neil und Kim beschreiben dasselbe ausdrücklich. Ross deutet es an („writing a biography before they say hello"). Das ist keine Randnotiz. Es ist der emotionale Kern der meisten Interviews und ein Treiber für Burnout und Fluktuation. Green spricht nach zwei Monaten von „exhausting", Chen schläft „four hours a night", und O'Neil nennt es „a terrible use of their talent".

### P4 — Veraltete, falsche Kontakt- und CRM-Daten
**Genannt von: 6 von 10 · Schmerz: hoch**

- **Jenkins:** Etwa 40 % der Kontakte haben die Firma verlassen, die Hälfte der E-Mails kommt zurück („zombie data").
- **Baker:** Laut CRM ist ein Kontakt „at Oracle", tatsächlich ist er vor sechs Monaten gewechselt. „It's always wrong anyway."
- **Kim:** „graveyard of outdated info", „Swiss cheese". Das CRM ist nur noch ein Provisions-Logbuch, die eigentliche Datenbasis ist LinkedIn („90%" laut Traffic-Logs).
- **Chen:** errät E-Mail-Adressen mit drei Chrome-Extensions.
- **Ross:** Leads sind pauschal als „Outbound" erfasst, deshalb ist keine Attribution möglich.
- **Petit:** „We never have the real org chart."

Recherche-Ergebnisse fließen nicht zurück ins System. Jede Person fängt jedes Mal von vorn an.

### P5 — Die Übergabe Marketing → Sales funktioniert nicht
**Genannt von: 5 von 10 · Schmerz: hoch**

- **Blunt:** 90 % der MQLs bleiben unbearbeitet („rotting in the queue"), das Budget verpufft.
- **Jenkins:** Die Marketing-Listen sind „absolute garbage".
- **Chen:** Die Qualität der SDR- und Inbound-Leads „just isn't there"; ohne eigene Recherche würde sie die Quote verfehlen.
- **Green:** Auf die Frage, ob Marketing „a spreadsheet of gold" liefert: „I wish!"
- **Ross:** Die Closer sind „starving for good meetings".

Beide Seiten beschreiben dieselbe Lücke von entgegengesetzten Enden. Marketing liefert Volumen ohne Kontext. Sales kann Kontext nicht in diesem Volumen herstellen und sucht sich deshalb nur wenige Leads aus.

### P6 — Zielkonflikt Tempo gegen Qualität, und die Führung sieht nicht hinein
**Genannt von: 4 von 10 (Ross, Thorne, Blunt, O'Neil) · Schmerz: mittel bis hoch**

Ross: „I want speed, they want quality, and right now we have neither." Thorne: „shotgun coverage with sniper precision. I need both." Der Konflikt existiert nur, weil Qualität heute Handarbeit bedeutet. Die Interviews belegen, dass Kontext wirkt: Greens Sourdough-Mail bekam eine Antwort, Chen ist Platz 1, und Blunt räumt die höhere Conversion ein. Mehr Druck auf Volumen („keep yelling at them to make more calls") ist deshalb der falsche Hebel.

### P7 — Tool-Lücken und brüchige Integrationen
**Genannt von: 3 von 10 (Jenkins, Chen, Kim) · Schmerz: mittel**

Es gibt zu wenige ZoomInfo-Lizenzen („the login is always taken"). Chen zahlt Sales Navigator selbst („the company is too cheap"). Enrichment-Tools „break, or they're too expensive to run on every single contact record". API-Syncs fallen nachts aus. Die vorhandenen Werkzeuge lösen das Problem also nicht, sie verlagern es.

### P8 — Verlängerte Ramp-Zeit neuer Reps
**Genannt von: 2 von 10 (O'Neil, Green) · Schmerz: hoch für die Betroffenen**

Das Onboarding bringt Recherche bei statt Verkaufen. Checklisten sollen gegensteuern, verkürzen den Suchaufwand aber nicht. Green ist nach zwei Monaten erschöpft und deutet ihr Tempo als persönliches Versagen.

### P9 — Enterprise-Account-Mapping
**Genannt von: 1 von 10 (Petit) · Schmerz: hoch, geschäftskritisch**

Hier ist P1 bis P4 am stärksten ausgeprägt: Informelle Machtstrukturen (Influencer, Blocker mit Nähe zum Incumbent) werden tagelang aus LinkedIn-Signalen rekonstruiert und an einem Whiteboard festgehalten. Ein übersehener Blocker „is going to kill the deal".

---

## 3. Dringende Probleme

Nur Probleme mit direkter, messbarer Wirkung heute.

**1. Die Vertriebskapazität ist etwa halbiert (P1, P3).**
Die Front-Line verliert rund die Hälfte ihrer Zeit an Recherche. Jenkins schafft etwa 20 statt der geforderten 50 Calls am Tag. Zwei Personen schätzen unabhängig voneinander, dass sie ohne die Recherche ihre Leistung verdoppeln würden: Jenkins („I could double my quota. Easy.") und Chen („I'd double my numbers"). Kim beziffert die Kosten mit 2 Stunden pro Tag bei einem Gehalt von 80.000 $.
*Was heute verloren geht:* Calls, Meetings und Quote, an jedem Arbeitstag.

**2. Pipeline und Marketing-Budget versickern (P5).**
90 % der MQLs werden nicht bearbeitet (Blunt), die Closer bekommen zu wenige Meetings (Ross). Teure Events, Webinare und Whitepaper erzeugen Leads, die verrotten.
*Was heute verloren geht:* bezahlte Pipeline und der Nachweis, dass sich das Marketing-Budget lohnt.

**3. Die Marktabdeckung wird verfehlt, und das Board sieht es (P1, P6).**
Thorne verfehlt die Ziele für die Territory Coverage deutlich („Not even close. We're scratching the surface.") und kam am Interviewtag aus einem Board-Meeting („the job you're trying to save").
*Was heute verloren geht:* Marktanteile an schnellere Wettbewerber („The competition isn't waiting") und das Vertrauen des Boards in die Vertriebsführung.

**4. Die Top-Performerin trägt ein Klumpenrisiko (P1, P3, P7).**
Chen arbeitet 4 Stunden pro Nacht unbezahlt, schläft wenig und zahlt ihre Tools selbst. Ihr Targeting-Modell existiert nur in ihrem Kopf und ihrer Tabelle.
*Was heute verloren geht:* noch nichts Sichtbares. Fällt sie aus oder geht, verschwindet aber die beste Pipeline der Organisation, und das Wissen geht mit.

**5. Neue Reps brauchen zu lange bis zur Produktivität (P8).**
Eine neue Kohorte startete am Tag des Interviews mit O'Neil. Eine Recherche dauert etwa 40 Minuten statt der angestrebten unter 2 Minuten, also rund Faktor 20. Green ist nach zwei Monaten erschöpft.
*Was heute verloren geht:* Ramp-Zeit bei jeder Kohorte und vermutlich Leute durch frühe Fluktuation.

**6. Unvorbereitete Kundengespräche und Deal-Risiko (P2, P9).**
Baker kannte im Termin den Artikel des Prospects nicht („It was embarrassing. I looked like a dinosaur."). Petit braucht Tage, bevor er einen Fortune-500-Account überhaupt anschreiben kann.
*Was heute verloren geht:* Glaubwürdigkeit beim Kunden, Zeit bis zum ersten Kontakt und, im Enterprise-Geschäft, Deals mit übersehenen Blockern.

---

## 4. Zusammenfassung

**Die eine Grundursache:** Erfolgreicher Vertrieb in dieser Organisation hängt am Kontext zum einzelnen Prospect: Funding, Hiring, Rollenwechsel, aktuelle Themen, Beziehungen. Dieser Kontext ist öffentlich verfügbar und liegt zu etwa 90 % auf LinkedIn. Es gibt aber **kein System, das ihn sammelt, filtert und zum richtigen Zeitpunkt liefert.** Deshalb erledigt jeder Mensch diese Arbeit selbst: von Hand, jedes Mal neu, in 15 bis 40 Minuten pro Prospect. Das Ergebnis fließt nicht zurück ins CRM, also veralten die Daten, und die nächste Person beginnt wieder bei null. Alle anderen Symptome folgen daraus: die verfehlte Call-KPI, die verrottenden MQLs, die verfehlte Coverage, die lange Ramp-Zeit, die Nachtschichten der Top-Performerin und die Entfremdung von der eigenen Rolle.

**Die Führung setzt am falschen Hebel an.** Ross und Thorne sehen „paralysis by analysis" und fordern mehr Wählversuche. Die Interviews zeigen das Gegenteil: Kontext ist der Grund, warum es funktioniert. Die Person, die am meisten recherchiert, ist Platz 1. Der Konflikt zwischen Tempo und Qualität ist nicht naturgegeben. Er entsteht nur, weil Qualität heute Handarbeit ist.

**Der größte Hebel** ist ein Agent, der die Recherche-Schicht übernimmt. Er beobachtet laufend die Quellen und erkennt die wenigen Signale, die zählen: Funding, Hiring, VP- und CTO-Wechsel, Jobwechsel, relevante Posts. Pro Prospect liefert er ein Briefing, das sich in zwei Minuten lesen lässt: verifizierter Kontakt, konkreter Anlass für den Anruf, nachvollziehbare Quellen. Das Ergebnis schreibt er automatisch ins CRM zurück. Damit wäre O'Neils Ziel erreicht („signals on a platter … in under two minutes"), ebenso Thornes („just hand them the dossier"), Greens Suchanfrage und Kims Wunsch nach einem lebenden CRM. Wichtig für die Akzeptanz: Der Agent übernimmt das Sammeln und Filtern, das Urteil bleibt beim Menschen. Petit, Baker und Chen wollen Unterstützung beim Denken, keinen Ersatz dafür. Für NeoEmployee ist das ein Musterbeispiel des eigenen Ansatzes: eine klar umrissene Skill-Lücke, die heute teure Menschen manuell schließen, mit messbarer Wirkung auf Quote, Coverage und Ramp-Zeit.

---

*Hinweis zur Methodik:* Alle Zahlen sind Selbstauskünfte aus kurzen Gesprächen, keine gemessenen Werte. Einige Interviewfragen waren suggestiv. Vor einem Business Case sollten Recherchezeit pro Prospect und Antwortquoten mit gegenüber ohne Kontext gemessen werden.
