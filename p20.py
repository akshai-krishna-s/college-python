# AIM: Write a program to check whether a string is palindrome or not

# Source Code:
string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

# Output:
# Enter a string: madam
# The string is palindrome
# Enter a string: hello
# The string is not palindrome
