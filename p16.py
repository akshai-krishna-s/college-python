# Write a python program to read and write a file

name1 = input("Enter the name of the file: ")

file1 = open(name1, "w")
str = input("Enter the text: ")
file1.write(str)
file1.close()

file2 = open(name1, "r")
print(file2.read())
file2.close()

# Output:
# Enter the name of the file: test.txt
# Enter the text: hello world
# hello world
