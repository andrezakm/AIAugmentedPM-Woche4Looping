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

