# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-17 ~07:10 ET (pre-market routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, next open 2026-07-17 09:30 ET). NO trades this routine (research/drafting only).
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,461.84
- **Buying power:** $389,402.23
- **Day P/L:** -$119.93 (-0.12%) — equity $100,461.84 vs last_equity $100,581.77. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$461.84 (+0.46%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $654.09 | +$529.49 (+13.08%) | **7% trailing**, GTC, live (two legs, both stop $638.04975 / hwm $686.075; at 7% since 7/10 — never loosen) | Core AI name (~4.56% of equity = target weight). Day **-1.57%** (rode the tech risk-off). +13.08% now in the 0-15% band; both legs already at 7% → no change (never loosen). Wedbush Street-low PT $671 (Neutral) but consensus ~$820 Buy. Earnings Jul 29. HOLD — add complete, no add. |
| MRK | 23 | $125.90 | $128.81 | +$66.93 (+2.31%) | 10% trailing, GTC, live (order stop $116.037 / hwm $128.93) | Defensive/oil-insensitive pharma starter (~2.95%). Day **+0.93%**, **+3.24% on 7/16 = the day's winner again** (oncology pipeline + immunology optimism). +2.31% from entry, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $202.12 | -$134.54 (-4.54%) | **10% trailing**, GTC, live (order stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.82%). Day-3 starter, **-4.54% from entry** after 2 down sessions on TSMC **sell-the-news** + broad semi risk-off (NOT a thesis break; TSMC's beat confirmed AI demand, new Vera Rubin AI-factory deal, Strong Buy $301.62). Still ≫ the -7% cut (~$196.91) & above the $191.31 trail. HOLD — do NOT add; **midday re-checks the -7% cut**. |

_Notes: Fri 7/17 **pre-market** — NO trades (research/drafting only). **Tape turned risk-off-tech into the weekly review:** TSMC's record beat SOLD THE NEWS (-4%), Nasdaq -1.6% Thu → META -1.57% & NVDA -2.55% on the day, MRK +0.93% (defensive cushion). **Oil ticked back UP** (Brent >$84 +1.7%) so the 7/16 "1st down session" was a one-day head-fake → oil overhang re-established. Book down just -$119.93 (-0.12%) on the day; no position at/below the -7% cut (worst NVDA -4.54%, ~2.6% of cushion above its ~$196.91 cut — midday will re-check). All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10%, NVDA @10%). Book ~89.7% cash (~$90.1k dry powder). Weekly slots: 2 of 3 used (MRK + NVDA). Deployment-floor: staying in cash into the weekly review is a DELIBERATE logged decision (risk-off-tech tape + oil overhang back; FDX oil-wrong + spread-gated). No Telegram (no urgent catalyst; pre-market research run). Next routine: market-open, then midday/close + **weekly-review at today's close**._
