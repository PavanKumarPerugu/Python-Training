import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from calculator.tests_with_fixtures.conftest import get_test_data   # directly import fixture function
from src.operations.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_using_fixture_data(self):
        data = get_test_data()  # call it manually
        for a, b in data:
            self.assertEqual(multiply(a, b), a * b)
