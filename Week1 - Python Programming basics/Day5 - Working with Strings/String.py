# # String Concatenation
# string_A = 'Hello'
# string_B = 'World'
# result = string_A + " " + string_B
# print(result)

# # Slicing of Strings
# text = 'I love Java Programming'
# print(text[:11])
# print(text[-11:])

# # Formatiing a String
# student = {'Name':'Shiva','Class':8}
# print(f"{student['Name']} is studying in {student['Class']}th standard")

# Split method in Strings
sentence = 'I love Python Programming'
words = sentence.split()
print(words)

# Join method in Strings
# join_var = " * ".join(words).upper()
# print(join_var)

# Replace method in Strings
replace_var = sentence.replace('Python','JAVA')
print(replace_var)

# Strip method in Strings
messy_text = "       Hello, World !    !   !           "
print(messy_text)
cleaned_text = messy_text.strip()
print(cleaned_text)