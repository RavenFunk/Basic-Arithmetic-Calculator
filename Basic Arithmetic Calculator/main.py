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

def calculator():
    print("- - - - - - - - - - - - - - - - - - - - - - -\nInput 'help' to get a list of useful commands.")
    result = 0
    calculations = 0
    while True:
        
        userInput = input("> ").strip()
        if not userInput:
            continue
        parts = userInput.split()
        command = (parts[0]).strip().lower()
        if command == 'new':
            calculations = 0 
            print()
            continue
        elif command == "help":
            print("- - - - - - - - - Help - - - - - - - - - \n\n [1] new : Begins a new input, type [See 3] to calculate something.\n [2] quit/exit : Closes the calculator.\n [3] x [operation] x : Valid for any basic arithmetic, returns the answer. \n [4] [operation] x : Allows you to further calculate on the previous output. \n [5] sqrt x : Returns the square root of x, begins a new calculation. \n")
            continue
        elif command in {"quit", "exit"}:
            print("Goodbye!")
            break
        elif command == "sqrt":
            number = float(parts[1])
            print(sqrt(number))
            print("Ran command: 'new'\n")
            calculations = 0
            continue
            
        if calculations == 0:
            try:
                first = float(parts[0])
                second = float(parts[2])
            except ValueError:
                print("Please enter a valid number\n")
                continue    

            first = float(parts[0])
            operator = parts[1]
            second = float(parts[2])
          
        elif calculations > 0:
            try:
                first = float(result)
                second = float(parts[1])
            except ValueError:
                print("Please enter a valid number\n")
                continue    
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
            if second == 0:
                print("ERROR: Unable to divide by 0, please try again.")
                calculations = 0
                continue
            result = divide(first, second)
            print(result)

calculator()
