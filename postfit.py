
def postfix(formula, priority):
    new_formula = ""
    stack = []
    for string in formula.split():
        if string not in priority:
            new_formula += string + " "    
        elif string == "(":
            stack.append(string)
        elif string == ")":
            while stack and stack[-1] != "(":
                new_formula += stack.pop() + " "
            stack.pop()       
        else:
            while stack and priority[stack[-1]] >= priority[string]:
                new_formula += stack.pop() + " "
            stack.append(string)
    while stack:
        new_formula += stack.pop() + " "
    return new_formula.rstrip()

def transform_formula(formula):
    new_formula = ""
    minus_flag = 0
    if formula[0] == "-":
        new_formula += "-"
        formula = formula[1:]
        
    for index, string in enumerate(formula):
        if string.isdigit():
            if minus_flag == 1:
                minus_flag = 0
                new_formula = new_formula[:-3]
                new_formula += "-"
            new_formula += string
        else:
            try:
                if formula[index+1] == "-":
                    minus_flag = 1
            except:
                pass
            if string == "(":
                new_formula += f"{string} "
            elif string == ")":
                new_formula += f" {string}"
            elif string == "*":
                try:
                    if formula[index-1] == "*":
                        new_formula = new_formula[:-1]
                        new_formula += f"{string} "
                    else:
                        new_formula += f" {string} "
                except:
                    pass
            else:
                new_formula += f" {string} "
    return new_formula