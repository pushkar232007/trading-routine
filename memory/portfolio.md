# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-16 ~07:10 ET (pre-market routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, next open 2026-07-16 09:30 ET). NO trades this routine (research/drafting only).
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,666.65
- **Buying power:** $389,975.71
- **Day P/L:** -$11.45 (-0.01%) — equity $100,666.65 vs last_equity $100,678.10 (flat; pre-open read). Far inside the -3% daily cap.
- **vs. $100k paper start:** +$666.65 (+0.67%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $683.86 | +$737.90 (+18.22%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; at 7% since 7/10, auto-ratcheting up on new highs — never loosen) | Core AI name (~4.76% of equity = target weight). Up 17% in July = 3rd-best S&P performer; Bloomberg "investors endorse AI plans" (Meta Compute cloud + Muse Spark 1.1 paid tier + Iris chip Sept). +18.22% is in the 15-30% ratchet band → target trail 7%; already at 7% → no change (never loosen). Earnings Jul 29. HOLD — add complete, no add (target weight). |
| MRK | 23 | $125.90 | $124.54 | -$31.30 (-1.08%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.85%). **+3.05% on 7/15 — Ph3 KEYNOTE-C93 met primary endpoint (Keytruda PFS in MMR-deficient endometrial cancer); JPM PT→$140.** -1.08%, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $208.85 | -$40.32 (-1.36%) | **10% trailing**, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.90%). Day-2 starter, -1.36% from entry (pre-mkt -1.7% = noise, ≫ the -7% cut, above the $191.31 trail). **TSMC Q2 record beat + AI demand "extremely robust" = bullish thesis confirm; Jensen confirmed Vera Rubin in production.** B200 lease firm ~$6; P/E lowest in 7 years. HOLD — manage per stop rules; do NOT add a 1-day-old position. |

_Notes: Thu 7/16 **pre-market** — research/drafting only, NO trades. All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). **Overnight = all constructive:** TSMC Q2 record beat (AI-demand confirm → NVDA), oil finally reversed (Brent below $85, 1st down session), MRK Ph3 KEYNOTE-C93 win + JPM $140 — nothing urgent, no Telegram. Book ~89.5% cash (~$90.1k dry powder). **Weekly slots: 2 of 3 used (MRK + NVDA);** last slot's named deployable = FDX (oil reversal eased its fuel-cost headwind) IF /trade re-samples a tight live spread. Next routine: market-open Thu 7/16 (retail sales/claims 8:30 ET, second-tier; NFLX after close)._
