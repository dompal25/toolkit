#!/usr/bin/env python3
import sys, time, json, requests, os
from dotenv import load_dotenv
load_dotenv()

API = os.getenv("API_BASE_URL", "http://localhost:8080")
KEY = os.getenv("API_KEY", "dev-key")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def main(path):
    with open(path) as f:
        data = [json.loads(line) for line in f]
    for batch in chunks(data, 100):
        r = requests.post(f"{API}/events", headers={"Authorization": f"Bearer {KEY}"}, json=batch, timeout=10)
        print("POST /events", r.status_code, r.text[:120])
        time.sleep(0.1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: event-batch-uploader.py events.ndjson"); sys.exit(1)
    main(sys.argv[1])
