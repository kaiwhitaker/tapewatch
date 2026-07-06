# CLAUDE.md — entry map for the tapewatch repo

Tapewatch: independent, loan-level surveillance for tokenized private credit.
This repo is the company brain: memory, methodology, rubrics, session prompts,
scripts. Operating rules live in AGENTS.md — read it first, obey it.

## Start of every session
Read, in order:
1. memory/working/pipeline.md — live pipeline state
2. memory/working/gates.md — validation gates and kill-signals
3. The 3 newest files in memory/lessons/

## Entry map

### memory/semantic/ — slow-changing truth
- methodology.md — surveillance methodology, **v0.2, canonical**. Universe rule
  is frozen per issue; never re-derive mid-analysis.
- methodology-v0.1.md — superseded draft, kept as record. Do not cite.
- icp.md — who Tapewatch sells to.
- moats.md — why this business defends.
- voice.md — how everything is written.
- incidents.md — known incident history (xUSD/Stream etc.). Never re-research
  a known incident.
- outreach-templates.md — DM/reply skeletons, confirm-tier. Nothing sends
  without the real finding filled in, Kaï's edit, and Kaï's send.

### memory/working/ — fast-changing state
- pipeline.md — prospect/task pipeline. Updated via lesson.md diffs.
- gates.md — gate metrics; graded Fridays.
- tapewatch-list.md — curator/delegate/manager/analyst target list (v1,
  2026-07-05). Principals/handles marked [TBD] need Kaï's enrichment pass
  before any outreach.
- monitor-1-pool-shortlist.md — Monitor #1 candidate pools with selection
  evidence. The 10-pool pick is Kaï's alone (never-tier).

### memory/episodic/ — dated session logs, append-only
### memory/lessons/ — compound-loop output, one lesson per file

### prompts/ — paste-ready session prompts (2026-07-05 versions)
- morning-ops.md — Mon–Fri 7:45, 15 min cap.
- scout.md — Mon/Wed/Fri sweep, 10 min cap, web search on.
- friday-scorecard.md — Friday gates + evals, 30 min cap.
- lesson.md — end-of-day compound prompt, 10 min.
Note: sessions/ holds earlier scaffold variants of the same four routines
(Gmail/Calendar-integrated style). Kaï to consolidate; until then prompts/
is the paste-based set actually in use.

### Everything else
- rubrics/ — what good looks like (monitor, outreach, teardown); graded Fridays.
- protocols/permissions.md — auto/confirm/never tiers. Drafts are DRAFTS.
- scripts/ — fetch.py, metrics.py, lint.py. Every Monitor number comes from a
  named function in metrics.py; no ad-hoc calcs.
- data/snapshots/ — timestamped raw pulls; this IS the DRIFT time series.
  Commit every snapshot.
- drafts/ — Monitor issues and outreach awaiting Kaï's edit/send.

## Hard rules (full list in AGENTS.md and protocols/permissions.md)
- Claude drafts; Kaï sends, commits, publishes. Single-threaded writes.
- Verdicts (CLEAN/WATCH/DRIFT), pricing, legal posture = Kaï alone.
- Research-publisher posture: facts + methodology-based opinions; no advice,
  no accusations of intent, ever.
- Every session ends with a lesson (or an explicit "no lesson today").
