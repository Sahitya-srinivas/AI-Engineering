def isPalindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input = input("Enter the input: ")
if isPalindrome(input):
    print(f"{input} is a Palindrome")
else:
    print(f"{input} is not a Palindrome")
