# Review C, Runde 2: Entwickler

Rolle: Entwickler, der den Signal-Dossier-Agenten bauen soll. Gelesen wurde nur `output/experiment-prd/C-ausschnitt-logik.md` (Lösung, Ziele, Nicht-Ziele, Logik).

Vorgehen: Für jede Regel L1–L11 und jede harte Regel aus Lösung, Zielen und Nicht-Zielen ein Testfall *Eingabe → erwartetes Verhalten*. Wo das nicht eindeutig geht, steht die offene Frage dabei. Quellen (LinkedIn usw.) werden in allen Tests nachgebildet; die rechtliche Quellenfrage (O1) ist im PRD selbst als offen markiert und blockiert das Bauen des Status-Checks, nicht das Testen.

---

## Testfälle zur Logik

### L1 Auslöser
- T1.1 Kontakt ohne Owner wird Vertriebler A zugewiesen → genau ein Lauf startet.
- T1.2 Kontakt wird von A auf B umgehängt → neuer Lauf, Dossier ersetzt, alte Version im Log.
- T1.3 Kontakt hat Dossier, Vertriebler klickt *Dossier anfordern* → neuer Lauf, altes Dossier ersetzt.
- T1.4 Kontakt wird bearbeitet (z. B. Telefon geändert), keine Zuweisung, kein Klick → kein Lauf.
- T1.5 Es gibt keinen Job, der über alle Kontakte läuft → Code-/Konfig-Prüfung: kein geplanter Batch.
- **Offen:** Was passiert, wenn während eines laufenden Laufs ein zweiter Auslöser kommt (Neuzuweisung während der Klick-Lauf noch läuft)? Abbrechen und neu starten, ignorieren oder in die Warteschlange? Der Knopf ist laut L11 während des Laufs offenbar inaktiv, die Zuweisung aber nicht. Ebenso: Massen-Neuzuweisung (z. B. 2.000 Kontakte bei Gebietswechsel) löst 2.000 Läufe aus; ist das gewollt oder gibt es eine Obergrenze? Ohne Antwort kein eindeutiger Testfall für Nebenläufigkeit.

### L2 Status-Check
- T2.1 CRM *Oracle*, Profil *Oracle Corporation*, Titel gleich → (a) *aktuell*, weiter mit L3.
- T2.2 CRM *VP Sales*, Profil *Vice President Sales* → (a).
- T2.3 CRM *Acme GmbH / Head of Sales*, Profil *ACME / VP Sales* → (b), *Titel* = *VP Sales*, Status *Titel aktualisiert*, Log-Eintrag alt/neu/Quelle/Zeit.
- T2.4 CRM *Oracle*, Profil *Salesforce* → (c), Status *gewechselt*, *Neuer Arbeitgeber laut Quelle* = *Salesforce*, Aufgabe *Kontakt hat gewechselt, prüfen* an Owner, kein Signal-Teil, Arbeitgeber/Account unverändert.
- T2.5 Ein Profil, zwei aktuelle Stellen (*Oracle*, *Beirat XY*), CRM *Oracle* → Stelle Oracle zählt, (a) bzw. (b).
- T2.6 Zwei Profile mit verschiedenen Arbeitgebern → (d), Status *unklar*, *Titel* unverändert, Vermerk *Status unklar, bitte prüfen*, weiter mit L3.
- T2.7 Keine Quelle gefunden → (e), Status *nicht geprüft*, weiter mit L3.
- T2.8 CRM *Acme,  Inc.* (Doppelleerzeichen, Komma), Profil *acme* → (a).
- Kleine Lücke (nicht als offen gezählt, Annahme möglich): Ein Profil, zwei aktuelle Stellen, keine passt zum CRM → (c), aber welcher Arbeitgeber kommt in *Neuer Arbeitgeber laut Quelle*? Annahme für den Test: beide, kommagetrennt.

### L3 Signal-Katalog
- T3.1 Neuer *Chief Revenue Officer* bei der Firma, vor 20 Tagen → Typ 1.
- T3.2 Neuer *Team Lead Sales* → kein Signal.
- T3.3 Prospect hat Rolle vor 2 Monaten angetreten → Typ 2.
- T3.4 Finanzierungsmeldung vor 30 Tagen → Typ 3.
- T3.5 Zwei Stellen in Engineering im Fenster → kein Signal; drei → Typ 4; Schwelle auf 5 konfiguriert, drei Stellen → kein Signal.
- T3.6 Beitrag der Person mit Stichwort *Pipeline* aus Themenliste (Schreibweise *PIPELINE*) → Typ 5. Themenliste leer → nie Typ 5.
- T3.7 Urlaubs-Post, Hobbyfoto → kein Signal.
- **Offen:** Typ 4 ist kein Einzelereignis, sondern eine Zählung. (a) Wie wird eine Stellenanzeige als *Engineering* oder *Operations* eingestuft (Abteilungsfeld der Quelle, Stichworte im Stellentitel, Liste)? (b) Zählen Engineering und Operations zusammen (2 + 1 = 3 → Signal?) oder je Bereich? (c) Welches Datum und welche URL bekommt das Signal, das L4, L5 und L6 verlangen (älteste Anzeige, neueste, alle Links)? Ohne das ist weder die Fenster-Prüfung noch die Sortierung „neueres zuerst" testbar.
- Kleine Lücke (nicht gezählt): Wird der Prospect selbst neuer VP, ist das Typ 1 *und* Typ 2? L5 dedupliziert nur bei gleichem Typ, also erschiene dasselbe Ereignis doppelt. Annahme für den Test: Typ 1 schließt den Prospect aus.

