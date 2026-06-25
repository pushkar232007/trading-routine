#!/usr/bin/env python3
"""Thin CLI wrapper around the Alpaca Trading + Market Data REST APIs.

Reads credentials from environment variables (set in the Claude Code routine's
cloud environment, never from a .env file):

    ALPACA_API_KEY_ID
    ALPACA_API_SECRET_KEY
    ALPACA_BASE_URL      e.g. https://paper-api.alpaca.markets

Usage:
    python3 scripts/alpaca.py account
    python3 scripts/alpaca.py positions
    python3 scripts/alpaca.py orders [--status open|closed|all]
    python3 scripts/alpaca.py clock
    python3 scripts/alpaca.py quote SYMBOL
    python3 scripts/alpaca.py buy SYMBOL QTY [--trail-percent 10]
    python3 scripts/alpaca.py sell SYMBOL QTY
    python3 scripts/alpaca.py close SYMBOL
    python3 scripts/alpaca.py cancel-all
    python3 scripts/alpaca.py tighten-stop SYMBOL NEW_TRAIL_PERCENT
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DATA_BASE_URL = "https://data.alpaca.markets"


def _env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(
            f"Missing required environment variable: {name}\n"
            "Set it in the Claude Code routine's cloud environment "
            "(Claude Desktop app -> routine -> environment), not in a .env file."
        )
    return value


def _headers():
    return {
        "APCA-API-KEY-ID": _env("ALPACA_API_KEY_ID"),
        "APCA-API-SECRET-KEY": _env("ALPACA_API_SECRET_KEY"),
        "Content-Type": "application/json",
    }


def _request(method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=_headers())
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode() or "null")
    except urllib.error.HTTPError as e:
        detail = e.read().decode()
        sys.exit(f"Alpaca API error {e.code} on {method} {url}: {detail}")


def trading_url(path):
    base = _env("ALPACA_BASE_URL").rstrip("/")
    return f"{base}{path}"


def cmd_account(_args):
    print(json.dumps(_request("GET", trading_url("/v2/account")), indent=2))


def cmd_positions(_args):
    print(json.dumps(_request("GET", trading_url("/v2/positions")), indent=2))


def cmd_orders(args):
    status = args.status or "open"
    qs = urllib.parse.urlencode({"status": status})
    print(json.dumps(_request("GET", trading_url(f"/v2/orders?{qs}")), indent=2))


def cmd_clock(_args):
    print(json.dumps(_request("GET", trading_url("/v2/clock")), indent=2))


def cmd_quote(args):
    url = f"{DATA_BASE_URL}/v2/stocks/{args.symbol.upper()}/quotes/latest"
    print(json.dumps(_request("GET", url), indent=2))


def _wait_for_fill(order_id, timeout=15, interval=0.5):
    """Poll an order until it fills. A market buy must actually fill before a
    trailing-stop sell can be submitted, or Alpaca rejects the stop leg as a
    naked short (seen in practice on 2026-06-24)."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        order = _request("GET", trading_url(f"/v2/orders/{order_id}"))
        if order.get("status") == "filled":
            return order
        if order.get("status") in ("canceled", "expired", "rejected"):
            sys.exit(f"Buy order {order_id} did not fill: status={order.get('status')}")
        time.sleep(interval)
    sys.exit(
        f"Buy order {order_id} did not fill within {timeout}s (still pending). "
        "Run `python3 scripts/alpaca.py positions` to check manually — if the buy did fill, "
        "resubmit just the trailing-stop sell leg for the same symbol/qty."
    )


def cmd_buy(args):
    order = {
        "symbol": args.symbol.upper(),
        "qty": str(args.qty),
        "side": "buy",
        "type": "market",
        "time_in_force": "day",
    }
    result = _request("POST", trading_url("/v2/orders"), order)

    if args.trail_percent:
        filled = _wait_for_fill(result["id"])
        print(json.dumps(filled, indent=2))
        stop_order = {
            "symbol": args.symbol.upper(),
            "qty": str(args.qty),
            "side": "sell",
            "type": "trailing_stop",
            "trail_percent": str(args.trail_percent),
            "time_in_force": "gtc",
        }
        stop_result = _request("POST", trading_url("/v2/orders"), stop_order)
        print(json.dumps(stop_result, indent=2))
    else:
        print(json.dumps(result, indent=2))


def cmd_sell(args):
    order = {
        "symbol": args.symbol.upper(),
        "qty": str(args.qty),
        "side": "sell",
        "type": "market",
        "time_in_force": "day",
    }
    print(json.dumps(_request("POST", trading_url("/v2/orders"), order), indent=2))


def cmd_close(args):
    print(json.dumps(_request("DELETE", trading_url(f"/v2/positions/{args.symbol.upper()}")), indent=2))


def cmd_cancel_all(_args):
    print(json.dumps(_request("DELETE", trading_url("/v2/orders")), indent=2))


def cmd_tighten_stop(args):
    qs = urllib.parse.urlencode({"status": "open", "symbols": args.symbol.upper()})
    open_orders = _request("GET", trading_url(f"/v2/orders?{qs}"))
    stop_orders = [o for o in open_orders if o.get("type") == "trailing_stop" and o.get("side") == "sell"]
    if not stop_orders:
        sys.exit(f"No open trailing stop order found for {args.symbol.upper()}")
    order_id = stop_orders[0]["id"]
    result = _request("PATCH", trading_url(f"/v2/orders/{order_id}"), {"trail": str(args.trail_percent)})
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("account").set_defaults(func=cmd_account)
    sub.add_parser("positions").set_defaults(func=cmd_positions)

    p = sub.add_parser("orders")
    p.add_argument("--status", choices=["open", "closed", "all"], default="open")
    p.set_defaults(func=cmd_orders)

    sub.add_parser("clock").set_defaults(func=cmd_clock)

    p = sub.add_parser("quote")
    p.add_argument("symbol")
    p.set_defaults(func=cmd_quote)

    p = sub.add_parser("buy")
    p.add_argument("symbol")
    p.add_argument("qty", type=float)
    p.add_argument("--trail-percent", type=float, default=None)
    p.set_defaults(func=cmd_buy)

    p = sub.add_parser("sell")
    p.add_argument("symbol")
    p.add_argument("qty", type=float)
    p.set_defaults(func=cmd_sell)

    p = sub.add_parser("close")
    p.add_argument("symbol")
    p.set_defaults(func=cmd_close)

    sub.add_parser("cancel-all").set_defaults(func=cmd_cancel_all)

    p = sub.add_parser("tighten-stop")
    p.add_argument("symbol")
    p.add_argument("trail_percent", type=float)
    p.set_defaults(func=cmd_tighten_stop)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
