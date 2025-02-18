def my_sum(a, b):
    return a + b

def test_my_sum():
    assert my_sum(1, 2) == 3
    assert my_sum(-1, 1) == 0
    assert my_sum(0, 0) == 0