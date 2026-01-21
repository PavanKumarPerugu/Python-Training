import unittest
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
