# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-23 ~13:05 ET (Thu **midday risk-check** routine) — snapshot from live `account` + `positions`. **NO trades this routine** — clean risk check: no position at/below the -7% cut, no winner ≥+15% to tighten. All 3 trailing stops live & confirmed via `orders --status open`. Regime: **oil at a saga high (Brent >$98) + GOOGL capex-hot (net-bullish for NVDA), sell-semis rotation circulating.**
- **Mode:** paper
- **Cash:** $91,737.54
- **Equity / portfolio value:** $100,500.58 (last_equity field reads 0/stale intraday — value is live)
- **Buying power:** $91,737.54
- **Invested:** ~8.7% (long mkt value $8,763.04); **~91.3% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**
- **vs. $100k paper start:** ~+$501 (+0.50%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $315.50 | +$22.52 (+0.80%) | 10% trailing, GTC, live (order 6f599c57, stop $289.8945 / hwm $322.105) | Non-tech logistics diversifier (~2.83% of equity), opened 7/21. **Oil >$98 fuel headwind biting — day -1.72%, giving back some of yesterday's +1.85% — but still green, well inside the trail.** Most oil-exposed holding → WATCH; let the 10% trail manage risk, don't pre-emptively cut (7/22 head-fake lesson). 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | $130.07 | +$95.80 (+3.31%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.98% of equity). Day's winner (+2.04%), doing its job on a new oil-spike high. Lipfendra (oral PCSK9) + Keytruda/Qlex oncology intact; Buy, avg PT $134, bull range $138-155. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $209.46 | -$31.78 (-1.07%) | 10% trailing, GTC, live (order 92b2b072, stop $192.951 / hwm $214.39) | AI-hardware starter, opened 7/15 (~2.92%). **GOOGL's capex raise to $195-205B = net-bullish read-through** (extends the AI-chip cycle), though a "sell-semis/buy-hyperscalers" rotation is circulating. -1.07% on live feed, above the -7% cut (~$196.91) & the $191.31 trail. 0-15% band → stop stays 10%. **HOLD, no add** (risk-off oil tape; MSFT/META 7/29 = next confirm). |

_Notes: Thu 7/23 **midday risk check** — NO trades; HOLD all three. All 3 trailing legs live (qty_available 0 = shares held by the open stops). **No position at/below the -7% cut** (worst NVDA -1.07%); no winner ≥+15% to tighten (MRK +3.31%, FDX +0.80%, NVDA -1.07%). **GEHC (primary deployable) still not deployed — deliberate: oil at a saga high = risk-off + GEHC Q2 earnings 7/29 (~4 sessions out) → don't deploy right into the print.** Weekly slots: 1 of 3 used (FDX). Next routine: market-close wrap Thu 7/23._
