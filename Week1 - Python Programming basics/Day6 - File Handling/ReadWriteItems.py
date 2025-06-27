def writeItemsToFile(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

def readItemsFromFile(filename):
    try:
        with open(filename, "r") as file:
            print("Items in the file:")
            items = file.readlines()
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} is not found!")

skills = ['Java', 'Python', 'Spring Boot', 'SQL', 'AI/ML', 'Data Science']
writeItemsToFile("Week1 - Python Programming basics\Day6 - File Handling\skills.txt",skills)
readItemsFromFile("Week1 - Python Programming basics\Day6 - File Handling\skills.txt")
