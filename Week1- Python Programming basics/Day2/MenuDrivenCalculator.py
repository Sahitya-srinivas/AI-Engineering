# create a menu driven calculator
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b != 0:
        return a/b
    else:
        print("Division by zero is not allowed")


while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice = int(input("Please enter your choice: "))
    if choice == 5:
        break
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == 1:
        print(f"The Addition of {num1} and {num2} is {add(num1,num2)}")
    elif choice == 2:
        print(f"The Subtraction of {num1} and {num2} is {sub(num1,num2)}")
    elif choice == 3:
        print(f"The Multiplication of {num1} and {num2} is {mul(num1,num2)}")
    elif choice == 4:
        print(f"The Division of {num1} and {num2} is {div(num1,num2)}")
    else:
        print("Please select the choice from 1 to 5")
        continue
