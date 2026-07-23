# Trade Log

_Bull: append a new entry every time you place, close, or deliberately skip a trade. Newest
entries at the top. Keep each entry to a few lines — this file gets read often, so don't bloat it._

Format:

```
## YYYY-MM-DD HH:MM — ACTION SYMBOL
- Qty / price / stop:
- Reasoning:
- Guardrail check:
```

---

## 2026-07-23 16:05 ET — NO-OP (market-close wrap; HOLD FDX + MRK + NVDA, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed today (open + midday + close all NO-OP). All 3 trailing legs live
  (qty_available 0 = shares held by the open stops): FDX 9-sh 10% trail, stop ~$289.89 / hwm $322.105 (6f599c57);
  NVDA 14-sh 10% trail, stop ~$192.95 / hwm $214.39 (92b2b072); MRK 23-sh 10% trail, stop ~$118.57 / hwm $131.74
  (3d2f860f). Fully stop-protected.
- **Oil >$98 stayed elevated all day but the book held ~flat — MRK carried it.** MRK: 23 sh @ $125.90, current
  $130.46, **+$104.88 (+3.62%)**, day **+2.35%** = day's winner, oil-insensitive defensive doing its job on the
  oil-spike high. Far above the ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- FDX: 9 sh @ $313.00, current $315.62, **+$23.58 (+0.84%)**, day **-1.68%** — gave back some of yesterday's +1.85%
  as the oil >$98 fuel headwind bit, but still green from entry, well inside the 10% trail. Most oil-exposed holding;
  didn't pre-emptively cut (7/22 head-fake lesson). 0-15% band → stop stays 10%. HOLD.
- **NVDA: 14 sh @ $211.73, current $209.15, -$36.12 (-1.22%)**, day **-1.37%**. -7% cut line ~$196.91 → ABOVE it →
  HOLD, no cut. GOOGL capex raise = net-bullish read-through, but risk-off oil tape + sell-semis rotation → no add.
  Loser → ratchet N/A. MSFT/META 7/29 = next AI-capex confirm.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -1.22%)** ✅. Ratchet: N/A (no
  winner ≥+15%; MRK +3.62%, FDX +0.84%, NVDA red) ✅. Sizes FDX 2.83% ($2,840.58) / MRK 2.99% ($3,000.58) / NVDA
  2.91% ($2,928.10) of $100,506.80 equity ≤ 5% ✅. Day P/L ~-$20.57 (~-0.02%, flat: FDX -$48.60, MRK +$68.77,
  NVDA -$40.74) ≪ -3% cap ✅. Weekly slots: 1 of 3 used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $91.74k (~91.3% cash). Equity +$507
  (+0.51%) vs the $100k paper start. GEHC (primary deployable) not deployed — deliberate cash (oil saga high +
  GEHC 7/29 earnings ~4 sessions out). Next routine: pre-market Fri 7/24 → **weekly review at Fri close.**

## 2026-07-23 13:05 ET — NO-OP (midday risk check; HOLD FDX + MRK + NVDA, no cut/tighten; market OPEN)
- Qty / price / stop: none placed/closed. All 3 trailing legs live & confirmed via `orders --status open`
  (qty_available 0 = shares held by the open stops): FDX 9-sh 10% trail, stop $289.8945 / hwm $322.105 (6f599c57);
  NVDA 14-sh 10% trail, stop $192.951 / hwm $214.39 (92b2b072); MRK 23-sh 10% trail, stop $118.566 / hwm $131.74
  (3d2f860f). Fully stop-protected.
- **NVDA (the flagged one): 14 sh @ $211.73, current $209.46, -$31.78 (-1.07%)**, day -1.23%. **-7% cut line
  ~$196.91 → $209.46 is ABOVE it → HOLD, no cut required.** GOOGL capex raise ($195-205B) = net-bullish
  read-through, but risk-off oil-spike tape + sell-semis rotation → no add. Loser → ratchet N/A.
- FDX: 9 sh @ $313.00, current $315.50, **+$22.52 (+0.80%)**, day -1.72% (giving back some of yesterday's +1.85%
  as oil >$98 fuel headwind bites — but still green, well inside the 10% trail). Well above the -7% cut. **Ratchet:
  +0.80% in the 0-15% band → stop stays 10% (no tighten).** Most oil-exposed holding but not near a cut; don't
  pre-emptively cut (7/22 head-fake lesson). HOLD.
- MRK: 23 sh @ $125.90, current $130.07, **+$95.80 (+3.31%)**, day **+2.04%** — day's winner, oil-insensitive
  defensive doing its job on the oil-spike high. Far above the ~$117.09 -7% cut. **Ratchet: +3.31% in the 0-15%
  band → stop stays 10%.** HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -1.07%)** ✅. Ratchet: N/A (no
  winner ≥+15%; MRK +3.31%, FDX +0.80%, NVDA red) ✅. Sizes FDX 2.83% ($2,839.52) / MRK 2.98% ($2,991.50) / NVDA
  2.92% ($2,932.44) of $100,500.58 equity ≤ 5% ✅. Day P/L ~flat (equity $100,500.58 vs ~$100,529 prior close)
  ≪ -3% cap ✅. Weekly slots: 1 of 3 used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed; a clean risk check isn't notify-worthy). Dry powder $91.74k (~91.3% cash).
  Next routine: market-close wrap 7/23.

## 2026-07-23 09:31 ET — NO-OP (market-OPEN; HOLD FDX + MRK + NVDA, no new buy; deployment-floor deliberate cash)
- Qty / price / stop: none placed/closed. Executed the 7/23 pre-market plan = HOLD all three, no adds. All 3
  trailing legs live & confirmed via `orders --status open`: FDX 10% trail, stop $289.8945 / hwm $322.105 (6f599c57);
  NVDA 10% trail, stop $192.951 / hwm $214.39 (92b2b072); MRK 10% trail, stop $118.566 / hwm $131.74 (3d2f860f).
- Standing-plan catch-up: NONE pending — 7/22 close ran & is logged; no misfired plan to salvage. Market `is_open: true`.
- **NVDA: 14 sh @ $211.73, current $209.29, -$34.17 (-1.15%)**, day -1.31%. HOLD, do NOT add — GOOGL capex raise to
  $195-205B is a net-bullish read-through, but a risk-off oil-spike tape (Brent >$98) + a live "sell-semis/buy-hyperscalers"
  rotation + NVDA still worst chip performer 2026 argue against adding. Well above the -7% cut (~$196.91). MSFT/META 7/29 = next confirm.
- FDX: 9 sh @ $313.00, current ~$320, **+$63.00 (+2.24%)**, day -0.32%. Oil >$98 = worst fuel headwind since entry
  (flip-flop risk at its peak), but shrugged off $94 → inside the 10% trail. HOLD, WATCH at midday; don't pre-emptively
  cut on the overnight oil read (7/22 head-fake lesson).
- MRK: 23 sh @ $125.90, current $127.99, **+$48.07 (+1.66%)**, day +0.41%. Oil-insensitive defensive doing its job on a
  new oil-spike high. Far above the ~$117.09 -7% cut. HOLD.
- **GEHC (primary deployable) — SKIPPED (deliberate).** Q2 earnings 7/29 before open (~4 sessions out) = a binary +
  oil at a saga high = risk-off tape → don't deploy right into the print. Falling-knife leans caution on the oil driver.
  MRK-add's pullback trigger not met (MRK green). This is a LOGGED deployment-floor decision, not a silent hold.
- Guardrail check: PASS (no trade). **-7% cut: N/A (NVDA -1.15% worst, above ~$196.91)** ✅. Ratchet: N/A (no winner
  ≥+15%; FDX +2.24%, MRK +1.66%) ✅. Sizes FDX 2.87% ($2,880) / MRK 2.93% ($2,943.77) / NVDA 2.92% ($2,930.05) of
  $100,485.06 equity ≤ 5% ✅. Day P/L ~flat (~$100,485 vs ~$100,529 prior close) ≪ -3% cap ✅. Weekly slots: 1 of 3
  used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: no trade placed → no Telegram (per protocol). Dry powder $91.74k (~91.3% cash). Next routine: midday risk check
  (re-check the -7% cut on NVDA + FDX vs live oil; tighten any winner that crosses +15%).

## 2026-07-22 16:05 ET — NO-OP (market-close wrap; HOLD FDX + MRK + NVDA, no cut/tighten; ALL 3 GREEN; market CLOSED)
- Qty / price / stop: none placed/closed. All 3 trailing legs live & confirmed via `orders --status open`
  (qty_available 0 = shares held by the open stops): FDX 9-sh 10% trail, stop $289.8945 / hwm $322.105 (order
  6f599c57, hwm ratcheted UP intraday); NVDA 14-sh 10% trail, stop $192.951 / hwm $214.39 (order 92b2b072, hwm
  ratcheted UP); MRK 23-sh 10% trail, stop $118.566 / hwm $131.74 (order 3d2f860f). Fully stop-protected.
- **Notable: the risk-off pre-market read REVERSED intraday.** Despite oil ~$94 + chips cooling into GOOGL/TSLA
  tonight, the tape rallied and all 3 closed GREEN. **NVDA: 14 sh @ $211.73, current $212.11, +$5.32 (+0.18%)**,
  day **+2.33%** — recovered from -2.83% at the open to green from entry. -7% cut line ~$196.91 → HOLD, no cut.
- FDX: 9 sh @ $313.00, current $321.02, **+$72.18 (+2.56%)**, day **+1.85%** — shrugged off the oil headwind;
  hwm ratcheted to $322.11. 0-15% band → stop stays 10%. HOLD.
- MRK: 23 sh @ $125.90, current $127.51, **+$37.03 (+1.28%)**, day **+0.99%** — steady defensive. Far above the
  ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (all 3 GREEN)** ✅. Ratchet: N/A (no winner ≥+15%; FDX +2.56%,
  MRK +1.28%, NVDA +0.18%) ✅. Sizes FDX 2.87% ($2,889.18) / MRK 2.92% ($2,932.73) / NVDA 2.95% ($2,969.54) of
  $100,528.99 equity ≤ 5% ✅. Day P/L equity $100,528.99 vs last_equity $100,380.29 = **+$148.70 (+0.148%)** ≪
  -3% cap ✅. Weekly slots: 1 of 3 used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $91.74k (~91.3% cash). Equity
  +$528.99 (+0.53%) vs the $100k paper start. GEHC (primary deployable) not deployed — deliberate cash into
  tonight's GOOGL/TSLA binary + GEHC's 7/29 earnings. Next routine: pre-market Thu 7/23 (GOOGL/TSLA capex prints
  after tonight's close = the semi-sentiment read).

## 2026-07-21 16:02 ET — NO-OP (market-close wrap; HOLD FDX + MRK + NVDA, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed at the close. Market CLOSED (`is_open: false`, 16:02 ET, next open Wed 7/22).
  Today's one trade was the FDX starter at the 7/21 open (9 sh @ $313.00 — already logged). All 3 trailing legs live &
  confirmed via `orders --status open` (qty_available 0 = shares held by the open stops): FDX 9-sh 10% trail, stop
  $285.30 / hwm $317 (order 6f599c57); NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072); MRK 23-sh
  10% trail, stop $118.566 / hwm $131.74 (order 3d2f860f). Fully stop-protected. open BUY + midday NO-OP + close NO-OP.
- **NVDA: 14 sh @ $211.73, current $206.78, -$69.30 (-2.34%)**, day **+1.72%** (recovered strongly intraday). **-7% cut
  line ~$196.91 → $206.78 is ABOVE it → HOLD, no cut.** Bear thesis SOFTENING (Kimi K3 re-read memory-bullish; risk-on
  tape); do NOT average down. Loser → ratchet N/A.
- FDX: 9 sh @ $313.00, current $315.19, **+$19.71 (+0.70%)**, day **+2.93%** — day 1 of the position, green. Well above
  the -7% cut. 0-15% band → stop stays 10% (no tighten). HOLD.
- MRK: 23 sh @ $125.90, current $126.27, **+$8.51 (+0.29%)**, day **+1.50%** — oil-insensitive defensive, back green.
  Far above the ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -2.34%)** ✅. Ratchet: N/A (no winner
  ≥+15%; FDX +0.70%, MRK +0.29%, NVDA red) ✅. Sizes FDX 2.83% ($2,836.71) / MRK 2.89% ($2,904.21) / NVDA 2.88%
  ($2,894.92) of $100,373.39 equity ≤ 5% ✅. Day P/L equity $100,373.39 vs last_equity $100,261.67 = **+$111.72
  (+0.111%)** ≪ -3% cap ✅. Weekly slots: 1 of 3 used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $91.74k (~91.4% cash). Equity +$373.39
  (+0.37%) vs the $100k paper start. Next routine: pre-market Wed 7/22.

## 2026-07-21 13:08 ET — NO-OP (midday risk check; HOLD FDX + MRK + NVDA, no cut/tighten; market OPEN)
- Qty / price / stop: none placed/closed. Market OPEN (`is_open: true`, 13:08 ET, next close 16:00). All three
  trailing legs live & confirmed via `orders --status open` (qty_available 0 = shares held by the open stops):
  FDX 9-sh 10% trail, stop $285.30 / hwm $317 (order 6f599c57, ratcheted UP intraday from $312.60); NVDA 14-sh
  10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072); MRK 23-sh 10% trail, stop $118.566 / hwm $131.74
  (order 3d2f860f). Fully stop-protected.
- **NVDA (the flagged one): 14 sh @ $211.73, current $205.33, -$89.61 (-3.02%)**, day **+1.01%** (recovering
  intraday). **-7% cut line ~$196.91 → $205.33 is ABOVE it → HOLD, no cut required.** Bear thesis SOFTENING
  (Kimi K3 re-read memory-bullish; risk-on tape); do NOT average down. Loser → ratchet N/A.
- FDX: 9 sh @ $313.00, current $315.42, **+$21.74 (+0.77%)**, day **+3.00%** — day's winner, 1 day into the
  position. Well above the -7% cut. **Ratchet: +0.77% in the 0-15% band → stop stays 10% (no tighten).** HOLD.
- MRK: 23 sh @ $125.90, current $125.36, **-$12.42 (-0.43%)**, day **+0.77%** — ~flat, oil-insensitive defensive.
  Far above the ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -3.02%)** ✅. Ratchet: N/A
  (FDX +0.77% & MRK ~flat — no winner ≥+15%; NVDA red) ✅. Sizes FDX 2.83% ($2,838.74) / MRK 2.87% ($2,883.28) /
  NVDA 2.86% ($2,874.61) of $100,333.91 equity ≤ 5% ✅. Day P/L equity $100,333.91 vs last_equity $100,261.67 =
  **+$72.24 (+0.072%)** ≪ -3% cap ✅. Weekly slots: 1 of 3 used (FDX) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed; a clean risk check isn't notify-worthy). Dry powder $91.74k (~91.4% cash).
  Next routine: market-close wrap 7/21.

## 2026-07-20 16:02 ET — NO-OP (market-close wrap; HOLD MRK + NVDA, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed. Market CLOSED (`is_open: false`, 16:02 ET, next open Tue 7/21). Both trailing
  legs live & confirmed via `orders --status open`: MRK 23-sh 10% trail, stop $118.566 / hwm $131.74 (order 3d2f860f);
  NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072). Fully stop-protected. No trades today: open +
  midday + close all NO-OP → nothing to cut/tighten at the wrap.
- NVDA: 14 sh @ $211.73, current $203.19, **-$119.56 (-4.03%)**, day **+0.19%** (held above $200). **-7% cut line
  ~$196.91 → $203.19 is ABOVE it → HOLD, no cut.** Slide remains a structural semi bear-market re-rating (Kimi K3), not
  a fresh thesis-breaker; do NOT average down. Loser → ratchet N/A.
