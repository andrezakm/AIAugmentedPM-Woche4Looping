# Review C, Runde 1: Entwickler-Sicht auf „Lösung" und „Logik"

Grundlage: nur `output/experiment-prd/C-ausschnitt-logik.md`. Rolle: der Entwickler, der das bauen soll. Für jede Regel ein Testfall *Eingabe → erwartetes Verhalten*; wo das nicht geht, die offene Frage.

## 1. Regeln aus „Logik"

| # | Testfall(e): Eingabe → erwartetes Verhalten | Baubar? | Offene Frage |
|---|---|---|---|
| L1 Auslöser | (a) Kontakt X wird Vertriebler A zugewiesen → genau ein Dossier-Job für X startet. (b) A klickt „Dossier anfordern" an Kontakt Y → Job startet. (c) Kontakt Z ohne Zuweisung, ohne Klick, nächtlicher Batch läuft → kein Job für Z. | ✅ | Nebenfrage: Neuzuweisung an Vertriebler B oder erneuter Klick, wenn schon ein Dossier existiert → neuer Lauf, Überschreiben oder nichts? |
| L2 Status-Check | (a) CRM „Acme / Head of Sales", Profil „Acme / Head of Sales" → weiter mit L3. (b) CRM „Acme / Head of Sales", Profil „Acme / VP Sales" → Titel aktualisiert (L9), weiter mit L3. (c) CRM „Oracle", Profil „Salesforce" → Status *gewechselt*, Arbeitgeber „Salesforce" eingetragen, kein Signal-Teil, Hinweis an Vertriebler. (d) kein Profil gefunden → Dossier mit Vermerk *Status nicht geprüft*, weiter mit L3. | ❌ | **Wann ist „gleich" gleich?** CRM „Oracle", Profil „Oracle Corporation"; CRM „VP Sales", Profil „Vice President of Sales"; zwei Profile mit widersprüchlichen Angaben; Person mit zwei aktuellen Stellen. Ohne Vergleichsregel kann ich (a) vs. (b)/(c) nicht testen, und Fehlalarme schreiben falsche Daten ins CRM (Risiko für G2). Außerdem: In welchem Feld steht *gewechselt*, und über welchen Kanal geht der „Hinweis an den Vertriebler" (CRM-Aufgabe, Notiz, Mail)? Und: Wird bei (c) der Kontakt umgeschrieben (dann sitzt er bei der neuen Firma) oder bleibt er bei der alten? Das „Nachher" spricht von einem angelegten Nachfolger, L2/L9 nicht (siehe H6). |
| L3 Signal-Katalog | Urlaubs-Post → kein Signal. Finanzierungsmeldung → Signal Typ 3. Neuer CRO bei der Firma → Typ 1. Person seit 2 Monaten in der Rolle → Typ 2. Neuer „Team Lead" (unter VP) → kein Typ-1-Signal. | ❌ | **Typ 4:** Was zählt als „Neueinstellungen in Engineering oder Operations"? Eine Stellenanzeige, eine bestätigte Einstellung, ab N Stück? Ohne Schwelle kein Testfall. **Typ 5:** Die „Themenliste des Kunden" existiert im Dokument nicht: Wer liefert sie, wo liegt sie, wie wird „über ein Thema geschrieben" erkannt (Stichwort, semantisch)? Typ 1: Gilt der Führungswechsel bei der Firma des Prospects allgemein oder nur in bestimmten Bereichen? |
| L4 Aktualität | Finanzierung vor 30 Tagen → Signal. Vor 200 Tagen → kein Signal. Typ 2, Rollenstart vor 5 Monaten → Signal; vor 7 Monaten → kein Signal. Typ-3-Fenster per Konfiguration auf 30 Tage gesetzt, Meldung vor 45 Tagen → kein Signal. | ✅ | Klein: Grenze inklusive (Tag 90 zählt?), Bezugsdatum = Zeitpunkt der Dossier-Erstellung (angenommen). |
| L5 Höchstens drei | Fünf gültige Signale Typ 3, 1, 5, 1, 4 → angezeigt: Typ 1 (neuer), Typ 1 (älter), Typ 3; Typ 4 und 5 verworfen und geloggt. | ✅ | Klein: Dubletten (dieselbe Finanzierungsrunde aus zwei Quellen) → ein Signal oder zwei? |
| L6 Kein Signal ohne Beleg | Fund mit Datum, ohne URL → nicht im Dossier, Log *verworfen: ohne Beleg*. Fund mit URL, ohne Datum → ebenso. Fund mit beidem → anzeigbar. | ✅ | „Schließt nicht auf Fakten" ist nicht automatisch prüfbar, nur per Stichprobe (G3). Akzeptabel. |
| L7 Einstiegsvorschlag | Signal Finanzierungsrunde → Vorschlag ≤ 2 Sätze, nennt die Runde, keine weiteren Behauptungen, Label *Vorschlag*, kein Versand-Knopf, kein API-Aufruf an Mail/Sequenz-System. | ✅ | – |
| L8 Kein Signal | Kontakt, alle Funde verworfen → Dossier zeigt *kein aktuelles Signal gefunden*, Vorschlagsfeld leer. | ✅ | Klein: Zeigt ein Dossier im Fall L2(c) *gewechselt* zusätzlich diesen Vermerk oder nicht? |
| L9 Schreiben ins CRM | Titel weicht ab → Titelfeld neu, Historie zeigt alten Wert, Quelle, Zeitpunkt. E-Mail-Feld vorher = nachher. Telefon-Feld vorher = nachher. | ❌ | **„Notiz bzw. eigenes Feld"** ist keine Entscheidung: Ich muss wissen, welches CRM (im Text taucht Salesforce nur im „Vorher" auf), welches Objekt/Feld, und was bei einem zweiten Lauf passiert (überschreiben, anhängen, versionieren). **Widerspruch:** „alle anderen Felder ändert der Agent nicht", aber L2(c) verlangt eine Markierung *gewechselt* und das „Nachher" einen neu angelegten Nachfolger-Kontakt. Welche Schreibrechte hat der Agent genau? Und: Nutzt das CRM eine Feld-Historie, die „Quelle" aufnehmen kann, oder muss der Agent sie selbst ablegen? |
| L10 Protokoll | Dossier erstellt, bewertet *brauchbar* → Log-Eintrag mit Quellen, gefundenen Signalen, verworfenen Signalen mit Grund, Laufzeit, Bewertung. Dossier nicht bewertet → Eintrag mit Bewertung leer. | ✅ | Klein: Wo liegt das Log und wie lange (Datenschutz)? |
| L11 Laufzeit | Auslöser t0, Lead geöffnet bei t0+30 s, Job läuft → Anzeige *Dossier in Arbeit*. Job fertig bei t0+90 s → Dossier sichtbar. Messung: 95 % der Jobs unter 2 Min. (Perzentil angenommen). | ✅ | Fehlend, aber nicht blockierend: Was zeigt das CRM, wenn der Job scheitert oder nach X Minuten noch läuft (Timeout, Fehlerstatus, Retry)? Ohne Regel bleibt *Dossier in Arbeit* für immer stehen. |

