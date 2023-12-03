#calculator
from calculator_art import logo

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract, 
    "*": multiply,
    "/": divide,
}

# attempt 1
# if operation_symbol == "+":
#     result = add(num1, num2)
# elif operation_symbol == "-":
#     result = subtract(num1, num2)
# elif operation_symbol == "*":
#     result = multiply(num1, num2)
# else:
#     result = divide(num1, num2)

# solution with recursion. 
def calculator():
    print(logo)

    should_continue = True
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()