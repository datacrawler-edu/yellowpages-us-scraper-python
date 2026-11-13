# Run without code

1. Open [Yellow Pages US on Apify](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata).
2. In Input, enter business types in searchTerms and US cities/states or ZIP codes in locations.
3. Begin with maxResults=3. Turn reviews/photos on only when needed; choose small per-business caps.
4. Click Start and wait for the run to finish.
5. Check Output/Dataset and RUN_SUMMARY. Export JSON for nested reviews/photos or CSV for spreadsheet work.

Each term/location combination is searched. A finished platform run can still have partial coverage: read the summary and row statuses. Never treat a missing website or email as proof that one does not exist.
