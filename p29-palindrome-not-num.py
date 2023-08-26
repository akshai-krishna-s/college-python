# AIM: Write a program to check whether the given number is palindrome or not

# Source Code:

num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")


# Output:
# Enter number: 121
# The number is palindrome
# Enter number: 123
# The number is not palindrome
