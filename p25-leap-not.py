# AIM: Write a program to check if the given year is leap year or not

# Source Code:

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is leap year")
else:
    print("The year is not leap year")

# Output:
# Enter year: 2020
# The year is leap year
# Enter year: 2021
# The year is not leap year
