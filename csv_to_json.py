import csv
import json
from datetime import datetime
from statistics import median

SOURCE_CSV = "removed_ads.csv"
DATE_FORMAT = "%Y.%m.%d"

OUTPUTS = {
    "per_year": "docs/data/apartment_removed_per_year.json",
    "per_month": "docs/data/apartment_removed_per_month.json",
    "days_hist": "docs/data/apartment_days_listed_histogram.json",
    "sqm_price_year": "docs/data/apartment_median_sqm_price_by_year.json",
    "kpis": "docs/data/apartment_kpis.json",
}

year_counts = {}
month_counts = {}
days_bins = {}
sqm_price_by_year = {}
prices = []
sqm_prices = []
days_listed_values = []
listed_dates = []
removed_dates = []

BIN_SIZE_DAYS = 10

def add_bin(days_value: int) -> None:
    bin_start = (days_value // BIN_SIZE_DAYS) * BIN_SIZE_DAYS
    bin_end = bin_start + BIN_SIZE_DAYS - 1
    label = f"{bin_start}-{bin_end}"
    days_bins[label] = days_bins.get(label, 0) + 1


with open(SOURCE_CSV, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        removed_date = row.get("removed_date")
        if removed_date:
            try:
                removed_dt = datetime.strptime(removed_date, DATE_FORMAT)
            except ValueError:
                removed_dt = None
            if removed_dt:
                removed_dates.append(removed_dt)
                year = removed_dt.year
                month_key = removed_dt.strftime("%Y-%m")
                year_counts[year] = year_counts.get(year, 0) + 1
                month_counts[month_key] = month_counts.get(month_key, 0) + 1

                sqm_price_raw = row.get("sqm_price")
                if sqm_price_raw:
                    try:
                        sqm_price = float(sqm_price_raw)
                    except ValueError:
                        sqm_price = None
                    if sqm_price is not None:
                        sqm_prices.append(sqm_price)
                        sqm_price_by_year.setdefault(year, []).append(sqm_price)

        listed_date = row.get("listed_date")
        if listed_date:
            try:
                listed_dt = datetime.strptime(listed_date, DATE_FORMAT)
            except ValueError:
                listed_dt = None
            if listed_dt:
                listed_dates.append(listed_dt)

        price_raw = row.get("price")
        if price_raw:
            try:
                price = float(price_raw)
            except ValueError:
                price = None
            if price is not None:
                prices.append(price)

        days_listed_raw = row.get("days_listed")
        if days_listed_raw:
            try:
                days_listed = int(float(days_listed_raw))
            except ValueError:
                days_listed = None
            if days_listed is not None and days_listed >= 0:
                days_listed_values.append(days_listed)
                add_bin(days_listed)


per_year = [
    {"year": str(year), "count": count}
    for year, count in sorted(year_counts.items())
]

per_month = [
    {"month": month, "count": count}
    for month, count in sorted(month_counts.items())
]

days_hist = [
    {"bin_label": label, "count": count}
    for label, count in sorted(
        days_bins.items(),
        key=lambda item: int(item[0].split("-")[0]),
    )
]

sqm_price_year = [
    {
        "year": str(year),
        "median_sqm_price": round(median(values), 2),
        "sample_size": len(values),
    }
    for year, values in sorted(sqm_price_by_year.items())
]

kpis = []

def add_kpi(label: str, value: str) -> None:
    kpis.append({"label": label, "value": value})

add_kpi("Total removed listings", str(sum(year_counts.values())))
if days_listed_values:
    add_kpi("Median days listed", f"{median(days_listed_values):.0f}")
if prices:
    add_kpi("Median price", f"{median(prices):.0f}")
if sqm_prices:
    add_kpi("Median sqm price", f"{median(sqm_prices):.2f}")
if listed_dates:
    add_kpi("Listed date range (min)", listed_dates and min(listed_dates).date().isoformat())
if removed_dates:
    add_kpi("Removed date range (max)", removed_dates and max(removed_dates).date().isoformat())

with open(OUTPUTS["per_year"], "w") as f:
    json.dump(per_year, f, indent=2)

with open(OUTPUTS["per_month"], "w") as f:
    json.dump(per_month, f, indent=2)

with open(OUTPUTS["days_hist"], "w") as f:
    json.dump(days_hist, f, indent=2)

with open(OUTPUTS["sqm_price_year"], "w") as f:
    json.dump(sqm_price_year, f, indent=2)

with open(OUTPUTS["kpis"], "w") as f:
    json.dump(kpis, f, indent=2)
