---
name: prd-goal
description: Schreibt einen PRD nicht nach Template, sondern gegen 14 prüfbare Zielkriterien, in einer eigenen Schleife aus Autor-Subagent, Prüfskript und unabhängigen Prüfer-Subagenten mit Anzeigetafel und offener Liste. Alternative zu /prd-writer. Nutzen, wenn der PRD belastbar sein muss oder wenn du die Prüfkriterien selbst schärfen willst.
---

# Skill: PRD gegen Zielkriterien

## Idee
- **Gerüst für die Form:** `skeleton.md`, nur Überschriften.
- **Kriterien für die Qualität:** `criteria.md`, 14 Kriterien, jedes mit Prüfer und Erfüllt-wenn.
- **Unabhängige Prüfung:** Der Autor prüft sich nie selbst. Skript und Prüfer-Subagenten sehen nur, was ihre Rolle braucht (`reviewers.md`).
- **Eigene Schleife statt `/goal`:** Diese Schleife macht die Arbeit. `/goal` kann sie von außen bewachen („bis die Anzeigetafel grün ist, höchstens 4 Runden“). Prüfen kann es sie nicht, denn es sieht nur das Gespräch.

## Rollen

| Rolle | Wer | Darf lesen |
|---|---|---|
| Koordinator | du (Haupt-Agent) | alles; schreibt nur Anzeigetafel, offene Liste, Ausschnitte, Loop-Protokoll |
| Autor | neuer Subagent je Runde | Synthese, `context/`, `input/`, `skeleton.md`, `criteria.md`, Vorentwurf und Reviews; **keine** anderen PRDs |
| Skript | `scripts/check_prd.py` | PRD, `input/`, `context/` (C1, C2, Hinweise zu C3) |
| Prüfer | je Rolle ein neuer Subagent je Runde | siehe `reviewers.md` |

## Ablauf

Arbeitsordner: `output/prd-goal-[produkt]-[YYYY-MM-DD]/` mit `PRD.md`, `reviews/`, `scoreboard.md`, `offene-punkte.md`.

**Schritt 0, optional: Blindentwurf (Variante D).** Ein Autor schreibt nur mit Gerüst und Auftrag, ohne Kriterien. Das hält den Lösungsraum offen. Danach folgt Schritt 1 als **Neuschrift**: Der Autor bekommt Kriterien und Blindentwurf *als Material* und schreibt neu, statt zu überarbeiten. Überarbeiten verankert am ersten Entwurf und lässt den Text wachsen.

**Schritt 1: Entwurf.** Autor-Subagent mit Gerüst und Kriterien. Auftrag: *„Schreibe einen PRD auf Basis der Synthese und wäge ab und dokumentiere, welches Bedürfnis die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat. Beachte unsere Strategie.“* Das Loop-Protokoll führt der Koordinator.

**Schritt 2: Runde 1 prüfen (Suche).**
1. `python3 -I .claude/skills/prd-goal/scripts/check_prd.py [PRD]` → `reviews/r1-skript.txt`
2. Ausschnitte schneiden: *Problem* (für LAIE), *Kurzfassung* (für KUNDE), *Lösung* bis vor *Plan* (für ENTW)
3. LAIE, ENTW, KUNDE und CEO parallel starten, danach PRÜFER mit Skriptausgabe und Kunden-Einwänden
4. Anzeigetafel C1–C14 eintragen. Jedes ❌ und jeden Einwand als nummerierten Punkt in `offene-punkte.md` aufnehmen, nach Rolle gruppiert

**Schritt 3: Überarbeiten.** Neuer Autor-Subagent mit PRD, Reviews, offener Liste und Kriterien. Er behebt die Punkte, ohne erfüllte Kriterien zu brechen.

**Schritt 4: Runde 2+ prüfen (Abhaken).** Wie Schritt 2, aber jeder Prüfer bekommt seinen Teil der offenen Liste und hakt ab. Höchstens 1 neuer Punkt je Prüfer, nur Blocker oder K.-o.-Grund (siehe `reviewers.md`).

**Abbruch:** alle 14 ✅ in einer Runde, oder nach 4 Runden mit offenen Punkten berichten.

## Was der Mensch entscheidet
- Alles unter `[Platzhalter]` mit Geldbezug (Preise, Tagessatz, Umsatz)
- Die Annahmen im Annahmen-Block: übernehmen, ändern, streichen
- Ob ein Kriterium selbst falsch ist. Das ist die äußere Schleife: Kriterien gegen Ergebnis prüfen und `criteria.md` mit Änderungseintrag anpassen.

## Ablage im PRD
Am Ende des PRD: Abschnitt `## Loop-Protokoll` mit der Anzeigetafel je Runde und der Checkliste der Abbruchkriterien (Format aus `CLAUDE.md`).

## Herkunft
Experiment vom 2026-11-05, siehe `output/experiment-prd/vergleich-template-vs-kriterien.md`: Template-PRD 4/14, Kriterien-PRDs 11/14 nach zwei Runden. Kriterien v2 und das Abhaken ab Runde 2 sind die Konsequenz daraus, dass v1 nicht konvergierte.