- MRK: 23 sh @ $125.90, current $124.41, **-$34.27 (-1.18%)**, day **-2.42%** — day's laggard but ~flat from entry,
  oil-insensitive defensive. Far above the ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -4.03%)** ✅. Ratchet: N/A (both red,
  no winner ≥+15%) ✅. Sizes MRK 2.85% ($2,861.43) / NVDA 2.84% ($2,844.66) of $100,260.64 equity ≤ 5% ✅. Day P/L equity
  $100,260.64 vs last_equity $100,326.39 = **-$65.75 (-0.066%)** ≪ -3% cap ✅. Weekly slots: 0 of 3 used (new week) ✅.
  Paper mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $94.55k (~94.3% cash). Equity +$260.64
  (+0.26%) vs the $100k paper start. Next routine: pre-market Tue 7/21.

## 2026-07-20 13:05 ET — NO-OP (midday risk check; HOLD MRK + NVDA, no cut/tighten; market OPEN)
- Qty / price / stop: none placed/closed. Market OPEN (`is_open: true`, 13:05 ET, next close 16:00). Both trailing
  legs live & confirmed via `orders` (qty_available 0 = shares held by the open stops): MRK 23-sh 10% trail, stop
  $118.566 / hwm $131.74 (order 3d2f860f); NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072).
  Fully stop-protected.
- **NVDA re-check (the flagged one): 14 sh @ $211.73, current $203.665, -$112.91 (-3.81%)**, day **+0.42%**
  (recovering intraday, stabilizing above $200). **-7% cut line ~$196.91 → current $203.665 is ABOVE it → HOLD, no
  cut required.** The slide remains a structural semi bear-market re-rating (Kimi K3), not a fresh thesis-breaker;
  higher bar to hold but nowhere near the cut. Do NOT average down. Loser → ratchet N/A.
- MRK: 23 sh @ $125.90, current $125.72, **-$4.14 (-0.14%)**, day **-1.40%** — essentially flat, oil-insensitive
  defensive. Far above the ~$117.09 -7% cut. 0-15% band → stop stays 10%. HOLD.
- Guardrail check: PASS (no trade). **-7% cut: N/A (none at/below -7%; worst NVDA -3.81%)** ✅. Ratchet: N/A (MRK
  ~flat, NVDA red — no winner ≥+15%) ✅. Sizes MRK 2.88% ($2,891.56) / NVDA 2.84% ($2,851.31) of $100,297.42 equity
  ≤ 5% ✅. Day P/L equity $100,297.42 vs last_equity $100,326.39 = **-$28.97 (-0.029%)** ≪ -3% cap ✅. Weekly slots:
  0 of 3 used (new week) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed; a clean risk check isn't notify-worthy). Dry powder $94.55k (~94.3% cash). Next
  routine: market-close wrap 7/20.

## 2026-07-17 16:02 ET — NO-OP close / weekly-review (HOLD MRK + NVDA; META already CLOSED by trail this AM; market CLOSED)
- Qty / price / stop: none placed this run. Market CLOSED (`is_open: false`, 16:02 ET, next open Mon 7/20). MRK + NVDA
  trailing legs live & confirmed via `orders` (qty_available 0 = shares held by the open stop orders): MRK 23-sh 10%
  trail (order 3d2f860f); NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072). Both stop-protected.
- **META CLOSED @ ~09:45 ET by its standing 7% trailing stop** (recorded here for the log — the fill happened intraday,
  midday updated portfolio.md but no trade-log entry was written yet). Both legs filled: 3 sh @ $637.796667 + 4 sh @
  $637.57 (avg ~$637.68); entry $578.4486 → **realized +$414.53 / +10.24%**. The trail fired as META pulled back 7%
  from its $686.075 hwm on the TSMC-sell-the-news tech risk-off. The 7% ratchet (tightened 7/10 at the +17% high) did
  its job — banked a double-digit winner instead of a round-trip. Logged to signals-learnings as a validated signal.
- MRK: 23 sh @ $125.90, current $127.495, **+$36.69 (+1.267%)**, day -0.11% — defensive flat on a mild risk-off day.
  Above the ~$117.09 -7% cut. 10% trail live. HOLD — winner but <+15% so ratchet N/A.
- NVDA: 14 sh @ $211.73, current $202.6266, **-$127.45 (-4.30%)**, day -2.30% (day-4 starter, TSMC sell-the-news +
  semi risk-off, NOT a thesis break; Vera Rubin AI-factory deal, Strong Buy $301.62). Above the ~$196.91 -7% cut & the
  $191.31 trail. 10% trail live. HOLD — loser so ratchet N/A; nowhere near the cut line.
- Guardrail check: PASS (no new trade). -7% cut: N/A (none at/below -7%; worst NVDA -4.30%) ✅. Ratchet: N/A (MRK <+15%,
  NVDA red). Sizes MRK 2.92% / NVDA 2.83% ≤ 5% ✅. Day P/L equity $100,323.73 vs last_equity $100,581.77 = **-$258.04
  (-0.256%)** ≪ -3% cap ✅. **Weekly slots: 2 of 3 used (MRK + NVDA)** — META was a CLOSE, not a new slot ✅. Paper mode
  ✅. No options/margin/short/crypto ✅.
- Note: EOD / weekly-review Telegram summary sent (close routine always notifies). Dry powder $94.55k (~94.2% cash).
  Week's scorecard: banked the META winner (+10.24%) on the ratcheted trail; deployment-floor stayed a deliberate,
  logged cash call into the risk-off Friday (FDX oil-wrong + spread-gated; NVDA already held). Next routine: pre-market
  Mon 7/20.

