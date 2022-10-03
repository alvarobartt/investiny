# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from typing import Any, Dict, List, Literal, Union
from uuid import uuid4

import httpx

__all__ = ["request_to_investing"]


def request_to_investing(
    endpoint: Literal["history", "search"], params: Dict[str, Any]
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """Sends an HTTP GET request to Investing.com API with the introduced params.

    Args:
        endpoint (Literal["history", "search"]): Endpoint to send the request to.
        params (Dict[str, Any]): A dictionary with the params to send to Investing.com API.

    Returns:
        Dict[str, Any]: A dictionary with the response from Investing.com API.
    """
    url = f"https://tvc4.investing.com/{uuid4().hex}/0/0/0/0/{endpoint}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like"
            " Gecko) Chrome/104.0.5112.102 Safari/537.36"
        ),
        "Referer": "https://tvc-invdn-com.investing.com/",
        "Content-Type": "application/json",
    }
    r = httpx.get(url, params=params, headers=headers)
    if r.status_code != 200:
        raise ConnectionError(
            f"Request to Investing.com API failed with error code: {r.status_code}."
        )
    return r.json()  # type: ignore
