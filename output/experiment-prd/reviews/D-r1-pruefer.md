# Faktenprüfer: Runde 1, PRD D (`output/experiment-prd/D-PRD.md`)

Geprüft gegen `.claude/skills/prd-goal/criteria.md` (v2), `input/` (10 Interviews), `context/strategy.md`, `context/company.md`, Skriptausgabe `D-r1-skript.txt`, Kunden-Einwände `D-r1-kunde.md`. Andere PRDs und Reviews wurden nicht gelesen.

## C3: Keine erfundenen Zahlen

Die 8 Skript-Treffer habe ich nachgerechnet:

| Zeile | Zahl | Herkunft | Urteil |
|---|---|---|---|
| 21 | 13 bis 20 PT | A1 (3–5) + A2 (10–15) | berechnet aus Annahmen ✅ |
| 42 | 24 Min. | 4 Std. / 10 Kontakte (Chen) | berechnet ✅ |
| 187 | 7 Tage | Green: "in the last week" | belegt ✅ |
| 228 | 33 bis 50 PT | A1 + A2 + A3 = 3+10+20 / 5+15+30 | berechnet ✅ |
| 291 | 24 / 23 | 19+2+3 / 18+3+2 | berechnet ✅ |
| 292 | 25 / 21 | 19+3+3 / 18+1+2 | berechnet ✅ |
| 301 | 25, 26 (und 20, 23) | K7 für B1 von 1 auf 2 → 20; +2+3 = 25; +3+3 = 26; G-d 20+1+2 = 23 | berechnet ✅ |

Weitere Zahlen: 15/40/30/20 Min. (Thorne, O'Neil, Green, Ross), 50 und 20 Calls, 40 % (Jenkins), 40 % des Tagesziels (20/50), 5 von 100 (Blunt), 6 Monate (Chen), 90 % / 9 von 10 (Kim, O'Neil), 14 und 2 Personen (strategy.md), zwölf (Ross: "A dozen"), $80k (Kim-Zitat), 48 bis 75 PT (33+15 / 50+25), 9 von 10 und 5 von 10 (mit Namen aufgezählt, an den Interviews nachvollziehbar). Alle Aufwände, Teamgröße, Zeitfenster, Gültigkeit, Wortzahl, Laufzeit und Skala stehen im Block „Annahmen (nicht belegt)“ (A1–A12) mit Begründung und Ersatz-Messwert, im Fließtext nur mit Verweis. Geld: nur `[Platzhalter]`. **✅**

## C5: Problem breit belegt

Der Problem-Abschnitt zitiert wörtlich Thorne, O'Neil, Jenkins, Green, Ross, Chen, Petit, Blunt, Baker (9 Personen). Budgetverantwortung: Blunt, "We spend serious budget—my budget—getting these people into the funnel" (Interview 05, wörtlich), dazu Thorne als VP of Sales. Stichproben aller Zitate in `input/` gefunden. **✅**

## C6: Wahl begründet und robust

8 benannte Kriterien (K1–K8), beide Bedürfnisse bewertet, jede Bewertung begründet. 4 Gewichtungen (G-a bis G-d) plus Variante „B1 mit Rollen-Check“ durchgerechnet, alle Summen stimmen. Ergebnis benannt („Wir wählen Bedürfnis 1 mit Rollen-Check“). Schicksal des Verlierers ausdrücklich: Rollen-Check als MVP-Baustein, voller CRM-Abgleich als Phase 2 / eigenes Angebot, mit Kipp-Bedingungen (A.5). Hinweis ohne Abwertung: Die Variante hebt nur B1 an (K7 1→2), B2 bleibt unverändert; das ist offengelegt. **✅**

## C7: Strategie nachgewiesen

- S1: „we pursue any revenue-generating opportunity that fits within our vision of building AI agents that replace employee skills“ steht wörtlich in strategy.md, Begründung vorhanden.
- S2: „anything that brings in money and aligns with our vision, we do.“ und „every deal we close extends how long we can operate and invest in the product path“ wörtlich, Begründung vorhanden.
- S3: „These patterns are the seeds of future products: non-custom, reusable agents built on real-world demand rather than speculation.“ wörtlich, Begründung inkl. Einschränkung (nur ein Kunde).
**✅**

