#  To import mysql connector

import sqlite3

# To establish connnection with database

conn = sqlite3.connect("student_database.db")

cur = conn.cursor()
cur.execute("""Create table If not exists Students(  
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    course TEXT)""")

conn.commit()
conn.close()

print("Database setup complete.")

# -----------------Registration--------------------

import sqlite3

def register_student(name, email, password, course):
    conn = sqlite3.connect("student_portal.db")
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO students (name, email, password, course)
            VALUES (?, ?, ?, ?)
        """, (name, email, password, course))

        conn.commit()
        print("Student registered successfully!")

    except sqlite3.IntegrityError:
        print("Error: email already exists")

    conn.close()


# ------------------- Login --------------------


def login(email, password):
    conn = sqlite3.connect("student_portal.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM students WHERE email=? AND password=?
    """, (email, password))

    student = cur.fetchone()
    conn.close()

    if student:
        print("Login successful!")
        return student
    else:
        print("Invalid email or password")
        return None
    
# ------------------- Views all Student --------------------

def list_students():
    conn = sqlite3.connect()
