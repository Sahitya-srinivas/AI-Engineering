# Take input from user
sentence = input("Enter the sentence: ")
# Split each word from the user input
words = sentence.split()
# Create an empty dictionary to collect the word frequency
word_count = {}
for word in words:
    # change the case to lower for case insensivity
    word = word.lower()
    # Check if the word is already there in the dictionary
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# print the dictionary
print(word_count)
