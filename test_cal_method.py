from cal_method import *
import pytest

priority = {"*": 3, "**": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
new_formula = "3 2 + 4 5 * + 3 1 / +"
new_formula2 = "12 0 /"


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(1, 2) == 1


def test_mul():
    assert mul(10, 5) == 50


def test_div():
    assert div(2, 10) == 5


def test_squared():
    assert squared(2, 5) == 25


def test_calculate_postfix():
    assert calculate_postfix(new_formula, priority) == 28.0


def test_calculate_postfix2():
    with pytest.raises(ZeroDivisionError):
        assert calculate_postfix(new_formula2, priority) == ZeroDivisionError


def test_calculate_now():
    assert calculate_now("+12", 15) == 27

