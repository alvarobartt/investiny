# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, timezone
from typing import Any, Dict, Literal, Union

from investiny.utils import calculate_date_intervals, request_to_investing

__all__ = ["historical_data"]


def historical_data(
    investing_id: int,
    from_date: Union[str, None] = None,
    to_date: Union[str, None] = None,
    interval: Literal[1, 5, 15, 30, 45, 60, 120, 240, 300, "D", "W", "M"] = "D",
) -> Dict[str, Any]:
    """Get historical data from Investing.com.

    Args:
        investing_id (int): Investing.com's ID for the asset.
        from_date (Union[str, None], optional): Initial date to retrieve historical data (formatted as m/d/Y). Defaults to None.
        to_date (Union[str, None], optional): Final date to retrieve historical data (formatted as m/d/Y). Defaults to None.
        interval (Literal[1, 5, 15, 30, 45, 60, 120, 240, 300, "D", "W", "M"], optional): Interval between each historical data point. Defaults to "D".

    Note:
        If no dates are introduced, the function will retrieve the last 30 days of historical data.

    Returns:
        Dict[str, Any]: A dictionary with the historical data.
    """
    from_datetimes, to_datetimes = calculate_date_intervals(
        from_date=from_date, to_date=to_date, interval=interval
    )

    result: Dict[str, Any] = {
        "date": [],
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
    }

    time_format = "%m/%d/%Y %H:%M" if interval not in ["D", "W", "M"] else "%m/%d/%Y"

    for to_datetime, from_datetime in zip(to_datetimes, from_datetimes):
        params = {
            "symbol": investing_id,
            "from": int(from_datetime.timestamp()),
            "to": int(to_datetime.timestamp()),
            "resolution": interval,
        }
        data = request_to_investing(endpoint="history", params=params)
        result["date"] += [datetime.fromtimestamp(t, tz=timezone.utc).strftime(time_format) for t in data["t"]]  # type: ignore
        result["open"] += data["o"]  # type: ignore
        result["high"] += data["h"]  # type: ignore
        result["low"] += data["l"]  # type: ignore
        result["close"] += data["c"]  # type: ignore
        if "v" in data:
            result["volume"] += data["v"]  # type: ignore
    if len(result["volume"]) < 1:
        result.pop("volume")
    return result
