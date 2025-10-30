def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input, please enter a number.")

num1 = get_positive_float("enter first number")
num2 = get_positive_float("enter second number")
operation = input("enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero"
    else:
        result = num1 / num2