## 2026-07-17 09:31 ET — NO-OP (market-open; HOLD all 3, deployment-floor = deliberate cash; market OPEN)
- Qty / price / stop: none placed. Market OPEN (`is_open: true`, 09:31 ET, next close 16:00). All 4 trailing legs
  live & confirmed via `orders`: META 4-sh & 3-sh both 7% trail, stop $638.04975 / hwm $686.075; MRK 23-sh 10% trail,
  stop $116.262 / hwm $129.18 (ratcheted up on today's high); NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693.
  Fully stop-protected.
- Standing-plan catch-up: the 7/17 pre-market plan was HOLD-all + a DELIBERATE logged decision to stay ~89.7% cash
  into today's weekly review — NOT a pending buy. So there is no missed guardrail-clean buy to salvage; open = execute
  the "hold" plan. Live tape confirms the risk-off-tech read (META -2.77%, NVDA -2.44% on the day) → no reason to force
  the last weekly slot into a risk-off Friday. Named deployable FDX still oil-wrong + spread-gated; NVDA already held.
- META: 7 sh @ $578.4486, current $646.11, **+$473.66 (+11.70%)**, day **-2.77%** (rode the tech risk-off). Weight
  4.50% ($4,522.80 / $100,414.57) ≤ 5% cap → no add. 7% trail live (never loosen). Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $129.18, **+$75.44 (+2.61%)**, day **+1.21%** — defensive doing its job on a risk-off
  day. Above the ~$117.09 -7% cut. 10% trail live (hwm ratcheted to $129.18). HOLD.
- NVDA: 14 sh @ $211.73, current $202.35, **-$131.33 (-4.43%)**, day **-2.44%** (day-4 starter, TSMC sell-the-news +
  semi risk-off, NOT a thesis break). Above the ~$196.91 -7% cut & the $191.31 trail. 10% trail live. HOLD — do NOT
  add; midday re-checks the cut.
- Guardrail check: PASS (no trade). -7% cut: N/A (none at/below -7%; worst NVDA -4.43%) ✅. Sizes META 4.50% / MRK
  2.96% / NVDA 2.82% ≤ 5% ✅. Day P/L equity $100,414.57 vs last_equity $100,581.77 = **-$167.20 (-0.17%)** ≪ -3% cap
  ✅. **Weekly slots: 2 of 3 used (MRK + NVDA)** ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (no trade placed). Dry powder $90.09k (~89.7% cash). Next routine: midday risk check, then
  market-close + **weekly-review at today's close**.

## 2026-07-16 16:02 ET — NO-OP (market-close wrap; HOLD all 3, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed. Market CLOSED (`is_open: false`, 16:02 ET) — properly-timed close run.
  All 4 trailing legs live & confirmed via `orders`: META 4-sh & 3-sh both 7% trail, stop $638.04975 / hwm $686.075;
  MRK 23-sh 10% trail, stop $116.037 / hwm $128.93 (ratcheted UP on today's high); NVDA 14-sh 10% trail, stop
  $191.31237 / hwm $212.5693. Fully stop-protected.
- No trades today: open + midday both NO-OP. Close wrap = nothing to cut/tighten.
- META: 7 sh @ $578.4486, current $664.00, **+$598.86 (+14.79%)**, day **-2.54%** (give-back off yesterday's highs;
  deep green from entry). **Loss-cut: +14.79% ≫ -7% → HOLD. Ratchet: +14.79% slipped back into the 0-15% band; both
  legs already at 7% (tightened 7/10) → NEVER LOOSEN, stays 7%.** Weight 4.62% ($4,648 / $100,577.51) ≤ 5% cap → no
  add. Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $127.67, **+$40.71 (+1.41%)**, day **+3.29%** — the day's winner (Ph3 KEYNOTE-C93 win +
  JPM PT→$140 tailwind; oil-insensitive defensive did its job). Above the ~$117.09 -7% cut. 10% trail live. HOLD —
  winner but <+15% so ratchet N/A.
- NVDA: 14 sh @ $211.73, current $207.30, **-$62.02 (-2.09%)**, day **-2.45%** (day-2 starter, soft-tech session).
  Above the ~$196.91 -7% cut. 10% trail live. HOLD — loser so ratchet N/A; nowhere near the cut line. TSMC Q2
  confirmed the AI-demand thesis. Earnings ~late Aug.
- Guardrail check: PASS (no trade). -7% cut: N/A (none at/below -7%; worst NVDA -2.09%) ✅. Ratchet: META already at
  7% target ✅, others N/A (MRK <+15%, NVDA red). Sizes META 4.62% / MRK 2.92% / NVDA 2.89% ≤ 5% ✅. Day P/L equity
  $100,577.51 vs last_equity $100,678.10 = **-$100.59 (-0.10%)** ≪ -3% cap ✅. **Weekly slots: 2 of 3 used (MRK +
  NVDA)** ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $90.09k (~89.6% cash). Next routine:
  pre-market Fri 7/17 → weekly review at Fri close.

## 2026-07-16 13:05 ET — NO-OP (midday risk check; HOLD all 3, no cut/tighten; market OPEN)
- Qty / price / stop: none placed/closed. Market OPEN (`is_open: true`, 13:05 ET, next close 16:00). All 4 trailing
  legs live & confirmed via `orders`: META 4-sh & 3-sh both 7% trail, stop $638.04975 / hwm $686.075; MRK 23-sh 10%
  trail, stop $115.308 / hwm $128.12 (order 3d2f860f, ratcheted up on today's high); NVDA 14-sh 10% trail, stop
  $191.31237 / hwm $212.5693 (order 92b2b072). Fully stop-protected.
- META: 7 sh @ $578.4486, current $669.03, **+$634.07 (+15.66%)**, day **-1.80%** (mild give-back off yesterday's
  highs; deep green from entry). **Loss-cut: +15.66% ≫ -7% → HOLD. Ratchet: +15.66% has CROSSED into the 15-30%
  band → target trail = 7%; both legs ALREADY at 7% (tightened 7/10) → no change, and never loosen.** Weight 4.65%
  ($4,683.21 / $100,617.03) ≤ 5% cap → no add. Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $127.985, **+$47.96 (+1.66%)**, day **+3.54%** (defensive firming; Ph3 KEYNOTE-C93
  win + JPM PT→$140 tailwind). Above the ~$117.09 -7% cut. 10% trail live. HOLD — winner but <+15% so ratchet N/A.
- NVDA: 14 sh @ $211.73, current $207.10, **-$64.82 (-2.19%)**, day **-2.54%** (day-3 starter, soft-tech session).
  Above the ~$196.91 -7% cut. 10% trail live. HOLD — loser so ratchet N/A; nowhere near the cut line. TSMC Q2
  confirmed the AI-demand thesis. Earnings ~late Aug.
- Guardrail check: PASS (no trade). -7% cut: N/A (none at/below -7%; worst NVDA -2.19%) ✅. Ratchet: META already at
  7% target ✅, others N/A (MRK <+15%, NVDA red). Sizes META 4.65% / MRK 2.93% / NVDA 2.88% ≤ 5% ✅. Day P/L equity
  $100,617.03 vs last_equity $100,678.10 = **-$61.07 (-0.06%)** ≪ -3% cap ✅. **Weekly slots: 2 of 3 used (MRK +
  NVDA)** ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed; a clean risk check isn't notify-worthy). Dry powder $90.09k (~89.5% cash). Next
  routine: market-close wrap 7/16.

## 2026-07-15 16:02 ET — NO-OP (market-close wrap; HOLD all 3, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed. Market CLOSED (`is_open: false`, 16:02 ET) — properly-timed close run.
  All 4 trailing legs live & confirmed via `orders`: META 4-sh & 3-sh both 7% trail, stop $638.04975 / hwm $686.075
  (7/10 tighten, auto-ratcheted UP on today's new high); MRK 23-sh 10% trail, stop $115.263 / hwm $128.07 (order
  3d2f860f); NVDA 14-sh 10% trail, stop $191.31237 / hwm $212.5693 (order 92b2b072, ratcheted up on today's high).
  Fully stop-protected.
- No trades today: 09:47 open BOUGHT NVDA (already logged) + 13:05 midday NO-OP. Close wrap = nothing to cut/tighten.
- META: 7 sh @ $578.4486, current $680.90, **+$717.16 (+17.71%)**, day **+3.00%** (fresh highs). **Loss-cut: +17.71%
  ≫ -7% → HOLD. Ratchet: +17.71% in the 15-30% band → target trail 7%; both legs ALREADY at 7% → no change, never
  loosen.** Weight 4.73% ($4,766.30 / $100,674.89) ≤ 5% cap → no add. Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $123.61, **-$52.67 (-1.82%)**, day **+2.34%** (defensive firming). Above the ~$117.09
  -7% cut. 10% trail live. HOLD per stop rules.
- NVDA: 14 sh @ $211.73, current $212.40, **+$9.38 (+0.32%)**, day **+0.28%** — day-1 closed slightly GREEN, recovered
  from the midday -1.84%. Above the ~$196.91 -7% cut. 10% trail live. HOLD — winner but <+15% so ratchet N/A. TSMC AI
  read Thu 7/16.
- Guardrail check: PASS (no trade). -7% cut: N/A (none at/below -7%; worst MRK -1.82%) ✅. Ratchet: META already at 7%
  target ✅, others N/A (<+15%). Sizes META 4.73% / MRK 2.82% / NVDA 2.95% ≤ 5% ✅. Day P/L equity $100,674.89 vs
  last_equity $100,460.35 = **+$214.54 (+0.21%)** ≪ -3% cap ✅. **Weekly slots: 2 of 3 used (MRK + NVDA)** ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $90.09k (~89.5% cash). Next routine:
  pre-market Thu 7/16 (TSMC Q2 ~2am ET = AI-demand read for NVDA/AVGO/MU).

## 2026-07-15 13:05 ET — NO-OP (midday risk check; HOLD all 3, no cut/tighten; market OPEN)
- Qty / price / stop: none placed/closed. Market OPEN (`is_open: true`, 13:05 ET, next close 16:00). All 4 trailing
  legs live & confirmed via `orders`: META 4-sh & 3-sh both 7% trail, stop $638.04975 / hwm $686.075 (auto-ratcheted
  UP from the 7/10 tighten as META printed a new high today); MRK 23-sh 10% trail, stop $115.263 / hwm $128.07 (order
  3d2f860f); NVDA 14-sh 10% trail, stop $190.87191 / hwm $212.0799 (order 92b2b072). Fully stop-protected.
- META: 7 sh @ $578.4486, current $675.25, **+$677.61 (+16.74%)**, day **+2.15%** (fresh highs). **Loss-cut: +16.74%
  ≫ -7% → HOLD. Ratchet: +16.74% has now CROSSED into the 15-30% band → target trail = 7%; both legs are ALREADY at
  7% (tightened 7/10) → no change, and never loosen.** Weight 4.70% ($4,726.75 / $100,572.59) ≤ 5% cap → no add.
  Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $123.755, **-$49.34 (-1.70%)**, day **+2.46%** (defensive firming). Above the ~$117.09
  -7% cut. 10% trail live. HOLD per stop rules.
- NVDA: 14 sh @ $211.73, current $207.83, **-$54.60 (-1.84%)**, day **-1.87%** (day-1 of the new position, mild red on
  a soft-tech session; oil/Iran still the macro overhang). Above the ~$196.91 -7% cut. 10% trail live. HOLD — loser so
  ratchet N/A; nowhere near the cut line. Earnings/TSMC AI-demand read Thu 7/16.
- Guardrail check: PASS (no trade). -7% cut: N/A (none at/below -7%; worst is NVDA -1.84%) ✅. Ratchet: META already at
  7% target ✅, others N/A (red). Sizes META 4.70% / MRK 2.83% / NVDA 2.89% ≤ 5% ✅. Day P/L equity $100,572.59 vs
  last_equity $100,460.35 = **+$112.24 (+0.11%)** ≪ -3% cap ✅. **Weekly slots: 2 of 3 used (MRK + NVDA)** ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed; a clean risk check isn't notify-worthy). Dry powder $90.09k (~89.6% cash). Next
  routine: market-close wrap 7/15.

## 2026-07-14 16:02 ET — NO-OP (market-close wrap; HOLD META + MRK, no cut/tighten; market CLOSED)
- Qty / price / stop: none placed/closed. Market CLOSED (`is_open: false`, 16:02 ET) — properly-timed close run.
  All three trailing legs live & confirmed via `orders`: META 4-sh & 3-sh legs both 7% trail, stop $630.3912 /
  hwm $677.84 (tightened 7/10); MRK 23-sh 10% trail, stop $115.263 / hwm $128.07 (order 3d2f860f). Fully stop-protected.
- No trades today: 09:xx open (no fresh plan; NVDA oil-gated) + midday risk check were both NO-OP. Nothing to cut/tighten.
- META: 7 sh @ $578.4486, current $661.00, **+$577.86 (+14.27%)**, day **+0.65%** (green into the close). Weight
  4.61% ($4,627 / $100,460.53) ≤ 5% cap → no add. **Loss-cut: +14.27% ≫ -7% → HOLD. Ratchet: +14.27% in the
  0-15% band, stop already 7% → NEVER LOOSEN, stays 7%.** Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $120.80, **-$117.30 (-4.05%)**, day **-2.60%** (day's laggard but defensive; above
  the ~$117.09 -7% cut). 10% trail live. HOLD per stop rules.
- Guardrail check: PASS (no trade). Day P/L equity $100,460.53 vs last_equity $100,504.93 = **-$44.40 (-0.044%)**
  ≪ -3% cap ✅. Sizes META 4.61% / MRK 2.77% ≤ 5% ✅. **Weekly slots: 1 of 3 used (MRK)** ✅. Paper mode ✅. No
  options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $93.06k (~92.6% cash). NVDA stays
  primary tech deployable once the oil/Iran shock stabilizes (CPI benign + lease firm; oil = only remaining gate).
  Next routine: pre-market Wed 7/15.

## 2026-07-13 16:18 ET — NO-OP (market-close wrap; HOLD META + MRK, no cut/tighten; market CLOSED; API RESTORED)
- Qty / price / stop: none placed/closed. Market CLOSED (`is_open: false`, 16:17 ET) — properly-timed close run.
  All three trailing legs live & confirmed via `orders`: META 4-sh & 3-sh legs both stop $630.3912 / hwm $677.84
  (7% trail, tightened 7/10); MRK 23-sh stop $115.263 / hwm $128.07 (10% trail, order 3d2f860f). Fully stop-protected.
- **API note: Alpaca 401 outage RESOLVED.** Earlier today (midday/close) the key was 401 → carried-forward stale
  snapshot + Telegram flag. By this run the human had rotated the key; `account`/`positions` return live data → this
  is a genuine live EOD read, healing the stale snapshot. (Logged to signals-learnings.)
- No trades today: 09:32 open = NO-OP (falling-knife risk-off + no fresh plan); midday = NO-OP. Nothing to cut/tighten.
- META: 7 sh @ $578.4486, current $656.69, **+$547.69 (+13.53%)**, day **-1.87%** (faded with the AI-under-pressure
  tape but deep green from entry). Weight 4.57% ($4,596.83 / $100,501.22) ≤ 5% cap → no add. **Loss-cut: +13.53% ≫
  -7% → HOLD. Ratchet: +13.53% in the 0-15% band, stop already at 7% → NEVER LOOSEN, stays 7%.** Earnings Jul 29.
- MRK: 23 sh @ $125.90, current $124.03, **-$43.01 (-1.49%)**, day **+0.40%** (defensive did its job on the oil-spike
  tape). -7% cut: N/A (far above ~$117.09). 10% trail live. HOLD per stop rules.
- Guardrail check: PASS (no trade). Day P/L equity $100,501.22 vs last_equity $100,581.02 = **-$79.80 (-0.079%)**
  ≪ -3% cap ✅. Sizes META 4.57% / MRK 2.84% ≤ 5% ✅. **Weekly slots: 1 of 3 used (MRK)** ✅. Paper mode ✅. No
  options/margin/short/crypto ✅.
- Note: EOD Telegram summary sent (close routine always notifies). Dry powder $93.06k (~92.6% cash). Deployment gated
  pre-CPI — **June CPI Tue 7/14 8:30 ET is the binary** (+ big-bank earnings pre-open); named deployable once tape/CPI
  clear = NVDA (lease gate firming). Next routine: pre-market Tue 7/14.

## 2026-07-13 09:32 ET — NO-OP (market-open; HOLD META + MRK, NO new positions — falling-knife risk-off open)
- Qty / price / stop: none placed, none closed, no stop touched. Market OPEN (clock is_open=true).
- Standing-plan catch-up: the last pre-market plan (7/9) was FULLY executed (MRK bought 7/9, FDX skipped on
  spread, META held) → nothing pending. **No fresh pre-market plan exists for today** — origin/main's newest
  commit is the 7/9 market-close wrap; no Fri 7/10 or Mon 7/13 pre-market commit. (NB: META's stop was
  tightened to 7% on the broker Fri 7/10 13:06 ET — a Friday routine ran but its memory commit never reached
  main. Reconciled all state from the live broker per the "trust the broker" learning; committing now heals it.)
- TAPE (WebSearch 7/13): fresh **geopolitical risk-off open** — US renewed Strait-of-Hormuz strikes over the
  weekend, **Iran retaliated vs US allies (Kuwait/Jordan/Qatar), oil jumping**; futures Dow -0.1% / S&P -0.3% /
  Nasdaq-100 -0.8%, prediction mkts ~22% odds of an up open. Fri 7/11 closed strong (S&P +0.42% 7,575) but today
  is day-1 of an unconfirmed sentiment shock = the falling-knife setup.
- DECISION — **no new positions.** (a) **Falling-knife rule binds**: unconfirmed Iran/oil risk-off, not a
  confirmed bottom. (b) **FDX fails spread gate** — sampled 3x LIVE: bid $296.75 / ask $316.92 = **6.6%, feed
  frozen** (identical timestamps) → un-buyable, AND oil-sensitive on an oil-spike day = doubly wrong. (c) **NVDA**
  tight spread (~$209.74, 0.02%) but B200-lease gate unconfirmed + no fresh research to clear it → do NOT initiate.
  (d) No fresh plan today. **Deployment-floor: staying ~92% cash is a DELIBERATE, logged decision today**, not a
  silent default — the one live deployable (FDX) is spread-gated + oil-wrong, and the tape is an unconfirmed shock.
- META: 7 sh @ $578.4486, current $664.71, **+$603.83 (+14.91%)**, day -0.67%. Thesis STRENGTHENED (best week
  since early 2024, +15% on Meta Compute + Muse Image/Spark 1.1 + Iris chip Sept). Weight 4.63% ($4,652.97 /
  $100,542.25) ≤ 5% cap → no add (and not chasing into a risk-off open after a 15% week). Earnings Jul 29.
  Stops: two trailing legs (4-sh & 3-sh) at **7% trail** (tightened Fri at the +17% $677 high), hwm $677.84,
  stop $630.3912 — +14.91% now sits in the 0-15% band but rule is NEVER LOOSEN → leave at 7%. HOLD.
- MRK: 23 sh @ $125.90, current $123.30, **-$59.80 (-2.07%)**, day -0.19%. No thesis-breaker. -7% cut: N/A
  (far above ~$117.09). 10% trail live (stop $115.263, hwm $128.07, order 3d2f860f). HOLD per stop rules.
- Guardrail check: PASS (no trade). Day P/L equity $100,542.25 vs last_equity $100,581.02 = **-$38.77 (-0.04%)**
  ≪ -3% cap. Both names ≤ 5% size cap. **New week 7/13 → 0 of 3 new-position slots used.** TRADING_MODE = paper.
  No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed; a risk-off HOLD isn't notify-worthy). Dry powder ~$93.1k. MU/AVGO/GEHC
  WATCH. This week's catalysts: bank earnings (JPM/GS/BAC), TSMC (AI read), NFLX, UNH. Next routine: midday risk check.

## 2026-07-09 16:02 ET — NO-OP (market-close wrap; HOLD META + MRK, no cut/tighten; market CLOSED)
- Qty / price / stop: none — no order placed or closed. All three trailing legs live & confirmed via `orders`:
  META 4-sh & 3-sh legs both stop $569.943 / hwm ratcheted UP to $633.27 (new intraday high today); MRK 23-sh
  stop $115.263 / hwm $128.07. All 10% trail, GTC, status new. Both positions fully stop-protected.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET). Today's one trade was the 09:36 MRK
  deployment-floor starter (23 sh @ $125.90, 10% trail — already logged). Wrap: **META ripped +4.58% today**
  ($603.12 → $630.73 close, a FRESH intraday high), fully reclaiming its -4% open gap and then some; 7 sh @
  $578.4486 blended, unrealized **+$365.97 (+9.04%)**. **Loss-cut: +9.04% far above the -7% cut → HOLD.**
  **Ratchet: +9.04% inside the 0–15% band → trail stays 10%, no tighten (never loosen).** MRK: 23 sh @ $125.90,
  $125.07, **-$19.09 (-0.66%)** — barely red, far inside the -7% cut → HOLD; loser so ratchet N/A. EOD summary
  sent via Telegram.
- Guardrail check: PASS (no trade). -7% cut: N/A (META +9.04% green; MRK -0.66% » -7%) ✅. +15% ratchet: N/A
  (META +9.04% < +15%; MRK red) ✅. Sizes: META 4.40% ($4,415.11) / MRK 2.87% ($2,876.61) of equity, both ≤ 5%
  cap ✅. Day P/L equity $100,346.86 vs last_equity $100,172.68 = +$174.18 (+0.17%) → no daily-loss-cap concern ✅.
  Weekly slots: 1 of 3 used (MRK) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $93.06k (~92.7% cash). Deployment-floor rule: 1 slot deployed (MRK) this week; NVDA gate
  unconfirmed → do NOT initiate; FDX spread-gated (broken paper feed); MU/AVGO/GEHC WATCH. Next routine:
  pre-market Fri 7/10 → weekly review at Fri close.

## 2026-07-09 09:36 ET — BUY MRK (deployment-floor deploy; defensive starter; market OPEN)
- Qty / price / stop: **BUY 23 sh MRK @ $125.90** (market, filled at the ask, cost basis $2,895.70). **10% trailing stop attached: stop_price $112.8465 / hwm $125.385, GTC, live** (order 3d2f860f). Position now fully protected.
- Reasoning: Executed the pre-market deployment-floor plan's PRIMARY deployable (MRK). Both gates evaluated LIVE: **(a) spread re-sampled 3x = 0.45%** (bid $125.33 / ask $125.90, 100 sh each side) → TIGHT, clears the <~2-3% gate; **(b) tape** — SPY ~flat (-0.2%, market near record highs, NOT a rout). New wrinkle vs the 07:10 plan: **Iran/oil RE-escalated this morning** (US airstrikes on 90 targets, oil +4.4%), flipping the plan's "oil fading" premise, and **META gapped -4%** at the open (idiosyncratic — broad market flat). But MRK is precisely the DEFENSIVE, oil-insensitive, low-tech-correlation name named for exactly this tape — a war/oil-shock + tech-selloff day is its environment (rotation into defensives), not a disqualifier. MRK pulled back to ~$126 → upside now ~4.6% vs consensus PT $131.67 (better than the ~2% the plan feared). Falling-knife rule doesn't bind (no confirmed 3+ day broad rout); deployment-floor discipline (96% cash, 0 slots) argues against drifting into cash. Small starter (2.88%), fresh 10% trail, limited defined risk.
- EXECUTION NOTE: the `buy` script timed out at 15s (market order still `new`) and exited WITHOUT attaching the trail. Checked positions → the order had filled LATE at $125.90 (clean, no slippage — the tight 0.45% ask held). Targeted cancel by order-id returned 422 "already filled," so I manually submitted the trailing_stop sell leg (23 sh, 10%, GTC) → attached. **Distinct from the FDX flicker: here the ask was genuinely good, so the late fill was fine — the timeout was script latency, not a bad price.**
- Guardrail check: PASS. Size: MRK 2.88% of equity ($2,881.90 / $100,010.48) ≤ 5% ✅. Weekly slots: MRK = fresh position → **1 of 3 used** ✅. Daily loss cap: day P/L -$162.20 (-0.16%) « -3% ✅. Paper mode ✅. No options/margin/short/crypto ✅. 10% trail attached at entry ✅.

## 2026-07-09 09:36 ET — SKIP FDX (spread gate failed; oil headwind returned)
- Qty / price / stop: none — not placed.
- Reasoning: FDX secondary deployable — spread re-sampled 3x = **4.6%** (bid $314.14 / ask $328.65), still the broken/pathologically-wide paper feed → fails the <~2-3% gate; a market buy would lift a junk ask ~4.6% above bid. Also the fresh Iran/oil re-escalation (oil +4.4%) revives the fuel-cost headwind that makes FDX a worse deploy on THIS tape. Skip; retry when the quote normalizes.
- Guardrail check: N/A (no trade).

## 2026-07-09 09:36 ET — HOLD META (no add, no cut; market OPEN)
- Qty / price / stop: none. Both trailing legs live (4-sh stop $565.452 / hwm $628.28; 3-sh stop $562.833 / hwm $625.37).
- Reasoning: META 7 sh @ $578.4486, current $581.15, +$18.91 (+0.47%), gapped -3.6% intraday (idiosyncratic; broad market flat). At target weight ~4.07%, no add (plan = HOLD). Loss-cut: +0.47% green » -7% → HOLD. Ratchet: +0.47% in the 0–15% band → trail stays 10%.
- Guardrail check: PASS. -7% cut N/A ✅. +15% ratchet N/A ✅. Size 4.07% ≤ 5% ✅.

## 2026-07-08 16:02 ET — NO-OP (market-close wrap; HOLD META, green, no cut/tighten; market CLOSED)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs live & confirmed via `orders`:
  4-sh leg stop_price $565.452 / hwm $628.28; 3-sh leg stop_price $562.833 / hwm $625.37. Both 10% trail, GTC,
  status new. Full 7-sh position stop-protected.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET, post-16:00 close). No trades today —
  the standing plan was HOLD META / no new positions all day (deployment-floor decision to stay >90% cash was a
  LOGGED deliberate call: falling-knife Iran/oil war-shock + the same-day FOMC-minutes binary). Only holding is
  META: 7 sh @ $578.4486 blended entry, closed $603.12, unrealized +$172.70 (+4.27%), faded −2.02% intraday
  ($615.58 → $603.12) into/after the 2pm FOMC June minutes — a mild risk-off drift, nothing thesis-breaking.
  **Loss-cut: +4.27% far above the −7% cut → HOLD.** **Ratchet: +4.27% inside the 0–15% band → trail stays 10%,
  no tighten (never loosen).** EOD summary sent via Telegram.
- Guardrail check: PASS (no trade). −7% cut: N/A (position +4.27% green) ✅. +15% ratchet: N/A (+4.27% < +15%) ✅.
  META 4.21% of equity ($4,221.84 / $100,172.68) ≤ 5% size cap ✅. Day P/L equity $100,172.68 vs last_equity
  $100,259.90 = −$87.22 (−0.087%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $95.95k intact (~95.8% cash). Deployment-floor rule stays OPEN — MRK (primary,
  defensive/oil-insensitive) + FDX (secondary, oil-headwind) remain spread-gated on the broken paper feed;
  re-sample live next session. NVDA gate unconfirmed → do NOT initiate. MU/AVGO/GEHC WATCH. Next routine:
  pre-market Thu 7/9.

## 2026-07-08 13:05 ET — NO-OP (midday risk check; HOLD META, green, no cut/tighten; market OPEN)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs live & confirmed via `orders`:
  4-sh leg stop_price $565.452 / hwm $628.28; 3-sh leg stop_price $562.833 / hwm $625.37. Both 10% trail, GTC,
  status new. Full 7-sh position stop-protected.
- Reasoning: Properly-timed midday risk check (`is_open: true`, 13:05 ET). Only position is META: 7 sh @
  $578.4486 blended entry, current $604.08, unrealized +$179.42 (+4.43%), intraday -1.87% ($615.58 → $604.08,
  mild pullback consistent with the risk-off tape into the 2pm FOMC minutes). **Loss-cut: +4.43% green → far
  above the -7% cut line → HOLD, no close.** **Ratchet: +4.43% inside the 0–15% band → trail stays 10%, no
  tighten (fires at +15%; never loosen).** No position down -7% to cut; no winner ≥+15% to tighten. Midday is
  risk-only — no new positions (FDX/MRK remain spread-gated deployables for /trade; NVDA gate unconfirmed;
  MU/AVGO/GEHC WATCH). Nothing to do.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +4.43% green) ✅. +15% ratchet: N/A (+4.43% < +15%) ✅.
  META 4.22% of equity ($4,228.56 / $100,179.40) ≤ 5% size cap ✅. Day P/L equity $100,179.40 vs last_equity
  $100,259.90 = -$80.50 (-0.080%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅.
  Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $95.95k intact (~95.8% cash). Deployment-floor rule
  stays OPEN (MRK primary / FDX secondary spread-gated on the broken paper feed). FOMC June minutes land 2pm ET
  (week's binary, not yet out at 13:05). Next routine: market-close wrap Wed 7/8.

## 2026-07-08 09:32 ET — NO-OP (market-open; HOLD META, deployables spread-gated + tape not cleared; market OPEN)
- Qty / price / stop: none — no order placed. Both META trailing legs live: 4-sh stop $565.452 / hwm $628.28;
  3-sh stop $562.833 / hwm $625.37 (10% trail, GTC, new). Full 7-sh position stop-protected.
- Reasoning: Properly-timed open run (`is_open: true`, 09:30 ET). No pending guardrail-clean plan to catch up
  (7/6 & 7/7 FDX attempts were both CANCELED → 0 slots used). Executed the standing pre-market plan: **HOLD META,
  NO new positions at the open** — a LOGGED deployment-floor decision now confirmed by live data. Three independent
  reasons: (1) **falling-knife rule** — Iran ceasefire "over" + oil +6% is an unconfirmed sentiment risk-off, not a
  confirmed bottom; (2) **FOMC June minutes 2pm ET** = same-day binary, unresolved; (3) **spread gate FAILS** —
  re-sampled live 2x at 09:31: MRK bid $121.91/ask $127.33 = 4.44% (100-200 sh), FDX bid $312.35/ask $328.65 =
  5.09% (40 sh) — both >2-3%, same pathologically-wide paper feed as 7/6/7/7; a market buy fills ~4-5% below bid,
  near-instantly tripping the 10% trail. So neither MRK (primary) nor FDX (secondary) is buyable cleanly today.
  META: 7 sh @ $578.4486 blended, $611, unrealized +$227.86 (+5.63%), intraday -0.74% (mild risk-off, consistent
  with the tape). **Loss-cut: +5.63% far above -7% → HOLD. Ratchet: +5.63% inside 0-15% band → trail stays 10%,
  no tighten.**
- Guardrail check: PASS (no trade). -7% cut: N/A (META +5.63% green) ✅. +15% ratchet: N/A (+5.63% < +15%) ✅.
  META 4.27% of equity ($4,277 / $100,226.41) ≤ 5% size cap ✅. Day P/L equity $100,226.41 vs last_equity
  $100,259.90 = -$33.49 (-0.033%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅.
  TRADING_MODE = paper ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $95.95k intact (~95.7% cash). Deployment-floor rule stays
  OPEN — deployables MRK (primary, defensive/oil-insensitive) + FDX (secondary, oil-headwind today) remain
  spread-gated; re-sample live post-minutes. NVDA gate unconfirmed (lease $4.22 soft; H20 China license restart =
  new +) → do NOT initiate. MU/AVGO/GEHC = WATCH. Next routine: midday risk check Wed 7/8 (13:xx ET) — re-check
  spreads live + FOMC minutes land at 2pm ET.

## 2026-07-07 16:02 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs live & auto-ratcheting:
  4-sh leg stop_price $565.452 / hwm $628.28; 3-sh leg stop_price $562.833 / hwm ratcheted UP to $625.37
  (from $615.99 — META printed a new intraday high today). Both 10% trail, GTC, status new. Full 7-sh
  position stop-protected.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET, post-16:00 close). No trades today —
  the only order action was the 09:32 FDX starter attempt, CANCELED at the open (paper quote flickered wide
  again) → no new-position slot consumed. META had a strong session: 7 sh @ $578.4486 blended entry, closed
  $614.22, unrealized +$250.40 (+6.18%), day +$97.51 (+2.32% on the position, $600.29 → $614.22).
  **Loss-cut: +6.18% far above the -7% cut → HOLD.** **Ratchet: +6.18% inside the 0–15% band → trail stays 10%,
  no tighten (never loosen).** EOD summary sent via Telegram.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +6.18% green) ✅. +15% ratchet: N/A (+6.18% < +15%) ✅.
  META 4.29% of equity ($4,299.54 / $100,250.38) ≤ 5% size cap ✅. Day P/L equity $100,250.38 vs prior close
  $100,152.87 = +$97.51 (+0.097%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $95.95k intact. Deployment-floor rule still OPEN (FDX/MRK spread-gated on the broken paper
  feed). Week's binary = Wed 7/8 FOMC June minutes. Next routine: pre-market Wed 7/8.

## 2026-07-07 13:05 ET — NO-OP (midday risk check; market OPEN)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs live & auto-ratcheting:
  4-sh leg stop_price $565.452 / hwm $628.28; 3-sh leg stop_price $554.39091 / hwm ratcheted UP to $615.99
  (from $608.88 — META printed a new intraday high today). Both 10% trail, GTC, status new. Full 7-sh
  position stop-protected.
- Reasoning: Properly-timed midday risk check (`is_open: true`, 13:05 ET). Only position is META: 7 sh @
  $578.4486 blended entry, current $607, unrealized +$199.86 (+4.94%), day +$46.97 (+1.12% on position).
  **Loss-cut: +4.94% green → far above the -7% cut line → HOLD, no close.** **Ratchet: +4.94% inside the
  0–15% band → trail stays 10%, no tighten (fires at +15%; never loosen).** No position down -7%; no winner
  ≥+15% to tighten. No new positions this routine (midday is risk-only). FDX/MRK still spread-gated deployables
  for /trade; NVDA gate unconfirmed; MU don't chase. Nothing to do.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +4.94% green) ✅. +15% ratchet: N/A (+4.94% < +15%) ✅.
  META 4.24% of equity ($4,249 / $100,199.84) ≤ 5% size cap ✅. Day P/L equity $100,199.84 vs prior close
  $100,031.14 = +$168.70 (+0.169%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅.
  Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed). Dry powder $95.95k intact. Deployment-floor rule still OPEN (FDX/MRK
  spread-gated). Week's binary = Wed 7/8 FOMC June minutes. Next routine: market-close Tue 7/7.

## 2026-07-07 09:32 ET — ATTEMPTED BUY FDX → CANCELED (paper quote flickered wide again); META HELD (market OPEN)
- Qty / price / stop: FDX market buy for 10 sh submitted with `--trail-percent 10`, but it NEVER FILLED
  (stayed `status: new`, filled_qty 0 for 15s+); canceled by ID via targeted DELETE (HTTP 204) so the script's
  already-exited-without-a-stop order couldn't fill later UNPROTECTED. No FDX position opened, no stop leg created.
  META: no order — HOLD per plan; both trailing legs remain live (qty 4 @ $565.452 / hwm $628.28; qty 3 @ $547.992 /
  hwm $608.88, 10% trail, GTC).
- Reasoning: Executing the 7/7 pre-market plan. (1) META — HOLD, no add: at target weight (~4.23%, +4.70%),
  Strong Buy, no binary until Jul 29 → monitor only. (2) FDX — the deployment-floor NAMED deployable, spread-gated
  after the 7/6 broken quote. At 09:31 the quote briefly printed CLEAN (bid $311.15 / ask $312.63, 0.48% spread) so I
  fired the ~3% starter (10 sh, 10% trail). The market order sat unfilled 15s; I canceled it (targeted DELETE, NOT
  cancel-all — preserved META's stops) to avoid a late unprotected fill, then re-sampled the quote: ask had jumped to
  $327.48 (bid steady $311.14) = 5.25% spread, STUCK there across 4 consecutive polls, only 40 sh offered. That's the
  same pathological flickering paper feed as 7/6 — the tight open print didn't hold. A market fill would land ~$327
  (~5% above bid, near-instant 10%-trail trip risk, ~5% above the plan's ~$312 assumption). SKIPPED — don't chase a
  wide/broken quote; the `buy` script is market-only so there's no limit-order workaround. FDX thesis UNCHANGED; retry
  when the quote normalizes. (3) MRK — the backup deployable — was also spread-gated (bid $122.54 / ask $129.11 =
  5.36%), so no clean fill there either → skip. (4) NVDA — gate unconfirmed, do NOT initiate; MU — don't chase; AVGO/GEHC — WATCH.
- Guardrail check: PASS. FDX starter would have been 10 sh ≈ $3.13k ≈ 3.12% of equity ≤ 5% cap ✅; but it never filled
  so **NO new-position slot consumed — still 0 of 3 this week** ✅. Day P/L equity $100,188.08 vs prior close
  $100,031.14 = +$156.94 (+0.157%) → no daily-loss-cap concern ✅. 10% trail was attached to the (unfilled) order ✅.
  Paper mode ✅. No options/margin/short/crypto ✅. META 4.23% ≤ 5% size cap ✅.
- Note: No Telegram (no trade actually filled/placed; recurring FDX-quote issue is a known, already-logged process note,
  not a new abnormality). Deployment-floor rule STILL OPEN — named deployable FDX blocked twice now by the broken paper
  feed; MRK backup also spread-gated today. Dry powder $95.95k intact. Week's binary = Wed 7/8 FOMC June minutes. Next
  routine: midday risk-check Tue 7/7.

## 2026-07-06 18:08 ET — NO-OP (midday risk check; market CLOSED, ran post-close on frozen prices)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs live & auto-ratcheting:
  4-sh leg stop_price $565.452 / hwm $628.28; 3-sh leg stop_price $543.222 / hwm ratcheted UP to $603.58
  (from $600.50 — META printed a new high today). Both 10% trail, GTC, status new. Full 7-sh position stop-protected.
- Reasoning: Midday risk-check routine fired at 18:08 ET — AFTER the 16:00 close (`is_open: false`), so it ran on
  frozen close prices. NOT the old 8h-early misfire (those fired ~01:xx ET pre-open); the market being closed at
  6pm is expected, not abnormal → no Telegram escalation. Ran the check anyway for discipline. Only position is
  META: 7 sh @ $578.45 blended, current $599.92, unrealized +$150.30 (+3.71%), day +$119.14 (+2.92% on position).
  **Loss-cut: +3.71% green → far above the -7% cut line → HOLD, no close.** **Ratchet: +3.71% inside the 0–15%
  band → trail stays 10%, no tighten (never loosen).** No position down -7%; no winner ≥+15% to tighten. Nothing to do.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +3.71% green) ✅. +15% ratchet: N/A (+3.71% < +15%) ✅.
  META 4.19% of equity ($4,199.44 / $100,150.28) ≤ 5% size cap ✅. Day P/L equity $100,150.28 vs prior close
  $100,031.14 = +$119.14 (+0.119%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing closed). Dry powder $95.95k intact. Deployment-floor rule still OPEN (FDX retries when
  the paper quote normalizes near ~$313). Week's binary = Wed 7/8 FOMC June minutes. Next routine: market-close Tue 7/7.

## 2026-07-06 16:02 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs remain live (4-sh stop_price
  $565.452 / hwm $628.28; 3-sh stop_price $540.45 / hwm $600.50; both 10% trail, GTC). Full 7-sh position stop-protected.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET, post-16:00 close). No trades today — the
  only order action was this morning's FDX starter attempt, which was CANCELED at the open (pathologically wide paper
  quote wouldn't fill) → no new-position slot consumed. META had a strong session: 7 sh @ $578.45 blended entry,
  closed $600.20, unrealized +$152.26 (+3.76%), day +$121.10 (+2.968% on the position). **Loss-cut: +3.76% far above
  the -7% cut → HOLD.** **Ratchet: +3.76% inside the 0–15% band → trail stays 10%, no tighten (never loosen).** EOD
  summary sent via Telegram.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +3.76% green) ✅. +15% ratchet: N/A (+3.76% < +15%) ✅.
  META 4.19% of equity ($4,201.40 / $100,152.24) ≤ 5% size cap ✅. Day P/L equity $100,152.24 vs prior close
  $100,031.14 = +$121.10 (+0.121%) → no daily-loss-cap concern ✅. 0 of 3 weekly new-position slots used ✅. Paper
  mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $95.95k intact. Deployment-floor rule still OPEN (FDX retries when quote normalizes near ~$313).
  Next: pre-market Tue 7/7. Week's binary = Wed 7/8 FOMC June minutes.

## 2026-07-06 09:35 ET — ATTEMPTED BUY FDX → CANCELED (thin paper liquidity); META HELD (market OPEN)
- Qty / price / stop: FDX market buy for 9 sh submitted with `--trail-percent 10`, but it NEVER FILLED
  (stayed `status: new`, filled_qty 0 for >1 min); order canceled by ID (HTTP 204). No FDX position opened,
  no stop leg created. META: no order — HOLD per plan; both trailing legs remain live (qty 4 @ $565.452,
  qty 3 @ $540.45, 10% trail, GTC).
- Reasoning: Executing the 7/6 pre-market plan. (1) META — HOLD, no add: at target weight (~4.1%, +2.6%),
  Strong Buy, no binary until Jul 29 → monitor only. (2) FDX — the deployment-floor NAMED deployable; trigger
  was "initiate on a constructive/non-selloff tape." Tape WAS constructive (Nasdaq +0.8%, S&P +0.5%, Dow +0.2%,
  tech jitters easing) so the trigger fired and I placed the ~3% starter (9 sh) with a 10% trail. BUT the Alpaca
  paper quote was pathologically wide — bid $296.40 / ask $329.70 (~11% spread), only 40 sh offered — and the
  market order would not cross. A fill at the ~$330 ask would sit ~10% below the bid instantly (bad entry that
  could immediately trip the 10% trail), and is well above the ~$313 the plan assumed. Canceled rather than take
  a broken fill. FDX thesis is UNCHANGED and still valid — retry on a future routine when the paper quote
  normalizes (tighter spread near ~$313). Not forcing a bad entry. (3) NVDA/MU/AVGO — no action (gated/WATCH).
- Guardrail check: PASS. FDX starter would have been 9 sh ≈ $2.97k ≈ 2.97% of equity ≤ 5% cap ✅; but it never
  filled so **NO new-position slot consumed — still 0 of 3 this week** ✅. Day P/L +$75 (+0.08%) → no
  daily-loss-cap concern ✅. 10% trail was attached to the (unfilled) order ✅. Paper mode ✅.
  No options/margin/short/crypto ✅. META 4.1% ≤ 5% size cap ✅.
- Note: Reconciled memory with broker at run start — prior routines' META position/history existed on remote
  main but my clone was briefly stale; re-synced. No Telegram (no trade actually filled/placed).
- Qty / price / stop: none — no order placed or closed. Both META trailing legs confirmed live: 4-sh starter
  stop_price $565.452 / hwm $628.28; 3-sh add stop_price $540.45 / hwm $600.50. Both 10% trail, GTC, status new.
  Full 7-sh position stop-protected.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET, post-16:00 close). One trade today:
  the sequenced-to-jobs META ADD (+3 sh @ $599.30, 09:40 ET) executed after June NFP printed soft-not-recessionary
  (57K, UE fell to 4.2%) and META held. META then faded most of the Wed "Meta Compute" pop — closed $582.70,
  -4.93% on the day ($612.91 → $582.70) — but the 7-sh blended position is still GREEN: avg entry $578.45,
  unrealized +$29.76 (+0.735%). **Loss-cut: +0.735% far above the -7% cut → HOLD.** **Ratchet: +0.735% inside
  the 0–15% band → trail stays 10%, no tighten (never loosen).** Markets CLOSED Fri 7/3 (July 4); next session
  Mon 7/6. EOD summary sent via Telegram.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +0.735% green) ✅. +15% ratchet: N/A (+0.735% < +15%) ✅.
  META 4.08% of equity ($4,078.90 / $100,029.75) ≤ 5% size cap ✅. Day P/L equity $100,029.75 vs prior close
  $100,200.39 = -$170.64 (-0.170%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used (the META
  buy was an ADD, consumes no slot) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $95.95k intact. Next: pre-market Mon 7/6.

## 2026-07-02 13:05 ET — NO-OP (midday risk check; market OPEN)
- Qty / price / stop: none — no order placed or closed. Both META trailing legs confirmed live & ratcheting:
  4-sh starter stop_price $565.452 / hwm $628.28; 3-sh add stop_price $540.45 / hwm ratcheted UP to $600.50
  (from $599.80 at entry). Both 10% trail, GTC, status new. Full 7-sh position stop-protected.
- Reasoning: Properly-timed midday risk check (`is_open: true`, 13:05 ET). Only position is META: 7 sh,
  avg entry $578.45, current $584.705, unrealized +$43.80 (+1.08%). META gave back most of the Wed
  "Meta Compute" pop — down -4.6% on the day ($612.91 → $584.705) — but is still GREEN from the blended entry.
  **Loss-cut check: +1.08% from entry → far above the -7% cut line → HOLD, no close.** **Ratchet check:
  gain +1.08% is inside the 0–15% band → leave trail at 10%, NO tighten (fires at +15%; never loosen).**
  No new positions: NVDA still gated (B200 lease forward-guide down to $2.50–3.00 by Q4; Wed semi selloff),
  MU breaking down (don't chase), AVGO/FDX low priority. Markets CLOSED Fri 7/3 (July 4).
- Guardrail check: PASS (no trade). -7% cut: N/A (position +1.08% green) ✅. +15% ratchet: N/A (+1.08% < +15%) ✅.
  META 4.09% of equity ($4,092.94 / $100,042.91) ≤ 5% size cap ✅. Day P/L equity $100,042.91 vs prior close
  $100,200.39 = -$157.48 (-0.157%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used ✅.
  Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $95.95k intact. Next: market-close wrap Thu 7/2.

## 2026-07-02 09:40 ET — BUY META (add to starter; sequenced-to-jobs plan EXECUTED)
- Qty / price / stop: +3 sh @ $599.30 fill; fresh 10% trailing stop live (GTC, stop_price $539.82,
  hwm $599.80, status new, qty 3). Original 4-sh starter stop also live (trail 10%, stop_price
  $565.45, hwm $628.28). Full 7-sh position now stop-protected.
- Reasoning: Executed the standing sequenced-to-Thursday META add (planned 6/30, deferred 6/30 & 7/1
  to await today's jobs binary). BOTH gates cleared post-8:30 print: (1) June NFP = **57K vs ~110-115K
  consensus, unemployment FELL to 4.2%** = soft-but-NOT-recessionary → closes the Warsh rate-hike door,
  fuels rate-cut hopes (2yr yield fell); broad tape green (Dow +0.5%, S&P +0.4%, Nasdaq +0.2%). (2) META
  -2.1% on the day (~$600 vs $612.91 close) = normal consolidation after the +8.8% Wed pop on the "Meta
  Compute" cloud-infra catalyst, NOT a hard reversal; no company-specific bad news, still green from entry.
  Catalyst (capex-monetization bear case answered) intact. Kept size to 3 sh (~$1.8k) — don't chase after
  a +8.8% pop. Lifted META 2.40% → 4.19% of equity toward the intended ~4% core weight.
- META position after add: 7 sh, avg entry $578.45, current ~$599.85, unrealized +$149.78 (+3.70%),
  4.19% of equity ($4,198.92 / $100,149.73). Gain +3.70% is inside the 0–15% band → trail stays 10%,
  no ratchet; far above the -7% cut line.
- Guardrail check: PASS. Size 4.19% ≤ 5% cap. Day P/L equity $100,149.73 vs prior close $100,200.39 =
  -0.051% → no daily-loss-cap concern. ADD to existing position consumes NO new-position slot (0 of 3
  used this week). 10% trailing stop attached at entry. TRADING_MODE = paper. No options/margin/short/crypto.
  Cash $95,950.85 (dry powder still ~$96k). Telegram sent (trade placed).

## 2026-07-01 16:02 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. META 10% trailing stop confirmed live: stop_price $565.452, hwm $628.28, trail 10%, GTC, status new.
- Reasoning: properly-timed market-close run (`is_open: false`, 16:02 ET, post-16:00 close). No trades today — the standing 07-01 plan deliberately sequenced the META ADD to Thu 7/2 POST-jobs; held at the open (09:32) and through the midday check (13:05). META had a strong session: 4 sh @ $562.81 entry, closed $611.72, unrealized +$195.64 (+8.69%), day +$193.72 (+8.60% on the position). Faded off the midday $618.69 / intraday high $628.28 but still finished deep green. **Loss-cut: +8.69% → far above the -7% cut line → held.** **Ratchet: gain +8.69% in the 0–15% band → trail left at 10%, no tighten (fires at +15%; never loosen).** Touched ~+11.6% at the $628 intraday high but closed +8.69% — no ratchet trigger. Add still sequenced to Thu 7/2 post-jobs (not chasing this run into the binary). NVDA gated on lease-recovery confirmation + jobs; MU/AVGO/FDX WATCH only. EOD summary sent via Telegram.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +8.69% green) ✅. +15% ratchet: N/A (+8.69% < +15% at close) ✅. META 2.44% of equity ($2,446.88 / $100,195.63) ≤ 5% size cap ✅. Day P/L +$193.72 (+0.194%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: Dry powder $97.7k intact. Next: pre-market Thu 7/2 → the June-NFP print (the META-add gate; markets CLOSED Fri 7/3).

## 2026-07-01 13:05 ET — NO-OP (midday risk check; market OPEN)
- Qty / price / stop: none — no order placed or closed. META 10% trailing stop confirmed live & ratcheting: stop_price $565.452, hwm ratcheted UP to $628.28 (from $607.91 at open), trail 10%, GTC, status new.
- Reasoning: Properly-timed midday risk check (`is_open: true`, 13:05 ET). Only position is META: 4 sh @ $562.81 entry, current $618.69, unrealized +$223.52 (+9.93%), day +$221.60 (+9.84%). META kept ripping since the 09:32 open ($597.05 → $618.69, intraday high $628.28) on the constructive-into-jobs tape. **Loss-cut check: +9.93% from entry, deep in the green, far above the -7% cut line → HOLD.** **Ratchet check: gain +9.93% is in the 0–15% band → leave trail at 10%, NO tighten (ratchet only fires at +15%; never loosen).** Approaching the +15% trigger — flag to tighten to 7% next check if it holds/rises. Existing META add still sequenced to Thu 7/2 post-jobs per standing plan (not chasing this spike into the binary). NVDA gated on B200 lease confirmation + jobs; MU/AVGO/FDX WATCH only.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +9.93% green) ✅. +15% ratchet: N/A (+9.93% < +15%) ✅. META 2.47% of equity ($2,474.76 / $100,223.49) ≤ 5% size cap ✅. Day P/L +$221.58 (+0.222%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $97.7k intact. Next: market-close wrap Wed 7/1, then the key Thu 7/2 June-NFP print (the META-add gate; markets CLOSED Fri 7/3).

## 2026-07-01 09:32 ET — NO-OP (market-open, market OPEN)
- Qty / price / stop: none — no order placed. META 10% trailing stop confirmed live & ratcheting: stop_price $547.119, hwm $607.91 (up from $570.90), GTC, status new.
- Reasoning: Executed the standing 07-01 pre-market plan, which deliberately sequenced the META ADD to **Thursday 7/2 POST-jobs**, not today. No misfired open plan to catch up on (META starter already opened last week w/ its stop; the add is a future, gated action). META RIPPED today: 4 sh @ $562.81 entry, current $597.05, unrealized +$136.96 (+6.08%), day +5.99% (hit $607.91 intraday) — vs the RED futures the pre-market read. The move does NOT trigger the add: adding now would chase a +6–8% intraday spike into the Thu June-NFP binary (markets CLOSED Fri 7/3) at a much worse entry (~$597 vs the ~$565 the plan assumed for a ~$1.7k/3-sh add), same binary risk. The existing 4-sh starter already captures today's upside. Disciplined sequencing holds: add Thu post-jobs IF jobs in-line/soft-not-recessionary AND META holds. NVDA gate thawing (B200 lease median recovered to $6.11) but do NOT initiate pre-jobs. MU/AVGO/FDX WATCH only.
- Guardrail check: PASS (no trade). -7% cut: N/A (position +6.08% green) ✅. +15% ratchet: N/A (+6.08% < +15%; also a midday-only check) ✅. META 2.39% of equity ($2,388.20 / $100,138.55) ≤ 5% size cap ✅. Day P/L +$136.64 (+0.137%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used (an ADD would consume none anyway) ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $97.7k intact. Next: midday risk check Wed 7/1, then the key Thu 7/2 jobs print (the META-add gate).

## 2026-06-30 16:04 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. META 10% trailing stop confirmed live (stop_price $513.81, hwm $570.90, GTC, status new).
- Reasoning: properly-timed market-close run (`is_open: false`, 16:04 ET, post-16:00 close). No trades today — the standing 06-30 plan held the contingent META add at the open (soft tape + pre-JOLTS) and held it through the midday risk check. META finished marginally GREEN: 4 sh @ $562.81 entry, current $563.29, unrealized +$1.92 (+0.085%), day +0.123% — drifted back into the black from the midday -0.68%. Inside the -7% cut line → held; gain below +15% so ratchet N/A. Posture CONSTRUCTIVE (rout bottomed), deploy-gated only on Thu 7/2 jobs (NFP a day early; markets CLOSED Fri 7/3). EOD summary sent via Telegram.
- Guardrail check: PASS. -7% cut: N/A (position green) ✅. +15% ratchet: N/A (+0.085% < +15%) ✅. META 2.25% of equity ($2,253.16 / $100,001.91) ≤ 5% size cap ✅. Day P/L +$2.76 (+0.003%) → no daily-loss-cap concern ✅. 0/3 weekly new-position slots used ✅. Paper mode ✅. No options/margin/short/crypto ✅.

## 2026-06-30 13:03 ET — NO-OP (midday risk check; market OPEN)
- Qty / price / stop: none — no order placed or closed. META 10% trailing stop remains live (stop_price ~$513.81, hwm $570.90, GTC).
- Reasoning: Properly-timed midday risk check (`is_open: true`, 13:03 ET). Only position is META: 4 sh @ $562.81 entry, current $558.965, unrealized -$15.38 (-0.68%), day -$14.56 (-0.015%). **Loss-cut check: -0.68% from entry, far inside the -7% cut line → HOLD, no close.** Position is a slight loser vs entry, so the stop-tightening ratchet (only fires on positive gains ≥+15%) does NOT apply — and you never loosen. 10% trailing stop verified live, current ~$559 nowhere near the ~$513.81 stop. No new positions: contingent META add still HELD pending Thu 7/2 jobs (per the standing plan); NVDA gated on B200 lease stabilization (unmet), MU don't chase, AVGO/FDX low priority.
- Guardrail check: PASS. -7% loss cut: N/A (-0.68% > -7%) ✅. +15% ratchet: N/A (position red) ✅. META 2.24% of equity ($2,235.86 / $99,984.59) ≤ 5% size cap ✅. Day P/L -$14.56 (-0.015%) → no daily-loss-cap breach ✅. 0/3 weekly new-position slots used ✅. Paper mode ✅. No options/margin/short/crypto ✅.
- Note: No Telegram (nothing placed/closed). Dry powder $97.7k intact. Next: market-close wrap Tue 6/30.

## 2026-06-30 09:32 ET — NO-OP (market-open, contingent META add HELD; market OPEN)
- Qty / price / stop: none — no order placed. Existing META 10% trailing stop remains live (stop_price ~$513.81, hwm $570.90, GTC).
- Reasoning: Properly-timed market-open run (`is_open: true`, 09:32 ET). Standing 06-30 pre-market plan's primary idea was to ADD ~3 sh META — but it was EXPLICITLY conditioned on "tape holds green / not selling off AND JOLTS (10:00 ET) isn't a shock; do not add into weakness." Both gates FAIL at the open: (1) META reversed from +0.17% pre-mkt ($563.75) to **-1.10% on the day ($556.43)** — selling off, not green; (2) JOLTS hasn't printed yet (10:00 ET). Per the plan's own stated alternative, HOLD the add and revisit Thu 7/2 AFTER the jobs print, which fully closes the third gate. Falling-knife/"don't add into weakness" discipline applies. No NEW positions (NVDA gated on B200 lease stabilization — still unmet; MU don't chase; AVGO/FDX low priority). Existing 4-sh META starter held: -1.13% from entry, well inside the -7% cut line; gain negative so ratchet N/A. Dry powder $97.7k intact.
- Guardrail check: PASS. META 2.23% of equity ($2,225.71 / $99,974.46) ≤ 5% cap ✅; 0/3 weekly new-position slots used ✅; day P/L -$24.69 (-0.025%) → no daily-loss-cap breach ✅; paper mode ✅. (A guardrail did not block the add — the add's own pre-conditions weren't met.)

## 2026-06-29 16:04 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. META trailing stop confirmed live (10% trail,
  stop_price $513.81, hwm $570.90, GTC, status new).
- Reasoning: properly-timed market-close run (`is_open: false`, 16:04 ET, post-16:00 close). No trades
  today — the standing 06-29 pre-market plan was an explicit HOLD / no new positions, executed as such at
  open (09:32) and held through the midday risk check (13:03). META drifted from the midday $564.70 to a
  $562.00 close (-0.14% from entry) but still finished UP +2.14% on the day vs $550.25 prior close — the
  rout-moderating bounce held. Well inside the -7% cut line → held; gain below +15% → ratchet N/A. Defensive
  posture holds: no confirmed bottom yet + the Thu 7/2 jobs binary is still ahead. Dry powder $97.7k intact.
  EOD summary sent via Telegram.
- Guardrail check: PASS. META 2.25% of equity ($2,248 / $99,996.75) ≤ 5% ✅; 0/3 weekly new-position slots
  used ✅; day P/L +$47.00 (+0.047%) → no daily-loss-cap breach ✅; paper mode ✅.

## 2026-06-26 16:05 ET — NO-OP (market-close wrap; market CLOSED)
- Qty / price / stop: none — no order placed or closed. META trailing stop confirmed live (10% trail,
  stop_price $511.227, hwm $568.03, GTC).
- Reasoning: properly-timed market-close run (`is_open: false`, 16:05 ET, post-16:00 close). No trades
  today — the only decision was the 09:32 deliberate HOLD of the contingent META add (held on hot May PCE
  + re-intensifying AI-cost/bubble rout, 4th straight down day). META faded from its midday bounce but
  still closed UP +1.11% on the day at $548.89, -2.47% from entry — well inside the -7% cut line → held.
  Loser vs entry, so the stop-tightening ratchet (only fires on +15%+ gains) does not apply. Defensive
  posture holds; rout not yet confirmed bottomed. EOD summary sent via Telegram.
- Guardrail check: PASS. META 2.20% of equity ≤ 5% ✅; 1/3 weekly slots used ✅; day P/L +$24.08
  (+0.024%) → no daily-loss-cap breach ✅; paper mode ✅.

## 2026-06-26 09:32 ET — NO-OP (market-open, deliberate HOLD, market OPEN)
- Qty / price / stop: none — no order placed.
- Reasoning: Executed the 06-26 pre-market standing plan = DEFENSIVE HOLD, no new positions.
  Not a misfire salvage: META starter already executed 06-24, and the contingent META add was
  intentionally HELD on two grounds (hot May PCE +3.4% core y/y on 06-25 + a re-intensifying
  AI-cost/bubble rout on 06-26 — OpenAI IPO-delay report, device-maker margin fears, NVDA B200
  lease price -31% in 3 wks). 4th straight down day; do not catch the falling knife. NVDA/MU/AVGO/
  FDX all WATCH-only, lower conviction than yesterday. Dry powder ($97.7k) is the position.
- Guardrail check: PASS. META 2.17% of equity ≤ 5% size cap ✅. 1 of 3 weekly new-position slots
  used (META 06-24), 2 open ✅. Day P/L +$1.32 (+0.001%) flat → no daily-loss-cap breach ✅.
  META -3.48% from entry > -7% cut line → hold; loser so stop-tightening ratchet N/A. Trailing stop
  live (10% trail, stop_price $511.227, hwm $568.03, GTC). Paper mode confirmed ✅.
- Note: No Telegram (no trade placed/closed). Next: midday risk check, then weekly review at Fri close.

## 2026-06-25 16:04 ET — NO-OP (market-close wrap; market closed)
- Qty / price / stop: none — no order placed or closed. META trailing stop confirmed live (10% trail,
  stop_price $511.227, hwm $568.03, GTC, status new).
- Reasoning: properly-timed market-close run (`is_open: false`, 16:04 ET, post-16:00 close). No trades
  today — the only decision was the 09:32 SKIP of the contingent META add (May core PCE hot, +3.4% y/y).
  META closed at $544.99, -3.17% from entry, well inside the -7% cut line → held. Loser, so the
  stop-tightening ratchet doesn't apply. EOD summary sent via Telegram.
- Guardrail check: PASS. META 2.18% of equity ≤ 5% ✅; 1/3 weekly slots used ✅; day P/L -$50.72
  (-0.051%) → no daily loss cap breach ✅; paper mode ✅.

## 2026-06-25 09:32 ET — SKIP META add (PCE hot surprise)
- Qty / price / stop: none — no order placed. META starter unchanged (4 sh @ $562.81, 10% trailing
  stop live: stop_price $511.227, hwm $568.03, GTC).
- Reasoning: Market confirmed open (`is_open: true`, 09:31 ET — real scheduled open routine).
  Standing-plan catch-up: nothing pending — the half-size META starter was already filled 06-24, so
  no misfired plan to salvage. The only candidate this routine was the PCE-CONTINGENT META add from
  the 07:00 pre-market plan. Add condition was: core ≤ ~+0.37% m/m / 3.3% y/y → add; core hot → HOLD.
  **May PCE (8:30 ET actual): core +0.3% m/m but +3.4% y/y vs +3.3% forecast (HOT, highest since
  Oct 2023); headline +0.4% m/m / +4.1% y/y (highest since Apr 2023), Iran-war oil reigniting
  inflation, rate-hike door stays open.** Core y/y surprised hot → per the documented rule, HOLD the
  add; don't add high-multiple tech into a hot inflation print. META already -1% on the day confirms
  the pressure. Keep dry powder. MU/NVDA/AVGO/FDX = WATCH only (no new catalyst; don't initiate into
  a hot-PCE tape).
- Guardrail check: n/a (no trade placed). For reference: META 2.21% of equity ≤ 5% ✅; 1/3 weekly
  new-position slots used ✅; day P/L -$22.12 (-0.022%), no daily loss cap breach ✅; paper mode ✅.

## 2026-06-24 13:03 ET — NO-OP (midday risk check; market open, no action triggered)
- Qty / price / stop: none — no order placed. Existing META trailing stop confirmed live (10% trail,
  hwm risen to $568.03, stop_price $511.23).
- Reasoning: properly-timed midday risk check (`is_open: true`, 13:03 ET). Only position is META:
  4 sh @ $562.81 entry, current $559.69, unrealized -$12.48 (-0.55%). Well within the -7% cut line —
  no loss to cut. Not a meaningful winner (slightly red on the day), so no manual stop tightening
  warranted; the 10% trailing stop is already auto-tracking the high-water mark up (hwm $568.03).
  No add to META (still day-3 of the AI/tech rout, MU binary tonight — waiting for confirmation per
  plan). No new position.
- Guardrail check: META 2.24% of equity ≤ 5% ✅; 1/3 weekly slots used; day P/L -$12.48 (-0.012%,
  flat) — no daily loss cap breach; paper mode confirmed. No close needed → no Telegram sent.

## 2026-06-24 10:38 ET — NO-OP (market-open re-fire; standing plan already deployed)
- Qty / price / stop: none — no order placed.
- Reasoning: market confirmed open (`is_open: true`). Cross-checked positions/trade-log: the only
  execution item in the 07:00 ET pre-market plan — the half-size META starter — was already filled
  earlier today (4 sh @ $562.81) and its 10% trailing stop is live (stop_price $508.05, hwm $564.50).
  Nothing pending/misfired to salvage. Re-evaluated remaining ideas: META add → plan says "add after
  confirmation"; it's day 3 of the AI/tech rout, META ~flat on the day, MU binary tonight → no
  confirmation, hold dry powder. MU → bars buying into tonight's print. FDX/NVDA/AVGO → watch-only,
  no new catalyst. No trade clears for execution.
- Guardrail check: n/a — no trade attempted. (For reference: META 2.25% ≤ 5% ✅, 1/3 weekly slots
  used, day P/L -$5.88 flat — no daily loss cap breach, paper mode confirmed.)

## 2026-06-24 09:55 ET — BUY META
- Qty / price / stop: 4 shares @ avg $562.81 fill ($2,251.24 cost basis, 2.25% of $100k equity). 10%
  trailing stop attached separately (see note below), stop_price $506.43, hwm $562.70.
- Reasoning: executed the standing half-size META starter from the 07:00 ET pre-market plan
  (macro-driven 3-day AI/tech rout dip, no company-specific bad news, no near-term earnings binary
  until Jul 29, avg PT $827 / Strong Buy consensus). Market confirmed open (`is_open: true`) — this
  was the actual scheduled market-open routine, not a misfire.
- Guardrail check: position size 2.25% ≤ 5% max ✅. 1st new position this week, ≤3/week cap ✅. Day
  P/L $0 before trade, no daily loss cap breach ✅. Equity (paper) confirmed via `account` ✅. No
  options/margin/short/crypto used ✅. `TRADING_MODE: paper` confirmed in strategy.md ✅.
- Note (script bug, not a guardrail issue): `alpaca.py buy META 4 --trail-percent 10` returned a 403
  on the trailing-stop leg ("cannot open a short sell while a long buy order is open") — the script
  fires the stop-sell immediately after the market buy without waiting for the fill, so Alpaca sees
  it as a naked short for an instant. The market buy itself filled fine. Worked around it by
  re-submitting just the trailing_stop sell order (same payload the script would have sent) once the
  buy showed `status: filled`. Stop is now live and attached. **Flagging for a script fix:** `cmd_buy`
  in `scripts/alpaca.py` should poll/wait for the buy order to fill (or at least retry once) before
  submitting the trailing-stop leg.

## 2026-06-24 01:29 — NO-OP (market-close wrap, no positions)
- Qty / price / stop: none — no order placed.
- Reasoning: "market-close" routine fired at 01:29 ET (~8h before the 09:30 open; clock `is_open: false`).
  Account still fully in cash: $100k equity, $0 positions, $0 day P/L. No trades were placed today because
  every routine fired pre-open. Nothing to wrap — logged the day, refreshed portfolio snapshot, sent EOD
  Telegram summary. META starter plan carries forward to the next real open.
- Guardrail check: n/a — no trade attempted.
- Note: routine timing offset is now a logged recurring issue (see signals-learnings.md → Process notes).

## 2026-06-24 01:26 — NO-OP (midday risk check, no positions)
- Qty / price / stop: none — no order placed.
- Reasoning: "midday" risk-check routine fired at 01:26 ET (~8h before the 09:30 open; clock `is_open: false`).
  `alpaca.py positions` returned `[]` — account still fully in cash ($100k equity, $0 positions). Nothing to
  risk-check: no position down -7% to cut, no winner to tighten a stop on. Pre-market META starter was never
  executed (market-open routine also fired pre-open). Plan unchanged: initiate META ~5% starter w/ 10% trailing
  stop at the real open; hold off MU/FDX; cautious into Thu Jun 26 PCE.
- Guardrail check: n/a — no trade attempted.
- Note: routines still firing ~8h early (timezone/cron offset). Recurring issue — flag for fix.

## 2026-06-24 01:11 — SKIP (market closed)
- Qty / price / stop: none — no order placed.
- Reasoning: "market-open" routine fired at 01:11 ET, ~8h before the 09:30 ET open. `alpaca.py clock`
  returned `is_open: false`. Cannot execute the pre-market plan (META ~5% starter) while the market
  is closed. Plan stands for the actual open: initiate META starter w/ 10% trailing stop, hold off MU
  (earnings tonight) + FDX (let dip settle), stay cautious into Thu Jun 26 PCE.
- Guardrail check: n/a — no trade attempted.
- Note: routine scheduled at wrong time (timezone/cron likely off). Account unchanged: $100k cash, flat.

## 2026-06-25 13:03 — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed.
- Reasoning: Only position is META (4 sh, entry $562.81, current $545.14, unrealized -$70.68 / -3.14%).
  Well inside the -7% loss-cut line, so no close required. META is a loser, not a winner, so the
  stop-tightening ratchet does not apply (only fires on positions with a positive gain from entry).
  Trailing stop verified live: 10% trail, stop_price $511.227, hwm $568.03, GTC, status new.
- Guardrail check: PASS. -3.14% > -7% cut line → hold. No winner ≥+15% gain → no tighten. Day P/L
  -$50.12 (-0.05%) → no daily-loss-cap concern. META 2.18% of equity ≤ 5% size cap.
- Note: No Telegram (nothing closed). Holding dry powder; MU/NVDA/AVGO/FDX = WATCH only. 1 of 3
  weekly new-position slots used.

## 2026-06-26 12:xx — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed.
- Reasoning: Only position is META (4 sh, entry $562.81, current $554.02, unrealized -$35.16 / -1.56%).
  META has RECOVERED off the open: was -3.48% at 09:32, now -1.56% from entry and +2.05% on the day
  (+$44.60 intraday). Comfortably inside the -7% loss-cut line → no close required. META is still a
  loser vs entry (negative gain), so the stop-tightening ratchet does not apply (it only fires on a
  positive gain ≥+15%). 10% trailing stop remains live (stop_price $511.227, hwm $568.03) — current
  ~$554 nowhere near it.
- Guardrail check: PASS. -1.56% > -7% cut line → hold. No winner ≥+15% gain → no tighten. Day P/L
  +$44.60 (+0.045%) → no daily-loss-cap concern. META 2.22% of equity ($2,216 / $99,965) ≤ 5% size cap.
- Note: No Telegram (nothing closed). Defensive posture holds into the AI-cost/bubble rout; the intraday
  bounce is not yet a confirmed bottom. NVDA/MU/AVGO/FDX = WATCH only. 1 of 3 weekly new-position slots used.

## 2026-06-29 09:32 — NO-OP (market-open, market OPEN)
- Qty / price / stop: none — no order placed.
- Reasoning: Executed the standing pre-market plan (06-29 07:10), which was an explicit HOLD / no new
  positions. Nothing guardrail-clean was pending — the META starter was already opened last week with its
  10% trailing stop attached, so there was no missed-open plan to catch up on. No new buys today per the
  falling-knife rule: no confirmed bottom (Fri treaded water, no clear up day) AND the week's binary (June
  jobs report Thu 7/2, consensus +172k) is still ahead. Initiating before jobs clears + a bottom confirms
  is premature. NVDA still gated on B200 lease stabilization; MU don't chase; AVGO/FDX low priority.
- META: 4 sh, entry $562.81, current $564.705, unrealized +$7.58 (+0.34%) — crossed into the green off the
  open (+2.63% on the day). 10% trailing stop verified live (stop_price $511.227, hwm $568.03, GTC, new) —
  nowhere near it. Loser→winner flip is marginal (+0.34%), below the +15% ratchet trigger, so no stop tighten.
- Guardrail check: PASS (no trade). META 2.26% of equity ($2,258.82 / $100,007.57) ≤ 5% size cap. Day P/L
  +$57.82 (+0.058%) → no daily-loss-cap concern. 0 of 3 weekly new-position slots used this week (META was
  last week). TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed). Dry powder $97.7k intact. Holiday-shortened week: Warsh Wed 7/1,
  jobs Thu 7/2, markets CLOSED Fri 7/3. Deploy a slot once jobs clears AND a bottom confirms.

## 2026-06-29 13:03 — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed.
- Reasoning: Only position is META (4 sh, entry $562.81, current $564.70, unrealized +$7.56 / +0.336%,
  day +$57.80 / +2.626%). Small WINNER vs entry — comfortably above the -7% loss-cut line, so no close
  required. Gain is only +0.34%, far below the +15% stop-tightening ratchet trigger, so no tighten (and
  you never loosen). 10% trailing stop verified live: stop_price $513.81, hwm ratcheted UP to $570.90
  (was $568.03) as the rally pulled the high-water-mark higher, GTC, status new — current ~$564.70 nowhere
  near the stop.
- Guardrail check: PASS (no trade). -7% cut: N/A (position is green). +15% ratchet: N/A (+0.34% < +15%).
  META 2.26% of equity ($2,259.56 / $100,008.31) ≤ 5% size cap. Day P/L +$58.56 (+0.0586%) → no
  daily-loss-cap concern. 0 of 3 weekly new-position slots used. TRADING_MODE = paper.
- Note: No Telegram (nothing placed/closed). Dry powder $97.7k intact. Posture DEFENSIVE-but-THAWING into
  the holiday-shortened week (Warsh Wed 7/1, June jobs Thu 7/2 consensus +172k, markets CLOSED Fri 7/3).
  No new buys until jobs clears AND a bottom confirms. NVDA/MU/AVGO/FDX = WATCH only.

## 2026-07-03 09:30 — NO-OP (market-open, market CLOSED — July 4th holiday)
- Qty / price / stop: none — no order placed. Market CLOSED (clock: is_open=false, next_open Mon 2026-07-06 09:30 ET).
- Reasoning: Routine fired at 09:30:46 ET — the CORRECT market-open time — but NYSE/Nasdaq are closed for the
  July 4th holiday (observed Fri 7/3 since the 4th is Sat). This is NOT the old "8h-early misfire" (those fired
  ~01:xx ET); the cron is working, the market is simply closed for a federal holiday the pre-market routine
  already flagged. So no Telegram misfire escalation is warranted — nothing is broken. The standing plan
  (pre-market 07-03) was explicit HOLD / no trades, and even for Mon 7/6 the plan is HOLD META, no add, no new
  positions. Nothing guardrail-clean was pending to catch up on.
- META: 7 sh, entry $578.45 blended, frozen at Thu 7/2 close $582.90, unrealized +$31.16 (+0.77%), 4.08% of
  equity = at target weight. Both trailing legs live (4-sh stop $565.452 / hwm $628.28; 3-sh stop $540.45 /
  hwm $600.50). Add is COMPLETE — HOLD, no further add. Prices frozen; no ratchet/cut evaluation on a closed market.
- Guardrail check: PASS (no trade). META 4.08% ≤ 5% size cap. Day P/L $0.00 (market closed). 0 of 3 weekly
  new-position slots used (new week resets Mon 7/6). TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed; holiday closure is expected, not abnormal). Dry powder ~$96k intact.
  NVDA gate doubly-unconfirmed (lease forward-guide down + WSJ OpenAI-demand-miss chip rout) → do NOT initiate.
  MU breaking down, don't chase. AVGO/FDX low priority. Next session Mon 7/6; week's binary = Wed 7/8 FOMC June
  minutes. Next routine: pre-market Mon 7/6.

