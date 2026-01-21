import pytest
import os
import sys

# Changing CWD
print("Before: Current working directory:", os.getcwd())
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Current script directory:", script_dir)
up_dir = os.path.dirname(script_dir)
work_dir = os.path.dirname(up_dir)
print("One folder up to the current script directory:", work_dir)
sys.path.append(work_dir)
print("After: Current working directory:", os.getcwd())

from src.operations.subtract import subtract


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(-5, 3) == -8

