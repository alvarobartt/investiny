from typing import List

import pytest

from investiny import info


@pytest.mark.usefixtures("asset")
def test_info_with_asset(asset: str) -> None:
    res = info(asset=asset)
    assert isinstance(res, dict)
    assert asset in res.keys()


@pytest.mark.usefixtures("assets")
def test_info_with_assets(assets: str) -> None:
    res = info(asset=assets)
    assert isinstance(res, dict)
    assert all(key in res.keys() for key in assets.split(","))


@pytest.mark.usefixtures("asset_list")
def test_info_with_asset_list(asset_list: List[str]) -> None:
    res = info(asset=asset_list)
    assert isinstance(res, dict)
    assert all(key in res.keys() for key in asset_list)
