# Surveillance Methodology — v0.2
Change log: v0.1 drafted during Monitor Issue #1 session (2026-07-05).
v0.2 (2026-07-06): universe rule fixed BEFORE data inspection, per process-log
lesson. Amendments to the universe rule are logged here and take effect at the
NEXT issue boundary — never mid-analysis.

## Universe rule (frozen per issue)
- Tokenized credit instruments with ≥$15M on-chain observable supply.
- Must span ≥4 platforms and ≥3 structure types (pool / feeder fund / CLO fund
  / PayFi-receivables).
- Per platform: include the largest instruments meeting the floor, max 3.
- Universe cap: 12 instruments per issue. Entrants added only at issue
  boundaries; exits reported in a "tape changes" note.

## Five lenses (applied per instrument, every issue)
1. Concentration — borrower/allocator concentration where tape data permits.
2. Redemption terms vs. asset duration — continuous exit promises against
   periodic-liquidity underlyings.
3. NAV cadence & observability — how often marks update on-chain; whether
   derived metrics (APY) can mislead.
4. Mandate vs. composition — what the wrapper claims vs. what flows show.
5. Rehypothecation footprint — where the instrument's tokens reappear as
   collateral elsewhere; consolidated cross-venue exposure.

## Grades
- CLEAN: no anomaly surfaced under the five lenses at current disclosure depth.
  Not an endorsement.
- WATCH: a named, checkable question is open. Every WATCH must state what
  observation would resolve it.
- DRIFT: a metric moved against a prior issue's baseline. Trend verdict —
  unavailable in an instrument's first issue on the tape.

## Severity × confidence (paid teardowns; lightweight version in Monitor)
- Severity: S1 structural (could impair principal) / S2 material (could impair
  liquidity or pricing) / S3 informational (disclosure/data quality).
- Confidence: C1 verified on-chain or in primary docs / C2 single-source or
  inferred / C3 hypothesis needing data we've requested.
- Monitor WATCH items carry [S,C] tags from Issue #2 onward.

## Data rules
- Any number driving a verdict needs two independent sources.
- Record the counting convention next to every market-size figure.
- APY figures are point-in-time API reads; footnote convention: (a) supply-side
  listings showing 0.00% are excluded, (b) share-price-derived APYs flagged.
- Every issue's raw pulls are committed to data/snapshots/ — the time series
  IS the DRIFT verdict's evidence base.

## Legal posture (verbatim, every issue)
Research publication. Facts and methodology-based opinions about pools and
structures; no investment advice, no ratings, no accusations of intent.
Errors flagged to us are corrected in the next issue, prominently.
