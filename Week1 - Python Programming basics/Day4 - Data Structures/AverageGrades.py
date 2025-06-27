# Create a program that stores student grades in a dictionary and calculates the average grade
student_grades = {
    'Priya': 85,
    'Geeta': 90,
    'Siri': 78,
    'Rama': 92,
    'Shiva': 88
}
total = sum(student_grades.values())
count = len(student_grades)
average = total / count

print("Student Grades:", student_grades)
print("Average Grade:", average)