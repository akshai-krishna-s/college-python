# AIM: Write a program to implement insertion sort algorithm

# Source Code:
a = list(map(int, input("Enter a list of numbers: ").split()))

print("The list before sorting:", a)

for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print("The list after sorting:", a)

# Output:
# Enter a list of numbers: 5 6 3 9 4 5
# The list before sorting: [5, 6, 3, 9, 4, 5]
# The list after sorting: [3, 4, 5, 5, 6, 9]
