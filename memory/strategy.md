# Strategy & Guardrails

_Last updated: 2026-06-29 07:10 ET (pre-market — AI rout MODERATING into an orderly rotation; posture defensive-but-thawing, gated on Thu jobs report)._

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

_Context (06-29): AI rout has shifted from PANIC to an ORDERLY VALUATION RESET + SECTOR ROTATION (healthcare XLV +7.88% on the week; non-tech sectors all up; S&P only ~3% off its high). Mon futures modestly green (Dow +0.2%, S&P +0.1%); the Kospi-circuit-breaker panic has passed. BUT no clear up day yet (Fri treaded water) and a fresh binary is ahead: **June jobs report Thu 7/2 (early for the holiday), consensus +172k** — hot = rate-hike fears pressure high-multiple tech, cool = relief. Warsh speaks Wed 7/1; **markets CLOSED Fri 7/3**. Posture: DEFENSIVE-but-THAWING — hold, preserve dry powder, deploy a slot only once jobs clears AND a bottom confirms. NEW WEEK: 0 of 3 new-position slots used (META opened last week)._

- **META** — HOLD (4-sh starter). NO add yet. Strong Buy (58 buys/0 sells), no near-term binary (earnings Jul 29), no company-specific bad news — weakness was 100% the macro rout and the position is now HEALING (~$558.80 pre-mkt Mon, only -0.71% from entry vs -2.28% Fri). The "add after confirmation" plan now has THREE gates: hot PCE (06-25) + the AI rout + the Thu 7/2 jobs binary. Re-evaluate the add only after jobs clears AND a bottom confirms. 10% trailing stop live (stop_price $511.23). (2026-06-29)
- **NVDA** — cautious-watch (HOLDS). B200 GPU hourly lease price still at the $4.22 low (the -31% from $6.11 has NOT reversed/stabilized) + China headwind (Commerce closing the offshore loophole; mainland-China DC rev ~$0). Falling lease = supply built faster than workloads = pricing-power warning. Do not initiate until lease pricing stabilizes AND the rout bottoms. (2026-06-29)
- **MU** — Q3 blowout (rev quadrupled); analysts raised fair value ~$866.60, DRAM/HBM tight through FY27. But Morningstar warns of a 2029-2030 supply GLUT (50%+ rev drop) → -4% Fri. Memory is cyclical; do NOT chase. WATCH for a base. (2026-06-29)
- **AVGO** — Record FQ2 but its cautious AI-chip commentary helped trigger the rout; fell >12% post-earnings. Lower priority. WATCH. (2026-06-29)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-29)
