"""Read-only official market-data endpoints. No trading methods or stored secrets."""
from datetime import datetime, timezone
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request

from .core import Candle, DataError, H1, H4, aggregate_hours, number


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def iso(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat().replace("+00:00", "Z")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise DataError("Unexpected provider redirect; request stopped")


def get_json(url, params=None, headers=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "pivot-watch/1.0", "Accept": "application/json", **(headers or {})})
    opener = urllib.request.build_opener(NoRedirect())
    for attempt in range(3):
        try:
            with opener.open(request, timeout=20) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            # Never include a response body, account URL, bearer token or raw exception.
            raise DataError(f"Provider HTTP {exc.code}; check entitlement, region and rate limits") from None
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise DataError("Provider connection unavailable after 3 attempts") from None
        except (json.JSONDecodeError, UnicodeError):
            raise DataError("Provider returned invalid JSON") from None


def quote(price, when, now):
    when = float(when)
    if not -60 <= now - when <= 900:
        raise DataError("Quote is stale or has a future timestamp")
    return {"price": number(price), "time": when}


def parse_oanda(payload, duration=H4):
    bars = []
    for c in payload["candles"]:
        if not isinstance(c["complete"], bool):
            raise DataError("OANDA completion flag is not boolean")
        p = c["mid"]
        bars.append(Candle(int(timestamp(c["time"])), *(number(p[k]) for k in ("o", "h", "l", "c")), c["complete"], duration))
    return bars


def parse_binance(rows, now, duration=H4):
    bars = []
    for row in rows:
        start = int(row[0]) // 1000
        if int(row[6]) + 1 != (start + duration) * 1000:
            raise DataError("Binance candle duration does not match requested timeframe")
        bars.append(Candle(start, *(number(x) for x in row[1:5]), start + duration <= now, duration))
    return bars


def fetch(config, now, include_hourly=False):
    provider, symbol = config["provider"], config["symbol"]
    safe_symbol = urllib.parse.quote(symbol, safe="")
    if provider == "coinbase":
        base = f"https://api.exchange.coinbase.com/products/{safe_symbol}"
        # 280 hours <= Coinbase's 300 bucket limit. Filter active and partial buckets.
        end = int(now) // 3600 * 3600
        rows = get_json(base + "/candles", {"granularity": 3600, "start": iso(end - 280 * 3600), "end": iso(end)})
        bars = aggregate_hours(rows, now)
        ticker = get_json(base + "/ticker")
        q = quote(ticker["price"], timestamp(ticker["time"]), now)
        stats = get_json(base + "/stats")
        low, high = number(stats["low"]), number(stats["high"])
        range_label = "Provider rolling 24h range (retrieved at check time)"
        sources = [base + "/candles", base + "/ticker", base + "/stats"]
    elif provider == "binance":
        base = "https://data-api.binance.vision/api/v3"
        bars = parse_binance(get_json(base + "/klines", {"symbol": symbol, "interval": "4h", "limit": 200}), now)
        ticker = get_json(base + "/ticker/24hr", {"symbol": symbol})
        q = quote(ticker["lastPrice"], ticker["closeTime"] / 1000, now)
        low, high = number(ticker["lowPrice"]), number(ticker["highPrice"])
        range_label = "Provider rolling 24h range"
        sources = [base + "/klines?symbol=" + safe_symbol + "&interval=4h&limit=200", base + "/ticker/24hr?symbol=" + safe_symbol]
    elif provider == "oanda":
        token, account = os.getenv("OANDA_TOKEN"), os.getenv("OANDA_ACCOUNT_ID")
        if not token or not account:
            raise DataError("Set GitHub Secrets OANDA_TOKEN and OANDA_ACCOUNT_ID; OANDA access is not configured")
        env = config.get("environment", "practice")
        if env not in ("practice", "live"):
            raise DataError("OANDA environment must be practice or live")
        base = "https://api-fxpractice.oanda.com" if env == "practice" else "https://api-fxtrade.oanda.com"
        headers = {"Authorization": "Bearer " + token}
        payload = get_json(base + f"/v3/instruments/{safe_symbol}/candles",
            {"granularity": "H4", "price": "M", "count": 200, "dailyAlignment": 0,
             "alignmentTimezone": "UTC", "smooth": "false"}, headers)
        bars = parse_oanda(payload)
        prices = get_json(base + "/v3/accounts/" + urllib.parse.quote(account, safe="") + "/pricing",
                          {"instruments": symbol}, headers)["prices"]
        price = next((p for p in prices if p["instrument"] == symbol), None)
        if not price or price.get("status") != "tradeable":
            raise DataError("OANDA market closed or instrument not tradeable; no current signal")
        q = quote((number(price["bids"][0]["price"]) + number(price["asks"][0]["price"])) / 2,
                  timestamp(price["time"]), now)
        completed = sorted([c for c in bars if c.complete and c.end <= now], key=lambda c: c.start)
        window = completed[-6:]
        if len(window) != 6:
            raise DataError("Six completed OANDA candles are unavailable for the display range")
        low, high = min(c.low for c in window), max(c.high for c in window)
        elapsed_hours = (window[-1].end - window[0].start) / 3600
        range_label = (f"Last six completed 4H candles, {iso(window[0].start)} to {iso(window[-1].end)} "
                       f"({elapsed_hours:g}h elapsed; gaps not filled; not rolling live 24h)")
        sources = ["https://developer.oanda.com/rest-live-v20/instrument-df/", "https://developer.oanda.com/rest-live-v20/pricing-ep/"]
    else:
        raise DataError("Unknown market-data provider")
    if low > high:
        raise DataError("Invalid market range")
    result = {"candles": bars, "quote": q, "low": low, "high": high, "range_label": range_label,
              "source": provider, "sources": sources}
    if include_hourly:
        try:
            if provider == 'coinbase':
                hourly = [Candle(int(r[0]), *(number(r[i]) for i in (3, 2, 1, 4)),
                                int(r[0]) + H1 <= now, H1) for r in rows]
            elif provider == 'binance':
                hourly = parse_binance(get_json(base + '/klines',
                    {'symbol': symbol, 'interval': '1h', 'limit': 200}), now, H1)
            else:
                hourly = parse_oanda(get_json(base + f'/v3/instruments/{safe_symbol}/candles',
                    {'granularity': 'H1', 'price': 'M', 'count': 200, 'dailyAlignment': 0,
                     'alignmentTimezone': 'UTC', 'smooth': 'false'}, headers), H1)
            hourly = sorted((c for c in hourly if c.complete and c.end <= now), key=lambda c: c.start)
            for c in hourly:
                c.validate()
            if len({c.start for c in hourly}) != len(hourly):
                raise DataError('Duplicate hourly candles')
            result['hourly_candles'] = hourly
        except (DataError, KeyError, TypeError, ValueError, IndexError):
            result['hourly_error'] = 'Hourly provider data unavailable or invalid'
    return result


