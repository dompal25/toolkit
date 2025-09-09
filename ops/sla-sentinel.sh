#!/usr/bin/env bash
set -euo pipefail
URL="${1:-https://httpbin.org/status/200}"
THRESH="${2:-500}" # ms threshold
SLACK="${SLACK_WEBHOOK_URL:-}"
t0=$(date +%s%3N)
code=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
t1=$(date +%s%3N); dt=$((t1 - t0))
echo "code=$code latency_ms=$dt"
if [[ "$dt" -gt "$THRESH" || "$code" -ge 500 ]]; then
  msg="SLA breach: $URL code=$code latency_ms=$dt"
  echo "$msg"
  if [[ -n "$SLACK" ]]; then
    curl -s -X POST -H "Content-type: application/json" --data "{"text":"$msg"}" "$SLACK" >/dev/null
  fi
fi
