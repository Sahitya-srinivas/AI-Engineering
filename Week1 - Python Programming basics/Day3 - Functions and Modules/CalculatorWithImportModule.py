import mathoperations as mo

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The sum of {num1} and {num2} is : {mo.add(num1,num2)}")
print(f"The difference of {num1} and {num2} is : {mo.subtract(num1,num2)}")
print(f"The product of {num1} and {num2} is : {mo.multiply(num1,num2)}")
print(f"The quotient of {num1} and {num2} is : {mo.divide(num1,num2)}")
