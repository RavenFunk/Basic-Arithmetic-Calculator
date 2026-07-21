import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b):
    return a / b
def sqrt(a):
    return math.sqrt(a)
def power(a, b):
    return a**b
 
def calculator():
    print("- - - - - - - - - - - - - - - - - - - - - - -\nInput 'help' to get a list of useful commands.")
    result = 0
    calculations = 0
    while True:
        userInput = input("> ")
        if not userInput:
            continue
        parts = userInput.split()
        command = (parts[0]).strip().lower()
        if command == 'new':
            calculations = 0 
            result = 0
            print()
            continue
        elif command == "help":
            print("- - - - - - - - - HELP - - - - - - - - - \n\n - - - - - Commands - - - - - \n [1] new : Begins a new input, type [See 3] to calculate something.\n [2] quit/exit : Closes the calculator.\n\n - - - - - Operations - - - - -\n\n [3] x + y : Adds y to x. \n [4] x - y : Subtracts y from x. \n [5] x * y : Multiplies x by y. \n [6] x / y : Divides x by y. \n [7] x ^ y OR x ** y : Raises x to the power of y. \n [8] sqrt x : Returns the square root of x. Starts a new calculation. \n\n - - - - - General - - - - -\n [9] x [operation] y : Valid for any basic arithmetic, returns the answer. \n [10] [operation] x : Allows you to further calculate on the previous output. \n\n ")
            continue
        elif command in {"quit", "exit"}:
            print("Goodbye!")
            break
        elif command == "sqrt":
            if len(parts) == 2:
                try:
                    number = float(parts[1])
                except ValueError:
                    print("Please enter a valid number\n")
                    continue
                
                if number >= 0:
                    
                    print(sqrt(number))
                    print("\nRan command: 'new'")
                    calculations = 0
                    result = 0
                    continue
                else:
                    print("Please enter a number greater than or equal to zero.")
                    continue
            else:
                print("Please enter a valid operation. Or enter 'help' to get a list of useful commands.\n")
                continue
        if calculations == 0:
            if len(parts) == 3:
                try:
                    first = float(parts[0])
                    operator = parts[1]
                    second = float(parts[2])
                except ValueError:
                    print("Please enter a valid number\n")
                    continue
            else:
                print("Please enter a valid operation. Or enter 'help' to get a list of useful commands.\n")    
                continue 
          
        elif calculations > 0:
            if len(parts) == 2:
                try:
                    first = float(result)
                    operator = parts[0]
                    second = float(parts[1])
                except ValueError:
                    print("Please enter a valid number\n")
                    continue
            else:
                print("Please enter a valid operation. Or enter 'help' to get a list of useful commands.\n") 
                continue   
            
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
            if second == 0:
                print("ERROR: Unable to divide by 0, please try again.\n")
                calculations = 0
                continue
            result = divide(first, second)
            print(result)
        elif operator in {"^", "**"}:
            result = power(first, second)
            print(result)
        else:
            print("Invalid operator, please try again. Or enter 'help' to get a list of useful commands.\n")
calculator()