## 2026-07-03 13:05 — NO-OP (midday risk check, market CLOSED — July 4th holiday)
- Qty / price / stop: none — no order placed. Market CLOSED (clock: is_open=false, timestamp 13:05 ET, next_open Mon 2026-07-06 09:30 ET).
- Reasoning: Routine fired at 13:05 ET — the CORRECT midday time — but NYSE/Nasdaq are closed for the July 4th
  holiday (observed Fri 7/3). Cron is working; the market is simply closed. Prices frozen at Thu 7/2 close, so
  no live risk evaluation is possible — but ran the check anyway for discipline.
- META: 7 sh, entry $578.45 blended, frozen at $582.90, unrealized +$31.16 (+0.77%), 4.08% of equity = target
  weight. -7% loss-cut: N/A — position is GREEN (+0.77%), nowhere near the cut line, HOLD. +15% ratchet: N/A
  (+0.77% << +15%), no tighten (and never loosen). Both trailing legs remain live (4-sh stop $565.452 / hwm
  $628.28; 3-sh stop $540.45 / hwm $600.50). Add is COMPLETE — HOLD, no further add.
- Guardrail check: PASS (no trade). META 4.08% ($4,080.30 / $100,031.14) ≤ 5% size cap. Day P/L $0.00 (market
  closed) → no daily-loss-cap concern. 0 of 3 weekly new-position slots used (new week resets Mon 7/6).
  TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed; holiday closure is expected, not abnormal). Dry powder ~$96k intact.
  NVDA gate doubly-unconfirmed → do NOT initiate. MU breaking down, don't chase. AVGO/FDX low priority. Next
  session Mon 7/6; week's binary = Wed 7/8 FOMC June minutes. Next routine: pre-market Mon 7/6.

