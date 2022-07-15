from calculator import calculator
import os


if __name__ == "__main__":
    # formula = "-15*(-32--3)/-54-"
    # formula = "15*(32+3)/54"
    # "1+(1*3+1)+12*3"
    c = calculator()
    while 1:
        formula = input(
'''input "c" to reset
input your formula : '''
        )
        
        os.system('cls')
        priority = {
                    "*":3, "**":3, "/":3, 
                    "+":2, "-":2, 
                    "(":1, ")":1
                    }
        print(f"result :",  c(formula, priority))

                        
                        
