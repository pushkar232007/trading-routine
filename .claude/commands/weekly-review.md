---
description: Friday close — grade the week, compare to the S&P 500, propose changes
---

Read `memory/portfolio.md`, all of this week's entries in `memory/trade-log.md`, and all of this
week's entries in `memory/research-log.md`.

1. Calculate the portfolio's return for the week (`python3 scripts/alpaca.py account` gives
   current equity; compare against last Friday's equity recorded in `memory/weekly-review.md`).
2. Look up the S&P 500's return for the same week (WebSearch — e.g. SPY weekly performance).
3. Identify the single best decision and single worst decision of the week, honestly.
4. Grade the week A-F. Be honest, not generous.
5. Propose concrete changes if something isn't working — to `memory/strategy.md` guardrails, to
   a `.claude/commands/*.md` skill, or to the routine cron schedule itself. Don't just say "do
   better" — name the specific file and the specific change.

Append the entry to `memory/weekly-review.md` in the documented format.

Always send a WhatsApp summary this run (`python3 scripts/whatsapp.py "..."`) — portfolio return,
S&P return, delta, and the grade. This is one of the two routines (along with market close) that
always notifies regardless of whether a trade happened.

Commit and push everything at the end.
