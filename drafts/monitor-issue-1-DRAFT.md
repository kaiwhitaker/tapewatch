# The Tokenized Credit Monitor — Issue #1

**[DRAFT v2, refreshed 2026-10-10. Grades signed off by Kaï on 2026-10-10, except rows 3 and 4, which were relabeled after sign-off and need his call. Data: 2026-10-10 snapshot, compared against the 2026-07-05 reference pull; both committed in data/snapshots/, every figure from scripts/metrics.py. The July draft (v1) is in git history.]**

*Surveillance for tokenized private credit. Free, monthly, methodology in the appendix. We watch the tape so you don't have to reconcile it at 2am.*

---

## The finding that leads this issue

Eleven months after Stream Finance, the structural pattern that turned a $93M loss into $285M of mapped exposure (yield tokens redeposited as collateral across other lending protocols) is running at about 2.4x that mapped figure on the largest pool in tokenized credit, and it grew over the past three months.

- **The number:** $689M of Maple's syrup tokens sit as supplied assets inside Aave v3 ($345M), Morpho Blue ($219M), Kamino ($59M) and Aave v4 ($51M). That is 19.7% of Maple's $3.50B USDC and USDT pools.
- **Three months ago:** $635M, or 15.0% of $4.23B (2026-07-05 pull). The share rose for two reasons, and both are on the tape: the redeposited amount grew $54M, and the home pools shrank $732M. Morpho Blue alone went from $138M to $219M.
- **Against:** $40.2M of DEX exit liquidity across syrupUSDC and syrupUSDT pairs, 1.15% of the home pools (July: $53.9M, 1.27%).
- **What this is not:** Stream. Maple's book is overcollateralized institutional lending with published delegates, and Maple exited its own DeFi lending positions within 24 hours of the April 18 rsETH incident. The risk process demonstrably works. This is a structure observation, not a solvency observation.
- **Why it still matters:** rehypothecated supply means redemption behavior is partly governed by liquidation engines Maple doesn't control. In stress, about a fifth of the book unwinds on Aave's and Morpho's parameters, not on Maple's withdrawal queue. Nobody publishes that consolidated exposure. That's the gap this Monitor exists to fill.

**Grade: WATCH.** Not for credit quality: the consolidated rehypothecation footprint is unmonitored by anyone, as far as public disclosure shows, and it is growing as a share of the book.

---

## The tape, October 2026

All figures from the 2026-10-10 snapshot (scripts/metrics.py). On-chain T-bill benchmark: Midas mTBILL, 3.73% (July: 3.12%). Grades in Issue #1 are **baseline grades only**. DRIFT is a trend verdict that requires a prior issue to drift *from*, so it is unavailable until Issue #2. The July column is a pre-launch reference pull, shown as fact, not as a graded baseline.

| # | Instrument | Platform / manager | TVL Oct (Jul) | APY | Spread vs mTBILL | Grade |
|---|-----------|--------------------|-----|-----|------------------|-------------|
| 1 | syrupUSDC pool | Maple | $2,820M ($3,186M) | 5.21% | +148bp | WATCH |
| 2 | syrupUSDT pool | Maple | $682M ($1,048M) | 5.53% | +180bp | WATCH |
| 3 | JTRSY (Treasury fund; USDS share class) | Janus Henderson / Centrifuge | $326M ($871M) | 3.63% | −10bp | [Kaï: re-decide; T-bill fund, see note] |
| 4 | JAAA (AAA CLO fund) | Janus Henderson / Centrifuge | $592M across share classes ($690M) | [TBD]ᵇ | [TBD] | [Kaï: grade] |
| 5 | STAC (AAA CLO fund) | Securitize | $104M ($102M) | 3.49% | **−24bp** | WATCH |
| 6 | ACRED / sACRED | Apollo / Securitize | $79.5M on-chain ($96.7M) | [TBD]ᵃ | [TBD] | WATCH |
| 7 | mF-ONE | Midas / Fasanara | $65.8M ($72.6M) | 7.60% | +387bp | WATCH |
| 8 | Goldfinch Prime | Goldfinch | Wound down ($37M) | — | — | Exits the tape |
| 9 | Huma V2 (PayFi) | Huma | [TBD] ($187M) | 7.62% (Morpho mkt) | +389bp | CLEAN |
| 10 | Maple USDG pool | Maple | $503M ($99M) | 4.95% | +122bp | CLEAN |

ᵃ DefiLlama lists ACRED at 0.00% on every chain in this pull; zero-APY listings are excluded per our footnote convention.
ᵇ Sources disagree: DefiLlama lists 6.28%; rwa.xyz shows a 30-day APY of 3.06%. TVL agrees across both: $592M (DefiLlama, sum of Centrifuge share classes) and $589M (rwa.xyz, 2026-10-10).

**Tape changes:** Goldfinch Prime exits. Goldfinch token holders passed GIP-87 in June 2026, putting the protocol in maintenance mode and winding Prime down, with existing Prime investors fully redeemed (Goldfinch governance forum; The Block, June 2026). A replacement enters only at the next issue boundary, per the universe rule.

