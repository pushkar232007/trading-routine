# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-22 ~09:31 ET (Wed **market-open** routine) — LIVE read from `account` + `positions`. Market OPEN (`is_open: true`, next close 16:00 ET). **NO trades this routine — HOLD all 3.** No position at/below the -7% cut (worst NVDA -2.83%, ~$8.83 above the ~$196.91 cut); no winner ≥+15% to tighten. All 3 trailing stops live. **Regime: RISK-OFF** — oil re-spiking (Brent ~$94, Iran ceasefire stalled) + chips cooling into GOOGL/TSLA earnings tonight. Deployment-floor: GEHC named (feed frozen + risk-off tape → skipped); logged deliberate cash. See strategy.md/research-log.md.
- **Mode:** paper
- **Cash:** $91,737.54
- **Equity:** $100,376.09
- **Buying power:** ~$391,138 (regt ~$192,114)
- **Day P/L:** -$4.20 (-0.004%) — equity $100,376.09 vs last_equity $100,380.29 (~flat; MRK green, FDX ~flat, NVDA red on the risk-off tape).
- **vs. $100k paper start:** +$376.09 (+0.38%); account funded 2026-06-22
- **Invested:** ~8.61% (long mkt value $8,638.55); **~91.4% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $314.95 | +$17.55 (+0.62%) | 10% trailing, GTC, live (order 6f599c57, stop $285.30 / hwm $317) | Non-tech logistics diversifier (~2.82% of equity), opened 7/21. **Oil re-spike to ~$94 (Iran ceasefire stalled) revives the fuel-cost headwind — the logged flip-flop risk materializing.** Most oil-exposed holding; inside the trail (not a cut). 0-15% band → stop stays 10%. WATCH at midday. |
| MRK | 23 | $125.90 | $127.06 | +$26.68 (+0.92%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.91% of equity). Doing its job on an oil-spike risk-off day (intraday +0.63%). Lipfendra (oral PCSK9) + Keytruda/Qlex oncology approvals intact; PTs $138-155. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $205.74 | -$83.86 (-2.83%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.87%). Chips cooling on the risk-off tape; worst chip performer 2026 (~-18% off June high) but thesis intact (Goldman 21.7x "compelling"). Above the -7% cut (~$196.91) & the $191.31 trail. **GOOGL/TSLA earnings tonight = the AI-capex read-through.** HOLD, no add (don't average down; don't add into the binary). |

_Notes: Wed 7/22 **market-open** — NO trades, HOLD all 3. All 3 trailing legs live (qty_available 0 = shares held by the open stops). **No position at/below the -7% cut** (worst NVDA -2.83%); no winner ≥+15% to tighten (MRK +0.92%, FDX +0.62%, NVDA red). Day P/L -0.004% (far inside the -3% cap). **GEHC (primary deployable) SKIPPED** — frozen paper feed (3 identical timestamps) + oil-driven risk-off tape + GOOGL/TSLA binary tonight = not a tape to add risk into; deployment-floor satisfied (named + gated + logged cash reason). Weekly slots: 1 of 3 used (FDX). Next routine: midday risk check — re-check NVDA's -7% cut (~$196.91) & FDX on the oil headwind._
