# AIM: Write a program to find n prime numbers

# Source Code:
n = int(input("Enter the range: "))
for i in range(2, n):
    isPrime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            isPrime = False
    if isPrime:
        print(i)

# Output:
# Enter the range: 20
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
