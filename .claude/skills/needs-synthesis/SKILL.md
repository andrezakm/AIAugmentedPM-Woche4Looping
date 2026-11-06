---
name: needs-synthesis
description: Verdichtet alle Einzelanalysen aus output/ auf höchstens zwei Kundenbedürfnisse, jeweils belegt durch wörtliche Zitate und nachweisbar an context/strategy.md ausgerichtet. Mit dokumentierten Loop-Durchgängen. Nutzen nach /interview-analysis (Goal 2 im FLOW.md).
---

# Skill: Bedürfnis-Synthese

## Zweck
Aus zehn Einzelanalysen werden **höchstens zwei** Bedürfnisse. Jedes muss
1. aus den Interviews **herausstechen** (Häufigkeit, Schmerz, Zahlen),
2. über Zitate **rückverfolgbar** sein, bis ins Original-Interview,
3. **nachweisbar** zur Firmenstrategie passen.

Was nicht durchkommt, wird mit Begründung ausgeschlossen, nicht weggelassen.

## Input
- Alle `output/interview-individual-*.md`
- `input/` (für die Zitatprüfung, die Einzelanalysen können Umschreibungen in Anführungszeichen enthalten)
- `context/strategy.md` und `context/company.md`

## Vorgehen

### 1. Kandidaten sammeln
Alle Probleme und Bedürfnisse aus den Einzelanalysen in Kandidaten bündeln (typisch 6–10, Buchstaben A, B, C …). Pro Kandidat: wer hat es genannt?

### 2. Kandidaten-Tabelle mit Kriterien
| Kandidat | Nennungen (n/10) | Harte Zahlen | Schmerz | S1 Vision | S2 Umsatz | S3 Muster | Ergebnis |

Die Strategiekriterien kommen aus `context/strategy.md`:
- **S1 Vision-Filter:** Ersetzt der Agent eine Fähigkeit, die heute ein Mensch ausübt?
- **S2 Umsatz ist Runway:** Als T&M-Projekt in Wochen lieferbar, schnelles Geld?
- **S3 Muster / Brücke:** Wiederholbar bei anderen Kunden, Schritt Richtung Produkt?

Ein Kandidat kommt nur weiter, wenn er S1–S3 erfüllt **und** in den Interviews heraussticht.

### 3. Die (maximal) zwei Bedürfnisse ausformulieren
Pro Bedürfnis:
- Ein Satz in Kundensprache: *Warum soll ich diese Person jetzt anrufen …* (Beispiel)
- **Zitat-Spur:** Tabelle Person | Rolle | wörtliches Zitat | Ableitung. Zitate in "…", exakt aus `input/`.
- **Ableitung:** Wie kommt man vom Zitat zum Bedürfnis? In eigenen Worten, *kursiv* wo es Umschreibung ist.
- **Strategie-Nachweis:** Tabelle S1/S2/S3 mit dem Satz aus `context/strategy.md` (in „…", wörtlich) und der Begründung.

### 4. Ausschlüsse
Jeder nicht gewählte Kandidat mit einem Satz, warum nicht (zu selten, verletzt S1, kein T&M-Fit …).

### 5. Prüfen
- `/quote-check` auf die Synthese, Quellen `input context`. Ziel: **0 NICHT BELEGT.**
- Jedes Bedürfnis hat Zitate von mindestens 3 Personen.
- Jedes Bedürfnis hat S1–S3 mit Strategie-Zitat.
- Höchstens zwei Bedürfnisse.

Schlägt eine Prüfung fehl: korrigieren, erneut prüfen, als neuen Durchgang protokollieren.

### 6. Loop-Protokoll
Am Ende der Datei, eigener Abschnitt `## Loop-Protokoll` im Format aus `CLAUDE.md`. Auch verworfene Prüfläufe (z. B. ein Prüfskript, das selbst fehlerhaft war) werden als „verworfen" dokumentiert.

## Ablage
`output/interview-synthesis-[heute YYYY-MM-DD].md`

## Abbruchkriterium (für `/goal`)
Höchstens zwei Bedürfnisse, jedes mit Zitat-Spur aus mindestens drei Interviews und S1–S3-Nachweis; `/quote-check` meldet 0 NICHT BELEGT; Loop-Protokoll vorhanden.
