import io
from pathlib import Path
import logging
import sys
import builtins
import pytest
from unittest.mock import patch
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from day_13.logs.calculator_.main import calculator

def run_calculator_with_inputs(inputs, log_dir):
    """Run the calculator with fake inputs and a temporary log directory."""
    
    log_file = log_dir / "calculator.log"
    
    # Reconfigure logging to write to this test's log file
    logging.getLogger().handlers.clear()  # remove old handlers
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="a"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        try:
            calculator()
        except SystemExit:
            pass
        return mock_stdout.getvalue(), log_file

def test_addition_flow(tmp_path):
    inputs = ["1", "5", "3", "5"]  # Add 5 + 3, then Exit
    output, log_file = run_calculator_with_inputs(inputs, tmp_path)
    assert "Sum is 8.0" in output
    assert "Exiting the Calculator" in output
    assert "Performed addition" in log_file.read_text()

def test_subtraction_flow(tmp_path):
    inputs = ["2", "9", "4", "5"]  # Subtract 9 - 4, then Exit
    output, log_file = run_calculator_with_inputs(inputs, tmp_path)
    assert "Difference is 5.0" in output
    assert "Performed subtraction" in log_file.read_text()

def test_multiplication_flow(tmp_path):
    inputs = ["3", "4", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, tmp_path)
    assert "Product is 8.0" in output
    assert "Performed multiplication" in log_file.read_text()

def test_division_flow(tmp_path):
    inputs = ["4", "8", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, tmp_path)
    assert "Division is 4.0" in output
    assert "Performed division" in log_file.read_text()
