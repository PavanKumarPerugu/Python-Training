# pytests/conftest.py
import pytest
import os
import sys

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """
    Setup & Teardown fixture to configure environment paths once per session.
    This ensures that imports like 'from src.operations.add import add' work across all test files.
    """

    # ---------- SETUP ----------
    print("\n[SETUP] Configuring working directory and Python path...")

    script_dir = os.path.dirname(os.path.abspath(__file__))          # pytests folder
    project_root = os.path.dirname(script_dir)                       # one folder up → calculator
    src_path = os.path.join(project_root, "src")                     # calculator/src path

    if src_path not in sys.path:
        sys.path.append(src_path)

    print(f"Script dir: {script_dir}")
    print(f"Project root: {project_root}")
    print(f"Added to sys.path: {src_path}")

    yield  # ---------- test execution happens here ----------

    # ---------- TEARDOWN ----------
    print("\n[TEARDOWN] Test session completed. Cleaning up environment (if needed).")



# Optional reusable test data fixture
@pytest.fixture
def sample_numbers():
    """Reusable numeric pairs for arithmetic tests."""
    return [(3, 2), (-3, -2), (-3, 2), (5, 0)]

def get_test_data():
    """Reusable numeric pairs for arithmetic tests."""
    return [(3, 2), (-3, -2), (-3, 2), (5, 0)]