#!/usr/bin/env bash
# One analysis run: engine -> AI analysis -> review draft. No push, no broadcast.
set -euo pipefail
cd /home/pi/code/market-pivot-watch

set -a
source .env
set +a

echo "[runner] engine run $(date -Is)"
python3 -m pivot_watch --config config.json --state .state/state.json --out output || true

echo "[runner] ai analysis $(date -Is)"
python3 -m pivot_watch.ai_analysis --out output || true

echo "[runner] sending review draft $(date -Is)"
python3 scripts/market_bot.py draft || true
