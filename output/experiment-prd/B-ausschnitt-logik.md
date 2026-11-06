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

