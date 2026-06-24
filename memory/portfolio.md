# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-06-24 01:33 ET (weekly-review routine — fired pre-open, market closed)
- **Mode:** paper
- **Cash:** $100,000.00
- **Equity:** $100,000.00
- **Buying power:** $400,000.00 (4x margin available — not used; no margin per guardrails)
- **Day P/L:** $0.00 (no positions, no trades)
- **vs. S&P 500 (since inception):** flat — account funded 2026-06-22, no trades placed yet

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| _none yet_ | | | | | | |

_Notes: Still a fully-cash $100k paper account — no positions. Weekly-review routine fired at 01:33 ET
while market was closed (`is_open: false`) — same ~8h-early mistiming as all of today's runs. Inception
week (funded 06-22) graded **D**: 0 trades, 0.00% vs S&P +1.6% (delta -1.6%) — sat in cash because the
timing bug blocked every execution routine. Fixes applied: catch-up rule in trade.md + escalate-once on
misfire in signals-learnings.md; cron-timezone fix flagged to human. Pre-market META starter still stands
for the next real open: initiate ~5% META w/ 10% trailing stop; hold off MU/FDX; cautious into Thu Jun 26 PCE._
