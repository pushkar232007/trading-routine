# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-20 ~09:31 ET (Mon **market-open** routine) — LIVE read from `account` + `positions` + `orders`. Market OPEN (`is_open: true`, next close 16:00 ET). **No trades** (executed the plan: HOLD NVDA + MRK; GEHC deployable SKIPPED on a frozen ~6.9% spread). Both trailing-stop legs confirmed live. **Regime: confirmed semiconductor BEAR MARKET (Kimi K3) + oil spiking — risk-off; see strategy.md/research-log.md.**
- **Mode:** paper
- **Cash:** $94,554.55
- **Equity:** $100,355.23
- **Buying power:** $394,460.10
- **Day P/L:** +$28.84 (+0.029%) — equity $100,355.23 vs last_equity $100,326.39.
- **vs. $100k paper start:** +$355.23 (+0.36%); account funded 2026-06-22
- **Invested:** ~5.8% (long mkt value $5,800.68); **~94.2% cash.** New week 7/20 → 0 of 3 new-position slots used.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| MRK | 23 | $125.90 | $127.01 | +$25.53 (+0.88%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.91% of equity). Intraday -0.38%. +0.88% from entry → 0-15% band, stop stays 10%. Well above the ~$117.09 -7% cut. New Lipfendra (oral PCSK9) FDA approval 7/16; PTs $140-150. Doing its job in a semi-rout + oil-spike tape. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $205.675 | -$84.77 (-2.86%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.87%). Intraday +1.41% (recovering, stabilizing above $200). **The -2.86% slide is a structural semi bear-market re-rating (Kimi K3 open-weight model, SOX -20% from peak) — higher bar to hold, do NOT average down.** Above the -7% cut (~$196.91) & the $191.31 trail. HOLD, no add. **Midday MUST re-check the -7% cut.** |

_Notes: Mon 7/20 **market-open**, market OPEN. No trades — executed the plan: HOLD both holdings; the one named deployable **GEHC** (primary rotation-into-defensives name) was **SKIPPED on a frozen/broken paper feed** (live spread re-sampled 3x = bid $62.51 / ask $66.96 ≈ 6.9%, identical timestamps — classic FDX-style junk feed; an ask fill would sit ~7% below bid). MRK-add secondary trigger (a pullback) not met (MRK +0.88%). **Regime: the semiconductor complex is in a confirmed BEAR MARKET** (Kimi K3 drove SOX/SOXX >20% off its June-2 peak) + oil spiking (Brent ~$88, +14%/wk, Iran) → risk-off; falling-knife binds for tech, so ~94.2% cash is the DELIBERATE logged decision. NVDA recovering intraday (+1.41% ~$205.68), no fresh thesis-breaker → no Telegram. Deployment-floor satisfied: named deployable (GEHC, spread-gated) + logged risk-off reason. Weekly slots: 0 of 3 used (new week). Next routine: midday risk check — **MUST re-check NVDA's -7% cut (~$196.91)**._
