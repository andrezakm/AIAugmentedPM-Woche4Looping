---
name: prototype
description: Baut aus dem PRD einen klickbaren HTML-Prototypen der einen Kerninteraktion und öffnet ihn im Browser. Optional, nach /prd-writer.
---

# Skill: HTML-Prototyp

## Zweck
Die eine Interaktion, die ein Stakeholder in 30 Sekunden anklickt und sofort versteht. Kein ganzes Produkt, kein Dashboard mit allen Features.

## Input
- Der neueste `output/PRD-*.md`
- `input/` für realistische Rollen, Situationen und Begriffe

## Vorgehen
1. Lies den PRD. Bestimme die **eine** Kerninteraktion (beim Signal-Brief-Agenten z. B.: Morgenliste öffnen → Brief zu einem Prospect aufklappen → Einstieg übernehmen).
2. Baue eine einzelne `.html`-Datei:
   - alles inline (CSS und JS), keine externen Abhängigkeiten
   - mindestens eine echte Aktion (Button, Eingabe, Aufklappen), die den Nutzen zeigt
   - plausible Beispieldaten aus dem Interview-Kontext, erkennbar erfunden (Example Corp, Jane Doe), keine echten Firmen oder Personen
   - kein Lorem Ipsum, alle Texte aus Produkt und Nutzerkontext
   - aufgeräumtes, bewusstes Design, kein Wireframe-Look
3. Speichern und öffnen:
   ```
   open output/prototype-[produktname]-[YYYY-MM-DD].html
   ```
   (Windows: `start`, Linux: `xdg-open`)

## Ablage
`output/prototype-[produktname-kebab-case]-[heute YYYY-MM-DD].html`

## Abbruchkriterium (für `/goal`)
Die Datei öffnet sich ohne Fehler, die Kerninteraktion funktioniert per Klick, und ein Außenstehender kann in 30 Sekunden sagen, was das Produkt tut.
