# AIM: Write a program to find gcd


# Source Code:
def gcd(a: int, b: int) -> int:
    if max([a, b]) % min([a, b]) == 0:
        return min([a, b])
    return gcd(min([a, b]), max([a, b]) % min([a, b]))


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The GCD of", a, "and", b, "is", gcd(a, b))

# Output:
# Enter the first number: 12
# Enter the second number: 18
# The GCD of 12 and 18 is 6
