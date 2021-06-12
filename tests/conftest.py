import pytest


@pytest.fixture(scope="module")
def pagination_size():
    yield 30
