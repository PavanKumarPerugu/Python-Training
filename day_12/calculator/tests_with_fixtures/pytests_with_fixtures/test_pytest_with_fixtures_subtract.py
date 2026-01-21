from src.operations.subtract import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(-5, 3) == -8
