# Build a calculator that:

# Asks the user to input two numbers.

# Asks the user to choose an operation (+, -, *, /).

# Performs the operation and shows the result.

# Handles errors like invalid input or division by zero gracefully.

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
def main():
    print("Welcome to the Simple Calculator!")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    
    try:
        result = calculate(num1, num2, operation)
        print(f"The result of {num1} {operation} {num2} is: {result}")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
