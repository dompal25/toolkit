#!/usr/bin/env bash
set -euo pipefail
NAME="${1:-poc-demo}"
mkdir -p "$NAME"/{src,docs}
cat > "$NAME/README.md" <<EOF
# $NAME
Problem → Solution → Tech → Usage → Screenshots

## Setup
- Copy ../.env.example to .env and fill values
- Run locally with Docker or Node
EOF
cp -r ../postman "$NAME/postman" 2>/dev/null || true
echo "Scaffolded $NAME/"
