# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

from investiny import recent_data  # noqa: F401


@pytest.mark.usefixtures("investing_id")
def test_recent(investing_id: int) -> None:
    res = recent_data(investing_id=investing_id)
    assert all(key in res.keys() for key in ["open", "high", "low", "close"])
    assert isinstance(res, dict)
