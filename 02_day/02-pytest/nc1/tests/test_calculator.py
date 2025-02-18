import pytest
from nc1.calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(3, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5
    assert subtract(3.5, 1.5) == 2.0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, -1) == 0.5
    assert power(2.5, 2) == 6.25 