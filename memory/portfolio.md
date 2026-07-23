# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-23 ~09:31 ET (Thu **market-open** routine) — snapshot from live `account` + `positions`. **NO trades this routine** — executed the pre-market plan = HOLD all three, no adds; deployment-floor deliberate cash. All 3 trailing stops live & confirmed via `orders --status open`. No position at/below the -7% cut; no winner ≥+15% to tighten. Regime: **oil at a saga high (Brent >$98) + GOOGL capex-hot (net-bullish for NVDA), sell-semis rotation circulating.**
- **Mode:** paper
- **Cash:** $91,737.54
- **Equity / portfolio value:** $100,485.06 (last_equity field reads 0/stale intraday — value is live)
- **Buying power:** $91,737.54
- **Invested:** ~8.7% (long mkt value $8,747.52); **~91.3% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**
- **vs. $100k paper start:** ~+$485 (+0.49%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $320.00 | +$63.00 (+2.24%) | 10% trailing, GTC, live (order 6f599c57, stop $289.8945 / hwm $322.105) | Non-tech logistics diversifier (~2.87% of equity), opened 7/21. **Oil >$98 = the worst fuel headwind since entry (the flip-flop risk at its peak) — BUT shrugged off $94 → still green, well inside the trail.** Most oil-exposed holding → WATCH at midday; let the 10% trail manage risk, don't pre-emptively cut (7/22 head-fake lesson). 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | $127.99 | +$48.07 (+1.66%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.93% of equity). Doing its job on a new oil-spike high. Lipfendra (oral PCSK9) + Keytruda/Qlex oncology intact; Buy, avg PT $134, bull range $138-155. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $209.29 | -$34.17 (-1.15%) | 10% trailing, GTC, live (order 92b2b072, stop $192.951 / hwm $214.39) | AI-hardware starter, opened 7/15 (~2.92%). **GOOGL's capex raise to $195-205B = net-bullish read-through** (extends the AI-chip cycle), though a "sell-semis/buy-hyperscalers" rotation is circulating. -1.15% on live feed, above the -7% cut (~$196.91) & the $191.31 trail. 0-15% band → stop stays 10%. **HOLD, no add** (risk-off oil tape; MSFT/META 7/29 = next confirm). |

_Notes: Thu 7/23 **market-open** — NO trades; executed the plan = HOLD all three. All 3 trailing legs live (qty_available 0 = shares held by the open stops). **No position at/below the -7% cut**; no winner ≥+15% to tighten (FDX +2.24%, MRK +1.66%, NVDA -1.15%). **GEHC (primary deployable) NOT deployed — deliberate: oil at a saga high = risk-off + GEHC Q2 earnings 7/29 (~4 sessions out) → don't deploy right into the print.** Weekly slots: 1 of 3 used (FDX). Next routine: midday Thu 7/23 — risk check (re-check the -7% cut on NVDA/FDX vs live oil; tighten any winner crossing +15%)._
