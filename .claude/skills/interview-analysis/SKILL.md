---
name: interview-analysis
description: Analysiert jedes Interview in input/ einzeln, ein Subagent pro Interview, und legt pro Person eine Einzelanalyse in output/ ab. Macht KEINE Synthese. Nutzen, wenn Interviews analysiert werden sollen (Goal 1 im FLOW.md) oder wenn nur ein einzelnes Interview analysiert werden soll.
---

# Skill: Interview-Einzelanalyse

## Zweck
Pro Interview eine tiefe, fokussierte Analyse. Jeder Subagent sieht genau ein Interview und sonst nichts. Das hält den Fokus scharf und verhindert, dass sich Aussagen verschiedener Personen vermischen.

**Dieser Skill macht keine Synthese.** Die Synthese ist ein eigener Schritt mit eigenem Ziel: `/needs-synthesis`. Nach der letzten Einzelanalyse ist hier Schluss.

## Input
- Alle Dateien in `input/`, oder nur die Datei, die der Nutzer nennt
- Lies zuerst die Dateiliste, damit klar ist, wie viele Analysen am Ende vorliegen müssen

## Vorgehen

### 1. Ein Subagent pro Interview, parallel
Starte für jede Interview-Datei einen eigenen Subagenten im selben Schritt (parallel). Gib jedem Subagenten mit:
- den Pfad zu genau einer Interview-Datei
- die sechs Abschnitte unten
- die Zitat-Regeln unten
- den Zielpfad der Ausgabedatei

### 2. Die sechs Abschnitte jeder Einzelanalyse

**1. Profil der interviewten Person**
- Name, Rolle, Datum des Interviews
- Ein Absatz: Wer ist diese Person in der Organisation, durch welche Brille sieht sie die Welt?

**2. Stimmung (Sentiment)**
- Vorherrschender Ton, konkret (nicht nur „frustriert", sondern welche Art von Frust und warum)
- Energie: ausgebrannt, aufgeladen, resigniert, defensiv?
- Vertrauen: in Tools, Kollegen, Führung?
- Ein wörtliches Zitat, das den Zustand am besten einfängt

**3. Beschriebene Probleme**
- Jedes genannte Problem, direkt oder implizit
- Pro Problem: Was ist es, wie wurde es beschrieben, wie viel Schmerz steckt darin?

**4. Dringlichkeitssignale**
- Welche Probleme kosten *jetzt* etwas?
- Achte auf „right now", „every day", „I can't", Zahlen und Kennzahlen, emotionale Spitzen

**5. Eigentliche Bedürfnisse**
- Je Bedürfnis: *Diese Person braucht X, damit Y*
- Trenne, was sie sagt, dass sie will, von dem, was sie tatsächlich braucht

**6. Bemerkenswerte Zitate**
- 3–5 wörtliche Zitate, die lebendig, konkret oder entlarvend sind

### 3. Zitat-Regeln (für jeden Subagenten verbindlich)
- Zitate stehen in englischen Anführungszeichen "…" und sind **Zeichen für Zeichen** aus dem Interview kopiert, inklusive Groß-/Kleinschreibung.
- Eigene Umschreibungen stehen *kursiv* und **ohne** Anführungszeichen.
- Fragen des Interviewers werden nie der interviewten Person zugeschrieben.
- Auslassungen mit …, aber nichts umformulieren.

### 4. Ablage
`output/interview-individual-[nachname-kleingeschrieben]-[Interviewdatum YYYY-MM-DD].md`

Gibt es die Datei schon, wird sie überschrieben. Keine Skript-Anweisungen in die Ausgabedatei schreiben.

### 5. Abschlussprüfung
- Anzahl Dateien in `output/interview-individual-*` = Anzahl Interviews im Lauf
- Jede Datei hat alle sechs Abschnitte
- Optional, aber empfohlen: `/quote-check` auf jede Datei. Was dort als NICHT BELEGT auftaucht, wird in der nächsten Stufe nicht ungeprüft übernommen.

## Abbruchkriterium (für `/goal`)
Für jedes Interview in `input/` liegt genau eine Einzelanalyse mit allen sechs Abschnitten in `output/`. Es gibt keine Synthese-Datei aus diesem Lauf.
