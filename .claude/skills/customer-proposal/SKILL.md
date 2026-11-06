---
name: customer-proposal
description: Macht aus dem internen PRD ein Angebot für den Kunden, in der Sprache des Kunden, ohne interne Inhalte, mit Leak-Check und einem Testleser in der Rolle des Entscheiders beim Kunden. Nutzen nach /stakeholder-review (Goal 5 im FLOW.md).
---

# Skill: Kundenangebot

## Zweck
Der PRD ist intern: Er spricht über unsere Strategie, unsere Marge, unseren Produktpfad. Der Kunde soll davon nichts sehen. Er soll sehen: *Ihr habt uns zugehört, ihr habt ein klares Angebot, ich weiß, was es kostet und wann ich aussteigen kann.*

## Input
- Der neueste `output/PRD-*.md`
- `input/` (Sprache, Rollen und Zitate des Kunden)

## Vorgehen

### 1. Sprache und Ansprache
- Sprache der Interviews (hier Englisch), adressiert an den Entscheider beim Kunden (die Person mit Budget, z. B. VP Sales)
- **Anonymisieren nach Rolle:** Außer dem Adressaten keine Namen von Interviewten. *Sales development*, *Enablement*, *Account executive* …
- Zitate nur, wenn wörtlich und nicht peinlich für die Person. Höchstens zwei, eines davon gern vom Adressaten selbst.

### 2. Aufbau
In short · What we heard from your team · What we propose (mit Beispiel-Brief, klar als *illustrativ* markiert) · What the agent does not do · How we would work (Wochenplan mit Entscheidungspunkt) · How we measure success · What we need from you · Data and compliance · Commercials · Possible next step (der Phase-2-Folgeauftrag) · Next steps · Kontakt

### 3. Was nicht hineingehört
Strategie (S1–S3, Vision-Filter, Brücke), Bewertungstabellen (K1–K7), Marge, interne Personenzahl, Produktpfad, Investorenargumente, die Namen anderer Kunden, das Loop-Protokoll.

### 4. Leak-Check
Grep auf das Angebot nach internen Begriffen und Namen, z. B.:
```
grep -n -i -E "strateg|vision|S1|S2|S3|K[1-7]|Brücke|bridge|bootstrap|runway|investor|margin|marge|loop|productiz|Jenkins|Ross|Chen|Baker|Blunt|Kim|Green|Petit|O'Neil" output/proposal-*.md
```
Jeder Treffer wird geprüft. Treffer, die erlaubt sind (z. B. der Name des Adressaten), bewusst stehen lassen.

### 5. Platzhalter statt Zusagen
Alles, was eine kaufmännische Zusage ist, wird `[Platzhalter]` oder als *Vorschlag* markiert: Tagessatz, Gesamtsumme, Deckel, Laufkosten, Hosting, Kontaktdaten, Versanddatum, Schwellenwerte für den Entscheidungspunkt. Diese Liste am Ende der Antwort an den Nutzer ausgeben: **Das muss ein Mensch entscheiden, bevor das Angebot rausgeht.**

### 6. Testleser
Ein Subagent in der Rolle des Adressaten (nur Angebot und Rolle, kein PRD). Er antwortet mit:
1. Urteil *nicht verständlich / verständlich mit Lücken / klar und überzeugend*
2. Was ihn zögern lässt
3. Was er vor der Unterschrift noch wissen will

Überarbeiten und neu testen (neuer Subagent), bis *klar und überzeugend*.

### 7. Prüfen
- `/quote-check` mit Quellen `input`. Ziel: 0 NICHT BELEGT, außer bewusst gesetzte Labels (z. B. eine UI-Beschriftung in Anführungszeichen), die beim Durchlesen bestätigt werden.
- Leak-Check ohne unerlaubte Treffer.
- Im PRD-Anhang einen Link auf das Angebot ergänzen.

## Ablage
`output/proposal-[produktname-kebab-case]-[heute YYYY-MM-DD].md`

Das Loop-Protokoll für diesen Schritt kommt **nicht** ins Angebot, sondern als neue Runde in den Anhang des PRD.

## Abbruchkriterium (für `/goal`)
Testleser in der Rolle des Entscheiders urteilt *klar und überzeugend*; Leak-Check sauber; Platzhalter-Liste an den Nutzer ausgegeben; Runde im Loop-Protokoll des PRD dokumentiert.
