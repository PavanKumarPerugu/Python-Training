from src.operations.add import add

def test_add():
    assert add(3, 2) == 5
    assert add(-3, -2) == -5
    assert add(-3, 2) == -1
