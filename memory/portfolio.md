# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-29 ~09:32 ET (Wed **market-open** — NO trades placed; market OPEN, `is_open: true`) — snapshot from live `account` + `positions`. Regime: **DECISION DAY — GEHC Q2 beat big (deploy gate MET) BUT its paper feed is broken/wide (5.4-6.9% spread, sampled 3x) → SKIPPED on the spread gate, not the thesis. FOMC decision 2pm ET (~64% CME hold = live hike tail); MSFT+META after close = AI-capex reads. Oil easing (Brent ~$87.5).**
- **Mode:** paper
- **Cash:** $94,480.54
- **Equity / portfolio value:** $100,316.95 (last_equity $100,326.16)
- **Buying power:** ~$394,264.11 (margin multiplier; non-marginable ~$97,398.74)
- **Invested:** ~5.8% (long mkt value $5,836.41); **~94.2% cash.** New week 7/27 → **1 of 3 new-position slots used (FDX).**
- **Day P/L:** ~-$9.21 (-0.01%) (equity $100,316.95 vs last_equity $100,326.16) — flat, far inside the -3% daily cap.
- **vs. $100k paper start:** ~+$317 (+0.32%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | ~$310.68 | -$20.88 (-0.74%) | 10% trailing, GTC, live (order 6f599c57, stop ~$289.89 / hwm ~$322.11) | Non-tech logistics diversifier (~2.79% of equity), opened 7/21. Oil easing (Brent ~$87.5) = fuel tailwind persists; slightly red intraday, well inside the trail. -7% cut line ~$291.09 → ABOVE it → not a cut. UBS/WF Buy; FY26 Q4 beat + Freight spin intact. 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | ~$131.92 | +$138.46 (+4.78%) | 10% trailing, GTC, live (order 3d2f860f, stop ~$121.55 / hwm ~$135.05) | Defensive/oil-insensitive pharma (~3.02% of equity). Book's best performer; hit a fresh 52-wk high $135.05 on 7/28. Alimatravir once-monthly oral HIV-PrEP (Ph3) + Lipfendra + Keytruda/Qlex oncology intact; PTs to $150 (avg ~$134.81 = thin upside). Running (+4.78%), not a pullback → MRK-add trigger NOT met. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |

_Notes: Wed 7/29 **market-open** — NO trades placed. Book = 2 holdings (FDX + MRK), both stop-protected (trailing legs live, qty_available 0). No position at/below the -7% cut (FDX -0.74%, MRK +4.78%); no winner ≥+15% → both stops stay 10% (ratchet check is the midday routine's job). Book ~94.2% cash (~$94.5k dry powder). **GEHC deploy gate is MET on the print (Q2 beat big — EPS $1.13 vs $1.04, record orders/backlog, guide reaffirmed) BUT was SKIPPED at the open because the live paper feed is broken/wide — sampled 3x, bid $69.51→$68.99→$68.51 vs a stuck $73.24 ask = 5.4-6.9% spread, far above the <~3% gate; a market-only buy would fill near the ask and instantly trip the trail.** This is a broken-feed block, not a thesis change — GEHC stays the named primary deployable the moment the spread tightens; retry midday/close, preferably post-2pm FOMC. Secondary = MRK-add on a pullback (trigger not met, MRK running). Weekly slots: 1 of 3 used (FDX). No Telegram (no trade, open routine only pings on an actual fill). Next routine: midday risk check 13:00 ET (re-sample GEHC spread; re-check FDX/MRK vs ratchet & -7% cut; weigh the 2pm FOMC decision)._
