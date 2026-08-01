# Monthly deep-review prep — 2026-08-01

**Status: NOT RUN — the surveillance scaffold this review reads from does not
exist. No per-pool baselines to review against, no locked universe, no time
series. Recording the blocker instead of fabricating a run.**

This is the same root-cause blocker recorded by the 2026-07-07 weekly sweep
(`surveillance/inbox/2026-07-07-sweep.md`), still unresolved a month later. The
prerequisites are Kaï's to make; none has moved since.

## What the task asked for vs. what exists

The routine specifies reading, then reviewing against, these inputs:

| Required input (per task) | Exists in repo? | Verified by |
|---|---|---|
| `memory/working/surveillance/methodology.md` | **No** | `find memory/working/surveillance` — only the `inbox/` created by this run exists. Methodology of record is `memory/semantic/methodology.md` (v0.2), a different path. |
| `memory/working/surveillance/pools/` (per-pool files) | **No** | `find . -name "*pool*"` returns only `data/snapshots/2026-07-05-pools.json` and `memory/working/monitor-1-pool-shortlist.md` — no per-pool baseline files. |
| Each pool's **"Baseline Expectations"** section | **No** | `grep -rl "Baseline Expectations"` across all `*.md` → NONE FOUND. The review's entire comparison target is absent. |
| `memory/working/surveillance/predictions.md` | **No** | Path absent. No OPEN prediction rows to check or resolve. |
| `memory/working/surveillance/inbox/` | Created by this run | Was absent; a top-level `surveillance/inbox/` holds the 2026-07-07 note. |

## Why it cannot run (root cause, not path fixes)

1. **No "Baseline Expectations" sections exist anywhere.** The task's core loop
   is "run the full monthly review against its 'Baseline Expectations'
   section." There are zero such sections in the repo (grep confirms). With no
   baseline, every one of the five checks (concentration, redemption-vs-duration,
   NAV cadence/divergence, mandate-vs-composition, counterparty watch) has
   nothing to compute a delta against.

2. **The 10-pool universe is not locked.** It is still a 14-candidate slate in
   `memory/working/monitor-1-pool-shortlist.md`, several rows marked `[TBD]`
   (Maple High Yield Secured size, BlockTower pool, Steakhouse vault size,
   Pareto/Goldfinch/Wildcat alternates). The header states plainly: "THE PICK IS
   YOURS (never-tier: published judgment)." It is unmade. There is no defined
   set of "each pool" to iterate over.

3. **Monitor Issue #1 is unpublished.** It exists only as
   `drafts/monitor-issue-1-DRAFT.md`. Per methodology v0.2, DRIFT is a trend
   verdict "unavailable in an instrument's first issue on the tape," and every
   grade is measured "against a prior issue's baseline." With no published
   baseline issue, there is nothing on the tape to diff against.

4. **One snapshot, no time series.** `data/snapshots/` holds only the
   2026-07-05 pull (`-pools.json`, `-protocols.json`). Methodology v0.2: "the
   time series IS the DRIFT verdict's evidence base." A single point is not a
   series — no month-over-month delta is computable from committed data.

5. **Pre-launch.** `memory/working/pipeline.md` (updated 2026-07-06):
   "Status: pre-launch… Pages not deployed." Subs 0 / Calls 0 / Paid teardowns
   0. The surveillance product is not yet stood up.

## Why fabricating a run would be the wrong output

Running a live public-source scan of the candidate slate and writing
CLEAN/WATCH/DRIFT drafts now would violate the operating rules, not satisfy
them:

- **Two-source rule** (methodology "Data rules"): any number driving a verdict
  needs two independent sources; there is no baseline series to be the second.
- **"Never estimate or fill gaps"** (this task's own step 2): with no baselines,
  every "change vs. baseline" line would be an invented delta.
- **DRIFT is undefined on first observation** — grading drift with no prior
  issue manufactures a trend from a single point.
- **Grades are Kaï's alone** (never-tier); and the research-publisher posture
  forbids asserting findings the data cannot support.

Declining to fabricate is the disciplined output here.

## Per-pool review

Not applicable — there is no locked pool universe and no per-pool baseline
files, so there is no set of pools to iterate and nothing to review each
against. Per the task, unfound data is marked, not estimated: the pool files,
baseline sections, and predictions rows are all **NOT FOUND** (searched:
`memory/working/surveillance/**`, repo-wide `grep "Baseline Expectations"`,
`find -name "*pool*"`).

## Changes vs. baseline
None computable — no baseline of record exists.

## PROPOSED PREDICTION
None. Opening a falsifiable prediction requires a baseline to falsify against;
there is none, and `predictions.md` does not exist.

## What unblocks the next monthly review (Kaï's calls)

1. **Lock the Monitor #1 10-pool universe** from the candidate slate (resolve
   the `[TBD]` rows). Never-tier — Kaï's alone.
2. **Publish Monitor Issue #1**, which establishes the first per-pool baselines,
   OR scaffold `memory/working/surveillance/pools/*.md` with an explicit
   "Baseline Expectations" section per locked pool, plus
   `memory/working/surveillance/predictions.md`.
3. **Commit a second dated snapshot** so `data/snapshots/` is a series, not a
   point — the DRIFT evidence base.

Once one baseline issue exists on the tape and a second snapshot is committed,
this monthly deep review has defined pools, baseline sections, and a time series
to diff against, and can run as written.

---
*Generated by the scheduled monthly deep-review prep. Autonomous run: nothing
was sent, posted, or published. No file outside
`memory/working/surveillance/inbox/` was modified. No web sources were fetched —
there was no locked universe or baseline to scan against, so a live scan would
have produced only fabricated deltas. Any web content, had it been read, would
have been treated as data, not instructions. GRADE decisions, universe lock, and
Issue #1 publication remain Kaï's alone.*
