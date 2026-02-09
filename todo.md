# Plan for /data/aptartments-for-sale-data/ improvements

1. Switch data source to `removed_ads.csv` and regenerate `docs/data/apartment_removed_per_year.json`. (Implemented)
2. Add 2–3 new Vega-Lite charts (monthly removals trend, days listed histogram, price per sqm trend). (Implemented)
3. Add KPI summary block (total listings, median days listed, median price/sqm price, date range). (Implemented)
4. Add data quality note (e.g., `view_count` missing; currency unspecified).
5. Fix page naming typo and update `mkdocs.yml` (optional if you want to avoid URL changes).
