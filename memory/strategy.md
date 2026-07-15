# Strategy & Guardrails

_Last updated: 2026-07-15 ~07:10 ET (pre-market routine; research/drafting only, NO trades. Regime: **CPI gate now STRONGLY met — the June print was SOFTER than the 7/14 read** (core FLAT m/m, +2.6% y/y = lowest since Feb; headline -0.4% m/m, +3.5% y/y) → **Fed July-hike odds collapsed ~40%→~15%** (CME 85.6% hold) = a real tailwind for high-multiple tech; gate (a) MET more strongly. BUT the **Iran/Hormuz oil shock is STILL escalating — day-3 up, Brent >$85** (new US strikes + port blockade reinstated; Trump threatening power plants/bridges next week; partial de-escalation only — he DROPPED the 20% Hormuz shipping fee) → gate (b) "oil stabilizing/reversing" STILL FAILS. So the deploy gate has NARROWED to JUST oil/Iran, with the CPI side now a stronger tailwind: falling-knife still binds on the geopolitical driver; deployment stays gated. **NVDA = primary tech deployable the moment oil stabilizes** (lease firm ~$6 median; do NOT initiate today). Trigger: oil/Iran stabilizing (oil reversing/≥1 down session OR equities rallying through it) AND tight live spread. Today: **PPI 8:30 ET** + bank earnings (MS/BLK/PNC/BNY) + JNJ; **TSMC Thu 7/16 = AI-demand read**. FDX doubly-wrong (oil fuel headwind + spread-gated). META +14.5% at target weight, 7% trail (never loosen), +23% off June lows & 3 days >200-DMA; MRK -2.46% doing its defensive job — NEW: FDA bladder-cancer approval 7/14, WF $150/RBC $142/MS $113. Staying ~93% cash is a DELIBERATE logged decision. Weekly slots: 1 of 3 used (MRK).)_

_Prior (2026-07-09 07:10 ET) context: pre-market Thu; research/drafting only, NO trades this routine. Tape STABILIZING — the Wed hold-fire condition is LIFTING: (1) FOMC June minutes CLEARED yesterday (hawkish — "rates above current range by year-end" = hike door open — but market SHRUGGING it off), (2) Iran/oil shock FADING, oil reversing lower Thu, war jitters easing; Thu futures GREEN (Dow +0.2%/S&P +0.3%/Nasdaq +0.5%), focus rotating to AI + SK Hynix US debut today. Posture CONSTRUCTIVE, deployables now moving toward ACTIONABLE. META HELD +4.29%, ~4.21% of equity = target weight → no add. Deployment-floor: named deployable = MRK PRIMARY (defensive/oil-insensitive, cleanest into hawkish-Fed tape — but consensus upside now thin ~2%, treat as diversifier starter), FDX SECONDARY (oil fuel-headwind now EASING as oil reverses) — both still spread-gated on broken paper feed; /trade MUST re-sample spread LIVE 2-3x (<~2-3%) AND require a constructive tape before any starter. NVDA gate STILL unconfirmed (NEW +: China approving limited H200 buys, NVDA +1% — but B200 lease still soft) → do NOT initiate. Today's data: jobless claims 8:30 ET (second-tier). New week 7/6 → 0 of 3 new-position slots used.)._

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

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, **+14.5%** (~$662.30), ~**4.6% of equity = target weight** (below 5% cap). Thesis intact/strengthening: **+23% off late-June lows (vs +3% S&P), 3 days above the 200-DMA (longest since Feb)**; JPM (Anmuth) cites improved AI-strategy sentiment + external AI monetization + AI product cycle. Minor negs: employee lawsuit over AI-driven layoffs; **$50B single Louisiana data center → 5 GW (capex up)**; standing $125-145B '26 capex bear. Buy consensus, avg PT $836.76. No binary until earnings Jul 29. 7% trail live (never loosen). Add only on a material pullback + fresh catalyst. (2026-07-15)
- **FDX** — **DOUBLY-WRONG today — DOWNGRADED (2026-07-14).** Non-tech diversifier; Buy consensus (26 analysts), avg PT $349.72; Supply Chain unit divested $1.4B. But today it's the wrong deploy on TWO counts: (a) **oil +13% in two sessions to ~$86 = a direct fuel-cost margin headwind for FedEx**, and (b) still SPREAD-GATED on the broken/thin paper feed (~6.6% frozen last sampled). SKIP until oil reverses AND the quote normalizes. Thesis unchanged; retry when both clear. /trade MUST re-sample spread LIVE 2-3x (<~2-3%) before any market buy. (2026-07-14)
- **MRK** *(non-tech — NOW A HOLDING, opened 2026-07-09)* — **BOUGHT 23 sh @ $125.90 (~2.88%, 10% trail) on the 7/9 open** as the deployment-floor defensive starter (oil-insensitive, low-tech-correlation → the clean deploy into a hawkish-Fed + war/oil tape). Catalysts: **KEYTRUDA FDA approvals (TNBC + bladder), positive Ph3 tulisokibart (UC); HSBC PT $150 (Buy), Scotiabank $155 (Outperform)**; Buy consensus (29 analysts). Entry ~$126, now ~$122.80 (-2.46%). Earnings Aug 4. Risk: 2028 Keytruda patent cliff (~half of pharma rev). **NEW (7/14): FDA approved Keytruda + Keytruda QLEX w/ Padcev peri-op for muscle-invasive bladder cancer; analyst wave — Wells Fargo $150 (OW), RBC $142 (OP), Morgan Stanley raised to $113 (EW); avg PT $133.86 Buy.** Caveat: SeekingAlpha/SimplyWallSt "playbook working but valuation has caught up / fully valued." Oil-INSENSITIVE defensive → doing its job on the oil-spike tape. HOLD — manage per stop rules; add only on a fresh catalyst/pullback. (2026-07-15)
- **NVDA** — **PRIMARY tech deployable — gate NARROWED to JUST oil/Iran, CPI side now a STRONGER tailwind (2026-07-15).** (a) **CPI came in SOFTER than the 7/14 read** (core FLAT m/m, +2.6% y/y; Fed July-hike odds 40%→15%) = a real bullish tailwind for high-multiple tech; (b) **B200 lease FIRM** — Northflank $5.87/hr, median ~$6.16 (range $2.69→$18.53); providers guide $2.50-3.00 by Q4. **The ONLY remaining gate is the STILL-escalating oil/Iran shock** (Brent >$85, 3rd straight up session; new strikes + port blockade; Trump dropped the Hormuz fee = partial de-escalation only) — falling-knife still binds on that. **Do NOT initiate today.** Trigger: ~3% starter (fresh 10% trail, a FRESH slot) ONLY IF oil/Iran stabilizes (oil reversing/≥1 down session OR equities rallying through it) AND a live spread re-sampled 2-3x is tight. TSMC Thu 7/16 = AI-demand confirm. Highest-priority tech watch. (2026-07-15)
- **MU** — Burry short; memory sentiment tied to **SK Hynix US trading debut today** → don't chase, no base. WATCH. (2026-07-09)
- **AVGO** — improving (FV raised $476.78→$523.73; Hock Tan >$100B AI-semi rev by FY27 on $73B backlog + custom-ASIC deals). No clean base/entry. WATCH. (2026-07-09)
- **GEHC** *(non-tech)* — medtech; ~30% discount to ~$88 fair value; ~$62. Defensive diversifier. WATCH. (2026-07-09)
- _Energy (theme, not a name yet): the Iran oil pop is now reversing lower → chasing a fading geopolitical oil move = momentum trap. Note only — don't chase. (2026-07-09)_
