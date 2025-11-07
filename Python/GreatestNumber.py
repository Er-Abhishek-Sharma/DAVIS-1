first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))
if first_num == second_num == third_num:
    print("The numbers are equal")
elif first_num > second_num and first_num > third_num:
    print(first_num, "is greatest number")
elif second_num > first_num and second_num > third_num:
    print(second_num, "is greatest number")
else:
    print(third_num, "is greatest number")