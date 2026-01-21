from src.operations.multiply import multiply

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-3, -2) == 6
    assert multiply(-3, 2) == -6
