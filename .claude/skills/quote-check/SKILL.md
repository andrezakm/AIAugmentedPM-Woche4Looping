---
name: quote-check
description: Prüft mechanisch, ob jedes Zitat in einem Dokument wörtlich in den Quellen (input/, context/) steht. Nutzen nach jedem Schritt, der Zitate schreibt (Synthese, PRD, Angebot), und immer, bevor ein Dokument als fertig gilt.
---

# Skill: Zitat-Check

## Zweck
KI-Texte enthalten oft Sätze in Anführungszeichen, die *fast* so im Interview stehen: umformuliert, verkürzt, mit anderer Groß-/Kleinschreibung oder sogar die Frage des Interviewers statt der Antwort. Inhaltlich meist richtig, als Zitat aber falsch. Das Skript findet sie.

## Aufruf
Aus dem Kursordner:
```
python3 -I .claude/skills/quote-check/scripts/verify_quotes.py output/DATEI.md
```
Standardquellen sind `input` und `context`. Andere Quellen mit `--sources`:
```
python3 -I .claude/skills/quote-check/scripts/verify_quotes.py output/DATEI.md --sources input
```

## Was das Skript tut
- Findet Text in "…" (englisch) und „…" (deutsch), **getrennt** voneinander
- Normalisiert typografische Anführungszeichen, Gedankenstriche, Leerraum, Groß-/Kleinschreibung
- Zerlegt Zitate mit Auslassung (…) in Teile und prüft jeden Teil
- Ignoriert alles ab der Überschrift „Loop-Protokoll", dort stehen Fehlzitate absichtlich als Dokumentation

## Ergebnis lesen
| Kategorie | Bedeutung | Was tun |
|---|---|---|
| belegt | steht wörtlich in einer Quelle | nichts |
| eigene Worte | deutscher Text oder Label in Anführungszeichen | kurz ansehen: Wirkt es wie ein Zitat einer Person? Dann *kursiv* ohne Anführungszeichen |
| NICHT BELEGT | englischer Text, der so nirgends steht | Originalwortlaut in `input/` suchen und einsetzen, **oder** als *kursive Umschreibung* ohne Anführungszeichen schreiben |

Exit-Code 1, wenn etwas NICHT BELEGT ist.

## Wichtig
- Nicht mit `sed` oder `grep` auf Unicode-Anführungszeichen prüfen. Die Bytes werden verstümmelt und **alle** Zitate erscheinen als fehlend. Ein solcher Lauf ist ungültig und wird im Loop-Protokoll als „verworfen" vermerkt.
- Ein NICHT BELEGT ist meist kein inhaltlicher Fehler, sondern ein Formfehler. Trotzdem korrigieren: Wer ein Zitat liest, prüft es im Original.