## 2026-07-09 13:xx — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- META: 7 sh, entry $578.4486 blended, current $612.78, unrealized +$240.32 (+5.94%), day +1.60%. Ran up
  hard from the morning read ($581 → $612.78, ~+5.4% intraday). -7% cut: N/A (big WINNER). +15% ratchet: N/A
  (+5.94% < +15%) → leave trail at 10%, do NOT tighten (never loosen). Both trailing legs live: 4-sh
  stop $565.452 / hwm $628.28; 3-sh stop $562.833 / hwm $625.37. Price pulled back off the $628 hwm but
  stops nowhere near hit. Weight 4.28% ($4,289.46 / $100,223.28) ≤ 5% cap. HOLD — add complete.
- MRK: 23 sh, entry $125.90, current $125.085, unrealized -$18.75 (-0.65%), day -0.72%. -7% cut: N/A
  (only -0.65%, far from the -7.0% line = ~$117.09). No thesis change needed. Trailing stop live:
  stop_price $115.263, hwm $128.07, trail 10%, GTC, order 3d2f860f — protecting cleanly. HOLD per stop rules.
- Guardrail check: PASS (no trade). No position ≤ -7% → no forced close. No position ≥ +15% → no ratchet.
  Day P/L +$50.60 (+0.05%) → nowhere near the -3% daily cap. Weekly slots 1 of 3 used (MRK). Both names
  ≤ 5% size cap. TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed). Book ~93% cash (~$93.1k dry powder). META's run-up is the
  standout — watch for the +15% ratchet on future runs; still +5.94%, no action yet. MRK holding as the
  defensive/oil-insensitive starter. NVDA gate unconfirmed; FDX spread-gated; MU/AVGO/GEHC WATCH.
  Next routine: market-close Thu 7/9.

