# Personal Finance - Expense Tracker

expenses = []  # List of all expenses

print("Welcome to Expense Tracker")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    # Add Expense
    if choice == 1:
        date = input("Kis date par kharcha kiya tha? : ")
        category = input("Kis type ka kharcha kiya? : ")
        description = input("Aur detail do : ")
        amount = float(input("Enter the amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("\n✅ Expense added successfully!")

    # View All Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("❌ No expenses added. Jao pehle kharcha karo.")
        else:
            print("\n==== Aapke Sare Expenses ====")

            for i, expense in enumerate(expenses, start=1):
                print(f"\nExpense #{i}")
                print(f"Date       : {expense['date']}")
                print(f"Category   : {expense['category']}")
                print(f"Description: {expense['description']}")
                print(f"Amount     : ₹{expense['amount']}")

    # View Total Expense
    elif choice == 3:
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\n💰 Total Kharcha: ₹{total}")

    # Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid Choice! Please try again.")