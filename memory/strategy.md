# Strategy & Guardrails

_Last updated: 2026-07-01 07:05 ET (pre-market — posture CONSTRUCTIVE (rout bottomed 6/29); day 2 of the jobs gauntlet: ADP/ISM/Warsh today, June NFP Thu 7/2 (consensus lowered to ~100–115K), markets CLOSED Fri 7/3. Plan: deploy the META add Thu POST-jobs, not into today's red pre-payrolls tape. NVDA gate thawing — B200 lease median recovered to $6.11.)._

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

_Context (07-01): AI rout BOTTOMED Mon 6/29 (clear up day + Dow record 52,182.74) → posture CONSTRUCTIVE. Best H1 in years just closed (Dow +8.9%, S&P +9.6%, Nasdaq +12.8%). Today (Wed 7/1) futures RED into payrolls (Dow -0.33%, S&P -0.29%, NQ -0.34%) = normal pre-jobs profit-taking, NOT a new leg down. Data gauntlet: ADP est 118K + ISM-mfg 53.8 + Warsh today; **June NFP Thu 7/2, consensus LOWERED to ~100–115K vs May 172K** = week's binary; **markets CLOSED Fri 7/3**. Plan: execute the META add THURSDAY post-jobs (if in-line/soft-not-recessionary + META holds up), not into today's red pre-binary tape. NEW WEEK: 0 of 3 new-position slots used (META opened last week; an ADD to META consumes no slot)._

- **META** — HOLD (4-sh starter), **ADD candidate LIVE but sequenced to Thu.** Strong Buy, no near-term binary (earnings Jul 29). Fully healed/green (~$565.52 pre-mkt, +0.48% from entry). Add gate ("tape green / no data shock") is NOT met today (red pre-payrolls). Plan: ADD ~3 sh (~$1.7k, fresh 10% trail) to lift toward ~4% of equity THU 7/2 POST-jobs IF jobs in-line/soft-not-recessionary AND META holds. No new-position slot consumed. Stale item: Google capacity-limits Meta's Gemini use (Mar origin, Meta mitigating via Muse Spark — not thesis-breaking). 10% trailing stop live (hwm $570.90, stop $513.81). (2026-07-01)
- **NVDA** — cautious-watch, **GATE THAWING.** B200 lease median has RECOVERED to $6.11 (matches the May-30 pre-drop level); the $6.11→$4.22 (-31%) crack has reversed. Data still noisy (on-demand $3.70–$14.24, huge provider spread) → want one more read to confirm real stabilization. China headwind (mainland-China DC rev ~$0) persists. Do NOT initiate yet — wait for lease-recovery confirmation + the Thu jobs print. Highest-priority watch; a buy would be a fresh slot. (2026-07-01)
- **MU** — Q3 blowout (rev quadrupled); analysts raised fair value ~$866.60, DRAM/HBM tight through FY27. But Morningstar warns of a 2029-2030 supply GLUT (50%+ rev drop) → -4% Fri. Memory is cyclical; do NOT chase. WATCH for a base. (2026-06-29)
- **AVGO** — Record FQ2 but its cautious AI-chip commentary helped trigger the rout; fell >12% post-earnings. Lower priority. WATCH. (2026-06-29)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-29)
