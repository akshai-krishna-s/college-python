# AIM: Write a program to find the fibonacci series upto a given limit

# Source Code:

limit = int(input("Enter limit: "))
a = 0
b = 1
print(a, b, end=" ")
while True:
    c = a + b
    if c > limit:
        break
    print(c, end=" ")
    a = b
    b = c

# Output:
# Enter limit: 100
# 0 1 1 2 3 5 8 13 21 34 55 89
