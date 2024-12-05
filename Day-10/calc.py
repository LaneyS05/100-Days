
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add, 
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    should_accumulate = True
    num1 = float(input("what is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        op_symbol = input("pick an operation: ")
        num2 = float(input("what is the next number?: "))
        print(f"{num1} {op_symbol} {num2} = {operations[op_symbol](num1, num2)}")

        choice = input(f"if you want to contineu with {operations[op_symbol](num1, num2)} type y if not type n to start new: ")

        if choice == "y":
            num1 = operations[op_symbol](num1, num2)

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()