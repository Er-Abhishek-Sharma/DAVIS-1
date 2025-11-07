# WAP to count a no of lines in the given file

# Specify the file name
filename = "sample.txt"

# Initialize line counter
line_count = 0

file = open(filename, 'r')
for line in file:
    line_count += 1
file.close()
print("Total number of lines:", line_count)