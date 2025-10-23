def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error: Divisible by zero"
    return x / y
    
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

    
print("Select Operation:")    
print("+ Add")    
print("- Subtract")    
print("* Multiply")    
print("/ Division")

choice = input("Enter Choice (+, -, *, /):")

if choice == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '/':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
