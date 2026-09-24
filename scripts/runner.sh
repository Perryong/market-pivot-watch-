#!/usr/bin/env bash
# One analysis run: engine -> AI analysis -> auto-publish (git push + telegram).
set -euo pipefail
cd /home/pi/code/market-pivot-watch
mkdir -p logs
exec >> logs/runner.log 2>&1

set -a
source .env
set +a

echo "[runner] engine run $(date -Is)"
python3 -m pivot_watch --config config.json --state .state/state.json --out output || true

echo "[runner] ai analysis $(date -Is)"
python3 -m pivot_watch.ai_analysis --out output || true

echo "[runner] auto-publish $(date -Is)"
python3 scripts/market_bot.py publish || true
