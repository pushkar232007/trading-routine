# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-16 ~13:05 ET (midday risk-check routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 16:00 ET). NO trades this routine.
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,617.03
- **Buying power:** $389,836.75
- **Day P/L:** -$61.07 (-0.06%) — equity $100,617.03 vs last_equity $100,678.10. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$617.03 (+0.62%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $669.03 | +$634.07 (+15.66%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; at 7% since 7/10, auto-ratcheting up on new highs — never loosen) | Core AI name (~4.65% of equity = target weight). Day -1.80% (mild give-back off yesterday's highs). +15.66% now in the 15-30% ratchet band → target trail 7%; already at 7% → no change (never loosen). Earnings Jul 29. HOLD — add complete, no add. |
| MRK | 23 | $125.90 | $127.985 | +$47.96 (+1.66%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.308 / hwm $128.12) | Defensive/oil-insensitive pharma starter (~2.93%). +3.54% today. **Ph3 KEYNOTE-C93 win (Keytruda PFS in MMR-deficient endometrial cancer); JPM PT→$140.** +1.66% from entry, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $207.10 | -$64.82 (-2.19%) | **10% trailing**, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.88%). Day-3 starter, -2.19% from entry, ≫ the -7% cut & above the $191.31 trail. Soft-tech session (-2.54% today). **TSMC Q2 record beat + AI demand "extremely robust" confirmed thesis.** HOLD — manage per stop rules; do NOT add a fresh position. |

_Notes: Thu 7/16 **midday risk check** — NO trades. No position at/below the -7% cut (worst NVDA -2.19%); META crossed into the 15-30% ratchet band but both legs already at 7% target → no change (never loosen). All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). Book ~89.5% cash (~$90.1k dry powder). Weekly slots: 2 of 3 used (MRK + NVDA this week). No Telegram (nothing closed). Next routine: market-close wrap 7/16._
