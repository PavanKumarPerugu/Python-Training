import pytest
import os
import sys

# Changing CWD
day13_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(day13_dir)
work_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(work_dir)
print("Current working directory:", os.getcwd())

from day_13.logs.calculator_.operations_.add_ import add

def test_add():
    assert add(3, 2) == 5
    assert add(-3, -2) == -5
    assert add(-3, 2) == -1

