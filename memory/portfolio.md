# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-20 ~16:02 ET (Mon **market-close wrap** routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, 16:02 ET, next open Tue 7/21 09:30). **No trades today — clean NO-OP day (open + midday + close all NO-OP).** No position at/below -7% (worst NVDA -4.03%, above the ~$196.91 cut); no winner ≥+15% to tighten. Both trailing-stop legs confirmed live. **Regime: confirmed semiconductor BEAR MARKET (Kimi K3) + oil spiking — risk-off; see strategy.md/research-log.md.**
- **Mode:** paper
- **Cash:** $94,554.55
- **Equity:** $100,260.64
- **Buying power:** $394,195.25
- **Day P/L:** -$65.75 (-0.066%) — equity $100,260.64 vs last_equity $100,326.39.
- **vs. $100k paper start:** +$260.64 (+0.26%); account funded 2026-06-22
- **Invested:** ~5.7% (long mkt value $5,706.09); **~94.3% cash.** New week 7/20 → 0 of 3 new-position slots used.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| MRK | 23 | $125.90 | $124.41 | -$34.27 (-1.18%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.85% of equity). Intraday -2.42% (day's laggard but held far above its cut). Essentially flat from entry → 0-15% band, stop stays 10%. Well above the ~$117.09 -7% cut. Lipfendra (oral PCSK9) FDA approval 7/16; PTs $140-150. Doing its job in a semi-rout + oil-spike tape. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $203.19 | -$119.56 (-4.03%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.84%). Intraday +0.19% (holding above $200). **The -4.03% slide is a structural semi bear-market re-rating (Kimi K3 open-weight model, SOX -20% from peak) — higher bar to hold, do NOT average down.** Above the -7% cut (~$196.91) & the $191.31 trail. HOLD, no add. |

_Notes: Mon 7/20 **market-close wrap**, market CLOSED (`is_open: false`, 16:02 ET) — properly-timed close run. No trades today: open + midday + close all NO-OP. Close wrap = nothing to cut/tighten. **NVDA -7% cut re-check: current $203.19 is above the ~$196.91 -7% cut line → HOLD, no cut required.** The slide remains a structural semi bear-market re-rating (Kimi K3), not a fresh thesis-breaker; steadied intraday (+0.19%). MRK -2.42% intraday (day's laggard) but ~flat from entry (-1.18%), oil-insensitive defensive still well above its cut. No winner ≥+15% → no stop-tightening. Both trailing legs live & confirmed (NVDA stop $191.31237 / hwm $212.5693; MRK stop $118.566 / hwm $131.74). **Regime: the semiconductor complex is in a confirmed BEAR MARKET** (Kimi K3 drove SOX/SOXX >20% off its June-2 peak) + oil spiking (Brent ~$88, Iran) → risk-off; falling-knife binds for tech, so ~94.3% cash is the DELIBERATE logged decision. EOD Telegram summary sent (close routine always notifies). Weekly slots: 0 of 3 used (new week). Next routine: pre-market Tue 7/21._
