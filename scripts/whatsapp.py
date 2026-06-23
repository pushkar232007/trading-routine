#!/usr/bin/env python3
"""Send a WhatsApp notification via CallMeBot.

Setup (one-time, by the human, not the agent):
1. Save the CallMeBot number in your phone contacts: +34 644 51 95 23
2. Send it this WhatsApp message: "I allow callmebot to send me messages"
3. CallMeBot replies with your personal API key.
4. Set env vars in the Claude Code routine's cloud environment:
       CALLMEBOT_PHONE   (your WhatsApp number, international format, e.g. 15551234567)
       CALLMEBOT_APIKEY  (the key CallMeBot sent you)

Usage:
    python3 scripts/whatsapp.py "Market closed. Portfolio +1.2% today, S&P +0.8%."
"""
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://api.callmebot.com/whatsapp.php"


def _env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(
            f"Missing required environment variable: {name}\n"
            "Set it in the Claude Code routine's cloud environment, not in a .env file."
        )
    return value


def send(message: str) -> str:
    params = {
        "phone": _env("CALLMEBOT_PHONE"),
        "text": message,
        "apikey": _env("CALLMEBOT_APIKEY"),
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read().decode()
    except urllib.error.HTTPError as e:
        sys.exit(f"CallMeBot API error {e.code}: {e.read().decode()}")


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 scripts/whatsapp.py "<message>"')
    print(send(sys.argv[1]))


if __name__ == "__main__":
    main()
