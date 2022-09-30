# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import json
from datetime import datetime
from typing import Any, Dict, Literal
from uuid import uuid4

import httpx

__all__ = ["historical_data"]


def request_to_investing(params: Dict[str, Any]) -> Dict[str, Any]:
    """Sends an HTTP GET request to Investing.com API with the introduced params.
    
    Args:
        params (Dict[str, Any]): A dictionary with the params to send to Investing.com API.

    Returns:
        Dict[str, Any]: A dictionary with the response from Investing.com API.
    """
    url = f"https://tvc4.investing.com/{uuid4().hex}/0/0/0/0/history"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like"
            " Gecko) Chrome/104.0.5112.102 Safari/537.36"
        ),
        "Referer": "https://tvc-invdn-com.investing.com/",
        "Content-Type": "application/json",
    }
    r = httpx.get(url, params=params, headers=headers)
    return json.loads(r.text)


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
