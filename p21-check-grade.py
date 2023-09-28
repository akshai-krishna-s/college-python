# AIM: Write a program to check grade of a student

# Source Code:

marks = int(input("Enter marks: "))
if marks > 95:
    print("Grade A+")
elif marks > 90:
    print("Grade A")
elif marks > 85:
    print("Grade B+")
elif marks > 80:
    print("Grade B")
elif marks > 75:
    print("Grade C+")
elif marks > 70:
    print("Grade C")
elif marks > 65:
    print("Grade D+")
elif marks > 60:
    print("Grade D")

# Output:
# Enter marks: 95
# Grade A
# Enter marks: 80
# Grade C+
