# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-14 ~16:02 ET (market-close routine) — LIVE EOD read from `account` + `positions`. Market CLOSED (`is_open: false`).
- **Mode:** paper
- **Cash:** $93,055.13
- **Equity:** $100,460.53
- **Buying power:** $392,955.64
- **Day P/L:** -$44.40 (-0.044%) — equity $100,460.53 vs last_equity $100,504.93. Well inside the -3% daily cap.
- **vs. $100k paper start:** +$460.53 (+0.46%); account funded 2026-06-22

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $661.00 | +$577.86 (+14.27%) | **7% trailing**, GTC, live (two legs 4-sh + 3-sh, both stop $630.3912 / hwm $677.84; tightened to 7% on 7/10 at the +17% high — never loosen) | Core AI name (~4.61% of equity = target weight). +14.27% sits in the 0-15% band; stop already 7% and ratchet never loosens → stays 7%. Day +0.65% (green into the close). Thesis strengthened: BofA cost-savings note, Muse Spark 1.1 API monetization, Iris chip mfg Sept. Buy consensus, avg PT $836.76. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $120.80 | -$117.30 (-4.05%) | 10% trailing, GTC, live (order 3d2f860f, stop $115.263 / hwm $128.07) | Defensive/oil-insensitive pharma starter (~2.77%). -4.05%, day's laggard (-2.60% intraday) but well above the -7% cut (~$117.09). Guggenheim PT $145 (Buy), BMO $142 (OP) on Keytruda Qlex uptake. Earnings Aug 4. Risk: 2028 Keytruda patent cliff. HOLD per stop rules. |

_Notes: Tue 7/14 **market-close wrap** — **NO trades, no closes, no stop changes.** Loss-cut scan: neither position at/past -7% (MRK worst at -4.05%, cut ~$117.09) → no forced closes. Winner scan: META +14.27% still in the 0-15% band, stop already 7% (never loosen) → no tightening. All three trailing legs confirmed live via `orders`. Both positions stop-protected & within guardrails; day P/L -0.044% far inside the -3% cap. Book ~92.6% cash (~$93.1k dry powder). NVDA stays primary tech deployable once the oil/Iran shock stabilizes (CPI cleared benign + lease firm; oil is the only remaining gate). **Weekly slots: 1 of 3 used (MRK).** Next routine: pre-market Wed 7/15._
