# AIM: Write a program to find the greatest of three numbers

# Source Code:
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    print(n1, "is the greatest")
elif n2 >= n1 and n2 >= n3:
    print(n2, "is the greatest")
elif n3 >= n1 and n3 >= n2:
    print(n3, "is the greatest")

# Output:
# Enter the first number: 5
# Enter the second number: 15
# Enter the third number: 3
# 15 is the greatest
