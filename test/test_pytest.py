import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    # Division
    assert calculator.fun5(10, 2) == 5
    assert calculator.fun5(5, 2) == 2.5
    assert calculator.fun5(-10, 2) == -5
    assert calculator.fun5(0, 5) == 0


def test_fun5_divide_by_zero():
    # Division by zero should raise an exception
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(10, 0)


def test_fun6():
    # Power
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1
    assert calculator.fun6(-2, 2) == 4
    assert calculator.fun6(10, 2) == 100


def test_fun7():
    # Modulus
    assert calculator.fun7(10, 3) == 1
    assert calculator.fun7(8, 2) == 0
    assert calculator.fun7(5, 2) == 1
    assert calculator.fun7(15, 4) == 3


def test_fun7_zero():
    # Modulus by zero should raise an exception
    with pytest.raises(ZeroDivisionError):
        calculator.fun7(10, 0)


def test_fun8():
    # Average of three numbers
    assert calculator.fun8(10, 20, 30) == 20
    assert calculator.fun8(1, 2, 3) == 2
    assert calculator.fun8(-1, -2, -3) == -2
    assert calculator.fun8(0, 0, 0) == 0


def test_fun9():
    # Maximum of three numbers
    assert calculator.fun9(10, 20, 5) == 20
    assert calculator.fun9(-1, -2, -3) == -1
    assert calculator.fun9(5, 5, 5) == 5
    assert calculator.fun9(100, 0, 50) == 100


def test_fun10():
    # Minimum of three numbers
    assert calculator.fun10(10, 20, 5) == 5
    assert calculator.fun10(-1, -2, -3) == -3
    assert calculator.fun10(5, 5, 5) == 5
    assert calculator.fun10(100, 0, 50) == 0


def test_invalid_inputs():
    # Invalid input should raise ValueError
    with pytest.raises(ValueError):
        calculator.fun1("2", 3)

    with pytest.raises(ValueError):
        calculator.fun2(2, "3")

    with pytest.raises(ValueError):
        calculator.fun3("2", "3")

    with pytest.raises(ValueError):
        calculator.fun4(1, "2", 3)

    with pytest.raises(ValueError):
        calculator.fun5("10", 2)

    with pytest.raises(ValueError):
        calculator.fun6(2, "3")

    with pytest.raises(ValueError):
        calculator.fun7("10", 3)

    with pytest.raises(ValueError):
        calculator.fun8(1, "2", 3)

    with pytest.raises(ValueError):
        calculator.fun9(1, 2, "3")

    with pytest.raises(ValueError):
        calculator.fun10("1", 2, 3)