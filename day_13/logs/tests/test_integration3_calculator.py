import io
import sys
import logging
import pytest
from unittest.mock import patch
from pathlib import Path
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from day_13.logs.calculator_.main import calculator

from datetime import datetime

# ============================================================
# FIXTURE: Custom Log Directory (instead of tmp_path)
# ============================================================
@pytest.fixture
def custom_tmp_path():
    """
    Returns a dedicated directory (pytest_logs) for logs instead of OS temp.
    Keeps logs persistent for review after tests.
    """
    base_dir = Path(__file__).resolve().parent / "pytest_logs"
    base_dir.mkdir(parents=True, exist_ok=True)
    return base_dir


# ============================================================
# HELPER FUNCTION: Run calculator with fake inputs
# ============================================================
def run_calculator_with_inputs(inputs, log_dir, request = None):
    """
    Runs the calculator() function by mocking user inputs and capturing stdout.
    Also redirects log file output to a per-test log file.
    """
    test_name = request.node.name if request else "manual_run"
    test_file_name = f"{test_name}_{datetime.now():%Y%m%d_%H%M%S}"
    log_file = log_dir / f"{test_file_name}.log"

    # Reconfigure logging from scratch for each test
    logging.shutdown()
    logging.getLogger().handlers.clear()
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

    # Mock user inputs and capture printed output
    with patch("builtins.input", side_effect=inputs), \
         patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        try:
            calculator()
        except SystemExit:
            pass  # ignore exit() calls
        return mock_stdout.getvalue(), log_file


# ============================================================
# TESTS: ADDITION
# ============================================================
def test_addition_basic(custom_tmp_path, request):
    inputs = ["1", "5", "3", "5"]  # 5 + 3 → Exit
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Sum is 8.0" in output
    assert "Performed addition" in log_file.read_text()


def test_addition_negative_numbers(custom_tmp_path, request):
    inputs = ["1", "-5", "-3", "5"]  # -5 + -3 → Exit
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Sum is -8.0" in output
    assert "Performed addition" in log_file.read_text()


def test_addition_large_numbers(custom_tmp_path, request):
    inputs = ["1", "999999999", "1", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Sum is 1000000000.0" in output
    assert "Performed addition" in log_file.read_text()


# ============================================================
# TESTS: SUBTRACTION
# ============================================================
def test_subtraction_basic(custom_tmp_path, request):
    inputs = ["2", "9", "4", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Difference is 5.0" in output
    assert "Performed subtraction" in log_file.read_text()


def test_subtraction_negative_result(custom_tmp_path, request):
    inputs = ["2", "3", "10", "5"]  # 3 - 10 = -7
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Difference is -7.0" in output
    assert "Performed subtraction" in log_file.read_text()


# ============================================================
# TESTS: MULTIPLICATION
# ============================================================
def test_multiplication_basic(custom_tmp_path, request):
    inputs = ["3", "4", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Product is 8.0" in output
    assert "Performed multiplication" in log_file.read_text()


def test_multiplication_by_zero(custom_tmp_path, request):
    inputs = ["3", "5", "0", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Product is 0.0" in output
    assert "Performed multiplication" in log_file.read_text()


def test_multiplication_negative(custom_tmp_path, request):
    inputs = ["3", "-4", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Product is -8.0" in output
    assert "Performed multiplication" in log_file.read_text()


# ============================================================
# TESTS: DIVISION
# ============================================================
def test_division_basic(custom_tmp_path, request):
    inputs = ["4", "8", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Division is 4.0" in output
    assert "Performed division" in log_file.read_text()


def test_division_fractional_result(custom_tmp_path, request):
    inputs = ["4", "7", "2", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Division is 3.5" in output
    assert "Performed division" in log_file.read_text()


def test_division_by_zero(custom_tmp_path, request):
    inputs = ["4", "10", "0", "5"]
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Error" in output  # calculator should handle division by zero
    assert "Error" in log_file.read_text()


# ============================================================
# TESTS: INVALID INPUTS & MENU
# ============================================================
def test_invalid_menu_choice(custom_tmp_path, request):
    inputs = ["abc", "5"]  # invalid menu → exit
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Please enter a valid integer choice." in output
    assert "Invalid input" in log_file.read_text()


def test_invalid_numeric_input(custom_tmp_path, request):
    inputs = ["1", "abc", "3", "5", "2", "5"]
    # 1️⃣ invalid numeric input (abc)
    # 2️⃣ choose valid operation again (3 = multiply)
    # 3️⃣ first number 5
    # 4️⃣ second number 2
    # 5️⃣ exit
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Please enter valid numeric values." in output
    assert "Invalid numeric input" in log_file.read_text()



def test_invalid_operation_choice(custom_tmp_path, request):
    inputs = ["10", "5", "3", "5"]  # invalid menu choice
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Invalid choice!" in output
    assert "Invalid menu choice" in log_file.read_text()


# ============================================================
# TESTS: EXIT
# ============================================================
def test_exit_message(custom_tmp_path, request):
    inputs = ["5"]  # exit immediately
    output, log_file = run_calculator_with_inputs(inputs, custom_tmp_path, request)
    print("\nTest name:", request.node.name)
    print("Full node ID:", request.node.nodeid)
    print("File path:", request.node.fspath)
    assert "Exiting the Calculator" in output
    assert "Calculator exited by user" in log_file.read_text()
