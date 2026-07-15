# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-15 ~16:02 ET (market-close wrap routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, next open 2026-07-16 09:30 ET).
- **Mode:** paper
- **Cash:** $90,090.91
- **Equity:** $100,674.89
- **Buying power:** $389,998.78
- **Day P/L:** +$214.54 (+0.21%) — equity $100,674.89 vs last_equity $100,460.35. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$674.89 (+0.67%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $680.90 | +$717.16 (+17.71%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; tightened to 7% on 7/10, auto-ratcheting up on new highs — never loosen) | Core AI name (~4.73% of equity = target weight). Fresh highs today (+3.00%). +17.71% sits in the 15-30% ratchet band → target trail 7%; already at 7% → no change (never loosen). JPM cites AI-strategy sentiment + external AI monetization + AI product cycle. Buy consensus, avg PT $836.76. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $123.61 | -$52.67 (-1.82%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.82%). Day +2.34% (defensive firming). -1.82%, well above the ~$117.09 -7% cut. FDA bladder-cancer approval 7/14; WF $150/RBC $142/MS $113, avg PT $133.86. Earnings Aug 4. Risk: Keytruda patent cliff. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $212.40 | +$9.38 (+0.32%) | **10% trailing**, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | Primary tech deployable, ~2.95%. Opened 7/15 market-open (gate cleared via equities-rallying-through-oil branch: benign CPI+PPI + bullish ASML AI read). Closed day-1 slightly GREEN (+0.32%, day +0.28%) — recovered from the midday -1.84% red. Fresh 10% trail; oil/Iran still the macro overhang. B200 lease firm ~$6; TSMC AI-demand confirm Thu 7/16. HOLD — manage per stop rules. |

_Notes: Wed 7/15 **market-close wrap** — **NO-OP, HOLD all 3.** No cut (worst MRK -1.82% ≫ -7%), no tighten (META +17.71% is in the 15-30% band but both legs already at 7% since 7/10, never loosen; MRK/NVDA green-to-flat → ratchet N/A). All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%; NVDA hwm ratcheted to $212.5693 on today's high). Book ~89.5% cash (~$90.1k dry powder). **Weekly slots: 2 of 3 used (MRK + NVDA).** EOD Telegram summary sent (close routine always notifies). Next routine: pre-market Thu 7/16 (TSMC Q2 ~2am ET = AI-demand read for NVDA/AVGO/MU)._
