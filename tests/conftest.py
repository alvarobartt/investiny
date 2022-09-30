# Copyright 2022 Name Surname, username @ GitHub
# See LICENSE for details.

import pytest


@pytest.fixture
def hello_world() -> str:
    return "hello world!"
