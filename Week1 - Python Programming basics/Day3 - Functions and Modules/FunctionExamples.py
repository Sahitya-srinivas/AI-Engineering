#Function with parameters and return value
def add_numbers(a, b):
    return a + b

result = add_numbers(3,5)
print(f"The sum is {result}")

# Local Scope variale
def greet():
    message = "Hello World"
    print(message)

greet()
'''print(message)  -- Local scope variable can't be accessed outside block'''

# Global Scope Variable
message = "Hi"

def greet():
    print(f"{message} from inside the function")

greet()
print(f"{message} from outside the function")
