# Opening files and reading files
with open("Week1 - Python Programming basics\Day6 - File Handling\sample2.txt", "r") as file:
    content = file.read()
    print(content)

# Writing content to files
with open("Week1 - Python Programming basics\Day6 - File Handling\sample2.txt", "w") as sample:
    updated_content = sample.write("Hi, This is AI Engineering.\n")   
    print(updated_content)

# Appending content to the files
with open("Week1 - Python Programming basics\Day6 - File Handling\sample2.txt", "a") as writeLast:
    append_content = writeLast.write("AI is the future.\n")   
    append_content = writeLast.write("And also, Python is fun.\n")   
    print(append_content)