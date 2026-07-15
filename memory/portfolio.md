# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-15 ~09:47 ET (market-open routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 16:00 ET).
- **Mode:** paper
- **Cash:** $90,090.91
- **Equity:** $100,505.93
- **Buying power:** $389,525.68
- **Day P/L:** +$45.58 (+0.045%) — equity $100,505.93 vs last_equity $100,460.35. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$505.93 (+0.51%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $657.88 | +$556.02 (+13.73%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $630.3912 / hwm $677.84; tightened to 7% on 7/10 at the +17% high — never loosen) | Core AI name (~4.58% of equity = target weight). +13.73% sits in the 0-15% band; stop already 7% and ratchet never loosens → stays 7%. +23% off late-June lows, longest run >200-DMA since Feb. JPM cites AI-strategy sentiment + external AI monetization. Buy consensus, avg PT $836.76. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $123.785 | -$48.65 (-1.68%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.83%). -1.68%, well above the -7% cut (~$117.09). FDA bladder-cancer approval 7/14; WF $150/RBC $142/MS $113, avg PT $133.86. Earnings Aug 4. Risk: Keytruda patent cliff. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $211.715 | -$0.21 (-0.007%) | **10% trailing**, GTC, live (order 92b2b072, stop $190.5615 / hwm $211.735) | **NEW today (market-open 7/15) — primary tech deployable, ~2.95%.** Bought as the deployment-floor deploy once the gate cleared via the "equities-rallying-through-it" branch (double-benign inflation CPI+PPI + bullish ASML AI read → tech-led up tape looking through the still-escalating oil/Iran shock). B200 lease firm ~$6; TSMC AI-demand confirm 7/16. Fresh 10% trail. HOLD — manage per stop rules. |

_Notes: Wed 7/15 **market-open** — **BOUGHT NVDA 14 sh @ $211.73 (~2.95%, fresh 10% trail)** as the deployment-floor deploy: the NVDA gate cleared via the "equities rallying through it" OR-branch (S&P +0.39%/Nasdaq +0.67% tech-led on a 2nd benign inflation print [PPI -0.3% headline / +0.2% core] + bullish ASML AI read), while the live spread re-sampled 3x was tight (~0.01-0.02%). Oil itself still escalating (Brent ~$85, 4th up session) but equities durably looking through it. META HOLD (no add, target weight, 7% trail never loosen); MRK HOLD (defensive, above -7% cut). All three trailing stops confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). Book ~89.6% cash (~$90.1k dry powder). **Weekly slots: 2 of 3 used (MRK + NVDA).** **Alpaca API had a ~15-min partial 504 outage this run** (account/positions/order-POST down; clock/quote/orders-GET up) — recovered mid-run; buy filled cleanly after re-checking for no double-order. Next routine: midday risk check 7/15._
