# 🧰 Sales Engineering Toolkit

[![Node.js](https://img.shields.io/badge/node-%3E=18-brightgreen)](https://nodejs.org/)  
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)  
[![Postman](https://img.shields.io/badge/Postman-Collection-orange)](./postman/toolkit.postman_collection.json)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)  
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#-contributing)

A batteries-included toolkit for **Sales Engineers & Solutions Architects** to spin up demos, simulate integrations, and package POCs quickly.  
Perfect for showing **enterprise integrations**, **mock APIs**, and **data transformations** without waiting on production systems.

---

## 🚀 Quick Start

```bash
git clone https://github.com/<your-handle>/sales-engineering-toolkit.git
cd sales-engineering-toolkit

# Node / TypeScript tools
npm install
npm run dev:mock      # start mock API with chaos knobs
npm run dev:replay    # start webhook replayer
npm run check:latency # run latency probe

# Python helpers
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python env/env-wizard.py  # create a .env file

```

## 📂 Structure
``` bash
pgsql
Copy code
auth/        # JWTs, OIDC handshake
integrations/# webhooks, mock APIs, batch uploaders
data/        # seeding, conversion, redaction
ops/         # perf checks, uptime sentinels, log helpers
env/         # .env wizard + Postman sync
scaffolds/   # POC scaffolding + sandbox reset
postman/     # Postman collection & environment
``` 
## 🌟 Featured Scripts

🔐 Auth

1. jwt-mint.js → mint demo JWTs
2. oidc-handshake.py → tiny OIDC provider

🔗 Integrations

1. mock-api.ts → mock REST API w/ latency + error knobs
2. webhook-replay.ts → replay captured webhooks
3. event-batch-uploader.py → send NDJSON/CSV events



📊 Data

1. seed-demo-data.py → fake account/leads CSV
2. csv2json.py / sample-redact.py → safe transforms

⚙️ Ops

1. latency-check.ts → p50/p95/p99 table
2. la-sentinel.sh → uptime & SLA alerts → Slack
3. log-tail.sh → pretty-tail JSON logs

🧭 Env & Scaffolds

1. env-wizard.py → guided .env creation
2. scaffold-poc.sh → scaffold a new POC folder
3. reset-sandbox.sh → reset & reseed demo data


📑 Usage Examples
Mint a JWT:

``` bash
JWT_SECRET=supersecret node auth/jwt-mint.js user@acme.com acme 30m
Run webhook replayer:
```
``` bash
TARGETS="http://localhost:4000/hook" npm run dev:replay
Check endpoint latency:
```
``` bash
node ops/latency-check.ts https://api.example.com/health
🔌 Postman
Collection: postman/toolkit.postman_collection.json

Environment: postman/toolkit.postman_environment.json
```
## 🛠 Tech
1. Node.js 18+, TypeScript, Express
2. Python 3.10+, Faker, Requests, Dotenv
3. Postman for demo workflows

## 🗺 Roadmap
Planned additions:

1. SaaS quota & pricing simulator
2. gRPC mock server
3. Terraform demo scaffolds

Live Docker Compose setup

## 🤝 Contributing
Fork, tweak, and PR with new utilities!
Ideas: SaaS pricing simulator, gRPC mock server, Terraform demo scaffolds.

## 📅 Maintained by
Dominick Palma (@dompal25)
Solutions Architect / Sales Engineer
Helping enterprise clients integrate next-gen Martech solutions 🚀

📜 License
Distributed under the MIT License.
