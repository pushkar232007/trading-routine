---
description: Refresh portfolio snapshot and write any lessons learned this run
---

Run:
```
python3 scripts/alpaca.py account
python3 scripts/alpaca.py positions
```

Overwrite `memory/portfolio.md` with the fresh snapshot (cash, equity, buying power, day P/L,
open positions table). This file should always reflect current state, not history.

Then think back over this routine's run: did anything happen that's worth remembering next time?
A guardrail that almost got breached, an API quirk, a signal that worked or didn't. If so, append
a terse note to `memory/signals-learnings.md` under the right section (Signals worth weighting /
Mistakes to avoid / Process notes). If nothing new was learned, skip this step — don't pad the
file with filler.

Finally, commit and push:
```
git add -A && git commit -m "journal: <one-line summary>" && git push
```
