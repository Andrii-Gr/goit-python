def summ(a = 0, b = 0):
    return a + b

def substraction(a = 0, b = 0):
    return a - b

def multiplicationa(a = 0, b = 0):
    return a * b

def devision(a = 0, b = 1):
    return a / b

def calc(a=0, b=0, c=""):
    if c == "+":
        return summ(a=0, b=0)
    elif c  == "-":
        return substraction(a=0, b=0)
    elif c == "*":
        return multiplicationa(a=0, b=0, c!=0)
    elif c == "/"and num2 != 0:
        return devision(a=0, b=0)


print(calc(2, 3, "/"))