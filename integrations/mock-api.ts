import express from "express";
const app = express(); app.use(express.json());

const chaos = {
  latencyMs: Number(process.env.LATENCY_MS || 120),
  errorRate: Number(process.env.ERROR_RATE || 0.05)
};

app.get("/health", (_req, res) => res.json({ ok: true }));

app.get("/campaigns/:id", (req, res) => {
  setTimeout(() => {
    if (Math.random() < chaos.errorRate) return res.status(503).json({ error: "upstream timeout" });
    res.json({ id: req.params.id, name: "Fall Promo", status: "active" });
  }, chaos.latencyMs);
});

app.post("/events", (req, res) => setTimeout(() => res.status(202).json({ accepted: (req.body || []).length || 1 }), chaos.latencyMs));

app.listen(8080, () => console.log("Mock API on :8080"));
