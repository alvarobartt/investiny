# 🤝🏻 Integrations

Here we'll explain how to integrate `investiny` with other packages/libraries.

## 🐼 Pandas

You'll need to install `pandas` as `pip install pandas`, and then in case you want to mimic
`investpy`'s output for historical data retrieval functions, you'll need to run the following
code:

```python
from investiny import historical_data
import pandas as pd

output = historical_data(investing_id=6408)
data = pd.DataFrame.from_dict(output)
data.rename(columns={
    "date": "Date",
    "open": "Open",
    "high": "High",
    "low": "Low",
    "close": "Close",
    "volume": "Volume"
}, inplace=True)
data.set_index("Date", inplace=True)
```

## ➕ More to come...

Feel free to submit a PR to update the documentation by adding more integrations with any
other package/library that you think can be useful to be documented.
