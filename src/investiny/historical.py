# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Literal, Union

from investiny.utils import request_to_investing

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
    if from_date and to_date:
        from_datetimes = [
            datetime.strptime(from_date, "%m/%d/%Y").astimezone(tz=timezone.utc)
        ]
        to_datetimes = [
            datetime.strptime(to_date, "%m/%d/%Y").astimezone(tz=timezone.utc)
        ]
        if from_datetimes[0] > to_datetimes[0]:
            raise ValueError("`from_date` cannot be greater than `to_date`")
        if to_datetimes[0] - from_datetimes[0] > timedelta(
            days=6940
        ):  # round(365.25 * 19)
            max_to_datetime = to_datetimes[0]
            to_datetimes = [from_datetimes[0] + timedelta(days=6940)]
            while to_datetimes[-1] - from_datetimes[-1] > timedelta(
                days=6940
            ):  # round(365.25*19) = 6940
                from_datetimes.append(to_datetimes[-1] + timedelta(days=1))
                to_datetimes.append(from_datetimes[-1] + timedelta(days=6940))
            if to_datetimes[-1] != max_to_datetime:
                from_datetimes.append(to_datetimes[-1] + timedelta(days=1))
                to_datetimes.append(max_to_datetime)
    else:
        to_datetimes = [datetime.now(tz=timezone.utc)]
        from_datetimes = [to_datetimes[0] - timedelta(days=30)]

    result: Dict[str, Any] = {
        "date": [],
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
    }

    for to_datetime, from_datetime in zip(to_datetimes, from_datetimes):
        params = {
            "symbol": investing_id,
            "from": int(from_datetime.timestamp()),
            "to": int(to_datetime.timestamp()),
            "resolution": interval,
        }
        data = request_to_investing(endpoint="history", params=params)
        time_format = "%H:%M %m/%d/%Y" if isinstance(interval, int) else "%m/%d/%Y"
        result["date"] += [datetime.fromtimestamp(t).strftime(time_format) for t in data["t"]]  # type: ignore
        result["open"] += data["o"]  # type: ignore
        result["high"] += data["h"]  # type: ignore
        result["low"] += data["l"]  # type: ignore
        result["close"] += data["c"]  # type: ignore
        if "v" in data:
            result["volume"] += data["v"]  # type: ignore
    if len(result["volume"]) < 1:
        result.pop("volume")
    return result
