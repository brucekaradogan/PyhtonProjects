def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    n1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operation_sign = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        answer = operations[operation_sign](n1, n2)
        print(f"{n1} {operation_sign} {n2} = {answer}")

        continue_with_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if continue_with_answer == 'y':
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
