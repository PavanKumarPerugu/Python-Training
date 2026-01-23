import io
from pathlib import Path
import sys
import builtins
import pytest
from unittest.mock import patch
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from day_13.logs.calculator_.main import calculator

# --- Helper function to simulate input sequence ---
def run_calculator_with_inputs(inputs):
    """
    Simulate running the calculator by providing a list of inputs.
    Each input() call will take the next value from this list.
    """
    with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        try:
            calculator()
        except SystemExit:
            pass  # ignore exit() calls
        return mock_stdout.getvalue()

# --- Test 1: Valid Addition Flow ---
def test_addition_flow():
    inputs = ["1", "5", "3", "5"]  # Choose Add → 5 + 3 → Exit
    output = run_calculator_with_inputs(inputs)
    assert "Sum is 8.0" in output
    assert "Exiting the Calculator" in output

# --- Test 2: Invalid Menu Input ---
def test_invalid_menu_choice():
    inputs = ["abc", "5"]  # Invalid menu input → then exit
    output = run_calculator_with_inputs(inputs)
    assert "Please enter a valid integer choice." in output
    assert "Exiting the Calculator" in output

# --- Test 3: Division by Zero ---
def test_division_by_zero():
    inputs = ["4", "10", "0", "5"]  # Choose Divide → 10 / 0 → Exit
    output = run_calculator_with_inputs(inputs)
    assert "Error: Cannot divide by zero" in output
    assert "Exiting the Calculator" in output

# --- Test 4: Valid Multiplication ---
def test_multiplication_flow():
    inputs = ["3", "4", "2", "5"]  # Multiply 4 * 2 → Exit
    output = run_calculator_with_inputs(inputs)
    assert "Product is 8.0" in output
    assert "Exiting the Calculator" in output