## C8: Alternativen ernsthaft

Drei Lösungsalternativen (Signal-Feed ohne Synthese, vollautomatische Ansprache, vorhandene Tools ausbauen). Ausschlussgründe: O'Neil-Zitat; Petit- und Green-Zitat; S1 plus Kim-Zitat. Alle Zitate wörtlich in `input/`. **✅**
Nebenbefund (kein ❌): Die Alternativen heißen A1–A3, genau wie die Annahmen A1–A3. „33 bis 50 Personentage (A1 + A2 + A3)“ ist dadurch missverständlich. Umbenennen (z. B. L1–L3).

## C9: Narrativ echt

Vorher-Szenen gegen `input/` geprüft:
- Jenkins: Salesforce, dann LinkedIn, ~40 % weg, Nachfolger suchen, Titel kopieren, 20 statt 50 Calls → Interview 01 ✅
- Green: 30 Min., Sauerteig-Thread, Mail; sonst generisches LinkedIn-Like → Interview 07 ✅
- Chen: 4 Std. abends, 10 Leute, drei Erweiterungen zum E-Mail-Raten → Interview 03 ✅
- Baker: Artikel des Kunden nicht gekannt → Interview 04 ✅
- Thorne: geht an Tischen vorbei, "a black box" → Interview 08 ✅ (sinngemäß: er sagt "on the internet", nicht „Browser-Tabs“; Tabs stammen von Ross; sinngemäß tragbar)
Nachher-Szenen sind ausdrücklich *illustrativ* markiert. **✅**

## C10: Ziele messbar

Z1–Z4: Kennzahl, Ausgangswert (Interview plus `[Platzhalter: messen in Woche 1]`), Messzeitpunkt vorhanden. Guardrails G1 und G2 vorhanden. N1–N3: Kennzahl, Ausgangswert, Zeitpunkt vorhanden.
**Fehler:** Z5 (Nutzung) hat als Ausgangswert „neue Funktion, kein Ausgangswert“. Das ist weder ein Interviewwert noch `[Platzhalter: messen in Woche 1]`. Streng nach „Erfüllt, wenn“ → ❌. Behebung: „0 (Funktion existiert nicht)“ oder Platzhalter. (G2 hat dasselbe Muster, Guardrails verlangen laut Kriterium aber keinen Ausgangswert.) Nebenbefund: Z1 misst den Ausgangswert in „Woche 1 des Pilots“, also nachdem die Pilotgruppe schon Dossiers hat; der Ausgangswert müsste vor Start oder an der Vergleichsgruppe gemessen werden. **❌**

## C11: Abgrenzung klar

Alle 7 Nicht-Ziele haben „Warum nicht“ und „Wohin“ (Phase 2, nie, anderer Auftrag, Pattern-Team nach N3). **✅**
Nebenbefund: „Einigung Marketing und Sales → Anderer Auftrag (kein Agent-Projekt)“ widerspricht leicht S1 („We do not chase work outside that frame“); passender wäre „nie (außerhalb unseres Rahmens)“.

## C13: Einwände beantwortet

