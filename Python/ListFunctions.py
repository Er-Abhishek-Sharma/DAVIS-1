# # Create of list of 9 elements
# numbers=[40, 50, 90, 40, 60, 20, 40, 90, 10, 20]
# print("List is:", numbers)
# # Counting occurrence of 40
# x = numbers.count(40)
# for i in range(x):
#     numbers.remove(40)
# print("After removing the 40 from the list:", numbers)

"""Write a program to create a list of 20 numbers and ask user to enter any number and
remove its all the occurrence except first occurrence"""

# Create a list of 20 numbers
"""numbers=[40, 50, 90, 40, 60, 20, 40, 90, 10, 20, 10, 30, 40, 40, 40, 50, 20, 90, 30, 20]
print("List is:", numbers)
x = int(input("Enter a number to remove its duplicates: "))
freq = numbers.count(x)
numbers.reverse()
for index in range(freq-1):
    numbers.remove(x)
numbers.reverse()

print("After removing the duplicates except first occurrence:", numbers)
"""

#slice method
n=[40, 50, 60, 70, 80, 90, 100]
print("List is:", n)
m = n[1:5]
print("After removing the duplicates except first occurrence:", m)












