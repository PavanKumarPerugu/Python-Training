import unittest
from src.operations.add import add

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 2), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -2), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-3, 2), -1)

if __name__ == '__main__':
    unittest.main()
