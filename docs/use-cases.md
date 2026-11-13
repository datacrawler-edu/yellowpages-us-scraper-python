# Business research workflows

## Compare local business categories
Search plumbers or dentists in a few cities, retain ypid for deduplication and review coverage before comparing counts. maxResults is a cap, not a census guarantee.

## Build a contact research spreadsheet
Use the export example on an existing Dataset. Phone, website and address depend on published listing data; confirm important details before contacting a business.

## Inspect published reviews and photos
Enable the corresponding options and small caps. Keep nested JSON for review text/dates and photo metadata. A rating count does not imply that every review is available.

## Run a city-by-city workflow
The batch example starts separate sequential runs, each with its own spending cap. Businesses shared between different runs may occur again; deduplicate merged outputs by ypid.
