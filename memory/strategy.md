# Strategy & Guardrails

_Last updated: 2026-07-06 07:10 ET (pre-market, first session back post-July 4; research/drafting only, NO trades this routine. Posture CONSTRUCTIVE. META HELD, +2.17%, ~4.13% of equity = target weight → no add. Book ~96% cash → deployment-floor rule LIVE: named deployable = FDX (non-tech industrial, improving, ungated by the Wed FOMC tech binary) — starter ~3% if tape is constructive this week; a fresh slot. NVDA gate still doubly-unconfirmed → do NOT initiate. MU now has a Michael Burry SHORT + breaking down → don't chase. Added MRK + GEHC as non-tech watchlist diversifiers (≥2-non-tech rule). Week's binary = Wed 7/8 FOMC June minutes. New week 7/6 → 0 of 3 new-position slots used.)._

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

_Context (07-06, first session back post-July 4): posture CONSTRUCTIVE. Light data week; Wed 7/8 FOMC June minutes is the binary (no US CPI/NFP). META held & higher (+2.17%). Book ~96% cash → deployment-floor rule LIVE this week: named deployable = FDX (non-tech). AI-hardware names all still gated (NVDA doubly-unconfirmed; MU now has a Michael Burry short + breaking down; AVGO improving but no base). Diversification: FDX + MRK + GEHC = 3 non-tech names now on the list (≥2 rule satisfied). New week 7/6 → 0 of 3 new-position slots used._

- **META** — HOLD, **add COMPLETE — no further add.** 7 sh @ $578.45 blended, **+2.17%** (~$591), ~**4.13% of equity = target weight** (near 5% cap). "Meta Compute" cloud thesis intact (rent excess AI compute → answers the capex-monetization bear case). Minor overnight negatives (Zuck: AI agents "slower than anticipated"; India child-abuse-content order) — not thesis-breaking. 2026 capex ~2x '25 = standing bear worry. Strong Buy, no binary until earnings Jul 29. Both trailing legs live. Add only on a material pullback + fresh catalyst. (2026-07-06)
- **FDX** — **PRIMARY deployable / non-tech diversifier.** Improving: divesting Supply Chain unit $1.4B (refocus on core), UBS + Wells Fargo Buy early July, Buy consensus (15B/2H/1S), avg PT $367.61 (~17% up from ~$313), P/E 16.9, 1.78% div. Based-and-improving industrial, ungated by the AI re-rate or the Wed FOMC tech binary. Idea: starter ~9-10 sh / ~$3k (≈3%), fresh 10% trail, a FRESH slot, on a constructive tape this week. Alpaca mid ~$313 (bid $299/ask $328, Thu close). (2026-07-06)
- **NVDA** — cautious-watch, **GATE STILL DOUBLY-UNCONFIRMED — do NOT initiate.** Bull pieces tout Blackwell sold-out / Rubin-early / hyperscaler capex, but the two concrete gating bears are unresolved: B200 lease forward-guide-down to $2.50–3.00 by Q4 + WSJ OpenAI demand-miss. Highest-priority tech watch; a buy is a fresh slot. (2026-07-06)
- **MU** — **NEW: Michael Burry disclosed a SHORT** (AI-bubble/valuation) despite record earnings; fell ~15% in two sessions, <$1,000 first time since 6/12. Offsets (HBM sold out '26, GM partnership, Japan fab) don't change the tape. Breaking down + high-profile short → do NOT chase. WATCH. (2026-07-06)
- **AVGO** — improving: fair value raised $476.78 → $523.73; Hock Tan reaffirms >$100B AI-semi rev by FY27 on $73B backlog + custom-ASIC deals (Google/Meta/OpenAI/Anthropic). No clean base/entry yet. WATCH. (2026-07-06)
- **MRK** *(non-tech)* — large-cap pharma, 3.1% div, defensive value; ~$121. Low correlation to the AI-tech book. WATCH — want a specific catalyst/entry before initiating. (2026-07-06)
- **GEHC** *(non-tech)* — medtech; cited ~30% discount to ~$88 fair value; ~$61.65. Defensive diversifier. WATCH. (2026-07-06)
