# Strategy & Guardrails

_Last updated: 2026-06-26 07:05 ET (pre-market — AI rout RE-INTENSIFIED on cost/bubble narrative; NVDA downgraded, posture defensive)._

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

_Context (06-26): AI rout RE-INTENSIFIED on a NEW driver — not just the rate scare but an AI-COST + AI-BUBBLE narrative: OpenAI IPO-delay report, AI data-center cost fears, Apple/MSFT raising device prices on the memory squeeze MU foreshadowed, and NVDA's B200 lease price collapsing ~31% in 3 wks. 4th straight down day; Fri futures red (NQ -1.2%); Kospi -8% circuit breaker. Posture: DEFENSIVE — hold, preserve dry powder, do NOT catch the falling knife. The rout has NOT bottomed. Today's data is second-tier (UMich sentiment, goods trade, Fed speakers); PCE (hot) was 06-25._

- **META** — HOLD (4-sh starter). NO add. Strong Buy (58 buys/0 sells, Piper Sandler Buy), no near-term binary (earnings Jul 29), no company-specific bad news — weakness is 100% the macro AI-sentiment rout. The "add after confirmation" plan is now held on TWO grounds: hot PCE (06-25) + re-intensifying AI rout (06-26). Re-evaluate the add only once the rout confirms a bottom. 10% trailing stop live (stop_price $511.23). (2026-06-26)
- **NVDA** — DOWNGRADED to cautious-watch (was top-watch). B200 GPU hourly lease price collapsed $6.11→$4.22 (~31% in 3 wks) + $410M insider selling = a real AI-compute pricing/demand crack that undercuts the "AI capex intact" thesis. Do not initiate until lease pricing stabilizes AND the rout bottoms. (2026-06-26)
- **MU** — Q3 blowout ($50B Q4 guide, $100B contracted, PTs to $2,000) but -3.5% on supply-GLUT fears + selloff; the same print is bearish for device-maker margins. Do NOT chase. WATCH for a base. (2026-06-26)
- **AVGO** — Record FQ2 (AI semi $10.8B) but fell >12% post-earnings on below-hopes >$100B-by-2027 AI target + margin worry. Lower priority. WATCH. (2026-06-26)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-26)
