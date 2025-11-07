# Write a program in python to copy data from one file to another file
with open('file1.txt', 'r') as source_file:
    data = source_file.read()

with open('file2.txt', 'w') as dest_file:
    dest_file.write(data)