# FAQ

## Is this the scraper source?
No. These examples call the [hosted Actor](https://apify.com/datascraperes/yellowpages-mobile-api-scraper?fpr=edudata); no scraper installation is required.

## Do I need to code?
No. Use Apify Input, Start and Dataset export. API examples are optional.

## Are all businesses guaranteed to have emails or reviews?
No. Only available published source fields can be returned.

## Is one run enough for every result in a city?
No guarantee. Your result cap, available source data and run limits determine coverage. Split large work into small, checked runs.

## Can I safely rerun after a timeout?
First inspect your existing Apify runs. A run may have been created even if your client lost the response. The examples do not automatically repeat run creation.

## Does export start another billed collection?
The CSV example reads an existing Dataset. It does not start an Actor run; platform storage/API usage can still apply.

## Can I download the photos?
The Actor returns public photo URLs; the examples do not download image files.