| Einwand | Antwort im PRD | Urteil |
|---|---|---|
| **K1** LinkedIn-Zugriff erst klären; was taugt das Dossier ohne LinkedIn? | E1 als **offenes Risiko** markiert, Prüfung in Phase 1 vor dem Pilot, Start ohne LinkedIn-Adapter (Offene Punkte 1, R16), „funktioniert auch ohne LinkedIn … dann mit mehr `unklar`-Status“. | ✅ formal als offenes Risiko beantwortet. Lücke: Reihenfolge bleibt „Rechtsprüfung parallel zu Phase 1“, wie vom Kunden kritisiert; der Wert ohne LinkedIn wird nicht beziffert, obwohl Rollen-Check und Anlässe laut Kim ("It’s 90% LinkedIn.") daran hängen. |
| **K2** Welche Trefferquote muss der Pilot zeigen, wer prüft sie, was passiert bei Verfehlen? Quelle neben jedem Anlass = Nachprüfaufwand. | E2 sagt „Beantwortet; Fehlerquote wird im Pilot gemessen“. G2 misst den Anteil als falsch markierter Anlässe, hat aber **keine Schwelle**. Phase 1 nennt „Fehlerquote in Stichprobe“ ohne Schwelle und ohne Prüfer. Nachprüfaufwand durch Quellen wird nicht behandelt. | ❌ weder beantwortet noch als offen markiert |
| **K3** Pipeline-Wirkung statt Aktivität (Antwortrate, Meetings, Pipeline pro SDR gegen Kontrollgruppe); Käufer unklar; Preis Platzhalter. | Budget: E8 offenes Risiko ✅. Preis: E7 offen ✅. Pipeline: G1 misst „Antworten oder Termine pro Kontaktversuch“ gegen Vergleichsgruppe, aber nur als Guardrail („darf nicht schlechter werden“), kein Ziel, kein Pipeline-/Opportunity-Wert pro SDR, und nicht als offen markiert. | ❌ teilweise: Pipeline-Ziel fehlt |

**❌**

## Ergebnis

| Kriterium | ✅/❌ | Begründung in einem Satz | Was konkret fehlt |
|---|---|---|---|
| C3 | ✅ | Alle Zahlen sind belegt, nachvollziehbar berechnet (alle 8 Skript-Treffer nachgerechnet) oder Annahmen A1–A12 im Annahmen-Block; Geld nur als Platzhalter. | nichts |
| C5 | ✅ | Wörtliche Zitate von 9 Personen, darunter Blunt mit "my budget" und der VP of Sales. | nichts |
| C6 | ✅ | 8 begründete Kriterien, 4 Gewichtungen plus Variante korrekt gerechnet, Ergebnis benannt, Verlierer mit Schicksal (MVP-Baustein und Phase 2). | nichts |
| C7 | ✅ | S1, S2, S3 sind je mit wörtlichem Satz aus strategy.md und Begründung belegt. | nichts |
| C8 | ✅ | Drei echte Lösungsalternativen, jede mit Ausschlussgrund aus Interview oder Strategie. | nichts (Empfehlung: Alternativen A1–A3 umbenennen, Kollision mit Annahmen A1–A3) |
| C9 | ✅ | Alle Vorher-Szenen stehen in den Interviews, Nachher-Szenen sind als *illustrativ* markiert. | nichts |
| C10 | ❌ | Z5 hat als Ausgangswert „kein Ausgangswert“ statt Interviewwert oder `[Platzhalter: messen in Woche 1]`. | Ausgangswert für Z5 (z. B. „0, Funktion existiert nicht“); Ausgangsmessung für Z1 vor Pilotstart bzw. an der Vergleichsgruppe |
| C11 | ✅ | Jedes Nicht-Ziel nennt Grund und Ziel (Phase 2, nie, anderer Auftrag, Pattern-Team). | nichts (Empfehlung: Marketing/Sales-Einigung als „nie“ statt „anderer Auftrag“) |
| C13 | ❌ | K1 ist als offenes Risiko beantwortet, K2 (Trefferquote) und der Pipeline-Teil von K3 sind weder belegt beantwortet noch als offen markiert. | K2: Mindest-Trefferquote für Anlässe und Rollen-Check, wer sie prüft, was bei Verfehlen passiert (oder als offenes Risiko markieren). K3: Pipeline-Ziel (Antwortrate, gebuchte Meetings, Opportunities pro SDR gegen Vergleichsgruppe) als Ziel statt nur Guardrail. K1 (Empfehlung): Rechtsprüfung vor das Go für Phase 1 ziehen und den Wert ohne LinkedIn benennen. |
