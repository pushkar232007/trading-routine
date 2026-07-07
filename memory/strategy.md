# Strategy & Guardrails

_Last updated: 2026-07-07 07:10 ET (pre-market Tue; research/drafting only, NO trades this routine. Posture CONSTRUCTIVE but respect the Wed 7/8 FOMC-minutes binary + today's semi-led RED tape [Samsung memory miss → Nasdaq futures -1%]. META HELD, +4.86%, ~4.24% of equity = target weight → no add; NEW positive (3rd-gen custom AI silicon talks). Book ~96% cash → deployment-floor LIVE: named deployable = FDX (non-tech, ungated by the tech binary) — but /trade must CHECK SPREAD first (7/6 quote was pathologically wide + un-buyable). MRK UPGRADED within watch (KEYTRUDA approvals + tulisokibart Ph3 + Scotiabank PT $155) = live backup deployable. NVDA gate still unconfirmed (Samsung read reinforces) → do NOT initiate. MU −4.9% premkt on Samsung → don't chase. Week's binary = Wed 7/8 FOMC June minutes. New week 7/6 → 0 of 3 new-position slots used.)._

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

_Context (07-07, Tue): posture CONSTRUCTIVE but data-gated. Mon 7/6 record close (Dow >53k); Tue futures RED (Nasdaq -1%) on Samsung memory miss → semi-led pullback into the Wed 7/8 FOMC June minutes (week's binary; no US CPI/NFP). META held & higher (+4.86%). Book ~96% cash → deployment-floor rule LIVE: named deployable = FDX (non-tech, ungated by the tech binary) but SPREAD-GATED. MRK upgraded within watch = live backup. AI-hardware names still gated (NVDA unconfirmed + Samsung read; MU -4.9% premkt on Samsung + Burry short; AVGO no base). Diversification: FDX + MRK + GEHC = 3 non-tech names (≥2 rule satisfied). New week 7/6 → 0 of 3 new-position slots used._

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, **+4.86%** ($606.55), ~**4.24% of equity = target weight** (below 5% cap). "Meta Compute" cloud thesis intact & reinforced (spiked 9%→$612.91 on 7/1). NEW positive: talks with chip makers for **3rd-gen custom AI silicon** (vertical integration, capex-efficiency). Minor negatives: India asked to DELAY WhatsApp username rollout (fraud); Zuck "AI agents slower than expected"; $145B 2026 capex = standing bear worry — not thesis-breaking. Strong Buy, no binary until earnings Jul 29. Both trailing legs live. Add only on a material pullback + fresh catalyst. (2026-07-07)
- **FDX** — **PRIMARY deployable / non-tech diversifier, but SPREAD-GATED.** CMA CGM buying Supply Chain unit $1.4B (2nd asset sale after Freight spin → refocus on core parcel). 16 Strong Buy, avg PT $355.64 (~13% up from ~$314), well below 52wk high $404. Ungated by the AI re-rate or the Wed FOMC tech binary → cleaner deploy on a semi-led red day. Idea: starter ~9-10 sh / ~$3k (≈3%), fresh 10% trail, a FRESH slot. **CAVEAT: 7/6 paper quote was pathologically wide (bid $296/ask $330) and blocked a clean fill — /trade MUST check spread (<~2-3%) before any market buy.** (2026-07-07)
- **MRK** *(non-tech — UPGRADED within watch)* — real near-term catalysts: **new KEYTRUDA FDA approvals (TNBC + bladder), positive Phase 3 tulisokibart (UC); Scotiabank PT raised to $155 (Outperform)**; Buy consensus, median PT $130 vs ~$121; 3.1% div. H2-2026 pipeline re-rate setup; low correlation to the AI book. Risk: China trial scrutiny. Live BACKUP deployable if FDX's quote stays broken; want a specific entry/pullback. (2026-07-07)
- **NVDA** — cautious-watch, **GATE STILL UNCONFIRMED — do NOT initiate.** B200 lease still ~$4.22 (−31%), China DC rev ~$0, Burry short, ~40x P/E; Samsung's soft memory read reinforces caution. Analysts Strong Buy (38)/$299 PT but tape unconfirmed. Highest-priority tech watch; a buy is a fresh slot. (2026-07-07)
- **MU** — **−4.9% premkt Tue on Samsung/SK Hynix drop** despite own record Q3; Burry short + breaking down + Samsung sentiment read-through → do NOT chase. WATCH. (2026-07-07)
- **AVGO** — improving (FV raised $476.78→$523.73; Hock Tan >$100B AI-semi rev by FY27 on $73B backlog + custom-ASIC deals). No clean base/entry. WATCH. (2026-07-06)
- **GEHC** *(non-tech)* — medtech; ~30% discount to ~$88 fair value; ~$61.65. Defensive diversifier. WATCH. (2026-07-06)
