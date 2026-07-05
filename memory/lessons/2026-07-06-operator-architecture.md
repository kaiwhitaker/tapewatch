## 2026-07-06 — Claude-as-operator architecture, decided
- Claude runs in sessions Kaï opens — no cron, no autonomous send. Kaï is the
  cron and the send button. Gmail drafts folder = the physical confirm queue.
- Plumbing: Tally→Gmail, Cal.com→Calendar, Beehiiv stats→Gmail.
- Security: no GitHub PAT in browsing sessions (trifecta); Dune read-only key
  OK per-session; money credentials never; Resolve MCP not in this Project.
- Named failure mode (watch week 3): queue rot → fewer motions, not fewer gates.
