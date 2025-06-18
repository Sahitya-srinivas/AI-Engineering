# Creating an Integers List
integer_list = [1,4,6,3,7]

# Creating a String List
string_list = ["Priya", 'Geeta', "Bhoomi", 'Rama']

# Creating List with different data types
all_list = [1, 'Priya', True, {"Role":"Engineer"}]
for item in all_list:
    print(item)

# Accessing List using index based
print(integer_list[3])

# Accessing List using negative indexing
print(string_list[-2])

# Adding elements in a List at last
string_list.append('Siri')
print(string_list)

# Adding an element at particular index
integer_list.insert(2,5)
print(integer_list)

# Removing an element based on it's value
string_list.remove("Bhoomi")
print(string_list)

# Removing an element based on it' index
del integer_list[4]
print(integer_list)

# Remove the last value from the list
integer_list.pop()
print(integer_list)

# Slicing the List elements
print(integer_list[0:3])

