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


menu = {
    '1. Registration of New Student'

    '2. Student Profile'

    '3. Delete Student'

    '4. List of all Student sorted as per standard'

    '5. List of Students of Particular Standard'

    '6. List of students with attendance greater than 50% standard wise'
}

def take_order():
    print("Welcome to Python Restaurant")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

    order_total = 0

    while True:
        item = input("Enter the name of the item you want to order (or type 'done' to finish) = ")
        
        if item.lower() == 'done':
            break
        
        if item in menu:
            order_total += menu[item]
            print(f"Your item {item} has been added to your order.")
        else:
            print(f"Order item {item} is not available yet!")

        another_order = input("Do you want to add another item? (Yes/No) ")
        if another_order.lower() != "yes":
            break

    print(f"The total amount to pay is Rs{order_total}")


take_order()