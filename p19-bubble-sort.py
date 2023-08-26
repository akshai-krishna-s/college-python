# Write a program to implement bubble sort algorithm

# Source Code:
a = list(map(int, input("Enter a list of numbers: ").split()))

print("The list before sorting:", a)

for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("The list after sorting:", a)

# Output:
# Enter a list of numbers: 5 6 3 9 4 2
# The list before sorting: [5, 6, 3, 9, 4, 2]
# The list after sorting: [2, 3, 4, 5, 6, 9]
