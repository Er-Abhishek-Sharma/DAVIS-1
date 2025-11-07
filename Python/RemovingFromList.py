# Create of list of 9 elements
numbers=[40, 50, 90, 40, 60, 20, 40, 90, 10, 20]
print("List is : ", numbers)
# Removing the 5th element
numbers.pop(4)
print("After removing the 5th number")
print("List is : ", numbers)
# Removing the first occurrence of 70 from list
numbers.remove(20)
print("After removing 70 from list")
print("List is : ", numbers)
# Removing elements from 3rd to 5th position from the list
del numbers[2:5:2]  #Start : Stop : Step
print("After removing elements from 3rd to 5th position from the list")
print("List is : ", numbers)