### L4 Aktualität
- T4.1 Bezugsdatum 05.11.2026, Finanzierung 06.10.2026 (30 Tage) → Signal.
- T4.2 Finanzierung 07.08.2026 (genau 90 Tage) → Signal (Grenztag eingeschlossen).
- T4.3 Finanzierung 06.08.2026 (91 Tage) → kein Signal.
- T4.4 Fenster für Typ 3 auf 30 Tage konfiguriert, Finanzierung vor 45 Tagen → kein Signal; Typ 1 vor 45 Tagen weiter Signal.
- T4.5 Rollenstart vor 5 Monaten → Typ 2; vor 7 Monaten → kein Signal.
- Kleine Lücke (nicht gezählt): „6 Monate" als Kalendermonate oder 182/183 Tage? Annahme für den Test: Kalendermonate, Grenztag eingeschlossen (Bezugsdatum 05.11.2026 → Start 05.05.2026 zählt, 04.05.2026 nicht). Signal mit Datum in der Zukunft: Annahme verwerfen.

### L5 Höchstens drei Signale
- T5.1 Dieselbe Finanzierungsrunde (Typ 3, Firma X, 01.10.) aus zwei Quellen → ein Signal, zwei Links.
- T5.2 Fünf Signale Typ 3, 1 (10.10.), 5, 1 (01.09.), 4 → angezeigt Typ 1 (10.10.), Typ 1 (01.09.), Typ 3; Typ 4 und 5 im Log als verworfen.
- T5.3 Zwei Signale → beide angezeigt, keine Verwerfung.
- Kleine Lücke (nicht gezählt): gleiche Runde, zwei Quellen mit um einen Tag abweichendem Datum → nach Regel zwei Signale. Gleicher Typ und gleiches Datum, verschiedene Ereignisse → Reihenfolge unbestimmt; Annahme: stabil nach Fundreihenfolge.

### L6 Kein Signal ohne Beleg
- T6.1 Fund mit URL, ohne Datum → nicht im Dossier, Log *verworfen: ohne Beleg*.
- T6.2 Fund mit Datum, ohne URL → dito.
- T6.3 Fund mit beidem → kann angezeigt werden (vorbehaltlich L4/L5).

### L7 Einstiegsvorschlag
- T7.1 Signal Finanzierungsrunde → genau ein Vorschlag, ≤ 2 Sätze (Satzzählung), Kennzeichnung *Vorschlag*.
- T7.2 Kein Versand-Knopf in der Oberfläche; Netzwerk-/API-Mock zeigt keinen Aufruf an Mail- oder Sequenz-System.
- T7.3 „Enthält keine weiteren Behauptungen" ist bei LLM-Text nicht mechanisch prüfbar → Abnahme per Stichprobe gegen die Quelle (wie G3). Testbar, aber als manuelle/LLM-Judge-Prüfung, nicht als Unit-Test.

### L8 Kein Signal gefunden
- T8.1 Status (a), keine gültigen Signale → Vermerk *kein aktuelles Signal gefunden*, kein Vorschlag.
- T8.2 Status (c) → nur Status *gewechselt*, kein Vermerk.
- T8.3 Status (d) oder (e), keine Signale → Vermerk *Status unklar, bitte prüfen* **und** *kein aktuelles Signal gefunden*.

### L9 Schreiben ins CRM
- T9.1 Lauf fertig → *Signal-Dossier* gefüllt, *Dossier-Stand* = Fertigstellungszeit.
- T9.2 Fall (b) → *Titel* neu; Log enthält alten Wert, neuen Wert, Quelle, Zeitpunkt; auch bei abgeschalteter Feld-Historie.
- T9.3 Snapshot aller Kontaktfelder vor/nach dem Lauf → nur die fünf eigenen Felder und *Titel* verändert; E-Mail, Telefon, Account gleich.
- T9.4 Zweiter Lauf → *Signal-Dossier* neu, vorige Version im Log.

### L10 Protokoll
- T10.1 Lauf mit 4 Funden, 1 verworfen → Log enthält Quellen, 3 gefundene, 1 verworfenen mit Grund, Feldänderungen, Laufzeit.
- T10.2 Nicht bewertet → Bewertung leer.
- T10.3 Bewertung *brauchbar* → *nicht brauchbar* geändert → Z4 zählt *nicht brauchbar*.
- **Offen:** Was passiert mit *Dossier-Bewertung*, wenn ein neuer Lauf das Dossier ersetzt? Wird das Feld auf leer zurückgesetzt (Bewertung gehört zur alten Version, nur im Log), oder bleibt sie stehen und gilt dann scheinbar für das neue Dossier? Das bestimmt, ob Z4 pro Dossier-Version oder pro Kontakt zählt.

