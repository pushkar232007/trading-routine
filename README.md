# Bull — 24/7 AI Trading Agent (Claude Code Routines)

A Claude Code project that runs on a schedule (pre-market, market open, midday, close, and a
Friday weekly review), researches the market with native web search, places trades via the
Alpaca API within hard guardrails, journals everything to files so a stateless agent can pick up
where it left off, and sends Telegram notifications on trades and daily/weekly summaries.

**This is not financial advice.** It's an experiment in agentic trading. Start in paper mode and
stay there until you're genuinely comfortable with what the agent does on its own.

## How it's structured

```
CLAUDE.md                  Bull's identity, protocol, and rules — read by every routine automatically
memory/                     Persistent state — the only thing Bull remembers between runs
  strategy.md               Guardrails, thesis, trading mode (paper/live), watchlist
  portfolio.md              Current snapshot of cash/equity/positions (overwritten each run)
  trade-log.md              History of every trade placed/skipped, append-only
  research-log.md           History of research findings, append-only
  signals-learnings.md       Running playbook of what's working / not working
  weekly-review.md           Friday grades vs. the S&P 500, append-only
scripts/
  alpaca.py                  CLI wrapper for the Alpaca trading + market data REST API
  telegram.py                 CLI wrapper for Telegram Bot API notifications
.claude/commands/            Custom skills: /research, /trade, /journal, /weekly-review
routines/                    The exact prompt + cron schedule for each of the 5 scheduled triggers
.claude/settings.json        Pre-approved permissions so routines don't stall waiting for a human
.env.example                 Documents required env var names (not filled in, not used at runtime)
```

## One-time setup

### 1. Alpaca (broker)

1. Sign up at [alpaca.markets](https://alpaca.markets) → Trading API.
2. You get a paper trading account automatically (default $100k paper balance).
3. In the dashboard, generate API keys — you'll get a **Key ID** and a **Secret Key**. Save both
   immediately; the secret is only shown once.
4. Paper base URL: `https://paper-api.alpaca.markets`. (Live: `https://api.alpaca.markets` — only
   switch to this, and flip `TRADING_MODE` in `memory/strategy.md` to `live`, once you've watched
   the paper bot for a while and are comfortable with real money.)

### 2. Telegram notifications (Bot API)

1. In Telegram, message **@BotFather** → `/newbot` → follow the prompts to name your bot.
   BotFather replies with a token like `123456789:ABCdefGhIJKlmNoPQRstuVwxyz`.
2. Open a chat with your new bot (search its `@username`) and send it any message (e.g. "hi") so
   it's allowed to message you back.
3. Fetch your chat ID by visiting `https://api.telegram.org/bot<TOKEN>/getUpdates` in a browser
   (replace `<TOKEN>`) and finding `"chat":{"id": NUMBER, ...}` in the response.
4. You'll need both the bot token and that chat ID.

This is the official Telegram Bot API — free, reliable, no business verification needed. If you
ever want a different channel, `scripts/telegram.py` is the only file you'd need to swap out.

### 3. Claude Desktop app

1. Install from the Claude downloads page. You need a paid plan (Pro/Max) — routines require it.
2. Open this folder (`~/trading-routine`) as a project, either via the Claude Desktop app directly
   or via VS Code with the Claude Code extension (recommended while you're still setting things
   up, since VS Code shows you the file tree).

### 4. GitHub repo

Done — this is pushed to a private repo at `https://github.com/pushkar232007/trading-routine`,
with `origin/main` tracked. Remote routines clone this repo fresh on every run and push memory
updates back to `main`, so every future commit (made by you or by Bull) needs `git push`ed for
the next routine to see it.

### 5. Set up the cloud environment (API keys)

In the Claude Desktop app: **Routines → Environments → Add environment.** Name it something like
`trading`, give it network access, and set these environment variables (real values, not the
placeholders in `.env.example`):

- `ALPACA_API_KEY_ID`
- `ALPACA_API_SECRET_KEY`
- `ALPACA_BASE_URL` → `https://paper-api.alpaca.markets` to start
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

### 6. Create the 5 routines

For each file in `routines/`, create a routine in the Claude Desktop app:

| Routine | Cron (adjust timezone) | Prompt source |
|---|---|---|
| Pre-market | `0 6 * * 1-5` | `routines/pre-market.md` |
| Market open | `30 8 * * 1-5` | `routines/market-open.md` |
| Midday | `0 12 * * 1-5` | `routines/midday.md` |
| Close | `0 15 * * 1-5` | `routines/close.md` |
| Weekly review | `0 16 * * 5` | `routines/weekly-review.md` |

For each one: choose **Remote**, point it at the `trading` cloud environment, point it at this
GitHub repo, use Claude Opus (4.6/4.7, whichever you have access to), paste in the prompt from the
corresponding file, and set the cron schedule. Then in that routine's **Permissions**, turn on
**"allow unrestricted branch pushes"** so it can actually push memory updates back to `main`.

### 7. Test before trusting

Use **Run now** on each routine at least once and watch it execute. Read the conversation
transcript afterward — this is how the original creator caught bugs (e.g. credentials not where
expected). Only let it run unattended once you've watched a few cycles and you trust the
guardrails are being respected.

## Guardrails (enforced in `memory/strategy.md`, not just suggested)

- Paper trading until you explicitly flip the mode.
- Max 5% of equity per position.
- 10% trailing stop on every new buy.
- Cut any position down 7%+ at the midday check unless explicitly justified and logged.
- Max 3 new positions per week.
- Daily loss cap of 3% halts new positions for the rest of that day.
- No options, no margin/leverage, no shorting, no crypto.

Edit `memory/strategy.md` directly any time you want to change these — it's the single source of
truth the agent checks before every trade.
