# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-15 ~07:10 ET (pre-market routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, next open 09:30 ET).
- **Mode:** paper
- **Cash:** $93,055.13
- **Equity:** $100,515.63
- **Buying power:** $393,109.92
- **Day P/L:** +$55.28 (+0.055%) — equity $100,515.63 vs last_equity $100,460.35 (pre-open read). Well inside the -3% daily cap.
- **vs. $100k paper start:** +$515.63 (+0.52%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $662.30 | +$586.96 (+14.50%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $630.3912 / hwm $677.84; tightened to 7% on 7/10 at the +17% high — never loosen) | Core AI name (~4.61% of equity = target weight). +14.50% sits in the 0-15% band; stop already 7% and ratchet never loosens → stays 7%. +23% off late-June lows, 3 days >200-DMA (longest since Feb). JPM cites AI-strategy sentiment + external AI monetization. Minor negs: AI-layoff lawsuit, $50B Louisiana DC (5 GW, more capex). Buy consensus, avg PT $836.76. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $122.80 | -$71.30 (-2.46%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.81%). -2.46%, well above the -7% cut (~$117.09). NEW 7/14: FDA bladder-cancer approval; WF $150 (OW)/RBC $142 (OP)/MS $113 (EW), avg PT $133.86. Earnings Aug 4. Risk: Keytruda patent cliff. HOLD per stop rules. |

_Notes: Wed 7/15 **pre-market** — research/drafting only, **NO trades** (correct for a pre-market routine). Both positions stop-protected & within guardrails; all three trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%), unchanged. Book ~92.6% cash (~$93.1k dry powder). **Regime: CPI gate now STRONGLY met** (June core FLAT m/m, +2.6% y/y; Fed July-hike odds 40%→15%) = a tailwind for tech — **but oil/Iran STILL escalating (Brent >$85, day-3)** → NVDA (primary tech deployable, lease firm ~$6) stays gated on oil alone; do NOT initiate until oil stabilizes + tight live spread. Today: PPI 8:30 ET + bank earnings (MS/BLK/PNC/BNY) + JNJ; TSMC Thu 7/16 = AI-demand read. **Weekly slots: 1 of 3 used (MRK).** Next routine: market-open 7/15._
