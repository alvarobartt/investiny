# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

from investiny import historical_data  # noqa: F401


@pytest.mark.usefixtures("investing_id", "from_date", "to_date")
def test_historical(investing_id: int, from_date: str, to_date: str) -> None:
    res = historical_data(
        investing_id=investing_id, from_date=from_date, to_date=to_date
    )
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )
    assert isinstance(res, dict)


@pytest.mark.usefixtures("investing_id")
def test_historical_without_dates(investing_id: int) -> None:
    res = historical_data(investing_id=investing_id)
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )
    assert isinstance(res, dict)


@pytest.mark.usefixtures("investing_id", "from_date_wide_range", "to_date_wide_range")
def test_historical_wide_range(
    investing_id: int, from_date_wide_range: str, to_date_wide_range: str
) -> None:
    res = historical_data(
        investing_id=investing_id,
        from_date=from_date_wide_range,
        to_date=to_date_wide_range,
    )
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )
    assert isinstance(res, dict)
