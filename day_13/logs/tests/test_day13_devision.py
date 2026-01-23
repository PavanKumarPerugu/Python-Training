import pytest
import os
import sys

# Changing CWD
day13_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(day13_dir)
work_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(work_dir)
print("Current working directory:", os.getcwd())

from day_13.logs.calculator_.operations_.division_ import divide

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, -2) == 3
    assert divide(-6, 2) == -3
    with pytest.raises(ValueError) as error:
        divide(10, 0)
    assert str(error.value) == "Cannot divide by zero"

