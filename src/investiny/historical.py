# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime
from typing import Any, Dict, Literal

from investiny.utils import request_to_investing

__all__ = ["historical_data"]


def historical_data(
    investing_id: int,
    from_date: str,
    to_date: str,
    interval: Literal["D", "W", "M"] = "D",
) -> Dict[str, Any]:
    """Get historical data from Investing.com.

    Args:
        investing_id (int): Investing.com's ID for the asset.
        from_date (str): Initial date to retrieve historical data (formatted as m/d/Y).
        to_date (str): Final date to retrieve historical data (formatted as m/d/Y).
        interval (Literal["D", "W", "M"], optional): Interval to retrieve historical data. Defaults to "D" which stands for Daily.

    Returns:
        Dict[str, Any]: A dictionary with the historical data.
    """
    params = {
        "symbol": investing_id,
        "from": int(datetime.strptime(from_date, "%m/%d/%Y").timestamp()),
        "to": int(datetime.strptime(to_date, "%m/%d/%Y").timestamp()),
        "resolution": interval,
    }
    data = request_to_investing(params=params)
    return {
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
    }