[Kaï, before publishing: rows 3 and 4 were mislabeled in the July draft by their settlement stablecoin. DefiLlama's poolMeta and rwa.xyz both identify them as Janus Henderson funds. Row 3 is JTRSY, a tokenized Treasury fund: a yield just under the T-bill benchmark is expected after fees, so the negative spread isn't a finding, and the universe rule covers credit instruments, which suggests it leaves the tape. Row 4 is JAAA, a AAA CLO fund. Its July AUSD share class ($371M) is gone; a USAT share class ($296M) appeared. Whether one replaced the other is unconfirmed. Huma V2's total (row 9) is also unconfirmed; the row stands on the Morpho market figure.]

CLEAN means: no anomaly surfaced under this issue's five lenses at current disclosure depth. It is not an endorsement; disclosure depth varies widely.

---

## Three sections worth your time

### 1. ACRED: a quarterly-tender fund living a block-by-block life

Apollo's tokenized Diversified Credit feeder holds $79.5M on-chain across **six chains** in this pull: Ethereum ($28.8M), Solana ($18.3M), Sei ($15.6M), Ink ($11.1M), Avalanche ($4.9M), Polygon ($0.9M). In July it was $96.7M across the same six.

- **The structure:** ACRED wraps into sACRED, accepted as collateral on Morpho (Gauntlet-curated vaults, RedStone NAV feeds) for USDC borrowing that loops back into more ACRED, capturing the spread between fund yield and stablecoin borrow rates.
- **The mismatch:** the underlying is an interval fund, so redemptions are periodic tenders. The borrowing on top is liquidatable continuously. If positions sour, the liquidator receives an asset it cannot promptly redeem. That question was raised publicly at launch and, per available disclosure, still has no published backstop. [TBD: current Gauntlet vault parameters and liquidation-buyer arrangements — Dune + Gauntlet docs.]
- **The fragmentation angle:** six chains means six oracle deployments and six liquidity surfaces for one NAV.

**Grade: WATCH.** Structure, not manager. Apollo's underlying book is not the question; the wrapper's stress mechanics are.

### 2. STAC: when a AAA CLO fund prints below T-bills, check the oracle before the credit

The Securitize tokenized AAA CLO fund prints 3.49%, **24bp below the on-chain T-bill benchmark**. In July it printed 19bp below. AAA CLO paper does not yield less than T-bills in a functioning market.

- **Most likely explanation:** the figure is share-price-derived over a trailing window, and NAV update cadence is distorting the annualization. Not a credit event.
- **Why it's still a finding:** a routine metrics API has now produced a below-risk-free print for a AAA instrument in two pulls three months apart, and nothing in the disclosure stack flags it. NAV observability, not asset quality, is the weak layer. An allocator screening on published APY would wrongly exclude the fund, or stop trusting the category's numbers.
- **What resolves it:** NAV timestamp history against price-feed history. [TBD Issue #2: the fund's oracle update log — a two-hour Dune job.]

**Grade: WATCH.** A data-integrity watch, explicitly not a credit watch. We flag anomalies; we don't speculate on causes we haven't verified.

### 3. mF-ONE: the spread compressed, the disclosure questions didn't

Fasanara's mF-ONE via Midas: $65.8M at 7.60%, +387bp over T-bills. In July: $72.6M at 12.85%, +973bp.

- **The honest framing:** fintech-lending private credit at high single digits to low teens is normal in TradFi. Neither print is suspicious in itself.
- **What the spread buys you the right to ask:** loan count, top-10 borrower concentration, weighted average life against the token's redemption terms, delinquency roll rates. Fasanara publishes more than most; the question is whether on-chain disclosure keeps pace with off-chain fund reporting. [TBD: side-by-side of Midas on-chain disclosures vs. the Fasanara factsheet.]
- **What moved:** the headline yield fell 525bp in three months while TVL fell 9%. The pull doesn't say why. [TBD: Fasanara fund reporting on the yield change.]

**Grade: WATCH.** A disclosure-depth watch. Sharpens if TVL grows >50% before the questions above are answerable from public sources.

---

## Quick notes on the rest of the tape

- **JTRSY ($326M in the USDS share class, down from $871M):** a tokenized Treasury fund, not credit. rwa.xyz shows its total down 55% in the last 30 days, to $345M. The pull doesn't show whose capital left. [Kaï: grade or drop from the tape; see the note under the table.]
- **Maple USDG ($503M, up from $99M):** a fivefold increase in three months. Standard Maple underwriting posture. CLEAN at baseline; growth this fast is worth a note in Issue #2's tape changes.
- **Huma V2:** the Morpho HUMAUSDC market is $12.8M at 7.62% (July: $15.8M at 4.48%) and bears watching only as a rehypothecation seed. [TBD: Huma V2 total from a second source.]

## What we said → what happened

Starts in Issue #2. Every grade above is on the record as of this issue; the next issue reports against it. That ledger, not any single teardown, is the product.

## If a pool you hold isn't on this tape

Private surveillance: $2,500, loan-level teardown of any pool you name, memo in 5 business days. Reply to this email.

---

## Methodology appendix (v0.2 — full version in the repo)

**Universe:** tokenized credit instruments ≥$15M on-chain observable supply, ≥4 platforms, ≥3 structure types, cap 12; rule frozen per issue.
**Five lenses:** concentration; redemption terms vs. asset duration; NAV cadence & observability; mandate vs. composition; rehypothecation footprint.
**Grades:** CLEAN / WATCH / DRIFT as defined above. Grades are opinions about observability and structure, formed from public data, stated with their evidence.
**Data:** DefiLlama yields and protocol APIs (2026-10-10 snapshot, with a 2026-07-05 reference pull; both committed), protocol documentation, public disclosures. Instruments matched across pulls by DefiLlama pool id. Dune loan-level queries begin Issue #2. All figures reproducible; query set available on request.
**Source note:** between the two pulls DefiLlama relabeled Midas listings and stopped reporting protocol-level totals for several RWA platforms. Where our source has no October figure, this issue says [TBD] rather than estimating.
**What this is not:** investment advice, a rating, or an accusation. We analyze structures and disclosures, not intentions. We publish facts and methodology-based opinions about pools; we do not make recommendations to any person about any investment. Errors flagged to us get corrected in the next issue, prominently.

— Kaï
