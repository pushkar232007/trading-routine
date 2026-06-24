# Weekly Review

_Bull: append a new entry every Friday close. Newest at top. Be honest — grade yourself, don't
just write a highlight reel._

Format:

```
## Week of YYYY-MM-DD
- Portfolio return: __%  |  S&P 500 return: __%  |  Delta: __%
- Best decision:
- Worst decision:
- Grade: A-F
- Changes to make next week (strategy.md / commands / cron):
```

---

## Week of 2026-06-22 (inception week)
- Portfolio return: 0.00%  |  S&P 500 return: +1.6%  |  Delta: -1.6%
- Best decision: **Discipline on binary/momentum names.** Held off MU into its after-close fiscal
  Q3 print (binary), refused to chase FDX's guidance-driven falling knife pre-open, and avoided
  INTC's +250% YTD momentum chase. Capital fully preserved — no reckless entries on a stretched,
  narrow-leadership tape. The META starter plan itself was sound (fresh multi-bank upgrades, no
  imminent catalyst, ≤5% sizing + 10% trailing stop).
- Worst decision: **Letting the ~8h-early routine-timing bug block all execution for a second day.**
  A ready, guardrail-clean META starter never got placed because every execution routine (open,
  midday, close) fired at ~01:xx ET while `is_open: false`. Net result: sat 100% cash through a
  +1.6% S&P week with a plan in hand. This is a process/operational failure, not a thesis failure —
  and it went only *logged*, not *escalated*, so it recurred.
- Grade: **D.** Clean slate, zero losses, sound research and disciplined risk posture — but the core
  mission (deploy capital, beat the S&P) was failed: 0 trades, underperformed the benchmark by 1.6%
  purely by being stuck in cash. Not an F because capital is intact and the plan is ready to fire the
  moment the timing is fixed; not higher than D because "good plan, never executed" still loses to the
  index.
- Changes to make next week:
  1. ~~Routine cron timezone (highest priority — needs the human).~~ **CORRECTED post-run, 2026-06-24:**
     this was a false alarm. The `is_open: false` firings all week were manual "Run now" test triggers
     during initial setup (often run at ~1 AM ET by the human), not the actual scheduled cron. The human
     independently verified the real configured crons already match what's proposed below — no change
     was needed. See `memory/signals-learnings.md` Process notes for the full correction. (Original text
     preserved for history: "`routines/*.md` crons are written as `30 8 * * 1-5` etc. assuming ET, but
     the scheduler fires them ~8h early. Pin the cloud routine schedule to `America/New_York`, OR convert
     every cron to UTC: market-open `30 13 * * 1-5`, midday `0 16 * * 1-5`, close `0 20 * * 1-5`.")
  2. **Standing-plan catch-up rule (implemented this run in `.claude/commands/trade.md`).** If a prior
     pre-market plan was never executed and the market is now open, execute the standing plan first —
     so a single in-hours run salvages the day even if the open routine misfired.
  3. **Escalate-once on misfire (implemented in `memory/signals-learnings.md`).** When an execution
     routine fires with `is_open: false`, send ONE Telegram flag (not silent logging) so the human
     notices the broken schedule instead of it recurring unseen.
