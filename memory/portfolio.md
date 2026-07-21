# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-21 ~13:08 ET (Tue **midday risk check** routine) — LIVE read from `account` + `positions`. Market OPEN (`is_open: true`, next close 16:00 ET). **No trade placed.** No position at/below -7% (worst NVDA -3.02%, above the ~$196.91 cut); no winner ≥+15% to tighten. All 3 trailing stops confirmed live. **Regime: BOTH overhangs EASING → risk-on tape** (oil reversing on Iran ceasefire talks + Kimi K3 re-framed memory-bullish); see strategy.md/research-log.md.
- **Mode:** paper
- **Cash:** $91,737.55
- **Equity:** $100,333.91
- **Buying power:** ~$391,020 (regt ~$192k)
- **Day P/L:** +$72.24 (+0.072%) — equity $100,333.91 vs last_equity $100,261.67.
- **vs. $100k paper start:** +$333.91 (+0.33%); account funded 2026-06-22
- **Invested:** ~8.57% (long mkt value $8,596.36); **~91.4% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $315.42 | +$21.74 (+0.77%) | 10% trailing, GTC, live (order 6f599c57, stop $285.30 / hwm $317) | Non-tech logistics diversifier (~2.83% of equity), opened 7/21 open. Day's winner (+3.00%). Bought on the risk-on tape as oil eases (Iran ceasefire talks) → fuel headwind easing; Citizens JMP "market outperform" PT $375, Buy consensus ~$350. Trail already ratcheted up intraday (hwm $317). 0-15% band → stop stays 10%. Risk: oil flip-flops with Iran headlines. |
| MRK | 23 | $125.90 | $125.36 | -$12.42 (-0.43%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.87% of equity). ~Flat from entry, day +0.77%. No new negative catalyst; Lipfendra (oral PCSK9) approval + raised FY guidance intact; PTs $140-150. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $205.33 | -$89.61 (-3.02%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.86%). Day **+1.01%** (recovering intraday) — bear thesis SOFTENING (Kimi K3 now read memory-bullish, NVDA a possible net winner via more HBM/systems demand; tape risk-on). Above the -7% cut (~$196.91) & the $191.31 trail. HOLD, no add (don't average down; one green session ≠ confirmed bottom). |

_Notes: Tue 7/21 **midday risk check** — pure risk pass, no new positions (midday is risk-only). All 3 trailing legs confirmed live via `orders --status open`. **No position at/below the -7% cut** (worst NVDA -3.02%, ~$8.42 above the ~$196.91 cut line); no winner ≥+15% to tighten (FDX +0.77%, MRK ~flat, NVDA red). FDX's 10% trail has already ratcheted up intraday (hwm $312.60 → $317, stop $281.34 → $285.30). Day P/L +0.072% (far inside the -3% cap). Weekly slots: 1 of 3 used (FDX). No Telegram (nothing closed). Next routine: market-close wrap 7/21 — EOD summary + re-check NVDA's -7% cut (~$196.91)._
