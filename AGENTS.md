<!-- software-factory:start -->
# Software factory

Every task, in every repo, with any agent (Claude Code, Codex, or anything
else that reads `AGENTS.md` and `SKILL.md`), goes through the same five
steps. Each step has a skill. If your agent doesn't load skills on its own,
open the skill's `SKILL.md` and follow it.

Skills live in `.agents/skills/` in the repo (vendored copy) or in
`~/.agents/skills/` and `~/.claude/skills/` (global install on Kai's Mac
mini). Repo-specific facts (commands, invariants, what runs where) are in the
repo's own `AGENTS.md`, after the factory block. Where they conflict with the
factory, the repo wins. A repo with no repo section hasn't adopted the factory
yet; offer to run `adopt-factory`.

## Know where you are

Check this first. Several skills behave differently depending on it.

- **Local**: Kai's Mac mini. A shared checkout that other agents may also be
  using, the real app can run, `gh` is installed and signed in.
- **Cloud**: a container from Claude Code on the web, Codex cloud, or
  similar. You have your own fresh clone and usually an assigned branch, no
  display, and possibly no `gh` (use the GitHub tools you were given).

If unsure: `uname -s` prints `Darwin` locally; a cloud container is Linux.

## Workflow

1. **Start: `start-task`.** Get onto a task branch from the latest
   `origin/main` (locally, in its own git worktree). Check open PRs for
   files you'd also touch. Install and run the checks once for a baseline.
2. **Build: `code-structure`.** Flows decide *why and when*; shared
   services do the *how*, take explicit inputs, and return results. Keep
   platform-specific calls in small functions so the logic around them can
   be tested anywhere.
3. **Prove: `prove-it`.** Capture the before while reproducing, add a test,
   capture the after. Use the strongest evidence your environment allows,
   and write a manual checklist for whatever you couldn't run.
4. **Review: `review-loop`.** Review your own diff with your agent's review
   command, fix, repeat until clean (max 3 rounds). Add a security review
   when the diff touches secrets, auth, shell commands, or elevated
   permissions.
5. **Ship.** Open the PR (see "Completing a task") and end by giving Kai
   its URL.

## Writing for humans

Apply `unslop` to anything Kai or anyone else will read before you commit or
post it: commit messages, PR title and body, docs, code comments, and your
closing reply. Only to text you wrote or changed.

## Rules

- Never commit to `main`. Never force-push except `--force-with-lease` on
  your own task branch.
- One task, one branch. Never touch another agent's branch, worktree, or
  uncommitted work.
- Resolve lockfile conflicts by regenerating, never by hand-merging.
- Worktrees don't isolate ports or databases. Confirm a dev server is
  *yours* before trusting it.
- If a conflict or a decision can't be resolved confidently, stop and ask.
- Don't merge a PR unless Kai asks.

## Completing a task

1. Keep changes to the assigned task.
2. Run the repo's checks (listed in the repo section below).
3. Commit with a clear message, bring in the latest `origin/main`, rerun
   the checks.
4. Push: `git push -u origin <branch>`.
5. Open the PR. The body covers: what changed; a **Testing** section with
   the evidence from `prove-it` (check results, before/after, manual
   checklist); review findings you chose not to fix, and why; risks and
   follow-ups.
6. Give Kai the PR URL.
<!-- software-factory:end -->

## How the factory applies here

Everything below this section is Tapewatch's own rules, and they win over
the factory block above wherever the two differ:

- The factory's start, build, prove, review, ship steps apply to code in
  `scripts/`. For memory, methodology, drafts, outreach, and data snapshots,
  follow `protocols/permissions.md` (auto / confirm / never) instead.
- Single-threaded writes stand: Kaï sends, publishes, and decides
  verdicts. Agents may commit and open PRs, but never merge or push to
  `main` without Kaï saying so.
- Prove changes to `scripts/` with before/after output on a saved snapshot
  from `data/snapshots/` (never a live pull mid-analysis). Run
  `python3 scripts/lint.py <draft>` on any draft before handing it to Kai.
- Writing rules: `unslop` and `memory/semantic/voice.md` both apply; where
  they disagree, `voice.md` wins.

# AGENTS.md — SKELETON (Kaï: rewrite in your own hand before first use; the
# <150-line hand-written rule exists because generated entry maps measurably
# reduce task success. Delete this header when done.)

## What this company is
Tapewatch: independent, loan-level surveillance for tokenized private credit.
Product = independence + a timestamped public track record, not analysis.
[TODO Kaï: one paragraph in your words on why this exists.]

## Entry map
- Start every session by reading: memory/working/pipeline.md,
  memory/working/gates.md, the 3 newest files in memory/lessons/.
- Methodology → memory/semantic/methodology.md (universe rule is frozen per
  issue — never re-derive mid-analysis).
- Voice → memory/semantic/voice.md. Outreach bar → rubrics/outreach.md.
- Incident history → memory/semantic/incidents.md. Never re-research a known incident.

## Operating rules ([TODO Kaï: cut to the ones you'll actually obey])
1. Compound: every session ends with a lesson to memory/lessons/.
2. Permission tiers per protocols/permissions.md. Drafts are DRAFTS.
3. Single-threaded writes: one actor (Kaï) sends/commits/publishes.
4. Code before agents: if the steps can be written down, it's a script.
5. Verdicts (CLEAN/WATCH/DRIFT), pricing, legal = Kaï alone.
6. Budget attention: a routine whose review burden exceeds its value dies.
7. Legal posture: research publisher. Facts + methodology-based opinions.
   No tailored advice. No accusations of intent. Ever.

---

<!-- Moved from CLAUDE.md, unchanged, so every agent reads it. CLAUDE.md now points here. -->

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
