# AIM: Write a program to implement a calculator

# Source Code:
n1 = float(input("Enter the first number: "))
op = input("Enter the operator(+, -, *, /, %): ")
n2 = float(input("Enter the second number: "))
if op == "+":
    print("Result: ", n1 + n2)
elif op == "-":
    print("Result: ", n1 - n2)
elif op == "*":
    print("Result: ", n1 * n2)
elif op == "/":
    print("Result: ", n1 / n2)
elif op == "%":
    print("Result: ", n1 % n2)
else:
    print("Invalid operator")

# Output:
# Enter the first number: 5
# Enter the operator(+, -, *, /, %): *
# Enter the second number: 10
# Result:  50.0
