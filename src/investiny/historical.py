# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, timedelta
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
        from_datetime = datetime.strptime(from_date, "%m/%d/%Y")
        to_datetime = datetime.strptime(to_date, "%m/%d/%Y")
    else:
        to_datetime = datetime.now()
        from_datetime = to_datetime - timedelta(days=30)

    params = {
        "symbol": investing_id,
        "from": int(from_datetime.timestamp()),
        "to": int(to_datetime.timestamp()),
        "resolution": interval,
    }
    data = request_to_investing(endpoint="history", params=params)
    time_format = "%H:%M %m/%d/%Y" if isinstance(interval, int) else "%m/%d/%Y"
    return {
        "date": [datetime.fromtimestamp(t).strftime(time_format) for t in data["t"]],  # type: ignore
        "open": data["o"],  # type: ignore
        "high": data["h"],  # type: ignore
        "low": data["l"],  # type: ignore
        "close": data["c"],  # type: ignore
    }
