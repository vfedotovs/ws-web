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





