#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os, urllib.parse

PORT = int(os.environ.get("PORT", "8888"))
CLIENT_ID = os.environ.get("OIDC_CLIENT_ID", "demo-client")
REDIRECT_URI = os.environ.get("OIDC_REDIRECT_URI", "http://localhost:3000/callback")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/authorize"):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            code = "demo-code-123"
            redir = q.get("redirect_uri", [REDIRECT_URI])[0]
            self.send_response(302)
            self.send_header("Location", f"{redir}?code={code}&state={q.get('state',[''])[0]}")
            self.end_headers()
        elif self.path.startswith("/.well-known/openid-configuration"):
            self.send_json({
              "authorization_endpoint": f"http://localhost:{PORT}/authorize",
              "token_endpoint": f"http://localhost:{PORT}/token"
            })
        else:
            self.send_json({"ok": True})

    def do_POST(self):
        if self.path == "/token":
            self.send_json({"access_token":"fake-access","id_token":"fake-id","token_type":"Bearer","expires_in":900})
        else:
            self.send_json({"ok": True})

    def send_json(self, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", PORT), H).serve_forever()
