from unittest.mock import Mock

import pytest

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    return mock_ingredient