# Strategy & Guardrails

_Last updated: 2026-07-03 07:10 ET (pre-market on a MARKET HOLIDAY — NYSE/Nasdaq CLOSED for July 4th, no trading until Mon 7/6; research/drafting only. Posture CONSTRUCTIVE. META add DONE Thu 7/2 (7 sh @ $578.45 blended, now 4.08% of equity = target weight); "Meta Compute" cloud thesis intact → HOLD, no further add. NVDA gate now DOUBLY-unconfirmed: lease forward-guide down to $2.50–3.00 by Q4 + WSJ report OpenAI missed user/revenue targets (AI-demand question) drove a broad chip rout — do NOT initiate. New-week binary = Wed 7/8 FOMC June minutes. New week 7/6 → new-position slots reset to 0 of 3.)._

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

_Context (07-03, MARKET HOLIDAY — CLOSED): posture CONSTRUCTIVE. No trading today; next session Mon 7/6. Thu 7/2 closed mixed — Dow all-time high, S&P flat as a late tech backslide (Nasdaq-100 -1.61% intraday) erased broad gains. The META add is DONE (7 sh @ $578.45 blended, 4.08% of equity = at target weight) → the barbell is now fully positioned: long META (capex bear case answered by "Meta Compute"), patient on the AI-hardware names being re-rated (NVDA/MU). NVDA gate got WORSE — WSJ says OpenAI missed internal user/revenue targets, an AI-demand question that drove a broad chip rout (7/1: AMD -6%, ARM -8%, AVGO -5%, MU -4%). New-week binary = Wed 7/8 FOMC June minutes. New week 7/6 → 0 of 3 new-position slots used._

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, +0.77%, now **4.08% of equity = target weight** (near the 5% cap). "Meta Compute" cloud thesis intact/strengthening (Meta building a cloud biz to sell excess AI compute, led by Dina Powell McCormick → recoups part of $125–145B 2026 capex, answers the #1 bear case). Faded from the $628 Wed intraday spike to ~$583 but held green. Strong Buy, no binary until earnings Jul 29. Sizing is done — only add again on a material pullback + fresh catalyst. Both trailing legs live. (2026-07-03)
- **NVDA** — cautious-watch, **GATE DOUBLY-UNCONFIRMED — do NOT initiate.** Two bearish reads now: (1) B200 lease providers GUIDE PRICING DOWN to $2.50–3.00 by Q4 2026 (forward pricing-power erosion), and (2) NEW — WSJ reports OpenAI MISSED internal weekly-user + revenue targets = an AI-DEMAND question, which sparked a broad chip rotation (7/1). NVDA pinned ~$200 for 7 straight sessions; China DC rev ~$0 persists. Highest-priority watch; a buy would be a fresh slot. (2026-07-03)
- **MU** — Q3 blowout (rev quadrupled), DRAM/HBM tight through FY27, but Morningstar warns of a 2029-30 supply GLUT. Caught in the AI-hardware selloff again (-4% Wed 7/1) — no base yet, breaking down. Memory is cyclical; do NOT chase a falling knife. WATCH. (2026-07-03)
- **AVGO** — Record FQ2 but its cautious AI-chip commentary helped trigger the rout; fell >12% post-earnings. Lower priority. WATCH. (2026-06-29)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-29)
