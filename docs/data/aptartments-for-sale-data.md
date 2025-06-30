## This is sample bar chart 


```vegalite
{
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```


```vegalite
{
  "description": "Apartments listed and removed per year",
  "data": {
    "url": "docs/data/apartment_removed_per_year.json"
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





