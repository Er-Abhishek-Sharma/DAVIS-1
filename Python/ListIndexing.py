# num = [30, 40, 90, 70, 60, 20, 60]
# # Display list using forward
# for index in range(len(num)):
#     print(num[index], end=", ")

# Create a list of 10 numbers and display the elements starting from left to right using backward indexing
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for index in range(-len(l1), 0):
    print(l1[index], end=",")
print()
for index in range(len(l1) - 1, -1, -1):
    print(l1[index], end=",")

# Write a program to find out the average of a list of 10 numbers without using any library functions
total = 0
for num in l1:
    total += num
average = total / len(l1)
print("\nAverage of list numbers : ", average)

# --------------------------------------------------------------------------------
# Inserting elements in the list
# Create a program to find out average of numbers given by the user
# Creating a blank list
numbers=[]
total=0
print("Enter 10 numbers : ")
# Enter 10 numbers in the list
for x in range(10):
    num = int(input())
    # Calculating sum of the list
    total += num
    numbers.append(num)
print("Entered 10 numbers are : ", numbers)
# Finding the average of the list
average = total / len(numbers)
# Printing the average
print("Average of list numbers : ", average)

