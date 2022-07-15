from cal_method import calculate_postfix, calculate_now
from postfit import postfix, transform_formula
from validation import validation_formula, validate_now


def calculator():
    result = 0

    def inner_func(formula, priority):
        nonlocal result

        try:
            val_formula = validation_formula(formula)
            if val_formula == "calculate_now":
                result = calculate_now(formula, result)
                return result
        except ValueError as e:
            return e

        if val_formula == "c":
            result = 0
            return result
        else:
            tr_formula = transform_formula(val_formula)
            new_formula = postfix(tr_formula, priority)
            try:
                result = calculate_postfix(new_formula, priority)
            except ZeroDivisionError as e:
                return e

        return result

    return inner_func

