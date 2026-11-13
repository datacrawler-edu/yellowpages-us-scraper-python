# Start one hosted search with cURL

Run from the repository root after setting `APIFY_API_TOKEN`. This creates a potentially paid run, once. Do not add an automatic retry to the start request.

```bash
curl --fail-with-body --max-time 30 --request POST \
  'https://api.apify.com/v2/acts/datascraperes~yellowpages-mobile-api-scraper/runs?timeout=180&maxTotalChargeUsd=0.05' \
  --header "Authorization: Bearer $APIFY_API_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-binary @data/sample-input.json --output run.json
```

Read `data.id` from `run.json`. Check that run in Apify before repeating if creation times out or its response is lost. Read `GET /v2/actor-runs/RUN_ID` until terminal; use the same Authorization header. After SUCCEEDED, read `RUN_SUMMARY` from the returned `defaultKeyValueStoreId` and require `complete=true`, then export `/v2/datasets/DATASET_ID/items`. The Python and JavaScript examples implement waiting and paginated retrieval.
