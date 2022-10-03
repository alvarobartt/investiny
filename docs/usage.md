## 💻 Usage

Retrieve historical data from Investing.com using the Investing.com ID of the asset
that you want to retrieve the data from.

```python
from investiny import historical_data

data = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022") # Returns AAPL historical data as JSON (without date)
```

And, also retrive recent data (no need to specify dates, it's just the last 30 days) from
Investing.com using the Investing.com ID of the asset that you want to retrieve the data from.

```python
from investiny import recent_data

data = recent_data(investing_id=6408) # Returns AAPL recent data as JSON (without date)
```
