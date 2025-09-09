import jwt from "jsonwebtoken";

const payload = {
  sub: process.argv[2] || "demo-user@acme.com",
  org: process.argv[3] || "acme",
  roles: ["admin"],
};
const expiresIn = process.argv[4] || "15m";
const secret = process.env.JWT_SECRET || "dev-secret";

const token = jwt.sign(payload, secret, { algorithm: "HS256", expiresIn });
console.log(token);
