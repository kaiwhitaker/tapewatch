# Monitor #1 — candidate pools (pick 10)
Built: July 5, 2026 · Purpose: playbook Step 1, weeks 1–2. This is the candidate slate with selection evidence. THE PICK IS YOURS (never-tier: published judgment). I've flagged a suggested 10 but every inclusion/exclusion call is a judgment call you should make against methodology v0.1.

Selection criteria (from methodology draft): span big/small, span platforms (Morpho / Maple / Centrifuge / standalone), span asset classes (fintech receivables, corporate credit, CLO, high-yield bonds, crypto-native secured), include at least one levered structure, include at least one fresh launch, all analyzable from public data.

## Candidates

| # | Pool / asset | Platform | Type | Size (approx, per public sources) | Why it's Monitor-worthy | Suggested |
|---|---|---|---|---|---|---|
| 1 | mF-ONE (Midas × Fasanara F-ONE) | Morpho (collateral market) | Fintech receivables + SME + RE-backed credit, tokenized certificate | ~$107–190M depending on date/measure | Leading RWA market on Morpho; ~33% of tokens posted as collateral; 10% instant-liquidity sleeve, socialized not pro-rata — redemption-vs-duration mismatch is a textbook Monitor section | YES |
| 2 | sACRED (Securitize × Apollo Diversified Credit) | Morpho/Compound Blue (Polygon), levered via Gauntlet | Multi-asset corporate credit feeder, LEVERED loop | ~$131M (rwa.xyz Feb 2026) | The levered-RWA archetype: loop of borrow-USDC-buy-more; unwind logic set by curator. Leverage-on-illiquid-credit = drift watchlist by construction | YES |
| 3 | Maple Blue Chip Secured | Maple | Overcollateralized institutional loans | Maple TVL ~$2.1B protocol-wide | Baseline "clean" candidate; collateral schedules onchain | YES |
| 4 | Maple High Yield Secured | Maple | Institutional loans, concentrated collateral | [TBD — pull from Maple/rwa.xyz] | Concentration analysis showcase | YES |
| 5 | syrupUSDC | Maple | Permissionless yield token over institutional credit | ~$1B+ (syrupUSDT listed at ~$1.01B June 2026; syrupUSDC comparable) | Retail-wrapped institutional credit; the transparency question ("what's actually inside syrup?") is high-engagement | YES |
| 6 | BlockTower structured-credit pool | Maple (and Centrifuge history) | Corporate lending vs receivables/equipment | [TBD] | Real structured credit, real credit shop — tests whether the methodology holds up beyond crypto-native collateral | YES |
| 7 | A Centrifuge fintech-receivables pool (pick largest active) | Centrifuge | Invoice/trade receivables, senior/junior tranches | Centrifuge active loans mid-hundreds of $M | Tranching + originator risk; Codex Finance default is the historical case study for the asset class | YES |
| 8 | NYLIM HYB | Centrifuge | Tokenized US high-yield bond fund (BVI, Reg S, USDC settle) | New (launched June 30, 2026) | Freshest launch in the space; "near-instant redemptions" via Fission liquidity facility vs bond-market settlement = exactly the redemption-liquidity flag the Monitor exists for | YES |
| 9 | JAAA (Janus Henderson AAA CLO, via Centrifuge/Anemoy ecosystem) | Centrifuge | Tokenized AAA CLO | ~$720M (rwa.xyz Feb 2026) | In Ethena USDe reserves — systemic linkage story; AAA tranche framing vs actual liquidity | YES |
| 10 | Steakhouse High Yield USDC vault | Morpho | Curated vault WITH RWA collateral exposure (siUSD, mF-ONE) | [TBD — Morpho app] | The meta-layer: a curated stablecoin vault whose yield comes partly from private-credit collateral markets. Mandate-vs-composition analysis showcase | YES |
| 11 | Pareto FalconX Credit Vault (AA_FalconXUSDC) | Morpho (collateral) | Credit vault token, up to 77% LTV at launch | [TBD] | High LTV on private credit; alternate pick if any of 1–10 falls out on data availability | Alternate |
| 12 | Goldfinch borrower pool (largest active) | Goldfinch | Emerging-market unsecured fintech debt | [TBD] | Highest structural opacity in the set; Tugende default history | Alternate |
| 13 | Wildcat v-wmtUSDC | Wildcat | Wintermute-backed undercollateralized credit | [TBD] | Crypto-native undercollateralized; niche but loud audience | Alternate |
| 14 | An Anemoy treasury pool | Centrifuge | Tokenized T-bills | ~$1B (Janus Henderson Anemoy Treasury Fund) | Control-group "CLEAN" anchor — but low information value; include only if you want a calibration baseline | Alternate |

## Rationale for the suggested 10
- **Platforms:** 3 Morpho-linked (1, 2, 10), 4 Maple (3–6), 3 Centrifuge (7–9).
- **Asset classes:** receivables, corporate direct lending, structured/CLO, high-yield bonds, crypto-native secured, retail wrappers.
- **Structures:** one levered (2), one meta-vault (10), one brand-new (8), tranched (7, 9).
- **Deliberate exclusions:** pure treasury pools (low signal), anything requiring non-public data for even a first pass.

## Data-pull plan per pool (playbook Step 2)
- **Dune:** fork existing public queries per protocol (search "Morpho", "Maple", "Centrifuge" in Dune's query library) — don't write from scratch. Free tier: 2,500 credits.
- **rwa.xyz:** per-asset pages give total value, NAV, mint/burn volumes, holders, 7D APY (mF-ONE page confirmed to have all five tabs).
- **Protocol docs:** Maple pool pages publish collateral schedules; Centrifuge pool pages publish originator, NAV, senior/junior APY, transparency dashboard; Midas publishes the mF-ONE liquidity-sleeve design; Morpho markets show LTV/oracle config.
- **Watch for:** NAV cadence and who computes it; oracle design (mF-ONE uses Fasanara NAV → eOracle → Steakhouse discount — a three-party chain worth mapping); redemption terms vs. asset duration; concentration disclosures or their absence.

## Open questions for your pick session
- Include a control-group CLEAN pool (14) or keep all 10 high-signal?
- Issue #1 lead finding candidates: (a) redemption-liquidity design across the set (HYB's Fission facility vs mF-ONE's 10% sleeve vs Maple queues), or (b) the oracle/NAV chain-of-custody map. Both are impersonal, methodology-based, no-accusation framings consistent with the research-publisher posture.
