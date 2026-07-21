import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b):
    if b == 0:
        return print("ERROR: Unable to divide by 0, please try again.")
    elif b != 0: return a / b
def sqrt(a):
    return math.sqrt(a)


def calculator():
    result = 0
    calculations = 0
    while True:
        userInput = input("> ").strip()
        if not userInput:
            continue
        parts = userInput.split()

        if parts[0] == 'new':
            calculations = 0
            continue
        if calculations == 0:

            first = float(parts[0])
            operator = parts[1]
            second = float(parts[2])
        
            
        elif calculations > 0:
            first = result
            operator = parts[0]
            second = float(parts[1])

        calculations = calculations + 1
        if operator == "+":
            result = add(first, second)
            print(result)

        elif operator == "-":
            result = subtract(first, second)
            print(result)

        elif operator == "*":
            result = multiply(first, second)
            print(result)

        elif operator == "/":
            result = divide(first, second)
            print(result)



    


    

    

    



calculator()
