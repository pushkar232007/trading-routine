# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-16 ~16:02 ET (market-close wrap routine) — LIVE read from `account` + `positions` + `orders`. Market CLOSED (`is_open: false`, next open 2026-07-17 09:30 ET). NO trades this routine.
- **Mode:** paper
- **Cash:** $90,090.90
- **Equity:** $100,577.51
- **Buying power:** $389,726.11
- **Day P/L:** -$100.59 (-0.10%) — equity $100,577.51 vs last_equity $100,678.10. Far inside the -3% daily cap.
- **vs. $100k paper start:** +$577.51 (+0.58%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $664.00 | +$598.86 (+14.79%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $638.04975 / hwm $686.075; at 7% since 7/10 — never loosen) | Core AI name (~4.62% of equity = target weight). Day **-2.54%** (give-back off yesterday's highs). +14.79% now back in the 0-15% band; both legs already at 7% → no change (never loosen). Earnings Jul 29. HOLD — add complete, no add. |
| MRK | 23 | $125.90 | $127.67 | +$40.71 (+1.41%) | 10% trailing, GTC, live (order stop $116.037 / hwm $128.93, ratcheted up on today's high) | Defensive/oil-insensitive pharma starter (~2.92%). Day **+3.29%** — the day's winner. Ph3 KEYNOTE-C93 win + JPM PT→$140 tailwind. +1.41% from entry, well above the ~$117.09 -7% cut. Earnings Aug 4. Risk: 2028 Keytruda LOE. HOLD per stop rules. |
| NVDA | 14 | $211.73 | $207.30 | -$62.02 (-2.09%) | **10% trailing**, GTC, live (order stop $191.31237 / hwm $212.5693) | Primary tech deployable, opened 7/15 (~2.89%). Day-2 starter, day **-2.45%** on a soft-tech session, -2.09% from entry, ≫ the -7% cut & above the $191.31 trail. TSMC Q2 record beat + AI demand "extremely robust" confirmed thesis. HOLD — manage per stop rules; do NOT add a fresh position. |

_Notes: Thu 7/16 **market-close wrap** — NO trades (open/midday both NO-OP). Mild risk-off tech session: META -2.54% & NVDA -2.45% gave back, MRK +3.29% (defensive did its job) cushioned the book to just -$100.59 (-0.10%) on the day. No position at/below the -7% cut (worst NVDA -2.09%); META slipped from +15.66% midday back to +14.79% (below the 15% ratchet band) but both legs already at 7% → no change (never loosen). All 4 trailing legs confirmed live via `orders` (META 2 legs @7%, MRK @10% ratcheted up, NVDA @10%). Book ~89.6% cash (~$90.1k dry powder). Weekly slots: 2 of 3 used (MRK + NVDA). EOD Telegram summary sent (close routine always notifies). Next routine: pre-market Fri 7/17 (weekly review at Fri close)._
