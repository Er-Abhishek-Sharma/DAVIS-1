# WAP to count a no of characters in the given file

# Specify the file name
filename = "sample.txt"

# Open the file in read mode
file = open(filename, 'r')

# Initialize character counter
char_count = 0

# Read the file content
for line in file:
    for char in line:
        char_count += 1

# Close the file
file.close()

# Print the result
print("Total number of characters:", char_count)