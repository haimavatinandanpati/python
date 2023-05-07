def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = float(input("Enter the first number: "))

print("Select an operation:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

choice = input("Enter your choice : ")

num2 = float(input("Enter the second number: "))

if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
    if num2 != 0:
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid input.")
