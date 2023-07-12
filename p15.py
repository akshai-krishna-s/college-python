# AIM: Write a program to collect and print employee's data

# Source Code:
e_no = int(input("Enter employee number: "))
e_name = input("Enter employee name: ")
e_salary = float(input("Enter employee salary: "))
e_address = input("Enter employee address: ")
married = input("Is employee married? (True/False): ")

if married == "True":
    married = True
elif married == "False":
    married = False

print("Employee number:", e_no)
print("Employee name:", e_name)
print("Employee salary:", e_salary)
print("Employee address:", e_address)
print("Is employee married?", married)

# Output:
# Enter employee number: 1
# Enter employee name: John
# Enter employee salary: 10000
# Enter employee address: 123, Street, City
# Is employee married? (True/False): True

# Employee number: 1
# Employee name: John
# Employee salary: 10000.0
# Employee address: 123, Street, City
# Is employee married? True
