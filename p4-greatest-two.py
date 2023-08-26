# AIM: Write a program to find the greatest of two numbers

# Source Code:
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if n1 > n2:
    print(n1, "is greater than", n2)
elif n2 > n1:
    print(n2, "is greater than", n1)
else:
    print("Both are equal")

# Output:
# Enter the first number: 5
# Enter the second number: 10
# 10 is greater than 5
