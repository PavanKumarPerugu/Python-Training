import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from calculator.tests_with_fixtures.conftest import get_test_data   # directly import fixture function
from src.operations.division import divide

class TestDivision(unittest.TestCase):
    def test_using_fixture_data(self):
        data = get_test_data()  # call it manually
        for a, b in data:
            if b == 0:
                with self.assertRaises(ValueError) as error:
                    divide(a, b)
                self.assertEqual(str(error.exception), "Cannot divide by zero")
            else:
                self.assertEqual(divide(a, b), a / b)
