# Portfolio Snapshot

_Bull: overwrite this entire file with a fresh snapshot every routine run. This should always
reflect the CURRENT state, not history (history lives in trade-log.md)._

- **Last updated:** 2026-08-03 ~16:05 ET (Mon **market-close wrap** — market CLOSED; **NO TRADE / no cut / no tighten** all day) — snapshot from live `positions` + `account`. Regime: **constructive/expansion, cut-anticipating tape** (Fed held 7/29, cooling June PCE 7/31). Week's binaries: **MRK Q2 tomorrow Tue 8/4 before open** (ugly headline = a KNOWN one-time Terns IPR&D charge, not operational) + **July NFP Fri 8/7**.
- **Mode:** paper
- **Cash:** $91,480.89
- **Equity / portfolio value:** $100,131.42 (last_equity $100,098.93)
- **Buying power:** ~$390,145 (margin multiplier; non-marginable ~$95,806)
- **Invested:** ~8.6% (long mkt value $8,650.53); **~91.4% cash.** Week 8/3 → **0 of 3 new-position slots used.**
- **Day P/L:** ~+$32.49 (+0.03%) (equity $100,131.42 vs last_equity $100,098.93) — quiet green day. Far inside the -3% daily cap.
- **vs. $100k paper start:** ~+$131.42 (+0.13%); account funded 2026-06-22.

## Open positions

| Symbol | Qty | Avg entry | Current price | Unrealized P/L | Stop level | Thesis |
|---|---|---|---|---|---|---|
| GEHC | 42 | $71.42 | ~$69.73 | -$70.98 (-2.37%) | 10% trailing, GTC, live (order 85f200d4, stop $63.918 / hwm $71.02) | **Opened 7/30 ~09:32 ET (~2.93% of equity).** Medtech, non-tech + semi-uncorrelated diversifier. Q2 (7/29) BEAT — EPS $1.13 vs $1.04, rev $5.30B (+5.8%), record backlog $23.9B, FY26 guide reaffirmed. Post-print analyst wave RAISED PTs: BTIG $79, UBS $73, JPM $70, Evercore $84; central ~$81.72 (~17% up) = thesis strengthening while it digests the +11% pop. **Recovered +2.51% today** (best of the book). **-7% cut line ~$66.42 → $69.73 ABOVE it → not a cut.** 0-15% band → stop stays 10%. HOLD — do NOT average down. |
| FDX | 9 | $313.00 | ~$309.24 | -$33.84 (-1.20%) | 10% trailing, GTC, live (order 6f599c57, stop $289.8945 / hwm $322.105) | Non-tech logistics diversifier (~2.78% of equity), opened 7/21. Firmed +0.60% today, no fresh catalyst, oil quiet, well inside the trail. -7% cut line ~$291.09 → ABOVE it → not a cut. Buy consensus, avg PT ~$352; FY26 guide up ~11% rev; Freight spin (FDXF) trading. 0-15% band → stop stays 10%. HOLD. |
| MRK | 23 | $125.90 | ~$127.77 | +$43.01 (+1.49%) | 10% trailing, GTC, live (order 3d2f860f, stop ~$121.55 / hwm $135.05) | Defensive/oil-insensitive pharma (~2.93% of equity). **Q2 earnings TOMORROW Tue 8/4 before open = the binary** — headline ~$1.36 diluted EPS (-36% y/y) is a KNOWN one-time ~$5.8B / ~$2.35-per-share Terns-acquisition IPR&D charge, NOT operational (rev +3.3% $16.33B, beat 4 straight); Qlex subcutaneous Keytruda secured exclusivity to 2039 = LOE-cliff de-risking. Gave back -1.87% today into the print but still green from entry. **Do NOT add ahead of the print.** Avg PT ~$133.89. 0-15% band → stop stays 10%. Well above the ~$117.09 -7% cut. HOLD. |

_Notes: Mon 8/3 **market-close wrap** — market CLOSED, **NO TRADE placed / no cut / no tighten** (open + midday + close all NO-OP). Book = 3 holdings (GEHC + FDX + MRK), all stop-protected (trailing legs live & confirmed via `orders --status open`, qty_available 0). **-7% cut: N/A — no position at/below -7% (GEHC -2.37%, FDX -1.20%, MRK +1.49%).** **Ratchet: N/A — no winner ≥+15% → all stops stay 10%.** Book ~91.4% cash (~$91.5k dry powder). Non-tech ≥2 rule amply satisfied (all 3 holdings non-tech + CI candidate). **Weekly slots: 0 of 3 used.** **Deployment-floor / CI: CI was the named primary deployable this week (earnings-binary gate cleared 7/30, deep value fwd P/E ~9.5 vs industry ~17.7, ~22% upside), and its paper feed HAD normalized at the 8/3 midday (~0.22% spread). But opening a new position is out of scope for open/midday/close risk routines — it's the /trade routine's job — so CI was NOT deployed today; it stays the clean primary deployable for the next /trade run IF the live spread re-samples tight. Secondary = MRK-add, still gated by the 8/4 print.** EOD Telegram summary sent (close routine always notifies). Next routine: pre-market Tue 8/4 — digest the MRK Q2 print (before open) and re-check the ratchet & -7% cut._
