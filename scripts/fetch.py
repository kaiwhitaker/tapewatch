#!/usr/bin/env python3
"""Fetch public data snapshots for the Tokenized Credit Monitor.
Saves timestamped raw JSON to data/snapshots/. Run before every issue and on
Scout days if cheap. COMMIT every snapshot — the series is DRIFT's evidence."""
import json, urllib.request, datetime, pathlib

BASE = pathlib.Path(__file__).resolve().parents[1] / "data" / "snapshots"
STAMP = datetime.date.today().isoformat()
SOURCES = {
    "protocols": "https://api.llama.fi/protocols",
    "pools": "https://yields.llama.fi/pools",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "tapewatch-monitor/0.1"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def main():
    BASE.mkdir(parents=True, exist_ok=True)
    for name, url in SOURCES.items():
        out = BASE / f"{STAMP}-{name}.json"
        out.write_text(json.dumps(fetch(url)))
        print(f"saved {out.name} ({out.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
