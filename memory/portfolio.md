# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-06-24 09:55 ET (market-open routine — executed standing META plan)
- **Mode:** paper
- **Cash:** $97,748.76
- **Equity:** $100,000.22
- **Buying power:** $397,299.13
- **Day P/L:** +$0.22 (essentially flat — META fill basically at quote, no meaningful move yet)
- **vs. S&P 500 (since inception):** ~flat — account funded 2026-06-22, first trade placed today

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 4 | $562.81 | $562.79 | -$0.10 (-0.004%) | 10% trailing stop, stop_price $506.43 | Half-size starter on macro AI/tech rout dip (day-3 selloff, no company-specific bad news, no earnings binary until Jul 29, Strong Buy consensus avg PT $827). Plan: add after confirmation. |

_Notes: Market-open routine confirmed `is_open: true` and executed the standing half-size META
starter from the 07:00 ET pre-market plan (2.25% of equity, within the 5% max). 1 of 3 weekly new-
position slots used. MU reports fiscal Q3 after close tonight (6/24) — do not buy into the print,
reassess Thu AM per pre-market plan. FDX/NVDA/AVGO remain watch-only. Hit a script bug placing the
trailing stop (see trade-log.md note) — worked around it manually, stop is live. Script fix still
needed: `cmd_buy` should wait for the buy fill before submitting the trailing-stop leg._
