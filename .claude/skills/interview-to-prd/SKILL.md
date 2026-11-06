---
name: interview-to-prd
description: Full Pipeline. Führt den kompletten Standard-Flow aus FLOW.md in einem Rutsch aus, von den Interviews in input/ bis zum Kundenangebot, jeder Schritt mit eigenem Abbruchkriterium und Loop-Protokoll. Nutzen, wenn alles ohne Zwischenstopp laufen soll.
---

# Skill: Interview → PRD → Angebot (Full Pipeline)

## Zweck
Derselbe Ablauf wie in `FLOW.md`, nur ohne menschliche Zwischenstopps. Jeder Schritt läuft so lange, bis **sein** Abbruchkriterium erfüllt ist. Erst dann beginnt der nächste.

## Regeln
- Nicht zwischen den Schritten nachfragen. Fehlt etwas, triff eine vernünftige Entscheidung und dokumentiere sie im Loop-Protokoll des jeweiligen Dokuments.
- Kaufmännische Zusagen (Preise, Deckel, Hosting) nie erfinden: Platzhalter setzen und am Ende auflisten.
- Kein Schritt überspringt seine Prüfung. Ein Schritt ohne erfülltes Abbruchkriterium stoppt die Pipeline; dann berichten, was fehlt.

## Ablauf

| # | Skill | Abbruchkriterium |
|---|---|---|
| 1 | `/interview-analysis` | Eine Einzelanalyse pro Interview, alle sechs Abschnitte, keine Synthese |
| 2 | `/needs-synthesis` | ≤ 2 Bedürfnisse, Zitat-Spur aus ≥ 3 Interviews, S1–S3-Nachweis, `/quote-check` 0 NICHT BELEGT, Loop-Protokoll |
| 3 | `/prd-writer` | Alle Abschnitte gefüllt, Anhang A mit gewichteter Abwägung und Robustheit, `/quote-check` 0, Anhang B Loop-Protokoll |
| 4 | `/stakeholder-review` | CEO- und Investor-Testleser: *klar und überzeugend*, keine erfundenen Zahlen |
| 5 | `/customer-proposal` | Entscheider-Testleser: *klar und überzeugend*, Leak-Check sauber, Platzhalter-Liste |
| 6 | `/prototype` *(optional)* | Kerninteraktion klickbar, im Browser geöffnet |

## Am Ende
Kurzer Bericht an den Nutzer:
1. Welche Dateien entstanden sind
2. Welches Bedürfnis gewählt wurde und warum, in zwei Sätzen
3. Wie viele Loop-Durchgänge je Schritt nötig waren
4. **Offen für einen Menschen:** die Platzhalter-Liste aus dem Angebot
