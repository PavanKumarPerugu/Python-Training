import unittest
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

from src.operations.division import divide

class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    # def test_divide_by_zero1(self):
        # with self.assertRaises(ValueError):
           # divide(10, 0)

    def test_divide_by_zero2(self):
        with self.assertRaises(ValueError) as error:
            divide(10, 0)

        self.assertEqual(str(error.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
