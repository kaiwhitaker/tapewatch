# The Tokenized Credit Monitor — Issue #1

**[DRAFT — every verdict requires Kaï's sign-off before publication. Data: 2026-07-05 snapshot, committed in data/snapshots/. PUBLISH GATE: PIIA review complete.]**

*Loan-level surveillance for tokenized private credit. Free, monthly, methodology in the appendix. We watch the tape so you don't have to reconcile it at 2am.*

---

## The finding that leads this issue

Eight months after Stream Finance, the structural pattern that turned a $93M loss into $285M of mapped exposure — yield tokens re-deposited as collateral across other lending protocols — is running again, at roughly 25x the scale, on the largest pool in tokenized credit.

- **The number:** $635M of Maple's syrup tokens sit as supplied assets inside Aave (Plasma, Mantle, Ethereum, Base, Monad), Morpho Blue, and Kamino — 15.0% of Maple's $4.2B stablecoin pools, redeposited one layer up the stack.
- **Against:** $53.9M of DEX exit liquidity across syrupUSDC/USDC and syrupUSDT/USDT pairs (Uniswap v4, Orca, Kamino) — 1.27% of supply.
- **What this is not:** Stream. Maple's book is overcollateralized institutional lending with published delegates, and Maple exited its own DeFi lending positions within 24 hours of the April 18 rsETH incident — the risk process demonstrably works. This is a structure observation, not a solvency observation.
- **Why it still matters:** rehypothecated supply means redemption behavior is partially governed by liquidation engines Maple doesn't control. In stress, 15% of the book unwinds on Aave's and Morpho's parameters, not on Maple's withdrawal queue. Nobody publishes that consolidated exposure. That's the gap this Monitor exists to fill.

**Draft verdict: WATCH** — not for credit quality, but because the consolidated rehypothecation footprint is unmonitored by anyone, as far as public disclosure shows. [Kaï: sign off / soften / sharpen.]

---

## The tape: 10 instruments, July 2026 baseline

All figures from the 2026-07-05 snapshot (scripts/metrics.py). On-chain T-bill benchmark: Midas mTBILL, 3.12%. Verdicts in Issue #1 are **baseline grades only** — DRIFT is a trend verdict and requires a prior issue to drift *from*; it becomes available in Issue #2.

| # | Instrument | Platform / manager | TVL | APY | Spread vs mTBILL | Draft grade |
|---|-----------|--------------------|-----|-----|------------------|-------------|
| 1 | syrupUSDC pool | Maple | $3,186M | 5.09% | +197bp | WATCH |
| 2 | syrupUSDT pool | Maple | $1,048M | 4.02% | +90bp | WATCH |
| 3 | USDS vault | Centrifuge (Sky allocation) | $871M | 5.35% | +223bp | CLEAN |
| 4 | AUSD vault | Centrifuge | $371M | 7.96% | +484bp | CLEAN |
| 5 | STAC (AAA CLO fund) | Securitize | $102M | 2.93% | **−19bp** | WATCH |
| 6 | ACRED / sACRED | Apollo / Securitize | $97M on-chain | 5.30% | +218bp | WATCH |
| 7 | mF-ONE | Midas / Fasanara | $73M | 12.85% | +973bp | WATCH |
| 8 | Goldfinch Prime | Goldfinch | $37M | 10.12% | +700bp | CLEAN |
| 9 | Huma V2 (PayFi) | Huma | $187M | 4.48% (Morpho mkt) | +136bp | CLEAN |
| 10 | Maple USDG pool | Maple | $99M | 4.86% | +174bp | CLEAN |

CLEAN means: no anomaly surfaced under this issue's five lenses at current disclosure depth — not an endorsement; disclosure depth varies widely.

---

## Three sections worth your time

### 1. ACRED: a quarterly-tender fund living a block-by-block life

Apollo's tokenized Diversified Credit feeder holds ~$97M on-chain across **seven chains** — Ethereum ($38.1M), Solana ($24.8M), Sei ($15.5M), Ink ($11.0M), Avalanche ($6.4M), Polygon ($0.9M), Sui ($0.3M).

- **The structure:** ACRED wraps into sACRED, accepted as collateral on Morpho (Gauntlet-curated vaults, RedStone NAV feeds) for USDC borrowing that loops back into more ACRED — capturing the spread between fund yield (~5.3% now; 8–9% at launch marketing) and stablecoin borrow rates.
- **The mismatch:** the underlying is an interval fund — redemptions are periodic tenders. The borrowing on top is liquidatable continuously. If positions sour, the liquidator receives an asset it cannot promptly redeem — a question raised publicly at launch and, per available disclosure, still without a published backstop. [TBD Issue #2: current Gauntlet vault parameters and liquidation-buyer arrangements — Dune + Gauntlet docs.]
- **The fragmentation angle:** seven chains = seven oracle deployments and seven liquidity surfaces for one NAV. Compressed yield also compresses the loop's margin for error: ~130–230bp over borrow costs before a single parameter moves.

**Draft grade: WATCH** — structure, not manager. Apollo's underlying book is not the question; the wrapper's stress mechanics are.

### 2. STAC: when a AAA CLO fund shows a negative spread, check the oracle before the credit

The Securitize tokenized AAA CLO fund prints 2.93% — **19bp below the on-chain T-bill benchmark**. AAA CLO paper does not yield less than T-bills in a functioning market.

- **Most likely explanation:** the figure is share-price-derived over a trailing window, and NAV update cadence is distorting the annualization — not a credit event.
- **Why it's still a finding:** if a routine metrics API can produce a below-risk-free print for a AAA instrument and nothing in the disclosure stack flags it, NAV observability — not asset quality — is the weak layer. An allocator screening on published APY would wrongly exclude the fund, or stop trusting the category's numbers.
- **What resolves it:** NAV timestamp history vs. price-feed history. [TBD Issue #2: the fund's oracle update log — a two-hour Dune job and the centerpiece of the first "we said → what happened" entry.]

**Draft grade: WATCH** — data-integrity watch, explicitly not a credit watch. We flag anomalies; we don't speculate on causes we haven't verified.

### 3. mF-ONE: 973bp of spread is a disclosure question, not a red flag

Fasanara's mF-ONE via Midas: $72.6M, 12.85% — the widest spread in our universe.

- **The honest framing:** fintech-lending private credit at 10–13% gross is normal in TradFi. The spread isn't suspicious in itself.
- **What the spread buys you the right to ask:** loan count, top-10 borrower concentration, weighted average life vs. the token's redemption terms, delinquency roll rates. Fasanara publishes more than most; the question is whether on-chain disclosure keeps pace with the off-chain fund reporting. [TBD Issue #2: side-by-side of Midas on-chain disclosures vs. Fasanara factsheet.]
- **The pattern to watch:** post-Stream, the market punishes opacity at exactly the moment yield gets attention. A 12.85% headline is an inflow magnet; inflows outpacing disclosure is the setup for every trust break this asset class has had.

**Draft grade: WATCH** — disclosure-depth watch. Sharpens if TVL grows >50% before the questions above are answerable from public sources.

---

## Quick notes on the rest of the tape

- **Centrifuge USDS/AUSD ($1.24B combined):** the quiet institutional workhorse; CLEAN under our lenses, with the caveat that a single-allocator base (Sky) is a redemption-concentration fact worth pricing.
- **Goldfinch Prime ($37M, 10.12%):** senior exposure to name-brand managers. CLEAN at baseline; small enough that one redemption cycle tells us more than any static analysis.
- **Huma V2 ($187M):** PayFi receivables — the healthiest duration profile on the tape. The Morpho HUMAUSDC market ($15.8M) bears watching purely as a rehypothecation seed.
- **Maple USDG ($99M):** standard Maple underwriting posture. CLEAN at baseline.

## What we said → what happened

Starts in Issue #2. Every verdict above is on the record as of today; next issue reports against it. That ledger — not any single teardown — is the product.

## If a pool you hold isn't on this tape

Private surveillance: $2,500, loan-level teardown of any pool you name, memo in 5 business days. Reply to this email.

---

## Methodology appendix (v0.2 — full version in the repo)

**Universe:** tokenized credit instruments ≥$15M on-chain observable supply, ≥4 platforms, ≥3 structure types, cap 12; rule frozen per issue.
**Five lenses:** concentration; redemption terms vs. asset duration; NAV cadence & observability; mandate vs. composition; rehypothecation footprint.
**Grades:** CLEAN / WATCH / DRIFT as defined above. Grades are opinions about observability and structure, formed from public data, stated with their evidence.
**Data:** DefiLlama protocol & yields APIs (2026-07-05 snapshot, committed), protocol documentation, public disclosures. Dune loan-level queries begin Issue #2. All figures reproducible; query set available on request.
**What this is not:** investment advice, a rating, or an accusation. We analyze structures and disclosures, not intentions. We publish facts and methodology-based opinions about pools; we do not make recommendations to any person about any investment. Errors flagged to us get corrected in the next issue, prominently.

— Kaï
