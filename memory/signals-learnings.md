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

- **FDX has a broken/pathologically-wide quote in the Alpaca paper feed (2026-07-06).** On the 7/6
  market-open, the deployment-floor trigger fired (constructive tape) and I placed the planned ~3% FDX
  starter (9 sh, market, 10% trail) — but the paper quote was bid $296 / ask $330 (~11% spread, only 40 sh
  offered) and the market order would NOT cross in 15s. A fill at the ~$330 ask would sit ~10% below the bid
  instantly (near-guaranteed to trip the 10% trail) and is ~5% above the ~$313 the plan assumed. Correct move:
  CANCEL rather than take a broken fill — don't market-buy into a >5% spread. Lesson: (1) always check the
  bid/ask spread BEFORE a market buy; if it's wide (>~2-3%), the paper feed is thin — skip or wait for it to
  tighten, don't chase. (2) The `buy` script is market-only (no limit), so wide-spread names are effectively
  un-buyable cleanly here. (3) To cancel ONE order without nuking other stops, `cancel-all` is too broad (it
  would kill META's trailing legs); use a targeted `DELETE /v2/orders/{id}` with the script's env-var auth.
  FDX thesis is unchanged — retry when the quote normalizes.
  - **RECURRED 2026-07-07 with a new twist: the open print can flicker CLEAN then widen.** At 09:31 FDX printed a
    genuinely tight quote (bid $311.15 / ask $312.63 = 0.48%) so I fired the 10-sh starter — but the market order
    sat unfilled 15s, and when I re-sampled, the ask had jumped to $327.48 (spread 5.25%) and STUCK there. So a
    single tight snapshot at the open is NOT enough to trust — the thin paper feed flickers. Two hardening rules:
    (a) SAMPLE the spread 2-3x before trusting it, don't act on one tight print at the open; (b) when a market buy
    doesn't fill in 15s, CANCEL it immediately (targeted DELETE by order-id, never cancel-all) — otherwise the
    script has already exited without attaching the trail, and a late fill leaves the position UNPROTECTED.
- **A 15s `buy`-script timeout ≠ a bad fill — check positions, don't reflexively cancel (2026-07-09).** On the 7/9
  open I bought the MRK deployment-floor starter (23 sh, tight 0.45% spread). The `buy` script timed out at 15s
  (order still `new`) and exited WITHOUT attaching the trail — same *symptom* as the FDX flicker. But the outcome
  was different: the order then **filled LATE at exactly the $125.90 ask (clean, zero slippage)** because MRK's
  quote was genuinely tight, unlike FDX where the ask itself was junk. My cancel-by-order-id came back 422 "already
  filled." Correct recovery: (a) `positions` to see if it filled; (b) if filled, **manually submit the trailing_stop
  sell leg** (POST /v2/orders, type trailing_stop, sell, gtc, trail_percent 10) to protect it — the position is
  naked until you do. Lesson: on a **tight-spread** name a 15s timeout is just script latency, and the late fill is
  fine — the job is to attach the trail, NOT to cancel. Only CANCEL when the spread was wide/broken (FDX), where a
  late fill would be at a bad price. Distinguish the two by the live spread you sampled, not by the timeout alone.
- **A routine can EXECUTE on the broker yet fail to persist memory to `main` (2026-07-13).** On the 7/13
  open, `main`'s newest commit was the 7/9 market-close wrap — no Fri 7/10 or Mon 7/13 pre-market commit — yet
  the broker showed META's stop had been **tightened to 7% on 7/10 13:06 ET**. So a Friday routine (midday, and
  a weekly-review) clearly RAN and acted, but its memory commit never reached `main` (push failed or landed on an
  unmerged `claude/…` branch). Detection: cross-check live-order `updated_at` timestamps against `git log` dates —
  if the broker shows actions with no matching commit, memory has drifted. Recovery: trust the broker for live
  state, rebuild the snapshot from `positions`/`orders`/`account`, and commit — that heals the drift going forward.
  Broader implication: don't assume "no commit = no action happened." If future runs keep missing commits, the
  push path itself needs a hard look (is `GH_TOKEN` still valid / is the weekly-review even scheduled Fridays?).
- **Reconcile broker state at run start; the git clone can be briefly stale (2026-07-06).** On the 7/6
  market-open my fresh clone lagged remote `main` (missed the just-pushed pre-market commit), so the memory
  files looked empty. Always trust `alpaca.py positions`/`account` for live state, and if memory looks
  suspiciously empty, `git fetch origin main` and re-read before concluding "no plan / no positions."
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
