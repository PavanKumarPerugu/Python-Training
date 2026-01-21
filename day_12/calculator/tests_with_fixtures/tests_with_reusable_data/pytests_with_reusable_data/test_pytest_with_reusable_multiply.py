import pytest
from src.operations.multiply import multiply

def test_multiply(sample_numbers):
    """Test multiplication using shared fixture data."""
    for a, b in sample_numbers:
        result = multiply(a, b)
        assert result == a * b
