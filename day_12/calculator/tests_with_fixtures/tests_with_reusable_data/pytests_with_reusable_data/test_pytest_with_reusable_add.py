import pytest
from src.operations.add import add

def test_add(sample_numbers):
    """Test addition using shared fixture data."""
    for a, b in sample_numbers:
        result = add(a, b)
        assert result == a + b