# Strategy & Guardrails

_Last updated: 2026-07-09 07:10 ET (pre-market Thu; research/drafting only, NO trades this routine. Tape STABILIZING — the Wed hold-fire condition is LIFTING: (1) FOMC June minutes CLEARED yesterday (hawkish — "rates above current range by year-end" = hike door open — but market SHRUGGING it off), (2) Iran/oil shock FADING, oil reversing lower Thu, war jitters easing; Thu futures GREEN (Dow +0.2%/S&P +0.3%/Nasdaq +0.5%), focus rotating to AI + SK Hynix US debut today. Posture CONSTRUCTIVE, deployables now moving toward ACTIONABLE. META HELD +4.29%, ~4.21% of equity = target weight → no add. Deployment-floor: named deployable = MRK PRIMARY (defensive/oil-insensitive, cleanest into hawkish-Fed tape — but consensus upside now thin ~2%, treat as diversifier starter), FDX SECONDARY (oil fuel-headwind now EASING as oil reverses) — both still spread-gated on broken paper feed; /trade MUST re-sample spread LIVE 2-3x (<~2-3%) AND require a constructive tape before any starter. NVDA gate STILL unconfirmed (NEW +: China approving limited H200 buys, NVDA +1% — but B200 lease still soft) → do NOT initiate. Today's data: jobless claims 8:30 ET (second-tier). New week 7/6 → 0 of 3 new-position slots used.)._

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

_Context (07-09, Thu): posture CONSTRUCTIVE — the Wed hold-fire condition is LIFTING. (1) FOMC June minutes CLEARED yesterday (hawkish — hike door open by year-end — but market SHRUGGING it off); (2) Iran/oil shock FADING, oil reversing LOWER Thu, war jitters easing. Thu futures GREEN (Dow +0.2%/S&P +0.3%/Nasdaq +0.5%), rotating to AI + SK Hynix US debut today. META held & higher (+4.29%, target weight, no add). Book ~96% cash → deployment-floor: named deployable MRK PRIMARY (defensive/oil-insensitive, cleanest into hawkish-Fed tape, HSBC $150/Scotia $155 — but consensus upside now thin ~2%, "valuation caught up" → diversifier starter), FDX SECONDARY (oil fuel-headwind now EASING as oil reverses). Both still spread-gated; /trade must re-sample LIVE 2-3x + require constructive tape. AI-hardware still gated (NVDA B200 lease soft though China H200 buys approving = new +; MU/AVGO WATCH into SK Hynix debut). Diversification: FDX + MRK + GEHC = 3 non-tech names (≥2 rule satisfied). New week 7/6 → 0 of 3 new-position slots used._

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, **+4.29%** (~$603), ~**4.21% of equity = target weight** (below 5% cap). Ad engine strong (Q1 rev $56.3B +33% YoY, on track to pass Google as #1 digital advertiser, Q2 guide $58–61B). "Meta Compute" cloud/MaaS thesis intact; new $9.1B Alberta data center. Standing bears: AI-oversupply worry + $125–145B 2026 capex; one rotation piece ("Wall St quietly dumping Meta for Google") = noise, not a catalyst. Strong Buy, no binary until earnings Jul 29. Both trailing legs live. Add only on a material pullback + fresh catalyst. (2026-07-09)
- **FDX** — **SECONDARY deployable / non-tech diversifier — SPREAD-GATED; oil headwind now EASING.** ~$312.88; Buy consensus (26 analysts), avg PT $349.72 (~12% up); Supply Chain unit divested $1.4B. **UPGRADE within-watch: the Wed oil +6% fuel-cost headwind is now EASING as oil reverses lower Thu** → FDX back to a live secondary deploy. Idea when spread clears: starter ~9-10 sh / ~$3k (≈3%), fresh 10% trail, a FRESH slot. **CAVEAT: paper quote remains pathologically wide (close snapshot ~11%) — /trade MUST re-sample spread LIVE 2-3x (<~2-3%) before any market buy.** (2026-07-09)
- **MRK** *(non-tech — NOW A HOLDING, opened 2026-07-09)* — **BOUGHT 23 sh @ $125.90 (~2.88%, 10% trail) on the 7/9 open** as the deployment-floor defensive starter (oil-insensitive, low-tech-correlation → the clean deploy into a hawkish-Fed + war/oil tape). Catalysts: **KEYTRUDA FDA approvals (TNBC + bladder), positive Ph3 tulisokibart (UC); HSBC PT $150 (Buy), Scotiabank $155 (Outperform)**; Buy consensus (29 analysts). Entry ~$126 → upside ~4.6% vs consensus PT $131.67 (better than the ~2% feared at ~$129). Earnings Aug 4. Risk: 2028 Keytruda patent cliff (~half of pharma rev). HOLD — manage per stop rules; add only on a fresh catalyst/pullback. (2026-07-09)
- **NVDA** — cautious-watch, **GATE STILL UNCONFIRMED — do NOT initiate.** **NEW positive: China approving LIMITED H200 purchases** (ByteDance/DeepSeek, ≤~200K units, training-only; NVDA +1% on 7/8) — incremental +, but the specific gate — **B200 lease pricing — is STILL soft** ($2.50–3.00 Q4 guide). Highest-priority tech watch; a buy is a fresh slot. (2026-07-09)
- **MU** — Burry short; memory sentiment tied to **SK Hynix US trading debut today** → don't chase, no base. WATCH. (2026-07-09)
- **AVGO** — improving (FV raised $476.78→$523.73; Hock Tan >$100B AI-semi rev by FY27 on $73B backlog + custom-ASIC deals). No clean base/entry. WATCH. (2026-07-09)
- **GEHC** *(non-tech)* — medtech; ~30% discount to ~$88 fair value; ~$62. Defensive diversifier. WATCH. (2026-07-09)
- _Energy (theme, not a name yet): the Iran oil pop is now reversing lower → chasing a fading geopolitical oil move = momentum trap. Note only — don't chase. (2026-07-09)_
