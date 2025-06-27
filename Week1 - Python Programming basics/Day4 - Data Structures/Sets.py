# Creating an Integer Set
integer_set = {1,4,2,6,5,5}
print(integer_set)

# Creating a String Set
string_set = {'Priya', 'Geeta', 'Siri', 'Rama', 'Geeta'}
print(string_set)

# Creating an empty Set
empty_set = set()
print(empty_set)

# Adding elements in a set
string_set.add('Shiva')
print(string_set)

# Removibg elements from a set
integer_set.remove(5)
print(integer_set)

# Set operations
set_A = {2,10,4,8,6,0}  # Even numbers
set_B = {3,7,5,2}     # Prime numbers

# Union of 2 sets
print(set_A | set_B)

# Intersection of 2 sets
print(set_A & set_B)

# Difference of 2 sets
print(set_A - set_B)
print(set_B - set_A)