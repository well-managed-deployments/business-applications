from wmd import controllers


def test_index_returns_paginated_applications():
    results = controllers.index()

    assert len(results) > 0
    assert len(results) < 30
