#!/usr/bin/env bash
# Approval poller: watches the bot for Approve/Reject button presses.
set -euo pipefail
cd /home/pi/code/market-pivot-watch
mkdir -p logs

set -a
source .env
set +a

exec python3 scripts/market_bot.py serve >> logs/approve.log 2>&1
