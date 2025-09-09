
# Sales Engineering Toolkit

A batteries-included toolkit to spin up demos, simulate integrations, and package POCs quickly.

## Quick Start

```bash
git clone <your-fork-url> sales-engineering-toolkit
cd sales-engineering-toolkit

# Node / TS tools
npm install
npm run dev:mock          # start mock API with chaos knobs
npm run dev:replay        # start webhook replayer
npm run check:latency     # sample latency run

# Python tools
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python env/env-wizard.py  # create a .env from prompts
```

### Structure
```
auth/        # JWTs, OIDC handshake
integrations/# webhooks, mock APIs, batch uploaders
data/        # seeding, conversion, redaction
ops/         # perf checks, uptime sentinels, log helpers
env/         # .env wizard + Postman sync
scaffolds/   # POC scaffolding + sandbox reset
postman/     # collection & env template
```

### Featured Scripts
- **Auth**: `jwt-mint.js`, `oidc-handshake.py`
- **Integrations**: `mock-api.ts`, `webhook-replay.ts`, `event-batch-uploader.py`
- **Data**: `seed-demo-data.py`, `csv2json.py`, `sample-redact.py`
- **Ops**: `latency-check.ts`, `load-probe.py`, `sla-sentinel.sh`, `log-tail.sh`
- **Env**: `env-wizard.py`, `postman-env-sync.js`
- **Scaffolds**: `scaffold-poc.sh`, `reset-sandbox.sh`

### Demo
- `npm run dev:mock` → `http://localhost:8080/campaigns/123`
- `npm run dev:replay` → POST any JSON to `http://localhost:9000` and it will forward to your targets.

---

**Created:** 2025-09-09
```

