#!/usr/bin/env python3
import sys, json, re, hashlib

def det_fake_email(email):
    sha = hashlib.sha256(email.encode()).hexdigest()[:8]
    return f"user_{sha}@example.com"

if len(sys.argv) < 3:
    print("usage: sample-redact.py in.json out.json"); sys.exit(1)

with open(sys.argv[1]) as f: data = json.load(f)
for row in data:
    if "email" in row:
        row["email"] = det_fake_email(row["email"])
    if "name" in row:
        row["name"] = "REDACTED"

with open(sys.argv[2], "w") as out:
    json.dump(data, out, indent=2)
