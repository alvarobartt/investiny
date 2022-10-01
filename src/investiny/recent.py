# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, timedelta
from typing import Any, Dict, Literal

from investiny.utils import request_to_investing

__all__ = ["recent_data"]


def recent_data(
    investing_id: int, interval: Literal["D", "W", "M"] = "D"
) -> Dict[str, Any]:
    """Get recent (last 30 days) historical data from Investing.com.

    Args:
        investing_id (int): Investing.com's ID for the asset.
        interval (Literal["D", "W", "M"], optional): Interval to retrieve historical data. Defaults to "D" which stands for Daily.

    Returns:
        Dict[str, Any]: A dictionary with the recent historical data.
    """
    to_date = datetime.now()
    from_date = to_date - timedelta(days=30)
    params = {
        "symbol": investing_id,
        "from": int(from_date.timestamp()),
        "to": int(to_date.timestamp()),
        "resolution": interval,
    }
    data = request_to_investing(params=params)
    return {
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
    }
