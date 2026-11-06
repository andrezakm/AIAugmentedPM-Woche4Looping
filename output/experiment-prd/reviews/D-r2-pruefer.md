# D-PRD, Runde 2: Faktenprüfer

Geprüft: `output/experiment-prd/D-PRD.md` gegen `criteria.md` (v2), `input/`, `context/`, Skript-Lauf `D-r2-skript.txt`.
Kriterien: C3, C5–C11, C13 (Abgleich).

## 1. Bestätigung der Vorrunden-✅ (C3, C5–C9, C11)

Keine Änderung gefunden, die eines dieser Kriterien bricht.

- **C3 Zahlen:** Die 7 Skript-Hinweise sind alle aufgelöst:
  - Z.42 „24 Min. pro Kontakt“: berechnet aus Chens "4 hours a night just building a list of 10 people" (240 / 10).
  - Z.188 „7 Tage“: Umsetzung von Greens "in the last week" (Interview_Gen_07); „6 Monaten“ steht wörtlich bei Chen ("less than 6 months").
  - Z.229 „33 bis 50“: A1 + A2 + A3 = 3+10+20 bzw. 5+15+30. Ebenso nachgerechnet: 48–75 (+A5 15–25), 9–10 Wochen (A1 1–2 + A2 2 + A3-Aufbau 2 + A4 4), „bis zu 20 PT“ (A1 + A2 = 5+15).
  - Z.307/308/317 „24, 25, 26“: Gewichtungssummen in Anhang A.2/A.3 nachgerechnet, alle korrekt (G-b 24/23, G-c 25/21, G-d 21/23; Variante 20/18, 25/23, 26/21, 23/23).
  - Übrige Zahlen belegt: 15 Min./4 pro Stunde (Thorne), 40 Min. (O'Neil), 30 Min. (Green), 20 Min. (Ross), 50/20 Calls und 40 % (Jenkins), 5 von 100 (Blunt), $80k (Kim), „a dozen“ (Ross), 2 von 14 (strategy.md), „under two minutes“ (O'Neil). Aufwände und Startwerte stehen als A1–A14 im Annahmen-Block, jede mit Begründung und Ersetzungszeitpunkt. Geld ist durchgehend `[Platzhalter]`.
- **C5:** Problem mit wörtlichen Zitaten von 8 Personen belegt, Budget: Blunt ("my budget"), dazu VP Thorne. Zitate stichprobenartig in input/ gefunden, Skript meldet 0 NICHT BELEGT.
- **C6:** 8 benannte Kriterien mit Begründung je Bedürfnis, 4 Gewichtungen durchgerechnet und benannt, Schicksal von B2 (MVP-Baustein Rollen-Check + Phase-2-Angebot) ausdrücklich.
- **C7:** S1, S2, S3 je wörtlich in strategy.md gefunden (S2 dort fett gesetzt, Wortlaut identisch), je mit Begründung.
- **C8:** 3 Lösungsalternativen (L-A, L-B, L-C), Ausschlussgründe auf O'Neil, Thorne, Petit, Green, Kim bzw. S1 gestützt.
- **C9:** Vorher-Szenen alle in input/ (Jenkins LinkedIn-Check/40 %/Titel kopieren; Green Sauerteig, 30 Min., „Digital Transformation“-Like; Chen 4 Std., drei Extensions; Baker Artikel; Thorne „black box“). Nachher ist *illustrativ* markiert.
- **C11:** Jedes Nicht-Ziel hat Warum und Wohin (Phase 2 / nie / anderer Auftrag / Pattern-Team).

## 2. Offene Punkte der Vorrunde

| Punkt | Stand | Begründung und Stelle |
|---|---|---|
| **P1** C10: Z5 ohne Ausgangswert | *erledigt* | Z5 hat jetzt „0 (Funktion existiert nicht)“ (*Ziele*, Zeile Z5); ebenso G2. |
| **P2** C10: Ausgangswert Z1 erst in Woche 1 des Piloten | *erledigt* | Z1 misst die Vergleichsgruppe (nie mit Dossier) und die Pilotgruppe in der Woche vor Pilotstart; Messzeitpunkt „vor Pilotstart, Woche 1 und Ende“ (*Ziele*, Einleitungssatz und Zeile Z1); zeitlich gedeckt durch die 2 Wochen Aufbau in A3. |
| **P3** C8 (Hinweis): Alternativen hießen wie Annahmen | *erledigt* | Alternativen heißen jetzt L-A, L-B, L-C (*Lösung › Alternativen*), Verweise in Nicht-Zielen und E6 angepasst. |

## 3. C13: Kunden-Einwände

