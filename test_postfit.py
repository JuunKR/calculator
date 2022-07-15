from postfit import *

priority = {
            "*":3, "**":3, "/":3, 
            "+":2, "-":2, 
            "(":1, ")":1
            }
formula = "3+2+4*5+3/1"

tr_formula = "3 + 2 + 4 * 5 + 3 / 1"
new_formula = "3 2 + 4 5 * + 3 1 / +"
def test_transform_formula():
    return transform_formula(formula) == tr_formula
def test_postfix():
    assert postfix(tr_formula, priority) == new_formula

