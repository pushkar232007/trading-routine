# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-24 ~16:02 ET (Fri **market-close wrap** — NO trades today, HOLD all 3, no cut/tighten) — snapshot from live `account` + `positions`, market CLOSED (`is_open: false`, next open Mon 7/27). Regime: **oil dipped off Thu's >$100 spike (fuel headwind easing); Friday finished roughly flat after the S&P's worst-day-in-a-month Thursday.**
- **Mode:** paper
- **Cash:** $91,737.54
- **Equity / portfolio value:** $100,484.58 (last_equity $100,501.80)
- **Buying power:** $391,441.86 (margin multiplier; non-marginable $96,111.05)
- **Invested:** ~8.7% (long mkt value $8,747.04); **~91.3% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**
- **Day P/L (close):** **-$17.22 (-0.017%)** (equity $100,484.58 vs last_equity $100,501.80) — essentially flat (FDX -$5.94, MRK +$13.92, NVDA -$25.20). Far inside the -3% daily cap.
- **vs. $100k paper start:** ~+$485 (+0.48%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $314.96 | +$17.64 (+0.63%) | 10% trailing, GTC, live (order 6f599c57, stop $289.8945 / hwm $322.105) | Non-tech logistics diversifier (~2.82% of equity), opened 7/21. Oil dipped off Thu's >$100 spike → fuel headwind easing; day ~flat (-0.21%), still green from entry. Most oil-exposed holding → WATCH; let the 10% trail manage risk, don't pre-emptively cut (7/22 head-fake lesson). 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | $131.085 | +$119.26 (+4.12%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~3.00% of equity). **Book's best performer** — did its job on the oil tape all week; day +0.46%; fresh Buy/$141 PT (7/24) on ISLEND HIV upside. Lipfendra (oral PCSK9) + Keytruda/Qlex oncology intact. Buy, avg PT ~$134, bull range $138-155. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $206.96 | -$66.78 (-2.25%) | 10% trailing, GTC, live (order 92b2b072, stop $192.951 / hwm $214.39) | AI-hardware starter, opened 7/15 (~2.88%). Day -0.86% — gave back Fri after Intel's beat; still the group laggard on the Thu rotation OUT of NVDA/Mag7 into specialized semis. Above the -7% cut (~$196.91) & the $191.31 trail. 0-15% band → stop stays 10%. **HOLD, no add** (MSFT/META 7/29 = next confirm). |

_Notes: Fri 7/24 **market-close wrap** — NO trades today (open + midday + close all NO-OP), HOLD all three, no cut/tighten. All 3 trailing legs live & confirmed via `orders --status open` (qty_available 0 = shares held by the open stops). **No position at/below the -7% cut** (worst NVDA -2.25%); no winner ≥+15% to tighten (MRK +4.12%, FDX +0.63%, NVDA red). **GEHC (primary deployable) still not deployed — deliberate: Q2 print 7/29 before open (~3 sessions out) + the 7/29-30 binary stack (FOMC/GDP/PCE + MSFT/META/GEHC 7/29, AAPL/AMZN 7/30) → don't deploy right into the print.** Weekly slots: 1 of 3 used (FDX). Equity +$485 (+0.48%) vs the $100k start. EOD Telegram summary sent (close routine always notifies). Next routine: pre-market Mon 7/27._
