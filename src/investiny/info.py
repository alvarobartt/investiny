# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from typing import Any, Dict, List, Union

from investiny.utils import request_to_investing


def obtain_info(asset: Union[str, List[str]]) -> Dict[str, Any]:
    results = request_to_investing(
        endpoint="quotes",
        params={"symbols": asset if isinstance(asset, str) else ",".join(asset)},
    )
    if len(results["d"]) < 2:
        return {results["d"][0]["n"]: results["d"][0]["v"]}
    info = {}
    for result in results["d"]:
        info[result["n"]] = result["v"]
    return info
