import unittest
from src.operations.division import divide

class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as error:
            divide(10, 0)
        self.assertEqual(str(error.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
