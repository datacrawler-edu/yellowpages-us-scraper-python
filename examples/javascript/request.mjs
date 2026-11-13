import fs from 'node:fs/promises';

const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN before running this example.');
const base = 'https://api.apify.com/v2';
const input = JSON.parse(await fs.readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));
async function get(path) {
  const response = await fetch(base + path, { headers: { Authorization: `Bearer ${token}` }, signal: AbortSignal.timeout(30000) });
  if (!response.ok) throw new Error(`API read failed: ${response.status}. Inspect your existing run.`);
  return response.json();
}
// fetch has no automatic HTTP retry. If this start fails, inspect existing runs first.
const started = await fetch(base + '/acts/datascraperes~yellowpages-mobile-api-scraper/runs?timeout=180&maxTotalChargeUsd=0.05', {
  method: 'POST', headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
  body: JSON.stringify(input), signal: AbortSignal.timeout(30000),
});
if (!started.ok) throw new Error('Run creation failed. Check Apify runs before repeating.');
let run = (await started.json()).data;
if (!run?.id) throw new Error('Run ID unavailable. Check Apify runs before repeating.');
const deadline = Date.now() + 210000;
while (['READY', 'RUNNING', 'TIMING-OUT', 'ABORTING'].includes(run.status) && Date.now() < deadline) {
  await new Promise(resolve => setTimeout(resolve, 2000));
  run = (await get(`/actor-runs/${run.id}`)).data;
}
if (run.status !== 'SUCCEEDED') throw new Error(`Inspect run ${run.id}: ${run.status}`);
const summary = await get(`/key-value-stores/${run.defaultKeyValueStoreId}/records/RUN_SUMMARY`);
if (summary.status !== 'completed' || !summary.complete) throw new Error(`Inspect incomplete run ${run.id}`);
const items = [];
let offset = 0;
while (true) {
  const page = await get(`/datasets/${run.defaultDatasetId}/items?clean=true&offset=${offset}&limit=1000`);
  if (!Array.isArray(page)) throw new Error('Unexpected Dataset response');
  items.push(...page);
  offset += page.length;
  if (page.length < 1000) break;
}
console.log(JSON.stringify({ runId: run.id, datasetId: run.defaultDatasetId, items }, null, 2));
