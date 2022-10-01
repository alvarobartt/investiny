# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

from investiny import historical_data  # noqa: F401


@pytest.mark.usefixtures("investing_id", "from_date", "to_date")
def test_historical(investing_id: int, from_date: str, to_date: str) -> None:
    res = historical_data(
        investing_id=investing_id, from_date=from_date, to_date=to_date
    )
    assert all(key in res.keys() for key in ["open", "high", "low", "close"])
    assert isinstance(res, dict)
