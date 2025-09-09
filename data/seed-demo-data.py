#!/usr/bin/env python3
import csv, os, random
from faker import Faker
fake = Faker()

rows = []
for i in range(100):
    rows.append({
        "account_id": f"acct_{i:04d}",
        "company": fake.company(),
        "email": fake.unique.email(),
        "country": fake.country(),
        "plan": random.choice(["free","pro","enterprise"]),
        "mrr": random.choice([0,49,199,999])
    })

with open("seed_accounts.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print("Wrote seed_accounts.csv")
