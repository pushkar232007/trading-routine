---
description: Evaluate the current research/watchlist and execute trades within guardrails
---

Read `memory/strategy.md`, `memory/portfolio.md`, `memory/research-log.md` (last 2-3 entries),
and `memory/signals-learnings.md` before doing anything.

**Standing-plan catch-up:** first confirm the market is open (`python3 scripts/alpaca.py clock`
→ `is_open: true`). If it is, check whether the most recent pre-market plan in
`memory/research-log.md` was ever executed (cross-check `memory/trade-log.md` / current positions).
If a guardrail-clean plan is still pending because an earlier routine misfired (e.g. fired while
the market was closed), **execute that standing plan first**, then continue with today's ideas.
This way a single in-hours run can salvage a plan the open routine missed.

For each candidate trade idea:

1. **Check every guardrail in `memory/strategy.md`** before placing anything:
   - Position size ≤ 5% of total equity (check `python3 scripts/alpaca.py account` for equity).
   - Weekly new-position cap not exceeded (count this week's entries in `memory/trade-log.md`).
   - Daily loss cap not breached (check today's P/L before opening anything new).
   - No options, no margin, no shorting, no crypto.
   - `TRADING_MODE` in `memory/strategy.md` is `paper` unless explicitly set to `live`.
2. If a trade clears every guardrail, place it:
   ```
   python3 scripts/alpaca.py buy SYMBOL QTY --trail-percent 10
   ```
   This buys at market and immediately attaches a 10% trailing stop, per strategy.
3. If a trade does NOT clear a guardrail, skip it and log why in `memory/trade-log.md` anyway —
   skipped trades are still useful history.

**Post-earnings-gap entry discipline (added 2026-07-31 after the GEHC lesson).** "Buy the
reaction, not the run-up" is too vague — on 7/30 it let us buy GEHC AT its +11% earnings pop
($71.42, above the $71.25 pop close) with no consolidation, and it immediately gave back to
-4.76%. Concrete rule: if a name has gapped **≥8% on an earnings/catalyst print**, do NOT enter
on the pop (same-day or next-day). Require EITHER (a) a pullback of **≥⅓ of the gap** off the
post-print high, OR (b) **≥1 full consolidation session** that holds above the pre-gap level,
before deploying. If neither has happened, the gate stays met — wait for a cleaner entry rather
than chasing the vertical move.
4. To exit a position: `python3 scripts/alpaca.py close SYMBOL`.

After acting, append every action (or deliberate non-action) to `memory/trade-log.md` in the
documented format, and refresh `memory/portfolio.md` with the latest
`python3 scripts/alpaca.py account` + `python3 scripts/alpaca.py positions` output.

Only send a Telegram notification (`python3 scripts/telegram.py "..."`) if a trade was actually
placed or closed.
