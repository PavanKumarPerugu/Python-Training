import pytest
from src.operations.division import divide

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, -2) == 3
    assert divide(-6, 2) == -3
    with pytest.raises(ValueError) as error:
        divide(10, 0)
    assert str(error.value) == "Cannot divide by zero"
