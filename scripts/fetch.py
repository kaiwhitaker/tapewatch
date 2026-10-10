#!/usr/bin/env python3
"""Fetch public data snapshots for the Tokenized Credit Monitor.
Saves timestamped raw JSON (gzipped) to data/snapshots/. Runs weekly via
.github/workflows/snapshot.yml; run by hand before every issue too.
COMMIT every snapshot — the series is DRIFT's evidence."""
import datetime, gzip, json, pathlib, urllib.request

BASE = pathlib.Path(__file__).resolve().parents[1] / "data" / "snapshots"
SOURCES = {
    "protocols": "https://api.llama.fi/protocols",
    "pools": "https://yields.llama.fi/pools",
}
# A real pull has thousands of rows (2026-07-05: 7,778 protocols, 15,807
# pools). Anything far below that is an outage or error page, not data.
MIN_ROWS = 1000

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "tapewatch-monitor/0.1"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def check(name, data):
    """Refuse to save a pull that isn't a real dataset, so a bad API day
    never lands in the time series."""
    if name == "pools":
        if not isinstance(data, dict) or data.get("status") != "success":
            raise ValueError("pools: unexpected response shape or status")
        rows = data.get("data")
    else:
        rows = data
    if not isinstance(rows, list) or len(rows) < MIN_ROWS:
        n = len(rows) if isinstance(rows, list) else "no"
        raise ValueError(f"{name}: {n} rows, expected at least {MIN_ROWS}")

def save(name, data, base, stamp):
    """Write gzipped JSON. mtime=0 keeps the bytes identical for identical data."""
    base.mkdir(parents=True, exist_ok=True)
    out = base / f"{stamp}-{name}.json.gz"
    out.write_bytes(gzip.compress(json.dumps(data).encode(), mtime=0))
    return out

def main(base=BASE, sources=SOURCES):
    stamp = datetime.date.today().isoformat()
    pulled = {name: fetch(url) for name, url in sources.items()}
    for name, data in pulled.items():
        check(name, data)
    for name, data in pulled.items():
        out = save(name, data, base, stamp)
        print(f"saved {out.name} ({out.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
