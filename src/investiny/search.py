# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from typing import Any, Dict, List, Literal, Union

from investiny.utils import request_to_investing

__all__ = ["search_assets"]


def search_assets(
    query: str,
    limit: int = 10,
    type: Union[
        Literal[
            "Stock",
            "ETF",
            "Commodity",
            "Index",
            "Future",
            "Yield",
            "FX",
        ],
        None,
    ] = None,
    exchange: Union[str, None] = None,
) -> List[Dict[str, Any]]:
    """Search any available asset at Investing.com.

    Args:
        query: Query to search for.
        limit: Maximum number of results to retrieve. Defaults to 10.
        type: Type of asset to search for. Defaults to None.
        exchange: Exchange to search for. Defaults to None.

    Returns:
        A list of dictionaries with the search results from Investing.com.
    """
    params = {
        "query": query,
        "limit": limit,
        "type": type if type else "",
        "exchange": exchange if exchange else "",
    }
    return request_to_investing(endpoint="search", params=params)  # type: ignore
