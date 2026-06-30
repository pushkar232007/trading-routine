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
