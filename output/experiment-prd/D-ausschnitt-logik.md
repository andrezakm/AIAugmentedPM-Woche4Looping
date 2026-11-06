## Lösung

**Ein Agent, der pro Prospect ein Dossier erzeugt und am CRM-Datensatz ablegt. Das Dossier ist in unter zwei Minuten lesbar und besteht aus vier Teilen:**

1. **Rollen-Check:** `bestätigt`, `gewechselt` oder `unklar`, mit Quelle. Bei `gewechselt`: die neue Firma der Person und, falls gefunden, ein Nachfolger-Kandidat in der alten Firma. Das ersetzt Jenkins' Handarbeit: "I have to go hunt for who the new person is."
2. **Höchstens drei Anlässe** aus festen Kategorien: Finanzierung, Neueinstellungen, Führungswechsel auf VP-Ebene (O'Neils Checkliste), neue Rolle der Person (Chen sucht Leute unter 6 Monaten im Amt) und Themen-Beiträge (Green: "Show me everyone who posted about Cloud Migration in the last week."). Jeder Anlass hat Datum, einen Satz Inhalt und einen Quell-Link.
3. **Ein Vorschlag für den Gesprächsaufhänger**, der sich auf mindestens einen der Anlässe bezieht. Er ist ein Vorschlag und keine fertige Nachricht.
4. **Kopfzeile:** Erstellzeit, geprüfte Quellen, Warnhinweise.

**Auslöser:** Einzeln auf Knopfdruck am Prospect, oder als Stapel für alle Prospects, die einem Vertriebler für den nächsten Arbeitstag zugeordnet sind (Erkennung: R17). Der Stapel ersetzt Chens Abendschicht.

**Wo es landet:** Im CRM des Kunden, laut Jenkins Salesforce. Jedes Dossier ist ein eigener Dossier-Datensatz, verknüpft mit dem Kontakt. Auf der Kontaktseite zeigt eine Dossier-Komponente das neueste Dossier. Sie trägt die Knöpfe *Dossier erzeugen*, *Neu erzeugen* und je Anlass *falsch*, zeigt Meldungen (R1) und protokolliert, wer das Dossier wann öffnet (R15). Der Agent ändert keine bestehenden Kontaktfelder. Alles, was er schreibt (Dossier, Rollen-Hinweis, Null-Fall-Markierung), steht im Dossier-Datensatz. Damit bleibt das CRM der Ort des Ergebnisses, und das Dossier verschwindet nicht in Tabs.

**Quellen:** Nur Quellen auf einer Freigabeliste je Kunde, jede über einen eigenen austauschbaren Adapter: Firmenwebseiten, Pressemitteilungen und Nachrichten, Finanzierungsdatenbanken wie Crunchbase (von Ross, Kim und O'Neil genannt) und LinkedIn, sobald ein zulässiger Zugriffsweg geklärt ist (*Offene Punkte*, Nr. 1).

**Ausbaustufen:** Stufe 1 ist das Prospect-Dossier (dieser PRD). Stufe 2 ist die Account-Karte für Großkunden (Petit) und kommt erst, wenn Stufe 1 trägt (siehe *Nicht-Ziele*).

### Alternativen

Alle drei sind Lösungsalternativen für dasselbe Problem.

| Alternative | Was sie wäre | Warum nicht |
|---|---|---|
| **L-A: Signal-Feed ohne Synthese** | Ein Agent sammelt alle Rohsignale je Prospect und zeigt sie als Liste, ohne Auswahl und ohne Aufhänger. Billiger zu bauen. | Das löst das falsche Problem. Es fehlen nicht die Daten, es fehlt die Auswahl: "The problem isn't that the data is missing" (O'Neil). Ein längerer Feed verstärkt das Rauschen, das Thorne als Engpass benennt. |
| **L-B: Vollautomatische Ansprache** | Der Agent schreibt und versendet die personalisierte E-Mail selbst. Maximal skalierbar. | Die Erfahrenen wollen die Deutung behalten ("You have to read between the lines", Petit), und Green spürt schon heute, wenn ein Aufhänger nicht echt ist: "It feels a bit fake, honestly." Automatischer Versand gefährdet genau die Antwortquote, die Kontext erst bringt. |
| **L-C: Vorhandene Anreicherungs-Tools ausbauen** | Mehr ZoomInfo-Lizenzen oder Sales Navigator für alle, plus Schulung. | Das ist Einkauf und keine Agent-Arbeit, also nach S1 nicht unser Auftrag. Diese Tools liefern Rohdaten, und die Leute recherchieren trotzdem von Hand. Der Stack-Verantwortliche hält sie schon heute für unzuverlässig und zu teuer: "they break, or they’re too expensive to run on every single contact record". |

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

Messung in der Pilotgruppe gegen eine Vergleichsgruppe ohne Dossier (Größe: A4). Ausgangswerte aus *Woche 1* misst die Vergleichsgruppe, die nie ein Dossier hat; Z1 misst zusätzlich die Pilotgruppe in der Woche vor Pilotstart. Zielwerte außer Z1 legt der Kunde in Phase 0 fest.

| # | Ziel | Kennzahl | Ausgangswert | Zielwert | Messzeitpunkt |
|---|---|---|---|---|---|
| Z1 | Recherche pro Prospect verkürzen | Minuten vom Aufruf des Prospects bis zum ersten Kontaktversuch (Zeitstempel im CRM, *Offene Punkte* Nr. 5) | 15 bis 40 Min. laut Interviews; genau: `[Platzhalter: messen in Woche 1]` (Vergleichsgruppe) und vor Pilotstart (Pilotgruppe) | unter 2 Min. (O'Neils eigene Marke) | vor Pilotstart, Woche 1 und Ende des Pilots (A4) |
| Z2 | Mehr Kontaktversuche | Calls pro SDR und Tag | etwa 20 bei Tagesziel 50 (Jenkins); genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Ende des Pilots (A4) |
| Z3 | Mehr Leads mit Kontext | Anteil bearbeiteter Leads, die vor dem Erstkontakt ein Dossier haben | 5 von 100 (Blunt) | `[Platzhalter]` | Ende des Pilots (A4) |
| Z4 | Weniger tote Kontakte im Gespräch | Anteil Kontaktversuche, bei denen die Person nicht mehr in der Rolle ist | etwa 40 % (Jenkins); genau: `[Platzhalter: messen in Woche 1]` | `[Platzhalter]` | Ende des Pilots (A4) |
| Z5 | Nutzung | Anteil erzeugter Dossiers, die vor dem Kontaktversuch geöffnet werden | 0 (Funktion existiert nicht) | `[Platzhalter]` | wöchentlich im Pilot, Bericht am Ende (A4) |
| Z6 | Mehr Pipeline | Gebuchte Meetings und neue Opportunities pro SDR, Pilot- gegen Vergleichsgruppe | `[Platzhalter: messen in Woche 1]` (Vergleichsgruppe) | `[Platzhalter]` | Meetings: Ende des Pilots; Opportunities: Nachmessung (A4) |

**Guardrails (dürfen nicht schlechter werden):**

| # | Guardrail | Kennzahl | Ausgangswert | Messzeitpunkt |
|---|---|---|---|---|
| G1 | Antwortquote hält | Antworten oder Termine pro Kontaktversuch, Pilot- gegen Vergleichsgruppe | `[Platzhalter: messen in Woche 1]` | Ende des Pilots (A4) |
| G2 | Keine falschen Anlässe | Anteil Anlässe, die Nutzer als falsch markieren (Regel R14), und Anteil Anlässe ohne Quelle (muss null sein, Regel R7); Untergrenze: Mindest-Trefferquote `[Platzhalter]` aus Phase 0 | 0 (Funktion existiert nicht) | wöchentlich im Pilot |

G1 ist die wichtigste Leitplanke: Steigt das Volumen und fällt die Antwortquote, haben wir nur Druck automatisiert und keinen Kontext. Z6 ist das Ziel, für das der Kunde zahlt; Z1 und Z2 erklären, woher die Wirkung kommt.

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
| **Automatischer Versand** von E-Mails oder Nachrichten | Gefährdet Antwortquote und Vertrauen (Alternative L-B). | Nie in diesem Auftrag |
| **Account-Karte** für Großkunden (wer berichtet an wen, wer ist Blocker) | Deutlich schwieriger, braucht stabile Stufe 1. Petit beschreibt Tage Arbeit, das ist ein eigener Umfang. | Phase 2, nach dem Pilot |
| **Listenbau aus Anlässen** (*zeig mir alle neuen CTOs bei Series-B-Firmen*, wie Chen und Green es wollen) | Ist Prospect-Suche, nicht Prospect-Vorbereitung. Nutzt dieselben Bausteine, ist aber ein anderer Ablauf. | Phase 2 |
| **Einigung Marketing und Sales** auf einen guten Lead | Organisationsfrage, kein ersetzbarer Skill (S1). | Anderer Auftrag (kein Agent-Projekt) |
| **Lizenzbeschaffung** (ZoomInfo, Sales Navigator) | Einkauf, keine Agent-Arbeit (Alternative L-C). | Nie |
| **Produkt für viele Kunden** | Strategie: wir bauen kundenspezifisch. | Pattern-Team entscheidet nach Übergabe (N3) |

---

## Logik

Jede Regel ist als Testfall formuliert: Eingabe → erwartetes Verhalten. Startwerte mit Verweis auf A-Nummern sind Annahmen und konfigurierbar.

**Datenmodell Dossier-Datensatz** (eigenes Objekt, verknüpft mit dem Kontakt): `prospect_id`, `erstellt_am`, `ausloeser` (`einzeln` | `stapel`), `status` (`erzeugt` | `Eingabe unvollständig`), `rollen_status` (`bestätigt` | `gewechselt` | `unklar`), `rollen_quelle`, `rollen_hinweis` (Text, gesetzt bei `gewechselt`), `neue_firma` (optional), `nachfolger_kandidat` (optional, mit Quelle), `anlaesse[]` (je `kategorie`, `datum`, `inhalt`, `quell_url`, `belegauszug`, `falsch_markiert[]` mit `nutzer` und `zeit`), `null_fall` (ja/nein), `aufhaenger` (optional), `gepruefte_quellen[]`, `warnhinweise[]`, `geoeffnet[]` (je `nutzer`, `zeit`).

| Regel | Was gilt | Testfall (Eingabe → erwartet) |
|---|---|---|
| **R1 Pflichtfelder** | Ohne Name und Firma wird kein Dossier erzeugt. | Prospect ohne Firma → Datensatz mit `status` = `Eingabe unvollständig`, kein Dossier-Inhalt, Meldung in der Dossier-Komponente; im Stapel läuft der Rest weiter |
| **R2 Rollen-Check zuerst** | Vor allen Anlässen sucht der Agent die aktuelle Firma der Person in den freigegebenen Quellen. Prüfreihenfolge, die erste zutreffende Zeile gilt: (1) Keine Quelle findet die Person → `unklar`. (2) Die Quellen, die sie finden, nennen verschiedene aktuelle Firmen → `unklar`. (3) Alle nennen die Firma aus dem CRM → `bestätigt`. (4) Alle nennen dieselbe andere Firma → `gewechselt`. | CRM: X; Quelle: aktuell bei Y → `gewechselt`, `neue_firma` = Y. Quelle 1: X, Quelle 2: Y → `unklar` |
| **R3 Bei Wechsel** | Für die alte Firma werden keine personenbezogenen Anlässe erzeugt. Der Agent sucht in der alten Firma eine Person mit gleichem Titel nach Normalisierung (Kleinschreibung, Leerzeichen bereinigt) und trägt sie als `nachfolger_kandidat` mit Quelle ein. Der Wechsel selbst wird als Anlass `neue Rolle` für die neue Firma geführt. | Person wechselte von X zu Y; bei X hat jemand denselben Titel → Dossier zeigt Y, Nachfolger-Kandidat bei X mit Link, keine X-Anlässe zur Person |
| **R4 Bei unklar** | Das Dossier wird erzeugt, `warnhinweise` enthält *Rolle nicht bestätigt*. | Keine Quelle findet die Person → Dossier mit Warnhinweis oben |
| **R5 Kategorien** | Erlaubt sind nur: `Finanzierung`, `Neueinstellungen` (Bereiche je Kunde konfigurierbar, Start: Engineering und Ops laut O'Neil), `Führungswechsel` (VP-Ebene), `neue Rolle` der Person, `Thema` (Themenliste je Kunde). | Fund passt in keine Kategorie (z. B. Urlaubsfoto) → wird verworfen |
| **R6 Zeitfenster** | `Finanzierung`, `Neueinstellungen`, `Führungswechsel`: nicht älter als A7. `neue Rolle`: Rollenbeginn vor weniger als 6 Monaten (Chen). `Thema`: Beitrag aus den letzten 7 Tagen (Green: "in the last week"). | Finanzierungsmeldung älter als A7 → verworfen |
| **R7 Quellenpflicht** | Jeder Anlass braucht `quell_url`, `datum` und einen gespeicherten `belegauszug` aus der Quelle. Fehlt eines davon, wird er verworfen. `inhalt` darf nur aussagen, was im Belegauszug steht. | Anlass ohne Datum → nicht im Dossier |
| **R8 Auswahl** | Höchstens drei Anlässe. Reihenfolge nach Kategorie-Priorität (Start: Finanzierung, Neueinstellungen, Führungswechsel, neue Rolle, Thema; je Kunde änderbar), innerhalb einer Kategorie der neueste zuerst. | Fünf gültige Anlässe → die drei nach Priorität, Rest verworfen |
| **R9 Null-Fall** | Kein gültiger Anlass → Dossier zeigt *Kein aktueller Anlass gefunden*, kein Aufhänger, `null_fall` = ja im Dossier-Datensatz (nicht am Kontakt). Der Agent erfindet keinen Ersatz. | Keine Funde → Dossier ohne Aufhänger, `null_fall` = ja, Kontaktfelder unverändert |
| **R10 Aufhänger** | Nur wenn mindestens ein Anlass vorhanden ist. Er nennt mindestens einen Anlass ausdrücklich. Es gibt keine Versandfunktion. | Ein Anlass `Finanzierung` → Aufhänger bezieht sich auf die Finanzierung |
| **R11 Länge** | Das ganze Dossier hat höchstens A9 Wörter, damit es in unter zwei Minuten lesbar ist. | Entwurf zu lang → Inhalte kürzen, nie Quellen entfernen |
| **R12 Ausgabe** | Jedes Dossier ist ein neuer Dossier-Datensatz am Kontakt, angezeigt in der Dossier-Komponente. Bestehende Kontaktfelder ändert der Agent nie. Bei `gewechselt` setzt er `rollen_hinweis` im Dossier-Datensatz; die Komponente zeigt ihn als Banner oben. Ein neues Dossier mit anderem Status ersetzt den Hinweis in der Anzeige. | Status `gewechselt` → neuer Datensatz mit `rollen_hinweis`, Feld *Firma* am Kontakt unverändert (Feld-Diff leer) |
| **R13 Gültigkeit** | Ein Dossier gilt A8. Fragt jemand innerhalb dieser Zeit erneut an, zeigt die Komponente das gespeicherte Dossier mit Erstelldatum. Der Knopf *Neu erzeugen* erzwingt einen neuen Lauf. | Zweite Anfrage am selben Tag → gespeichertes Dossier, kein Quellenaufruf |
| **R14 Rückmeldung** | Nutzer können in der Komponente jeden Anlass als *falsch* markieren. Gespeichert in `falsch_markiert[]`, je Nutzer und Anlass einmal, gezählt für G2. | Klick auf *falsch* an Anlass 2 → Eintrag mit Nutzer und Zeit, G2 +1; zweiter Klick desselben Nutzers → kein weiterer Zähler |
| **R15 Protokoll** | Jede Erzeugung speichert Zeit, Nutzer, Auslöser und geprüfte Quellen. Jedes Öffnen der Komponente mit sichtbarem Dossier schreibt einen Eintrag in `geoeffnet[]`. | Dossier geöffnet → Eintrag mit Nutzer und Zeitstempel (für Z1, Z5) |
| **R16 Quellen-Freigabe** | Nur Quellen-Adapter auf der Freigabeliste des Kunden laufen. Das Dossier listet in `gepruefte_quellen`, was geprüft wurde. Ein freigegebener, aber nicht erreichbarer Adapter wird wie gesperrt behandelt, mit Warnhinweis. Ohne LinkedIn liefert das Dossier die Firmen-Anlässe (`Finanzierung`, `Neueinstellungen`, `Führungswechsel`); findet keine Quelle die Person, gilt R2 (1) und R4. | LinkedIn-Adapter gesperrt → kein LinkedIn-Aufruf, Firmen-Anlässe aus den übrigen Quellen, Kopfzeile *LinkedIn nicht geprüft*, bei fehlendem Personentreffer `unklar` mit Warnhinweis |
| **R17 Laufzeit und Stapel** | Einzel-Dossier fertig innerhalb von A10. Der Stapel nimmt alle Prospects mit offener Aufgabe des Nutzers, fällig am nächsten Arbeitstag. Er startet am Vorabend und ist vor Arbeitsbeginn fertig (Zeiten je Nutzer, Start: A13). Noch gültige Dossiers (R13) werden wiederverwendet. Was bis Arbeitsbeginn nicht fertig ist, läuft weiter; das Protokoll meldet die Verspätung. | Drei offene Aufgaben fällig morgen → drei Dossiers vor Arbeitsbeginn; Aufgabe fällig übermorgen → kein Dossier |

---

