#!/usr/bin/env python3
"""Named metric functions for the Monitor. RULE (lesson 2026-07-05): every
number printed in an issue comes from a function here — no ad-hoc calcs.
Usage: python3 scripts/metrics.py   (reads newest snapshot; compares to prior)"""
import gzip, json, pathlib

SNAP = pathlib.Path(__file__).resolve().parents[1] / "data" / "snapshots"
BENCHMARK_SYMBOL = "MTBILL"      # on-chain T-bill proxy
REHYPO_PREFIX = "SYRUP"          # tokens tracked for rehypothecation footprint
REHYPO_HOME_PROJECT = "maple"
UNIVERSE_PROJECTS = [            # keep in sync with methodology.md universe rule
    "maple", "centrifuge-protocol", "securitize-tokenized-aaa-clo-fund",
    "apollo-diversified-credit-securitize-fund", "midas-rwa", "goldfinch",
    "huma-finance-v2",
]  # morpho-blue excluded: its curated vaults are crypto-collateral lending, not
   # tokenized private credit (universe-rule bug caught in first run, 2026-07-05)

def load(name, offset=0, snap=SNAP):
    # Snapshots are .json (2026-07-05) or .json.gz (fetch.py since 2026-10).
    files = sorted(snap.glob(f"*-{name}.json*"), key=lambda f: f.name[:10])
    if len(files) <= offset:
        return None, None
    f = files[-(1 + offset)]
    raw = gzip.decompress(f.read_bytes()) if f.suffix == ".gz" else f.read_bytes()
    data = json.loads(raw)
    return (data.get("data", data)), f.name[:10]

def benchmark_apy(pools):
    """The Ethereum mTBILL instrument, specifically — one benchmark, not a max()
    over listings (bug caught in first run: max() picked a different chain's
    listing and flagged the benchmark against itself)."""
    for p in pools:
        if (p.get("symbol") == BENCHMARK_SYMBOL and p.get("chain") == "Ethereum"
                and p.get("project") == "midas-rwa" and (p.get("apy") or 0) > 0):
            return p["apy"]
    return None

def rehypo_footprint(pools):
    """$ of REHYPO_PREFIX tokens supplied inside OTHER protocols (not DEX pairs)."""
    return sum(p["tvlUsd"] for p in pools
               if REHYPO_PREFIX in (p.get("symbol") or "")
               and p.get("project") != REHYPO_HOME_PROJECT
               and "-" not in p.get("symbol", ""))

def dex_exit_liquidity(pools):
    """$ in DEX pairs (symbol contains '-') for REHYPO_PREFIX tokens."""
    return sum(p["tvlUsd"] for p in pools
               if REHYPO_PREFIX in (p.get("symbol") or "") and "-" in p.get("symbol", ""))

def home_pool_tvl(pools):
    return sum(p["tvlUsd"] for p in pools if p.get("project") == REHYPO_HOME_PROJECT
               and p.get("symbol") in ("USDC", "USDT"))

def chain_fragmentation(pools, symbol):
    rows = [(p["chain"], p["tvlUsd"]) for p in pools if p.get("symbol") == symbol]
    return sorted(rows, key=lambda x: -x[1])

def universe_rows(pools, floor=15_000_000):
    rows = [p for p in pools if p.get("project") in UNIVERSE_PROJECTS
            and p["tvlUsd"] >= floor and (p.get("apy") or 0) > 0]
    return sorted(rows, key=lambda x: -x["tvlUsd"])

def anomalies(pools, prev_pools=None):
    out, bench = [], benchmark_apy(pools)
    if bench:
        for p in universe_rows(pools):
            if p.get("symbol") == BENCHMARK_SYMBOL:
                continue
            if (p.get("apy") or 0) > 0 and p["apy"] < bench and p["tvlUsd"] > 50e6:
                out.append(f"NEGATIVE SPREAD: {p['project']}/{p['symbol']} "
                           f"{p['apy']:.2f}% vs benchmark {bench:.2f}% (NAV-observability flag)")
    home = home_pool_tvl(pools)
    if home:
        ratio = rehypo_footprint(pools) / home
        if ratio > 0.10:
            out.append(f"REHYPO >10%: {ratio:.1%} of {REHYPO_HOME_PROJECT} stable pools redeposited elsewhere")
    if prev_pools:
        # Key on DefiLlama's pool id: project/symbol/chain isn't unique (two
        # Centrifuge USDC pools on Base share it), which compared the wrong pools.
        prev = {p["pool"]: p["tvlUsd"] for p in prev_pools}
        for p in universe_rows(pools):
            k = p["pool"]
            if k in prev and prev[k] > 1e6:
                d = (p["tvlUsd"] - prev[k]) / prev[k]
                if abs(d) > 0.30:
                    name = f"{p['project']}/{p['symbol']}/{p['chain']}"
                    out.append(f"TVL MOVE {d:+.0%}: {name} [{k[:8]}] (${prev[k]:,.0f} -> ${p['tvlUsd']:,.0f})")
    return out

def main():
    pools, stamp = load("pools")
    if pools is None:
        raise SystemExit("no snapshot — run scripts/fetch.py first")
    prev, prev_stamp = load("pools", offset=1)
    bench = benchmark_apy(pools)
    home = home_pool_tvl(pools)
    rf, dex = rehypo_footprint(pools), dex_exit_liquidity(pools)
    print(f"== Monitor metrics — snapshot {stamp} (prior: {prev_stamp}) ==")
    print(f"benchmark ({BENCHMARK_SYMBOL}): {bench:.2f}%" if bench else "benchmark: MISSING")
    print(f"{REHYPO_HOME_PROJECT} USDC+USDT pools: ${home:,.0f}")
    print(f"rehypothecation footprint: ${rf:,.0f} ({rf/home:.1%} of home pools)")
    print(f"DEX exit liquidity: ${dex:,.0f} ({dex/home:.2%} of home pools)")
    print(f"\n-- universe (>=15M, APY>0) --")
    for p in universe_rows(pools)[:15]:
        sp = f"{(p['apy']-bench)*100:+.0f}bp" if bench else "n/a"
        print(f"{p['project'][:38]:38s} {p['symbol']:10s} {p['chain']:10s} "
              f"${p['tvlUsd']/1e6:8.1f}M  {p['apy']:6.2f}%  {sp}")
    print(f"\n-- auto-flagged anomalies --")
    for a in anomalies(pools, prev) or ["(none)"]:
        print(f"  * {a}")

if __name__ == "__main__":
    main()
