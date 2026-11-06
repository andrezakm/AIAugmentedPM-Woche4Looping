# Standard-Flow: Von Interviews zum Kundenangebot

Dieser Flow bildet nach, wie wir die Woche-1-Ergebnisse in `output/` tatsächlich erzeugt haben: **ein `/goal` pro Schritt.**

`/goal` legt eine Bedingung fest, die erfüllt sein muss, bevor Claude aufhören darf. Claude arbeitet, prüft, verbessert und prüft wieder, so lange, bis die Bedingung stimmt. Jeder Durchgang wird im Loop-Protokoll des Dokuments festgehalten. Du formulierst also nicht den Weg, sondern **wie ein gutes Ergebnis aussieht.** Den Weg kennt der Skill.

Du kannst die Goals wörtlich kopieren oder in eigenen Worten schreiben. Gib erst das nächste Goal, wenn du das Ergebnis des vorherigen gelesen hast.

---

## Goal 1: Einzelanalysen

```
/goal Lass Subagenten jedes Interview in input/ einzeln mit /interview-analysis analysieren, bis jedes Interview analysiert ist. Lege die Daten so ab, wie im Skill beschrieben. Keine Synthese.
```

**Fertig, wenn:** pro Interview eine Datei `output/interview-individual-*.md` mit allen sechs Abschnitten existiert.
**Warum keine Synthese?** Weil die Synthese ein eigenes Ziel mit eigenen Kriterien hat. Wer zu früh verdichtet, verliert die Einzelstimmen.

---

## Goal 2: Synthese auf zwei Bedürfnisse

```
/goal Mache mit /needs-synthesis eine Synthese aller Einzelanalysen in output/, bis sie auf höchstens zwei wichtige Kundenbedürfnisse reduziert ist. Die Bedürfnisse müssen anhand von Zitaten und Ableitungen eindeutig als herausstechend erkennbar und rückverfolgbar sein und sich nachweisbar an context/strategy.md orientieren. Dokumentiere die Loop-Durchgänge.
```

**Fertig, wenn:** ≤ 2 Bedürfnisse, jedes mit Zitaten von mindestens drei Personen und S1–S3-Nachweis; `/quote-check` meldet 0 NICHT BELEGT; Loop-Protokoll am Ende.

---

## Goal 3: PRD mit wirtschaftlicher Abwägung

```
/goal Schreibe mit /prd-writer einen PRD auf Basis der neuesten Synthese, bis du abgewogen und dokumentiert hast, welches der Bedürfnisse die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat. Beachte unsere Strategie. Dokumentiere die Loops.
```

**Fertig, wenn:** alle Template-Abschnitte gefüllt; Anhang A zeigt die gewichtete Bewertung (K1–K7) und Robustheitsszenarien; `/quote-check` 0; Anhang B Loop-Protokoll.

---

## Goal 4: Für CEO und Investoren

```
/goal Bearbeite den PRD mit /stakeholder-review, bis er sowohl Investoren als auch dem CEO gut zu erklären ist.
```

**Fertig, wenn:** CEO- und Investor-Testleser beide *klar und überzeugend* sagen; keine erfundenen Zahlen; Runden im Loop-Protokoll.

---

## Goal 5: Kundenangebot

```
/goal Erstelle mit /customer-proposal aus dem PRD ein Angebot für den Entscheider beim Kunden, bis ein Testleser in seiner Rolle es klar und überzeugend findet und kein interner Inhalt mehr darin steht.
```

**Fertig, wenn:** Testleser *klar und überzeugend*; Leak-Check sauber; die Liste der offenen kaufmännischen Entscheidungen liegt dir vor.

**Danach du:** Platzhalter füllen (Tagessatz, Deckel, Hosting, Kontakt …). Kein Angebot geht ohne menschliche Freigabe raus.

---

## Optional: Prototyp

```
/goal Baue mit /prototype einen klickbaren HTML-Prototypen der wichtigsten Kerninteraktion aus dem PRD und öffne ihn im Browser.
```

---

## Alles in einem Rutsch

```
/interview-to-prd
```

Führt Goal 1 bis 5 ohne Zwischenstopp aus. Gut, wenn du den Flow kennst. Schlecht zum Lernen, weil du die Zwischenergebnisse nicht beurteilst.

---

## Querschnitt: Zitat-Check

Nach jedem Schritt, der Zitate schreibt:

```
/quote-check output/DATEI.md
```

## Ergebnisse dieses Durchlaufs (Referenz)

| Goal | Datei |
|---|---|
| 1 | `output/interview-individual-*-2025-10-*.md` (10 Dateien) |
| 2 | `output/interview-synthesis-2026-11-03.md` |
| 3 + 4 | `output/PRD-signal-brief-agent-2026-11-03.md` |
| 5 | `output/proposal-signal-brief-agent-2026-11-03.md` |
