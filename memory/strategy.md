# Strategy & Guardrails

_Last updated: 2026-06-24 07:00 ET (pre-market — repriced watchlist after overnight AI/tech rout)._

## Mode

- `TRADING_MODE: paper`  ← do not flip to `live` without the human explicitly asking for it here.
- Broker: Alpaca (paper trading account, $100,000 starting paper balance unless noted otherwise below).

## Thesis

Swing / fundamentals-driven long-term investing. Goal: beat the S&P 500 over a multi-month
horizon. This is **not** day trading — no intraday scalping, no reading candlesticks/MACD for
minute-by-minute entries. Decisions are based on company fundamentals, catalysts, and macro
research, held for days-to-months, not minutes.

## Hard guardrails (never violate these)

- **Max position size:** no single position may exceed 5% of total portfolio value at time of entry.
- **Daily loss cap:** if the portfolio is down more than 3% on the day, stop opening new positions
  for the rest of that day — log it and notify.
- **New position cap:** max 3 new positions opened per calendar week.
- **Stop discipline:** every new position gets a 10% trailing stop at entry (via
  `python3 scripts/alpaca.py buy ... --trail-percent 10`).
- **Loss cutting:** at the midday check, any position down 7% or more from entry gets closed
  unless there's a specific, logged thesis reason to hold (and that reason must be written to
  `memory/trade-log.md`).
- **No options. No leverage/margin. No crypto. No shorting** unless the human explicitly changes
  this file to allow it.
- **Paper first.** Do not place a live-money order while `TRADING_MODE` above reads `paper`.

## Research cadence (what each routine should be checking)

- **Pre-market:** overnight news, earnings/catalysts for current holdings and watchlist
  candidates, macro calendar for the day (Fed events, CPI, jobs data, etc.). Draft trade ideas —
  don't execute yet.
- **Market open:** execute the pre-market plan's highest-conviction ideas, set trailing stops
  immediately on any new buy.
- **Midday:** risk check — cut losers past -7%, tighten stops on winners that have run up.
- **Close:** end-of-day wrap-up, log the day, send the daily summary notification.
- **Weekly review (Friday close):** performance vs. S&P 500 for the week, grade the week's
  decisions honestly, propose concrete changes to this strategy file or to the skills in
  `.claude/commands/` if something isn't working.

## Watchlist

_(Bull: keep this updated with tickers you're tracking but haven't bought yet, and why.)_

_Context (06-24): 2-day AI/tech rout (South Korea -10%, AI-profit fears, Fed door open to a 2026 rate hike). Drop is macro, not company-specific — improves entries but argues for caution/staging, not aggression._

- **META** — TOP candidate to initiate. Strong fundamentals, avg PT $827 (58 buys/0 sells), no near-term binary (earnings Jul 29). Sold off to ~$533 in the macro rout → better entry. Plan: HALF-SIZE ~2.5% starter w/ 10% trailing stop at open; add after confirmation. (repriced 2026-06-24)
- **MU** — Reports fiscal Q3 AFTER CLOSE TONIGHT (6/24). Binary; its reaction = market's AI-demand health check. Do NOT buy into the print; reassess Thu AM. (2026-06-24)
- **FDX** — ~$303 post-earnings. Q4 beat but soft CY26 guide + Freight spin stranded costs + fuel +70% YoY. Let it base; watch for overdone dip. (2026-06-24)
- **NVDA** — ~$200, caught in AI-bubble rout, no company-specific news. Watch; don't initiate into the downdraft. (2026-06-24)
- **AVGO** — ~$366, same macro rout. Hyperscaler design wins intact. Watch. (2026-06-24)
