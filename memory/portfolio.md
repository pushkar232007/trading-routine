# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-16 ~09:32 ET (market-open routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 16:00 ET). NO trades this routine (FDX skipped — broken feed).
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,655.44
- **Buying power:** $389,944.30
- **Day P/L:** -$22.66 (-0.02%) — equity $100,655.44 vs last_equity $100,678.10. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$655.44 (+0.66%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $679.15 | +$704.91 (+17.41%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; at 7% since 7/10, auto-ratcheting up on new highs — never loosen) | Core AI name (~4.72% of equity = target weight). Up 17% in July; Bloomberg "investors endorse AI plans" (Meta Compute cloud + Muse Spark 1.1 paid tier + Iris chip Sept). +17.41% is in the 15-30% ratchet band → target trail 7%; already at 7% → no change (never loosen). Earnings Jul 29. HOLD — add complete, no add. |
| MRK | 23 | $125.90 | $124.825 | -$24.73 (-0.85%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.85%). +0.98% today. **Ph3 KEYNOTE-C93 win (Keytruda PFS in MMR-deficient endometrial cancer); JPM PT→$140.** -0.85%, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $209.87 | -$26.04 (-0.88%) | **10% trailing**, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.92%). Day-3 starter, -0.88% from entry, ≫ the -7% cut & above the $191.31 trail. **TSMC Q2 record beat + AI demand "extremely robust" = bullish thesis confirm; Jensen confirmed Vera Rubin in production.** HOLD — manage per stop rules; do NOT add a fresh position. |

_Notes: Thu 7/16 **market-open** — NO trades. **FDX (last-slot deployable) SKIPPED:** live spread re-sampled 3x = ~11.4% (bid $295.45 / ask $329.18, 40 sh, frozen timestamps) = the chronic broken paper feed → un-buyable cleanly; retry when it normalizes. All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). Book ~89.5% cash (~$90.1k dry powder). Weekly slots: NVDA opened this week (7/15). Next routine: midday risk check 7/16 (cut losers past -7%, tighten stops on winners)._