## 2026-07-13 13:xx — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- META: 7 sh, entry $578.4486 blended, current $659.29, unrealized +$565.89 (+13.98%), intraday -1.48%.
  -7% cut: N/A (big WINNER). +15% ratchet: +13.98% sits in the 0-15% band → nominal band is 10%, but the
  stop was already tightened to **7% on 7/10** at the +17% high, and the rule is NEVER LOOSEN → stop STAYS 7%.
  No action. Both trailing legs live at 7% (4-sh & 3-sh, stop $630.3912 / hwm $677.84). Weight 4.59%
  ($4,615.03 / $100,511.48) ≤ 5% cap. HOLD — add complete.
- MRK: 23 sh, entry $125.90, current $123.56, unrealized -$53.82 (-1.86%), intraday +0.02%. -7% cut: N/A
  (only -1.86%, far from the -7.0% line = ~$117.09). Trailing stop live: 10%, stop $115.263 / hwm $128.07,
  GTC, order 3d2f860f — protecting cleanly. Weight 2.83% ≤ 5% cap. HOLD per stop rules, doing its defensive job.
- Guardrail check: PASS (no trade). No position ≤ -7% → no forced close. No position ≥ +15% → no ratchet
  (META already at 7%, can't loosen; MRK red). Day P/L -$69.54 (-0.07%) → nowhere near -3% daily cap.
  Weekly slots 1 of 3 used (MRK). Both names ≤ 5% size cap. TRADING_MODE = paper. No options/margin/short/crypto.
- Regime: still day-2 of the Iran/oil watch; the BIG binary = June CPI Tue 7/14 8:30 ET + big-bank earnings
  pre-open. Deployment stays gated pre-CPI. NVDA lease gate firming (re-check post-CPI); FDX spread-gated.
- Note: No Telegram (nothing placed/closed). Book ~92.6% cash (~$93.1k dry powder). Next routine: market-close 7/13.

## 2026-07-13 ~16:xx ET — NO-OP / API OUTAGE (market-close routine)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- **Alpaca API 401 unauthorized** on `account` and `positions`; confirmed via raw curl with the env key/secret →
  credential rotated/revoked/invalid (NOT a script/base-URL bug; all env vars present, base URL correct). Could
  NOT pull a live EOD snapshot — portfolio.md carries forward the midday numbers, STALE-stamped.
- Last-known state (midday 7/13): equity $100,511.48 (+0.51% vs $100k start), day -$69.54 (-0.07%); META 7sh
  +13.98% (7% trail), MRK 23sh -1.86% (10% trail); ~92.6% cash. No trades today.
- Guardrail check: N/A — no trade possible (API down). Weekly slots 1 of 3 used (MRK). TRADING_MODE = paper.
- Telegram EOD summary sent (msg 168) flagging the outage + the fix (refresh ALPACA_API_KEY_ID/SECRET in cloud env).
- Next routine: pre-market Tue 7/14 (June CPI 8:30 ET + big-bank earnings) — but the human must rotate the Alpaca
  key first, else the session stays blind.

## 2026-07-14 ~09:35 ET — NO-OP (market-open routine, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- Executed the pre-market plan: it had ONE conditional deployable (NVDA), gated on the oil/Iran shock
  stabilizing. **Live read confirms the gate FAILS:** Brent **+4.3% to ~$86.85** (fresh 1-month high),
  day-3 of US strikes on Iran, IRGC attacked 2 Hormuz tankers, US Navy blockade reimposing 4pm ET + 20%
  Hormuz cargo fees. That is the OPPOSITE of "≥1 up day OR oil reversing" → falling-knife still binds on
  the geopolitical driver. Tape risk-off (S&P -0.2%, Dow -0.6%, Nasdaq +0.38%; Mon Nasdaq -1.55%; banks
  beating but sold — JPM -2.5%, WFC -2%). **NVDA NOT initiated.** June CPI printed benign (gate a still MET)
  but gate b (oil) is worse, not better → deployment stays gated. Deployment-floor: LOGGED deliberate
  decision to stay ~92.6% cash is correct today.
- META: 7 sh, entry $578.4486 blended, current $652.05, unrealized +$515.21 (+12.72%), intraday -0.71%.
  HOLD — no add (at target weight 4.54%, add complete). Stop at 7% trail (tightened 7/10 at the +17% high,
  stop $630.3912 / hwm $677.84) — NEVER LOOSEN → stays 7%. +12.72% is in the 0-15% band but rule forbids
  loosening. Both trailing legs live.
- MRK: 23 sh, entry $125.90, current $123.215, unrealized -$61.76 (-2.13%), intraday -0.66%. HOLD — far from
  the -7% cut (~$117.09). 10% trail live, GTC, order 3d2f860f. Doing its defensive job on the oil-spike tape.
- Guardrail check: PASS (no trade). Day P/L -$50.24 (-0.050%) → nowhere near -3% daily cap. META 4.54% /
  MRK 2.82% ≤ 5% size cap. Weekly slots 1 of 3 used (MRK). TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed — market-open routine only pings on an actual trade). Book ~92.6%
  cash (~$93.1k dry powder). NVDA stays the primary tech deployable once oil reverses/stabilizes. Next
  routine: midday risk check 7/14.

