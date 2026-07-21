# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-21 ~16:02 ET (Tue **market-close wrap** routine) — LIVE read from `account` + `positions`. Market CLOSED (`is_open: false`, next open Wed 7/22 09:30 ET). **No trade at the close** (today's one trade was the FDX starter at the 7/21 open — already logged). No position at/below -7% (worst NVDA -2.34%, above the ~$196.91 cut); no winner ≥+15% to tighten. All 3 trailing stops confirmed live. **Regime: BOTH overhangs EASING → risk-on tape** (oil reversing on Iran ceasefire talks + Kimi K3 re-framed memory-bullish); see strategy.md/research-log.md.
- **Mode:** paper
- **Cash:** $91,737.55
- **Equity:** $100,373.39
- **Buying power:** ~$391,131 (regt ~$192,111)
- **Day P/L:** +$111.72 (+0.111%) — equity $100,373.39 vs last_equity $100,261.67.
- **vs. $100k paper start:** +$373.39 (+0.37%); account funded 2026-06-22
- **Invested:** ~8.60% (long mkt value $8,635.84); **~91.4% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $315.19 | +$19.71 (+0.70%) | 10% trailing, GTC, live (order 6f599c57, stop $285.30 / hwm $317) | Non-tech logistics diversifier (~2.83% of equity), opened 7/21 open. Day +2.93%. Bought on the risk-on tape as oil eases (Iran ceasefire talks) → fuel headwind easing; Citizens JMP "market outperform" PT $375, Buy consensus ~$350. 0-15% band → stop stays 10%. Risk: oil flip-flops with Iran headlines. |
| MRK | 23 | $125.90 | $126.27 | +$8.51 (+0.29%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.89% of equity). ~Flat from entry, day **+1.50%**. No new negative catalyst; Lipfendra (oral PCSK9) approval + raised FY guidance intact; PTs $140-150. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $206.78 | -$69.30 (-2.34%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.88%). Day **+1.72%** (recovered) — bear thesis SOFTENING (Kimi K3 now read memory-bullish, NVDA a possible net winner via more HBM/systems demand; tape risk-on). Above the -7% cut (~$196.91) & the $191.31 trail. HOLD, no add (don't average down; one green session ≠ confirmed bottom). |

_Notes: Tue 7/21 **market-close wrap** — no trade at the close (open BOUGHT FDX, midday NO-OP, close NO-OP → nothing to cut/tighten at the wrap). All 3 trailing legs confirmed live via `orders --status open` (qty_available 0 = shares held by the open stops). **No position at/below the -7% cut** (worst NVDA -2.34%, ~$9.87 above the ~$196.91 cut line); no winner ≥+15% to tighten (FDX +0.70%, MRK +0.29%, NVDA red). Day P/L +0.111% (far inside the -3% cap). Weekly slots: 1 of 3 used (FDX). EOD Telegram summary sent (close routine always notifies). Next routine: pre-market Wed 7/22._
