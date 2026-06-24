# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-06-24 10:38 ET (market-open re-fire — standing plan already deployed, no new trade)
- **Mode:** paper
- **Cash:** $97,748.76
- **Equity:** $99,994.12
- **Buying power:** $397,282.05
- **Day P/L:** -$5.88 (-0.006%, essentially flat — META drifting with the market, no meaningful move)
- **vs. S&P 500 (since inception):** ~flat — account funded 2026-06-22, only position is the META starter

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 4 | $562.81 | $561.42 | -$5.56 (-0.25%) | 10% trailing stop, stop_price $508.05 (hwm $564.50) | Half-size starter on macro AI/tech rout dip (day-3 selloff, no company-specific bad news, no earnings binary until Jul 29, Strong Buy consensus avg PT $827). Plan: add after confirmation. |

_Notes: Market-open routine re-fired at 10:38 ET with `is_open: true`. Standing pre-market plan is
fully deployed — META half-size starter (2.25% of equity) live with active 10% trailing stop. No new
trade this run: META add held for confirmation (day-3 rout, MU binary tonight); MU bars buying into
tonight's print; FDX/NVDA/AVGO watch-only. 1 of 3 weekly new-position slots used. MU reports fiscal
Q3 after close tonight (6/24) — reassess Thu AM. Known script bug still open: `cmd_buy` should wait
for the buy fill before submitting the trailing-stop leg (worked around manually on the original buy)._
