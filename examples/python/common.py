"""Helpers for calling the hosted Actor; no scraping code."""
import json
import os
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from apify_client import ApifyClient

ACTOR_ID = "datascraperes/yellowpages-mobile-api-scraper"
API_ORIGIN = "https://api.apify.com"
REPOSITORY = Path(__file__).resolve().parents[2]


def client_from_env():
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before calling the hosted Actor.")
    return ApifyClient(token, max_retries=0, api_url=API_ORIGIN, api_public_url=API_ORIGIN)


def sample_input():
    return json.loads((REPOSITORY / "data/sample-input.json").read_text(encoding="utf-8"))


def run_and_collect(client, run_input, max_charge_usd="0.05"):
    query = urlencode({"timeout": 180, "maxTotalChargeUsd": max_charge_usd})
    request = Request(
        API_ORIGIN + "/v2/acts/" + ACTOR_ID.replace("/", "~") + "/runs?" + query,
        data=json.dumps(run_input).encode("utf-8"), method="POST",
        headers={"Authorization": "Bearer " + os.environ["APIFY_API_TOKEN"], "Content-Type": "application/json"},
    )
    try:
        # One start request. A lost response must not create a second paid run.
        with urlopen(request, timeout=30) as response:
            run_id = json.load(response)["data"]["id"]
        if not isinstance(run_id, str) or not run_id:
            raise ValueError("Missing run ID")
    except Exception:
        raise RuntimeError("Run creation could not be confirmed. Check existing Apify runs before repeating.") from None
    run = client.run(run_id).wait_for_finish(wait_duration=timedelta(seconds=210))
    if run is None or run.status != "SUCCEEDED":
        raise RuntimeError(f"Run {run_id} did not complete successfully; inspect that run before repeating.")
    record = client.key_value_store(run.default_key_value_store_id).get_record("RUN_SUMMARY")
    summary = (record or {}).get("value")
    if not isinstance(summary, dict) or not summary.get("complete") or summary.get("status") != "completed":
        raise RuntimeError(f"Run {run_id} is incomplete; inspect RUN_SUMMARY and its saved Dataset.")
    items = list(client.dataset(run.default_dataset_id).iterate_items(clean=True))
    return {"runId": run_id, "datasetId": run.default_dataset_id, "summary": summary, "items": items}
