# Write a program to find the sum of elements of a list

n = int(input("Enter the number of elements: "))
list = []
for i in range(n):
    list.append(int(input("Enter element " + str(i + 1) + ": ")))
print("The sum of elements of the list is: ", sum(list))

# Output:
# Enter the number of elements: 5
# Enter element 1: 10
# Enter element 2: 20
# Enter element 3: 30
# Enter element 4: 40
# Enter element 5: 50
# The sum of elements of the list is:  150
