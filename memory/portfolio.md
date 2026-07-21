# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-07-21 ~09:34 ET (Tue **market-open** routine) — LIVE read from `account` + `positions`. Market OPEN (`is_open: true`, next close 16:00 ET). **TRADE PLACED: bought FDX 9 sh @ $313.00 (deployment-floor deploy, 10% trail attached).** No position at/below -7% (worst NVDA -2.52%, above the ~$196.91 cut); no winner ≥+15% to tighten. **Regime: BOTH overhangs EASING → risk-on tape** (oil reversing on Iran ceasefire talks + Kimi K3 re-framed memory-bullish); see strategy.md/research-log.md.
- **Mode:** paper
- **Cash:** $91,737.55
- **Equity:** $100,313.99
- **Buying power:** ~$385,860 (regt ~$185k)
- **Day P/L:** +$52.32 (+0.05%) — equity $100,313.99 vs last_equity $100,261.67.
- **vs. $100k paper start:** +$313.99 (+0.31%); account funded 2026-06-22
- **Invested:** ~8.55% (long mkt value $8,576.44); **~91.5% cash.** New week 7/21 → **1 of 3 new-position slots used (FDX).**

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| FDX | 9 | $313.00 | $312.60 | -$3.60 (-0.13%) | 10% trailing, GTC, live (order 6f599c57, stop $281.34 / hwm $312.60) | Non-tech logistics diversifier (~2.81% of equity), opened 7/21 open. Bought on the risk-on tape as oil eases (Iran ceasefire talks) → fuel headwind easing; Citizens JMP "market outperform" PT $375, Buy consensus ~$350. Spread sampled 3x stable ~2.26% before buy (cleanest FDX feed in weeks). Flat from entry. 0-15% band → stop stays 10%. Risk: oil flip-flops with Iran headlines. |
| MRK | 23 | $125.90 | $124.92 | -$22.54 (-0.78%) | 10% trailing, GTC, live (order 3d2f860f, stop $118.566 / hwm $131.74) | Defensive/oil-insensitive pharma (~2.86% of equity). ~Flat from entry. No new negative catalyst; Lipfendra (oral PCSK9) approval + raised FY guidance intact; PTs $140-150. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. Earnings Aug 4. HOLD. |
| NVDA | 14 | $211.73 | $206.39 | -$74.76 (-2.52%) | 10% trailing, GTC, live (order 92b2b072, stop $191.31237 / hwm $212.5693) | AI-hardware starter, opened 7/15 (~2.88%). **+1.53% intraday** — bear thesis SOFTENING (Kimi K3 now read memory-bullish, NVDA a possible net winner via more HBM/systems demand; tape risk-on). Above the -7% cut (~$196.91) & the $191.31 trail. HOLD, no add (don't average down; one green session ≠ confirmed bottom). |

_Notes: Tue 7/21 **market-open** routine — executed the pre-market plan's deployables against live gates on a risk-on tape. **BOUGHT FDX 9 sh @ $313.00 (~2.81%), 10% trail attached (order 6f599c57).** GEHC (primary) SKIPPED — feed broken again (bid frozen $58.65, ask flickering to $65.03, 5.8–9.8% spread). MRK-add (secondary) SKIPPED — no pullback/fresh catalyst. FDX (tertiary) BOUGHT — spread stable ~2.26% (cleanest in weeks, inside the <~3% gate) + thesis right this tape (oil easing). Buy script timed out at 15s pre-fill; order then completed fully (9/9 @ $313), trail POSTed manually per the 7/9 tight-spread lesson — position confirmed protected. All 3 positions have live 10% trailing stops. No position near the -7% cut; no winner ≥+15% to tighten. Day P/L +0.05% (far inside the -3% cap). Weekly slots: 1 of 3 used. Telegram SENT (trade placed). Next routine: midday risk check 7/21 — re-check NVDA's -7% cut (~$196.91) & FDX vs entry._
