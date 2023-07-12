# Write a program to calculate simple interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = (p * r * t) / 100
print("The simple interest is: ", si)

# Output:
# Enter the principal amount: 1000
# Enter the rate of interest: 5
# Enter the time in years: 2
# The simple interest is:  100.0
