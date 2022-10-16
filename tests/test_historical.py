import pytest

from investiny import historical_data


@pytest.mark.usefixtures("investing_id", "from_date", "to_date")
def test_historical(investing_id: int, from_date: str, to_date: str) -> None:
    res = historical_data(
        investing_id=investing_id, from_date=from_date, to_date=to_date
    )
    assert isinstance(res, dict)
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )
    assert res["date"][0] == from_date
    assert res["date"][-1] == to_date


@pytest.mark.usefixtures("investing_id")
def test_historical_without_dates(investing_id: int) -> None:
    res = historical_data(investing_id=investing_id)
    assert isinstance(res, dict)
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )


@pytest.mark.usefixtures("investing_id", "from_date_wide_range", "to_date_wide_range")
def test_historical_wide_range(
    investing_id: int, from_date_wide_range: str, to_date_wide_range: str
) -> None:
    res = historical_data(
        investing_id=investing_id,
        from_date=from_date_wide_range,
        to_date=to_date_wide_range,
    )
    assert isinstance(res, dict)
    assert all(
        key in res.keys() for key in ["date", "open", "high", "low", "close", "volume"]
    )
    assert res["date"][0] == from_date_wide_range
    assert res["date"][-1] == to_date_wide_range


@pytest.mark.usefixtures("investing_id_no_volume")
def test_historical_no_volume(investing_id_no_volume: int) -> None:
    res = historical_data(investing_id=investing_id_no_volume)
    assert isinstance(res, dict)
    assert "volume" not in res.keys()
