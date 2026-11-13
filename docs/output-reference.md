# Output reference

One business per Dataset row. Missing source values may be null or empty arrays; do not assume all businesses have emails, websites or reviews.

| Field | JSON type |
| --- | --- |
| `ypid` | "string" |
| `listingId` | ["string", "null"] |
| `name` | "string" |
| `phone` | ["string", "null"] |
| `phoneRaw` | ["string", "null"] |
| `emails` | "array" |
| `website` | ["string", "null"] |
| `yellowPagesUrl` | ["string", "null"] |
| `street` | ["string", "null"] |
| `city` | ["string", "null"] |
| `state` | ["string", "null"] |
| `zip` | ["string", "null"] |
| `country` | "string" |
| `latitude` | ["number", "null"] |
| `longitude` | ["number", "null"] |
| `distanceMiles` | ["number", "null"] |
| `primaryCategory` | ["string", "null"] |
| `categories` | "array" |
| `categoryBreadcrumbs` | "array" |
| `rating` | ["number", "null"] |
| `reviewCount` | ["integer", "null"] |
| `ratingAttributes` | "array" |
| `claimed` | ["boolean", "null"] |
| `openNow` | ["boolean", "null"] |
| `open24Hours` | ["boolean", "null"] |
| `coupon` | ["boolean", "null"] |
| `listingType` | ["string", "null"] |
| `yearEstablished` | ["string", "null"] |
| `yearsListed` | ["integer", "null"] |
| `description` | ["string", "null"] |
| `slogan` | ["string", "null"] |
| `paymentMethods` | "array" |
| `languages` | "array" |
| `accreditations` | "array" |
| `neighborhoods` | "array" |
| `brands` | "array" |
| `alsoKnownAs` | "array" |
| `socialLinks` | "array" |
| `services` | "array" |
| `products` | "array" |
| `about` | ["string", "null"] |
| `emergencyService` | ["string", "null"] |
| `hours` | ["object", "null"] |
| `hoursExtended` | ["object", "null"] |
| `photos` | "array" |
| `reviews` | "array" |
| `reviewTotal` | ["integer", "null"] |
| `searchTerm` | "string" |
| `searchLocation` | "string" |
| `searchPage` | "integer" |
| `searchRank` | "integer" |
| `source` | "string" |
| `appVersion` | "string" |
| `scrapedAt` | "string" |
| `detailStatus` | "string" |
| `reviewsStatus` | "string" |
| `photosStatus` | "string" |

`detailStatus`, `reviewsStatus` and `photosStatus` describe availability. `reviewCount` is the listing count; `reviewTotal` is the reviews endpoint total and can be null. The `reviews` array obeys your cap, so its length can be smaller.

Photos are URLs, not downloaded image files. Reviews/photos remain nested in JSON. The CSV example exports only the contact columns. Inspect the run's RUN_SUMMARY for complete/partial coverage before using results.
