def countWordsAndLength(fileName):
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Number of Lines: {line_count}")
            print(f"Number of Words: {word_count}")

    except FileNotFoundError:
        print(f"file {fileName} is not found!")

countWordsAndLength("Week1 - Python Programming basics/Day6 - File Handling/sample.txt")