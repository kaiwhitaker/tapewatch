# tapewatch — company brain

Private repo. This is the company: memory, methodology, rubrics, session
templates, and the deterministic scripts behind The Tokenized Credit Monitor.

## Commit workflow (until a routine earns API automation)
Claude generates/updates files in sessions → Kaï reviews → Kaï commits:

    git clone git@github.com:kaiwhitaker/tapewatch.git
    # copy scaffold contents in
    git add -A && git commit -m "scaffold v0.1" && git push

No credentials for this repo ever enter a Claude session (trifecta rule —
see protocols/permissions.md).

## Layout
- AGENTS.md — entry map + operating rules. HAND-WRITTEN by Kaï, <150 lines.
- memory/semantic/ — ICP, methodology, moats, voice, incidents. Slow-changing truth.
- memory/episodic/ — dated session logs, append-only.
- memory/lessons/ — the compound loop's output. One lesson per file.
- memory/working/ — pipeline.md, gates.md, curator list. Fast-changing state.
- protocols/ — permissions.md (auto/confirm/never).
- rubrics/ — what good looks like; graded Fridays.
- sessions/ — prompt templates for ops/scout/scorecard/lesson.
- scripts/ — fetch.py, metrics.py, lint.py. Every Monitor number comes from a
  named function in metrics.py. No ad-hoc calcs.
- data/snapshots/ — timestamped raw API pulls (gzipped since 2026-10). Commit
  every snapshot; this IS the time series the DRIFT verdict depends on.
  .github/workflows/snapshot.yml pulls and commits one every Monday; run it by
  hand from the Actions tab before an issue.
- drafts/ — Monitor issues and outreach awaiting Kaï's edit/send.
