def add(num1, num2):
    return num2 + num1
def sub(num1, num2):
    return num2 - num1
def mul(num1, num2):
    return num2 * num1
def div(num1, num2):
    try: 
        return num2 / num1
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    
def squared(num1, num2):
    return num2**num1

def calculate_postfix(formula, priority, add=add, sub=sub, mul=mul, div=div, squared=squared):
    stack = []
    for string in formula.split(" "):
        if string not in priority:
            stack.append(int(string))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if string == '+':
                stack.append(add(num1, num2))
            elif string == '-':
                stack.append(sub(num1, num2))
            elif string == '*':
                stack.append(mul(num1, num2))
            elif string == '/':
                stack.append(div(num1, num2))
            elif string == "**":
                stack.append(squared(num1,num2))
    return stack.pop() 

def calculate_now(formula, result, add=add, sub=sub, mul=mul, div=div, squared=squared):
    sign = ""
    num = ""
    for string in formula:
        if (sign is not "*") and (len(sign) >= 1) and (string.isdigit()==False):
            num += string
        elif string.isdigit():
            num += string
        else:
            sign += string
    num = int(num)
    if sign == '+':
        result = add(num, result)
    elif sign == '-':
        result = sub(num, result)
    elif sign == '*':
        result = mul(num, result)
    elif sign == '/':
        result = div(num, result)
    elif sign == "**":
        result = squared(num, result)
    return result
    

