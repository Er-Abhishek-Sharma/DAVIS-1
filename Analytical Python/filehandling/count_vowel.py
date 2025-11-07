# Write a program in python to count no of vowels in the given file

# File name to read from
filename = "sample.txt"

# Vowels to check
vowels = "aeiouAEIOU"
count = 0
file = open('file1.txt', 'r')
for line in file:
    for char in line:
        if char in vowels:
            count += 1
file.close()
print("Total number of vowels:", count)