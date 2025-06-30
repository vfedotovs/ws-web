import pandas as pd
from collections import Counter
import json

df = pd.read_csv(
    "docs/data/removed_ads_table_22_04_23.csv",
    parse_dates=["removed_date"],
    dayfirst=False,
)
df["year"] = pd.to_datetime(df["removed_date"], errors="coerce").dt.year
year_counts = df["year"].value_counts().sort_index()

output = [
    {"year": str(year), "count": int(count)} for year, count in year_counts.items()
]
with open("docs/data/apartment_removed_per_year.json", "w") as f:
    json.dump(output, f, indent=2)
