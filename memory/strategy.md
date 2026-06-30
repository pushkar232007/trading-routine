# Strategy & Guardrails

_Last updated: 2026-06-30 07:05 ET (pre-market — AI rout BOTTOMED Mon 6/29 (clear up day + Dow record); posture upgraded to CONSTRUCTIVE, now gated only on the 3-session jobs gauntlet (JOLTS/ADP/Warsh/NFP) ending Thu)._

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

_Context (06-30): AI rout has **BOTTOMED**. Mon 6/29 was the clear up day the falling-knife rule required — S&P +1.18% (7,440.43), Nasdaq +2.07% (25,820.14), Dow record close 52,182.74 (GOOGL Dow debut; TSLA +8.5%, AMZN +3.2%, META +2.2%). Both confirmation conditions met (clear up day AND index record). Posture upgraded DEFENSIVE → CONSTRUCTIVE; the only remaining caution is the 3-session data gauntlet: JOLTS Tue 6/30, ADP + ISM-mfg + Warsh (Europe, hawkish=growth headwind) Wed 7/1, **June NFP Thu 7/2 (a day early), consensus ~130k vs May's 172k** = week's binary; **markets CLOSED Fri 7/3**. Plan: begin redeploying dry powder into confirmed strength (start with the META add) rather than staying in cash now the bottom is in. NEW WEEK: 0 of 3 new-position slots used (META opened last week; an ADD to META consumes no slot)._

- **META** — HOLD (4-sh starter), **ADD candidate now LIVE.** Strong Buy, no near-term binary (earnings Jul 29). Position fully HEALED (~$563.75 pre-mkt, +0.17% from entry). The "add after confirmation" plan's gates have cleared: PCE is past, the AI rout has bottomed — only the Thu 7/2 jobs print remains. ADD ~3 sh (~$1.7k, fresh 10% trail) to lift toward ~4% of equity IF the tape holds green / JOLTS not a shock; else wait and add Thu post-jobs. Minor neg noted: AI-For-Work lead Emily Dalton Smith exited (not thesis-breaking). 10% trailing stop live (hwm $570.90, stop ~$513.81). (2026-06-30)
- **NVDA** — cautious-watch (HOLDS). B200 GPU hourly lease price STILL soft — the $6.11→$4.22 (-31%) drop has NOT reversed/stabilized (current on-demand $3.70–$5.50, spot ~$2.70) + China headwind (mainland-China DC rev ~$0). Even with the broad bottom in, the NVDA-specific gate (lease pricing stabilizes) is UNMET. Do not initiate yet. (2026-06-30)
- **MU** — Q3 blowout (rev quadrupled); analysts raised fair value ~$866.60, DRAM/HBM tight through FY27. But Morningstar warns of a 2029-2030 supply GLUT (50%+ rev drop) → -4% Fri. Memory is cyclical; do NOT chase. WATCH for a base. (2026-06-29)
- **AVGO** — Record FQ2 but its cautious AI-chip commentary helped trigger the rout; fell >12% post-earnings. Lower priority. WATCH. (2026-06-29)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-29)
