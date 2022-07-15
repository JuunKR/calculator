def validate_now(formula):
    temp_formula = ""
    for string in formula:
        if string.isdigit():
            temp_formula += string
        else:
            temp_formula += " "
    num_count = len(temp_formula.strip().split(" "))
    if num_count >= 2:
        return False
    else:
        return True


def validation_formula(formula):
    sign_list = ["*", "-", "+", "/"]
    if formula == "":
        raise ValueError("input None")

    if formula.lower() == "c":
        return "c"
    if formula[-1] in sign_list:
        raise ValueError("input wrong formula")

    if formula[0] in sign_list:
        if validate_now(formula):
            return "calculate_now"
        pass
    formula = formula.strip()
    return formula
