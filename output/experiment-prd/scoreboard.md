# Anzeigetafel: Template vs. Zielkriterien

A = bestehender Template-PRD nach Goal 3 + Goal 4, nicht weiter überarbeitet (Referenz).
B = Autor kennt nur das Gerüst, lernt nur über Prüfer-Feedback.
C = Autor kennt Gerüst + Kriterien von Anfang an.
D = Blindentwurf (B r1) als Material, Neuschrift mit **Kriterien v2** (Datenregel, C12 „blockierend“). Nicht direkt vergleichbar mit A–C (v1).
O = Lackmustest: ursprüngliches `scripts/PRD-writer.md` (Stand letzter Commit), ein Durchgang ohne jede Prüfung, bewertet mit Kriterien v2 wie D.
Jede Zelle = Urteil eines **neuen** Prüfer-Subagenten.

| Kriterium | Prüfer | A | B r1 | B r2 | C r1 | C r2 | D r1 | D r2 | O ohne Loop |
|---|---|---|---|---|---|---| --- | --- | --- |
| C1 Gerüst | Skript | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ 11/14 Abschn. |
| C2 Zitate echt | Skript | ❌ 3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ 4 |
| C3 Keine erfundenen Zahlen | Skript + Prüfer | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| C4 Problem für Laien | Laie | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C5 Beleg ≥ 4 Personen | Prüfer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C6 Wahl robust | Prüfer | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| C7 Strategie wörtlich | Prüfer | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| C8 Alternativen | Prüfer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C9 Narrativ echt | Prüfer | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| C10 Ziele messbar | Prüfer | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |
| C11 Nicht-Ziele | Prüfer | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| C12 Logik baubar | Entwickler | ❌ 6/23 | ❌ 10/23 | ❌ 6/27 | ❌ 3/16 | ❌ 4/15 | ❌ 0 blockierend, 17 offen nicht gelistet | ✅ 0 blockierend, 18 gelistet | ❌ 0 blockierend, nicht gelistet |
| C13 Einwände | Kunde + Prüfer | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| C14 CEO in 2 Min. | CEO | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| **Summe** | | **4/14** | **8/14** | **11/14** | **10/14** | **11/14** | **10/14** | **14/14** | **3/14** |
| Länge (Zeilen) | | 351 | 304 | 436 | 272 | 312 | 326 | 342 | 154 |

Laie: Verständnisfragen je Runde A 12 · B 10 → 10 · C 10 → 11 · D 11 → 12 · O 16 (C4 trotzdem ✅, weil die Wiedergabe stimmt).

D r2: Prüfer haken die offene Liste ab (`D-offene-punkte.md`), höchstens 1 neuer Punkt je Prüfer, nur Blocker/K.-o. Kein Prüfer hat einen neuen Punkt genannt.
