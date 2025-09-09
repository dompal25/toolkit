import http from "http";
import fetch from "node-fetch";

const PORT = Number(process.env.PORT || 9000);
const targets = (process.env.TARGETS || "http://localhost:3000/webhook").split(",");
const jitterMs = Number(process.env.JITTER_MS || 0);

http.createServer(async (req, res) => {
  if (req.method !== "POST") { res.writeHead(405); return res.end(); }
  let body = "";
  req.on("data", chunk => body += chunk);
  req.on("end", async () => {
    for (const t of targets) {
      const delay = jitterMs ? Math.random() * jitterMs : 0;
      setTimeout(() => {
        fetch(t, { method: "POST", headers: { "Content-Type":"application/json" }, body })
          .then(r => console.log(`→ ${t} ${r.status}`))
          .catch(e => console.error(`× ${t} ${e.message}`));
      }, delay);
    }
    res.end("ok");
  });
}).listen(PORT, () => console.log(`Replay listening on :${PORT}`));
