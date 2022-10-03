# 🤏🏻 `investpy` but made tiny

Suuuuuuuper simple and tiny `investpy` replacement while I try to fix it! Here I'll try
to add more or less the same functionality that was developed for `investpy` while keeping this
package tiny and up-to-date, as some solutions just work temporarily.

Everyone using `investiny` please go thank @ramakrishnamekala129 for proposing this solution
that seems to be stable and working fine so far (fingers crossed!). Also take the chance to explore
any other solution proposed by the `investpy` users at https://github.com/alvarobartt/investpy/issues.

I'm currently waiting to have a conversation with Investing.com so as to see whether we can get
to some sort of an agreement in order to keep `investpy` alive.

In the meantime you can follow me at https://twitter.com/alvarobartt as I post updates there, and
I highly appreciate your feedback.

@adelRosal, an `investpy` user created a change.org site so as to show some support, so please sign
the petition as it may be useful towards the continuity of `investpy` at https://www.change.org/p/support-from-investing-com-for-the-continuity-of-investpy-library

Finally, remember that `investiny` is super simple and tiny and shouldn't be considered reliable, it's
working fine so far, but it may be discontinued, so please use it carefully.

---

## 🛠️ Installation

🤏🏻 `investiny` requires Python 3.9+ and can be installed with `pip` as it follows:

`pip install investiny`

---

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

---

## 🔮 TODOs

- [ ] Add Search API as also available https://tvc4.investing.com/.../search?limit=30&query=USD&type=&exchange= (thanks again @ramakrishnamekala129) (also requested in [#4](https://github.com/alvarobartt/investiny/issues/4))
- [ ] Include date formatted as %m/%d/%Y in output JSON
- [ ] Add simple scraper for Investing.com IDs?
- [ ] Add error basic error handling
- [ ] Should `historical_data` work without `from_date` and `to_date` inheriting `recent_data` behavior?
- [ ] Even though it's working fine so far and it seems stable, should we run stress tests?
- [ ] Ideally we should keep the lenght of `investiny` code to less than 200 lines total?
- [ ] Add more issues so that community can contribute (also Hacktoberfest 2022 is starting?)