def fetch_review_bars(config, since, until):
    """Complete M5 bars strictly inside the observation window; never fill gaps."""
    start, end = math.ceil(since / 300) * 300, int(until) // 300 * 300
    # ponytail: review windows capped at 24h; paginate if multi-day reviews become necessary.
    if not 0 < end - start <= 86400:
        raise DataError('Review needs a window with complete M5 bars, at most 24 hours')
    symbol = urllib.parse.quote(config['symbol'], safe='')
    provider = config['provider']
    if provider == 'coinbase':
        rows = get_json(f'https://api.exchange.coinbase.com/products/{symbol}/candles',
                        {'granularity': 300, 'start': iso(start), 'end': iso(end)})
        values = [(r[0], r[3], r[2], r[1], r[4]) for r in rows]
    elif provider == 'binance':
        rows = get_json('https://data-api.binance.vision/api/v3/klines',
                        {'symbol': config['symbol'], 'interval': '5m', 'startTime': start*1000,
                         'endTime': end*1000-1, 'limit': 1000})
        if any(int(r[6])+1 != int(r[0])+300000 for r in rows):
            raise DataError('Invalid M5 candle duration')
        values = [(int(r[0])/1000, *r[1:5]) for r in rows]
    elif provider == 'oanda':
        token = os.getenv('OANDA_TOKEN')
        env = config.get('environment', 'practice')
        if not token or env not in ('practice', 'live'):
            raise DataError('OANDA review access is not configured')
        host = 'api-fxpractice.oanda.com' if env == 'practice' else 'api-fxtrade.oanda.com'
        rows = get_json(f'https://{host}/v3/instruments/{symbol}/candles',
                        {'granularity': 'M5', 'price': 'M', 'from': iso(start), 'to': iso(end), 'smooth': 'false'},
                        {'Authorization': 'Bearer ' + token})['candles']
        if any(not isinstance(r['complete'], bool) for r in rows):
            raise DataError('Invalid OANDA completion flag')
        values = [(timestamp(r['time']), *(r['mid'][k] for k in ('o', 'h', 'l', 'c')))
                  for r in rows if r['complete']]
    else:
        raise DataError('Unknown review provider')
    bars = []
    for when, op, high, low, close in values:
        if not start <= when < end:
            continue
        if when % 300:
            raise DataError('Misaligned M5 candle')
        op, high, low, close = map(number, (op, high, low, close))
        if not low <= min(op, close) <= max(op, close) <= high:
            raise DataError('Invalid M5 OHLC')
        bars.append(dict(start=int(when), end=int(when)+300, open=op, high=high, low=low, close=close))
    bars.sort(key=lambda bar: bar['start'])
    if [bar['start'] for bar in bars] != list(range(start, end, 300)):
        raise DataError('Missing or duplicate M5 bars; review coverage is incomplete')
    return bars
