---
name: prd-writer
description: Schreibt einen PRD auf Basis der neuesten Bedürfnis-Synthese, wägt dabei ab, welches Bedürfnis die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat, und dokumentiert die Abwägung und die Loops. Nutzen nach /needs-synthesis (Goal 3 im FLOW.md).
---

# Skill: PRD Writer

## Zweck
Ein PRD, das zeigt, **warum genau dieses** Bedürfnis zuerst gebaut wird. Die Abwägung zwischen den (bis zu) zwei Bedürfnissen der Synthese ist Teil des Dokuments, nicht ein Gedanke im Hintergrund.

## Input
1. `context/company.md`: Wer NeoEmployee ist, was wir bauen, wie wir arbeiten
2. `context/strategy.md`: Bootstrap, T&M, Weg zum Produkt, Vision-Filter
3. Die **neueste** `output/interview-synthesis-*.md`
4. `input/` für die Zitatprüfung
5. Ältere `output/PRD-*.md`, falls vorhanden: lesen, ob schon ein Bedürfnis gewählt wurde. Widerspricht die neue Wahl, das im PRD offen begründen.

## Vorgehen

### 1. Abwägung: Welches Bedürfnis zuerst?
Bewerte jedes Bedürfnis aus der Synthese auf 0–10 je Kriterium, gewichtet:

| # | Kriterium | Gewicht |
|---|---|---|
| K1 | Schmerz und Dringlichkeit (Zahlen, Häufigkeit) | 20 % |
| K2 | Zahlungsbereitschaft / Budget-Eigentümer erkennbar | 15 % |
| K3 | Lieferzeit als T&M-Projekt (S2) | 20 % |
| K4 | Vision-Fit, ersetzt eine Fähigkeit (S1) | 10 % |
| K5 | Wiederholbarkeit bei anderen Kunden (S3) | 15 % |
| K6 | Lieferrisiko (Daten, Integration, Rechtliches) | 10 % |
| K7 | Messbarkeit des Erfolgs | 10 % |

