# Signals & Learnings

_Bull: this is your running playbook — heuristics that worked, mistakes not to repeat, signal
patterns worth watching for. Update this whenever you notice something generalizable. This file
is what makes you better over time instead of repeating the same mistakes._

## Signals worth weighting

- **Falling-knife entry rule (validated 2026-06-26 weekly review).** In a confirmed 3+ day broad,
  sentiment-driven rout, do NOT initiate a NEW position until a bottom confirms — defined as ≥1 clear up
  day OR the index reclaiming a prior level OR (for AI names) AI-compute pricing stabilizing. The only
  exception is a pre-sized HALF-starter on the single highest-conviction name. Why it's here: the week of
  06-22 proved both sides — HOLDING the contingent META add through the rout (and not initiating
  NVDA/MU/AVGO/FDX) was the best decision and beat the S&P by ~1.9 pts in a -2% week; the one decision that
  cost money was buying the META starter into day-3 of the same rout (now -2.47% underwater). Defensive cash
  in a sentiment rout = relative alpha. But don't let it calcify — once a bottom confirms, deploy the dry
  powder; the mission is to beat the index, not to hide in cash.

- **Deployment-floor discipline (added 2026-07-02 weekly review).** Once posture is CONSTRUCTIVE
  and a bottom is confirmed, if the book is >90% cash the pre-market routine MUST either (a) name a
  specific deployable position with a concrete entry trigger for the week, or (b) log an explicit,
  dated reason why staying >90% cash is still correct. This is NOT a hard guardrail — never force a
  bad trade — it's a required, logged DECISION so "hold everything" can't be the silent default for
  an entire up week. Why it's here: the week of 6/29 we called the bottom Monday, wrote CONSTRUCTIVE
  daily, held 3 open slots + ~$96k dry powder, opened 0 new positions, and lagged a +1.76% S&P by
  1.68 pts. The falling-knife rule tells you when NOT to buy; this is its counterweight — once the
  bottom confirms, cash is a position you must defend on purpose, not drift into. Cash earns nothing
  in an up week; a one-name book only beats the index when the index falls.

- **Sequencing beats chasing a catalyst pop (validated 2026-07-02).** META re-rated +8.8% Wed 7/1 on the
  "Meta Compute" news. Rather than chase the pop (~$614–618), the plan added +3 sh POST the Thu June-NFP
  binary once it printed soft-not-recessionary (57K, UE 4.2%) AND META held — filled $599.30, below the
  pop high. META then faded -4.9% to close $582.70 (add slightly red intraday), but the discipline is sound:
  wait for the binary to clear, size small (3 sh) after a big move, don't demand a full pullback that may
  not come but don't chase the spike either. The 7-sh blended position still closed green (+0.735%). Also:
  the `alpaca.py buy --trail-percent` stop leg attached cleanly on the add (the old naked-short 403 bug
  stays fixed — no manual re-submit needed).

## Mistakes / anti-patterns to avoid

- **FIXED in code (2026-06-24, human): `alpaca.py buy` no longer races the stop leg.** The bug
  below (naked-short 403 on the trailing-stop leg) was real but is now fixed — `cmd_buy` polls
  `_wait_for_fill` until the market buy actually fills before submitting the trailing-stop sell.
  You should no longer hit this; if you somehow do, it's a new problem, not this one recurring.
  Original note, kept for context:
  - `alpaca.py buy SYMBOL QTY --trail-percent N` can 403 on the stop leg. The script submitted the
    market buy and the trailing-stop sell back-to-back without waiting for the buy to fill, so
    Alpaca briefly saw the stop-sell as a naked short and rejected it (`cannot open a short sell
    while a long buy order is open`) even though the buy itself filled fine. First hit 2026-06-24
    on the META starter. If `_wait_for_fill` ever times out (15s) instead, check `positions` — the
    buy likely filled — then re-submit just the trailing_stop sell order manually.

## Process notes

- **CONFIRMED (2026-06-24): crons now fire at correct NYSE times.** First full day with properly-timed
  execution routines — market-open ~09:55 ET (META starter filled), midday 13:03 ET, market-close 16:04 ET,
  all with the clock reading correctly (open during session, closed after 16:00). The "8h early" worry is
  resolved; deployment is no longer blocked by timing. Treat the early-firing notes below as historical.
- **CORRECTION (human-verified, 2026-06-24): the cron schedule is NOT broken.** The `is_open: false`
  runs logged below on 2026-06-22 through 2026-06-24 were all triggered manually via "Run now" during
  initial setup/testing, at whatever time of day the human happened to be testing (often ~1 AM ET) —
  not from the actual scheduled cron firing. The real configured crons (`30 13 * * 1-5` market-open,
  `0 17 * * 1-5` midday, `0 20 * * 1-5` close, all UTC) were independently verified by the human to
  correctly map to NYSE hours. No schedule change is needed. Do not re-propose a cron/timezone fix —
  if a future run still sees `is_open: false` at its scheduled time, that's a genuinely new problem,
  not this one recurring.
- **Routine scheduling is ~8h early (recurring).** On 2026-06-24 every routine — market-open, midday,
  and market-close — fired around 01:xx ET, before the 09:30 open, so the clock read `is_open: false`
  and no orders could execute. Net effect: the planned META starter never got placed all day despite a
  ready plan. Fix the cron/timezone offset so routines fire during/after the cash session (open ~09:30,
  close ~16:00 ET). Until fixed, treat early "open/midday/close" runs as plan-only, not execution.
  **(See correction above — this was manual test-run timing, not the actual cron.)**
- **Escalate the misfire, don't just log it.** When an *execution* routine (open/midday/close) fires
  with `is_open: false`, send ONE Telegram flag that day (not silent logging) so the human notices the
  broken schedule and fixes the cron. Silent logging let this recur unseen and cost a full +1.6% S&P
  week in cash (see weekly-review 2026-06-22). One flag per day, not per run — don't spam.
- **A good plan that never executes still loses to the index.** Inception week: sound META starter,
  disciplined avoidance of MU/FDX/INTC traps, zero losses — but 0 trades and -1.6% vs S&P because a
  timing bug blocked every execution. Risk discipline is necessary but not sufficient; deployment is
  the job. When a guardrail-clean plan is pending and the market is open, the catch-up rule in
  `.claude/commands/trade.md` says execute it.
