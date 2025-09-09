#!/usr/bin/env python3
from getpass import getpass
import re, os
pairs = {
  "API_BASE_URL": r"^https?://",
  "API_KEY": r"^[A-Za-z0-9_\-]{16,}$",
  "JWT_SECRET": r"^.{12,}$"
}
out = []
for k, rx in pairs.items():
  while True:
    v = getpass(f"{k}: ")
    if re.match(rx, v): out.append(f"{k}={v}"); break
    print(f"Invalid {k} format. Try again.")
open(".env","w").write("\n".join(out)+"\n")
print("Wrote .env (values hidden).")
