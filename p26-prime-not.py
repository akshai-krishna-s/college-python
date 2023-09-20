# AIM: Write a program to check if the given number is prime or not

# Source Code:

num = int(input("Enter number: "))
for i in range(2, num):
    if num % i == 0:
        print("The number is not prime")
        break
else:
        print("The number is prime")

# Output:
# Enter number: 7
# The number is prime
