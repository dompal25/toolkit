import fetch from "node-fetch";

const urls = process.argv.slice(2);
if (!urls.length) {
  console.error("usage: node ops/latency-check.ts <url1> <url2> ...");
  process.exit(1);
}

function percentile(arr:number[], p:number){ 
  const idx = Math.floor(p * arr.length);
  return arr[Math.min(idx, arr.length-1)];
}

(async () => {
  const timings:any[] = [];
  for (const url of urls) {
    const samples:number[] = [];
    for (let i=0; i<10; i++) {
      const t0 = Date.now();
      try { await fetch(url); } catch {}
      samples.push(Date.now() - t0);
    }
    samples.sort((a,b)=>a-b);
    timings.push({ url, p50:percentile(samples,0.5), p95:percentile(samples,0.95), p99:percentile(samples,0.99) });
  }
  console.log("| URL | p50 (ms) | p95 | p99 |\n|---|---:|---:|---:|");
  timings.forEach(t => console.log(`| ${t.url} | ${t.p50} | ${t.p95} | ${t.p99} |`));
})();