- Jede Bewertung mit einem Satz Begründung und, wo möglich, einem Zitat aus `input/`.
- **Robustheit:** Rechne mindestens drei andere Gewichtungen (z. B. „nur Geschwindigkeit", „nur Produktpfad", „gleich gewichtet"). Kippt das Ergebnis, sag es offen.
- Der Gewinner wird gebaut. Der Verlierer wird nicht verworfen: Prüfe, was davon als kleiner MVP-Baustein mitläuft und was **Phase 2 / Folgeauftrag** wird.

### 2. PRD schreiben
Fülle jeden Abschnitt der Vorlage unten (gleiche Vorlage wie `My-PRD-Template.md`). Nichts leer lassen. Fehlende Infos (Termine, Preise) als relative Angaben (Woche 1, Woche 2) oder als `[Platzhalter]`, **nie erfinden**.

- Zitate im PRD in "…", wörtlich aus `input/`. Umschreibungen *kursiv* ohne Anführungszeichen.
- Die Abwägung aus Schritt 1 kommt als **Anhang A: Problem-Auswahl** ins PRD.

### 3. Prüfen
- `/quote-check` auf den PRD. Ziel: 0 NICHT BELEGT.
- Jeder Abschnitt der Vorlage ist gefüllt.
- Anhang A enthält Bewertungstabelle, Robustheitsszenarien und die Entscheidung über den Verlierer.
- Keine erfundenen Zahlen.

### 4. Loop-Protokoll
Als **Anhang B: Loop-Protokoll** im Format aus `CLAUDE.md`.

## PRD Template

```
# PRD: [Product Name]

**Prepared by:** NeoEmployee
**Date:** [today's date]
**Based on:** Interview research — [number] interviews, [date range]
**Engagement type:** Time & Material / Custom AI Agent Build

---

# Problem Alignment

## Problem & Opportunity

[1–2 sentences. Must be readable standalone and communicable to a non-technical stakeholder.]

- Why does this matter to the customer and to NeoEmployee?
- What evidence from the interviews supports this? (Quote or cite specific interviewees.)
- Which roles and people are most affected?
- Why is solving this urgent — what is being lost every day it goes unsolved?
- Why now — what makes the timing right?

## High-Level Approach

[Describe the rough shape of the solution. One clear sentence that captures it. Then explain why this approach over alternatives.]

**Alternatives considered:**
- [Alternative 1] — why we ruled it out
- [Alternative 2] — why we ruled it out

### Narrative

[Write a brief story — one day in the life of the primary user before the agent, and one day after. Make the contrast concrete and human.]

## Goals

1. [Primary measurable goal — tied to the urgent problem]
2. [Secondary measurable goal]
3. [Qualitative/feeling goal — what should the user experience feel like?]
4. [Guardrail metric — what should NOT get worse]

## Non-Goals

1. [What this agent explicitly does not do — and why]
2. [What is out of scope for this engagement]
3. [What is saved for a future phase or product]

---

# Solution Alignment

## Key Features

**Plan of record (MVP):**

1. [Feature 1 — most critical, must-ship]
2. [Feature 2]
3. [Feature 3]
4. [Feature 4]

**Future considerations:**

1. [Feature saved for Phase 2]
2. [Feature saved for Phase 2]

### Key Flows

[Describe the end-to-end experience as numbered steps. What does the user do? What does the agent do? What lands in their hands?]

1. ...
2. ...
3. ...

### Key Logic

1. [Rule 1 — how the agent decides what to surface]
2. [Rule 2 — formatting or length constraints on output]
3. [Rule 3 — how conflicts or missing data are handled]
4. [Rule 4 — what the agent does NOT overwrite or touch]
5. [Non-functional requirement — performance, latency, reliability]

---

# Development and Launch Planning

| Milestone | Target | Description |
|-----------|--------|-------------|
| Kickoff | Week 1 | Scope confirmation, data source access, CRM credentials |
| Agent prototype | Week 2–3 | First working version on 20 test prospects |
| Client feedback round | Week 3 | Rep team tests prototype, feedback collected |
| Integration complete | Week 4–5 | CRM write-back, delivery mechanism live |
| QA & edge case hardening | Week 5–6 | Edge cases, formatting, error handling |
| Launch | Week 6 | Full prospect list live, all reps onboarded |

## Operational Checklist

- [ ] CRM credentials and API access confirmed
- [ ] Prospect list format agreed (CSV / CRM export / live sync)
- [ ] Output delivery method confirmed (email digest / CRM attachment / Slack)
- [ ] Data sources and scraping permissions reviewed
- [ ] Rep team onboarding session scheduled
- [ ] Success metrics baseline captured before launch
- [ ] Rollback / pause plan documented

---

## Other

### Risks

1. [Risk 1 — data source reliability or access]
2. [Risk 2 — CRM integration complexity]
3. [Risk 3 — rep adoption]

### FAQ

**Q: Why not just buy more ZoomInfo licenses?**
A: [Answer grounded in interview evidence]

**Q: How is this different from what the SDRs are doing today?**
A: [Answer grounded in interview evidence]

### Appendix

- Interview synthesis: `output/interview-synthesis-[date].md`
- Individual interview analyses: `output/interview-individual-*-[date].md`
- Company context: `context/company.md`
- Strategy context: `context/strategy.md`

---

## Product Summary

[Write 1 tight paragraph — maximum 5 sentences — that describes the product at the highest possible level. What is it, who is it for, what does it replace, what does it deliver, and what changes for the user the day it goes live. This paragraph should be readable by a CEO, a sales rep, or an investor in 30 seconds and leave them with a complete picture.]
```

---

## Ablage
`output/PRD-[produktname-kebab-case]-[heute YYYY-MM-DD].md`

Keine Skript-Anweisungen in die Ausgabedatei schreiben.

## Abbruchkriterium (für `/goal`)
Alle Abschnitte gefüllt; Anhang A zeigt gewichtete Abwägung und Robustheit, und der Gewinner ist in jedem Szenario benannt oder das Kippen ist begründet; `/quote-check` 0 NICHT BELEGT; Anhang B Loop-Protokoll vorhanden.
