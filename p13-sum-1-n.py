# AIM: Write a program to find the sum of 1 - n using while loop

# Source Code:
n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of 1 -", n, "is", sum)

# Output:
# Enter the value of n: 10
# The sum of 1 - 10 is 55
