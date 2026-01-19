# test_add.py

import unittest
from add import add   # import the function to be tested

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)  # check if 2 + 3 == 5

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)  # check if -2 + -3 == -5

    def test_add_mixed_numbers(self):
        result = add(-2, 3)
        self.assertEqual(result, 1)  # check if -2 + 3 == 1\

    def test_add_positive_numbers1(self):
        result = add(2, 3)
        self.assertEqual(result, 6)  # check if 2 + 3 == 6


# This ensures the tests run when file is executed directly
if __name__ == '__main__':
    unittest.main()