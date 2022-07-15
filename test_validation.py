from validation import *
import pytest

formula = "3+2+4*5+3/1"
formula3 = "-12"
formula4 = ""
formula5 = "3+2+4*5+3/1+"


def test_validate_now():
    assert validate_now("+12") == True


def test_validate_now2():
    assert validate_now("12+12") == False


def test_validation_formula():
    assert validation_formula(formula) == formula


def test_validation_formula2():
    assert validation_formula("c") == "c"


def test_validation_formula3():
    assert validation_formula(formula3) == "calculate_now"


def test_validation_formula4():
    with pytest.raises(ValueError):
        assert validation_formula(formula4) == ValueError


def test_validation_formula5():
    with pytest.raises(ValueError):
        assert validation_formula(formula5) == ValueError

