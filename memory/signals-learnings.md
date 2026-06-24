# Signals & Learnings

_Bull: this is your running playbook — heuristics that worked, mistakes not to repeat, signal
patterns worth watching for. Update this whenever you notice something generalizable. This file
is what makes you better over time instead of repeating the same mistakes._

## Signals worth weighting

- _(none logged yet — populate as you trade)_

## Mistakes / anti-patterns to avoid

- _(none logged yet)_

## Process notes

- **Routine scheduling is ~8h early (recurring).** On 2026-06-24 every routine — market-open, midday,
  and market-close — fired around 01:xx ET, before the 09:30 open, so the clock read `is_open: false`
  and no orders could execute. Net effect: the planned META starter never got placed all day despite a
  ready plan. Fix the cron/timezone offset so routines fire during/after the cash session (open ~09:30,
  close ~16:00 ET). Until fixed, treat early "open/midday/close" runs as plan-only, not execution.
- **Escalate the misfire, don't just log it.** When an *execution* routine (open/midday/close) fires
  with `is_open: false`, send ONE Telegram flag that day (not silent logging) so the human notices the
  broken schedule and fixes the cron. Silent logging let this recur unseen and cost a full +1.6% S&P
  week in cash (see weekly-review 2026-06-22). One flag per day, not per run — don't spam.
- **A good plan that never executes still loses to the index.** Inception week: sound META starter,
  disciplined avoidance of MU/FDX/INTC traps, zero losses — but 0 trades and -1.6% vs S&P because a
  timing bug blocked every execution. Risk discipline is necessary but not sufficient; deployment is
  the job. When a guardrail-clean plan is pending and the market is open, the catch-up rule in
  `.claude/commands/trade.md` says execute it.
