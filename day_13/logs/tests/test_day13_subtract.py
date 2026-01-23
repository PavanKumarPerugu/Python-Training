import pytest
import os
import sys

# Changing CWD
day13_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(day13_dir)
work_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(work_dir)
print("Current working directory:", os.getcwd())

from day_13.logs.calculator_.operations_.subtract_ import subtract


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(-5, 3) == -8

