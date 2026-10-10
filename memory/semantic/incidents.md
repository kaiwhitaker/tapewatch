# Incident registry — append-only. Never re-research these; cite this file.

## Stream Finance / xUSD (Oct 30 – Nov 2025)
- $93M loss by an external manager; xUSD depegged (~$1 → ~$0.10–0.26); withdrawals
  frozen (~$160M user deposits). Mapped debt exposure ≈ $285M across 7 networks (YAM).
- Curator exposures reported: TelosC ~$124M, Elixir $68M (65% of deUSD backing,
  private Morpho markets), MEV Capital ~$25M, Re7 ~$14.65M xUSD Euler vault + more.
- Mechanism: recursive looping / cross-minting with Elixir; ~$1.9M USDC spun into
  ~$14.5M xUSD. Oracle hardcoded ~$1.26 while market price collapsed → liquidations
  never fired (MEV Capital USDC market bad debt).
- Context: Balancer exploit ($128M, Nov 3) adjacent; DeFiLlama had disputed
  Stream's self-reported TVL ($200M vs claimed $520M).
- Aftermath: curator-vault TVL fell ~$10.3B → ~$7.5B in days; "risk curator"
  model under fire; Steakhouse/Gauntlet (no exposure) reputationally up.
- Why it matters to us: THE reference event for lenses 3 & 5. Post-Stream,
  NAV observability and rehypothecation are what the market is primed to read.

## rsETH-adjacent exploit (Apr 18, 2026)
- Compromised-collateral event; Maple had no direct exposure (rsETH never
  approved by its Risk Committee); indirect via Aave V3/Mantle exited within
  24h; later unwound all DeFi lending positions, redeploying to
  overcollateralized institutional loans. Evidence Maple's risk process works —
  cite when framing WATCH as structure-not-solvency.

## Balancer exploit (Nov 3, 2025) — ~$128M. Contagion vector into Stream loss.

## Goldfinch Prime wind-down (June 2026)
- GIP-87 passed (token-holder vote, June 2026): Goldfinch to maintenance mode,
  Prime wound down, existing Prime investors fully redeemed; $150K USDC to
  Warbler Labs for wind-down services. A trust under a chief restructuring
  officer pursues recoveries on legacy borrower pools.
- Legacy pools: ~$56M outstanding against ~$1.6M TVL per DefiLlama as cited
  by secondary coverage (single-source; verify before using in a verdict).
- Sources: gov.goldfinch.finance GIP-87 thread (primary); The Block, June 2026.
- Why it matters to us: Goldfinch Prime was on the Issue #1 tape (July draft,
  $37M). It exits in Issue #1's tape-changes note.
