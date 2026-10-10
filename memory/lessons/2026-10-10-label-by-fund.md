## 2026-10-10 — Name instruments by fund, not settlement token
- Centrifuge pools carry their fund in DefiLlama's poolMeta; the symbol is the
  settlement stablecoin. The July draft's "USDS vault" was JTRSY (a Treasury
  fund) and its "AUSD vault" was JAAA (a AAA CLO fund). Same trap as the
  Midas relabel.
- The mislabel led to a WATCH grade on a T-bill fund for yielding just under
  T-bills, which is expected after fees. Check what a pool holds before
  reading its spread.
- Follow-up: the negative-spread check in metrics.py should skip Treasury
  funds.
