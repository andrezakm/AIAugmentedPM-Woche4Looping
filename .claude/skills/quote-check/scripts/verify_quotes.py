#!/usr/bin/env python3
"""Prüft, ob die Zitate in einem Markdown-Dokument wörtlich in den Quellen stehen.

Aufruf (aus dem Kursordner):
    python3 -I .claude/skills/quote-check/scripts/verify_quotes.py output/DATEI.md
    python3 -I .claude/skills/quote-check/scripts/verify_quotes.py output/DATEI.md --sources input context

Was als Zitat gilt:
  - Text in "…" (englische Anführungszeichen), z. B. Interview-Zitate
  - Text in „…" (deutsche Anführungszeichen), z. B. Strategie-Zitate
  - Blockzitate, die mit > " beginnen
Beide Arten werden GETRENNT ausgewertet. Gemischt erzeugen sie falsche Treffer.

Normalisiert werden typografische Anführungszeichen, Apostrophe, Gedankenstriche,
Leerraum und Groß-/Kleinschreibung. Die Satzzeichen-Form zählt also nicht, der Wortlaut schon.
Zitate mit Auslassung (… oder ...) werden in Teile zerlegt, jeder Teil wird einzeln geprüft.

Ausgeklammert wird alles ab einer Überschrift, die "Loop-Protokoll" enthält.
Dort stehen Fehlzitate absichtlich, als Dokumentation.

Ergebnis:
  belegt          – steht wörtlich in einer Quelle
  eigene Worte    – deutscher Text oder Label in Anführungszeichen (kein Zitat), Kontrolle per Auge
  NICHT BELEGT    – muss korrigiert werden: Originalwortlaut einsetzen oder als *kursive Umschreibung* ohne Anführungszeichen schreiben
Exit-Code 1, wenn etwas nicht belegt ist.
"""
import argparse
import glob
import os
import re
import sys

ENGLISH_HINT = re.compile(
    r"\b(the|a|an|to|of|and|it|its|it's|is|are|was|in|on|you|we|i|they|no|not|my|for|that|this|with|be|do|don't|can|just|what|who|half)\b"
)
GERMAN_HINT = re.compile(
    r"[äöüß]|\b(der|die|das|und|nicht|keine?|warum|grund|zum|mehr|statt|für|auf|ist|sind|wir|ein|eine|mit)\b"
)


def normalize(text: str) -> str:
    text = re.sub(r"[‘’‚‛“”„\"'*`]", "", text)
    text = re.sub(r"[—–\-]+", "-", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def load_sources(paths):
    chunks = []
    for p in paths:
        files = [p] if os.path.isfile(p) else glob.glob(os.path.join(p, "**", "*.md"), recursive=True)
        for f in sorted(files):
            with open(f, encoding="utf-8") as fh:
                chunks.append(fh.read())
    return normalize("\n".join(chunks))


def extract_quotes(body: str):
    german = re.findall(r"„([^“\"\n]+)[“\"]", body)
    rest = re.sub(r"„[^“\"\n]+[“\"]", " ", body)
    english = re.findall(r"[\"“]([^\"“”\n]{4,}?)[\"”]", rest)
    return german + english


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("document")
    ap.add_argument("--sources", nargs="+", default=["input", "context"])
    ap.add_argument("--min-len", type=int, default=6)
    args = ap.parse_args()

    with open(args.document, encoding="utf-8") as fh:
        doc = fh.read()
    body = re.split(r"^#+ .*Loop-Protokoll.*$", doc, maxsplit=1, flags=re.M)[0]
    src = load_sources(args.sources)

    ok, own, missing = 0, [], []
    for q in extract_quotes(body):
        for part in re.split(r"…|\.\.\.", q):
            part = part.strip(" .,;:…")
            if len(part) < args.min_len:
                continue
            n = normalize(part)
            if n in src:
                ok += 1
            elif GERMAN_HINT.search(n) or not ENGLISH_HINT.search(n):
                own.append(part)
            else:
                missing.append(part)

    print(f"Dokument: {args.document}")
    print(f"Quellen:  {', '.join(args.sources)}")
    print(f"belegt: {ok} | eigene Worte (kein Zitat): {len(own)} | NICHT BELEGT: {len(missing)}")
    if own:
        print("\nEigene Worte in Anführungszeichen (prüfen, ob sie wie ein Zitat einer Person wirken):")
        for o in own:
            print("  -", o)
    if missing:
        print("\nNICHT BELEGT, Originalwortlaut suchen oder als *kursive Umschreibung* ohne Anführungszeichen schreiben:")
        for m in missing:
            print("  -", m)
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
