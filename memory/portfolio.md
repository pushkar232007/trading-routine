# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-15 ~13:05 ET (midday risk-check routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 16:00 ET).
- **Mode:** paper
- **Cash:** $90,090.91
- **Equity:** $100,572.59
- **Buying power:** $389,712.35
- **Day P/L:** +$112.24 (+0.11%) — equity $100,572.59 vs last_equity $100,460.35. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$572.59 (+0.57%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $675.25 | +$677.61 (+16.74%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; tightened to 7% on 7/10, auto-ratcheting up on new highs — never loosen) | Core AI name (~4.70% of equity = target weight). +16.74% has now CROSSED into the 15-30% ratchet band → target trail 7%; already at 7% → no change (never loosen). Fresh highs today (+2.15%). JPM cites AI-strategy sentiment + external AI monetization. Buy consensus, avg PT $836.76. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $123.755 | -$49.34 (-1.70%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.83%). -1.70%, well above the ~$117.09 -7% cut. FDA bladder-cancer approval 7/14; WF $150/RBC $142/MS $113, avg PT $133.86. Earnings Aug 4. Risk: Keytruda patent cliff. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $207.83 | -$54.60 (-1.84%) | **10% trailing**, GTC, live (order 92b2b072, stop $190.87191 / hwm $212.0799) | Primary tech deployable, ~2.89%. Opened 7/15 market-open as the deployment-floor deploy (gate cleared via equities-rallying-through-oil branch: benign CPI+PPI + bullish ASML AI read). Day-1 mild red (-1.84%), well above the ~$196.91 -7% cut; oil/Iran still the macro overhang. B200 lease firm ~$6; TSMC AI-demand confirm Thu 7/16. Fresh 10% trail. HOLD — manage per stop rules. |

_Notes: Wed 7/15 **midday risk check** — **NO-OP, HOLD all 3.** No position at/below -7% (worst NVDA -1.84%) → no cuts. META has crossed +15% (+16.74%, now in the 15-30% ratchet band, target trail 7%) but both legs are already at 7% (tightened 7/10) and the rule never loosens → no change. MRK/NVDA red → ratchet N/A. All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). Book ~89.6% cash (~$90.1k dry powder). **Weekly slots: 2 of 3 used (MRK + NVDA).** No Telegram (nothing closed). Next routine: market-close wrap 7/15._
