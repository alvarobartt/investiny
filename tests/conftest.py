# Copyright 2022 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest


@pytest.fixture
def investing_id() -> int:
    """Investing.com's AAPL ID."""
    return 6408