### L11 Laufzeit
- T11.1 Lauf gestartet → Anzeige *Dossier in Arbeit*.
- T11.2 Lauf fertig nach 90 s → Dossier sichtbar.
- T11.3 Erster Lauf nach 10 Min. nicht fertig → automatischer zweiter Versuch; zweiter erfolgreich → Dossier sichtbar.
- T11.4 Zweimal Zeitüberschreitung oder Fehler → *Dossier fehlgeschlagen*, Knopf aktiv.
- **Offen:** In welchem Feld stehen *Dossier in Arbeit* und *Dossier fehlgeschlagen*? Die Auswahlliste *Agent-Status* hat diese Werte nicht; schreibt man sie ins Feld *Signal-Dossier*, ist bei einem neuen Lauf das alte, noch brauchbare Dossier während des Laufs weg und nach einem Fehlschlag ganz weg (nur noch im Log). Gewünscht: altes Dossier sichtbar lassen bis das neue fertig ist? Und was steht nach einem Fehlschlag in *Dossier-Stand*? Ohne Antwort kein eindeutiges erwartetes Verhalten für T11.1 und T11.4 bei vorhandenem Dossier.

---

## Testfälle zu harten Regeln aus Lösung, Zielen, Nicht-Zielen

- H1 **Schreibrechte abschließend** (Logik-Vorspann): Integrations-User mit Feld-Berechtigungen nur auf die fünf Felder, *Titel* und Aufgabe-Anlegen; Versuch, Account oder E-Mail zu schreiben → Berechtigungsfehler. Testbar.
- H2 **Kein Versand, keine Kontaktanlage, keine Nachfolger-Suche, keine Prospect-Listen, kein Account-Mapping** (Lösung, Nicht-Ziele): API-Mock über einen Lauf → kein `insert Contact`, kein Mail-/Sequenz-Aufruf; Fall (c) erzeugt nur eine Aufgabe, keinen neuen Kontakt. Testbar.
- H3 **Bewertungsknopf** *brauchbar / nicht brauchbar* (Lösung 4, Z4): Klick → *Dossier-Bewertung* gesetzt und im Log; erneuter Klick → überschrieben. Testbar (Rücksetzen bei neuem Lauf siehe offene Frage L10).
- H4 **G3 Signale ohne Beleg bleibt 0**: durch L6 technisch erzwungen (T6.1/T6.2); die wöchentliche Stichprobe ist ein Prozess, Umfang `[Platzhalter]`. Testbar.
- Hinweis (keine Logikregel, nicht gezählt): Z1 „Zeit vom Öffnen eines Leads bis zum Start des Kontakts" und Z3 brauchen Ereignisse, die der Agent nicht schreibt (Lead geöffnet, Kontakt gestartet). Wer instrumentiert das, und welches CRM-Ereignis gilt als „Start des Kontakts" (Call geloggt, E-Mail gesendet)?

---

## Ergebnis

Regeln geprüft: 15 (L1–L11, H1–H4). Davon mit eindeutigem Testfall: 11. Offen: 4 (L1, L3, L10, L11).

Offene Fragen:
1. **L1:** Verhalten bei einem zweiten Auslöser während eines laufenden Laufs (abbrechen, ignorieren, Warteschlange) und bei Massen-Neuzuweisung (Obergrenze?).
2. **L3 Typ 4:** Wie wird eine Stelle als Engineering/Operations eingestuft, zählen beide Bereiche zusammen, und welches Datum und welche URL trägt das Signal für L4–L6?
3. **L10:** Wird *Dossier-Bewertung* bei einem neuen Lauf zurückgesetzt oder bleibt sie stehen?
4. **L11:** In welchem Feld stehen *in Arbeit* / *fehlgeschlagen*, und bleibt das alte Dossier während eines neuen Laufs und nach Fehlschlag sichtbar?

Kleinere Lücken, per Annahme testbar (nicht gezählt): Arbeitgeber bei mehreren nicht passenden Stellen (L2), Doppelzählung Typ 1/Typ 2 beim Prospect selbst (L3), „6 Monate" als Kalendermonate und Signale mit Zukunftsdatum (L4), Dedup bei abweichendem Datum (L5), Prüfmethode „keine weiteren Behauptungen" (L7).

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 Logik ist baubar | ❌ | Elf von 15 Regeln sind eindeutig testbar, aber vier bleiben offen und die Grenze ist eine. | L1: Nebenläufigkeit und Massen-Neuzuweisung; L3: Einstufung, Zählweise, Datum und URL für Typ 4; L10: Bewertung bei neuem Lauf; L11: Feld für *in Arbeit*/*fehlgeschlagen* und Sichtbarkeit des alten Dossiers. |
