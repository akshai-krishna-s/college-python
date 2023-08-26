# AIM: Write a program to find the sum of digits of a given number

# Source Code:

num = int(input("Enter number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("The sum of digits is", sum)

# Output:
# Enter number: 123
# The sum of digits is 6
