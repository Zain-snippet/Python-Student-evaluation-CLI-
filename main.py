from functools import reduce
import random

names = []
marks = []

# Take student names and assign random marks
def input_names(name_list, marks_list):
    print("Press Enter twice to stop entering names.\n")
    i = 1
    
    while True:
        name = input(f"Enter name of student {i}: ").title().strip()
        
        if not name: # Stop if empty
            print("\nNames entered successfully!\n")
            break
        elif name in name_list: # Avoid duplicates
            print("This name is already in the list.\n")
            continue
        else:
            name_list.append(name)
            marks_list.append(random.randint(0, 100)) # Random marks
            i += 1


# Zip names and marks
def zip_list(names, marks):
    return list(zip(names, marks))


# Assign grades based on marks
def grading(mark):
    if mark > 80:
        return "A"
    elif mark > 60:
        return "B"
    elif mark > 40:
        return "C"
    else:
        return "F"


# Apply grading to list
def graded(zipped_list):
    return [(name, mark, grading(mark)) for name, mark in zipped_list]


# Filter out A and B students
def filtered(graded_list):
    return list(filter(lambda x: x[2] in ("A", "B"), graded_list))


# Reduce: total marks of filtered students
def reduced(filtered_list):
    return reduce(lambda total, student: total + student[1], filtered_list, 0)


# Handle everything
def handle_functions():
    input_names(names, marks)

    zipped_list = zip_list(names, marks)
    graded_list = graded(zipped_list)
    filtered_list = filtered(graded_list)
    total_marks = reduced(filtered_list)

    print("\n--- Student Report ---\n")

    print("Zipped List (Name : Marks):")
    for i, (name, mark) in enumerate(zipped_list, start=1):
        print(f"{i}. {name} : {mark}")
    print()

    print("Graded List (Name : Marks -> Grade):")
    for i, (name, mark, grade) in enumerate(graded_list, start=1):
        print(f"{i}. {name} : {mark} -> {grade}")
    print()

    print("Filtered List (Grade A & B):")
    for i, (name, mark, grade) in enumerate(filtered_list, start=1):
        print(f"{i}. {name} : {mark} -> {grade}")
    print()

    print("--- Class Summary ---")
    if filtered_list:
        avg = total_marks / len(filtered_list)
        print(f"Total marks of A & B grade students: {total_marks}")
        print(f"Average marks (A & B students): {avg:.2f}")
    else:
        print("No students with grade A or B.")


handle_functions()