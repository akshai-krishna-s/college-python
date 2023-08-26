# AIM: Write a program to find the largest number in a list

# Source Code:
lst = list(map(int, input("Enter a list of numbers: ").split()))

# largest = lst[0]
# for i in lst:
#     if i > largest:
#         largest = i

largest = max(lst)

print("The largest number is", largest)

# Output:
# Enter a list of numbers: 1 2 3 4 5
# The largest number is 5
