# Tapewatch surveillance methodology — v0.1 (SUPERSEDED — kept as draft record)
July 5, 2026 · Status: superseded by memory/semantic/methodology.md (v0.2, 2026-07-06). Do not cite thresholds or definitions from this file; it is retained only as the v0.1 draft record.

Legal posture (governs everything): research publication, not investment advice. Analysis is impersonal — pools, not portfolios. Findings are facts plus methodology-based opinions. No statements about anyone's intent. Grades describe observable structure and disclosure, not predictions of default.

## Scope
- **Unit of analysis:** a tokenized credit pool/fund/vault — the structure, its assets, its liquidity design, its disclosure surface.
- **Data:** public only — on-chain state, published NAVs, protocol dashboards, disclosed docs, servicer reports posted publicly, rwa.xyz/Dune/DefiLlama.
- **Cadence:** monthly full pass per covered pool; updates on previously flagged items every issue ("we said → what happened").

## The five blowup patterns (what surveillance looks for)
- **1 · Concentration:** single-borrower, single-originator, or single-collateral-type exposure above [TBD]% of pool; borrower overlap across pools (same name in multiple pools = correlated, not diversified).
- **2 · Duration/redemption mismatch:** redemption terms faster than asset self-liquidation. Instruments: instant-liquidity sleeves (size, pro-rata vs socialized), withdrawal queues, gates, liquidity facilities (and the facility's own capacity/counterparty).
- **3 · NAV/oracle integrity:** who computes NAV, how often, who verifies, what discount logic sits between NAV and on-chain price; divergence between posted NAV and any secondary/oracle price above [TBD]%.
- **4 · Mandate drift:** current composition vs. stated mandate — asset types, ratings buckets, geography, leverage. Includes leverage-by-construction (looped collateral strategies) even where each step is within stated parameters.
- **5 · Disclosure decay:** cadence slippage, dropped line items, servicer reports going stale, transparency dashboards not updating. Silence is a signal.

## Grades
- **CLEAN:** no pattern triggered on available data; disclosure sufficient to check all five.
- **WATCH:** one pattern triggered, or disclosure insufficient to check two or more patterns. WATCH is frequently a transparency grade, not a solvency claim — say so every time.
- **DRIFT:** two or more patterns triggered, or one pattern materially worsening across two consecutive issues.
- Every grade ships with one paragraph of reasoning and the data it rests on. Grades are Kaï's calls, made per pool, per issue. No grade is ever automated.

## Per-pool checklist (the 15 bullets, v0.1)
- **1.** Legal wrapper: entity, jurisdiction, exemption (Reg D/S), who token holders actually have a claim on.
- **2.** Asset class and origination model: who originates, who underwrites, who services.
- **3.** Top-5 exposure concentration ([TBD] if undisclosed — which is itself a finding).
- **4.** Borrower/originator overlap vs. other covered pools.
- **5.** Stated mandate (quote it) vs. current composition (show it).
- **6.** Leverage: in the pool, on the pool (collateral markets, looped strategies), and who controls unwind.
- **7.** NAV: computed by whom, cadence, verified by whom, last update timestamp.
- **8.** Oracle chain: every party between manager NAV and on-chain price; discount/haircut logic.
- **9.** Redemption design: terms, queues, sleeves (size + allocation rule), gates, facilities.
- **10.** Asset duration vs. redemption speed: the mismatch, stated plainly.
- **11.** Tranching: senior/junior split, who absorbs first loss, attachment points if disclosed.
- **12.** Disclosure surface: what's published, at what cadence, and what changed since last issue.
- **13.** Historical events: prior impairments/defaults in this pool or by this originator (facts + dates + sources only).
- **14.** Platform-level dependencies: protocol risk, curator/delegate role, what the platform can and cannot do in stress.
- **15.** Delta section: what changed since last issue; status of any prior flag.

## Severity × confidence (for teardowns, from academy Unit 4)
- **Severity:** LOW (cosmetic/disclosure) / MED (structural weakness, no near-term trigger) / HIGH (triggered pattern with plausible stress path).
- **Confidence:** LOW (inference from partial data) / MED (public data, some gaps) / HIGH (directly observable on-chain or in published docs).
- Every teardown finding carries both tags plus the data trail.

## Language rules (voice + legal, enforced in every draft)
- Facts get sources. Opinions get "on this methodology" framing. Nothing gets intent ("chose to hide" → "is not disclosed").
- No portfolio advice, ever — not even "holders should."
- Flag the structure, not the sponsor. Tag platforms in distribution, not the flagged pool's sponsor.

## Known v0.1 gaps [TBD]
- Thresholds for patterns 1 and 3 need calibration against the first 10-pool pass — set them after seeing real dispersion, not before.
- Cross-chain pools (hub-and-spoke like Centrifuge's) need a rule for which chain's state is canonical.
- How to grade levered wrappers (sACRED-style) vs. their underlying fund — one grade or two?
