import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to calculate exponentiation
def power(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Invalid input (negative number)"
    return math.sqrt(x)

# Function to calculate modulus (remainder)
def modulus(x, y):
    if y == 0:
        return "Cannot compute modulus with zero"
    return x % y

# Main program
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for exponentiation")
    print("Enter 'sqrt' for square root")
    print("Enter 'modulus' for modulus")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide", "power", "sqrt", "modulus"]:
        if user_input in ["add", "subtract", "multiply", "divide", "power", "modulus"]:
            num1 = float(input("Enter first number: "))
        
        if user_input not in ["sqrt"]:
            num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
        elif user_input == "power":
            print("Result: ", power(num1, num2))
        elif user_input == "sqrt":
            num = float(input("Enter a number: "))
            print("Result: ", square_root(num))
        elif user_input == "modulus":
            print("Result: ", modulus(num1, num2))
    else:
        print("Invalid input. Please try again.")
