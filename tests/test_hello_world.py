# Copyright 2022 Name Surname, username @ GitHub
# See LICENSE for details.

import pytest


class TestHelloWorld:
    @pytest.fixture(autouse=True)
    @pytest.mark.usefixtures("hello_world")
    def setup_method(self, hello_world: str) -> None:
        self.hello_world = hello_world

    def teardown(self) -> None:
        del self.hello_world

    def test_hello_world(self) -> None:
        assert isinstance(self.hello_world, str)
        assert self.hello_world == "hello world!"
