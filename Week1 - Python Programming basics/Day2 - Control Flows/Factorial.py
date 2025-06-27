# Factorial of a number using function
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)
    
number = int(input("Enter the number: "))
print(f"The factorial of {number} is {factorial(number)}")

#Factorial of a number using While loop
number = int(input("Enter a number: "))
result = 1
original_number = number
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    while number > 1:
        result = result * number
        number = number - 1
    if original_number == 0:
        print(f"The factorial of {original_number} is 1")
    else:
        print(f"The factorial of {original_number} is {result}")
    