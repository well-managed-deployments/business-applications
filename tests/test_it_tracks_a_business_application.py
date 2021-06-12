from wmd import controllers


def test_index_returns_paginated_applications(pagination_size):
    response = controllers.index_business_applications()

    results = response.payload.get("business_applications", {})

    assert 0 <= len(results) <= pagination_size
