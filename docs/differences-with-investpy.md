# 🤔 What are the differences with `investpy`?

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
