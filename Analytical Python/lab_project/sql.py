import sqlite3
import os


# -------------------- DATABASE SETUP --------------------
def create_table():
    print("Using DB at:", os.path.abspath("students.db"))  # Debug path

    conn = sqlite3.connect("student_portal.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# -------------------- INSERT STUDENT --------------------
def insert_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                (name, age, course))

    conn.commit()
    conn.close()
    print("✔ Student inserted successfully!\n")


# -------------------- UPDATE STUDENT --------------------
def update_student():
    student_id = input("Enter student ID to update: ")

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Course")
    choice = input("Enter choice: ")

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute("UPDATE students SET name=? WHERE id=?", (new_name, student_id))

    elif choice == "2":
        new_age = input("Enter new age: ")
        cur.execute("UPDATE students SET age=? WHERE id=?", (new_age, student_id))

    elif choice == "3":
        new_course = input("Enter new course: ")
        cur.execute("UPDATE students SET course=? WHERE id=?", (new_course, student_id))

    else:
        print("Invalid choice!")
        conn.close()
        return

    conn.commit()
    conn.close()
    print("✔ Student updated successfully!\n")


# -------------------- DELETE STUDENT --------------------
def delete_student():
    student_id = input("Enter student ID to delete: ")

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

    print("✔ Student deleted successfully!\n")


# -------------------- VIEW ALL STUDENTS --------------------
def view_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    print("\n------ Student Records ------")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")
    print()

    conn.close()


# -------------------- MENU SYSTEM --------------------
def menu():
    create_table()  # IMPORTANT: Ensures table exists before any CRUD

    while True:
        print("--------- Student CRUD Portal ---------")
        print("1. Insert Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run Program
menu()
