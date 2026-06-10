"""---------------------------------Student Portal.-----------------------------------

1. Registration of New Student

2. Student Profile

3. Delete Student

4. List of all Student sorted as per standard

5. List of Students of Particular Standard

6. List of students with attendance greater than 50% standard wise

------------------------------------------------------------------------------------------
Select any one operation : 1
------------------------------------------------------------------------------------------
----------------------------------Student Registration------------------------------------

Student id:___________________________________

Name:___________________________________

Standard:___________________________________

Roll No. :___________________________________

Attendance:___________________________________
--------------------------------------------------------------------------------------------
Student Registered successfully.
--------------------------------------------------------------------------------------------
Press 0 to exit any other number to continue: 2
--------------------------------------------------------------------------------------------

--------------------------------------Student Portal----------------------------------------

1. Registration of New Student

2. Student Profile

3. Delete Student

4. List of all Student sorted as per standard

5. List of Students of Particular Standard

6. List of students with attendance greater than 50% standard wise
------------------------------------------------------------------------------------------
Select any one operation: 2
------------------------------------------------------------------------------------------
"""

# List to store all student records
students = []  

# Function to register a new student
def register_student():
    print("\n------- Student Registration -------")
    student_id = input("Student id: ")           # Get student ID from user
    name = input("Name: ")                        # Get student name
    standard = input("Standard: ")                # Get student's class/standard
    roll_no = input("Roll No.: ")                 # Get roll number
    attendance = float(input("Attendance (%): ")) # Get attendance percentage

    # Store student details as a list and append to the students list
    student = [student_id, name, standard, roll_no, attendance]
    students.append(student)

    print("\nStudent Registered successfully.\n")

# Function to view a student's profile by ID
def student_profile():
    sid = input("\nEnter Student id to view profile: ")
    found = False
    for s in students:
        if s[0] == sid:  # Check if ID matches
            print("\n------- Student Profile -------")
            print(f"Student id : {s[0]}")
            print(f"Name       : {s[1]}")
            print(f"Standard   : {s[2]}")
            print(f"Roll No.   : {s[3]}")
            print(f"Attendance : {s[4]}%\n")
            found = True
            break
    if not found:
        print("No student found with that ID.\n")

# Function to delete a student by ID
def delete_student():
    sid = input("\nEnter Student id to delete: ")
    for s in students:
        if s[0] == sid:
            students.remove(s)  # Remove the student from the list
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

# Function to list all students sorted by their standard/class
def list_all_sorted_by_standard():
    if not students:
        print("\nNo students registered yet.\n")
        return

    # Sort the students list by standard (index 2)
    sorted_students = sorted(students, key=lambda x: x[2])

    print("\n------- All Students Sorted by Standard -------")
    for s in sorted_students:
        print(f"{s[2]} | ID:{s[0]} | Roll:{s[3]} | Name:{s[1]} | Attendance:{s[4]}%")
    print()

# Function to list students of a particular standard
def list_students_of_standard():
    std = input("\nEnter the standard to list: ")
    found = False
    print(f"\n------- Students of Standard {std} -------")
    for s in students:
        if s[2] == std:
            print(f"ID:{s[0]} | Roll:{s[3]} | Name:{s[1]} | Attendance:{s[4]}%")
            found = True
    if not found:
        print("No students found in that standard.\n")
    print()

# Function to list students with attendance greater than 50%, grouped by standard
def list_attendance_greater_than_50():
    if not students:
        print("\nNo students registered yet.\n")
        return

    print("\n------- Students with Attendance > 50% (Standard-wise) -------")
    # Get all unique standards
    standards = sorted(list(set([s[2] for s in students])))

    for std in standards:
        # Filter students of that standard with attendance > 50
        filtered = [s for s in students if s[2] == std and s[4] > 50]
        if filtered:
            print(f"\nStandard: {std}")
            for s in filtered:
                print(f"  ID:{s[0]} | Roll:{s[3]} | Name:{s[1]} | Attendance:{s[4]}%")
        else:
            print(f"\nStandard: {std} — No students with attendance > 50%")
    print()

# Function to display the menu options
def show_menu():
    print("------------------------------------------------------------")
    print("-------------------- Student Portal ------------------------")
    print("1. Registration of New Student")
    print("2. Student Profile")
    print("3. Delete Student")
    print("4. List of all Students sorted as per standard")
    print("5. List of Students of Particular Standard")
    print("6. List of students with attendance greater than 50% standard wise")
    print("0. Exit")
    print("------------------------------------------------------------")

# Main function to run the portal
def main():
    while True:
        show_menu()
        choice = input("Select any one operation: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            student_profile()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_all_sorted_by_standard()
        elif choice == "5":
            list_students_of_standard()
        elif choice == "6":
            list_attendance_greater_than_50()
        elif choice == "0":
            print("\nExiting Student Portal. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Entry point of the program
if __name__ == "__main__":
    main()
