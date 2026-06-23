---
description: Evaluate the current research/watchlist and execute trades within guardrails
---

Read `memory/strategy.md`, `memory/portfolio.md`, `memory/research-log.md` (last 2-3 entries),
and `memory/signals-learnings.md` before doing anything.

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
4. To exit a position: `python3 scripts/alpaca.py close SYMBOL`.

After acting, append every action (or deliberate non-action) to `memory/trade-log.md` in the
documented format, and refresh `memory/portfolio.md` with the latest
`python3 scripts/alpaca.py account` + `python3 scripts/alpaca.py positions` output.

Only send a Telegram notification (`python3 scripts/telegram.py "..."`) if a trade was actually
placed or closed.
