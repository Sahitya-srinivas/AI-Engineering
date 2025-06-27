# Creating a list and remove duplicates by using Set and reverse the list 
list_variable = [5,2,7,2,4,1,6,9,2,7,8,3]
set_variable = set(list_variable)
print(set_variable)
reverse = list(reversed(list(set_variable)))
print(reverse)

# Creating a list and remove duplicates without using set and reverse it
list_elements = [10,2,4,8,2,6,12,20,14,2,8,6,16]
unique_elements = []
for item in list_elements:
    if item not in unique_elements:
        unique_elements.append(item)
print(unique_elements)
print(list(reversed(unique_elements)))
