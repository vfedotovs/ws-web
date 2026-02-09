## Summary KPIs

```vegalite
{
  "description": "Key metrics for removed listings",
  "data": {
    "url": "data/apartment_kpis.json"
  },
  "mark": {"type": "text"},
  "encoding": {
    "y": {"field": "label", "type": "ordinal", "axis": {"title": null}},
    "text": {"field": "value", "type": "nominal"}
  }
}
```

## Apartments listed and removed per year

```vegalite
{
  "description": "Count",
  "data": {
    "url": "data/apartment_removed_per_year.json"
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {
      "field": "year",
      "type": "ordinal",
      "axis": {"title": "Year"}
    },
    "y": {
      "field": "count",
      "type": "quantitative",
      "axis": {"title": "Apartments Listed and Removed"}
    }
  }
}
```

## Apartments removed per month

```vegalite
{
  "description": "Monthly count of removed listings",
  "data": {
    "url": "data/apartment_removed_per_month.json"
  },
  "mark": {"type": "line", "point": true, "tooltip": true},
  "encoding": {
    "x": {
      "field": "month",
      "type": "ordinal",
      "axis": {"title": "Month", "labelAngle": -45}
    },
    "y": {
      "field": "count",
      "type": "quantitative",
      "axis": {"title": "Removed Listings"}
    }
  }
}
```

## Days listed distribution

```vegalite
{
  "description": "Distribution of days listed (10-day bins)",
  "data": {
    "url": "data/apartment_days_listed_histogram.json"
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {
      "field": "bin_label",
      "type": "ordinal",
      "axis": {"title": "Days Listed (bin)", "labelAngle": -45}
    },
    "y": {
      "field": "count",
      "type": "quantitative",
      "axis": {"title": "Listings"}
    }
  }
}
```

## Median price per sqm by year

```vegalite
{
  "description": "Median sqm price by year",
  "data": {
    "url": "data/apartment_median_sqm_price_by_year.json"
  },
  "mark": {"type": "line", "point": true, "tooltip": true},
  "encoding": {
    "x": {
      "field": "year",
      "type": "ordinal",
      "axis": {"title": "Year"}
    },
    "y": {
      "field": "median_sqm_price",
      "type": "quantitative",
      "axis": {"title": "Median sqm price"}
    },
    "tooltip": [
      {"field": "year", "type": "ordinal"},
      {"field": "median_sqm_price", "type": "quantitative"},
      {"field": "sample_size", "type": "quantitative", "title": "Sample size"}
    ]
  }
}
```



