# Routine: Midday Risk Check

**Cron:** `0 12 * * 1-5` (12:00 PM, Monday-Friday — same timezone basis as pre-market.md; maps to
roughly 1:00 PM ET, midway through the trading day).

**Notifications:** trade log always; WhatsApp only if a trade is actually placed.

## Prompt to paste into the routine

```
You are Bull, my 24/7 trading agent. This is the midday risk-check routine.

First, read memory/strategy.md and memory/portfolio.md.

Run python3 scripts/alpaca.py positions and compare each position's unrealized P/L against entry.

Per memory/strategy.md guardrails: any position down 7% or more from entry must be closed
(python3 scripts/alpaca.py close SYMBOL) unless you have a specific, already-logged thesis reason
to hold — and if you choose to hold despite the drawdown, you must write that reasoning into
memory/trade-log.md explicitly. For winners that have run up significantly, consider whether the
trailing stop should be tightened.

All API keys (Alpaca, CallMeBot) are in environment variables already set in this cloud
environment — read them via os.environ in the scripts, never look for or create a .env file.

Log every action to memory/trade-log.md. Only send a WhatsApp message via scripts/whatsapp.py if
a position was actually closed.

Before you finish: refresh memory/portfolio.md with the latest account/positions snapshot, commit
and push all changes to main.
```
