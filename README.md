# 🤏🏻 `investiny` is `investpy` but made tiny

**`investiny` is faster, lighter, and easier to use** than `investpy`.

`investiny` has been created due to the latest Investing.com changes in their API protection protocols, as 
now their main APIs are Cloudflare V2 protected. Anyway, there are still some APIs working fine, so this package
has been created as a temporary replacement for `investpy` while we get to an agreement to continue the development
of `investpy`. In the meantime, anyone can use `investiny` as I'm actively working on it, and ideally, it should support
most of the functionality provided by `investpy`.


---

## 🤔 What are the differences with `investpy`?

**`investiny` is faster, lighter and easier to use**, but with reduced functionality for the moment. `investiny` 
lets you retrieve historical data from Investing.com through `historical_data` and search any available asset
through `search_assets`, while `investpy` offers more functions to also retrieve technical indicators, economic
calendars, dividends, etc. but those will come at some point to `investiny` too.

`investiny` introduces intraday data, so the specified intervals when retrieving historical data for any asset
available at Investing.com goes from 1 minute to monthly data.

`investpy` uses Investing.com's APIs at https://www.investing.com/instruments/HistoricalDataAjax and at
https://api.investing.com/api/financialdata/historical, that are Cloudflare protected and not working any more,
as you'll end up getting blocked with 403 Forbidden HTTP code; while `investiny` is using https://tvc6.investing.com/,
which seems to be more reliable right now according to the ran tests, as well as providing intraday data.

| | Intraday Data | Any Range Historical Data | Search Assets/Quotes | Dividends | Economic Calendar | Technical Indicators | Economic News |
|:--:|--:|--:|--:|--:|--:|--:|--:|
| **investiny** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **investpy**  | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 🛠️ Installation

`investiny` requires Python 3.8+ and can be installed with `pip` as it follows:

`pip install investiny`

---

## 💻 Usage

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


## ⚠️ Disclaimer

Investing.com is a registered trademark of Investing.com, and its services are offered by Fusion Media Limited.

Neither `investpy` nor `investiny` is affiliated, endorsed, or vetted by Investing.com.

Both `investpy` and `investiny` are open-source packages that use Investing.com's available data, intended for research and educational purposes only.

You should refer to Investing.com's terms and conditions at https://www.investing.com/about-us/terms-and-conditions for details on your rights to use the actual data, as it is intended for personal use only.
