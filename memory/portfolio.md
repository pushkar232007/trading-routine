# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-17 ~09:31 ET (market-open routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 2026-07-17 16:00 ET). NO trades this routine (HOLD all; deployment-floor = deliberate cash into the weekly review).
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,414.57
- **Buying power:** $389,269.87
- **Day P/L:** -$167.20 (-0.17%) — equity $100,414.57 vs last_equity $100,581.77. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$414.57 (+0.41%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $646.11 | +$473.66 (+11.70%) | **7% trailing**, GTC, live (two legs, both stop $638.04975 / hwm $686.075; at 7% since 7/10 — never loosen) | Core AI name (~4.50% of equity = target weight). Day **-2.77%** (rode the tech risk-off into the weekly review). +11.70% in the 0-15% band; both legs already at 7% → no change (never loosen). Wedbush Street-low PT $671 (Neutral) but consensus ~$820 Buy. Earnings Jul 29. HOLD — add complete, no add. |
| MRK | 23 | $125.90 | $129.18 | +$75.44 (+2.61%) | 10% trailing, GTC, live (order stop $116.262 / hwm $129.18, ratcheted up on today's high) | Defensive/oil-insensitive pharma starter (~2.96%). Day **+1.21%** — the day's winner again, doing its diversifier job on a risk-off-tech day. +2.61% from entry, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $202.35 | -$131.33 (-4.43%) | **10% trailing**, GTC, live (order stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.82%). Day-4 starter, **-4.43% from entry** on TSMC **sell-the-news** + broad semi risk-off (NOT a thesis break; TSMC's beat confirmed AI demand, Vera Rubin AI-factory deal, Strong Buy $301.62). Still ≫ the -7% cut (~$196.91) & above the $191.31 trail. HOLD — do NOT add; **midday re-checks the -7% cut**. |

_Notes: Fri 7/17 **market-open** — NO trades (HOLD all 3). Live tape confirmed the risk-off-tech read from pre-market: META -2.77% & NVDA -2.44% on the day, MRK +1.21% (defensive cushion). Book down just -$167.20 (-0.17%) on the day; no position at/below the -7% cut (worst NVDA -4.43%, ~2.3% of cushion above its ~$196.91 cut — midday will re-check). All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10% hwm-ratcheted to $129.18, NVDA @10%). Book ~89.7% cash (~$90.1k dry powder). Weekly slots: 2 of 3 used (MRK + NVDA). Deployment-floor: staying in cash into the weekly review is a DELIBERATE logged decision (risk-off-tech tape + oil overhang re-established; FDX oil-wrong + spread-gated; NVDA already held). No Telegram (no trade placed). Next routine: midday risk check, then market-close + **weekly-review at today's close**._
