# Review B, Runde 1: Entwickler-Sicht auf „Lösung" und „Logik"

Gelesen: nur `output/experiment-prd/B-ausschnitt-logik.md`.
Vorgehen: für jede Regel aus „Logik" und jede harte Regel aus Lösung, Zielen und Nicht-Zielen ein Testfall *Eingabe → erwartetes Verhalten*. Wo das nicht geht: offene Frage.

Vorbemerkung: Die „Logik" ist eine Wirkungskette mit Annahmen (Geschäftslogik), keine Systemlogik. Die baubaren Regeln stehen fast alle in „Lösung". Die Kette liefert drei Bau-Regeln (öffentliche Signale sammeln, filtern, Rolle prüfen) und sechs Prüfregeln (L1–L6).

## Testfälle

### Lösung

| # | Regel | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|---|
| R1 | Rollen-Check: noch im Unternehmen, Rolle, seit wann | Prospect „A. Muster, Firma X", öffentlich als „VP Sales bei X seit 03/2024" auffindbar → Dossier zeigt „aktiv, VP Sales, seit 03/2024" | testbar |
| R2 | Nicht mehr im Unternehmen → Hinweis, Nachfolger falls erkennbar | Prospect hat X verlassen, Nachfolgerin öffentlich benannt → Hinweis „nicht mehr bei X" + Name der Nachfolgerin mit Quelle. Kein Nachfolger auffindbar → Hinweis ohne Nachfolger, kein geratener Name | testbar (Annahme: „erkennbar" = mit Quelle belegbar) |
| R3 | Zwei bis drei Signale aus festen Kategorien (Funding, Hiring, Führungswechsel), gefiltert | Firma X hat Funding-Runde und 5 offene Stellen → 2 Signale. **Aber:** Firma Y hat kein Signal / nur eines / sieben Signale → ? | **offen** |
| R4 | Themen-Signale (z. B. „Cloud Migration in der letzten Woche") | Prospect postet zu Thema T → Signal, wenn T auf der Themenliste steht. Wer pflegt die Themenliste? | **offen** |
| R5 | „Warum jetzt": ein Satz zur Relevanz fürs Angebot | Dossier mit 2 Signalen → genau ein Satz „Warum jetzt", der auf das Angebot des Kunden Bezug nimmt | testbar (Annahme: Angebotsbeschreibung des Kunden liegt als Konfiguration vor) |
| R6 | Gesprächsaufhänger: ein Vorschlag, erster Satz, keine fertige Nachricht | Beliebiges Dossier → genau ein Satz, keine Anrede/Grußformel/Signatur, kein Versand-Button | testbar |
| R7 | Ein Link pro Signal | Dossier mit 3 Signalen → 3 Links, jeder erreichbar (HTTP 200) und belegt das jeweilige Signal | testbar |
| R8 | Zeitstempel pro Dossier | Jedes Dossier → Erstellzeitpunkt sichtbar; Signale mit Datum der Quelle | testbar |
| R9 | Ablage dort, wo der Vertriebler arbeitet; Speicherung im CRM | Dossier erstellt → erscheint im Kanal K und am CRM-Datensatz. K ist ausdrücklich noch offen | **offen** |
| R10 | Jeder bearbeitete Lead bekommt ein Dossier | Lead wird „bearbeitet" → Dossier entsteht. Was löst das aus, was ist die Eingabe? | **offen** |
| R11 | Stufe 2 Account-Karte erst, wenn Stufe 1 trägt | Kein Testfall formulierbar: weder das „trägt"-Kriterium noch der Inhalt der Karte sind definiert | **offen** |
| R12 | Veraltete Kontakte vor dem Anruf markiert, mit Nachfolger wenn erkennbar | Lead mit veraltetem Kontakt im CRM wird bearbeitet → Markierung im Dossier, bevor der Anruf ansteht (hängt an R10) | testbar |

### Logik (Wirkungskette)

| # | Regel | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|---|
| G1 | Agent sammelt **öffentliche** Signale | Quelle hinter Login (LinkedIn-Profil nur eingeloggt sichtbar), Bezahl-Datenbank, Firmen-Website → welche sind zulässig? | **offen** |
| G2 | Dossier in unter 2 Minuten lesbar (auch Z1) | Lesetest mit n Vertrieblern auf 10 Dossiers → Median Lesezeit < 2 Min. | testbar |
| L1 | Signale abrufbar; Spike in Phase 1 | Spike liefert Quellen, Zugriffswege, Rechtslage. Ab wann ist L1 bestanden, ab wann wird gestoppt? | **offen** |
| L2 | Vertrauen und Nutzung; Nutzungsquote im Pilot | Was zählt als „genutzt" (geöffnet? Link geklickt? Aufhänger übernommen?) und welche Quote gilt als Erfolg? | **offen** |
| L3 | Zeit fließt in Gespräche | Recherchezeit und Calls/Tag pro SDR vor und während des Pilots messen → Recherchezeit sinkt, Calls steigen | testbar (Zielwert Z2 noch Platzhalter) |
| L4 / Z5 | Antwort-/Meeting-Quote mindestens halten | Pilotgruppe vs. Vergleichsgruppe → Quote Pilot ≥ Quote Vergleich | testbar (was bei Verletzung passiert, ist nicht festgelegt) |
| L5 | Mehr Meetings → mehr Abschlüsse | PRD sagt selbst: im Projekt nicht messbar | **offen** |
| L6 / N3 | Bausteine wiederverwendbar, modular dokumentiert übergeben | Projektende → pro Signal-Baustein eine Doku beim Pattern-Team | testbar (nur die Übergabe, nicht die Wiederverwendbarkeit) |

### Nicht-Ziele

| # | Regel | Testfall: Eingabe → erwartetes Verhalten | Status |
|---|---|---|---|
| N1 | Rollen-Check nur für Prospects mit Dossier | CRM mit 1.000 Kontakten, 20 bekommen ein Dossier → genau 20 Rollen-Checks, kein Massenabgleich | testbar |
| N2 | Kein automatischer Versand | Agent hat keine Berechtigung/Schnittstelle zum Senden von Mail oder Nachricht; Versuch → nicht möglich | testbar |
| N3 | Keine Lizenzbeschaffung | Darf der Agent vorhandene Lizenzen des Kunden (z. B. Sales Navigator, ZoomInfo) als Quelle nutzen, oder nur frei Zugängliches? Kollidiert mit G1 | **offen** |

Ohne Bau-Regel (kein Testfall nötig): Konflikt Marketing ↔ Sales, kein Produkt, keine Vertriebsstrategie-Beratung. Z2–Z4 sind Messgrößen mit `[Platzhalter]`-Zielwerten, die Messung selbst ist in L3 abgedeckt.

## Offene Fragen

1. **R3 Signale:** Was passiert bei 0 oder 1 Signal (Dossier trotzdem, Hinweis „keine Signale")? Nach welchem Kriterium werden bei mehr als 3 Signalen die besten gewählt (Aktualität, Kategorie-Priorität)? Wie alt darf ein Signal höchstens sein?
2. **R4 Themen-Signale:** Wer legt die Themen fest, pro Kunde, pro Team oder pro Prospect, und wo wird das konfiguriert?
3. **R9 Ablage:** Welcher Kanal, und in welches CRM-Feld/-Objekt wird gespeichert? (Laut PRD bewusst auf Phase 1 vertagt.)
4. **R10 Auslöser und Eingabe:** Was startet ein Dossier (neuer Lead im CRM, Klick des Vertrieblers, Liste)? Welche Eingabe minimal (Name + Firma, LinkedIn-URL, CRM-ID)? Wird ein Dossier aktualisiert, und wann gilt es als veraltet?
5. **R11 Stufe 2:** Woran wird gemessen, dass Stufe 1 „trägt"? Was genau enthält die Account-Karte (Felder, Tiefe)?
6. **G1 öffentlich:** Welche Quellen sind zulässig, insbesondere LinkedIn hinter Login?
7. **L1 Spike:** Was sind Go/No-Go-Kriterien des Spikes?
8. **L2 Nutzung:** Definition von „genutzt" und Erfolgsschwelle der Nutzungsquote.
9. **L5:** Wie und von wem wird der Zusammenhang Meetings → Abschlüsse erhoben, wenn nicht im Projekt?
10. **N3 Lizenzen:** Dürfen vorhandene Lizenzen des Kunden als Datenquelle dienen?

Zusätzlich, nicht als Regel gezählt: Verhalten bei widersprüchlichen Quellen (zwei Rollen gefunden), Sprache des Dossiers, Umgang mit Namensgleichheit (zwei Personen gleichen Namens bei derselben Firma).

## Urteil

23 Regeln, 13 testbar, **10 offen**. Kriterium verlangt höchstens eine offene Regel.

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 Logik ist baubar | ❌ | Inhalt und Format des Dossiers sind testbar, aber Auslöser, Signalauswahl, Quellenzulässigkeit und Ablage sind nicht festgelegt, sodass 10 von 23 Regeln keinen Testfall erlauben. | Auslöser + Eingabe (R10); Verhalten bei 0/1/>3 Signalen, Auswahlkriterium, Zeitfenster (R3); Themenpflege (R4); zulässige Quellen inkl. LinkedIn/Lizenzen (G1, N3); Ablage-Kanal und CRM-Feld (R9); „trägt"-Kriterium und Inhalt Stufe 2 (R11); Go/No-Go des Spikes (L1); Definition und Schwelle der Nutzungsquote (L2); Erhebung L5. |
