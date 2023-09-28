# AIM: Write a program to store name and percentage marks of students in a dictionary and print them on screen 


# Source Code:
rec = {}
num = int(input("Enter number of students: "))
i = 1

while i <= num:
    name = input("Enter student name: ")
    marks = input("Enter % marks of student: ")
    rec[name] = marks
    i += 1


print("Name of the student", "\t", "% of marks obtained")

for x in rec:
    print("\t", x, "\t\t\t", rec[x])

# Output:
# Enter number of students: 3
# Enter student name: Ram
# Enter % marks of student: 75
# Enter student name: Shyam
# Enter % marks of student: 80
# Enter student name: Hari
# Enter % marks of student: 90
# Name of the student 	 % of marks obtained
# 	 Ram 			                  75
# 	 Shyam 			                80
# 	 Hari 			                90
