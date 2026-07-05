#!/usr/bin/env python3
"""Pre-publication linter. Usage: python3 scripts/lint.py drafts/issue.md
Checks: banned words, intent-accusation phrases, required disclaimer,
DRIFT-grammar. Exit 1 on failure (block publish), warnings otherwise."""
import re, sys, pathlib

BANNED = ["leverage", "seamless", "robust", "innovative", "delve", "unpack",
          "moreover", "furthermore", "in conclusion"]
# 'leverage' the noun is unavoidable in credit writing; ban only verb-ish uses:
BANNED_PATTERNS = [r"\bleverag(?:e[sd]?|ing)\b(?!\s+(loop|ratio|multiple))"]
INTENT = ["fraud", "scam", "ponzi", "lying", "lied", "deliberately", "knowingly",
          "hiding", "concealed", "misleading investors", "cover-up"]
REQUIRED = ["investment advice", "methodology"]

def main(path):
    text = pathlib.Path(path).read_text().lower()
    fails, warns = [], []
    for w in BANNED:
        if w == "leverage":
            continue
        if re.search(rf"\b{re.escape(w)}\b", text):
            fails.append(f"banned word: {w}")
    for pat in BANNED_PATTERNS:
        if re.search(pat, text):
            fails.append(f"banned pattern: {pat}")
    for w in INTENT:
        # word-boundary match (v0.1 substring bug: flagged 'underlying'/'supplied')
        if re.search(rf"\b{re.escape(w)}\b", text):
            fails.append(f"intent-accusation language: '{w}' — rewrite as structural observation")
    for r in REQUIRED:
        if r not in text:
            fails.append(f"missing required disclaimer phrase: '{r}'")
    if "issue #1" in text and "drift" in text and "unavailable" not in text and "available in issue #2" not in text and "requires a prior" not in text:
        warns.append("DRIFT mentioned in Issue #1 — verify grammar rule (trend verdicts need a baseline)")
    for f in fails: print(f"FAIL: {f}")
    for w in warns: print(f"WARN: {w}")
    print("PASS" if not fails else f"{len(fails)} failures")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main(sys.argv[1])
