import pytest

from investiny.search import search_assets


@pytest.mark.usefixtures("query")
def test_search(query: str) -> None:
    res = search_assets(query=query, limit=10, type="Stock")
    assert isinstance(res, list)
    assert all(
        key in res[0].keys()
        for key in ["symbol", "full_name", "description", "type", "ticker", "exchange"]
    )
    assert isinstance(res[0], dict)
