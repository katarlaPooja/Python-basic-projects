print("Welcome to Pooja's Python Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+ - * /): ")

if operation == '+':
    result = a + b
    print(f"Result: {a} + {b} = {result}")

elif operation == '-':
    result = a - b
    print(f"Result: {a} - {b} = {result}")

elif operation == '*':
    result = a * b
    print(f"Result: {a} * {b} = {result}")

elif operation == '/':
    if b == 0:
        print("Error: Division by zero is not allowed")
    else:
        result = a / b
        print(f"Result: {a} / {b} = {result}")

else:
    print("Invalid operation. Please use +, -, *, or /")
print("Thank you for using the calculator!")
