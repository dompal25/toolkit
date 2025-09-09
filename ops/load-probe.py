#!/usr/bin/env python3
import sys, time, requests, statistics

if len(sys.argv) < 3:
    print("usage: load-probe.py <url> <rps> [seconds]"); sys.exit(1)

url, rps = sys.argv[1], float(sys.argv[2])
seconds = int(sys.argv[3]) if len(sys.argv) > 3 else 10

latencies = []
end = time.time() + seconds
while time.time() < end:
    t0 = time.time()
    try:
        requests.get(url, timeout=5)
    except Exception:
        pass
    latencies.append((time.time()-t0)*1000)
    sleep = max(0, 1.0/rps - (time.time()-t0))
    time.sleep(sleep)

print("p50:", statistics.median(latencies))
print("count:", len(latencies))
