from unittest.mock import Mock

import pytest

@pytest.fixture
def mock_bun(name, price):
    mock_bun = Mock()
    mock_bun.name = name
    mock_bun.price = price
    return mock_bun

@pytest.fixture
def mock_ingredient(ingredient_type, name, price):
    mock_ingredient = Mock()
    mock_ingredient.type = ingredient_type
    mock_ingredient.name = name
    mock_ingredient.price = price
    return mock_ingredient