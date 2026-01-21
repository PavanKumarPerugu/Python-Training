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

from src.operations.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -2), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)

if __name__ == '__main__':
    unittest.main()
