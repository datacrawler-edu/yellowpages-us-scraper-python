# Input reference

Every term is searched in every location. At most 100 combinations per run. Unknown fields are rejected.

| Field | Type | Default | Meaning |
| --- | --- | --- | --- |
| `searchTerms` | array | `["plumbers"]` | What you would type into the Yellow Pages search box, one per line, for example plumbers or dentists. Every term is searched in every location. Up to 25 terms. |
| `locations` | array | `["Austin, TX"]` | US city and state, or a ZIP code, one per line, for example Austin, TX. Every business type is searched in every location. Up to 25 locations. |
| `maxResults` | integer | `100` | Total unique businesses to save across all searches. Default 100; maximum 20,000. The run stops when this limit is reached, even if Yellow Pages lists more matches. |
| `includeDetails` | boolean | `true` | Adds the business profile fields that are not on the search page: full address, hours, services, payment methods, languages, accreditations, and social links. Photos are added only when Include photos is enabled. Recommended. |
| `includeReviews` | boolean | `false` | Adds published review text, ratings, dates, authors, and business replies for each business. This adds one or more source requests per business. |
| `maxReviewsPerBusiness` | integer | `10` | Used only when Include reviews is on. Default 10; maximum 100. Reviews are collected in pages of 10. |
| `includePhotos` | boolean | `false` | Adds public photo URLs from the business gallery. Photo files are not downloaded; the URLs are included in each record. |
| `maxPhotosPerBusiness` | integer | `10` | Used only when Include photos is on. Default 10; maximum 200. Photos are requested in pages of up to 50. |
| `sortBy` | string | `"relevance"` | Order of businesses inside each search. Relevance is the source default. Sorting does not change the total number of matches. |
