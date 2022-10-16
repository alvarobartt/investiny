# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from typing import Any, Dict, List, Union

from investiny.utils import request_to_investing


def info(asset: Union[str, List[str]]) -> Dict[str, Any]:
    """Get assets' public information available at Investing.com

    Args:
        asset:
            name to retrieve its information from Investing.com. Note that this arg can be:
            the name of a single asset, a comma-separated string with asset names, or a list
            of asset names.

    Returns:
        A dictionary with the assets' public information available at Investing.com, where the
        key is the asset name and the value is a dictionary with the asset's information.
    """
    results = request_to_investing(
        endpoint="quotes",
        params={"symbols": asset if isinstance(asset, str) else ",".join(asset)},
    )
    if len(results["d"]) < 2:
        return {results["d"][0]["n"]: results["d"][0]["v"]}
    r = {}
    for result in results["d"]:
        r[result["n"]] = result["v"]
    return r


def investing_info(investing_id: int) -> Dict[str, Any]:
    """Get asset's information used internally by Investing.com.

    Args:
        investing_id: Investing.com's ID for the asset.

    Returns:
        A dictionary with the asset's information used internally by Investing.com.
    """
    return request_to_investing(
        endpoint="symbols",
        params={"symbol": investing_id},
    )
