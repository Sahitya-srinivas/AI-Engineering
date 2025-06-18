# check if a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("The number is zero")

# for loop in sequence
fruits = ['Apple','Banana','Cherry','Dragon Fruit']
for fruit in fruits:
    print(fruit)

# for loop in range
for i in range(1,11):
    print(i)

# while loop to print count from 5 to 0
num = 5
while num >= 0:
    print(num)
    num = num-1

# using break to exit the control flow
num = 1
while num < 10:
    if num == 7:
        break
    else:
        print(num)
        num+=1

# using continue to skip the control flow
for i in range(1,31):
    if i<=20:
        continue 
    else:
        print(i)