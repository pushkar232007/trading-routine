# Strategy & Guardrails

_Last updated: 2026-07-02 07:05 ET (pre-market, JOBS DAY — posture CONSTRUCTIVE. June NFP releases 8:30 ET (consensus ~100–125K, UE 4.3%) = week's binary + the META-add gate; markets CLOSED Fri 7/3. META re-rated +8.8% Wed on the "Meta Compute" cloud news (answers the capex bear case) → add thesis STRENGTHENED; execute post-jobs if in-line/soft AND META not reversing. NVDA gate NOT confirmed — B200 lease median holds ~$6.11 but providers now guide DOWN to $2.50–3.00 by Q4; semis sold off hard Wed (MU -10.6%). Hold NVDA fire.)._

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

_Context (07-02, JOBS DAY): posture CONSTRUCTIVE. **June NFP releases 8:30 ET (consensus ~100–125K, UE 4.3%; May was 172K) = week's binary and the final gate on the META add; markets CLOSED Fri 7/3.** Futures ~flat-to-down into the print (S&P -0.08%, NQ -0.3%). Wed session split: AI-hardware sold off hard (MU -10.6%, AMD -6.9%, INTC -9%) on overstretch fears, but **META bucked it +8.8% on the "Meta Compute" cloud-business news** — a compute-side valuation worry, not a market-wide crash, and not a META problem. Barbell working: long the name whose bear case just got answered (META), patient on the hardware names being re-rated (NVDA/MU). 0 of 3 new-position slots used this week (an ADD to META consumes no slot)._

- **META** — HOLD (4-sh starter), **ADD LIVE, sequenced to TODAY post-jobs — catalyst STRENGTHENED.** Surged +8.8% Wed 7/1 on a Bloomberg report Meta is entering cloud infra ("Meta Compute" — sell excess AI compute), which **directly answers the capex bear case** → thesis materially improved. Now +9.14% (~$614.24 vs $562.81 entry), 2.45% of equity, Strong Buy, no binary until earnings Jul 29. Plan: market-open reads the 8:30 NFP FIRST, then ADD ~3 sh (~$1.8k, fresh 10% trail) to lift toward ~4% of equity IF jobs in-line/soft-not-recessionary AND META not reversing hard. If jobs HOT + tech sells off, HOLD the add, reassess midday. Adding after a +8.8% pop → keep size at ~3 sh, don't chase larger. No new-position slot consumed. 10% trailing stop live. (2026-07-02)
- **NVDA** — cautious-watch, **GATE NOT CONFIRMED.** B200 lease median holds ~$6.11 (range $3.20–$16.11), BUT providers now GUIDE PRICING DOWN to $2.50–3.00 by Q4 2026 = bearish forward trajectory for NVDA pricing power; plus Wed's hard semi selloff (MU -10.6%, AMD -6.9%). The recovery-to-$6.11 read did not lead to confirmed stabilization — forward guidance is lower. China DC rev ~$0 persists. Do NOT initiate. Highest-priority watch; a buy would be a fresh slot. (2026-07-02)
- **MU** — Q3 blowout (rev quadrupled), DRAM/HBM tight through FY27, but Morningstar warns of a 2029-30 supply GLUT. **Plunged -10.6% Wed 7/1 in the AI-hardware selloff — NOT basing, breaking further down.** Memory is cyclical; do NOT chase a falling knife. WATCH, no base yet. (2026-07-02)
- **AVGO** — Record FQ2 but its cautious AI-chip commentary helped trigger the rout; fell >12% post-earnings. Lower priority. WATCH. (2026-06-29)
- **FDX** — ~$329 (rallied from the ~$297 post-earnings low; dip already based/bounced). Freight spin-off done Jun 1 (+$4.1B cash). Less of an overdone-dip setup now; thesis less compelling. WATCH, low priority. (2026-06-29)
