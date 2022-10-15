# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest


@pytest.fixture
def investing_id() -> int:
    """Investing.com's ID for the asset (in this case, AAPL)."""
    return 6408


@pytest.fixture
def from_date() -> str:
    """Initial date to retrieve historical data (formatted as m/d/Y)."""
    return "01/04/2021"


@pytest.fixture
def to_date() -> str:
    """Final date to retrieve historical data (formatted as m/d/Y)."""
    return "12/31/2021"


@pytest.fixture
def from_date_wide_range() -> str:
    """Initial date to retrieve historical data (formatted as m/d/Y) but with a wider range.
    """
    return "01/03/2000"


@pytest.fixture
def to_date_wide_range() -> str:
    """Final date to retrieve historical data (formatted as m/d/Y) but with a wider range.
    """
    return "12/31/2021"


@pytest.fixture
def query() -> str:
    """Query to search assets in Investing.com."""
    return "GOOGL"
