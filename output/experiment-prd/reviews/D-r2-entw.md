# Review D, Runde 2: Entwickler (C12 „Logik ist baubar")

Gelesen: `D-ausschnitt-logik.md`, `D-ausschnitt-offene-punkte.md`. Sonst nichts.

## Prüfung der offenen Punkte aus der Vorrunde

**E1 Oberfläche (F12): erledigt.** Statt einer statischen Notiz gibt es jetzt ein eigenes Dossier-Objekt und eine Komponente mit den Knöpfen *Dossier erzeugen*, *Neu erzeugen* und *falsch* je Anlass. „Geöffnet" heißt: Die Komponente wird mit sichtbarem Dossier geöffnet, das schreibt einen Eintrag in `geoeffnet[]`. Für den Fall ohne Objekt-Freigabe nennt OP 3 die Folge: R14, Z5 und G2 sind dann nicht messbar. (Lösung „Wo es landet", R12, R14, R15, OP 3)

**E2 Hinweis-Feld vs. „nie überschreiben" (F11): erledigt.** `rollen_hinweis` liegt jetzt im Dossier-Datensatz, nicht am Kontakt, und der Testfall verlangt einen leeren Feld-Diff. (R12, Datenmodell)

**E3 Stapel-Erkennung, Arbeitsbeginn (F13): erledigt.** Erkennung: offene Aufgaben des Nutzers, die am nächsten Arbeitstag fällig sind. Arbeitsbeginn wird je Nutzer konfiguriert, Startwert A13. Für Verspätung gibt es ein Verhalten, und der Testfall grenzt morgen gegen übermorgen ab. (R17, OP 6)

**E4 Dossier ohne LinkedIn (F16): erledigt.** Ohne LinkedIn liefert das Dossier die Firmen-Anlässe. Die Kopfzeile meldet *LinkedIn nicht geprüft*. Findet keine Quelle die Person, gilt `unklar` mit Warnhinweis. (R16, R2 (1), R4, OP 1)

**E5 R2 widersprüchlich (F1): erledigt.** Die Prüfreihenfolge ist jetzt fest: Die erste zutreffende Zeile gilt. Widersprüchliche Quellen werden vor `gewechselt` geprüft. Für beide Fälle gibt es einen Testfall. (R2)

**E6 Null-Fall vs. R12 (F9): erledigt.** `null_fall` wird im Dossier-Datensatz gesetzt, ausdrücklich „nicht am Kontakt". Der Testfall verlangt, dass die Kontaktfelder unverändert bleiben. (R9, Datenmodell)

**E7 Felder fehlen (F17): erledigt.** Das Datenmodell enthält jetzt `status` mit `Eingabe unvollständig` (R1), `null_fall` (R9), `rollen_hinweis` (R12) und `falsch_markiert[]` mit `nutzer` und `zeit` (R14). (Datenmodell)

**E8 Nicht blockierende Fragen fehlen unter Offene Punkte: erledigt.** Unter Offene Punkte stehen jetzt 18 Fragen, jede mit Startannahme. Abgedeckt sind Datenquellen (1), Firmen- und Personen-Abgleich (7, 8), Nachfolger (9), Kategorien (11), Schwellen und Zeitfenster (12), R7-Prüfung (13), Kürzung (14) und Gültigkeit über Nutzer hinweg (15). (Offene Punkte)

## Neuer blockierender Punkt

Keiner. Jede Regel R1–R17 hat einen Testfall. Wo Werte fehlen (A7–A10, A13), sind es benannte, konfigurierbare Parameter. Dagegen lassen sich parametrisierte Tests schreiben.

## Hinweise, nicht bewertet

- **R15 und Datenmodell:** R15 verlangt, dass jede Erzeugung den Nutzer speichert. Im Datenmodell fehlt dafür ein Feld, etwa `erstellt_von`. Gleiches gilt für die Verspätungsmeldung aus R17. Beides lässt sich leicht nachtragen.
- **R2 bei Teiltreffern:** „Alle nennen" heißt vermutlich: alle Quellen, die die Person finden. So würde ich es bauen. Ein Satz im PRD würde das klarstellen.
- **R4 `unklar`:** Für welche Firma werden die Anlässe gesucht? Annahme: die Firma aus dem CRM. Das steht so nicht im Text.
- **R16 ohne LinkedIn:** `neue Rolle` und `Thema` fallen dann in der Praxis weg, weil nur LinkedIn Personendaten liefert. Das sollte ausdrücklich dastehen, damit niemand diese Kategorien als Fehler meldet.
- **R3 und R6:** Liegt der Wechsel mehr als 6 Monate zurück, verwirft R6 den Anlass `neue Rolle`. Das ist konsistent. Trotzdem lohnt sich ein Testfall dafür.
- **R13 mit R15:** Auch ein gespeichertes Dossier, das erneut angezeigt wird, löst einen `geoeffnet`-Eintrag aus. Das ist richtig, sollte aber als Testfall drinstehen.

## Ergebnis

| Punkt | erledigt/nicht erledigt | Begründung | Stelle |
|---|---|---|---|
| E1 | erledigt | Eigenes Objekt mit Komponente, Knöpfen und Öffnungs-Protokoll; Notiz-Fallback mit Folgen benannt | Lösung „Wo es landet", R12, R14, R15, OP 3 |
| E2 | erledigt | `rollen_hinweis` liegt im Dossier-Datensatz, Testfall verlangt leeren Feld-Diff am Kontakt | R12, Datenmodell |
| E3 | erledigt | Offene Aufgaben, fällig am nächsten Arbeitstag; Arbeitsbeginn je Nutzer (A13), Verspätung geregelt | R17, OP 6 |
| E4 | erledigt | Ohne LinkedIn: Firmen-Anlässe, Kopfzeilen-Hinweis, bei fehlendem Treffer `unklar` mit Warnhinweis | R16, R2 (1), R4 |
| E5 | erledigt | Feste Prüfreihenfolge, erste zutreffende Zeile gilt, Widerspruch kommt vor `gewechselt` | R2 |
| E6 | erledigt | `null_fall` im Dossier-Datensatz, Kontakt unverändert | R9 |
| E7 | erledigt | Felder für R1, R9, R12 und R14 im Datenmodell vorhanden | Datenmodell |
| E8 | erledigt | 18 nicht blockierende Fragen mit Startannahmen unter Offene Punkte | Offene Punkte 1–18 |

**Urteil C12: ✅** Jede Regel hat einen prüfbaren Testfall, und jede offene Frage hat eine Startannahme, mit der sich bauen lässt; keine blockiert den Bau.
