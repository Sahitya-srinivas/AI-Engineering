# Creating a dictionary data type
dict_variable = {"Name":"Priya", "Role":"Developer", "Project":"IVR"}
print(dict_variable)

# Adding and updating values in the dictionary
dict_variable["Experience"] = '4 Years'
dict_variable['Role'] = 'Senior Developer'
print(dict_variable)

# Iterating the values in dictionary
for key, value in dict_variable.items():
    print(key,value)

# Remving Data from the dictionary 
del dict_variable['Experience']
print(dict_variable)

# Removing the last element from the dictionary
dict_variable.pop('Role')
print(dict_variable)