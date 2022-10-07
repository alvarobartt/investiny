# 🤏🏻 `investpy` but made tiny

Suuuuuuuper simple and tiny `investpy` replacement while I try to fix it! Here I'll try
to add more or less the same functionality that was developed for `investpy` while keeping this
package tiny and up-to-date, as some solutions just work temporarily.

Everyone using `investiny` please go thank @ramakrishnamekala129 for proposing this solution
that seems to be stable and working fine so far (fingers crossed!).

Remember that `investiny` shouldn't be considered reliable, as even though it's working fine, 
it may be discontinued, so please use it mindfully.

---

## 🤔 What are the differences with `investpy`?

**`investiny` is faster, lighter and easier to use**, but with reduced functionality for the moment. `investiny` 
lets you retrieve historical data from Investing.com through `historical_data` and search any available asset
through `search_assets`, while `investpy` offers more functions to also retrieve technical indicators, economic
calendars, dividends, etc. but those will come at some point to `investiny` too.

✨ `investiny` introduces intraday data, so the specified intervals when retrieving historical data for any asset
available at Investing.com goes from 1 minute to monthly data.

`investpy` uses Investing.com's APIs at https://www.investing.com/instruments/HistoricalDataAjax and at
https://api.investing.com/api/financialdata/historical, that are Cloudflare protected and not working any more,
as you'll end up getting blocked with 403 Forbidden HTTP code; while `investiny` is using https://tvc4.investing.com/,
which seems to be more reliable right now according to the ran tests, as well as providing intraday data.

---

## 🛠️ Installation

🤏🏻 `investiny` requires Python 3.8+ and can be installed with `pip` as it follows:

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
the Investing.com ID that you can later on use in `historical_data` as input parameter.

```python
from investiny import search_assets

results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ") # Returns a list with all the results found in Investing.com
```

As `search_assets` returns a list of results, you can check each of them, and retrieve the `ticker` from the
asset that you want to retrieve historical data from and pass it as parameter to `historical_data`. So on, the
combination of both functions should look like the following:

```python
from investiny import historical_data, search_assets

search_results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ")
investing_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)

data = historical_data(investing_id=investing_id, from_date="09/01/2022", to_date="10/01/2022")
```

## ⚠️ Disclaimer

Investing.com is a registered trademark from Investing.com, and their services offered by Fusion Media Limited.

Neither `investpy` nor `investiny` are affiliated, endorsed, or vetted by Investing.com.

Both `investpy` and `investiny` are open source packages that use Investing.com's available data, intended for research and educational purposes only.

You should refer to Investing.com's terms and conditions at https://www.investing.com/about-us/terms-and-conditions for details on your rights to use the actual data, as it is intended for personal use only.
