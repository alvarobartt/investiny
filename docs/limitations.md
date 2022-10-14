# 🛂 Limitations

After some extensive testing to explore further Investing.com's API limitations, we ran some tests to see whether Cloudflare was blocking incoming requests, and
it's not, so the API used by `investiny` seems stable enough for the moment (🤞🏻 fingers crossed!).

But besides that, there's a known limitation that we've spotted while retrieving historical data depending on the intervals used. All the limitations are now handled internally, so this is done transparently for the user, but whenever it comes to intra-day data, it seems that just a portion of it is available on Investing.com.

So here's the table with the intra-day data limitations:

| Interval | Limitation |
|:--:|--:|
| **1 min** | 6 months |
| **5 min** | ~ 1 year |
| **15 min** | ~ 1.5 years |
| **30 min** | ~ 2 years |
| **60 min (1 hour) ** | ~ 5 years |
| **300 min (5 hours) ** | ~ 13 years |

For the rest of the possible `interval` values for `investiny.historical_data` it doesn't seem to be any known limitation yet.
