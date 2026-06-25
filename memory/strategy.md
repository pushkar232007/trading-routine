# Strategy & Guardrails

_Last updated: 2026-06-25 07:00 ET (pre-market — MU blowout reset the AI-demand read; watchlist updated)._

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
- **Stop-tightening ratchet:** as a winning position's gain grows, tighten its trailing stop —
  never loosen it. Check at the midday routine using the position's unrealized gain % from entry:
  - Gain 0–15%: leave at 10% (no change).
  - Gain 15–30%: tighten to 7% (`python3 scripts/alpaca.py tighten-stop SYMBOL 7`).
  - Gain 30%+: tighten to 5% (`python3 scripts/alpaca.py tighten-stop SYMBOL 5`).
  This exists because a pure trailing stop alone can let a real unrealized gain round-trip back to
  breakeven if price pulls back less than the trail % without ever triggering it. Log every
  tightening action to `memory/trade-log.md` (symbol, old %, new %, gain % that triggered it).
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

_Context (06-25): MU's fiscal Q3 BLOWOUT (rev $41.46B, EPS $25.11, GM 84.9%, Q4 guide $50B, $100B contracted) +13% AH = the AI-demand all-clear; rebuts the SK-Hynix demand-slowdown fear that drove the rout. Net constructive on the AI complex BUT May PCE drops today 8:30 ET (forecast hot, +4.1% headline y/y) — a hot core pressures high-multiple tech. Posture: constructive but PCE-gated; stage, don't chase._

- **META** — HOLD (4-sh starter) + ADD candidate. Strong Buy, 64 analysts, avg PT $827-840 (~47% upside), no near-term binary (earnings Jul 29). MU = the demand-side confirmation the "add after confirmation" plan was waiting on. Plan: read 8:30 PCE first; if in-line/cooler, add ~2-3 sh toward ~4% of equity w/ fresh 10% trailing stop; if PCE hot, hold the add. (2026-06-25)
- **MU** — Binary RESOLVED bullish (Q3 blowout) but +13% to ~$1,186 — do NOT chase the spike. WATCH for a base/pullback before any initiation. (2026-06-25)
- **NVDA** — ~$200, no company-specific news; positive MU read-through (AI capex intact). Top watch for an add once PCE clears and the rout bottom confirms; don't initiate into a PCE-day tape. (2026-06-25)
- **AVGO** — ~$390, same rout but had its own weak-guide stumble ~Jun 6 — lower priority than NVDA. Watch. (2026-06-25)
- **FDX** — ~$297 post-earnings. Q4 beat but soft CY26 guide + Freight spin stranded costs + fuel +70% YoY. Still basing; watch for overdone dip. (2026-06-25)
