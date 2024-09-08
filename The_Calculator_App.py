#Task 1: Create functions for eacch arithmetic operation
#Function for addition
def add(x, y):
    return x + y

#Function for subtraction
def subtract(x, y):
    return x - y

#Function for multiplication
def multiply(x, y):
    return x * y

#Function for division
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

#Task 2:Take user inputs for operation and numbers
#Function to get the user's operation choice
def get_operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Enter choice (1/2/3/4): ")

#Function to get numbers from the user
def get_numbers():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y
#Task 3: Error handling for division by zero and other potential errors
def calculator():
    while True:
        operation = get_operation()

        if operation not in ['1', '2', '3', '4']:
            print("Invalid input, please select a valid operation.")
            continue

        x, y = get_numbers()

        if operation == '1':
            print(f"Result: {add(x, y)}")
        elif operation == '2':
            print(f"Result: {subtract(x, y)}")
        elif operation == '3':
            print(f"Result: {multiply(x, y)}")
        elif operation == '4':
            result = divide(x, y)
            print(f"Result: {result}")

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break
