#!/usr/bin/env bash
# Approval poller: watches the bot for Approve/Reject button presses.
set -euo pipefail
cd /home/pi/code/market-pivot-watch

set -a
source .env
set +a

exec python3 scripts/market_bot.py serve
