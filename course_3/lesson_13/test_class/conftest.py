import pytest
from simple_dao import SimpleDAO


@pytest.fixture
def simple_dao():
    instance = SimpleDAO()
    return instance