## 2026-07-14 ~12:50 ET — NO-OP (midday risk check, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- Loss-cut scan (-7% rule): NEITHER position is at/past -7% → no forced closes.
  - **META**: 7 sh, entry $578.4486, current $663.485, unrealized **+$595.26 (+14.70%)**, intraday +1.03%
    (up from +12.72% at the open — META ripping today). Gain sits in the **0-15% band** → rule leaves it at
    10%, BUT the stop is already at **7%** (tightened 7/10 at the +17% high) and the ratchet NEVER loosens →
    **stays 7%**. Watch: at +14.70% it's a whisker from the 15-30% band, whose target is also 7% — so no
    action pending regardless. Both trailing legs live (hwm $677.84, stop $630.3912). HOLD, add complete.
  - **MRK**: 23 sh, entry $125.90, current $120.39, unrealized **-$126.73 (-4.38%)**, intraday **-2.94%**
    (worsened from -2.13% at open; the defensive name is the day's laggard, not META). Still **well above
    the -7% cut** (cut ~$117.09; 10% trail stop at $115.263, hwm $128.07, order 3d2f860f live). Thesis
    intact (Keytruda Qlex uptake, Guggenheim $145 / BMO $142, earnings Aug 4). No specific-hold-reason memo
    needed — it isn't past the threshold. HOLD per stop rules.
- Guardrail check: PASS. Day P/L **-$36.33 (-0.036%)** (equity $100,468.60 vs last_equity $100,504.93) →
  nowhere near the -3% daily cap. META 4.62% / MRK 2.76% of equity ≤ 5% size cap. Weekly slots 1 of 3 used
  (MRK). TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing closed — midday only pings on an actual close). Book ~92.6% cash (~$93.1k dry
  powder). Alpaca API healthy again (Mon's key outage resolved). NVDA still the primary tech deployable once
  oil/Iran stabilizes. Next routine: market-close wrap 7/14.

## 2026-07-15 ~09:47 ET — BUY NVDA (market-open routine, market OPEN) — deployment-floor deploy, gate cleared via "equities-rallying-through-it" branch
- **Qty / price / stop: BOUGHT 14 sh NVDA @ $211.73 (market, filled 13:47:03Z). Fresh 10% trailing stop attached cleanly** (trailing_stop sell 14 sh GTC, stop $190.5615 / hwm $211.735, order 92b2b072). Cost ~$2,964.22 (~2.95% of equity). 2nd of 3 weekly new-position slots.
- **Why NOW (gate decision):** The NVDA trigger was oil/Iran stabilizing [(oil reversing/≥1 down session) OR **(equities rallying through it)**] AND a tight live spread. **Oil itself still escalating** (Brent ~$85.22 +0.58%, 4th straight up session; new US strikes, blockade reinstated, Trump threatening power plants/bridges next week, IRGC tanker attacks) → the "oil reversing" branch FAILS. **BUT the "equities rallying through it" OR-branch FIRED:** a **2nd benign inflation print** (June PPI headline **-0.3%**, core **+0.2%** vs +0.3% exp) stacked on Monday's soft CPI, plus a **bullish ASML AI-demand read**, drove a **tech-led up tape (S&P +0.39%, Nasdaq +0.67%, Dow +0.17%)** — the market is durably looking through the oil shock, and doing it in NVDA's own cohort on NVDA's own drivers (inflation relief + AI-capex). CPI gate strongly met, B200 lease firm ~$6, TSMC AI-demand confirm tomorrow (7/16). Falling-knife rule targets initiating into a *rout* — today is the opposite. Deployment-floor discipline: ~93% idle cash in an up market is the miss to avoid; NVDA is the named primary deployable.
- **Spread gate (hard AND-condition): PASS.** Re-sampled NVDA live 3x: $211.99/$212.02 (0.01%), $212.02/$212.06 (0.02%), $212.12/$212.16 (0.02%) — genuinely tight, real 100-share liquidity, ticking naturally. NOT the FDX-style broken feed.
- **Execution note — Alpaca partial outage during the run.** account/positions/order-POST all 504'd for ~15 min (clock/quote/orders-GET stayed up). First buy POST 504'd; I re-checked `orders --status all` (0 NVDA orders → not created server-side) BEFORE each retry to guard against a double-buy. Attempts 1-3 all 504'd with 0 orders created; on the ~4th, the API recovered and the buy filled cleanly with the trail attached. Confirmed post-fill: exactly ONE NVDA position (14 sh), no double-fill.
- **Book after:** META 7 sh (+13.73%, ~4.58%), MRK 23 sh (-1.68%, ~2.83%), NVDA 14 sh (~flat, ~2.95%). Cash $90,090.91, equity $100,505.93, ~89.6% cash. Day P/L +$45.58 (+0.045%) — far inside the -3% cap.
- **Guardrail check: PASS.** Each position <5% size cap; 10% trail on the new buy; weekly slots 2 of 3 (MRK + NVDA); TRADING_MODE = paper; no options/margin/short/crypto.
- **Telegram: SENT** (an actual trade was placed).

## 2026-07-16 ~09:32 ET — NO-OP (market-open routine, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- Executed the 7/16 pre-market plan: HOLD on all 3 holdings; the ONLY actionable idea was the
  deployment-floor's last weekly slot → **FDX**, hard-gated on the chronically-broken paper feed.
  **Live spread re-sampled 3x: bid $295.45 / ask $329.18 = ~11.4%, only 40 sh each side, and
  samples 2-3 had IDENTICAL frozen timestamps** (13:31:12.235). Classic broken/frozen paper feed
  (per 7/6+7/7 lessons) — an ask fill would sit ~11% below bid instantly, near-guaranteed to trip
  the 10% trail. **FDX SKIPPED** — don't market-buy into a >5% spread. Thesis unchanged (oil
  reversal eased the fuel-cost headwind; Buy consensus ~$350 PT); retry when the quote normalizes.
