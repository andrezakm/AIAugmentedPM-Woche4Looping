---
name: stakeholder-review
description: Überarbeitet einen PRD, bis er CEO und Investoren gut zu erklären ist. Testleser-Subagenten in der Rolle von CEO und Investor lesen den PRD, geben ein Urteil ab, und es wird iteriert, bis beide das beste Urteil geben. Nutzen nach /prd-writer (Goal 4 im FLOW.md).
---

# Skill: Stakeholder-Review (CEO und Investoren)

## Zweck
Der PRD ist für das Produktteam geschrieben. CEO und Investoren lesen anders: Sie wollen in zwei Minuten verstehen, worum es geht, was es kostet, was es bringt und was schiefgehen kann. Dieser Skill macht den PRD für sie lesbar, **ohne** den Inhalt für das Team zu verwässern.

## Input
- Der neueste `output/PRD-*.md` (oder der, den der Nutzer nennt)
- `context/company.md`, `context/strategy.md`

## Vorgehen

### 1. Leseführung oben einbauen
Vor die Template-Abschnitte, in dieser Reihenfolge:
- **Kopf:** Wer wir sind (ein Satz), wer der Kunde ist, wie aktuell die Interviews sind, Lesehilfe (wer welchen Abschnitt lesen sollte), Vermerk *internes Dokument*
- **Auf einer Seite:** Problem, Lösung, Aufwand, Entscheidungspunkt, Risiko, in 6–8 Zeilen
- **Für den CEO:** Was es uns bringt (Umsatz, Auslastung, Referenz), was es kostet, was wir entscheiden müssen, was wir nicht tun
- **Für Investoren:** Warum dieses Muster wiederholbar ist, wie es Richtung Produkt führt, welche Annahme das Ganze trägt und wie wir sie prüfen
- **Begriffe:** Fachwörter in einem Satz erklärt (SDR, T&M, CRM …)

Detailabschnitte (z. B. die Problem-Auswahl) wandern in den Anhang. Querverweise anpassen.

### 2. Keine erfundenen Zahlen
Umsatz, Tagessatz, Marge, Marktgröße: Wenn es nicht in `context/` oder `input/` steht, dann `[Platzhalter]` und in einer Liste *Offen für die Geschäftsführung* sammeln.

### 3. Testleser
Starte zwei Subagenten parallel, jeder bekommt nur den PRD und seine Rolle:
- **CEO von NeoEmployee:** bootstrapped, 14 Leute, will Cash und Auslastung, hasst Projekte, die sich nicht wiederholen
- **Investor:** prüft, ob aus Projekten ein Produkt werden kann, sucht die tragende Annahme und das größte Risiko

Jeder Testleser antwortet mit:
1. Urteil auf der Skala *nicht verständlich / verständlich mit Lücken / klar und überzeugend*
2. Die drei Stellen, an denen er hängen geblieben ist
3. Die eine Frage, die er im Meeting stellen würde

### 4. Iterieren
Lücken schließen, erneut testen (neue Subagenten, damit sie den PRD frisch lesen). Bis **beide** *klar und überzeugend* sagen. Zitate nach jeder Runde mit `/quote-check` prüfen.

### 5. Loop-Protokoll
Neue Runden an das bestehende Loop-Protokoll im Anhang anhängen (Runde 2, Runde 3 …), mit den Urteilen der Testleser je Durchgang.

## Ablage
Der PRD wird an Ort und Stelle überarbeitet.

## Abbruchkriterium (für `/goal`)
CEO- und Investor-Testleser urteilen beide *klar und überzeugend*; keine erfundenen Zahlen; `/quote-check` 0 NICHT BELEGT; Runden im Loop-Protokoll dokumentiert.
