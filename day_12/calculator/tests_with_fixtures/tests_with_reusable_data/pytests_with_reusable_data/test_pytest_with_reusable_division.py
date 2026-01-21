import pytest
from src.operations.division import divide

def test_divide(sample_numbers):
    """Test division using shared fixture data."""
    for a, b in sample_numbers:
        if b == 0:
            # Expect a ValueError when dividing by zero
            with pytest.raises(ValueError) as error:
                divide(a, b)
            assert str(error.value) == "Cannot divide by zero"
        else:
            result = divide(a, b)
            assert result == a / b