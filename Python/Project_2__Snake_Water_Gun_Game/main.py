# ==========================================
# Snake Water Gun Game
#
# -1 for Snake
#  1 for Water
#  0 for Gun
# ==========================================

import random
# Computer's choice
computer = random.choice([-1, 1, 0])

# Take input from user
youstr = input("Enter your choice (s/w/g): ")

# Convert user input into numeric value
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    -1: "Snake",
    1: "Water",
    0: "Gun"
}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Check for draw
if (computer == you):
    print("It's a draw")

else:
    # Snake vs Water
    if (computer == -1 and you == 1):
        print("You win!")

    # Snake vs Gun
    elif (computer == -1 and you == 0):
        print("You Loss!")

    # Water vs Snake
    elif (computer == 1 and you == -1):
        print("You Loss!")

    # Water vs Gun
    elif (computer == 1 and you == 0):
        print("You win!")

    # Water vs Water
    elif (computer == 1 and you == 1):
        print("You win!")

    # Gun vs Snake
    elif (computer == 0 and you == -1):
        print("You win!")

    # Gun vs Water
    elif (computer == 0 and you == 1):
        print("You Loss!")

    # Unexpected case
    else:
        print("Something went wrong")