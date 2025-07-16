# Write a program that:

# Takes a list of student grades (entered by the user).

# Calculates:

# The average grade.

# The highest and lowest grade.

# Shows all grades above the average.

def get_grades():
    raw_input = input("Enter student grades, separated by spaces: ")
    grades = list(map(int, raw_input.split()))
    return grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def display_above_average(grades, average):
    print("Students with above-average grades:")
    for i, grade in enumerate(grades):
        if grade > average:
            print(f"Student {i + 1}: {grade}")

grades = get_grades()
average = calculate_average(grades)

print(f"Average grade: {average:.2f}")
print("Max number of students:", max(grades))
print("Min number of students:", min(grades))

display_above_average(grades, average)
