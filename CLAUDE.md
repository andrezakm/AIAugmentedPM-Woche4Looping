# Kursumgebung: AI-Augmented PM — Woche 1

Sobald der Nutzer den Kurs starten möchte — z.B. durch "starte den Kurs", "starte den Kurs ab Schritt X", "los geht's", "weiter" oder ähnliches — lies `kurs.md` vollständig ein und führe die darin enthaltenen Anweisungen aus. Bei "ab Schritt X" springst du direkt zu diesem Schritt. Starte ohne Erklärungen vorweg.

Für alle anderen Fragen oder Aufgaben verhältst du dich normal.

## Aufbau

- `context/`: statischer Kontext (Firma, Strategie)
- `input/`: dynamischer Kontext (Interviews)
- `.claude/skills/`: was die KI tun soll, als Skills mit `/name` aufrufbar
- `output/`: Ergebnisse
- `FLOW.md`: der Standard-Flow, ein `/goal` pro Schritt

Skills: `/interview-analysis` → `/needs-synthesis` → `/prd-writer` → `/stakeholder-review` → `/customer-proposal`, optional `/prototype`. Querschnitt: `/quote-check`. Alles in einem: `/interview-to-prd`.

## Arbeitsregeln für alle Skills

**Ein Schritt, ein Ziel.** Tu, was das aktuelle Goal verlangt, nicht den nächsten Schritt gleich mit. Nach den Einzelanalysen kommt keine Synthese, bis der Nutzer sie verlangt.

**Zitate**
- Interview-Zitate in "…", Zeichen für Zeichen aus `input/`, inklusive Groß-/Kleinschreibung.
- Strategie-Zitate in „…", wörtlich aus `context/`.
- Eigene Umschreibungen *kursiv*, ohne Anführungszeichen.
- Nie eine Frage des Interviewers der interviewten Person zuschreiben.
- Einzelanalysen können Umschreibungen in Anführungszeichen enthalten. Zitate daraus vor der Übernahme immer gegen `input/` prüfen.
- Vor „fertig": `/quote-check` auf das Dokument.

**Keine erfundenen Daten.** Was nicht in `context/` oder `input/` steht, wird `[Platzhalter]`. Die genaue Regel, auch wann eine benannte Annahme erlaubt ist, steht in `.claude/skills/prd-goal/criteria.md` unter „Datenregel“. Sie gilt für alle Skills.

**Loop-Protokoll.** Jedes Dokument, das unter einem `/goal` entsteht, endet mit einem Abschnitt `## Loop-Protokoll`:

| Durchgang | Was gemacht | Ergebnis | Abbruchkriterium erfüllt? |
|---|---|---|---|
| 1 | … | … | nein: … |
| 2 | … | … | ja |

Danach eine Checkliste der Abbruchkriterien mit ✅/❌. Fehlerhafte oder ungültige Prüfläufe werden als „verworfen" mit Grund eingetragen, nicht weggelassen.

**Testleser.** Wo ein Skill Testleser verlangt, bekommt jeder Subagent nur das Dokument und seine Rolle, und jede Runde startet einen neuen Subagenten.
