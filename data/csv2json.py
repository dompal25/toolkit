#!/usr/bin/env python3
import sys, csv, json
if len(sys.argv) < 3:
    print("usage: csv2json.py input.csv output.json"); sys.exit(1)
with open(sys.argv[1]) as f, open(sys.argv[2], "w") as out:
    reader = csv.DictReader(f)
    json.dump(list(reader), out, indent=2)
