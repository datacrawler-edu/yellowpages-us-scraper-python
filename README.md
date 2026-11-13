# Yellow Pages US scraper: Python API examples and CSV export

Use the hosted **Yellow Pages US Scraper** to search business categories in US cities, retrieve contact details and optionally collect reviews and photo URLs. This repository is a practical integration guide, not the scraper source.

[Open Yellow Pages US on Apify](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata)

## What this repository helps you do

- Run a small business search from Python, JavaScript or cURL.
- Process several cities sequentially with a separate spending cap per run.
- Export an existing Dataset into a contact spreadsheet without starting another collection.
- Understand missing values and partial coverage before using the data.

## Example result

This excerpt shows a real business row. The complete representative record is in [sample-output.json](data/sample-output.json); [sample-output.csv](data/sample-output.csv) is a contact-column projection. The sample has no reviews because that business returned none, not because review support is disabled.

```json
{
  "ypid": "473194899",
  "name": "ARS Rescue Rooter",
  "phone": "(833) 947-9225",
  "city": "Austin",
  "state": "TX",
  "website": null,
  "detailStatus": "ok"
}
```

## Run without code

1. Open the [hosted Actor](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata).
2. Enter business types and US locations in **Input**.
3. Choose a small result limit and optional review/photo caps, then click **Start**.
4. Check the run summary and business statuses, then export from **Dataset**.

See the [no-code guide](docs/no-code-guide.md). No Python setup is needed for this route.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage**, with no credit card required to start. Available credit can cover a small test; this is not unlimited free use. Unused credits expire rather than rolling over. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) and your remaining usage before a larger batch.

## Quick start for developers

Use Python 3.11 or newer:

```bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/yellowpages_businesses.py
```

PowerShell token setup: `$env:APIFY_API_TOKEN = "your-token"`. The Python example uses pinned `apify-client==3.5.1` for reads/waiting and sends run creation once. If creation is interrupted, inspect existing runs before repeating. A successful platform status alone is insufficient: examples also require a complete run summary.

## Input example

```json
{
  "searchTerms": [
    "plumbers"
  ],
  "locations": [
    "Austin, TX"
  ],
  "maxResults": 3,
  "includeDetails": true,
  "includeReviews": true,
  "maxReviewsPerBusiness": 3,
  "includePhotos": true,
  "maxPhotosPerBusiness": 3,
  "sortBy": "relevance"
}
```

This small example searches plumbers in Austin and asks for up to three unique businesses. More matches may exist. See all nine fields and defaults in the [input reference](docs/input-reference.md).

## Request examples

- [cURL start request](examples/curl-request.md): one request and instructions for checking the existing run.
- [Python search](examples/python/yellowpages_businesses.py): waiting, summary validation and paginated Dataset retrieval.
- [JavaScript search](examples/javascript/request.mjs): Node.js 20+ with built-in fetch; run `node examples/javascript/request.mjs` from the repository root.

All examples call the hosted service with your Apify token. Never commit that token. A run can incur charges; default examples set a 180-second Actor timeout and a $0.05 maximum event charge.

## Output fields

| Field | Purpose |
| --- | --- |
| `ypid`, `name` | Business identity; deduplicate merged results by ypid |
| `phone`, `website`, `emails` | Published contact fields, when available |
| `street`, `city`, `state`, `zip` | Source address fields |
| `rating`, `reviewCount` | Listing rating and count |
| `reviews`, `reviewTotal` | Nested reviews and reported total, which can be unknown |
| `photos` | Public photo URLs and metadata |
| `detailStatus`, `reviewsStatus`, `photosStatus` | Availability for each enrichment stage |

The [complete output reference](docs/output-reference.md) lists all 57 fields. JSON keeps nested values intact; the CSV export deliberately selects contact columns.

## Common use cases

Compare local categories, prepare business contact research, inspect published reviews, or process small city batches. See [workflow notes](docs/use-cases.md). Source counts are not a guarantee of complete market coverage.

## Search Yellow Pages businesses across US cities

```bash
python examples/python/batch_yellowpages_cities.py --locations "Austin, TX" "Dallas, TX"
```

This starts one run per city, sequentially. The $0.05 cap applies **to each run**, not to the entire batch. The script stops on an incomplete/failed run. Retain run IDs and deduplicate cross-run results yourself.

## Export Yellow Pages business contacts to CSV

```bash
python examples/python/export_yellowpages_csv.py DATASET_ID --output yellowpages-businesses.csv
```

Use the Dataset ID from an existing run. The export pages through the entire Dataset and creates no new collection. It writes UTF-8 and prefixes formula-like string cells with an apostrophe for spreadsheet safety. Nested reviews/photos remain available in the JSON Dataset.

## FAQ

Can I run without code? Yes. Are emails/reviews guaranteed? No. Does a client timeout mean no run was created? No: check existing runs first. See [all questions](docs/faq.md).

## Limits and pricing

US listings only. At most 25 terms, 25 locations and 100 combinations. maxResults accepts 1–20,000 unique businesses; this is an input ceiling, not a promise that the largest workload completes in one run. Review caps are 1–100 per business and photo caps 1–200. Defaults leave reviews/photos off. Check the summary for result-limit, source or availability restrictions.

The Actor uses pay-per-event: a unique delivered business and a unique review delivered within a business are separate events. At the FREE tier, a business costs **$0.001 ($1 per 1,000)** and a review costs **$0.0005 ($0.50 per 1,000)**. Customer-plan discounts apply; see the current [Actor Pricing tab](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata) before running. The repository does not choose a customer tier or promise a fixed number of free results.

## Hosted version

[Run Yellow Pages US on Apify](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata) for hosted execution, stored output, scheduling and API access. These examples integrate with that product; they do not replace it with a local scraper.

## Responsible use

Use public business data lawfully, respect applicable terms and privacy/outreach rules, and verify important details before contacting businesses. This project is independent of Yellow Pages and does not imply endorsement.

## Support

For example problems, [open a GitHub issue](https://github.com/datacrawler-edu/yellowpages-us-scraper-python/issues) with sanitized input and the command used. For collection problems, use the [Actor's Issues tab](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata) and include the run ID. Never post tokens or private data.

## License

These integration examples and documentation use the [MIT License](LICENSE). The hosted Actor's usage is subject to its Apify pricing and terms.
