# AI-Augmented PM — Woche 4 Extra: Qualität zusichern mit dem Prüfloop

Dieses Repository gehört zur Extra-Lektion **„Qualität zusichern mit dem Prüfloop“** in Woche 4 des Kurses **AI-Augmented Product Management**.

In Woche 4 hast du Spec und Eval für Software kennengelernt: Kriterien festlegen, dann prüfen lassen. Hier wenden wir dieselbe Idee auf ein Produktdokument an, einen PRD. Als Versuchsobjekt dient das Material aus Woche 1: zehn (synthetische) Kundeninterviews der fiktiven Firma NeoEmployee, die Synthese und der PRD daraus.

---

## Voraussetzungen

- **Claude Code**, als Desktop-App (Code-Tab) oder im Terminal (`claude`). Die Lektion nutzt `/goal` und Subagenten.
- Ein Claude-Konto mit Zugang zu Claude Code
- Python 3 (für Zitat-Check und Prüfskript, auf dem Mac vorinstalliert)

---

## Installation

1. Auf dieser GitHub-Seite auf den grünen **Code**-Button → **Download ZIP**, dann entpacken.
   - **Windows:** Rechtsklick → **„Alle extrahieren"**.
   - **Mac:** Doppelklick genügt.
2. Den entpackten Ordner in Claude Code öffnen. Es muss der Ordner sein, in dem direkt `CLAUDE.md` liegt.
3. Beim ersten Öffnen fragt Claude Code, ob du dem Ordner vertraust. Bestätige.

---

## Was du hier findest

```
├── README.md              ← Diese Datei
├── CLAUDE.md              ← Arbeitsregeln (Zitate, keine erfundenen Daten, Loop-Protokoll)
├── FLOW.md                ← Der Woche-1-Flow: ein /goal pro Schritt
├── kurs.md                ← Der geführte Woche-1-Kurs („Starte den Kurs“)
├── context/               ← Firma und Strategie
├── input/                 ← 10 Interviews
├── .claude/skills/
│   ├── prd-goal/          ← /prd-goal: PRD gegen 14 Kriterien, mit Prüfern und Anzeigetafel
│   │   ├── criteria.md    ← die 14 Kriterien
│   │   ├── skeleton.md    ← das Gerüst (nur Überschriften)
│   │   ├── reviewers.md   ← die Prüferrollen
│   │   └── scripts/check_prd.py  ← das Prüfskript
│   ├── quote-check/       ← /quote-check: prüft jedes Zitat gegen die Interviews
│   └── ...                ← die Woche-1-Skills (interview-analysis, needs-synthesis, prd-writer, …)
└── output/
    ├── experiment-prd/    ← der Versuch: Varianten O, A, B, C, D mit allen Prüfberichten
    │   ├── vergleich-template-vs-kriterien.md  ← alle Ergebnisse
    │   └── scoreboard.md                       ← die Anzeigetafel
    └── ...                ← Ergebnisse des Woche-1-Flows (Analysen, Synthese, PRD)
```

`.claude` ist ein versteckter Ordner. Im Finder: `Cmd+Shift+.` zeigt ihn an. Im Explorer: Ansicht → Ausgeblendete Elemente.

---

## Loslegen

Die drei Stufen aus der Lektion, kurz:

**Stufe 1: `/goal`**

```
/goal Schreibe einen PRD auf Basis der neuesten Synthese in output/, bis abgewogen und dokumentiert ist, welches Bedürfnis die höhere Wahrscheinlichkeit wirtschaftlichen Erfolgs hat. Jedes Zitat steht wörtlich in input/, und /quote-check meldet 0 NICHT BELEGT.
```

**Stufe 2: eigene Prüfer.** Den Prompt dafür findest du in der Lektion.

**Stufe 3: der ausgebaute Loop als Skill**

```
/prd-goal
```

Oder mit `/goal` von außen bewacht:

```
/goal Führe /prd-goal mit Blindentwurf aus, bis die Anzeigetafel in einer Runde 14/14 zeigt, höchstens 4 Runden. Zeig mir am Ende die Anzeigetafel und die offene Liste.
```

---

## Hinweis: Nutzung

Stufe 2 und 3 starten viele Subagenten und verbrauchen spürbar mehr Kontingent als ein einzelner Prompt. Wer sparen will, liest zuerst die Ergebnisse in `output/experiment-prd/` und lässt nur Stufe 1 laufen.

---

## Probleme?

- Claude findet die Dateien nicht → richtigen Ordner geöffnet? Der, in dem direkt `CLAUDE.md` liegt.
- `/prd-goal` wird nicht erkannt → Session im Ordner neu starten, damit die Skills geladen werden.
- `/goal` hört nicht auf → Bedingung zu weich oder unerreichbar formuliert. Mit `Esc` abbrechen und das Goal schärfer formulieren.
- Bei allem anderen: Nachricht an Markus, oder im nächsten Call fragen.
