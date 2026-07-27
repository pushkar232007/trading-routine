# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-27 ~16:05 ET (Mon **market-close wrap** — HOLD FDX + MRK, no cut/tighten; market CLOSED) — snapshot from live `account` + `positions`. Regime: **RISK-OFF day — Kimi K3 weights dropped today, NVDA sold off through the -7% cut and was CLOSED at midday (realized -$221.20). Biggest binary week of the quarter dead ahead: FOMC 7/29 + GDP/PCE 7/30 + MSFT/META/GEHC 7/29, AAPL/AMZN 7/30.**
- **Mode:** paper
- **Cash:** $94,480.56
- **Equity / portfolio value:** $100,285.15 (last_equity $100,482.55)
- **Buying power:** ~$394,175.09 (margin multiplier; non-marginable ~$96,011)
- **Invested:** ~5.8% (long mkt value $5,804.59); **~94.2% cash.** New week 7/27 → **1 of 3 new-position slots used (FDX)** — a close does not consume a slot.
- **Day P/L:** **-$197.40 (-0.20%)** (equity $100,285.15 vs last_equity $100,482.55) — driven by the NVDA loss-cut. Far inside the -3% daily cap.
- **vs. $100k paper start:** ~+$285 (+0.29%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | ~$310.79 | -$19.89 (-0.71%) | 10% trailing, GTC, live (order 6f599c57, stop $289.8945 / hwm $322.105) | Non-tech logistics diversifier (~2.79% of equity), opened 7/21. Weekend oil relief eased the fuel headwind; gave back intraday (-1.32% today) as oil ticked back up. RJ PT $330, kept Outperform. 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | ~$130.76 | +$111.78 (+3.86%) | 10% trailing, GTC, live (order 3d2f860f, stop $119.277 / hwm $132.53) | Defensive/oil-insensitive pharma (~3.00% of equity). Book's best performer — bullish PTs $138-155; Keytruda/Qlex oncology intact. Running (+3.86%), not a pullback → MRK-add trigger NOT met. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |

_Notes: Mon 7/27 **market-close wrap** — NO trades at the close (open + close NO-OP; the day's one trade was the **midday NVDA loss-cut**: sold 14 sh @ $195.93, realized -$221.20 / -7.46%, on the hard -7% rule as the Kimi K3 weights dropped and NVDA sold ~-5.3%). Remaining book = 2 holdings, both stop-protected (both trailing legs verified live via `orders --status open`; NVDA's stop correctly gone). No position at/below the -7% cut (FDX -0.71%, MRK +3.86%); no winner ≥+15% → both stops stay 10% (ratchet N/A). Book ~94.2% cash (~$94.5k dry powder). GEHC (primary deployable) still SKIPPED — 7/29 print 2 sessions out; evaluate the REACTION post-print. Weekly slots: 1 of 3 used (FDX). EOD Telegram summary sent (close always notifies). Next routine: pre-market Tue 7/28._
