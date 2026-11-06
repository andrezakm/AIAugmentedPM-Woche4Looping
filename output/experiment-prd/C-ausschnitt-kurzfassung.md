## Kurzfassung

**Was wir bauen:** Einen KI-Agenten für die Vertriebsorganisation des Kunden. Zu jedem Prospect, der einem Vertriebler zugewiesen wird, legt er ein kurzes Dossier ins CRM (Salesforce): höchstens drei aktuelle, mit Quelle belegte Anlässe zum Anrufen (Finanzierungsrunde, Führungswechsel, Neueinstellungen, neu in der Rolle, Themen, über die die Person schreibt) und je einen Vorschlag für den Gesprächseinstieg. Vorher prüft er, ob die Person noch bei der Firma arbeitet. Er verschickt nichts und ersetzt nicht den Vertriebler, nur dessen Recherche.

**Warum der Kunde dafür zahlt:** Die Vertriebler recherchieren heute 15 bis 40 Minuten pro Prospect. Eine SDR schafft 20 statt der geforderten 50 Calls am Tag, von 100 Marketing-Leads werden 5 mit Kontext bearbeitet. Der VP Sales rechnet selbst: "If you do the math, that's only 4 prospects an hour." Laut Synthese nennen 9 von 10 Befragten das Problem.

**Was es uns kostet (Aufwand):** *Schätzung des PM vor dem Technik-Spike, nicht belastbar:* Spike 1 Person × 1 Woche, MVP 2 Personen × 4 bis 6 Wochen (8 bis 12 Personenwochen), Pilotbegleitung 1 Person in Teilzeit über `[Platzhalter: Pilotdauer]`. Das bindet 2 unserer 14 Leute; das Pattern-Team (2 Personen) bleibt unberührt. Belastbare Zahl nach dem Spike. Tagessatz `[Platzhalter]`.

**Was es uns bringt:** (1) T&M-Umsatz über Phase 0 bis 3, Volumen = Personentage × Tagessatz `[Platzhalter]`, bei der Schätzung oben also Spike plus 8 bis 12 Personenwochen plus Pilot. (2) Einen Folgeauftrag Phase 2 (Datenpflege mit Sales Ops, eigener Käufer), Größe `[Platzhalter: nach Scoping Phase 2]`. (3) Einen wiederverwendbaren Signal-Baustein für das Pattern-Team. Das passt zur Strategie: „every deal we close extends how long we can operate and invest in the product path.“

**Was schiefgehen kann:**
1. **Recht und Datenzugang (LinkedIn) ungeklärt.** Ohne LinkedIn sinkt der Nutzen stark. Gegenmittel: Go/No-Go am Ende von Phase 0, bevor wir das MVP-Team binden (R2).
2. **Technik trägt nicht** (Signale zu ungenau, Laufzeit zu lang). Gegenmittel: Spike vor dem Bau, Abbruch möglich (R9).
3. **Kunde gibt T&M ohne Deckel nicht frei, Business Case unbelegt.** Gegenmittel: Budgetrahmen je Phase, Pilot misst zusätzlich Termine pro SDR (Z5) und liefert eine Break-even-Rechnung (R10).
4. **Zahlungsrisiko** für uns als bootstrapped Firma. Gegenmittel (*Vorschlag*): Abrechnung je Phase, nächste Phase erst nach Zahlung der vorherigen (R11).
5. **Antwortquote fällt**, weil die Ansprache generisch wird. Gegenmittel: Guardrail G1 mit Abbruchregel (R1).

**Was die Geschäftsführung entscheiden muss:**
1. **Spike und Phase 0 bezahlt anbieten oder auf eigenes Risiko?** *Empfehlung PM:* bezahlt, als kleine eigene Phase, weil Umsatz unsere Runway ist (S2) und der Spike zugleich das Abbruchrisiko für uns begrenzt.
2. **Teambesetzung:** wer die 2 Personen sind, `[Platzhalter: Namen]`.
3. **Tagessatz und Preisuntergrenze** für Pilot und Ausbau (O3).
4. **Budgetdeckel je Phase ja oder nein** (Antwort auf den erwarteten Einwand *T&M ohne Zahl*, O8).

Beim Kunden zu klären, nicht unsere Entscheidung: Freigabe von Pilot und Pilotgruppe, erlaubte Datenquellen, Budget-Owner (O1, O2, O4).

---

