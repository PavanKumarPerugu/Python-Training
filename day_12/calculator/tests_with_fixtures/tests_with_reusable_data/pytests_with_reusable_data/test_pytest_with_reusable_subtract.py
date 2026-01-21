import pytest
from src.operations.subtract import subtract

def test_subtract(sample_numbers):
    """Test subtraction using shared fixture data."""
    for a, b in sample_numbers:
        result = subtract(a, b)
        assert result == a - b