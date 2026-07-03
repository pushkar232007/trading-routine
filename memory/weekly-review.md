# Weekly Review

_Bull: append a new entry every Friday close. Newest at top. Be honest — grade yourself, don't
just write a highlight reel._

Format:

```
## Week of YYYY-MM-DD
- Portfolio return: __%  |  S&P 500 return: __%  |  Delta: __%
- Best decision:
- Worst decision:
- Grade: A-F
- Changes to make next week (strategy.md / commands / cron):
```

---

## Week of 2026-06-29 (holiday-shortened, reviewed Thu 2026-07-02 close; Fri 7/3 CLOSED for July 4th)
- Portfolio return: **+0.08%** ($99,948.71 → $100,031.14)  |  S&P 500 return: **~+1.76%** (7,354.02 Fri 06-26 → 7,483.24 Thu 07-02)  |  Delta: **−1.68 pts** (UNDERPERFORMED)
- Best decision: **Reading the META "Meta Compute" re-rate as fundamental, not noise — and executing the add with discipline.** When META surged +8.8% Wed 7/1 on the Bloomberg cloud-infra report, the correct read was that it answers the #1 bear case (capex monetization), not a momentum spike to fade. Rather than chase the ~$614–618 pop, we sequenced the +3 sh add to POST the Thu June-NFP binary, filled $599.30 (below the pop high) once jobs printed soft-not-recessionary (57K, UE 4.2%) AND META held — lifting the position to 7 sh @ $578.45 blended, 4.08% of equity (target weight), currently +0.77%. Good fundamental read + clean sequencing + correct sizing after a big move. The `alpaca.py buy --trail-percent` stop leg attached cleanly (old naked-short bug stays fixed).
- Worst decision: **Sitting ~96% cash through a confirmed-bottom +1.76% rally — the exact "don't let defensive calcify into cash" mistake last week's review flagged (change #3).** The bottom was CONFIRMED Monday 6/29 (clear up day, Dow record close) — the falling-knife rule's own deploy condition was met — and posture read CONSTRUCTIVE from Tuesday on. Yet across the whole week we opened **0 of 3 new positions** and made only the one META add, leaving ~$96k dry powder idle while the index ran +1.76%. Each single-name skip was individually defensible (NVDA gate doubly-unconfirmed, MU breaking down, AVGO/FDX low priority), but the aggregate result is that we under-participated in a rally we correctly called the bottom of. Cash earns nothing in an up week — this is the inception-week lesson repeating: a good defensive read that doesn't convert to deployment still loses to the index.
- Grade: **C−.** Honest mark for a week we lagged the benchmark by 1.68 pts while repeating a previously-flagged over-caution error. Not lower because: zero losses, every guardrail respected (size 4.08% ≤ 5%, 10% trailing stops live on both legs, weekly-slot cap, daily-loss cap, paper mode), the one trade was genuinely well-executed, the thesis work on META was strong, and it was a 4-session holiday week. Not higher than C− because the core mission is to BEAT the S&P and we did the opposite — we identified the bottom, wrote "CONSTRUCTIVE" daily, held 3 open slots + $96k, and still deployed almost nothing into a +1.76% tape. Last week's +1.9-pt outperformance and this week's −1.68-pt underperformance are two sides of the same coin: we are running a one-name book that only wins relative to the index when the index falls.
- Changes to make next week:
  1. **Deployment-floor discipline (add to `memory/signals-learnings.md` → Signals worth weighting).** Once posture is CONSTRUCTIVE and a bottom is confirmed, if the book is >90% cash, the pre-market routine MUST either (a) name a specific deployable position with a concrete entry trigger for that week, or (b) log an explicit, dated reason why staying >90% cash is still correct. This forces a bias-to-act (or a justification), so "hold everything" can never again be the silent default for an entire up week. Not a hard guardrail (never force a bad trade) — a required decision, logged.
  2. **Widen the watchlist beyond correlated AI/tech (change to `.claude/commands/research.md`).** The entire watchlist — META/NVDA/MU/AVGO/FDX — is tech/AI-hardware and moves together; when that one sector is being re-rated, 4 of 5 names gate out and there is nothing left to buy. We even NOTED the rotation INTO non-tech (healthcare/XLV +7.88% the week of 6/26) and bought none of it. Add a requirement that the research routine surface **≥2 non-AI/non-tech candidates** each week so deployment isn't hostage to one sector's gate.
  3. **Consider sizing META toward the full 5% cap (lower priority, discretionary).** It's the only conviction name and the thesis strengthened this week; at 4.08% there's room. Not a rule change — flag it for the next pre-market/trade run to weigh against keeping powder for a diversifying second name (change #2).

## Week of 2026-06-22 (first full trading week, reviewed Fri 2026-06-26 close)
- Portfolio return: -0.05% ($100,000.00 → $99,948.71)  |  S&P 500 return: ~-2.0% (slid nearly 2% on the week; closed 7,354.02 Fri 06-26, Nasdaq -4.6%)  |  Delta: **+1.9 pts** (outperformed)
- Best decision: **Holding the contingent META add through the rout — defensive cash as relative alpha.**
  The add was gated on the 06-25 PCE print; core came in HOT (+3.4% y/y) → held. The 06-26 AI-cost/bubble
  rout (OpenAI IPO-delay report, NVDA B200 lease price -31%/3wks, device-maker margin fears, Kospi -8%
  circuit breaker) gave a second reason to keep it held and to NOT initiate NVDA/MU/AVGO/FDX. Net: we sat
  ~98% cash through a week the S&P fell ~2% and the Nasdaq fell ~4.6%, so being under-deployed and defensive
  turned a -2% benchmark week into a ~flat book — +1.9 pts of relative outperformance, the inverse of last
  week's mistake. Guardrails (size, weekly-slot, stop, daily-loss) all respected.
- Worst decision: **The META starter entry timing (06-24, 4 sh @ $562.81).** It's the one position we hold
  and it's underwater -2.47% from entry. We bought into day-3 of the rout — mildly inconsistent with the
  exact "don't catch the falling knife" rule we then applied correctly for the other four days. Damage was
  capped (half-size 2.2% of equity + 10% trailing stop), so this is a minor blemish, not a real loss, but
  honestly it's the only decision that cost money this week.
- Grade: **B.** Beat the benchmark by ~1.9 pts through disciplined defensive positioning, respected every
  guardrail, and read both the hot PCE and the AI rout correctly. Not an A: (1) the win is relative/defensive
  (we're -0.05% absolute — outperformance came from being in cash during a down week, not from a winning
  thesis), and (2) the single position we do hold is underwater because its entry slightly contradicted our
  own falling-knife rule. Clear improvement over last week's D — this time discipline produced the right
  outcome instead of the wrong one.
- Changes to make next week:
  1. **Codify the falling-knife entry rule (added to `memory/signals-learnings.md` → Signals worth
     weighting this run).** Validated twice now: in a confirmed 3+ day broad/sentiment-driven rout, do NOT
     initiate a NEW position until a bottom confirms (≥1 up day OR the index reclaims a prior level); the
     only exception is a pre-sized half-starter on the single highest-conviction name. This is exactly what
     went right (the held add) and what slightly went wrong (the 06-24 starter) this week — make it explicit
     so the next run doesn't have to re-derive it.
  2. **No strategy.md guardrail change needed.** The existing guardrails (5% size, half-size discretion,
     10% trailing stop, weekly-slot cap) worked — they capped the one mistake to a 2.2% underwater starter.
     The gap was a heuristic, not a hard rule, so it belongs in the playbook (change #1), not the guardrails.
  3. **Watch for the deploy signal.** Two weeks now of mostly-cash; that was correct into a rout but the
     mission is to BEAT the S&P, which means deploying when the rout confirms a bottom. Next week: if the
     AI rout shows a bottom (up day / index reclaim / AI-compute pricing stabilizes), the 2 open weekly
     slots and ~$97.7k dry powder are there to act — don't let "defensive" calcify into permanent cash.

## Week of 2026-06-22 (inception week)
- Portfolio return: 0.00%  |  S&P 500 return: +1.6%  |  Delta: -1.6%
- Best decision: **Discipline on binary/momentum names.** Held off MU into its after-close fiscal
  Q3 print (binary), refused to chase FDX's guidance-driven falling knife pre-open, and avoided
  INTC's +250% YTD momentum chase. Capital fully preserved — no reckless entries on a stretched,
  narrow-leadership tape. The META starter plan itself was sound (fresh multi-bank upgrades, no
  imminent catalyst, ≤5% sizing + 10% trailing stop).
- Worst decision: **Letting the ~8h-early routine-timing bug block all execution for a second day.**
  A ready, guardrail-clean META starter never got placed because every execution routine (open,
  midday, close) fired at ~01:xx ET while `is_open: false`. Net result: sat 100% cash through a
  +1.6% S&P week with a plan in hand. This is a process/operational failure, not a thesis failure —
  and it went only *logged*, not *escalated*, so it recurred.
- Grade: **D.** Clean slate, zero losses, sound research and disciplined risk posture — but the core
  mission (deploy capital, beat the S&P) was failed: 0 trades, underperformed the benchmark by 1.6%
  purely by being stuck in cash. Not an F because capital is intact and the plan is ready to fire the
  moment the timing is fixed; not higher than D because "good plan, never executed" still loses to the
  index.
- Changes to make next week:
  1. ~~Routine cron timezone (highest priority — needs the human).~~ **CORRECTED post-run, 2026-06-24:**
     this was a false alarm. The `is_open: false` firings all week were manual "Run now" test triggers
     during initial setup (often run at ~1 AM ET by the human), not the actual scheduled cron. The human
     independently verified the real configured crons already match what's proposed below — no change
     was needed. See `memory/signals-learnings.md` Process notes for the full correction. (Original text
     preserved for history: "`routines/*.md` crons are written as `30 8 * * 1-5` etc. assuming ET, but
     the scheduler fires them ~8h early. Pin the cloud routine schedule to `America/New_York`, OR convert
     every cron to UTC: market-open `30 13 * * 1-5`, midday `0 16 * * 1-5`, close `0 20 * * 1-5`.")
  2. **Standing-plan catch-up rule (implemented this run in `.claude/commands/trade.md`).** If a prior
     pre-market plan was never executed and the market is now open, execute the standing plan first —
     so a single in-hours run salvages the day even if the open routine misfired.
  3. **Escalate-once on misfire (implemented in `memory/signals-learnings.md`).** When an execution
     routine fires with `is_open: false`, send ONE Telegram flag (not silent logging) so the human
     notices the broken schedule instead of it recurring unseen.
