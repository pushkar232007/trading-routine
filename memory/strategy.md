# Strategy & Guardrails

_Last updated: 2026-07-08 07:10 ET (pre-market Wed; research/drafting only, NO trades this routine. DOUBLE risk-off today: (1) NEW overnight — Trump says Iran ceasefire "OVER" + oil +6% (Brent ~$78, WTI ~$74.55), Kospi -5.4% semi-heavy, US futures S&P -0.1%/Dow -0.4%; (2) FOMC June minutes 2pm ET = week's binary (hawkish-leaning). Posture CONSTRUCTIVE underlying but HOLD FIRE at the open — falling-knife (unconfirmed sentiment/war shock) + unresolved same-day binary. META HELD, +4.77%, ~4.24% of equity = target weight → no add; NEW positive: Muse Image launch (closed +2.6% Tue bucking red Nasdaq). Deployment-floor LOGGED DECISION: staying >90% cash today is DELIBERATE (see log). Deployables named for once tape clears: MRK PRIMARY (defensive/oil-insensitive), FDX secondary (oil = fuel-cost HEADWIND today) — both spread-gated on broken paper feed; /trade must re-sample spread LIVE 2-3x. NVDA gate unconfirmed (H20 China licenses resuming = new +, but lease $4.22 soft + semi risk-off) → do NOT initiate. New week 7/6 → 0 of 3 new-position slots used.)._

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

_Context (07-08, Wed): posture CONSTRUCTIVE underlying but DOUBLE risk-off today → hold fire at open. (1) Iran ceasefire "over" (Trump) + oil +6% → Kospi -5.4%, US futures mildly red; (2) FOMC June minutes 2pm ET (hawkish-leaning) = week's binary. META held & higher (+4.77%; Muse Image launch, closed +2.6% Tue bucking red Nasdaq). Book ~96% cash → deployment-floor LOGGED DECISION: staying >90% cash today is deliberate (falling-knife war-shock + unresolved binary). Deployables for once tape clears: MRK PRIMARY (defensive/oil-insensitive, HSBC PT $150), FDX SECONDARY (oil = fuel headwind today) — both spread-gated; re-sample LIVE. AI-hardware still gated (NVDA lease $4.22 soft though H20 China licenses resuming = new +; MU/AVGO under semi risk-off). Diversification: FDX + MRK + GEHC = 3 non-tech names (≥2 rule satisfied). New week 7/6 → 0 of 3 new-position slots used._

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, **+4.77%** (~$606), ~**4.24% of equity = target weight** (below 5% cap). "Meta Compute" cloud thesis intact. NEW positive: **Muse Image** (first image-gen model from Meta Superintelligence Labs) launched across IG/WhatsApp 7/7 → closed **+2.6% Tue bucking a red Nasdaq (-1.16%)**. Valuation 11.6x op cash flow vs 5y avg 13.7x = still cheap. Standing bear worry: $145B 2026 capex. Strong Buy, no binary until earnings Jul 29. Both trailing legs live. Add only on a material pullback + fresh catalyst. (2026-07-08)
- **FDX** — **SECONDARY deployable / non-tech diversifier — SPREAD-GATED + oil headwind today.** Buy consensus (14B/2H/1S), avg PT $349.72 (~12% up from ~$314); **BofA raised PT to $378**; Supply Chain unit divested $1.4B. **NEW: today's oil +6% spike is a direct fuel-cost NEGATIVE for FedEx margins → worse deploy on THIS oil-shock tape** (MRK now cleaner). Idea when tape/spread clear: starter ~9-10 sh / ~$3k (≈3%), fresh 10% trail, a FRESH slot. **CAVEAT: paper quote remains pathologically wide (close snapshot bid $293.55/ask $327.48 ≈ 11.6%) — /trade MUST re-sample spread LIVE 2-3x (<~2-3%) before any market buy.** (2026-07-08)
- **MRK** *(non-tech — PRIMARY deployable for today's tape)* — real near-term catalysts: **KEYTRUDA FDA approvals (TNBC + bladder), positive Ph3 tulisokibart (UC), EC approved Keytruda+Padcev 6/23; HSBC PT raised to $150 (Buy)**, Scotiabank $155, BofA $141; Buy consensus, ~$122; 3.1% div. **Defensive pharma, oil-insensitive, low AI-correlation → the CLEANER deploy than FDX on an oil-shock risk-off day.** H2-2026 pipeline re-rate setup. Minor neg: terminated MK-1167 oral Alzheimer's 7/1 (failed interim). Risk: 2028 Keytruda patent cliff. Still spread-gated + want it not into the pre-minutes ugliness. (2026-07-08)
- **NVDA** — cautious-watch, **GATE STILL UNCONFIRMED — do NOT initiate.** B200 lease still ~$4.22 (−31%), ~$195 (-17% from May peak). **NEW positive: US resuming H20 export licenses to China** (reopens a blocked market) — incremental +, but lease still soft + Kospi -5.4% semi risk-off today. Highest-priority tech watch; a buy is a fresh slot. (2026-07-08)
- **MU** — Burry short + memory names under today's semi risk-off (Kospi -5.4%) → do NOT chase. WATCH. (2026-07-08)
- **AVGO** — improving (FV raised $476.78→$523.73; Hock Tan >$100B AI-semi rev by FY27 on $73B backlog + custom-ASIC deals). No clean base/entry; semi risk-off today. WATCH. (2026-07-08)
- **GEHC** *(non-tech)* — medtech; ~30% discount to ~$88 fair value; ~$62. Defensive diversifier. WATCH. (2026-07-08)
- _Energy (theme, not a name yet): oil +6% on the Iran shock makes energy topical, but chasing a geopolitical oil pop = momentum trap. Note only — don't chase. (2026-07-08)_
