# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-13 ~16:xx ET (market-close routine) — ⚠️ **STALE: Alpaca API returned 401
  unauthorized, could NOT pull a live EOD snapshot.** Figures below are carried from the 13:xx ET midday
  pull, NOT a fresh close read. Refresh once the API key is fixed.
- **Mode:** paper
- **Cash:** $93,055.13 _(last-known midday; not refreshed)_
- **Equity:** $100,511.48 _(last-known midday; not refreshed)_
- **Buying power:** $393,098.29 _(last-known midday; not refreshed)_
- **Day P/L:** -$69.54 (-0.07%) as of midday — well inside the -3% daily cap _(close value unknown, API down)_
- **vs. $100k paper start:** +$511.48 (+0.51%); account funded 2026-06-22

## ⚠️ API status

- **Alpaca 401 unauthorized (2026-07-13 close).** Both `account` and `positions` fail; confirmed with raw
  curl using the env key/secret → the credential itself is rotated/revoked/invalid, not a script or base-URL
  bug (base URL correct: `https://paper-api.alpaca.markets`; all env vars present). Telegram flag sent
  (msg 168). **FIX:** refresh `ALPACA_API_KEY_ID` / `ALPACA_API_SECRET_KEY` in the cloud env settings.
  Until fixed, trading is blind — no live trades possible.

## Open positions _(last-known midday 7/13 — not refreshed at close)_

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| META | 7 | $578.4486 | $659.29 | +$565.89 (+13.98%) | **7% trailing**, GTC, live (2 legs 4-sh & 3-sh, stop $630.3912 / hwm $677.84 — tightened to 7% on 7/10 at the +17% high) | Core AI name (~4.59% of equity). +13.98% in the 0-15% band but stop already at 7% and the rule is NEVER LOOSEN → stays 7%. Meta Compute AI-cloud + "Iris" chip thesis intact. Earnings Jul 29. HOLD — add complete. |
| MRK | 23 | $125.90 | $123.56 | -$53.82 (-1.86%) | 10% trailing, GTC, live (stop $115.263 / hwm $128.07; order 3d2f860f) | Defensive/oil-insensitive pharma starter (~2.83%). Only -1.86%, far from the -7% cut (~$117.09). Keytruda+Padcev bladder FDA approval; WF PT $150. Earnings Aug 4. Risk: 2028 Keytruda patent cliff. HOLD per stop rules. |

_Notes: Mon 7/13 **market-close** — Alpaca API DOWN (401), so this is a carried-forward snapshot, not a live
close read. NO trades today (midday risk check found nothing to cut/ratchet). Both positions were stop-protected
& within guardrails at midday. Regime: day-2 Iran/oil watch; **THE binary = June CPI Tue 7/14 8:30 ET** + big-bank
earnings pre-open; TSMC Thu. Deployment gated pre-CPI AND now hard-blocked by the API outage. **Weekly slots: 1 of 3
used (MRK).** Named deployable once tape/CPI clear AND API restored: NVDA (lease gate firming). Next routine:
pre-market Tue 7/14 — but first the human must refresh the Alpaca key._
