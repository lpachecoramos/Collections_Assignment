def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# Input
student_name = input("Enter student name: ")

g1 = int(input("Enter grade 1: "))
g2 = int(input("Enter grade 2: "))
g3 = int(input("Enter grade 3: "))
g4 = int(input("Enter grade 4: "))
g5 = int(input("Enter grade 5: "))

# Calculate average
average = (g1 + g2 + g3 + g4 + g5) / 5

# Get letter grade
letter_grade = get_letter_grade(average)

# Output
print()
print(student_name)
print(f"Average: {average}")
print(f"Letter Grade: {letter_grade}")