- META: 7 sh, entry $578.4486, current $679.15, unrealized **+$704.91 (+17.41%)**, intraday -0.32%.
  HOLD — no add (target weight ~4.72%, add complete). Gain in the 15-30% ratchet band → target 7%;
  stop already at **7%** (both legs, hwm $686.075 / stop $638.04975) → no change (never loosen).
  Both trailing legs live.
- MRK: 23 sh, entry $125.90, current $124.825, unrealized -$24.73 (-0.85%), intraday +0.98%. HOLD —
  far above the -7% cut (~$117.09). 10% trail live (order 3d2f860f, stop $115.263 / hwm $128.07).
  Doing its diversifier job; KEYNOTE-C93 win + JPM $140 PT intact. Earnings Aug 4.
- NVDA: 14 sh, entry $211.73, current $209.87, unrealized -$26.04 (-0.88%), intraday -1.24%. HOLD —
  day-3 starter, well above the -7% cut & the $191.31 trail. TSMC Q2 record beat confirmed the
  AI-demand thesis; do NOT add a fresh position. 10% trail live (order 92b2b072).
- Guardrail check: PASS (no trade). Day P/L **-$22.66 (-0.02%)** (equity $100,655.44 vs last_equity
  $100,678.10) → nowhere near the -3% daily cap. META 4.72% / MRK 2.85% / NVDA 2.92% ≤ 5% size cap.
  Weekly slots: NVDA opened this week (7/15). TRADING_MODE = paper. No options/margin/short/crypto.
- Note: No Telegram (nothing placed/closed — open routine only pings on an actual trade). Book ~89.5%
  cash (~$90.1k dry powder). FDX stays the named last-slot deployable once its feed normalizes. Next
  routine: midday risk check 7/16.

## 2026-07-17 ~13:10 ET — META STOPPED OUT (winner locked in) + midday risk check (market OPEN)
- **META CLOSED by its 7% trailing stop @ ~09:45 ET (13:45:40Z).** Both legs filled: 3 sh @ $637.796667 + 4 sh @ $637.57 = 7 sh, avg **~$637.68** proceeds ~$4,463.67. Entry $578.4486 (cost $4,049.14) → **realized +$414.53 (+10.24%)**. The trail triggered on a 7% pullback from the $686.075 hwm to the $638.04975 stop (META rode the tech risk-off lower off its 7/16 high). **This is the trailing-stop doing exactly its job — a double-digit winner banked, not a loss.** META has since bounced to ~$650 bid / $664 ask (wide 40-sh frozen paper feed) — normal trail whipsaw; discipline held, no regret trade. META no longer a holding; re-entry is a /trade decision (add was "complete", only 1 weekly slot left, feed currently wide) — NOT a midday action.
- **Loss-cut scan (-7% rule): NO position at/past -7% → no forced closes.**
  - **MRK**: 23 sh, entry $125.90, current $127.745, unrealized **+$42.44 (+1.465%)**, intraday +0.09%. Ran to a $131.74 hwm today (trail ratcheted: order 3d2f860f, stop $118.566 / hwm $131.74). Gain in the **0-15% band → target 10%, already at 10% → no change.** Well above the ~$117.09 -7% cut. HOLD — defensive diversifier, earnings Aug 4.
  - **NVDA**: 14 sh, entry $211.73, current $205.875, unrealized **-$81.97 (-2.765%)**, intraday -0.735%. **Improved from -4.43% at the open** → NOT deteriorating toward the cut. Well above the -7% cut (~$196.91) & the $191.31 10% trail (order 92b2b072, hwm $212.5693). Thesis intact (TSMC AI-demand confirm, Vera Rubin deal, Strong Buy $301.62). HOLD — no add, no hold-memo needed (not past threshold).
- **Stop-tightening scan:** none actionable — MRK in 0-15% band (10%, no change); NVDA is a loser; META gone.
- **Guardrail check: PASS.** Day P/L **-$205.73 (-0.205%)** (equity $100,376.04 vs last_equity $100,581.77) → far inside the -3% daily cap. MRK 2.93% / NVDA 2.87% ≤ 5% size cap. Weekly slots: 2 of 3 used (MRK + NVDA); META was a CLOSE, not a new slot. TRADING_MODE = paper. No options/margin/short/crypto.
- **Telegram: SENT** (a position — META — was actually closed today).
- Note: Book now ~94.2% cash (~$94.55k dry powder) after META proceeds landed. Only 2 holdings left (MRK + NVDA). **Weekly-review routine fires at today's close (Fri 7/17)** — it will grade the week & the META stop-out vs the S&P. Next routine: market-close / weekly-review.

## 2026-07-20 ~09:31 ET — NO-OP (market-open routine, market OPEN)
- Qty / price / stop: none — no order placed, none closed, no stop tightened.
- Executed the 7/20 pre-market plan against live state. **Regime: confirmed semiconductor BEAR
  MARKET (China's Kimi K3 open-weight model, SOX/SOXX >20% off the June-2 peak) + oil spiking
  (Brent ~$88, +14%/wk, Iran attacked a Kuwaiti plant) = risk-off tape.** Falling-knife rule BINDS
  for any AI/tech name → the logged decision to stay mostly cash for tech is deliberate and correct.
- **Deployment-floor (new week, 0 of 3 slots, ~94.2% cash):** the plan named **GEHC** as the primary
  rotation-into-defensives deployable (oil-insensitive + uncorrelated to the semi rout), gated on a
  tight live spread. **Live spread re-sampled 3x: bid $62.51 / ask $66.96 = ~6.9%, 100 sh each side,
  and all 3 samples had IDENTICAL frozen timestamps (13:31:10.237266512Z).** Classic broken/frozen
  paper feed (per 7/6+7/7+7/16 FDX lessons) — an ask fill would sit ~7% below bid instantly,
  near-guaranteed to trip the 10% trail. **GEHC SKIPPED** — don't market-buy into a >5% spread.
  Thesis unchanged (~30% disc to ~$88 FV); retry when the quote normalizes. Secondary was an
  **MRK-add on a pullback** — trigger NOT met (MRK is +0.88% from entry, ~flat intraday, not a
  pullback). No deployable cleared its gate → book stays ~94% cash. Deployment-floor satisfied:
  named deployable (GEHC, spread-gated) + logged risk-off reason to hold cash.
- **NVDA**: 14 sh, entry $211.73, current $205.675, unrealized **-$84.77 (-2.86%)**, intraday
  **+1.41%** (recovering, stabilizing above $200). Well above the -7% cut (~$196.91) & the $191.31
  10% trail (order 92b2b072, hwm $212.5693). **HOLD, do NOT add** — the slide is now a structural
  semi bear-market re-rating (Kimi K3), higher bar to hold, no averaging down. Not past any
  threshold → no hold-memo needed. Midday MUST re-check the -7% cut.
- **MRK**: 23 sh, entry $125.90, current $127.01, unrealized **+$25.53 (+0.88%)**, intraday -0.38%.
  Well above the -7% cut (~$117.09). 10% trail live (order 3d2f860f, stop $118.566 / hwm $131.74).
  Doing its oil-insensitive defensive job in a semi-rout + oil-spike tape; new Lipfendra FDA
  approval; PTs $140-150. Earnings Aug 4. HOLD — no add (not a pullback).
- **Guardrail check: PASS.** Day P/L **+$28.84 (+0.029%)** (equity $100,355.23 vs last_equity
  $100,326.39) → far inside the -3% daily cap. MRK 2.91% / NVDA 2.87% of equity ≤ 5% size cap.
  Weekly slots: 0 of 3 used (new week 7/20). TRADING_MODE = paper. No options/margin/short/crypto.
- **Telegram: NOT sent** (nothing placed/closed — open routine only pings on an actual trade).
- Note: Book ~94.2% cash (~$94.55k dry powder). GEHC stays the named primary deployable once its
  feed normalizes; MRK-add on a genuine pullback is the secondary. Next routine: midday risk check —
  **MUST re-check NVDA's -7% cut** (~$196.91).

## 2026-07-21 ~09:34 ET — BOUGHT FDX (deployment-floor deploy, market OPEN)
- Qty / price / stop: **BOUGHT FDX 9 sh @ $313.00** (order a03872d0, ~2.81% of equity). **10% trailing
  stop attached** (order 6f599c57, sell trailing_stop, gtc, stop $281.34 / hwm $312.60). Fill note: the
  `buy` script timed out at 15s (order only partially filled — 4/9 — at that moment), so it exited
  WITHOUT attaching the trail; I re-checked `orders --status all` → the market order then completed FULLY
  (9/9 @ $313.00) and the spread had TIGHTENED to 0.31%, so per the 7/9 tight-spread lesson I **manually
  POSTed the trailing_stop sell leg for 9 sh** (did NOT cancel — the fill was clean at $313, not the FDX
  broken-feed case). Position confirmed protected.
- Reasoning: Executed the 7/21 pre-market plan's deployables against live gates on a **risk-on tape**
  (oil easing on Iran ceasefire talks; Kimi K3 re-framed memory-bullish). **GEHC (primary): SKIPPED** —
  feed broken again (bid frozen $58.65, ask flickering $62.25→$65.03 = 5.8–9.8% spread; an ask fill sits
  ~6–10% below bid → near-certain trail trip). **MRK-add (secondary): SKIPPED** — trigger is a pullback +
  fresh catalyst; MRK ~flat from entry, no new catalyst → not met. **FDX (tertiary): BOUGHT** — spread
  sampled 3x STABLE at ~2.26% (bid $307.01 held all 3, ask $313.95–99, NOT the flicker-wide 7/6–7/7
  pattern), cleanest FDX feed in weeks + inside the <~3% gate; thesis right THIS tape (oil-ease removes
  the fuel headwind; Citizens JMP "market outperform" PT $375, Buy consensus ~$350); non-tech diversifier.
  Deployment-floor discipline (0/3 slots, ~94% cash, up tape → idle cash is the logged miss) tipped a
  clean-gate name to action; falling-knife rule doesn't bind (not a rout). Sized SMALL (~2.8%) as a
  tertiary/lower-conviction starter with real oil flip-flop risk. NVDA (HOLD, +1.53% intraday, bear
  thesis softening) & MRK (HOLD) unchanged — no add, no cut.
- Guardrail check: **PASS.** FDX 2.81% / MRK 2.86% / NVDA 2.88% ≤ 5% size cap. Weekly slots: **1 of 3
  used (FDX, new week 7/21).** Day P/L **+$52.32 (+0.05%)** (equity $100,313.99 vs last_equity
  $100,261.67) → far inside the -3% daily cap. TRADING_MODE = paper. No options/margin/short/crypto.
  All 3 positions have live 10% trailing stops.
- Telegram: **SENT** (a trade was placed).

## 2026-07-22 ~09:31 ET — market-open (Wed; NO trades — HOLD all 3, deployment-floor logged as deliberate cash)
- **NO TRADES PLACED.** Standing-plan check: the 7/21 FDX deploy was already executed on 7/21;
  the 7/22 pre-market plan's logged decision is HOLD all three + deploy GEHC only IF the tape
  stabilizes AND its spread confirms. Market confirmed OPEN (`is_open: true`, 09:30 ET).
- **GEHC (primary deployable): SKIPPED.** Live quote sampled 3x = bid $62.28 / ask $62.46 (~0.29%,
  100 sh each side) — but all 3 samples had IDENTICAL frozen timestamps (13:31:25.019743689Z) =
  the same chronic broken/frozen paper feed flagged 7/6+7/7+7/16+7/21, not a trustworthy live read.
  More decisively, the TAPE fails the gate regardless: **oil-driven risk-off (Brent ~$94, Iran
  ceasefire stalled) + the GOOGL/TSLA AI-capex binary TONIGHT + GEHC's own Q2 print 7/29 (~5
  sessions out)** = not a tape to add risk into; falling-knife leans caution. Thesis unchanged
  (~30% disc to ~$88 FV; Citi/UBS upgrades); retry when the feed normalizes AND the tape stabilizes.
  Secondary = MRK-add on a pullback — trigger NOT met (MRK +0.92% from entry, not a pullback).
- **FDX**: 9 sh, entry $313.00, current $314.95, unrealized **+$17.55 (+0.62%)**, intraday -0.08%.
  10% trail live (order 6f599c57, stop $285.30 / hwm $317). **Oil re-spike to ~$94 revives the fuel
  headwind (logged flip-flop risk materializing) — inside the trail, NOT a cut; most oil-exposed
  holding → watch at midday.** 0-15% band → stop stays 10%. HOLD.
- **MRK**: 23 sh, entry $125.90, current $127.06, unrealized **+$26.68 (+0.92%)**, intraday +0.63%.
  Well above the -7% cut (~$117.09). 10% trail live (order 3d2f860f, stop $118.566 / hwm $131.74).
  Oil-insensitive defensive doing its job on an oil-spike day; PTs $138-155. Earnings Aug 4. HOLD.
- **NVDA**: 14 sh, entry $211.73, current $205.74, unrealized **-$83.86 (-2.83%)**, intraday -0.75%.
  Above the -7% cut (~$196.91) & the $191.31 10% trail (order 92b2b072, hwm $212.5693). Chips cooling
  on the risk-off tape; worst chip performer 2026 but thesis intact (Goldman 21.7x "compelling").
  **GOOGL/TSLA capex tonight = the AI-capex read-through — do NOT add ahead of the binary.** HOLD.
- **Guardrail check: PASS.** Day P/L **-$4.20 (-0.004%)** (equity $100,376.09 vs last_equity
  $100,380.29) → far inside the -3% daily cap. FDX 2.82% / MRK 2.91% / NVDA 2.87% of equity ≤ 5%
  size cap. Weekly slots: **1 of 3 used (FDX).** TRADING_MODE = paper. No options/margin/short/crypto.
  All 3 positions have live 10% trailing stops.
- **Telegram: NOT sent** (nothing placed/closed — open routine only pings on an actual trade).
- Note: Book ~91.4% cash (~$91.7k dry powder). GEHC stays the named primary deployable once its
  feed normalizes AND the tape stabilizes; MRK-add on a genuine pullback is the secondary. Next
  routine: midday risk check — re-check NVDA's -7% cut (~$196.91) & FDX on the oil headwind.
