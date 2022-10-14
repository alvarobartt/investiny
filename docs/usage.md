# 💻 Usage

Retrieve historical data from Investing.com using the Investing.com ID of the asset
that you want to retrieve the data from.

```python
from investiny import historical_data

data = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022") # Returns AAPL historical data as JSON (without date)
```

There's also a function to look for assets in Investing.com, that also lets you retrieve
the Investing.com ID that you can, later on, use in `historical_data` as an input parameter.

```python
from investiny import search_assets

results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ") # Returns a list with all the results found in Investing.com
```

As `search_assets` returns a list of results, you can check each of them, retrieve the `ticker` from the
asset that you want to retrieve historical data from and pass it as a parameter to `historical_data`. So on, the
combination of both functions should look like the following:

```python
from investiny import historical_data, search_assets

search_results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ")
investing_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)

data = historical_data(investing_id=investing_id, from_date="09/01/2022", to_date="10/01/2022")
```
