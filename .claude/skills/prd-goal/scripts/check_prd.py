#!/usr/bin/env python3
"""Mechanische Prüfung eines PRD gegen die SKRIPT-Kriterien C1, C2, C3.

Aufruf (aus dem Kursordner):
    python3 -I .claude/skills/prd-goal/scripts/check_prd.py output/DATEI.md

C1  Gerüst: alle Überschriften aus skeleton.md vorhanden und nicht leer
C2  Zitate: ruft quote-check auf (0 NICHT BELEGT)
C3  Zahlen: listet Zahlen, die weder in input/ noch in context/ stehen,
    nicht in [Platzhalter] stehen und nicht im Block "Annahmen (nicht belegt)"
    stehen oder auf eine Annahme verweisen ("Annahme A2", "(A2)").
    Zahlen, die nur im Fließtext als Schätzung markiert sind, werden mit
    [nur Fließtext] gelistet: nach Datenregel v2 ein ❌.
    Die Liste ist ein Hinweis, die Entscheidung trifft der Faktenprüfer.
Ausgeklammert wird alles ab der Überschrift "Loop-Protokoll".
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKELETON = os.path.join(HERE, "..", "skeleton.md")
QUOTE_CHECK = os.path.join(HERE, "..", "..", "quote-check", "scripts", "verify_quotes.py")
MARKED = re.compile(r"schätz|geschätzt|ca\.|etwa|rund|assum|estimat", re.I)
ASSUMPTION_REF = re.compile(r"Annahme\s+A\d+|\(A\d+\)|\bA\d+:", re.I)
ASSUMPTION_BLOCK = re.compile(r"Annahmen\s*\(nicht belegt\)", re.I)


def norm_heading(h):
    h = re.sub(r"\[.*?\]", "", h)
    h = re.sub(r"[^\wäöüß ]", " ", h.lower())
    return re.sub(r"\s+", " ", h).strip()


def skeleton_headings():
    text = open(SKELETON, encoding="utf-8").read()
    block = re.search(r"```\n(.*?)```", text, re.S).group(1)
    out = []
    for line in block.splitlines():
        m = re.match(r"^(#+)\s+(.*)$", line.strip())
        if m:
            out.append((len(m.group(1)), norm_heading(m.group(2))))
    return out


def check_c1(lines):
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#+)\s+(.*)$", line)
        if m:
            heads.append((i, len(m.group(1)), norm_heading(m.group(2))))
    problems = []
    for level, name in skeleton_headings():
        hit = [h for h in heads if h[2].startswith(name)]
        if not hit:
            problems.append(f"fehlt: {'#' * level} {name}")
            continue
        i, lvl, _ = hit[0]
        end = next((h[0] for h in heads if h[0] > i and h[1] <= lvl), len(lines))
        body = "".join(lines[i + 1:end]).strip()
        if not body and "loop" not in name:
            problems.append(f"leer: {'#' * level} {name}")
    return problems


def check_c3(body_lines):
    src = ""
    for f in glob.glob("input/*.md") + glob.glob("context/*.md"):
        src += open(f, encoding="utf-8").read().lower()
    src_nums = set(re.findall(r"\d+(?:[.,]\d+)?", src))
    found = []
    in_block = False
    for n, line in enumerate(body_lines, 1):
        if ASSUMPTION_BLOCK.search(line):
            in_block = True
            continue
        if line.lstrip().startswith("#"):
            in_block = False
            continue
        if in_block or ASSUMPTION_REF.search(line):
            continue
        tag = "[nur Fließtext] " if MARKED.search(line) else ""
        clean = re.sub(r"\[[^\]]*\]", "", line)                  # Platzhalter
        clean = re.sub(r"\b[A-Z]{1,2}\d+\b", "", clean)            # Kürzel wie C3, L4, O8, A2
        clean = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", "", clean)       # Datumsangaben
        clean = re.sub(r"\b\d{1,2}:\d{2}\b", "", clean)             # Uhrzeiten
        clean = re.sub(r"\b(Woche|Week|Phase|Runde|Durchgang|Anhang|Schritt)\s*\d+(\s*[–-]\s*\d+)?", "", clean, flags=re.I)
        clean = re.sub(r"^\s*\d+\.\s", "", clean)                 # Listennummern
        clean = re.sub(r"^\s*\|\s*\d+\s*\|", "|", clean)          # Tabellen-Nummernspalte
        for num in re.findall(r"\d+(?:[.,]\d+)?", clean):
            if num in src_nums or num in {"0", "1", "2", "3"}:
                continue
            found.append((n, num, tag + line.strip()[:110]))
    return found


def main():
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines(keepends=True)
    body = re.split(r"^#+ .*Loop-Protokoll.*$", text, maxsplit=1, flags=re.M)[0]

    c1 = check_c1(lines)
    q = subprocess.run([sys.executable, "-I", QUOTE_CHECK, path, "--sources", "input", "context"],
                       capture_output=True, text=True)
    c3 = check_c3(body.splitlines())

    print(f"PRD: {path}\n")
    print(f"C1 Gerüst: {'✅' if not c1 else '❌'}")
    for p in c1:
        print("   -", p)
    summary = next((l for l in q.stdout.splitlines() if l.startswith("belegt:")), "")
    print(f"C2 Zitate: {'✅' if q.returncode == 0 else '❌'}  ({summary})")
    if q.returncode:
        print("\n".join("   " + l for l in q.stdout.split("NICHT BELEGT,")[-1].splitlines()[1:]))
    print(f"C3 Zahlen ohne Fundstelle: {len(c3)} (Hinweis für den Faktenprüfer)")
    for n, num, ctx in c3:
        print(f"   Z.{n}: {num}  | {ctx}")
    sys.exit(0 if not c1 and q.returncode == 0 else 1)


if __name__ == "__main__":
    main()