| Einwand | Stand | Begründung und Stelle |
|---|---|---|
| **K1** LinkedIn-Zugriff, Rechtsprüfung vor Go Phase 1, Wert ohne LinkedIn | *erledigt* | Rechtsprüfung in Phase 0 als Go-Bedingung für Phase 1 (Kurzfassung (a), *Plan* Phase 0, E1, Offene Punkte 1); Wert ohne LinkedIn benannt (Firmen-Anlässe, Rollen-Check oft `unklar`), Phase 1 misst beide Anteile mit/ohne LinkedIn (R16, E1, *Plan* Phase 1); als **offenes Risiko** markiert. |
| **K2** Mindest-Trefferquote, wer prüft, was bei Verfehlen | *erledigt* | Schwelle `[Platzhalter]` legt der Kunde in Phase 0 fest; NeoEmployee prüft in Phase 1 von Hand an 50 Dossiers (A14), im Pilot die Nutzer über R14/G2; Verfehlen: einschränken und einmal nachmessen, sonst Stopp bzw. Kategorie abschalten, ohne Erholung kein Rollout (E2, *Plan* Phase 1 und 2). |
| **K3** Pipeline-Ziel gegen Vergleichsgruppe; wer kauft | *erledigt* | Z6 (Meetings und Opportunities pro SDR, Pilot gegen Vergleichsgruppe, Opportunities mit Nachmessung A4) als Ziel, das „der Kunde zahlt“; Antwortrate gegen Vergleichsgruppe als G1; Käuferfrage in Phase 0, E8 als **offenes Risiko**, Umkehr A.5. |

## 4. Neuer Punkt

Keiner. Kein Kriterium ist durch einen neuen Fund klar ❌.

## Hinweise, nicht bewertet

1. **Z1-Zielwert dehnt O'Neils Marke:** O'Neils "under two minutes" bezieht sich auf das *Finden* der drei Dinge; Z1 misst aber bis zum *ersten Kontaktversuch* (inkl. Schreiben). „unter 2 Min. (O'Neils eigene Marke)“ ist damit strenger als die Quelle. Entweder Kennzahl auf „Zeit bis Anlass gefunden/Dossier gelesen“ zuschneiden oder Zielwert als `[Platzhalter]` mit O'Neils Marke als Bezug.
2. **„Phase 2“ doppelt belegt:** *Plan* nennt den Pilot „2: Pilot“ und zugleich „Phase 2 (Option)“ für CRM-Abgleich/Account-Karte/Listenbau. E3 („Testnutzer in Phase 2“ = Pilot) und Nicht-Ziele („Phase 2“ = Option) meinen Verschiedenes. Gleiches Muster wie P3; Umbenennen (z. B. „Folgeangebot“) empfohlen.
3. **K2-Formulierung leicht uneinheitlich:** Kurzfassung „Wird sie verfehlt, gibt es keinen Pilot“, *Plan* Phase 1 erlaubt einmal Einschränken und Nachmessen. Kein Widerspruch, aber die Kurzfassung sollte die Nachmess-Option nennen.
4. **Antwortrate nur als Guardrail:** Der Kunde wollte die Antwortrate als Ziel; der PRD führt sie als G1 („darf nicht schlechter werden“). Bewusste Wahl, vertretbar; ggf. in E7 einen Halbsatz dazu.
5. **„7 Tage“ aus "last week"** ist eine Umsetzung, kein wörtlicher Wert; korrekt, aber man könnte es als Startwert in den Annahmen-Block (neben A7) legen.

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 | ✅ | Alle Zahlen belegt, nachgerechnet (Summen, Gewichtungen, Wochen) oder als A1–A14 bzw. `[Platzhalter]` geführt. | nichts |
| C5 | ✅ | Wörtliche Zitate von 8 Personen, Budget bei Blunt ("my budget"). | nichts |
| C6 | ✅ | 8 Kriterien mit Begründung, 4 Gewichtungen korrekt gerechnet, Schicksal B2 ausdrücklich. | nichts |
| C7 | ✅ | S1–S3 je wörtlich aus strategy.md mit Begründung. | nichts |
| C8 | ✅ | Drei Lösungsalternativen L-A bis L-C mit belegtem Ausschlussgrund; P3 erledigt. | nichts |
| C9 | ✅ | Alle Vorher-Szenen in input/ gefunden, Nachher als *illustrativ* markiert. | nichts |
| C10 | ✅ | P1 (Z5 = 0) und P2 (Z1 vor Pilotstart und an der Vergleichsgruppe) erledigt; jedes Ziel hat Kennzahl, Ausgangswert, Messzeitpunkt, Guardrails G1/G2. | nichts (Hinweis 1 zum Z1-Zielwert) |
| C11 | ✅ | Jedes Nicht-Ziel mit Warum und Wohin. | nichts (Hinweis 2 zur Doppelbelegung „Phase 2“) |
| C13 | ✅ | K1–K3 beantwortet, LinkedIn und Käufer als offene Risiken markiert, Trefferquote mit Prüfer und Folge bei Verfehlen. | nichts |
