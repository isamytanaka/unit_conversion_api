## Unit Conversion API

A simple **API for** converting temperature and distance units.

## Endpoints:

`/convert/celsius-to-fahrenheit?value=30` → Converts Celsius to Fahrenheit.

`/convert/fahrenheit-to-celsius?value=86` → Converts Fahrenheit to Celsius.

`/convert/km-to-miles?value=5` → Converts kilometers to miles.

`/convert/miles-to-km?value=3.1` → Converts miles to kilometers.


## Response Example:

```
{

  "celsius": 30,
  "fahrenheit": 86.0
  
}
```

_**How to Use: Send a GET request with the value parameter.**_

