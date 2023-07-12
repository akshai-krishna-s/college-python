# write a program to find gcd


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The GCD of", a, "and", b, "is", gcd(a, b))

# Output:
# Enter the first number: 12
# Enter the second number: 18
# The GCD of 12 and 18 is 6
