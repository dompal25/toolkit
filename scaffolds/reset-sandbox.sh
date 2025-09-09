#!/usr/bin/env bash
set -euo pipefail
echo "Resetting local sandbox..."
rm -f seed_accounts.csv
python data/seed-demo-data.py
echo "Re-seeded CSV and ready for upload."