## 2. Harte Regeln aus Lösung, Zielen und Nicht-Zielen

| # | Regel (Quelle) | Testfall: Eingabe → erwartetes Verhalten | Baubar? | Offene Frage |
|---|---|---|---|---|
| H1 | Agent verschickt nichts (Lösung, Nicht-Ziel 1, A3) | Beliebiges Dossier mit Vorschlägen → keine ausgehende Mail, keine Sequenz-Einschreibung, kein Versand-Endpunkt im Code aufrufbar. | ✅ | – |
| H2 | Bewertungsknopf *brauchbar / nicht brauchbar* (Lösung 4, Z4) | Vertriebler klickt *nicht brauchbar* → Wert im Log (L10), Kennzahl Z4 zählt ihn. | ✅ | Klein: Darf die Bewertung geändert werden, zählt die letzte? |
| H3 | Kein Lauf auf Vorrat (A4, Nicht-Ziel 2) | = L1(c). | ✅ | – |
| H4 | Keine E-Mail-Verifikation, keine E-Mail-Änderung (Nicht-Ziel 2) | = L9, E-Mail-Feld unverändert; kein Aufruf eines Verifikationsdienstes. | ✅ | – |
| H5 | Jedes Signal mit Datum und Quellenlink im Dossier (Lösung 2) | = L6; angezeigtes Signal hat sichtbares Datum und klickbaren Link. | ✅ | – |
| H6 | Nachfolger-Kontakt anlegen („Nachher", Szene 1) vs. Nachfolger-Suche als Nicht-Ziel | – | (Teil von L2/L9) | Ist „Nachfolger im CRM als neuer Kontakt angelegt" Teil des MVP? Nicht-Ziel 2 schließt Nachfolger-Suche nur „für alle Bestandskontakte" aus, L2 erwähnt sie gar nicht. Für mich ein Widerspruch, den ich nicht selbst auflösen sollte. |

Nicht baurelevant, kein Testfall nötig: Ziele Z1–Z3 und Guardrails G1–G3 sind Messgrößen des Piloten, keine Systemregeln (Z4 und G3 hängen an L10 bzw. L6). Nicht-Ziele Account-Mapping, Lead-Definition, Tool-Ersatz, Dashboard, Produkt für viele Kunden schließen nur Umfang aus.

## 3. Übergreifende offene Frage

**Quellen (O1):** Welche öffentlichen Quellen darf der Agent technisch und rechtlich nutzen, vor allem LinkedIn? Das PRD benennt das selbst als offen. Testfälle für L2 und L3 lassen sich mit gemockten Quellen schreiben, gebaut werden kann der Status-Check aber erst, wenn O1 entschieden ist. Ohne LinkedIn fällt vermutlich der größte Teil von L2 und Typ 2/5 aus L3 weg.

## 4. Zählung

- Regeln geprüft: **16** (L1–L11, H1–H5; H6 ist ein Widerspruch innerhalb von L2/L9 und wird dort gezählt)
- Davon mit Testfall: **13**
- Offen: **3** (L2 Vergleichsregel/Wechsel-Markierung, L3 Typ 4 und Typ 5, L9 Speicherort und Schreibrechte)
- Zusätzlich übergreifend offen: O1 Quellen (im PRD bereits als offen markiert)

## 5. Urteil

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C12 Logik ist baubar | ❌ | Drei Regeln (L2, L3, L9) lassen sich nicht in eindeutige Testfälle übersetzen, erlaubt ist höchstens eine. | L2: Vergleichsregel für Arbeitgeber/Titel (Normalisierung, widersprüchliche Quellen) plus Feld und Kanal für *gewechselt*/Hinweis; L3: Schwelle für Typ 4 „Neueinstellungen" und Quelle/Format/Erkennung der Themenliste für Typ 5; L9: konkretes CRM, Objekt/Feld, Verhalten bei erneutem Lauf und eindeutige Schreibrechte (Widerspruch zu *gewechselt*-Markierung und Nachfolger-Anlage im „Nachher"). |
