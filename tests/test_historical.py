# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

from investiny import historical_data  # noqa: F401


@pytest.mark.usefixtures("investing_id")
def test_historical(investing_id: int) -> None:
    res = historical_data(
        investing_id=investing_id, from_date="01/01/2021", to_date="01/01/2022"
    )
    assert all(key in res.keys() for key in ["open", "high", "low", "close"])
    assert isinstance(res, dict)
