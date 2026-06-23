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

Done — pushed to `https://github.com/pushkar232007/trading-routine`, with `origin/main` tracked.

This repo is **public**, not private. We tried private first, but as of now Claude Desktop's
repository picker for Routines doesn't surface private repos for this account even with the
GitHub App correctly configured for private-repo access — public was the only way to get the
repo to show up when creating a routine. Since trading starts in **paper mode** (fake money), the
exposure is low for now — but before ever flipping `TRADING_MODE` to `live`, revisit this, since
trade-log/portfolio data would then reveal real position sizes and balances publicly.

### 5. The git-push workaround (read this — it's not optional)

Claude Code Routines' built-in GitHub integration is **read-only for git operations** — `git push`
and the GitHub API both fail with 403 / "Resource not accessible by integration," regardless of
the routine's "Allow unrestricted git push" permission toggle (that toggle governs branch
namespace, not the actual write scope). This is a current architectural limitation of Routines,
not something fixable via settings, and it affects every plan tier.

**Workaround: a GitHub Personal Access Token (PAT), passed as an env var, used to authenticate
the push directly — bypassing the built-in integration entirely.**

1. Go to `https://github.com/settings/personal-access-tokens/new` (fine-grained tokens).
2. Name it something like `trading-routine-push`.
3. Resource owner: your account. Repository access: **"Only select repositories"** → choose
   `trading-routine`.
4. Permissions → Repository permissions → **Contents: Read and write**.
5. Generate, copy the token (starts with `github_pat_...`) — you'll only see it once.

`CLAUDE.md` already has the corresponding push command wired in
(`git push https://${GH_TOKEN}@github.com/pushkar232007/trading-routine.git HEAD:main`), so you
just need to supply the token as an env var — no per-routine prompt edits needed.

### 6. Set up the cloud environment (API keys)

In the Claude Desktop app: **Routines → Environments → Add environment.** Name it something like
`trading`, give it network access, and set these environment variables (real values, not the
placeholders in `.env.example`):

- `ALPACA_API_KEY_ID`
- `ALPACA_API_SECRET_KEY`
- `ALPACA_BASE_URL` → `https://paper-api.alpaca.markets` to start
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `GH_TOKEN` → the fine-grained PAT from step 5

### 7. Create the 5 routines

Claude Desktop's cron field is evaluated in **UTC**, not your local timezone (it shows a local-time
preview after you click away, which is handy for sanity-checking but isn't what you type). These
UTC cron values map to NYSE pre-market/open/midday/close while the US is on Daylight Time (EDT,
UTC-4, roughly mid-March to early November); shift every value 1 hour earlier in UTC once the US
falls back to Standard Time (EST, UTC-5) in November:

| Routine | NYSE-local time | UTC cron | Prompt source |
|---|---|---|---|
| Pre-market | 7:00 AM ET | `0 11 * * 1-5` | `routines/pre-market.md` |
| Market open | 9:30 AM ET | `30 13 * * 1-5` | `routines/market-open.md` |
| Midday | 1:00 PM ET | `0 17 * * 1-5` | `routines/midday.md` |
| Close | 4:00 PM ET | `0 20 * * 1-5` | `routines/close.md` |
| Weekly review | 5:00 PM ET Friday | `0 21 * * 5` | `routines/weekly-review.md` |

For each one: choose **Cloud** (not Local — Local only runs while your computer is on), point it
at the `trading` cloud environment, point it at this GitHub repo (defaults to branch `main`), use
an Opus model, paste in the prompt from the corresponding file, and set the cron schedule. Then in
that routine's **Permissions** tab, turn on **"Allow unrestricted git push."** (This alone won't
fix the read-only GitHub integration issue from step 5 — you still need `GH_TOKEN` — but leave it
on anyway since `CLAUDE.md` assumes it.)

### 8. Test before trusting

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
