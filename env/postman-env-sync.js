import fs from "fs";

const envPath = ".env";
const outPath = "postman/toolkit.postman_environment.json";
const content = fs.readFileSync(envPath, "utf8").split(/\r?\n/).filter(Boolean);
const values = content.map(line => {
  const [key, ...rest] = line.split("=");
  return { key, value: rest.join("="), enabled: true };
});
const env = {
  id: "toolkit-env",
  name: "Toolkit Env",
  values,
  _postman_variable_scope: "environment",
  _postman_exported_at: new Date().toISOString(),
  _postman_exported_using: "postman-collection"
};
fs.mkdirSync("postman", { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(env, null, 2));
console.log("Wrote", outPath);
